#Cree un algoritmo que imprima los primeros 20 términos de la sucesión Fibonacci 

#SERIE FIBONACCI

def fib(n):
    a = 1 
    b = 0
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
m = 20 #Límite de términos a mostrar en el resultado
fib(m)