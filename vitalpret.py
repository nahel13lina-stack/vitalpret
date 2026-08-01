import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="VitalPrêt - Plateforme Internationale de Santé et de Solidarité",
    page_icon="🩺",
    layout="wide"
)

DB_FILE = "donnees_vitalpret.json"

def charger_donnees():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"utilisateurs": [], "annonces": [], "bannis": []}

def sauvegarder_donnees(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = charger_donnees()
if "bannis" not in db:
    db["bannis"] = []

translations = {
    "Français": {
        "title": "🩺 VitalPrêt",
        "subtitle": "La plateforme internationale de santé, de solidarité et de gestion de matériel médical.",
        "desc": "Mise en relation globale : 100% gratuit pour les 3 premières annonces des particuliers. Accès payant pour les professionnels.",
        "admin_tab": "Espace Administrateur",
        "user_tab": "Particuliers & Entraide",
        "pro_tab": "Professionnels, Hôpitaux & ONG",
        "alert_config": "Configuration des alertes (WhatsApp & Email)",
        "save_btn": "Enregistrer les préférences"
    },
    "العربية": {
        "title": "🩺 فيتال بري (VitalPrêt)",
        "subtitle": "المنصة الدولية للصحة والتضامن وإدارة المعدات الطبية.",
        "desc": "مجاني تماماً لأول 3 إعلانات للأفراد. وصول مدفوع للمهنيين.",
        "admin_tab": "لوحة تحكم المشرف",
        "user_tab": "الأفراد والتضامن",
        "pro_tab": "المهنيون، المستشفيات والمنظمات",
        "alert_config": "إعدادات التنبيهات (واتساب والبريد الإلكتروني)",
        "save_btn": "حفظ التفضيلات"
    },
    "English": {
        "title": "🩺 VitalPrêt",
        "subtitle": "The international health, solidarity, and medical equipment management platform.",
        "desc": "Free for individuals up to 3 listings. Paid access for professional structures.",
        "admin_tab": "Admin Dashboard",
        "user_tab": "Individuals & Solidarity",
        "pro_tab": "Professionals, Hospitals & NGOs",
        "alert_config": "Alert Configuration (WhatsApp & Email)",
        "save_btn": "Save Preferences"
    },
    "Español": {
        "title": "🩺 VitalPrêt",
        "subtitle": "La plataforma internacional de salud, solidaridad y gestión de material médico.",
        "desc": "Gratis para particulares en sus primeros 3 anuncios. Acceso de pago para profesionales.",
        "admin_tab": "Espacio Administrador",
        "user_tab": "Particulares y Ayuda Mutua",
        "pro_tab": "Profesionales, Hospitales y ONG",
        "alert_config": "Configuración de alertas (WhatsApp y Correo)",
        "save_btn": "Guardar preferencias"
    }
}

# --- BARRE LATÉRALE ---
st.sidebar.title("🌍 Langue / Language")
selected_lang = st.sidebar.selectbox("Choisir la langue / Choose language", list(translations.keys()))
t = translations[selected_lang]

st.sidebar.markdown("---")
st.sidebar.markdown("### 🕒 Horloge Mondiale")
maintenant = datetime.now()
date_str = maintenant.strftime("%d/%m/%Y")
heure_str = maintenant.strftime("%H:%M:%S")
st.sidebar.info(f"📅 **Date:** {date_str}\n\n⏱️ **Heure:** {heure_str}\n\n🌐 **Fuseau:** UTC / Temps Universel")

st.sidebar.markdown("---")
menu = st.sidebar.radio("Navigation", [t["user_tab"], t["pro_tab"], t["admin_tab"]])

if menu == t["user_tab"]:
    st.title(t["title"])
    st.subheader(t["subtitle"])
    st.write(t["desc"])
    st.markdown("---")
    st.success("💡 **Règle Particuliers :** C'est **100% gratuit pour vos 3 premières annonces**. Au-delà de 3 annonces, une participation est demandée pour soutenir le service et la modération.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Rechercher ou Proposer du Matériel")
        with st.form("form_utilisateur"):
            nom = st.text_input("Nom et Prénom")
            adresse = st.text_input("Ville / Adresse (ex: Paris, Alger, Montréal, Maghnia, Madrid...)")
            telephone = st.text_input("Numéro de Téléphone / WhatsApp")
            
            type_action = st.radio("Je souhaite :", ["Proposer du matériel", "Rechercher du matériel"])
            
            categorie_materiel = st.selectbox(
                "Catégorie de matériel :", 
                [
                    "Concentrateur d'oxygène / Appareil respiratoire", 
                    "Fauteuil roulant / Déambulateur", 
                    "Lit médicalisé / Matelas anti-escarres", 
                    "Matériel orthopédique & Attelles (genouillères, colliers cervicaux...)", 
                    "Béquilles / Cannes / Cannes anglaises", 
                    "Tensiomètre / Glucomètre / Matériel de mesure et soins", 
                    "Autre matériel médical"
                ]
            )
            
            nature_offre = st.selectbox("Type de proposition :", ["🟢 Don (Gratuit)", "🔵 Prêt solidaire", "🔴 Vente"])
            disponibilite = st.selectbox("Disponibilité :", ["✅ Disponible immédiatement", "⏳ Sur demande / Bientôt disponible", "❌ Indisponible"])
            
            details = st.text_area("Précisions (état, taille pour les attelles, urgence...)")
            
            submit_user = st.form_submit_button("Valider et enregistrer sur la plateforme")
            
            if submit_user:
                if nom and telephone:
                    # Vérifier si l'utilisateur est banni
                    if nom.strip() in db["bannis"]:
                        st.error("⛔ Ce compte a été banni de la plateforme pour non-respect des règles.")
                    else:
                        annonces_user = sum(1 for u in db["utilisateurs"] if u["nom"].strip().lower() == nom.strip().lower() and u["action"] == "Proposer du matériel")
                        
                        statut_tarif = "Gratuit (Standard)"
                        if type_action == "Proposer du matériel" and annonces_user >= 3:
                            statut_tarif = "Payant (Au-delà de 3 annonces)"
                            st.warning("⚠️ Vous avez atteint vos 3 annonces gratuites. Cette annonce passe sur le forfait de soutien payant.")

                        nouveau_contact = {
                            "nom": nom,
                            "adresse": adresse,
                            "telephone": telephone,
                            "action": type_action,
                            "materiel": f"{categorie_materiel} ({nature_offre})",
                            "disponibilite": disponibilite,
                            "details": details,
                            "tarif": statut_tarif,
                            "date": f"{date_str} à {heure_str}"
                        }
                        db["utilisateurs"].append(nouveau_contact)
                        if type_action == "Proposer du matériel":
                            db["annonces"].append(nouveau_contact)
                        sauvegarder_donnees(db)
                        st.success(f"Merci {nom} ! Votre enregistrement a bien été pris en compte ({statut_tarif}).")
                else:
                    st.error("Veuillez remplir au moins votre nom et votre numéro de téléphone.")

    with col2:
        st.markdown("### 📋 Dernières annonces solidaires")
        if db["annonces"]:
            for ann in reversed(db["annonces"][-5:]):
                st.info(f"**{ann['nom']}** ({ann['adresse']}) — *{ann['materiel']}*\n\n📌 **Statut:** {ann.get('disponibilite', 'N/A')} | 🏷️ *{ann.get('tarif', 'Gratuit')}*\n📞 **Tél:** {ann['telephone']}\n💬 {ann['details']}")
        else:
            st.write("Aucune annonce pour le moment. Soyez le premier à en publier une !")

elif menu == t["pro_tab"]:
    st.title("🏥 Espace Professionnels, Hôpitaux & ONG")
    st.error("💼 **Espace Réservé & Payant** : Cet espace est dédié aux structures de santé, pharmacies, cliniques privées, associations et ONG. L'accès institutionnel est **payant** afin de garantir la pérennité et la sécurité de la plateforme internationale.")
    
    with st.form("form_pro"):
        nom_struct = st.text_input("Nom de l'établissement / Structure / ONG")
        type_struct = st.selectbox("Type", ["Hôpital / Clinique", "Pharmacie / Professionnel", "ONG / Association humanitaire"])
        ville_struct = st.text_input("Ville / Pays")
        contact_struct = st.text_input("Nom du responsable et téléphone / WhatsApp")
        besoin_struct = st.text_area("Besoins ou proposition de partenariat")
        
        submit_pro = st.form_submit_button("Souscrire à l'accès Pro & Rejoindre le réseau")
        if submit_pro:
            if nom_struct and contact_struct:
                if nom_struct.strip() in db["bannis"]:
                    st.error("⛔ Cette structure a été bannie de la plateforme.")
                else:
                    nouveau_pro = {
                        "nom": nom_struct,
                        "adresse": ville_struct,
                        "telephone": contact_struct,
                        "action": f"Structure Pro: {type_struct}",
                        "materiel": besoin_struct,
                        "disponibilite": "Institutionnel",
                        "tarif": "Payant / Pro",
                        "details": "Partenaire officiel abonné",
                        "date": f"{date_str} à {heure_str}"
                    }
                    db["utilisateurs"].append(nouveau_pro)
                    sauvegarder_donnees(db)
                    st.success("Structure Pro enregistrée avec succès ! Redirection vers le module de paiement sécurisé...")
            else:
                st.error("Veuillez remplir les champs obligatoires.")

elif menu == t["admin_tab"]:
    st.title("🔒 Espace Administrateur (Amel)")
    st.write("Bienvenue dans ton centre de pilotage global.")
    
    admin_password = st.text_input("Mot de passe administrateur", type="password")
    
    if admin_password == "Amel2026":
        st.success("Accès autorisé. Voici tes statistiques en temps réel :")
        
        total_inscrits = len(db["utilisateurs"])
        total_annonces = len(db["annonces"])
        structures_pro = sum(1 for u in db["utilisateurs"] if "Structure Pro" in u["action"])
        total_bannis = len(db["bannis"])
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Inscrits", total_inscrits)
        c2.metric("Structures Pro", structures_pro)
        c3.metric("Annonces Actives", total_annonces)
        c4.metric("Utilisateurs Bannis", total_bannis)
        
        st.markdown("---")
        st.subheader("⚠️ Gestion des signalements et des bannissements")
        
        # Formulaire pour bannir un utilisateur par son nom
        with st.form("bannir_form"):
            nom_a_bannir = st.text_input("Nom exact de l'utilisateur ou de la structure à bannir")
            btn_bannir = st.form_submit_button("🚫 Bannir cet utilisateur")
            if btn_bannir:
                if nom_a_bannir:
                    clean_name = nom_a_bannir.strip()
                    if clean_name not in db["bannis"]:
                        db["bannis"].append(clean_name)
                        sauvegarder_donnees(db)
                        st.success(f"L'utilisateur '{clean_name}' a été banni avec succès.")
                    else:
                        st.warning("Cet utilisateur est déjà sur la liste des bannis.")
                else:
                    st.error("Veuillez entrer un nom.")

        # Formulaire pour débannir si besoin
        if db["bannis"]:
            with st.form("debannir_form"):
                nom_a_debannir = st.selectbox("Utilisateurs actuellement bannis :", db["bannis"])
                btn_debannir = st.form_submit_button("✅ Lever le bannissement")
                if btn_debannir:
                    db["bannis"].remove(nom_a_debannir)
                    sauvegarder_donnees(db)
                    st.success(f"Le bannissement de '{nom_a_debannir}' a été levé.")
                    st.rerun()

        st.markdown("---")
        st.subheader("👥 Liste de tous les utilisateurs, inscrits et statuts tarifaires")
        if db["utilisateurs"]:
            for idx, u in enumerate(reversed(db["utilisateurs"]), 1):
                st.write(f"**{idx}. {u['nom']}** — 📍 *{u['adresse']}* — 📞 **{u['telephone']}**")
                st.write(f"   ↳ *Action:* {u['action']} | *Matériel:* {u['materiel']} | *Tarif:* 🏷️ **{u.get('tarif', 'N/A')}** | *Date:* {u.get('date', 'N/A')}")
                st.write(f"   ↳ *Détails:* {u['details']}")
                st.markdown("---")
        else:
            st.write("Aucun utilisateur inscrit pour le moment.")
            
        st.subheader(f"⚙️ {t['alert_config']}")
        with st.form("alert_form"):
            whatsapp_number = st.text_input("Ton numéro WhatsApp", value="+213 559 90 12 73")
            admin_email = st.text_input("Ton adresse e-mail de réception", value="nahel13.lina@gmail.com")
            submitted = st.form_submit_button(t["save_btn"])
            if submitted:
                st.success("Tes préférences sont enregistrées !")
    elif admin_password:
        st.error("Mot de passe incorrect.")

