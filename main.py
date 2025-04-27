import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração inicial da página
st.set_page_config(page_title='Análise de Pacientes - Data Storytelling', layout='wide')

# Carregar dados
df = pd.read_csv('health_data.csv')

# Título
st.title('Análise de Pacientes com Doenças Crônicas')
st.write("""
Este projeto analisa o perfil de pacientes diagnosticados com doenças crônicas para identificar padrões de risco e sugerir ações preventivas.
""")

# Visualizações
st.header('Distribuição dos Diagnósticos')
fig1, ax1 = plt.subplots()
df['Diagnosis'].value_counts().plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_ylabel('Número de Pacientes')
st.pyplot(fig1)

st.header('Média de Pressão Sanguínea por Diagnóstico')
fig2, ax2 = plt.subplots()
df.groupby('Diagnosis')['Blood_Pressure'].mean().plot(kind='bar', color='lightgreen', ax=ax2)
ax2.set_ylabel('Pressão Sanguínea Média')
st.pyplot(fig2)

st.header('Média de Colesterol por Diagnóstico')
fig3, ax3 = plt.subplots()
df.groupby('Diagnosis')['Cholesterol_Level'].mean().plot(kind='bar', color='salmon', ax=ax3)
ax3.set_ylabel('Colesterol Médio')
st.pyplot(fig3)

st.header('Distribuição da Idade por Diagnóstico')
fig4, ax4 = plt.subplots(figsize=(10,6))
sns.boxplot(x='Diagnosis', y='Age', data=df, palette='pastel', ax=ax4)
ax4.set_ylabel('Idade')
st.pyplot(fig4)

st.header('Diferenças de Diagnósticos entre Homens e Mulheres')
fig5, ax5 = plt.subplots(figsize=(10,6))
sns.countplot(x='Diagnosis', hue='Gender', data=df, palette='muted', ax=ax5)
ax5.set_ylabel('Número de Pacientes')
st.pyplot(fig5)

# Insights finais
st.header('Conclusões e Insights')
st.write("""
- **Hipertensão** e **Diabetes** são as doenças mais prevalentes.
- Pacientes com **Diabetes** tendem a apresentar **colesterol mais elevado**.
- **Mulheres** apresentam uma incidência ligeiramente maior de **Asma**.
- **Faixa etária acima de 50 anos** é mais vulnerável a doenças crônicas.

**Soluções sugeridas:**
- Incentivar programas de alimentação saudável.
- Promoção de atividade física regular.
- Realização de exames de rotina para detecção precoce.
""")
