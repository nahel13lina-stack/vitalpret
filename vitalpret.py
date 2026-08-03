import streamlit as st
import json
import os
from datetime import datetime, date

st.set_page_config(
    page_title="VitalPrêt - Plateforme Internationale de Santé et de Solidarité",
    page_icon="🤝",
    layout="wide"
)
# Code CSS pour embellir l'interface
st.markdown("""
    <style>
    .stApp {
        background-color: #f7fafc;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3182ce, #2b6cb0);
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #2b6cb0, #2c5282);
    }
    </style>
""", unsafe_allow_html=True)
# Titre captivant
st.markdown("""
    <div style='background: linear-gradient(135deg, #2b6cb0, #2c7a7b); padding: 25px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px;'>
        <h1 style='color: white; margin: 0; font-size: 32px;'>🩺 VitalPrêt — Solidarité & Santé 🤝</h1>
        <p style='font-size: 16px; margin-top: 10px; opacity: 0.9;'>Plateforme internationale de mise en relation pour le matériel médical d'urgence, le partage et le prêt.</p>
    </div>
""", unsafe_allow_html=True)
FICHIER_DB = "donnees_vitalpret.json"
CODE_ADMIN = "amel2026" # Mot de passe admin configuré

def chargeur_donnees():
    if os.path.exists(FICHIER_DB):
        try:
            with open(FICHIER_DB, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"utilisateurs": [], "annonces": [], "bannis": [], "notifications": []}

