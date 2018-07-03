"""
python的字典。有如下的好处:

1. 统一初始化一些需要在多个用例之间共享的数据
2. 可以在初始化的时候做一些数据的处理工作，比如过滤一些无效数据等

Test fixture最简单的实现方式是通过自定义下面的2个方法:

TestCase.setUp方法在每个测试方法运行之前都会运行一次，适合为每个用例都初始化一遍数据
TestCase.tearDown方法在每个测试方法运行之后都会运行一次，适合为每个用例都清理一遍数据
"""
import unittest 

class PasswordTestCase(unittest.TestCase):
	def setUp(self):
		print('set up')
		self.test_data = [
			dict(name = 'jack', password = 'Iloverose'),
			dict(name = 'rose', password = 'Ilovejack'),
			dict(name = 'tom', password = 'password123')]

	def test_week_password(self):
		for data in self.test_data:
			passwd = data['password']

			self.assertTrue(len(passwd) >= 6)

			msg = "usee %s has a week password" %(data['name'])
			self.assertTrue(passwd != 'password', msg)
			self.assertTrue(passwd != 'password123', msg)

	def test_dummy(self):
		pass

if __name__ == '__main__':
	unittest.main()
