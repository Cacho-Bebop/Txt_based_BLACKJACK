from classes import *

game_on = True

def bienvenida(name):

    print(f"\nBienvenido al juego {name}")

def reglas_juego():

    print("\n--Reglas--\n> debes contar con un minimo de 50$\n> debes sumar 21 con las cartas, de lo contrario perderas tu apuesta\n> Si logras blackjack el pago es 3 a 2 ( lo apostado + 1/2 de lo apostado)")

apuesta_minima = 50

# comienzo del juego
while game_on:

    name = input("\nHola! ingresa tu nombre para comenzar a jugar Blackjack")

    # inicio juego
    bienvenida(name)
    reglas_juego()

    #instanciar jugadores:
    player1 = player(name.title(), 500)
    
    #croupier:
    john = croupier('John', 999)


    play = input("\nReady to play?( press key 'Y' to say yes)\n->  ")

    if  play == 'Y' :
        
        playing = True

    else:

        
        print("\nPress enter when you are ready")

    input("\nPress enter")
    playing = True

    # comenzar la partida 
    #  
    while playing:

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


        player1.apostar(apuesta_p1)










