# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sompo Predict

## Grupo 55

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/guilherme-monteiro-tech/">Guilherme Monteiro Bitencourt (RM: 574151)</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b/">Sabrina Otoni</a>


## 📜 Descrição

A manutenção reativa no agronegócio gera custos altíssimos com sinistros e máquinas paradas. O **Sompo Predict** foi desenvolvido para a Sprint 2 do Challenge FIAP + Sompo Seguros e atua na **Prevenção de Quebra por Sobrecarga**.

O objetivo desta aplicação é analisar em tempo real os dados de telemetria de maquinários agrícolas (Temperatura do Motor, RPM, Horas de Uso Contínuo e Idade do Equipamento) para prever falhas mecânicas antes que elas ocorram. O fluxo de dados incluiu a geração de um dataset simulado, persistência em banco relacional SQLite e a construção de um Dashboard front-end interativo com Streamlit.

Para a predição, utilizamos Inteligência Artificial com o algoritmo **Random Forest Classifier**. O modelo foi submetido a uma validação estatística rigorosa (separando 20% dos dados para teste) e alcançou uma **Acurácia de 99.0%**. A Matriz de Confusão comprovou a eficácia para o negócio: `[[187, 0], [2, 11]]`. A IA não gerou nenhum alarme falso (0 falsos positivos) e previu corretamente as 11 quebras iminentes, permitindo à Sompo atuar de forma preventiva e mitigar riscos.

**Demonstração em Vídeo (Pitch):** 


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.1.0 - 02/06/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

