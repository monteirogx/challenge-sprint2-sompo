import streamlit as st
import pandas as pd
import joblib

# 1. Carregando o "cérebro" do robô que você salvou
modelo = joblib.load('modelo_sompo.pkl')

# 2. Construindo a Interface Visual (O Front-end)
st.title("🚜 Painel de Prevenção de Quebra - Sompo")
st.write("Insira os dados da telemetria do trator para analisar o risco de falha mecânica.")

st.markdown("---")  # Linha divisória

# 3. Criando as caixas de digitação para o Gestor de Frota
# Dividindo a tela em duas colunas para ficar bonito
col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade do Equipamento (anos)",
                            min_value=1, max_value=30, value=5)
    horas_uso = st.number_input(
        "Horas de Uso Contínuo", min_value=1, max_value=24, value=8)

with col2:
    rpm = st.number_input("RPM Médio", min_value=500,
                          max_value=3000, value=1500)
    temperatura = st.number_input(
        "Temperatura do Motor (°C)", min_value=50, max_value=150, value=80)

st.markdown("---")

# 4. O Botão Mágico
if st.button("Analisar Risco", type="primary"):

    # Pegando os dados que o usuário digitou na tela e transformando em tabela para a IA ler
    dados_entrada = pd.DataFrame({
        'idade_anos': [idade],
        'horas_uso_continuo': [horas_uso],
        'rpm_medio': [rpm],
        'temperatura_celsius': [temperatura]
    })

    # Pedindo para a IA fazer a previsão
    previsao = modelo.predict(dados_entrada)[0]

    # A IA também sabe dizer a "certeza" dela em porcentagem
    probabilidades = modelo.predict_proba(dados_entrada)[0]
    risco_quebra = probabilidades[1] * 100

    # 5. Exibindo o Alerta na Tela
    st.subheader("Resultado da Análise:")

    if previsao == 1:
        # Se previu 1 (Quebra), mostra uma caixa vermelha de erro
        st.error(
            f"🚨 ALERTA CRÍTICO: Risco de quebra de {risco_quebra:.1f}%. \n\n**Recomendação:** PARAR MÁQUINA IMEDIATAMENTE PARA MANUTENÇÃO.")
    else:
        # Se previu 0 (OK), mostra uma caixa verde de sucesso
        st.success(
            f"✅ Equipamento Seguro. Risco de apenas {risco_quebra:.1f}%. \n\n**Recomendação:** Operação liberada.")
