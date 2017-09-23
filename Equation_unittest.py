import unittest
from unittest import TestCase
from homework2 import Equation
from fractions import Fraction

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

	#用了十组测试样例，基本可以涵盖需要考虑的情况，但无法保证代码覆盖率为100%
	def test_getAnswer(self):
		self.assertEqual(self.equation.getAnswer("(1+2)*3="),9)
		self.assertEqual(self.equation.getAnswer("(6+4/5)÷3="),Fraction(34,15))
		self.assertEqual(self.equation.getAnswer("(8/9-7-2+3)+3*4-2/9="),Fraction(20,3))
		self.assertEqual(self.equation.getAnswer("3*7-3-6+3="),15)
		self.assertEqual(self.equation.getAnswer("5+5/9+6-5÷(6/8+3/6)="),Fraction(68,9))
		self.assertEqual(self.equation.getAnswer("1-6="),-5)
		self.assertEqual(self.equation.getAnswer("3÷1+8÷5*4*5-2/9*2="),Fraction(311,9))
		self.assertEqual(self.equation.getAnswer("(5+(6-3)*3/5)÷7="),Fraction(34,35))
		self.assertEqual(self.equation.getAnswer("(1+2)*(3*(4+5))="),81)
		self.assertEqual(self.equation.getAnswer("4+6*0="),4)

#测试  
if __name__ == "__main__":  
    #构造测试集              
    suite = unittest.TestSuite()  
    #suite.addTest(EquationTestCase("test_getEquation"))  
    suite.addTest(EquationTestCase("test_getAnswer"))  
    #执行测试  
    runner = unittest.TextTestRunner()  
    runner.run(suite) 