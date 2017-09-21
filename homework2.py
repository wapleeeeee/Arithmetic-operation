# -*- coding: gb2312 -*-

import sys
import random

from fractions import Fraction

class Equation():
	def __init__(self):
		self.op = ["+","-","*","÷","/"]
		self.priority = {'+':1,'-':1,'*':2,'÷':2}
		self.equ = self.getEquation()
		self.answer = self.getAnswer()

	#生成随机等式
	def getEquation(self):
		number = random.randint(2,9)
		tmpstring = ""
		tmpop = ''
		tmpint = 0
		for i in range(number):
			if tmpop == '/':            #分数情况
				tmpint = random.randint(tmpint+1,9)
				tmpop = random.choice(self.op[:-1])
			elif tmpop == '÷':          #除号情况
				tmpint = random.randint(1,8)
				tmpop = random.choice(self.op)
			else:
				tmpint = random.randint(0,8)
				tmpop = random.choice(self.op)
			#添加到算式中
			tmpstring += str(tmpint)
			tmpstring += tmpop
		tmpstring = list(tmpstring)
		#修改最后一个符号为=
		tmpstring[-1] = '='
		tmpstring = ''.join(tmpstring)
		return tmpstring

	#求算式答案
	def getAnswer(self):
		#将带有分号的表达式化成带分数的list
		equlist = []
		i = 0
		while(i < len(self.equ)-1):
			if self.equ[i+1] != '/':
				equlist.append(self.equ[i])
				i += 1
			else:
				equlist.append(Fraction(int(self.equ[i]),int(self.equ[i+2])))
				i += 3

		#将中缀表达式转化为后缀
		new_equlist = self.change_list(equlist)
		#计算后缀表达式的结果
		return(self.calculate(new_equlist))

	#转化为后缀表达式
	def change_list(self,equation):
		tmplist = []
		stack = []
		for op in equation:
			if type(op) == str and op >= '0' and op <= '9':
				tmplist.append(int(op))
			elif type(op) != str:
				tmplist.append(op)
			elif len(stack) == 0 or op == '(' or stack[-1] == '(':
				stack.append(op)
			elif op == ')':
				tmpTopStack = ''
				while tmpTopStack != '(':
					tmpTopStack = stack.pop()
					if tmpTopStack != '(':
						tmplist.append(tmpTopStack)
			else:
				while(len(stack) > 0 and self.priority[stack[-1]] >= self.priority[op]): #栈顶优先级大于等于该符号，持续出栈
					tmplist.append(stack.pop())
				stack.append(op)
		while(len(stack) != 0):
			tmplist.append(stack.pop())
		return tmplist 	


	#计算后缀表达式的结果
	def calculate(self,_list):
		tmpStack = []
		for tmpValue in _list:
			if type(tmpValue) != str:
				tmpStack.append(tmpValue)
			else:
				number_y = tmpStack.pop()
				number_x = tmpStack.pop()
				if tmpValue == "+":
					tmpStack.append(self.plus(number_x,number_y))
				elif tmpValue == "-":
					tmpStack.append(self.minus(number_x,number_y))
				elif tmpValue == "*":
					tmpStack.append(self.multiply(number_x,number_y))
				else:
					tmpStack.append(self.divide(number_x,number_y))
		return tmpStack[0]


	#四则运算
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2

	def multiply(self,num1,num2):
		return num1*num2

	def divide(self,num1,num2):
		return Fraction(num1,num2)


def main():
	if sys.argv[1] != "-n":
		raise IOError("Please enter the right command!")
	num = int(sys.argv[2])
	score = 0
	print("本次测试共{}题，满分100分".format(num))
	for i in range(1,num+1):
		equation = Equation()
		print("----------------------------")
		print("第{}题: {}".format(i,equation.equ),end = '')
		ans = input().strip()
		if ans == str(equation.answer):
			score += 1
			print("回答正确！：）")
		else:
			print("回答错误。：（ 正确答案：{}".format(equation.answer))
	print("----------------------------")
	print("测试结束，本次测试得分：{}分".format(round(float(score)/float(num)*100)))

if __name__ == '__main__':
	main()