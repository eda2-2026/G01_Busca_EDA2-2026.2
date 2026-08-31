import json

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

restaurantes = []
entregadores = []
hash_restaurantes = {}

# Abre o arquivo JSON e lê os dados
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    
    for r in dados['restaurantes']:
        novo_restaurante = Restaurante(r['id'], r['nome'], r['x'], r['y'])
        restaurantes.append(novo_restaurante)
    
        hash_restaurantes[novo_restaurante.nome.lower()] = novo_restaurante
        
    for e in dados['entregadores']:
        novo_entregador = Entregador(e['id'], e['nome'], e['disponivel'], e['x'], e['y'])
        entregadores.append(novo_entregador)

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

def busca_hash_por_nome(nome_digitado):
    nome_limpo = nome_digitado.lower().strip()
    return hash_restaurantes.get(nome_limpo, None)

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

def calcular_distancia(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)



