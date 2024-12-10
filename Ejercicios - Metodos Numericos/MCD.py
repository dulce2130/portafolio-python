a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))


def divisores(n):
    divisores =[]
    for i in range(1,n+1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def maximoComunDivisor(x,y,z):

    d1 = divisores(x)
    d2 = divisores(y)
    d3 = divisores(z)
    
    mcdlist=[]

    print("Divisores de ",x," = ",d1)
    print("Divisores de ",y," = ",d2)
    print("Divisores de ",z," = ",d3)
    
    for i in d1:
        if i in d2 and d3:
            mcdlist.append(i)

    
    mcd = mcdlist[-1]

    return mcd

f = maximoComunDivisor(a,b,c)
print("El MCD de ",a,", ",b," y ",c," es igual a",f)

  

 
