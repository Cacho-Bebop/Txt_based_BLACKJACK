""" 
El Black Jack es uno de los juegos más populares del Casino. El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21. Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor. El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
El juego

Se reparten dos cartas a la vista para cada jugador. Entonces el Croupier preguntará si necesita otra carta. En dicho caso, señáleselo claramente con la mano. Si usted tiene Black Jack, gana y se le paga 3 a 2, a menos que el Croupier también tenga Black Jack, en cuyo caso se llama un Empate y ninguna de las dos manos gana. Si sus cartas totalizan un valor más cercano a 21 que las del Croupier, usted gana y se le paga el valor de la apuesta. El Croupier deberá plantarse con un total de 17 o más y deberá tomar una carta más si tiene 16 o menos.
Doblando la apuesta

Usted podrá doblar su apuesta inicial con las dos (2) primeras cartas si la suma es 9, 10 u 11, recibiendo solamente una carta adicional.
Abriendo juegos

Si sus primeras dos cartas son iguales, podrá dividirlas abriendo dos juegos y haciendo una apuesta igual a la inicial para el segundo. El Croupier colocará una segunda carta en el primer juego y lo completará antes de continuar con el siguiente. Si divide los Ases, podrá pedir una sola carta más para cada uno. Si entonces recibe un Diez o una figura, en uno de los Ases, obtiene 21 y no Black Jack.
Seguro

Cuando la primera carta del Croupier es un As, usted podrá asegurar su apuesta apostando a que él obtenga Black Jack, colocando hasta la mitad de su apuesta en el espacio llamado “Seguro”. Entonces, si el Croupier obtiene Black Jack, usted pierde su apuesta inicial pero le pagan 2 a 1 su apuesta a “Seguro”. En cambio, si el Croupier no hace Black Jack, usted pierde su apuesta “Seguro”.
"""

from random import shuffle
from typing import List

# data para hacer el objeto carta

palos = ("corazones", "diamantes", "treboles", "picas")
rangos = ("as", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "rey", "reina", "comodin");

valores = {'as': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6,
'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10, 'rey': 10, 'reina': 10, 'comodin': 10}
#-------------------------------------------------------------------------

# carta-------------------------------------------------------
class card:

    def __init__(self, palo, rango):
        self.palo = palo
        self.rango = rango
        self.valor = valores[self.rango]

    ## devolucion si el objeto se quiere imprimir en pantalla
    def __str__(self):

        return self.rango + " de " + self.palo


# mazo------------------------------------------------------
class mazo:

    def __init__(self):
        self.full_deck = []

        # se crea una carta de cada palo con cada valor posible
        for palo in palos:

            for rango in rangos:

                new_card = card(palo, rango)
                self.full_deck.append(new_card)

    def __str__(self) -> str:

        return f"Hay {len(self.full_deck)} cartas en el mazo"
    

    def mezclar_cartas(self):

    
        shuffle(self.full_deck)
    
    # se retira carta del mazo y se retorna el objeto carta retirado
    def sacar_carta(self):

    
        return self.full_deck.pop()
#----------------------------------

#player---------------------------

class player:

    def __init__(self, nombre, dinero):

        self.nombre  = nombre
        self.dinero  = dinero
        self.cartas  = []
        self.jugando = False
    
    def recibir_carta(self, carta):
        
        if isinstance(carta, list):
        
            self.cartas.extend(carta)
        
        else:
            
            self.cartas.append(carta)
    
    def __str__(self) -> str:
        return "Hola! Soy" + self.nombre + "."    

    def apostar(self, cantidad):

        if self.dinero < 0:
            
            print("\nParece ser que no tengo mas dinero.\nTendre que retirarme del juego.")

        else:
            
            self.dinero = self.dinero - cantidad

    def recibir_dinero(self, cantidad):

        #suma el dinero que ya posee el jugador + la cantidad

        if cantidad <= 0:

            print("\nOperacion invalida.")

        else:    
            self.dinero = self.dinero + cantidad

    def comenzar_a_jugar(self):


        self.jugando = True

class croupier(player):

    def __init__(self, nombre, dinero):
        super().__init__(nombre, dinero)
        self.jugando = True
       
    
    def __str__(self) -> str:
        return "Hola, soy" + self.nombre + "! El croupier."


    def repartir_carta(self):
        
        #saca una carta del mazo y la retorna
        return self.mazo.pop()
    