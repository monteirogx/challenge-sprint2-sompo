import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

conexao = sqlite3.connect('sompo_seguros.db')

df = pd.read_sql_query("select * from Historico_Telemetria", conexao)

# X(causas) / y(Consequências) = Gabarito
X = df.drop(columns=['id_leitura', 'id_equipamento', 'houve_quebra'])
y = df['houve_quebra']

# Separando os dados (80% treino, 20% teste)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 2. Criando e treinando o robô (a floresta aleatória)
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_treino, y_treino)
previsoes = modelo.predict(X_teste)

# 4. Calculando as notas da IA
acuracia = accuracy_score(y_teste, previsoes)
matriz = confusion_matrix(y_teste, previsoes)

# 5. Mostrando o resultado na tela do terminal
print(f"Acurácia do Modelo: {acuracia * 100}%")
print("Matriz de Confusão:")
print(matriz)

# Salvando dados
joblib.dump(modelo, 'modelo_sompo.pkl')
