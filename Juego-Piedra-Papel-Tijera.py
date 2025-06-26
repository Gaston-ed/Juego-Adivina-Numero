#JUEGO PIEDRA, PAPEL O TIJERA

#Entrada de datos
nombre1 = input("Bienvenido Jugador 1! Cómo te llamas? ")
nombre2 = input("Bienvenido Jugador 2! Cómo te llamas? ")
puntos_max = input("A cuántos puntos desean jugar? ")
punt_max = int(puntos_max)
punt1 = 0
punt2 = 0

while not punt1 == punt_max and not punt2 == punt_max:
    print(nombre1,"es tu turno.")
    jugador1 = input("Qué eliges? Piedra, papel o tijera? ")
    print(nombre2,"es tu turno.")
    jugador2 = input("Qué eliges? Piedra, papel o tijera? ")
   
    #Limpieza y capitalización de entrada
    jugad1 = jugador1.casefold().strip() 
    jugad2 = jugador2.casefold().strip()
    jug1 = jugad1.capitalize()
    jug2 = jugad2.capitalize()

    #Condiciones de victoria J1
    cond1 = jug1 == "Piedra" and jug2 == "Tijera"
    cond2 = jug1 == "Papel" and jug2 == "Piedra"
    cond3 = jug1 == "Tijera" and jug2 == "Papel"
    cond4 = jug2 == "Piedra" and jug1 == "Tijera"
    cond5 = jug2 == "Papel" and jug1 == "Piedra"
    cond6 = jug2 == "Tijera" and jug1 == "Papel"

    #Comparación y resultados
    if jug1 == jug2:
        print("""Esta ronda ha sido un empate!
Ambos escogieron:  """,jug1,". Vuelvan a intentarlo")
    elif (cond1) or (cond2) or (cond3):
        print("Punto para: ",nombre1,"!", jug1," mata ",jug2,".")
        punt1 += 1
        if (punt1 == punt_max):
            print(nombre1, "ha ganado el juego!")
    elif(cond4) or (cond5) or (cond6):
        print ("Punto para: ",nombre2,"!", jug2," mata ",jug1,".")
        punt2 += 1
        if (punt2 == punt_max):
            print(nombre2, "ha ganado el juego!")
    else:
        print("Alguien cometió un error de ingreso, por favor vuelvan a intentarlo.")


