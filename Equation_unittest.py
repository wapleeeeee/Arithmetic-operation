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
		for i in range(10000):         
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

	#同样是十组样例，测试是否为预期后缀表达式
	def test_change_list(self):
		self.assertEqual(self.equation.change_list(["1", "+", Fraction(2,3), "÷", "3"]),[1, Fraction(2,3), 3, "÷", "+"])
		self.assertEqual(self.equation.change_list(['4', '*', '0', '*', '5', '÷', '7', '-', '0', '÷', '3']),[4, 0, '*', 5, '*', 7, '÷', 0, 3, '÷', '-'])
		self.assertEqual(self.equation.change_list(['2', '-', '6', '+', '4', '+', Fraction(1, 4), '÷', '5', '-', '5']),[2, 6, '-', 4, '+', Fraction(1, 4), 5, '÷', '+', 5, '-'])
		self.assertEqual(self.equation.change_list(['6', '*', '7']),[6, 7, '*'])
		self.assertEqual(self.equation.change_list(['7', '*', '(', '0', '÷', '4', '-', '5', ')']),[7, 0, 4, '÷', 5, '-', '*'])
		self.assertEqual(self.equation.change_list(['0', '*', '7', '+', '(', '8', '+', '7', '*', '6', ')', '÷', '4', '*', '4', '-', '7', '-', '4']),[0, 7, '*', 8, 7, 6, '*', '+', 4, '÷', 4, '*', '+', 7, '-', 4, '-'])
		self.assertEqual(self.equation.change_list(['0', '+', '1', '*', '8', '÷', '8', '*', '7']),[0, 1, 8, '*', 8, '÷', 7, '*', '+'])
		self.assertEqual(self.equation.change_list([Fraction(3, 7), '÷', '3', '÷', Fraction(2, 3), '÷', '3']),[Fraction(3, 7), 3, '÷', Fraction(2, 3), '÷', 3, '÷'])
		self.assertEqual(self.equation.change_list([Fraction(6, 7), '+', '0', '*', '(', '6', '-', '(', '3', '-', Fraction(5, 8), ')', ')']),[Fraction(6, 7), 0, 6, 3, Fraction(5, 8), '-', '-', '*', '+'])
		self.assertEqual(self.equation.change_list(['(', '4', '+', '8', '-', '4', '-', '3', '+', '2', '*', '0', ')', '÷', '4']),[4, 8, '+', 4, '-', 3, '-', 2, 0, '*', '+', 4, '÷'])

	#由于后缀表达式得结果的情况并不多，所以采用五组样例测试
	def test_calculate(self):
		self.assertEqual(self.equation.calculate([6, Fraction(2, 5), '÷', 2, 3, '÷', '-', 1, 4, '*', '-']),Fraction(31,3))
		self.assertEqual(self.equation.calculate([0, 3, 7, '÷', 6, '÷', 0, '-', '÷', 7, '÷']),0)
		self.assertEqual(self.equation.calculate([Fraction(8, 9), Fraction(2, 3), '+', 5, 5, '÷', 5, 1, '-', '÷', 7, '*', '+']),Fraction(119,36))
		self.assertEqual(self.equation.calculate([4, 7, 1, '+', Fraction(8, 9), '+', '*', 5, 6, '÷', '-']),Fraction(625,18))
		self.assertEqual(self.equation.calculate([2, 1, '÷', 8, '÷', 8, '*', Fraction(1, 2), '÷', Fraction(5, 8), '÷']),Fraction(32,5))

#测试  
if __name__ == "__main__":  
    #构造测试集              
    suite = unittest.TestSuite()  
    suite.addTest(EquationTestCase("test_getEquation"))  
    suite.addTest(EquationTestCase("test_getAnswer"))
    suite.addTest(EquationTestCase("test_change_list"))
    suite.addTest(EquationTestCase("test_calculate"))
    #执行测试  
    runner = unittest.TextTestRunner()  
    runner.run(suite) 