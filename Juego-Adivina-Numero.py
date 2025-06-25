#JUEGO DE ADIVINANZA NUMERICA

import random
max = 101                             #Recordar que el lim superior del rango no esta incluido
num_secreto = random.randint(0,max)
adivinado = False
max_intentos = 10
intento = 0

print("""   !Bienvenido al 'Juego de Adivinanza Numérica'!
El número a adivinar se encuentra en el rango: 0 -""", max-1 , """
Tienes """, max_intentos, " intentos disponibles.")

while not adivinado:
    if not intento < max_intentos:
        print("!Game Over! No has logrado adivinar el número")
        break

    entrada = input("Introduce un número: ")        #input lee y trae un str y debo pasarlo a int
    numero = int(entrada)
    intento += 1

    if numero >= max or numero < 0:
        intento -= 1
        print("""El número escogido está fuera del rango, vuelva a intentarlo.
Esta entrada no será contabilizada, aún tienes""", max_intentos-intento, " intentos.")

    elif numero == num_secreto:
        adivinado = True
        print("!Felicitaciones has adivinado el número!")
    elif numero < num_secreto:
        print("El número es mayor al ingresado, restan ", max_intentos-intento, " intentos.")
    else:                                           #tambien se puede expresar elif numero > num_secreto: pero como es la unica opcion restante es mas eficiente usar else
        print("El número es menor al ingresado, restan ", max_intentos-intento, " intentos.")
    
    
