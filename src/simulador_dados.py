# Importando as ferramentas necessárias
import pandas as pd
import numpy as np

# 1. Definindo o tamanho do nosso dataset (1000 registros para começar)
quantidade = 1000

# 2. Gerando as características básicas (Features)
# np.random.randint sorteia números inteiros entre um valor mínimo e máximo
ids = range(1, quantidade + 1)
idade = np.random.randint(1, 15, quantidade)
horas_uso = np.random.randint(1, 20, quantidade)

# 3. Gerando os dados de operação com base em uma distribuição normal
# np.random.normal(média, desvio_padrao, quantidade)
# A maioria dos tratores opera perto de 1500 RPM, variando uns 300 para mais ou menos.
rpm = np.random.normal(1500, 300, quantidade)

# A temperatura não é aleatória! Ela depende do esforço da máquina.
# Lógica: Temperatura base de 70 graus + (impacto do RPM) + (impacto das horas de uso) + (pequeno ruído aleatório)
temperatura = 70 + (rpm / 150) + (horas_uso * 0.8) + np.random.normal(0, 3, quantidade)

# 4. Criando a Tabela (DataFrame) com o Pandas
dataset_sompo = pd.DataFrame({
    'id_equipamento': ids,
    'idade_anos': idade,
    'horas_uso_continuo': horas_uso,
    'rpm_medio': rpm,
    'temperatura_celsius': temperatura
})

# 5. A REGRA DE OURO: Definindo quem quebra (Nossa variável alvo)
# Inicialmente, dizemos que ninguém quebrou (0)
dataset_sompo['houve_quebra'] = 0

# Vamos aplicar a regra: Se a máquina for velha (> 8 anos) E a temperatura passar de 95 graus...
# ... a chance de quebra é certa (1).
dataset_sompo.loc[(dataset_sompo['idade_anos'] > 8) & (dataset_sompo['temperatura_celsius'] > 95), 'houve_quebra'] = 1

# Adicionando uma segunda regra: Sobrecarga extrema de RPM (independente da idade)
dataset_sompo.loc[dataset_sompo['rpm_medio'] > 2200, 'houve_quebra'] = 1

# 6. Exportando o resultado para um arquivo CSV (que será enviado para o banco de dados depois)
dataset_sompo.to_csv('telemetria_sompo_simulada.csv', index=False)
print("Dataset gerado com sucesso! Arquivo salvo como 'telemetria_sompo_simulada.csv'.")