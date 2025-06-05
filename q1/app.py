import pandas as pd 
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv')

#print (data.head(5))
#print(data.columns.to_list()) 
#data["pickup_borough"].unique()

arrondissements = data['pickup_borough'].unique()
arrondissements = [x if pd.notna(x) else 'nan' for x in arrondissements]

# Affichage avec Streamlit
st.title("Bienvenue sur le site web de Sandrine")

# Liste déroulante
arrondissement_choisie = st.selectbox("Indiquez votre arrondissement de récupération :",arrondissements)

# Images associées aux villes (URL ou chemin local)
images_villes = {
    'Manhattan': 'https://img.freepik.com/photos-gratuite/panorama-du-crepuscule-new-york-city-manhattan_649448-3206.jpg?semt=ais_hybrid&w=740',
    'Queens': 'https://media-cdn.tripadvisor.com/media/photo-s/2e/60/49/46/city-view-terrace.jpg',
    'Brooklyn': 'https://preview.redd.it/brooklyn-bridge-park-nyc-v0-qu9cz6xas8td1.png?auto=webp&s=c83b4f6bef8f6305bfff82f22bd5cdab09309d70',
    'Bronx': 'https://s3.us-east-1.amazonaws.com/bt-prod-img/place/Bronx-NewYork.jpg',
    'nan': 'https://img.freepik.com/photos-premium/point-interrogation-verre-fond-blanc-illustration-3d-isolee_356060-7127.jpg'
}
# Affichage de l’image associée
st.text(f"Tu as choisi : {arrondissement_choisie}")

# Affichage de l’image si disponible
if arrondissement_choisie in images_villes:
    st.image(images_villes[arrondissement_choisie], caption=f"Vue de {arrondissement_choisie}", use_container_width=True)
else:
    st.warning("Aucune image disponible pour cet arrondissement.")
