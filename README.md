# 🍔 Mini-iFood: Aplicação de Algoritmos de Busca

Este projeto foi desenvolvido como trabalho semestral para demonstrar a aplicação prática de **Algoritmos de Busca** em um cenário real: um sistema simplificado de delivery de comida.

---

## Equipe
* **Semestre:** 2026.2
* **Desenvolvedores:**
  * Dara Maria Barbosa de Sousa - Matrícula: 202046040
  * Evellyn de Sousa Rocha  - Matrícula: 202045400

---

## Objetivo do Projeto
O objetivo deste sistema é simular a lógica de roteamento de um aplicativo de delivery utilizando estruturas de dados e algoritmos desenvolvidos em **Python**. O programa mapeia restaurantes, entregadores e clientes em um plano cartesiano (X, Y) e utiliza diferentes estratégias de busca para processar um pedido de forma eficiente. Todo o sistema interage com o usuário através de uma **Interface Web interativa**, construída com a biblioteca Streamlit.

---

## Arquitetura do Sistema

Para garantir que o código fosse escalável e organizado, o projeto foi dividido utilizando o padrão de responsabilidades (inspirado em MVC):
* **`app.py` (Front-end):** Interface gráfica e interações com o usuário.
* **`mini_ifood.py` (Back-end):** Lógica matemática e Algoritmos de busca.
* **`dados.json` (Database):** Armazenamento das entidades de forma independente.
* **`gerar_dados.py` (Mock Data):** Script gerador de grande volume de dados simulados (100+ restaurantes e 50+ entregadores) para estressar e provar a eficiência dos algoritmos de busca.

---

## Algoritmos e Conceitos Aplicados

Para otimizar o desempenho do sistema, aplicamos a ferramenta certa para cada tipo de dado. O projeto demonstra três complexidades de tempo diferentes:

### 1. Hashing / Tabelas Hash (O(1))
* **Onde foi usada:** Na busca do restaurante pelo Nome exato.
* **Por que:** Utilizando dicionários nativos do Python (que funcionam como Tabelas Hash na memória), o sistema não precisa ler a lista inteira. Ao digitar o nome, o algoritmo calcula a posição exata na memória e localiza o restaurante instantaneamente.

### 2. Busca Binária (O(log n))
* **Onde foi usada:** Na seleção do restaurante pelo código (ID).
* **Por que:** Como os Restaurantes possuem IDs fixos, armazenamos esses dados em um vetor previamente **ordenado**. Quando o cliente digita o ID desejado, a Busca Binária localiza o restaurante dividindo o vetor pela metade a cada iteração, tornando a busca extremamente rápida.

### 3. Busca Sequencial (O(n))
* **Onde foi usada:** Na busca pelo entregador ideal.
* **Por que:** Os entregadores estão em constante movimento pela cidade e seus status (Livre/Ocupado) mudam a todo momento. Como a lista não pode ser mantida ordenada por distância de forma simples, usamos a Busca Sequencial para varrer o vetor de entregadores, filtrando apenas os que estão "Livres" e calculando qual possui a menor distância até o restaurante.

### 4. Distância de Manhattan
* **Onde foi usada:** No cálculo de proximidade entre o Entregador e o Restaurante.
* **Por que:** Em uma malha urbana (ruas e quarteirões), a distância em linha reta (Euclidiana) não é realista. A Distância de Manhattan simula o percurso em quarteirões usando a soma dos valores absolutos das coordenadas:
  $d = |x_2 - x_1| + |y_2 - y_1|$

---

## Como Executar

Este projeto foi desenvolvido dividindo a lógica no *Back-end* (`mini_ifood.py`) e a interface gráfica no *Front-end* (`app.py`).

Para rodar na sua máquina, siga os passos abaixo:

1. Abra o terminal.
2. Instale a biblioteca de interface gráfica (Streamlit):
```bash
   pip install streamlit

```

3. Navegue até a pasta do projeto.
4. (Opcional) Gere um banco de dados novo e aleatório com 150 entidades executando:

 ```bash
  python gerar_dados.py

```
5. Execute o servidor local da aplicação:
```bash
  streamlit run app.py

```

6. O seu navegador padrão abrirá automaticamente com o aplicativo rodando!
   
## Video demonstração 
trabalho 1 : https://youtu.be/GkBA6VPwQkM

