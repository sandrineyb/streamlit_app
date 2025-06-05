# Importer les bibliothèques qui nous seront nécessaires
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement des datasets
st.title("Manipulation des données et création de graphiques")
datasets = {
    "flights": sns.load_dataset("flights"),
    "tips": sns.load_dataset("tips"),
    "iris": sns.load_dataset("iris")
}
# Changer le type de la colonne year en format date et choisir le dataset
#datasets["flights"]['year'] = pd.to_datetime(datasets["flights"]['year'], format='%Y')

selected_dataset = st.selectbox("Quel dataset veux-tu utiliser :", options=list(datasets.keys()))
df = datasets[selected_dataset]
if selected_dataset == "flights":
    df = df.sort_values(by='year')

# st.write("Aperçu du dataset sélectionné :")
st.dataframe(df)

# Sélectionner les colonnes X et Y
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
all_cols = df.columns.tolist()

x_col = st.selectbox("Choisissez la colonne X :", options=all_cols)
y_col = st.selectbox("Choisissez la colonne Y :", options= all_cols)

# Sélectionner le type de graphique
chart_type = st.selectbox("Quel type de graphique veux-tu utiliser :", ["scatter_chart", "bar_chart", "line_chart"])

# Affichage du graphique
st.subheader("Graphique")

try:
    data_to_plot = df[[x_col, y_col]].dropna()

    if chart_type == "scatter_chart":
        st.scatter_chart(df,x=x_col,y=y_col)
    elif chart_type == "bar_chart":
        st.bar_chart(df,x=x_col,y=y_col)
    elif chart_type == "line_chart":
        st.line_chart(df,x=x_col,y=y_col)
except Exception as e:
    st.error(f"Erreur lors de la génération du graphique : {e}")

# Matrice de corrélation
show_corr = st.checkbox("Afficher la matrice de corrélation (variables numériques)")

if show_corr:
    st.subheader("Matrice de corrélation")
    corr = df.select_dtypes(include=np.number).corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='rocket', ax=ax)
    st.pyplot(fig)
