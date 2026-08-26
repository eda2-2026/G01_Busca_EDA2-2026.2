# 🍔 B-Food: Aplicação de Algoritmos de Busca

Este projeto foi desenvolvido como trabalho semestral para demonstrar a aplicação prática de **Algoritmos de Busca** em um cenário real: um sistema simplificado de delivery de comida.

---

## 👥 Equipe
* **Semestre:** 2026.2
* **Desenvolvedores:**
  * Dara Maria Barbosa de Sousa - Matrícula: 202046040
  * Evellyn de Sousa Rocha  - Matrícula: 

---

## 🎯 Objetivo do Projeto
O objetivo deste sistema é simular a lógica de roteamento de um aplicativo de delivery utilizando estruturas de dados básicas em C. O programa mapeia restaurantes, entregadores e clientes em um plano cartesiano (X, Y) e utiliza diferentes estratégias de busca para processar um pedido de forma eficiente.

---

## 🧠 Algoritmos e Conceitos Aplicados

Para otimizar o desempenho do sistema, aplicamos a ferramenta certa para cada tipo de dado:

### 1. Busca Binária 
* **Onde foi usada:** Na seleção do restaurante pelo cliente.
* **Por que:** Como os Restaurantes possuem IDs fixos, armazenamos esses dados em um vetor previamente **ordenado**. Quando o cliente digita o ID desejado, a Busca Binária localiza o restaurante dividindo o vetor pela metade a cada iteração, tornando a busca extremamente rápida.

### 2. Busca Sequencial
* **Onde foi usada:** Na busca pelo entregador ideal.
* **Por que:** Os entregadores estão em constante movimento pela cidade e seus status (Livre/Ocupado) mudam a todo momento. Como a lista não pode ser mantida ordenada por distância de forma simples, usamos a Busca Sequencial para varrer o vetor de entregadores, filtrando os que estão "Livres" e calculando qual possui a menor distância até o restaurante.

### 3. Distância de Manhattan
* **Onde foi usada:** No cálculo de proximidade entre o Entregador e o Restaurante.
* **Por que:** Em uma malha urbana (ruas e quarteirões), a distância em linha reta (Euclidiana) não é realista. A Distância de Manhattan simula o percurso em quarteirões usando a soma dos valores absolutos das coordenadas:
  $d = |x_2 - x_1| + |y_2 - y_1|$

---

## 🛠️ Como Executar

Este projeto foi desenvolvido em **Python**. Para rodar na sua máquina, siga os passos abaixo:

1. Abra o terminal.
2. Navegue até a pasta do projeto.
3. Execute o programa:
   python b_food.py
