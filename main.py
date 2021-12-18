from classes import *
from mechanics import *

game_on = True

apuesta_minima = 50

# comienzo del juego
while game_on:

    ronda = 1

    name = input("\nHola! ingresa tu nombre para comenzar a jugar Blackjack")

    # inicio juego
    bienvenida(name)
    reglas_juego()

    #instanciar jugadores:
    player1 = player(name.title(), 500)
    
    #croupier:
    c1 = croupier('John', 999)


    play = input("\nReady to play?( press key 'Y' to say yes)\n->  ")

    if  play == 'Y' :
        
        playing = True

    else:
  
        print("\nPress enter when you are ready")

    input("\nPress enter")
    playing = True

    # comenzar la partida 
    #  ! 1 player

    while playing:

        # se crea el mazo
        mazo = mazo()

        # se mezcla el mazo
        mazo.mezclar_cartas()

        cartas_croupier = []

        player1.comenzar_a_jugar()

        print(f"\nCual es tu apuesta inicial? -> recuerda que lo apostado no puede ser menor a {apuesta_minima}.")

        ok = False

        while not ok:

            try:

                apuesta_p1 = float(input("apuesto: "))
        
            except TypeError:
                
                print("\nPorfavor ingrese un numero")

            else: 

                ok = True
                print("\nMucha gracias por confiar en Bash Casino!\nDisfrute su juego!")

        # se realiza apuesta
        player1.apostar(apuesta_p1)

        # como se añaden 2 cartas al "mazo del croupier" que son las que se repartiran luego al jugador.
        if ronda == 1:

            for i in range(2):
                cartas_croupier.append(c1.repartir_carta())           


        # player 1 añade la carta su mano
        player1.recibir_carta(cartas_croupier)
        

        cartas_croupier.clear()








