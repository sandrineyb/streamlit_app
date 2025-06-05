
import streamlit as st
import pandas as pd
from datetime import date, time

st.write("Hello World")

# Titre principal de l'application (affiché en haut de la page)
st.title("The title of my page")

# Titre de section important (taille 1)
st.header("An Important Header")

# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("A Secondary Header")

# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text("My classic text")

# Affiche du texte avec mise en forme Markdown
st.markdown(''':rainbow: :rainbow[My markdown]''')  # Ici, un effet arc-en-ciel est appliqué

# Affiche un dataframe (st.write accepte plusieurs arguments et plusieurs types de données)
st.write(
    pd.DataFrame({
            "Cards": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
            "Quantity": [0, 1, 0, 3]}
    )
)

# La commande st.checkbox vous permet d’afficher une case à cocher. Plusieurs checkbox peuvent être cocher en même temps.
st.checkbox(label = "Tu es incollable sur l'univers du Roi lion.") # label : paramètre (facultatif à écrire) qui permet d'afficher le contenu associé 
st.write('___')  # Ligne de séparation pour aérer l’interface visuellement.

# La commande radio permet à l'utilisateur de choisir UNE seule réponse parmi plusieurs propositions.
st.radio("Est-ce que Le Roi lion est le meilleur Disney ?", 
         ['Oui !', 'Evidemment !', 'La question ne se pose même pas.']) #Les réponses possibles sont stockées dans une liste 
st.write('___')

# Un interrupteur (toggle). Il s’agit d’un bouton on/off. 
st.toggle("Tu as vu Le Roi lion", value=True) #Ici, il est activé par défaut (value=True).
st.write('___')

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
st.selectbox("Qui a tué Mufasa ?",
             ['Simba', 'Scar', 'Zazu']) 
st.write('___')

# Une liste à choix multiples. L’utilisateur peut sélectionner plusieurs réponses à la fois.
st.multiselect("Quels sont vos personnages favoris ?", 
               ['Simba', 'Mufasa', 'Scar', 'Nala']) 
st.write('___')

# Un curseur avec des valeurs textuelles. L’utilisateur choisit son appréciation du film.
st.select_slider("Donnez votre appréciation sur le Roi lion", 
                 ['Mauvais', 'Bon', 'Excellent'], 
                 value='Excellent') # Paramètre permettant de positiionner le curseur par défaut sur "Excellent"


st.text_input("Quel est le titre de votre film favori ?", "Le Roi lion :D")

st.text_area("Peux-tu expliquer pourquoi c'est ton film favori")

""" Les entrées utilisateurs numériques

Il existe deux types de champs numériques dans Streamlit : st.number_input et st.slider.

La commande st.number_input permet à l’utilisateur de rentrer une valeur numérique. De plus, deux boutons sont ajoutés permettant d’augmenter ou de diminuer directement la valeur. Il est possible de définir les bornes minimales et maximales en utilisant respectivement les paramètres min_value et max_value. Le paramètre step permet de changer l’intervalle entre les valeurs.

La commande st.slider fonctionne comme st.select_slider sauf qu’il n’accepte que les types : int, float, date, time et datetime.
Exemple :"""
st.number_input("Tu en possèdes :", min_value=0)
st.slider("Sélectionnez la plage de date :",
           min_value=1923,
           max_value=date.today().year,
           value=(1923, date.today().year)
          )

"""Les entrées utilisateurs Date et Time

Il existe deux types de champs temporels dans Streamlit : st.date_input et st.time_input. Ces derniers fonctionnent comme une st.selectbox sauf qu’ils proposent respectivement un calendrier et une heure.
Exemple :"""
st.date_input("Sélectionnez votre date de naissance")

st.time_input("Configurez une alarme à ", time(7, 30))

# La récupération des données entrées utilisateurs

#Streamlit permet de collecter et de traiter les entrées utilisateurs à l'aide de variables. Vous pouvez ainsi stocker ces données et les réutiliser dans le reste de votre script Streamlit.
# Exemple :

st.text('TODO list')
task1 = st.checkbox("Lire un livre")
task2 = st.checkbox("Développer mes projets")
task3 = st.checkbox("Me promener")

st.write("\n\n")

if task1 and task2 and task3:
    st.write("Bravo, tu as réalisé tous tes objectifs du moment. :sunglasses:")
elif task1 or task2 or task3:
    st.write("Tu es sur la bonne voie, continue comme ça. :smile:")
else:
    st.write("Tu dois revoir tes priorités, " \
    "tu n'as encore réalisé aucunes de tes tâches. :pleading:")

    """Ajouter des médias
Il est facile d'intégrer des images, des vidéos et des fichiers audios directement dans vos applications Streamlit.
1. Les images
La commande st.image vous permet d’afficher une image ou une liste d’images. Le chemin de l’image peut être relatif (en local sur votre ordinateur) ou un lien URL.
Exemple :
    """
    st.image("logo.png") 

""". Les vidéos

La commande st.video, vous permet d’afficher un lecteur vidéo. Le chemin de la vidéo peut être relatif (en local sur votre ordinateur) ou un lien URL.
Exemple :"""

video_file = open("video.mp4", "rb") 
video_bytes = video_file.read()

st.video(video_bytes) 

"""3. Les fichiers audios

La commande st.audio, vous permet d’afficher un lecteur audio. Vous pouvez lui passer directement le fichier ou l’encoder comme pour l’exemple précédent avec la vidéo.
Exemple :
""" 
st.audio("music.mp3")

st.subheader("Voici un DataFrame interactif :")
st.dataframe(data)  # DataFrame scrollable et interactif

st.subheader("Ou une table statique :")
st.table(data)  # Affichage statique, pas de scroll