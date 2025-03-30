# Sistema web inteligente para recomendação de manutenção preventiva em equipamentos industriais

# Imports
import joblib
import pandas as pd
import streamlit as st

# Carregar o modelo e o scaler salvos
model_file = "modelos/modelo_v1.pkl"
scaler_file = "padronizadores/scaler_v1.pkl"
modelo = joblib.load(model_file)
scaler = joblib.load(scaler_file)


# Função para fazer a recomendação de manutenção
def recomenda_manutencao(novo_dado):
    # Definir os nomes das colunas conforme o scaler foi ajustado
    colunas = ["sensor_1", "sensor_2", "sensor_3", "sensor_4", "sensor_5"]

    # Converter o novo dado para DataFrame com os nomes de colunas corretos
    novo_dado_df = pd.DataFrame([novo_dado], columns=colunas)

    # Aplicar o scaler ao novo dado
    novo_dado_scaled = scaler.transform(novo_dado_df)

    # Fazer a previsão
    predicao = modelo.predict(novo_dado_scaled)
    predicao_proba = modelo.predict_proba(novo_dado_scaled)[:, 1]

    # Retornar a classe e a probabilidade
    return predicao[0], predicao_proba[0]


# Configura a página da aplicação no Streamlit
st.set_page_config(page_title="Recomenda ML", layout="centered")

# Define o título da aplicação
st.title(
    "Sistema web inteligente para recomendação de manutenção preventiva em equipamentos industriais"
)

# Define uma legenda explicativa da aplicação
st.caption(
    "Aplicação web para prever a necessidade de manutenção preventiva em equipamentos industriais"
)

st.header("Insira os valores dos sensores:")
sensor_1 = st.number_input("Sensor 1", value=0.0)
sensor_2 = st.number_input("Sensor 2", value=0.0)
sensor_3 = st.number_input("Sensor 3", value=0.0)
sensor_4 = st.number_input("Sensor 4", value=0.0)
sensor_5 = st.number_input("Sensor 5", value=0)

# Botão para realizar a previsão
if st.button("Verificar necessidade de manutenção"):
    novo_dado = [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5]
    classe, probabilidade = recomenda_manutencao(novo_dado)

    # Mostrar os resultados
    st.write(
        f"Classe da Previsão: {'Realizar manutenção' if classe == 1 else 'Nenhuma manutenção necessária'}"
    )
    st.write(f"Probabilidade de manutenção: {probabilidade:.2%}")
