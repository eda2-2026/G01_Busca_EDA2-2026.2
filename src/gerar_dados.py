import json
import random

tipos = ["Pizzaria", "Hamburgueria", "Sushi", "Churrascaria", "Doceria", "Pastelaria", "Açaí", "Restaurante", "Cantina", "Bistrô"]
sobrenomes = ["Central", "Express", "Premium", "Gourmet", "da Vila", "Chef", "Mais", "Top", "Delivery", "Saboroso"]
nomes_pessoas = ["Carlos", "Ana", "João", "Marcos", "Beatriz", "Lucas", "Pedro", "Mariana", "Julia", "Rafael", "Fernando", "Camila", "Rodrigo", "Amanda", "Diego"]

restaurantes = []

for i in range(1, 101):
    nome_restaurante = f"{random.choice(tipos)} {random.choice(sobrenomes)} {i}"
    
    restaurantes.append({
        "id": 100 + i,
        "nome": nome_restaurante,
        "x": random.randint(0, 100), 
        "y": random.randint(0, 100)
    })

entregadores = []

for i in range(1, 51):
    entregadores.append({
        "id": i,
        "nome": f"{random.choice(nomes_pessoas)} {i}",
        "disponivel": random.choice([True, True, False]), 
        "x": random.randint(0, 100),
        "y": random.randint(0, 100)
    })

dados = {
    "restaurantes": restaurantes,
    "entregadores": entregadores
}


with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("SUCESSO! O arquivo 'dados.json' foi gerado com 100 restaurantes e 50 entregadores.")