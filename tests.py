from classes import *

c1 = croupier('John', 99999)
deck = Mazo()

# se mezcla el mazo
deck.mezclar_cartas()
        
# el cropier ahora esta en poder del mazo
c1.cartas = deck.full_deck

# variable auxiliar para holdear la carta que va a ser repartida
cartas_en_mano_croupier = []



for carta in c1.cartas:
    print(carta)