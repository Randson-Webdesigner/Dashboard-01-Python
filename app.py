import streamlit as st
import pandas as pd
import plotly.express as px

# Layout da página
st.set_page_config(
    page_title="Dashboard de Vendas",
    layout="wide",  # <- usa a tela toda
    initial_sidebar_state="expanded"
)

# Simula um DataFrame com dados de vendas
df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago"],
    "Região": ["Sul", "Norte", "Sudeste", "Centro-Oeste", "Sul", "Norte", "Sudeste", "Sul"],
    "Vendas": [1500, 1800, 2300, 1200, 2500, 2100, 2400, 2600],
    "Despesas": [800, 900, 1100, 600, 950, 850, 1000, 1200]
})

df["Lucro"] = df["Vendas"] - df["Despesas"]

# ------------------ SIDEBAR ------------------
st.sidebar.title("Filtros")
regioes = st.sidebar.multiselect(
    "Selecione as regiões",
    options=df["Região"].unique(),
    default=df["Região"].unique()
)

# Aplica filtro
df_filtrado = df[df["Região"].isin(regioes)]

# ------------------ TOPO KPIs ------------------
st.title("📊 Dashboard de Vendas - Avançado")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Vendas", f"R$ {df_filtrado['Vendas'].sum():,.2f}")

with col2:
    st.metric("Total de Despesas", f"R$ {df_filtrado['Despesas'].sum():,.2f}")

with col3:
    st.metric("Lucro Total", f"R$ {df_filtrado['Lucro'].sum():,.2f}")

st.markdown("---")

# ------------------ GRÁFICO 1 ------------------
col4, col5 = st.columns(2)

with col4:
    fig1 = px.bar(
        df_filtrado,
        x="Mês",
        y="Vendas",
        color="Região",
        title="📈 Vendas por Mês e Região"
    )
    st.plotly_chart(fig1, use_container_width=True)

# ------------------ GRÁFICO 2 ------------------
with col5:
    fig2 = px.pie(
        df_filtrado,
        names="Região",
        values="Lucro",
        title="🧾 Distribuição de Lucro por Região"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ------------------ TABELA FINAL ------------------
st.markdown("### 📋 Tabela Detalhada")
st.dataframe(df_filtrado, use_container_width=True)
