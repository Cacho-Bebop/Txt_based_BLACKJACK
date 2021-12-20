from classes import *
from mechanics import *

game_on = True

apuesta_minima = 50

name = input("\nHola! ingresa tu nombre para comenzar a jugar Blackjack: ")

    # inicio juego
bienvenida(name)
reglas_juego()

# comienzo del juego
while game_on:

    ronda = 1

    #instanciar jugadores:
    player1 = player(name.title(), 500)
    
    #croupier:
    c1 = croupier('John', 999)


    play = input("\nReady to play?(press key  'Y' to say yes | press key 'N' to close the game)\n->  ")

    if  play.casefold() == 'Y'.casefold():
        
        playing = True

    elif play.casefold() == 'N'.casefold():

        playing = False
        game_on = False

    else:
  
        print("\nPress enter when you are ready")

    input("\nPress enter")
    playing = True

    player1.ver_dinero()
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
    player1.ver_dinero()
    player1.comenzar_a_jugar()
    # comenzar la partida 
    #  ! 1 player

    while playing and player1.jugando == True:
        
        print(f"RONDA {ronda}")

        # se crea el mazo
        deck = Mazo()

        # se mezcla el mazo
        deck.mezclar_cartas()
        
        # el cropier ahora esta en poder del mazo
        c1.cartas = deck.full_deck

        # variable auxiliar para holdear la carta que va a ser repartida
        cartas_en_mano_croupier = []

    
       
        # se realiza apuesta

                
          
    #condicion primera ronda ***
#-------------------------- ROUND ONE ----------------------------------#

        # se añaden 2 cartas al "mazo del croupier" que son las que se repartiran luego al jugador.
        # o sea la primeras 2 cartas iniciales 

        # player 1 añade la carta su mano
        if ronda == 1:
           
            for i in range(2):
                
                carta = c1.repartir_carta()
                
                print(carta)

                if carta.rango == 'as':

                    print("\n AS vale 1 o 11?\n oprime 0 para valor 1  | oprime 1 para valor 11:")
                    
                    good = False
                    while not good:
                        valor_as = input("opcion:")
                        if valor_as == 1 or valor_as == 0:

                            good = True
                            
                            if valor_as == 1:    
                                cartas_en_mano_croupier.append(carta)
                                cartas_en_mano_croupier[i] = card(carta.palo, 'once')

                        else:

                             valor_as = input("\nseleccione en el rango de opciones valido ( 0 | 1)\n: ")
                        
                else:

                    player1.recibir_carta(carta)
            


            # el jugador 1 recibe las primeras 2 cartas 
            #player1.recibir_carta(cartas_en_mano_croupier)
            cartas_en_mano_croupier.clear()
            
            # se suman la cartas 
            suma_de_cartas_p1 = player1.contar_cartas()

            print("\n Cartas en mano: ")        
            for carta in player1.cartas:
                    
                    print(carta)
            
            input()

            print(f"\nLas cartas suman: {suma_de_cartas_p1} ")
            player1.ver_dinero()   

            input()
        # checkea si hay blackjack con las primeras 2 cartas que dispone el jugador
            if is_blackjack(suma_de_cartas_p1):
            
                suma_de_cartas_croupier = c1.obtener_cartas()


            # checkea si el croupier tambien tiene black jack
                if suma_de_cartas_croupier < suma_de_cartas_p1:
                
                    print(f"\nTus cartas son superiores a las del croupier {suma_de_cartas_p1} > {suma_de_cartas_croupier}")
                    player1.recibir_dinero(apuesta_p1 + (apuesta_p1 / 2))
            
                elif(c1.obtener_cartas() < suma_de_cartas_p1):
                    print("\nEmpate")

#----------------------- RONDA REGULAR ------------------------------------- #
        
        #!!!!!! ERROR 
        
        jugada = movimiento_jugador()
        print(jugada)
        input()
        # 0 -> pide cartas
        # 1 -> no pide carta -> siguiente turno
        # 2 -> rendirse
        # 3 -> doblar
        # 4 -> dividir
        # 5 -> seguro



        # 0 choice --------------------------------------------
        if jugada == 0: 

            # croupier holdea una carta
            cartas_en_mano_croupier.append(c1.repartir_carta())
            print(f"Cartas que vas a recibir  {cartas_en_mano_croupier[0]} ")
            # el jugador recibe la carta pedida
            player1.recibir_carta(cartas_en_mano_croupier)
            print(f"\nTus cartas suman {player1.comenzar_a_jugar()}")
            cartas_en_mano_croupier.clear()
            input()

            if player1.contar_cartas() > 21:
                    
                print("\nLas cartas suman mas de 21.\nUsted a perdido el juego")
                player1.jugando = False
                input()

            elif player1.contar_cartas == 21:

                if (player1.cartas[0] + player1.cartas[1]) == 11 and c1.obtener_cartas() < 21:

                    print("\nBlackjack!")
                    player1.recibir_dinero(apuesta_p1 + (apuesta_p1 / 2))
                    input()

                elif c1.contar_cartas() == 21:

                    print("\nEmpate")
                    player1.recibir_dinero(apuesta_p1)
                    input()
                
        #-------------------------------------------------------------------

        if jugada == 1:

            cartas_en_mano_croupier.append(c1.repartir_carta())
            cartas_en_mano_croupier.clear()


        if jugada == 2:

            player1.jugando = False
            player1.recibir_dinero(apuesta_p1 / 2)
            

        if player1.jugando == False:
                
            playing = False
        
        
        # -> siguiente ronda
        ronda = ronda + 1 






