#Escriba un algoritmo que solicite un número por pantalla, y visualice el Factorial de dicho valor ingresado

#FACTORIAL DE UN NÚMERO

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n > 1:
            resultado=n*factorial(n-1)
   return resultado

#CALCULO DE LA FACTORIAL DE UN NÚMERO N
x = int(input("Ingrese el número para calcular la factorial: "))
fact=factorial(x)
print(fact)