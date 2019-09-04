#Escriba un algorítmo que reciba por pantalla N números y deje de solicitar números hasta que la SUMA de
# los ya ingresados sea mayor a 100

res = 0

while res <= 100:
    x = int(input("Ingrese un número para realizar la suma: "))
    res = res + x

print ("La suma es igual a: ", res)
