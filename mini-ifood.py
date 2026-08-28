class Restaurante:
    def __init__(self, id_rest, nome, x, y):
        self.id = id_rest
        self.nome = nome
        self.x = x
        self.y = y

class Entregador:
    def __init__(self, id_entregador, nome, disponivel, x, y):
        self.id = id_entregador
        self.nome = nome
        self.disponivel = disponivel  # True (Livre) ou False (Ocupado)
        self.x = x
        self.y = y

restaurantes = [
    Restaurante(1, "Pina hamburguers", 2, 5),
    Restaurante(2, "Boa comida", 8, 3),
    Restaurante(3, "Nonna Ristorante", 4, 9),
    Restaurante(4, "Mia madre italiana", 1, 2),
    Restaurante(5, "Cantina da massa", 7, 7)
]


entregadores = [
    Entregador(1, "Jean", True, 3, 4),
    Entregador(2, "Maria", False, 9, 2),
    Entregador(3, "Pedro", True, 5, 8),
    Entregador(4, "Ana", True, 1, 6)
]        

def calcular_distancia(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
