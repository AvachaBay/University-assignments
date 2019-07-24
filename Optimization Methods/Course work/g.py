
from scipy.optimize import linprog

# Входные данные

#	Коэффициенты в целевой функции
c = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

print('Целевая функция:')
goalstring=''
for index,elements in enumerate(c):
	if elements<0:
		goal='max'
	else:
		goal='min'
	if elements!=0: 
		goalstring+='+x'+str(index)
		if elements>1:
			goalstring+='*'+str(-elements)
print(goalstring+'->'+goal)


#	Коэффициенты ограничений
A_ub = [[1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1]]
b_ub = [200, 180, 250]

A_eq =[[20, 0, 0, 40, 0, 0, 50, 0, 0], [0, 10, 0, 0, 30, 0, 0, 40, 0],[0, 0, 15, 0, 0, 35, 0, 0 ,30]]
b_eq= [6000, 5000, 5600]


print('\nОграничения:')
for i in range(len(A_ub)):
	outstr=''
	for i_x in range(len(A_ub[1])):
		if A_ub[i][i_x]>0:
			if A_ub[i][i_x]>1:
				outstr+='+'+str(A_ub[i][i_x])+'*x'+str(i_x)
			else:
				outstr+='+x'+str(i_x)
	outstr+='<='+str(b_ub[i])
	print(outstr)
	outstr=''

for i in range(len(A_eq)):
	outstr=''
	for i_x in range(len(A_eq[1])):
		if A_eq[i][i_x]>0:
			if A_eq[i][i_x]>1:
				outstr+='+'+str(A_eq[i][i_x])+'*x'+str(i_x)
			else:
				outstr+='x'+str(i_x)
	outstr+='='+str(b_eq[i])
	print(outstr)
	outstr=''

# Преобразование в каноническую форму
# Формирование симплексной таблицы
# Вычисление симплекс методом
res = linprog(c, A_ub, b_ub, A_eq, b_eq)

# Вывод результатов
result=res['x']
value_f=0
for i,e in enumerate(result):
	result[i]=round(e,2)
	value_f+=result[i]*c[i]
print('\nОптимальное решение:\nx={0}'.format(result))
print ('\nЗначение целевой функции:\nf(x)={0}'.format(-value_f))
input()