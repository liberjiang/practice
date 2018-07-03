import unittest 

class  TestStringMethods(unittest.TestCase):
	"""docstring for  TestStringMethods"""
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = "carelinker "
		self.assertEqual(s.split(), ['carelinker'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)


""" 
套路：测试方法中以test开头的方法才是测试方法；断言时测试的核心
使用assertEqual()来判断预期，用assertTrue()和asserFalse来做是非
判断，以及用assertEqual（）来判断预期的异常是否有被抛出，这些unittest
提供的以assert开都的方法就是断言，一般情况，每个测试用例都必须有断言

"""
'''
if __name__ =='__main__':
	unittest.main()
'''
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)


