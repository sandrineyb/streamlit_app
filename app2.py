import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu

from streamlit_authenticator import Authenticate
# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

def accueil():
    st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    authenticator.login("Connexion")

if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"],
            icons = ["house", "images"],
            menu_icon = "cast",
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "container": {"padding": "0 !important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#ff4b4b"}}
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
# ... et ainsi de suite pour les autres pages

# Création de 3 colonnes 
col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

# Contenu de la troisième colonne : 
with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")


# On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", # Question affichée
    ("Email", "Home phone", "Mobile phone") # Options proposées
)

# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    add_radio = st.radio(
        "Choose a shipping method",  # Titre de la question
        ("Standard (5-15 days)", "Express (2-5 days)")  # Choix proposés
    )
