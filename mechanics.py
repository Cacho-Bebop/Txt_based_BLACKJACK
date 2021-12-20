def bienvenida(name):

    print(f"\nBienvenido al juego {name}")

def reglas_juego():

    print("\n--Reglas--\n> debes contar con un minimo de 50$\n> debes sumar 21 con las cartas, de lo contrario perderas tu apuesta\n> Si logras blackjack el pago es 3 a 2 ( lo apostado + 1/2 de lo apostado)")






def is_blackjack(cartas):



    if cartas == 21:
        
        print("\nBlackjack!")

        return True
    
    else:

        False


def movimiento_jugador():

    print("\nElige tu siguiente movimientos:\n -> perdir carta [0]\n -> Plantarse [1]\n -> Rendirse[2] \n -> Doblar apuesta[3] \n -> Dividir[4]\n -> Seguro[5]")

    ok = False

    while not ok:

        try:

            option = input("-> ")
        
        except  isinstance(option, int):
            
            print("\nPorfavor selecciona una opcion valida.")
        
        except option < 0 or option > 5:
            
            print("\nPorfavor selecciona una opcion valida.")

        else:

            ok = True


    return option

