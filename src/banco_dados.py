import sqlite3
import pandas as pd

print("Iniciando a criação do Banco de Dados SQL...")

# 1. Criando e conectando ao banco de dados (o arquivo será criado na pasta)
conexao = sqlite3.connect('sompo_seguros.db')
cursor = conexao.cursor()

# 2. Escrevendo o SQL para criar a tabela de Telemetria
# PRIMARY KEY AUTOINCREMENT cria um ID único para cada linha automaticamente
sql_tabela_telemetria = '''
CREATE TABLE IF NOT EXISTS Historico_Telemetria (
    id_leitura INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento INTEGER,
    idade_anos INTEGER,
    horas_uso_continuo INTEGER,
    rpm_medio REAL,
    temperatura_celsius REAL,
    houve_quebra INTEGER
)
'''
cursor.execute(sql_tabela_telemetria)

# 3. Escrevendo o SQL para criar a tabela de Alertas (que a IA vai usar depois)
sql_tabela_alertas = '''
CREATE TABLE IF NOT EXISTS Alertas_IA (
    id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento INTEGER,
    risco_quebra_porcentagem REAL,
    nivel_alerta TEXT,
    data_analise TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''
cursor.execute(sql_tabela_alertas)

# 4. Lendo o CSV com o Pandas
df_telemetria = pd.read_csv('telemetria_sompo_simulada.csv')

# 5. Jogando os dados do Pandas direto para o SQL!
# O 'if_exists="append"' adiciona os dados sem apagar a tabela.
# O 'index=False' evita que o Pandas crie uma coluna extra de numeração.
print("Transferindo dados do CSV para o Banco SQL...")
df_telemetria.to_sql('Historico_Telemetria', conexao, if_exists='append', index=False)

# 6. Salvando e fechando o banco
conexao.commit()
conexao.close()

print("Sucesso! Banco 'sompo_seguros.db' criado e populado com os dados da telemetria.")