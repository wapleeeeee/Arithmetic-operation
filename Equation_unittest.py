import unittest
from unittest import TestCase
from homework2 import Equation

class EquationTestCase(TestCase):
	#初始化对象
	def setUp(self):
		self.equation = Equation()

	#对象资源释放
	def tearDown(self):
		self.equation = None

	#对getEquation函数测试
	def test_getEquation(self):
		#随机1000000次
		for i in range(1000000):         
			tmpString = self.equation.getEquation()[:-1]   #保存生成的算式
			tmpString.replace('÷','/')                #将无法识别的除号替换
			self.assertEqual(type(tmpString),(str or int))


#测试  
if __name__ == "__main__":  
    #构造测试集              
    suite = unittest.TestSuite()  
    suite.addTest(EquationTestCase("test_getEquation"))  
    #suite.addTest(EquationTestCase("test_resize"))  
    #执行测试  
    runner = unittest.TextTestRunner()  
    runner.run(suite) 