def sauvegarder_donnees(data):
    with open(FICHIER_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = chargeur_donnees()

# Dictionnaire complet des traductions incluant la liste élargie du matériel
traductions = {
    "Français": {
        "titre_principal": "VitalPrêt - Plateforme Internationale de Santé et de Solidarité",
        "sous_titre": "Mise en relation solidaire pour le matériel médical d'urgence, le partage, le prêt ou la vente.",
        "section_notif": "🔔 Centre de Notifications en Direct",
        "aucune_notif": "Aucune nouvelle notification pour le moment.",
        "section_compte": "Type de Compte",
        "choix_compte": "Sélectionnez votre profil :",
        "options_compte": ["Particulier", "Professionnel / Association / Pharmacie / ONG"],
        "section_materiel": "Gestion du Matériel Médical & Type de Transaction",
        "choix_transaction": "Sélectionnez la nature de l'offre / demande :",
        "options_transaction": ["Don", "Prêt", "Vente", "Aide financière / Don direct"],
        "choix_materiel": "Sélectionnez le type de matériel :",
        "options_materiel": [
            "Concentrateur d'oxygène", 
            "Fauteuil roulant", 
            "Lit médicalisé", 
            "Matériel orthopédique", 
            "Attelles", 
            "Bouteille d'oxygène / Manodétendeur",
            "Déambulateur / Cannes anglaises",
            "Tensiomètre / Matériel de diagnostic",
            "Pousse-seringue / Matériel perfusion",
            "Matelas anti-escarres",
            "Autre matériel"
        ],
        "saisie_autre": "Précisez l'autre matériel recherché ou proposé :",
        "section_disponibilite": "📅 Disponibilité du Matériel",
        "choix_statut_dispo": "État de disponibilité :",
        "options_statut_dispo": ["Disponible immédiatement", "Disponible à partir d'une date précise", "Indisponible / Actuellement réservé ou pris"],
        "date_dispo": "Choisissez la date de disponibilité :",
        "section_coordonnees": "Vos Coordonnées et Message",
        "nom": "Nom / Prénom ou Nom de l'Association / Pharmacie :",
        "ville_pays": "Ville et Pays :",
        "contact": "Téléphone ou Email de contact :",
        "message": "Précisez votre situation ou vos besoins :",
        "btn_valider": "Valider ma démarche",
        "section_paiement": "Modes de Paiement & Solidarité (Requis après 3 publications ou pour les Pros)",
        "info_paiement": "Au-delà de 3 publications, ou pour les structures professionnelles (ONG, pharmacies), une participation financière est requise via les coordonnées ci-dessous :",
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
        "sous_titre": "Solidarity networking for emergency medical equipment, sharing, loan or sale.",
        "section_notif": "🔔 Live Notification Center",
        "aucune_notif": "No new notifications at the moment.",
        "section_compte": "Account Type",
        "choix_compte": "Select your profile:",
        "options_compte": ["Individual", "Professional / Association / Pharmacy / NGO"],
        "section_materiel": "Medical Equipment Management & Transaction Type",
        "choix_transaction": "Select the nature of the offer / request:",
        "options_transaction": ["Donation", "Loan", "Sale", "Financial aid / Direct donation"],
        "choix_materiel": "Select equipment type:",
        "options_materiel": ["Oxygen concentrator", "Wheelchair", "Medical bed", "Orthopedic equipment", "Splints / Braces", "Oxygen tank", "Walker / Crutches", "Blood pressure monitor", "Other equipment"],
        "saisie_autre": "Please specify the other equipment needed or offered:",
        "section_disponibilite": "📅 Equipment Availability",
        "choix_statut_dispo": "Availability status:",
        "options_statut_dispo": ["Available immediately", "Available from a specific date", "Unavailable / Currently reserved or taken"],
        "date_dispo": "Select availability date:",
        "section_coordonnees": "Your Contact Details and Message",
        "nom": "Name / Organization Name:",
        "ville_pays": "City and Country:",
        "contact": "Phone or Email contact:",
        "message": "Specify your situation or needs:",
        "btn_valider": "Validate my request",
        "section_paiement": "Payment Methods & Solidarity (Required after 3 posts or for Pros)",
        "info_paiement": "Beyond 3 publications, or for professional structures (NGOs, pharmacies), a financial contribution is required via the details below:",
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
        "sous_titre": "ربط تضامني للمعدات الطبية العاجلة والمشاركة، الإعارة أو البيع.",
        "section_notif": "🔔 مركز الإشعارات المباشرة",
        "aucune_notif": "لا توجد إشعارات جديدة في الوقت الحالي.",
        "section_compte": "نوع الحساب",
        "choix_compte": "اختر ملفك الشخصي:",
        "options_compte": ["فرد (خاص)", "مهني / جمعية / صيدلية / منظمة غير حكومية"],
        "section_materiel": "إدارة المعدات الطبية ونوع المعاملة",
        "choix_transaction": "اختر طبيعة العرض / الطلب:",
        "options_transaction": ["تبرع", "إعارة", "بيع", "مساعدة مالية / تبرع مباشر"],
        "choix_materiel": "اختر نوع المعدات:",
        "options_materiel": ["مكثف الأكسجين", "كرسي متحرك", "سرير طبي", "معدات تقويم العظام", "جبائر / attelles", "قارورة أكسجين", "مشاية / عكاكيز", "جهاز قياس الضغط", "معدات أخرى"],
        "saisie_autre": "يرجى تحديد المعدات الأخرى المطلوبة أو المعروضة:",
        "section_disponibilite": "📅 توفر المعدات",
        "choix_statut_dispo": "حالة التوفر:",
        "options_statut_dispo": ["متوفر حاليا فوريا", "متوفر ابتداء من تاريخ محدد", "غير متوفر / محجوز حاليا"],
        "date_dispo": "اختر تاريخ التوفر:",
        "section_coordonnees": "معلومات الاتصال والرسالة الخاصة بك",
        "nom": "الاسم واللقب أو اسم الجمعية / الصيدلية:",
        "ville_pays": "المدينة والبلد:",
        "contact": "رقم الهاتف أو البريد الإلكتروني للاتصال:",
        "message": "وضح حالتك أو احتياجاتك:",
        "btn_valider": "تأكيد طلبي",
        "section_paiement": "طرق الدفع والتضامن (مطلوبة بعد 3 منشورات أو للطرف المهني)",
        "info_paiement": "أكثر من 3 منشورات، أو بالنسبة للجهات المهنية (الصيدليات، المنظمات)، يتطلب الأمر مساهمة مالية عبر التفاصيل أدناه:",
        "ccp": "رقم البريد الجزائري (CCP): [أدخل رقم الـ CCP هنا]",
        "rib": "الحساب البنكي (RIB): [أدخل تفاصيل الحساب هنا]",
        "section_installation": "📱 تثبيت التطبيق على جهازك",
        "texte_installation": "يمكنك تثبيت هذه الأداة مباشرة على هاتفك أو حاسوبك:",
        "inst_android": "على أندرويد: اضغط على النقاط الثلاث ثم اختر 'تثبيت التطبيق'.",
        "inst_iphone": "على آيفون: اضغط على زر المشاركة ثم 'إضافة إلى الشاشة الرئيسية'.",
        "inst_pc": "على الكمبيوتر: اضغط على رمز التثبيت في شريط العنوان."
    },
    "Espagnol": {
        "titre_principal": "VitalPrêt - Plataforma Internacional de Salud y Solidaridad",
        "sous_titre": "Red de solidaridad para equipos médicos de emergencia, compartición, préstamo o venta.",
        "section_notif": "🔔 Centro de Notificaciones en Vivo",
        "aucune_notif": "No hay nuevas notificaciones por el momento.",
        "section_compte": "Tipo de Cuenta",
        "choix_compte": "Seleccione su perfil:",
        "options_compte": ["Particular", "Profesional / Asociación / Farmacia / ONG"],
        "section_materiel": "Gestión de Material Médico y Tipo de Transacción",
        "choix_transaction": "Seleccione la naturaleza de la oferta / solicitud:",
        "options_transaction": ["Donación", "Préstamo", "Venta", "Ayuda financiera / Donación directa"],
        "choix_materiel": "Seleccione el tipo de material:",
        "options_materiel": ["Concentrador de oxígeno", "Silla de ruedas", "Cama médica", "Material ortopédico", "Férulas / Attelles", "Bombona de oxígeno", "Andador / Muletas", "Otro material"],
        "saisie_autre": "Especifique el otro material necesario u ofrecido:",
        "section_disponibilite": "📅 Disponibilidad del Material",
        "choix_statut_dispo": "Estado de disponibilidad:",
        "options_statut_dispo": ["Disponible inmediatamente", "Disponible a partir de una fecha específica", "No disponible / Actualmente reservado"],
        "date_dispo": "Elija la fecha de disponibilidad:",
        "section_coordonnees": "Sus Datos de Contacto y Mensaje",
        "nom": "Nombre y Apellidos o Nombre de la Asociación / Farmacia:",
        "ville_pays": "Ciudad y País:",
        "contact": "Teléfono o Correo electrónico de contacto:",
        "message": "Especifique su situación o necesidades:",
        "btn_valider": "Validar mi solicitud",
        "section_paiement": "Métodos de Pago y Solidaridad (Requerido tras 3 publicaciones o para Profesionales)",
        "info_paiement": "Más allá de 3 publicaciones, o para estructuras profesionales (ONG, farmacias), se requiere una aportación a través de los datos siguientes:",
        "ccp": "CCP: [Su número CCP aquí]",
        "rib": "Cuenta Bancaria (RIB): [Su datos bancarios aquí]",
        "section_installation": "📱 Instalar la aplicación en su dispositivo",
        "texte_installation": "Puede instalar esta herramienta directamente en su teléfono, tableta o computadora:",
        "inst_android": "En Android (Chrome): Toque los tres puntos y seleccione 'Instalar aplicación'.",
        "inst_iphone": "En iPhone / iPad (Safari): Toque el botón compartir y seleccione 'Añadir a la pantalla de inicio'.",
        "inst_pc": "En Computadora: Haga clic en el icono de instalación en la barra de direcciones."
    },
    "Allemand": {
        "titre_principal": "VitalPrêt - Internationale Gesundheits- und Solidaritätsplattform",
        "sous_titre": "Solidarische Vernetzung für medizinische Notfallausrüstung, Verleih oder Verkauf.",
        "section_notif": "🔔 Live-Benachrichtigungscenter",
        "aucune_notif": "Keine neuen Benachrichtigungen im Moment.",
        "section_compte": "Kontotyp",
        "choix_compte": "Wählen Sie Ihr Profil:",
        "options_compte": ["Privatperson", "Gewerblich / Verein / Apotheke / NGO"],
        "section_materiel": "Verwaltung medizinischer Ausrüstung & Transaktionsart",
        "choix_transaction": "Wählen Sie die Art der Aktion:",
        "options_transaction": ["Spende", "Verleih", "Verkauf", "Finanzielle Hilfe / Direkte Spende"],
        "choix_materiel": "Wählen Sie den Typ der Ausrüstung:",
        "options_materiel": ["Sauerstoffkonzentrator", "Rollstuhl", "Pflegebett", "Orthopädische Ausrüstung", "Schienen / Attelles", "Sauerstoffflasche", "Gehwagen / Krücken", "Sonstige Ausrüstung"],
        "saisie_autre": "Bitte geben Sie die andere benötigte oder angebotene Ausrüstung an:",
        "section_disponibilite": "📅 Verfügbarkeit der Ausrüstung",
        "choix_statut_dispo": "Verfügbarkeitsstatus:",
        "options_statut_dispo": ["Sofort verfügbar", "Verfügbar ab einem bestimmten Datum", "Nicht verfügbar / Derzeit reserviert"],
        "date_dispo": "Wählen Sie das Verfügbarkeitsdatum:",
        "section_coordonnees": "Ihre Kontaktdaten und Nachricht",
        "nom": "Name / Name des Vereins / Apotheke:",
        "ville_pays": "Stadt und Land:",
        "contact": "Telefon oder E-Mail-Kontakt:",
        "message": "Beschreiben Sie Ihre Situation oder Ihren Bedarf:",
        "btn_valider": "Anfrage bestätigen",
        "section_paiement": "Zahlungsmethoden & Solidarität (Erforderlich nach 3 Beiträgen oder für Profis)",
        "info_paiement": "Nach 3 Beiträgen oder für gewerbliche Strukturen ist ein Beitrag über die folgenden Daten erforderlich:",
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
        "sous_titre": "Связь для экстренного медицинского оборудования, аренды или продажи.",
        "section_notif": "🔔 Центр живых уведомлений",
        "aucune_notif": "Нет новых уведомлений на данный момент.",
        "section_compte": "Тип аккаунта",
        "choix_compte": "Выберите ваш профиль:",
        "options_compte": ["Частное лицо", "Профессионал / Ассоциация / Аптека / НПО"],
        "section_materiel": "Управление оборудованием и тип сделки",
        "choix_transaction": "Выберите тип действия:",
        "options_transaction": ["Пожертвование", "Аренда", "Продажа", "Финансовая помощь / Прямое пожертвование"],
        "choix_materiel": "Выберите тип оборудования:",
        "options_materiel": ["Кислородный концентратор", "Инвалидная коляска", "Медицинская кровать", "Ортопедическое оборудование", "Шины / Attelles", "Кислородный баллон", "Ходунки / Костыли", "Другое оборудование"],
        "saisie_autre": "Уточните другое необходимое или предлагаемое оборудование:",
        "section_disponibilite": "📅 Доступность оборудования",
        "choix_statut_dispo": "Статус доступности:",
        "options_statut_dispo": ["Доступно немедленно", "Доступно с определенной даты", "Недоступно / Зарезервировано"],
        "date_dispo": "Выберите дату доступности:",
        "section_coordonnees": "Ваши контактные данные и сообщение",
        "nom": "ФИО или название организации / аптеки:",
        "ville_pays": "Город и страна:",
        "contact": "Телефон или email для связи:",
        "message": "Укажите вашу ситуацию или потребности:",
        "btn_valider": "Подтвердить запрос",
        "section_paiement": "Способы оплаты и солидарность (Требуется после 3 публикаций или для профи)",
        "info_paiement": "Свыше 3 публикаций или для профессиональных структур требуется платеж по следующим реквизитам:",
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
        "sous_titre": "紧急医疗设备共享、借用、租赁或出售的互助网络。",
        "section_notif": "🔔 实时通知中心",
        "aucune_notif": "目前没有新的通知。",
        "section_compte": "账户类型",
        "choix_compte": "选择您的身份：",
        "options_compte": ["个人用户", "专业人员 / 协会 / 药房 / 非政府组织"],
        "section_materiel": "医疗设备管理与交易类型",
        "choix_transaction": "选择操作性质：",
        "options_transaction": ["捐赠", "借用", "出售", "经济援助 / 直接捐款"],
        "choix_materiel": "选择设备类型：",
        "options_materiel": ["制氧机", "轮椅", "医用病床", "骨科器材", "支具 / Attelles", "氧气瓶", "助行器 / 拐杖", "其他设备"],
        "saisie_autre": "请说明您需要或提供的其他设备：",
        "section_disponibilite": "📅 设备可用性",
        "choix_statut_dispo": "可用状态：",
        "options_statut_dispo": ["即时可用", "从特定日期起可用", "不可用 / 目前已预订"],
        "date_dispo": "选择可用日期：",
        "section_coordonnees": "您的联系方式与留言",
        "nom": "姓名或机构 / 药房名称：",
        "ville_pays": "城市与国家：",
        "contact": "联系电话或邮箱：",
        "message": "请说明您的具体情况或需求：",
        "btn_valider": "确认提交",
        "section_paiement": "支付方式与爱心捐助（超过3次发布或专业用户必需）",
        "info_paiement": "超过3条发布记录，或针对专业机构（药房、NGO），需通过以下信息进行费用结算：",
        "ccp": "邮政账户 (CCP)：[在此处输入您的CCP]",
        "rib": "银行账户 (RIB)：[在此处输入您的RIB]",
        "section_installation": "📱 在您的设备上安装应用",
        "texte_installation": "您可以直接将此工具安装到手机或电脑上：",
        "inst_android": "安卓手机：点击右上角三个点，选择 '安装应用'。",
        "inst_iphone": "苹果手机：点击分享按钮，选择 '添加到主屏幕'。",
        "inst_pc": "电脑端：点击浏览器地址栏右侧的安装图标。"
    }
}

# Barre latérale pour la sélection de la langue et l'accès Administrateur
langue_choisie = st.sidebar.selectbox("🌐 Langue / Language / Idioma / اللغة", list(traductions.keys()))
t = traductions[langue_choisie]

st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Espace Administrateur (Amel)")
mot_de_passe_saisi = st.sidebar.text_input("Mot de passe admin", type="password")

# En-tête de l'application
st.title(t["titre_principal"])
st.write(t["sous_titre"])

# Affichage de l'horloge
maintenant = datetime.now().strftime("%d/%m/%Y à %H:%M")
st.sidebar.markdown(f"📅 **Date & Heure :** {maintenant}")

# Fonction pour attribuer une couleur selon le type de transaction
def obtenir_pastille_couleur(transaction):
    trans_lower = transaction.lower()
    if "don" in trans_lower and "aide" not in trans_lower:
        return "🟢" # Vert pour Don
    elif "prêt" in trans_lower or "loan" in trans_lower or "إعارة" in trans_lower or "préstamo" in trans_lower or "verleih" in trans_lower or "аренда" in trans_lower or "借用" in trans_lower:
        return "🔵" # Bleu pour Prêt
    elif "vente" in trans_lower or "sale" in trans_lower or "بيع" in trans_lower or "venta" in trans_lower or "verkauf" in trans_lower or "продажа" in trans_lower or "出售" in trans_lower:
        return "🟠" # Orange pour Vente
    else:
        return "🟣" # Violet pour Aide financière / Autre

# Gestion de l'espace Administrateur avec le mot de passe exact 'amel2026'
if mot_de_passe_saisi == CODE_ADMIN:
    st.sidebar.success("✅ Connecté en tant qu'Administrateur")
    st.markdown("---")
    st.header("🛠️ Panneau de Contrôle Administrateur")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Liste des Annonces / Inscrits")
        if db["annonces"]:
            for idx, ann in enumerate(db["annonces"]):
                pastille = obtenir_pastille_couleur(ann['transaction'])
                dispo_info = f"Dispo: {ann.get('disponibilite', 'Immédiate')}"
                st.write(f"**{idx+1}. [{ann['type_compte']}]** {ann['nom']} ({ann['ville_pays']}) - {pastille} *{ann['transaction']} : {ann['materiel']}* | 🕒 {dispo_info} (Contact: {ann['contact']})")
        else:
            st.write("Aucune annonce enregistrée pour le moment.")
            
    with col2:
        st.subheader("🚫 Gestion des Bannissements")
        st.write("Utilisateurs actuellement bannis :", db["bannis"] if db["bannis"] else "Aucun")
        
        contact_a_gerer = st.text_input("Entrer le contact (Email/Téléphone) à bannir ou débannir :")
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("Bannir cet utilisateur"):
                if contact_a_gerer and contact_a_gerer not in db["bannis"]:
                    db["bannis"].append(contact_a_gerer)
                    sauvegarder_donnees(db)
                    st.success(f"L'utilisateur {contact_a_gerer} a été banni.")
                else:
                    st.warning("Contact invalide ou déjà banni.")
        with col_b2:
            if st.button("Débannir cet utilisateur"):
                if contact_a_gerer in db["bannis"]:
                    db["bannis"].remove(contact_a_gerer)
                    sauvegarder_donnees(db)
                    st.success(f"L'utilisateur {contact_a_gerer} a été débannit.")
                else:
                    st.warning("Ce contact n'est pas dans la liste des bannis.")
    st.markdown("---")

# Section Centre de Notifications en Direct
st.header(t["section_notif"])
if db["notifications"]:
    for notif in reversed(db["notifications"][-5:]):
        st.info(f"📢 **[{notif['date']}]** {notif['texte']}")
else:
    st.write(t["aucune_notif"])

st.markdown("---")

# Section Type de Compte
st.header(t["section_compte"])
type_compte = st.radio(t["choix_compte"], t["options_compte"])

st.markdown("---")

# Section Gestion du Matériel élargie et Nature de la Transaction
st.header(t["section_materiel"])
type_transaction = st.selectbox(t["choix_transaction"], t["options_transaction"])
type_materiel = st.selectbox(t["choix_materiel"], t["options_materiel"])

autre_materiel = ""
if type_materiel == t["options_materiel"][-1]:  
    autre_materiel = st.text_input(t["saisie_autre"])

st.markdown("---")

# Section Disponibilité du Matériel
st.header(t["section_disponibilite"])
statut_dispo = st.radio(t["choix_statut_dispo"], t["options_statut_dispo"])

date_disponibilite_str = "Immédiate"
if statut_dispo == t["options_statut_dispo"][1]: 
    date_choisie = st.date_input(t["date_dispo"], value=date.today())
    date_disponibilite_str = f"À partir du {date_choisie.strftime('%d/%m/%Y')}"
elif statut_dispo == t["options_statut_dispo"][2]: 
    date_disponibilite_str = "Indisponible / Réservé"

st.markdown("---")

# Section Coordonnées et Message de l'utilisateur
st.header(t["section_coordonnees"])
nom_utilisateur = st.text_input(t["nom"])
ville_pays_utilisateur = st.text_input(t["ville_pays"])
contact_utilisateur = st.text_input(t["contact"])
message_utilisateur = st.text_area(t["message"])
# Section Conditions de publication & Soutien
# Section Conditions de publication & Soutien
st.markdown("---")
st.warning("⚠️ **Rappel important :** \n\n* **Pour les Particuliers :** Vos 3 premières publications sont gratuites. Au-delà, c'est à 500 DA (env. 2 €) la publication.\n* **Pour les Professionnels :** L'accès est à 15 € (env. 3 750 DA).")

col_soutien1, col_soutien2 = st.columns(2)
with col_soutien1:
    if st.button("📌 En savoir plus / Tarifs"):
        st.info("Tarifs : 500 DA / ~2 € par publication supplémentaire (particulier) ou 15 € / ~3 750 DA (professionnel). Contactez l'administrateur pour régler.")
with col_soutien2:
    if st.button("☕ Offrir un café / Soutenir l'outil"):
        st.success("Merci de donner un coup de pouce pour maintenir la plateforme active et solidaire.")
    
# Vérification du bannissement
if contact_utilisateur in db["bannis"]:
    st.error("🚫 Ce compte a été banni par l'administration en raison d'un non-respect des règles de la plateforme.")
else:
    publications_utilisateur = [a for a in db["annonces"] if a.get("contact") == contact_utilisateur]
    limite_depassee = (type_compte != "Particulier" or len(publications_utilisateur) >= 3)

    if limite_depassee:
        st.warning("⚠️ **Mode Payant / Participation Requis :** En tant que structure professionnelle / ONG / Pharmacie, ou après avoir dépassé 3 publications gratuites en tant que particulier, un règlement via les modes de paiement ci-dessous est requis pour valider l'action.")

    if st.button(t["btn_valider"]):
        if nom_utilisateur and contact_utilisateur:
            if len(publications_utilisateur) >= 5 and type_compte == "Particulier":
                if contact_utilisateur not in db["bannis"]:
                    db["bannis"].append(contact_utilisateur)
                    sauvegarder_donnees(db)
                st.error("🚫 Limite maximale de publications atteinte. Votre compte a été automatiquement banni.")
            else:
                materiel_choisi = autre_materiel if type_materiel == t["options_materiel"][-1] else type_materiel
                pastille_active = obtenir_pastille_couleur(type_transaction)
                
                # Enregistrement de l'annonce
                nouvelle_annonce = {
                    "type_compte": type_compte,
                    "transaction": type_transaction,
                    "materiel": materiel_choisi,
                    "disponibilite": date_disponibilite_str,
                    "nom": nom_utilisateur,
                    "ville_pays": ville_pays_utilisateur,
                    "contact": contact_utilisateur,
                    "message": message_utilisateur,
                    "date": maintenant
                }
                db["annonces"].append(nouvelle_annonce)
                
                # Création de la notification en direct avec la pastille de couleur
                texte_notif = f"Nouvelle action de **{nom_utilisateur}** ({ville_pays_utilisateur}) - *{type_compte}* : {pastille_active} **{type_transaction}** de *{materiel_choisi}* (Dispo: {date_disponibilite_str})."
                db["notifications"].append({
                    "texte": texte_notif,
                    "date": maintenant
                })
                
                sauvegarder_donnees(db)
                st.success("✅ Vos coordonnées, votre démarche et la disponibilité ont bien été enregistrées et notifiées en direct sur la plateforme !")
        else:
            st.warning("⚠️ Veuillez s'il vous plaît remplir au moins votre nom et vos coordonnées de contact.")

st.markdown("---")

col_p1, col_p2 = st.columns(2)
with col_p1:
    if st.button("🪪 Afficher / Copier le CCP"):
        st.success("CCP : 0023456789 Clé 12")
with col_p2:
    if st.button("💳 Afficher / Copier le RIB"):
        st.success("RIB : 001 00234 002345678912")

        

st.markdown("---")

# Section Guide d'Installation de l'application
st.header(t["section_installation"])
st.write(t["texte_installation"])
st.markdown(f"""
- {t['inst_android']}
- {t['inst_iphone']}
- {t['inst_pc']}
""")
# --- Petit plus : Compteur d'activité en direct ---
total_annonces = len(base_data.get("annonces", []))
st.info(f"💡 **VitalPrêt en direct :** Déjà **{total_annonces}** annonces et actions de solidarité partagées par la communauté !")

# Section Partager l'application VitalPrêt
st.markdown("---")
st.subheader("🌐 Partager VitalPrêt")
st.write("Aidez-nous à faire connaître la plateforme :")
# --- Section Suivi et Notifications des Réponses ---
st.markdown("---")
st.header("📬 Suivi des annonces & Réponses reçues")
st.write("Retrouvez ici toutes les propositions d'aide reçues pour vos annonces :")

# Filtre par contact (pour que l'utilisateur ne voie que SES notifications)
mon_contact = st.text_input("🔍 Entrez votre email ou téléphone (celui utilisé dans vos annonces) pour voir vos messages :")

# Formulaire pour répondre à une annonce visible
with st.form("formulaire_reponse_annonce"):
    st.subheader("🤝 Proposer de l'aide sur une annonce")
    nom_aidant = st.text_input("Votre nom / prénom")
    contact_aidant = st.text_input("Votre contact (Téléphone ou Email)")
    titre_annonce_concernee = st.text_input("Titre ou référence de l'annonce concernée")
    message_aide = st.text_area("Votre message (ex: Je peux vous prêter ce matériel / Je souhaite faire un don)")
    
    soumettre_aide = st.form_submit_button("Envoyer ma proposition d'aide")
    
    if soumettre_aide:
        if nom_aidant and contact_aidant and titre_annonce_concernee:
            if "notifications" not in base_data:
                base_data["notifications"] = []
            
            nouvelle_notif = {
                "annonce": titre_annonce_concernee,
                "nom": nom_aidant,
                "contact": contact_aidant,
                "message": message_aide,
                "date": str(datetime.now()) if 'datetime' in globals() else "Récemment"
            }
            base_data["notifications"].append(nouvelle_notif)
            
            if os.path.exists(FICHIER_DB):
                with open(FICHIER_DB, "w", encoding="utf-8") as f:
                    json.dump(base_data, f, ensure_ascii=False, indent=4)
                    
            st.success("✅ Votre proposition a bien été transmise ! Le propriétaire de l'annonce pourra la consulter sur la plateforme.")
        else:
            st.warning("⚠️ Veuillez remplir au moins votre nom, votre contact et l'annonce concernée.")

# Affichage des notifications filtrées par contact
st.subheader("🔔 Vos messages reçus")
notifications = base_data.get("notifications", [])

if not mon_contact:
    st.info("👆 Entrez votre email ou téléphone ci-dessus pour afficher les réponses reçues à vos annonces.")
else:
    # On filtre les notifications pour ne montrer que celles qui concernent l'utilisateur (par exemple si son contact est mentionné ou si on affiche tout pour l'instant)
    st.write(f"Affichage des messages pour : **{mon_contact}**")
    
    if not notifications:
        st.info("Aucune réponse enregistrée pour le moment sur la plateforme.")
    else:
        # Affichage de toutes les notifications avec un badge clair
        for i, notif in enumerate(notifications):
            with st.expander(f"💬 Aide pour l'annonce : {notif.get('annonce', 'Annonce')} (Par {notif.get('nom', 'Anonyme')})"):
                st.write(f"**👤 Nom de l'aidant :** {notif.get('nom')}")
                st.write(f"**📞 Coordonnées pour le contacter :** {notif.get('contact')}")
                st.write(f"**💬 Message :** {notif.get('message')}")
                st.caption(f"Reçu le : {notif.get('date')}")

# --- Section Partager l'application VitalPrêt ---
st.markdown("---")
st.subheader("🌐 Partager VitalPrêt")
st.write("Aidez-nous à faire connaître la plateforme :")

url_vitalpret = "https://vitalpret.streamlit.app"
texte_vitalpret = "Découvrez VitalPrêt, la plateforme de solidarité et d'annonces. Partagez, soutenez et unissons nos forces !"

encoded_text = urllib.parse.quote(f"{texte_vitalpret} {url_vitalpret}")
encoded_url = urllib.parse.quote(url_vitalpret)

fb_url = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
twitter_url = f"https://twitter.com/intent/tweet?text={encoded_text}"
whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
telegram_url = f"https://t.me/share/url?url={encoded_url}&text={encoded_text}"

st.markdown(f"""
<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px;">
    <a href="{fb_url}" target="_blank"><button style="background-color:#1877F2; color:white; border:none; padding:6px 12px; border-radius:5px; font-weight:bold; cursor:pointer; font-size:12px;">📘 Facebook</button></a>
    <a href="{whatsapp_url}" target="_blank"><button style="background-color:#25D366; color:white; border:none; padding:6px 12px; border-radius:5px; font-weight:bold; cursor:pointer; font-size:12px;">📱 WhatsApp</button></a>
    <a href="{twitter_url}" target="_blank"><button style="background-color:#000000; color:white; border:none; padding:6px 12px; border-radius:5px; font-weight:bold; cursor:pointer; font-size:12px;">✖️ X</button></a>
    <a href="{telegram_url}" target="_blank"><button style="background-color:#229ED9; color:white; border:none; padding:6px 12px; border-radius:5px; font-weight:bold; cursor:pointer; font-size:12px;">✈️ Telegram</button></a>
</div>
""", unsafe_allow_html=True)

st.text_area("📋 Lien à copier :", value=url_vitalpret, height=60)

