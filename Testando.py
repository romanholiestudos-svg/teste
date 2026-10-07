# -*- coding: utf-8 -*-
import streamlit as st

# Título do aplicativo
st.title("Avaliação 4 - Gestão de Tarifas")

# Criando uma tupla chamada
limites_tarifa = (15.50, 50.0)
tarifa_min, tarifa_max = limites_tarifa

st.subheader("Configurações de Tarifa")
st.write(f"**Tarifa mínima:** R$ {tarifa_min:.2f}")
st.write(f"**Tarifa máxima:** R$ {tarifa_max:.2f}")

st.subheader("Entrada de Dados da Esteira")

# Criando campos de entrada do Streamlit no lugar do 'input()' do terminal
v1 = st.number_input("Digite o valor do frete para o pacote 1: R$ ", min_value=0.0, step=1.0, value=10.0)
v2 = st.number_input("Digite o valor do frete para o pacote 2: R$ ", min_value=0.0, step=1.0, value=20.0)
v3 = st.number_input("Digite o valor do frete para o pacote 3: R$ ", min_value=0.0, step=1.0, value=30.0)

# Botão para processar os dados inseridos
if st.button("Calcular Relatório e Manifesto"):
    esteira = [v1, v2, v3]
    
    esteira.insert(0, 20.0)
    pacote_retido = esteira.pop()

    st.warning(f"**Pacote retido:** R$ {pacote_retido:.2f}")

    esteira.sort()

    st.write(f"**Esteira ordenada:** {[f'R$ {val:.2f}' for val in esteira]}")

    quantidade_final = len(esteira)
    faturamento_total = sum(esteira)
    maior_tarifa = max(esteira)

    st.markdown("---")
    st.subheader("📊 Relatório Final")
    st.write(f"**Quantidade final de pacotes:** {quantidade_final}")
    st.write(f"**Faturamento total da rota:** R$ {faturamento_total:.2f}")
    st.write(f"**Maior tarifa do lote:** R$ {maior_tarifa:.2f}")

    st.markdown("---")
    st.subheader("📋 Manifesto")

    for id, tarifa in enumerate(esteira, start=1):
        if tarifa < tarifa_max:
            classificacao = "PADRÃO"
        else:
            classificacao = "TARIFA PREMIUM"
        st.write(f"Entrega #{id}: R$ {tarifa:.2f} — :{classificacao}:")
