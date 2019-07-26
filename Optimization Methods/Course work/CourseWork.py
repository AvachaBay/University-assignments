from scipy.optimize import linprog
from math import fabs
# from inspect import getfullargspec
#
n=4

def coefficients_into_an_equation(List):
	"""
	Превращение массива коэффициентов в полноценный 
	текстовый вид (уравнение)
	"""
	out=''

	#Вычисление индекса первого и последнего вхождения числа отличного от (!=)0
	last_index=len(List)
	first_index=-1

	for i in range(last_index):
		if not List[i]==0:
			if first_index==-1:
				first_index=i
			last_index=i

	# testing results of for cycle
	# print('first={0},last=={1}'.format(first_index,last_index))
	
	#Основной  цикл
	i=0
	for element in List:
		if element!=0:

			if not i==first_index and element>0:
				out+='+'

			if element==-1:
				out+='-'

			if fabs(element)!=1:
				out+=str(element)+'*'

			out+='x'+str(i)

		i+=1

	return out



	# #Вариант №2
	# out=''
	# for index,element in enumerate(List):
	# 	if element>0:
	# 		if element>1:
	# 			out+=str(element)+'*'
	# 		out+=str(element)
	# 		out+=str(index)


	# #вариант №3
	# n=len(List)
	# for i in range(n):
	# 	if List[i]>0:
	# 		if List[i]>1:
	# 			out+=str(List[i])+'*'
	# 		out+=List[i]


def str_inequality_system(A_ub, b_ub, A_eq, b_eq):
	"""
	Превращает входные массивы коэффициентов в полноценную систему ограничений
	состоящей из множества уравнений с помощью функции coefficients_into_an_equation
	"""
	inequality_system=[[A_ub,b_ub],[A_eq,b_eq]]

	# # Код для определения имен, передаваемых в функцию
	# full=getfullargspec(str_inequality_system)
	# names=full[0]
	# print(names)

	out=''
	i=0
	#Проход по видам ограничений : неравенства и уравнения
	for i in range(2):
		#Проход уравнениям определенного ограничения
		for k in range(len(inequality_system[i][0])):
			# out=''
			out+=coefficients_into_an_equation(inequality_system[i][0][k])

			if inequality_system[i][1]==A_ub:
				out+='=>'
			else:
				out+='='

				out+=str(inequality_system[i][1][k])+'\n'
			# print(out)

	return out


# Основной цикл работы программы
for i in range(n):
	print('{0:_^20}'.format(i))

	# Обнуление массивов
	c = []	
	A_ub = []
	b_ub = []
	A_eq = []
	b_eq = []

	# Массивы входных данных
	if i==0 :
		#	Коэффициенты в целевой функции
		c = [40, 30, 1.5*15, 160 , 150 , 4*35, 350, 240, 150]
		#	Коэффициенты ограничений
		A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1]]
		b_ub = [200, 180, 250]
		A_eq =[[20, 0, 0, 40, 0, 0, 50, 0, 0], [0, 10, 0, 0, 30, 0, 0, 40, 0],[0, 0, 15, 0, 0, 32, 0, 0 ,30]]
		b_eq= [6000, 5000, 5600]

	if i==1:
		c = [-20, -10, -15, -40, -30, -35, -50, -40, -30]	
		A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1]]
		b_ub = [200, 180, 250]

	if i==2:
		c = [0, 0, 0, 0, 0, 0, 0, 0, 0, -1]	
		A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],[20, 0, 0, 40, 0, 0, 50, 0, 0, -2/9]]
		b_ub = [200, 180, 250, 0]
		A_eq =[[0, 10, 0, 0, 30, 0, 0, 40, 0, -1/3],[0, 0, 15, 0, 0, 35, 0, 0 ,30, -4/9]]
		b_eq= [0, 0]

	if i==3:
		c = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
		A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1]]
		b_ub = [200, 180, 250]
		A_eq = [[20, 0, 0, 40, 0, 0, 50, 0, 0], [0, 10, 0, 0, 30, 0, 0, 40, 0],[0, 0, 15, 0, 0, 35, 0, 0 ,30]]
		b_eq = [6000, 5000, 5600]


	# Определение цели оптимизации (мин, макс)
	for c_elements in c:
		goal = 'min' if c_elements > 0 else 'max'

	# Вывод целевой функции
	out=coefficients_into_an_equation(c)
	print(out+' --> '+goal)

	# Вывод системы ограничений
	out=str_inequality_system(A_ub, b_ub, A_eq, b_eq)
	print(out)

