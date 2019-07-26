#Подпрограмма вычисления х_
def x_calculation(x,f_val):
	a=[]
	for i in range(3):
		a.append([])
	a[0]=f_val[0]
	a[1]=(f_val[1]-f_val[0])/(x[1]-x[0])
	a[2]=1/(x[2]-x[1])*((f_val[2]-f_val[0])/(x[2]-x[0])-a[1])
	return ((x[0]+x[1])/2-a[1]/(2*a[2]))


def main(function, xn, xk):
	#Граничные точки для х берутся из этапа установления границ
	a=[0,0,0]
	x=[xn,(xk+xn)/2,xk]
	print('Начальный массив точек x=',x)

	#Вычисление значений функции в начальных точках и их вывод
	str1=''
	str1='Значения функции в начальных точках соответственно ='
	f_val=[]
	for i, e in enumerate(x):
		f_val.append(function(e))
		str1+=' '+str(round(f_val[i],3))
	f_val.append(0)
	print(str1)

	#Поиск индекса максимального значения функции для последующей сортировки
	imax=f_val.index(max(f_val))

	i=0 
	#Основной цикл
	while i!=20 and (abs(f_val[0]-f_val[1]) and abs(f_val[1]-f_val[2]))>10**(-5) :
		print ('\nИтерация #',i)
		x_=x_calculation(x,f_val)
		f_val[3]=(function(x_))
		print('Значение функции в точке х_   f({0:.3})={1:.3}'.format(x_,f_val[3]))

		#Поиск максимального значения функции и замена соответсвующего ему х
		imax=f_val.index(max(f_val))
		if f_val[3]!=max(f_val):
			print('Отбрасываем точку x={0:.3} со значением f(x)={1:.4}'.format(x[imax],max(f_val)))
			x[imax]=x_

		#Сортировка значений х и соответствующих им значений функции
		x.sort()
		for index,e in enumerate(x):
			if f_val[index]!=function(e):
				f_val[index]=function(e)


		if (abs(f_val[0]-f_val[1]) and abs(f_val[1]-f_val[2]))<10**(-5):
			print('Достигнута разница между значениями менее 0.00001 за количество итераций = ',i)
			print('')
		

		#Вывод значений в необходимом формате
		P=[round(elem,3) for elem in x]
		f_print=[round(elem,3) for elem in f_val]
		print('Полученный массив x={0}\nЗначения функции соответсвенно f={1}'.format(P,f_print))
		i+=1


if __name__ == '__main__':
	def f(x):
		return 3*x**4 + (x-1)**2
	main(f,-2.0,3.0)