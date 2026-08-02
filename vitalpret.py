import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    title="VitalPrêt - Plateforme Internationale de Santé et de Solidarité",
    page_icon="🤝",
    layout="large"
)

FICHIER_DB = "donnees_vitalpret.json"

def chargeur_donnees():
    if os.path.exists(FICHIER_DB):
        try:
            with open(FICHIER_DB, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"utilisateurs": [], "annonces": [], "bannis": []}

def sauvegarder_donnees(data):
    with open(FICHIER_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = chargeur_donnees()

# Dictionnaire des traductions
traductions = {
    "Français": {
        "titre_principal": "VitalPrêt - Plateforme Internationale de Santé et de Solidarité",
        "sous_titre": "Mise en relation solidaire pour le matériel médical d'urgence et le partage de soins.",
        "section_materiel": "Demande et Prêt de Matériel Médical",
        "choix_materiel": "Sélectionnez le type de matériel :",
        "options_materiel": ["Concentrateur d'oxygène", "Fauteuil roulant", "Lit médicalisé", "Matériel orthopédique", "Autre matériel"],
        "saisie_autre": "Précisez l'autre matériel recherché :",
        "section_paiement": "Modes de Paiement & Solidarité",
        "info_paiement": "Vous pouvez participer aux frais ou faire un don direct via les coordonnées suivantes :",
        "ccp": "CCP : [Votre Numéro CCP ici]",
        "rib": "Compte Bancaire (RIB) : [Votre RIB ici]",
        "section_installation": "📱 Installer l'application sur votre appareil",
        "texte_installation": "Vous pouvez installer cet outil directement sur votre téléphone, tablette ou ordinateur :",
        "inst_android": "Sur Android (Chrome) : Appuyez sur les trois points, puis choisissez 'Installer l'application'.",
        "inst_iphone": "Sur iPhone / iPad (Safari) : Appuyez sur le bouton de partage, puis sélectionnez 'Sur l'écran d'accueil'.",
        "inst_pc": "Sur Ordinateur : Cliquez sur l'icône d'installation dans la barre d'adresse."
    },
    "Anglais": {
        "titre_principal": "VitalPrêt - International Health & Solidarity Platform",
        "sous_titre": "Solidarity networking for emergency medical equipment and care sharing.",
        "section_materiel": "Medical Equipment Request & Loan",
        "choix_materiel": "Select equipment type:",
        "options_materiel": ["Oxygen concentrator", "Wheelchair", "Medical bed", "Orthopedic equipment", "Other equipment"],
        "saisie_autre": "Please specify the other equipment needed:",
        "section_paiement": "Payment Methods & Solidarity",
        "info_paiement": "You can contribute or make a direct donation using the following details:",
        "ccp": "CCP: [Your CCP Number here]",
        "rib": "Bank Account (RIB): [Your Bank Details here]",
        "section_installation": "📱 Install the app on your device",
        "texte_installation": "You can install this tool directly on your phone, tablet, or computer:",
        "inst_android": "On Android (Chrome): Tap the three dots, then select 'Install app'.",
        "inst_iphone": "On iPhone / iPad (Safari): Tap the share button, then select 'Add to Home Screen'.",
        "inst_pc": "On Computer: Click the install icon in the address bar."
    },
    "Arabe": {
        "titre_principal": "فيتال بري - المنصة الدولية للصحة والتضامن",
        "sous_titre": "ربط تضامني للمعدات الطبية العاجلة ومشاركة الرعاية.",
        "section_materiel": "طلب وإعارة المعدات الطبية",
        "choix_materiel": "اختر نوع المعدات:",
        "options_materiel": ["مكثف الأكسجين", "كرسي متحرك", "سرير طبي", "معدات تقويم العظام", "معدات أخرى"],
        "saisie_autre": "يرجى تحديد المعدات الأخرى المطلوبة:",
        "section_paiement": "طرق الدفع والتضامن",
        "info_paiement": "يمكنك المساهمة أو التبرع مباشرة عبر التفاصيل التالية:",
        "ccp": "رقم البريد الجزائري (CCP): [أدخل رقم الـ CCP هنا]",
        "rib": "الحساب البنكي (RIB): [أدخل تفاصيل الحساب هنا]",
        "section_installation": "📱 تثبيت التطبيق على جهازك",
        "texte_installation": "يمكنك تثبيت هذه الأداة مباشرة على هاتفك أو حاسوبك:",
        "inst_android": "على أندرويد: اضغط على النقاط الثلاث ثم اختر 'تثبيت التطبيق'.",
        "inst_iphone": "على آيفون: اضغط على زر المشاركة ثم 'إضافة إلى الشاشة الرئيسية'.",
        "inst_pc": "على الكمبيوتر: اضغط على رمز التثبيت في شريط العنوان."
    },
    "Allemand": {
        "titre_principal": "VitalPrêt - Internationale Gesundheits- und Solidaritätsplattform",
        "sous_titre": "Solidarische Vernetzung für medizinische Notfallausrüstung.",
        "section_materiel": "Anfrage und Verleih von medizinischer Ausrüstung",
        "choix_materiel": "Wählen Sie den Typ der Ausrüstung:",
        "options_materiel": ["Sauerstoffkonzentrator", "Rollstuhl", "Pflegebett", "Orthopädische Ausrüstung", "Sonstige Ausrüstung"],
        "saisie_autre": "Bitte geben Sie die andere benötigte Ausrüstung an:",
        "section_paiement": "Zahlungsmethoden & Solidarität",
        "info_paiement": "Sie können über die folgenden Daten beitragen oder direkt spenden:",
        "ccp": "CCP: [Ihre CCP-Nummer hier]",
        "rib": "Bankkonto (RIB): [Ihre Bankdaten hier]",
        "section_installation": "📱 App installieren",
        "texte_installation": "Installieren Sie dieses Tool auf Ihrem Gerät:",
        "inst_android": "Auf Android: Tippen Sie auf die drei Punkte und wählen Sie 'App installieren'.",
        "inst_iphone": "Auf iPhone: Tippen Sie auf das Teilen-Symbol und wählen Sie 'Zum Home-Bildschirm'.",
        "inst_pc": "Auf PC: Klicken Sie auf das Installieren-Symbol in der Adressleiste."
    },
    "Russe": {
        "titre_principal": "VitalPrêt - Международная платформа здоровья и солидарности",
        "sous_titre": "Связь для экстренного медицинского оборудования и помощи.",
        "section_materiel": "Запрос и аренда медицинского оборудования",
        "choix_materiel": "Выберите тип оборудования:",
        "options_materiel": ["Кислородный концентратор", "Инвалидная коляска", "Медицинская кровать", "Ортопедическое оборудование", "Другое оборудование"],
        "saisie_autre": "Уточните другое необходимое оборудование:",
        "section_paiement": "Способы оплаты и солидарность",
        "info_paiement": "Вы можете сделать вклад или прямой перевод по следующим реквизитам:",
        "ccp": "CCP: [Ваш номер CCP здесь]",
        "rib": "Банковский счет (RIB): [Ваши реквизиты здесь]",
        "section_installation": "📱 Установить приложение",
        "texte_installation": "Установите этот инструмент на устройство:",
        "inst_android": "На Android: Нажмите три точки и выберите 'Установить приложение'.",
        "inst_iphone": "На iPhone: Нажмите «Поделиться» и выберите 'На экран «Домой»'.",
        "inst_pc": "На ПК: Нажмите значок установки в адресной строке."
    },
    "Mandarin": {
        "titre_principal": "VitalPrêt - 国际健康与守望相助平台",
        "sous_titre": "紧急医疗设备与关怀共享的互助网络。",
        "section_materiel": "医疗设备申请与借用",
        "choix_materiel": "选择设备类型：",
        "options_materiel": ["制氧机", "轮椅", "医用病床", "骨科器材", "其他设备"],
        "saisie_autre": "请说明您需要的其他设备：",
        "section_paiement": "支付方式与爱心捐助",
        "info_paiement": "您可以通过以下信息进行资助或直接捐款：",
        "ccp": "邮政账户 (CCP)：[在此处输入您的CCP]",
        "rib": "银行账户 (RIB)：[在此处输入您的RIB]",
        "section_installation": "📱 在您的设备上安装应用",
        "texte_installation": "您可以直接将此工具安装到手机或电脑上：",
        "inst_android": "安卓手机：点击右上角三个点，选择 '安装应用'。",
        "inst_iphone": "苹果手机：点击分享按钮，选择 '添加到主屏幕'。",
        "inst_pc": "电脑端：点击浏览器地址栏右侧的安装图标。"
    }
}

# Barre latérale pour la sélection de la langue
langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / اللغة", list(traductions.keys()))
t = traductions[langue_choisie]

# En-tête de l'application
st.title(t["titre_principal"])
st.write(t["sous_titre"])

# Affichage de l'heure et date actuelles
maintenant = datetime.now().strftime("%d/%m/%Y à %H:%M")
st.sidebar.markdown(f"📅 **Date & Heure :** {maintenant}")

st.markdown("---")

# Section Gestion du Matériel Médical avec champ libre
st.header(t["section_materiel"])
type_materiel = st.selectbox(t["choix_materiel"], t["options_materiel"])

autre_materiel = ""
if type_materiel == t["options_materiel"][-1]:  
    autre_materiel = st.text_input(t["saisie_autre"])

if st.button("Valider ma démarche"):
    st.success("Votre demande a bien été enregistrée dans le système.")

st.markdown("---")

# Section Paiement / CCP et RIB
st.header(t["section_paiement"])
st.write(t["info_paiement"])
st.info(f"🔹 **{t['ccp']}**\n\n🔹 **{t['rib']}**")

st.markdown("---")

# Section Guide d'Installation de l'application
st.header(t["section_installation"])
st.write(t["texte_installation"])
st.markdown(f"""
- {t['inst_android']}
- {t['inst_iphone']}
- {t['inst_pc']}
""")
