## Desarrolladores: Cristian Astorquiza - Juan Felipe Riascos
''' 
Carrera numérica: Cree una función en Python que permita simular el comportamiento
 del juego de “Carrera numérica” bajo las siguientes condiciones y reglas
 de juego:

Entradas:
a. El sistema debe solicitar por pantalla la cantidad de jugadores
(Mínimo 2, máximo 4).
Remark: Valide que no acepte menor de dos, ni más de 4
jugadores.
b. El sistema debe solicitar por pantalla el Nivel de tablero a jugar:
 Considere el siguiente menú:
1. Nivel básico (Tablero de 20 posiciones)
2. Nivel intermedio (Tablero de 30 posiciones)
3. Nivel avanzado (Tablero de 50 posiciones)
Proceso:
c. Una vez inicie el juego, en el turno de cada jugador, el sistema debe
“lanzar los dados” y generar aleatoriamente las posiciones a
mover. Este proceso se realizará cíclicamente por cada turno. El
juego finalizará ÚNICAMENTE cuando un jugador llegue a la meta.
d. Remark: Si el jugador obtiene 3 pares consecutivos, es el ganador.
Tenga en cuenta que la meta será la última posición del tablero, de
acuerdo al nivel escogido en el ítem B.
'''
a = 1
players = []
points = []
i = 1
dado_1 = 0
dado_2 = 0

from random import randint, uniform, random

def tiros():
    puntaje =  randint(1,6)
    return puntaje

def nivel_basico():
    #JUEGO PARA 2 JUGADORES
    if x == 2:
    #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        acu = 0

        while ((p1 or p2) <= 20):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 20):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 20):
                print("El ganador es, el JUGADOR 2 !!!")
                break
            
    #JUEGO PARA 3 JUGADORES
    if x == 3:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        acu = 0

        while ((p1 or p2 or p3) <= 20):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 20):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 20):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 20):
                print("El ganador es, el JUGADOR 3 !!!")
                break
            
    #JUEGO PARA 4 JUGADORES
    if x == 4:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        acu = 0

        while ((p1 or p2 or p3 or p4) <= 20):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 20):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 20):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 20):
                print("El ganador es, el JUGADOR 3 !!!")
                break
                    
            #JUGADOR 4
            lanzar = input()
            print("Tira, Jugador: 4")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p4 = p4 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 4
            if(p4 >= 20):
                print("El ganador es, el JUGADOR 4 !!!")
                break

def nivel_intermedio():
    #JUEGO PARA 2 JUGADORES
    if x == 2:
    #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        acu = 0

        while ((p1 or p2) <= 30):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 30):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 30):
                print("El ganador es, el JUGADOR 2 !!!")
                break
            
    #JUEGO PARA 3 JUGADORES
    if x == 3:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        acu = 0

        while ((p1 or p2 or p3) <= 30):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 30):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 30):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 30):
                print("El ganador es, el JUGADOR 3 !!!")
                break
            
    #JUEGO PARA 4 JUGADORES
    if x == 4:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        acu = 0

        while ((p1 or p2 or p3 or p4) <=30):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 30):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 30):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 30):
                print("El ganador es, el JUGADOR 3 !!!")
                break
                    
            #JUGADOR 4
            lanzar = input()
            print("Tira, Jugador: 4")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p4 = p4 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 4
            if(p4 >= 30):
                print("El ganador es, el JUGADOR 4 !!!")
                break

