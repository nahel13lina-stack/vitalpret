import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="VitalPrêt",
    page_icon="🤝",
    layout="centered"
)

# Dictionnaire des traductions
traductions = {
    "Français": {
        "titre": "VitalPrêt - Solidarité & Matériel Médical",
        "description": "Plateforme de mise à disposition de matériel médical d'urgence et d'aide solidaire.",
        "selection_langue": "Choisissez votre langue :",
        "section_materiel": "Demande de Matériel Médical",
        "choix_materiel": "Sélectionnez le type de matériel :",
        "options_materiel": ["Concentrateur d'oxygène", "Fauteuil roulant", "Lit médicalisé", "Matériel orthopédique", "Autre matériel"],
        "saisie_autre": "Précisez l'autre matériel recherché :",
        "section_paiement": "Modes de Paiement & Solidarité",
        "info_paiement": "Vous pouvez participer aux frais ou faire un don direct via les coordonnées suivantes :",
        "ccp": "CCP : [Votre Numéro CCP ici]",
        "rib": "Compte Bancaire (RIB) : [Votre RIB ici]",
        "bouton_valider": "Envoyer la demande",
        "section_installation": "📱 Installer l'application sur votre appareil",
        "texte_installation": "Vous pouvez installer cet outil directement sur votre téléphone, tablette ou ordinateur pour l'utiliser comme une vraie application :",
        "inst_android": "**Sur Android (Chrome) :** Appuyez sur les trois petits points en haut à droite du navigateur, puis choisissez **'Installer l'application'** ou **'Ajouter à l'écran d'accueil'**.",
        "inst_iphone": "**Sur iPhone / iPad (Safari) :** Appuyez sur le bouton de partage (le carré avec une flèche vers le haut), puis sélectionnez **'Sur l'écran d'accueil'**.",
        "inst_pc": "**Sur Ordinateur (Chrome / Edge) :** Cliquez sur l'icône d'installation (un petit ecran avec une flèche) située tout à droite dans la barre d'adresse du navigateur."
    },
    "Anglais": {
        "titre": "VitalPrêt - Solidarity & Medical Equipment",
        "description": "Platform for emergency medical equipment and solidarity support.",
        "selection_langue": "Choose your language:",
        "section_materiel": "Medical Equipment Request",
        "choix_materiel": "Select equipment type:",
        "options_materiel": ["Oxygen concentrator", "Wheelchair", "Medical bed", "Orthopedic equipment", "Other equipment"],
        "saisie_autre": "Please specify the other equipment needed:",
        "section_paiement": "Payment Methods & Solidarity",
        "info_paiement": "You can contribute or make a direct donation using the following details:",
        "ccp": "CCP: [Your CCP Number here]",
        "rib": "Bank Account (RIB): [Your Bank Details here]",
        "bouton_valider": "Submit request",
        "section_installation": "📱 Install the app on your device",
        "texte_installation": "You can install this tool directly on your phone, tablet, or computer to use it like a real app:",
        "inst_android": "**On Android (Chrome):** Tap the three dots in the top right, then select **'Install app'** or **'Add to Home screen'**.",
        "inst_iphone": "**On iPhone / iPad (Safari):** Tap the share button (square with an upward arrow), then select **'Add to Home Screen'**.",
        "inst_pc": "**On Computer (Chrome / Edge):** Click the install icon in the right side of the browser address bar."
    },
    "Arabe": {
        "titre": "فيتال بري - التضامن والمعدات الطبية",
        "description": "منصة لتوفير المعدات الطبية الطارئة والدعم التضامني.",
        "selection_langue": "اختر لغتك:",
        "section_materiel": "طلب معدات طبية",
        "choix_materiel": "اختر نوع المعدات:",
        "options_materiel": ["مكثف الأكسجين", "كرسي متحرك", "سرير طبي", "معدات تقويم العظام", "معدات أخرى"],
        "saisie_autre": "يرجى تحديد المعدات الأخرى المطلوبة:",
        "section_paiement": "طرق الدفع والتضامن",
        "info_paiement": "يمكنك المساهمة أو التبرع مباشرة عبر التفاصيل التالية:",
        "ccp": "رقم البريد الجزائري (CCP): [أدخل رقم الـ CCP هنا]",
        "rib": "الحساب البنكي (RIB): [أدخل تفاصيل الحساب هنا]",
        "bouton_valider": "إرسال الطلب",
        "section_installation": "📱 تثبيت التطبيق على جهازك",
        "texte_installation": "يمكنك تثبيت هذه الأداة مباشرة على هاتفك أو جهازك اللوحي أو حاسوبك لاستخدامها التطبيق كنظام مستقل:",
        "inst_android": "**على أندرويد (متصفح كروم):** اضغط على النقاط الثلاث في أعلى اليسار/اليمين، ثم اختر **'تثبيت التطبيق'** أو **'إضافة إلى الشاشة الرئيسية'**.",
        "inst_iphone": "**على آيفون / آي باد (متصفح سفاري):** اضغط على زر المشاركة (المربع الذي بداخله سهم للأعلى)، ثم اختر **'إضافة إلى الشاشة الرئيسية'**.",
        "inst_pc": "**على الكمبيوتر:** اضغط على رمز التثبيت في شريط عنوان المتصفح."
    },
    "Allemand": {
        "titre": "VitalPrêt - Solidarität & Medizinische Ausrüstung",
        "description": "Plattform für medizinische Notfallausrüstung und solidarische Unterstützung.",
        "selection_langue": "Wählen Sie Ihre Sprache:",
        "section_materiel": "Anfrage für medizinische Ausrüstung",
        "choix_materiel": "Wählen Sie den Typ der Ausrüstung:",
        "options_materiel": ["Sauerstoffkonzentrator", "Rollstuhl", "Pflegebett", "Orthopädische Ausrüstung", "Sonstige Ausrüstung"],
        "saisie_autre": "Bitte geben Sie die andere benötigte Ausrüstung an:",
        "section_paiement": "Zahlungsmethoden & Solidarität",
        "info_paiement": "Sie können über die folgenden Daten beitragen oder direkt spenden:",
        "ccp": "CCP: [Ihre CCP-Nummer hier]",
        "rib": "Bankkonto (RIB): [Ihre Bankdaten hier]",
        "bouton_valider": "Anfrage absenden",
        "section_installation": "📱 App auf Ihrem Gerät installieren",
        "texte_installation": "Sie können dieses Tool direkt auf Ihrem Telefon oder Computer installieren:",
        "inst_android": "**Auf Android (Chrome):** Tippen Sie auf die drei Punkte und wählen Sie **'App installieren'**.",
        "inst_iphone": "**Auf iPhone (Safari):** Tippen Sie auf das Teilen-Symbol und wählen Sie **'Zum Home-Bildschirm'**.",
        "inst_pc": "**Auf PC (Chrome / Edge):** Klicken Sie auf das Installieren-Symbol in der Adressleiste."
    },
    "Russe": {
        "titre": "VitalPrêt - Солидарность и медицинское оборудование",
        "description": "Платформа для предоставления экстренного медицинского оборудования и помощи.",
        "selection_langue": "Выберите ваш язык:",
        "section_materiel": "Запрос медицинского оборудования",
        "choix_materiel": "Выберите тип оборудования:",
        "options_materiel": ["Кислородный концентратор", "Инвалидная коляска", "Медицинская кровать", "Ортопедическое оборудование", "Другое оборудование"],
        "saisie_autre": "Уточните другое необходимое оборудование:",
        "section_paiement": "Способы оплаты и солидарность",
        "info_paiement": "Вы можете сделать вклад или прямой перевод по следующим реквизитам:",
        "ccp": "CCP: [Ваш номер CCP здесь]",
        "rib": "Банковский счет (RIB): [Ваши реквизиты здесь]",
        "bouton_valider": "Отправить запрос",
        "section_installation": "📱 Установить приложение на устройство",
        "texte_installation": "Вы можете установить этот инструмент на телефон или компьютер:",
        "inst_android": "**На Android (Chrome):** Нажмите три точки вверху и выберите **'Установить приложение'**.",
        "inst_iphone": "**На iPhone (Safari):** Нажмите кнопку «Поделиться» и выберите **'На экран «Домой»'**.",
        "inst_pc": "**На ПК (Chrome / Edge):** Нажмите значок установки в адресной строке браузера."
    },
    "Mandarin": {
        "titre": "VitalPrêt - 守望相助与医疗设备",
        "description": "提供紧急医疗设备和声援支持的平台。",
        "selection_langue": "请选择您的语言：",
        "section_materiel": "医疗设备申请",
        "choix_materiel": "选择设备类型：",
        "options_materiel": ["制氧机", "轮椅", "医用病床", "骨科器材", "其他设备"],
        "saisie_autre": "请说明您需要的其他设备：",
        "section_paiement": "支付方式与爱心捐助",
        "info_paiement": "您可以通过以下信息进行资助或直接捐款：",
        "ccp": "邮政账户 (CCP)：[在此处输入您的CCP]",
        "rib": "银行账户 (RIB)：[在此处输入您的RIB]",
        "bouton_valider": "提交申请",
        "section_installation": "📱 在您的设备上安装应用",
        "texte_installation": "您可以直接将此工具安装到手机或电脑上：",
        "inst_android": "**安卓手机 (Chrome)：** 点击右上角三个点，选择 **'安装应用'** 或 **'添加到主屏幕'**。",
        "inst_iphone": "**苹果手机 (Safari)：** 点击分享按钮（带向上箭头的方框），选择 **'添加到主屏幕'**。",
        "inst_pc": "**电脑端 (Chrome / Edge)：** 点击浏览器地址栏右侧的安装图标。"
    }
}

# Barre latérale pour le choix de la langue
langue_choisie = st.sidebar.selectbox("Langue / Language / اللغة", list(traductions.keys()))
t = traductions[langue_choisie]

# En-tête de l'application
st.title(t["titre"])
st.write(t["description"])

st.markdown("---")

# Section Matériel Médical
st.header(t["section_materiel"])
type_materiel = st.selectbox(t["choix_materiel"], t["options_materiel"])

autre_materiel = ""
if type_materiel == t["options_materiel"][-1]:  # Si "Autre matériel" est sélectionné
    autre_materiel = st.text_input(t["saisie_autre"])

if st.button(t["bouton_valider"]):
    st.success("Votre demande a bien été enregistrée. Merci pour votre démarche !")

st.markdown("---")

# Section Paiement / Coordonnées Bancaires et CCP
st.header(t["section_paiement"])
st.write(t["info_paiement"])
st.info(f"🔹 **{t['ccp']}**\n\n🔹 **{t['rib']}**")

st.markdown("---")

# Section Instructions d'installation
st.header(t["section_installation"])
st.write(t["texte_installation"])
st.markdown(f"""
- {t['inst_android']}
- {t['inst_iphone']}
- {t['inst_pc']}
""")
