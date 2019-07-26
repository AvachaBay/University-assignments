import sys
from Methods import Golden_section, Quadratic_approximation
#from Methods.Golden_section import main
import Newtone
# точка x = 0.451 точка минимума функции. 

print("###Установление границ________________________________________________")

#Функция 

# Вариант №1
# def f(x):
# 	return 3*x**4 + (x-1)**2
# Вариант №2
# f = lambda x: 3*x**4 + (x-1)**2[]
# Вариант №3
equation='3*x**4 + (x-1)**2'
f = lambda x: eval(equation)


# Вычисление соседних точек с x0 
h=0.5
x=[4]
x=x+[x[0]+h]
x=[x[0]-h]+x
print ('X нач =',x)


#Вывод значений функции
outstr=''
for e in x:
	outstr+=str(f(e))+', '
print('F[Х нач] =',outstr[:-2])

k=1 #Номер итерации
sign=1 #Переменная, отвечающая за направление

#Функция вычисления коэффициента альфа
def alpha(k,sign=-1):
	return sign*2**(k)



#Определение направления движения, корректировка коэффициента alpha
if f(x[k-1])<f(x[k]):
	print('Направление движения - влево')
	sign=-sign

	x[0],x[2]=x[2],x[0]
	
	x+=[x[k+1]+alpha(k)*h]
	print('X след={0} со значением функции f(x)={1}'.format(x[-1:],f(x[3])))
	k+=1

elif f(x[k+1])<f(x[k]):
	print('Направление движения - вправо')

	x+=[x[k+1]+alpha(k)*h]
	print('X след={0} со значением функции f(x)={1}'.format(x[-1:],f(x[3])))
	k+=1
else :
	print('Минимум - x=',x[2])

print('X =',x)

# Основной цикл
while not(f(x[k-1])>=f(x[k]) and f(x[k])<=f(x[k+1])):
	k+=1
	x+=[x[k]+alpha(k-1)*h]
	print('Следующее значение х={0}, сo значением функции f(x)={1}'.format(x[-1:],f(x[k])))
print('X конеч.=',x[-3:])


emptystrings='\n\n\n\n'
print(emptystrings+'###Golden section method____________________________________________________________')
xn=x[len(x)-1]
xk=x[len(x)-3]
Golden_section.main(f,xn,xk)

print(emptystrings+'Квадратичная аппроксимация______________________________________')
Quadratic_approximation.main(f,xn,xk)

print(emptystrings+'Newtone method____________________________________________________________')
# Newtone.main(-3,2)


input(emptystrings+'Нажмите Enter для выхода\n')
