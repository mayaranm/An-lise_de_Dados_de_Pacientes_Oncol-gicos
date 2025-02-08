#importando as bibliotecas : Como e Por que:
#Pandas (pd): É a principal biblioteca para manipulação e análise de dados em Python. O pandas facilita o carregamento, limpeza, transformação e análise de grandes conjuntos de dados. Usamos o DataFrame do pandas, que é uma estrutura de dados semelhante a uma tabela, ideal para trabalhar com dados tabulares, como uma planilha do Excel.
#NumPy (np): É uma biblioteca fundamental para computação científica. Embora o pandas seja muito eficiente para dados tabulares, o NumPy fornece suporte para arrays multidimensionais, operações matemáticas e funções estatísticas. Ele é usado internamente pelo pandas, mas, no seu projeto, ele pode ser útil em futuras análises que envolvem operações matemáticas mais avançadas.
#Matplotlib (plt) e Seaborn (sns): São bibliotecas de visualização de dados. O Matplotlib é a base, enquanto o Seaborn é uma extensão do Matplotlib que facilita a criação de gráficos estatísticos bonitos e mais informativos. Usaremos essas bibliotecas para gerar gráficos e visualizar os dados de forma clara.  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Dados fictícios
dados = {
    "Paciente": ["Maria", "Carlos", "Joáo", "Rita", "Renato", "Miguel", "Jorge", "Ana", "Jessica", "Robson"],
    "Idade": [55, 60, 45, 50, 65, 70, 40, 58, 62, 48],
    "Tipo_Cancer": ["Mama", "Pulmão", "Próstata", "Mama", "Pulmão", "Leucemia", "Próstata", "Mama", "Leucemia", "Pulmão"],
    "Sobrevivencia_Meses": [48, 24, 60, 36, 18, 12, 72, 30, 20, 25],
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Exibindo os dados carregados
print("Dados carregados com sucesso!")
print(df)

#Criando o Dicionário de Dados: Aqui, criamos um dicionário com os dados fictícios. Cada chave representa uma coluna de dados (por exemplo, Paciente, Idade, etc.), e os valores são listas com as informações relacionadas a cada paciente. Esse formato é muito comum em Python, pois facilita o acesso e manipulação dos dados.
#Convertendo para DataFrame: Utilizamos o pandas.DataFrame() para transformar o dicionário em uma tabela estruturada (DataFrame). A vantagem do DataFrame é que ele permite realizar operações e análises de maneira eficiente e simples, como cálculo de estatísticas e visualizações.
#Exibindo os Dados: O print(df) exibe o DataFrame no terminal, permitindo que você veja os dados carregados e verifique se tudo foi feito corretamente.

#agora vamos fazer a Análise Estatística (Correlação)
#calcular a correlação entre a idade e a sobrevivência para entender melhor a relação entre essas duas variáveis. A correlação nos ajudará a identificar se existe uma relação linear entre elas.

# Análise Estatística (Correlação)
# Calcular a correlação entre idade e sobrevida
correlacao = df['Idade'].corr(df['Sobrevivencia_Meses'])  # Usando 'df' aqui, em vez de 'dados'
print(f'Correlação entre Idade e Sobrevivência: {correlacao}')

#Como funciona:dados['Idade'].corr(dados['Sobrevivência (meses)']): Calcula a correlação entre as colunas Idade e Sobrevivência (meses).
#O método .corr() calcula o coeficiente de correlação de Pearson, que varia de -1 a 1, indicando a força e a direção da relação linear entre as variáveis.



# Visualizar os Dados
#A visualização de dados ajuda a entender melhor a distribuição e as relações entre as variáveis. Para este passo, vamos gerar gráficos para a Idade e a Sobrevivência (meses), utilizando o Matplotlib e Seaborn.

#Vamos criar:
#Um gráfico de dispersão para visualizar a correlação entre Idade e Sobrevivência.
#Um gráfico de caixa (boxplot) para entender melhor a distribuição das idades e sobrevida.


# Visualizando a correlação com um gráfico de dispersão (scatter plot)
plt.figure(figsize=(8, 6)) # Define o tamanho da figura (gráfico)
sns.scatterplot(x=df['Idade'], y=df['Sobrevivencia_Meses']) # Cria o gráfico de dispersão
plt.title('Relação entre Idade e Sobrevivência (meses)') # Título do gráfico
plt.xlabel('Idade (anos)') # Rótulo do eixo X
plt.ylabel('Sobrevivência (meses)') # Rótulo do eixo Y
plt.grid(True)  # Adiciona uma grade para facilitar a leitura
plt.show()   # Exibe o gráfico

# Visualizando a distribuição da Idade com boxplot - gráfico de caixa
plt.figure(figsize=(8, 6))   #tamanho
sns.boxplot(x=df['Idade'])   #boxplot para a Idade
plt.title('Distribuição da Idade dos Pacientes')  # Título
plt.xlabel('Idade (anos)')     # Rótulo do eixo X
plt.show()  # Exibe o gráfico

# Visualizando a distribuição da Sobrevivência com boxplot
plt.figure(figsize=(8, 6))  #tamanho
sns.boxplot(x=df['Sobrevivencia_Meses'])   #boxplot para a Sobrevivência
plt.title('Distribuição da Sobrevivência dos Pacientes')  # Título do gráfico
plt.xlabel('Sobrevivência (meses)')  # Rótulo do eixo X
plt.show()  # Exibe o gráfico


#Gráfico de Dispersão: Ele mostra como a Idade e a Sobrevivência estão relacionadas visualmente. Se houver alguma tendência (por exemplo, conforme a idade aumenta, a sobrevivência diminui), ela será mais fácil de ser percebida neste gráfico.
#Boxplot: Ele mostra a distribuição das idades e da sobrevivência, destacando a mediana, quartis e possíveis valores atípicos.  sns.boxplot(x=df['Idade']): Cria um boxplot para a Idade. Ele mostra os valores mínimos, máximos, a mediana (valor central) e os quartis (valores que dividem os dados em 4 partes iguais). Ele também pode identificar outliers, que são valores muito distantes da média.



#Salvar os Resultados da Análise
#Agora, vamos salvar os resultados da análise em um arquivo, tanto para a correlação quanto para os gráficos gerados.

#Para isso, vamos:
#Salvar o valor da correlação em um arquivo de texto.
#Salvar os gráficos gerados em arquivos de imagem (formato PNG).

# Salvar a correlação em um arquivo de texto
with open('resultado_correlacao.txt', 'w') as f:      #Abre um arquivo chamado resultado_correlacao.txt para escrita ('w'). Se o arquivo não existir, ele será criado.
    f.write(f'Correlação entre Idade e Sobrevivência: {correlacao}\n')  #Escreve o valor da correlação no arquivo. O valor da variável correlacao é salvo no arquivo de texto.

print("Correlação salva em 'resultado_correlacao.txt'.")

# Salvar os gráficos gerados (gráfico de dispersão e boxplots) como imagens, para que você possa visualizá-los ou compartilhá-los.
# Gráfico de Dispersão
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Idade'], y=df['Sobrevivencia_Meses'])
plt.title('Relação entre Idade e Sobrevivência (meses)')
plt.xlabel('Idade (anos)')
plt.ylabel('Sobrevivência (meses)')
plt.grid(True)
plt.savefig('grafico_correlacao.png')   #Salva o gráfico gerado em um arquivo com o nome especificado. O formato da imagem é PNG.
print("Gráfico de correlação salvo como 'grafico_correlacao.png'.")  #Mostra uma mensagem no terminal indicando que o arquivo foi salvo.

# Boxplot da Idade
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Idade'])
plt.title('Distribuição da Idade dos Pacientes')
plt.xlabel('Idade (anos)')
plt.savefig('grafico_idade.png')
print("Gráfico de distribuição da Idade salvo como 'grafico_idade.png'.")

# Boxplot da Sobrevivência
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Sobrevivencia_Meses'])
plt.title('Distribuição da Sobrevivência dos Pacientes')
plt.xlabel('Sobrevivência (meses)')
plt.savefig('grafico_sobrevivencia.png')
print("Gráfico de distribuição da Sobrevivência salvo como 'grafico_sobrevivencia.png'.")


#Salvar a Correlação: Usamos with open para abrir um arquivo de texto e salvar o valor da correlação. O comando f.write grava o valor no arquivo.

#Salvar os Gráficos: Utilizamos plt.savefig para salvar cada gráfico gerado como uma imagem PNG. Assim, podemos visualizar os resultados mais tarde, fora do código.
