def F(x):
    return 3*x**4+(x-1)**2
 
#Производная 1
def F1(x):
    return 12*x**3+2*x-2

#Производная 2
def F2(x):
    return 36*x*x+2

def Newtone(x):
    i=0
    print ('X[{0}]={1}'.format(i,x))
    xn=x-F1(x)/F2(x)
    i+=1
    print('X[{1}]={0}'.format(xn,i))
    while abs(xn-x)>10**(-5) and i!=20:
        i+=1
        x=xn
        xn=x-F1(x)/F2(x)
        print('X[{1}]={0}'.format(xn,i))
    print('Достигнута разница между значениями менее 0.00001')

if __name__=="__main__":
    Newtone(1)