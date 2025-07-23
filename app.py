import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/gabrielbianqui/datathon_FIAP/refs/heads/main/df_prospects_compatibilidade.csv'

@st.cache_data
def load_data(url):
    """Função para carregar os dados de uma URL e guardar em cache."""
    df = pd.read_csv(url)
    # Garante que os IDs sejam tratados como strings para evitar problemas de formatação
    df['codigo_candidato'] = df['codigo_candidato'].astype(str)
    df['codigo_vaga'] = df['codigo_vaga'].astype(str)
    return df

df_prospects = load_data(url)

st.write('# Análise de Compatibilidade Candidato-Vaga')
st.markdown("Use o menu na barra lateral para selecionar o tipo de análise e escolher um ID.")

analysis_type = st.sidebar.radio(
    "1. Escolha o tipo de análise:",
    ('Por Candidato', 'Por Vaga')
)

if analysis_type == 'Por Candidato':
    # Pega a lista de IDs únicos dos candidatos para o selectbox
    lista_ids = df_prospects['codigo_candidato'].unique()
    
    selected_id = st.sidebar.selectbox(
        "2. Selecione o ID do Candidato:",
        options=lista_ids,
        placeholder="Digite ou selecione um ID",
        index=None # Garante que nada seja selecionado por padrão
    )

    if selected_id:
        st.subheader(f"Mostrando vagas para o candidato: {selected_id}")

        # Filtra o dataframe para o candidato escolhido
        df_filtrado = df_prospects[df_prospects['codigo_candidato'] == selected_id]
        
        # Seleciona, renomeia e ordena as colunas para melhor visualização
        df_resultado = (
            df_filtrado[['codigo_vaga', 'compatibilidade']]
            .rename(columns={'codigo_vaga': 'Vaga Aplicada', 'compatibilidade': 'Compatibilidade'})
            .sort_values(by='Compatibilidade', ascending=False)
        )
        
        # Formata a coluna de compatibilidade como porcentagem
        df_resultado['Compatibilidade'] = df_resultado['Compatibilidade']

        st.dataframe(df_resultado, use_container_width=True)

else: # A análise é 'Por Vaga'
    # Pega a lista de IDs únicos das vagas
    lista_ids = df_prospects['codigo_vaga'].unique()

    selected_id = st.sidebar.selectbox(
        "2. Selecione o ID da Vaga:",
        options=lista_ids,
        placeholder="Digite ou selecione um ID",
        index=None
    )

    if selected_id:
        st.subheader(f"Mostrando candidatos para a vaga: {selected_id}")

        # Filtra o dataframe para a vaga escolhida
        df_filtrado = df_prospects[df_prospects['codigo_vaga'] == selected_id]
        
        # Seleciona, renomeia e ordena as colunas
        df_resultado = (
            df_filtrado[['codigo_candidato', 'compatibilidade']]
            .rename(columns={'codigo_candidato': 'Candidato Inscrito', 'compatibilidade': 'Compatibilidade'})
            .sort_values(by='Compatibilidade', ascending=False)
        )
        
        # Formata a coluna de compatibilidade como porcentagem
        df_resultado['Compatibilidade'] = df_resultado['Compatibilidade']
        
        st.dataframe(df_resultado, use_container_width=True)