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

