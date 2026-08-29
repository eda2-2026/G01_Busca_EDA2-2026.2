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
        self.disponivel = disponivel 
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

hash_restaurantes = {}

for r in restaurantes:
    chave = r.nome.lower()
    hash_restaurantes[chave] = r

def busca_hash_por_nome(nome_digitado):
    nome_limpo = nome_digitado.lower().strip()

    return hash_restaurantes.get(nome_limpo, None)

def calcular_distancia(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def busca_binaria_restaurante(restaurantes, id_procurado):
    inicio = 0
    fim = len(restaurantes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if restaurantes[meio].id == id_procurado:
            return restaurantes[meio]

        elif id_procurado < restaurantes[meio].id:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None

def busca_sequencial_entregador(lista_entregadores, rest_x, rest_y):
    melhor_entregador = None
    menor_distancia = float('inf')  
    
    for entregador in lista_entregadores:
        if entregador.disponivel:
            dist = calcular_distancia(entregador.x, entregador.y, rest_x, rest_y)
            
            if dist < menor_distancia:
                menor_distancia = dist
                melhor_entregador = entregador
                
    return melhor_entregador, menor_distancia

