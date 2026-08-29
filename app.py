import streamlit as st
from mini_ifood import restaurantes, entregadores 
from mini_ifood import busca_binaria_restaurante, busca_hash_por_nome, busca_sequencial_entregador

st.set_page_config(page_title="Mini-iFood", page_icon="🛵", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #EA1D2C;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #C01220;
    }
    </style>
""", unsafe_allow_html=True)

# O @st.dialog transforma essa função em uma janela que sobrepõe o site
@st.dialog("Resumo do seu Pedido")
def abrir_card_resultado(restaurante):
    st.success(f"✅ Pedido confirmado no **{restaurante.nome}**!")
    st.markdown("Buscando o entregador mais próximo... 📡")
    
    entregador, distancia = busca_sequencial_entregador(
        entregadores, restaurante.x, restaurante.y
    )
    
    if entregador:
        col_motoboy, col_dist = st.columns(2)
        col_motoboy.metric(label="🛵 Entregador", value=entregador.nome, delta="A caminho!")
        col_dist.metric(label="📍 Distância", value=f"{distancia} km", delta="- Rápido!", delta_color="inverse")
        st.balloons()
    else:
        st.warning("❌ Todos os nossos entregadores estão ocupados no momento.")
        
    st.divider()
    
    if st.button("❌ Fechar e Voltar"):
        st.rerun()

st.title("🛵 Mini-iFood")
st.markdown("**Seu app de delivery impulsionado por Algoritmos de Busca!**")
st.divider()

st.subheader("🔍 Fazer um Pedido")

aba_nome, aba_id = st.tabs(["🔤 Buscar por Nome", "🔢 Buscar por ID"])

with aba_nome:
    nome_digitado = st.text_input("Qual restaurante você procura?", placeholder="Ex: Pizzaria Boa Massa 🍕")
    if st.button("Buscar Restaurante", key="btn_nome"):
        restaurante_escolhido = busca_hash_por_nome(nome_digitado)
        if restaurante_escolhido:
            abrir_card_resultado(restaurante_escolhido)
        else:
            st.error("❌ Ops! Não encontramos nenhum restaurante com esse nome.")

with aba_id:
    id_digitado = st.number_input("Sabe o código? Digite aqui:", min_value=0, step=1)
    if st.button("Buscar por Código", key="btn_id"):
        restaurante_escolhido = busca_binaria_restaurante(restaurantes, id_digitado)
        if restaurante_escolhido:
            abrir_card_resultado(restaurante_escolhido)
        else:
            st.error("❌ Código inválido! Verifique o ID.")

st.divider()

st.subheader("🍽️ Restaurantes Parceiros")
col1, col2, col3 = st.columns(3)

for i, r in enumerate(restaurantes):
    if i % 3 == 0:
        col1.info(f"**{r.nome}**\n\nID: {r.id}")
    elif i % 3 == 1:
        col2.info(f"**{r.nome}**\n\nID: {r.id}")
    else:
        col3.info(f"**{r.nome}**\n\nID: {r.id}")