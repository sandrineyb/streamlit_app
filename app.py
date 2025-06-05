# ------------Importation des modules nécessaires au code-----------
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu 

############Utiliser streamlit_autheticator ou authenticator uniquement avec un fichier dictionnaire !!!!! """
#______________________________________________________________________________________________________________
#______________________________________________________________________________________________________________
# ---------Charger le fichier CSV avant de pouvoir s'authentifier -----------
@st.cache_data                          # Permet de charger le fichier CSV uniquement une seule fois
def fichier_chargement():
    try:
        return pd.read_csv("user.csv")           # Tentative pour charger le fichier CSV	
    except FileNotFoundError:                    # Si le fichier n'existe pas
        st.error("Le fichier est introuvable")      # Affiche un message d'erreur
        return pd.DataFrame()                    # Retourne un DataFrame vide
    except pd.errors.EmptyDataError:             # Si le fichier est vide
        st.error("Le fichier 'user.csv' est vide")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Une erreur s'est produite lors du chargement du fichier 'user.csv': {e}")
        return pd.DataFrame()
    

# Fonction pour vérifier si l'utilisateur existe dans le fichier
def verifier_utilisateur(nom, mot_de_passe, df):
    for _, row in df.iterrows():            # Iterrows => Parcourir chaque ligne du fichier
        if row['name'] == nom and row['password'] == mot_de_passe:
            return True                     # Identifiants valides
    return False                            # Sinon, identifiants incorrects

# Chargement du fichier CSV
df = fichier_chargement() 


# Création de la page d'affichage principale
st.title("Animaux Lovers")
    
# Initialiser la session / st.session_state garde en mémoire les valeurs entre le rechargement de la page
if "connecte" not in st.session_state: # Si la variable "connecte" n'est pas dans la session
    st.session_state["connecte"] = False # Initialiser la variable "connecte" comme non connecté
if "utilisateur" not in st.session_state:
    st.session_state["utilisateur"] = ""

# ---------------- FORMULAIRE DE CONNEXION ----------------
if not st.session_state["connecte"]:
    st.subheader("Authentification")

    nom = st.text_input("Nom d'utilisateur")
    mdp = st.text_input("Mot de passe", type="password")

    col1, col2, col3 = st.columns(3)
    # Bouton de connexion si cliquer 
    with col1:
        if st.button("Connexion"):
            if verifier_utilisateur(nom, mdp, df):
                st.success("Connexion réussie ")
                st.session_state["connecte"] = True
                st.session_state["utilisateur"] = nom
                #st.rerun() # Recharge la page après connexion
            else:
                st.error("Identifiants incorrects")
    with col2:
    # Bouton d'inscription si cliquer
        if st.button("Inscription"):
            st.session_state["connecte"] = False
            st.session_state["utilisateur"] = ""
            st.info("Fonction non encore disponible.")            
            #st.rerun()

    # Bouton de mot de passe oublé si cliquer
    with col3:
        if st.button("Mot de passe oublié"):
            st.session_state["connecte"] = False
            st.session_state["utilisateur"] = ""
            st.info("Fonction non encore disponible.")
            #st.rerun()
else:
    # ----------------------SIDEBAR ----------------------
    with st.sidebar:           # Grouper plusieurs éléments dans la sidebar
        st.title(f"Bienvenue {st.session_state['utilisateur']}")
        selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Albums Photos", "Déconnexion"]
                    )
            # ---------------------- DECONNEXION ----------------------
        if selection  == "Déconnexion":
            st.success("Déconnexion réussie")
            st.session_state["connecte"] = False
            st.session_state["utilisateur"] = ""
            #st.rerun()
            # ---------------------- ACCUEIL ----------------------
    if selection == "Accueil":
        st.write("Bienvenue sur ta page d'accueil")
        st.image("https://scontent.fcdg3-1.fna.fbcdn.net/v/t39.30808-6/492734127_1229536465841636_3814169372039668021_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=x0ZiJOmg_04Q7kNvwF6tk17&_nc_oc=AdkDgpyp-xvrWtkk_OTcHL1gl5gaNOHIYtffSKdLXKiUFZBvGXpMgbSQFE84ATe-gTg&_nc_zt=23&_nc_ht=scontent.fcdg3-1.fna&_nc_gid=ctsnr_hjz5pkVfg4OkmDdA&oh=00_AfNsI32mkNJA0CGEYOBuNlm-WTbVDkhjChyb6amZSO-CEA&oe=68473122")

        # ---------------------- ALBUMS PHOTOS ----------------------
    elif selection == "Albums Photos":
        st.write("Bienvenue sur votre album photo")
                
            ## Page "album photo des animaux" ##
            # A noter les images doivent être  afficher sur chaque ligne 3 photos.
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")
        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")
        