def nivel_avanzado():
    #JUEGO PARA 2 JUGADORES
    if x == 2:
    #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        acu = 0

        while ((p1 or p2) <= 50):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 50):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 50):
                print("El ganador es, el JUGADOR 2 !!!")
                break
            
    #JUEGO PARA 3 JUGADORES
    if x == 3:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        acu = 0

        while ((p1 or p2 or p3) <= 50):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 50):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 50):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 50):
                print("El ganador es, el JUGADOR 3 !!!")
                break
            
    #JUEGO PARA 4 JUGADORES
    if x == 4:
        #Puntajes para cada jugador
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        acu = 0

        while ((p1 or p2 or p3 or p4) <=50):
            #JUGADOR 1
            lanzar = input()
            print("Tira, Jugador: 1")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p1 = p1 + acu
            print("Avanza a la posición: ", p1)

            #VALIDACION PUNTAJE JUGADOR 1
            if(p1 >= 50):
                print("El ganador es, el JUGADOR 1 !!!")
                break
                    
            #JUGADOR 2
            lanzar = input()
            print("Tira, Jugador: 2")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p2 = p2 + acu
            print("Avanza a la posición: ", p2)

            #VALIDACION PUNTAJE JUGADOR 2
            if(p2 >= 50):
                print("El ganador es, el JUGADOR 2 !!!")
                break
                    
            #JUGADOR 3
            lanzar = input()
            print("Tira, Jugador: 3")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p3 = p3 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 3
            if(p3 >= 50):
                print("El ganador es, el JUGADOR 3 !!!")
                break
                    
            #JUGADOR 4
            lanzar = input()
            print("Tira, Jugador: 4")
            dado_1 = tiros()
            dado_2 = tiros()
            print ("Su puntaje fue: ", dado_1, ",", dado_2)
            acu = dado_1 + dado_2
            p4 = p4 + acu
            print("Avanza a la posición: ", p3)

            #VALIDACION PUNTAJE JUGADOR 4
            if(p4 >= 50):
                print("El ganador es, el JUGADOR 4 !!!")
                break



while a == 1:
    x = int(input("Ingrese la cantidad de Jugadores que van a participar: "))
    while i <= x:
        players.append(i)
        i = i + 1
    if x < 2 or x > 4:
        print("Cantidad de Jugadores no válida, min 2 máx 4")
    else:
        a=0
        print("=============================")
        print("      NIVEL DE JUEGO         ")
        print("=============================")
        print("1. Nivel Básico")
        print("2. Nivel Intermedio")
        print("3. Nivel Avanzado")
        z = int(input("Ingresa el número del nivel de juego: "))

        if z == 1: #Menú
            i = 0
            #a = 0
            print(":::TIPO DE NIVEL: BÁSICO :::")
            while i < x:
                print("Jugador ", players[i], " con :", 0, " puntos ")
                i = i + 1
            
            '''while a < x:
                key = int(input("Digite el numero que saco: "))
                points.append(key)
                a = a + 1 '''
            print("=========================================================================")
            print("Recuerde: Para avanzar en cada tiro por jugador, presionar la tecla ENTER")
            print("=========================================================================")
            print("Empieza el JUEGO !!!")
            print("")
            nivel_basico()
        
        elif z == 2: #Menú
            i = 0
            #a = 0
            print(":::TIPO DE NIVEL: INTERMEDIO :::")
            while i < x:
                print("Jugador ", players[i], " con :", 0, " puntos ")
                i = i + 1
            
            '''while a < x:
                key = int(input("Digite el numero que saco: "))
                points.append(key)
                a = a + 1 '''
            print("=========================================================================")
            print("Recuerde: Para avanzar en cada tiro por jugador, presionar la tecla ENTER")
            print("=========================================================================")
            print("Empieza el JUEGO !!!")
            print("")
            nivel_intermedio()
            
        elif z == 3: #Menú
            i = 0
            #a = 0
            print(":::TIPO DE NIVEL: AVANZADO :::")
            while i < x:
                print("Jugador ", players[i], " con :", 0, " puntos ")
                i = i + 1
            
            '''while a < x:
                key = int(input("Digite el numero que saco: "))
                points.append(key)
                a = a + 1 '''
            print("=========================================================================")
            print("Recuerde: Para avanzar en cada tiro por jugador, presionar la tecla ENTER")
            print("=========================================================================")
            print("Empieza el JUEGO !!!")
            print("")
            nivel_avanzado()
            


            
