from fpdf import FPDF

class PitchDeck(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, 'NATURA AI - Document de presentation confidentiel', 0, 1, 'R')
            self.ln(5)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def slide_title(self, title, subtitle=""):
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(34, 139, 34) # Vert NATURA
        self.cell(0, 15, title, 0, 1, 'L')
        if subtitle:
            self.set_font('Helvetica', 'I', 14)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, subtitle, 0, 1, 'L')
        self.ln(10)
        self.set_draw_color(34, 139, 34)
        self.line(10, self.get_y(), 80, self.get_y())
        self.ln(10)

    def bullet_point(self, title, text):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(5, 8, "-", 0, 0)
        self.cell(0, 8, title, 0, 1)
        self.set_font('Helvetica', '', 11)
        self.set_text_color(80, 80, 80)
        self.set_x(15)
        self.multi_cell(0, 6, text)
        self.ln(3)

# --- GENERATION DU DOCUMENT ---
pdf = PitchDeck()
pdf.set_auto_page_break(auto=True, margin=20)

# --- PAGE 1 : COUVERTURE ---
pdf.add_page()
pdf.ln(50)
pdf.set_font('Helvetica', 'B', 40)
pdf.set_text_color(34, 139, 34)
pdf.cell(0, 20, 'NATURA AI', 0, 1, 'C')
pdf.set_font('Helvetica', 'B', 18)
pdf.set_text_color(50, 50, 50)
pdf.cell(0, 15, "L'Assistant Intelligent de Recherche Scientifique", 0, 1, 'C')
pdf.set_font('Helvetica', 'I', 14)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, "Rapport de presentation - Version Pilote 9.0D", 0, 1, 'C')
pdf.ln(30)
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(120, 120, 120)
pdf.cell(0, 10, "Propulse par l'Intelligence Artificielle", 0, 1, 'C')
pdf.cell(0, 10, "Date : Novembre 2024", 0, 1, 'C')

# --- PAGE 2 : LE PROBLEME ---
pdf.add_page()
pdf.slide_title("Le Constat", "Pourquoi la recherche scientifique est un defi aujourd'hui")
pdf.bullet_point("Surcharge d'informations", "Plus de 1,5 million d'articles scientifiques sont publies chaque annee. Il est impossible pour un professionnel de lire tout ce qui sort.")
pdf.bullet_point("La barriere de la langue", "90% de la litterature scientifique mondiale est redigee en anglais, ce qui ralentit la recherche pour les non-anglophones.")
pdf.bullet_point("Le temps perdu", "Un chercheur passe en moyenne 30% de son temps a chercher, filtrer et lire des resumes plutot qu'a analyser les donnees.")
pdf.bullet_point("Les doublons", "Les informations sont dispersees sur de multiples bases de donnees (PubMed, Europe PMC, editeurs), creant des doublons chronophages.")

# --- PAGE 3 : LA SOLUTION ---
pdf.add_page()
pdf.slide_title("La Solution NATURA AI", "Un moteur de recherche augmentee par l'IA")
pdf.bullet_point("Agregation Multi-Sources", "Interrogation simultanee des 3 plus grandes bases de donnees mondiales : PubMed, Europe PMC et Crossref.")
pdf.bullet_point("Dedoublonnage Intelligent", "Fusion automatique des articles trouves sur plusieurs bases (par PMID, DOI ou titre) pour ne garder que l'information unique.")
pdf.bullet_point("Analyse par Intelligence Artificielle", "Extraction automatique des donnees cles (Plante, Molecule, Pathologie, Type d'etude) grace a une IA entrainee.")
pdf.bullet_point("NATURA SCORE", "Une note de confiance sur 100 attribuee a chaque article en fonction de son type d'etude, de son impact (citations) et de sa completude.")

# --- PAGE 4 : EXEMPLE CONCRET ---
pdf.add_page()
pdf.slide_title("Cas d'usage concret", 'Exemple de recherche : "Artemisinin resistance"')
pdf.set_font('Helvetica', 'B', 12)
pdf.cell(0, 8, "1. Recherche brute (30 resultats) :", 0, 1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, "L'utilisateur lance la recherche. L'outil interroge les 3 bases de donnees, recupere les articles et supprime les doublons. Il ne reste que 29 articles uniques.")
pdf.ln(5)

pdf.set_font('Helvetica', 'B', 12)
pdf.cell(0, 8, "2. Analyse par l'IA :", 0, 1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, "L'utilisateur clique sur un article. L'IA Agnes lit le resume en anglais et extrait instantanement :")
pdf.set_font('Helvetica', 'I', 11)
pdf.set_text_color(34, 139, 34)
pdf.multi_cell(0, 6, "Plante : Artemisia annua | Molecule : Artemisinin | Pathologie : Paludisme | Resultat : Mitige")
pdf.set_text_color(0, 0, 0)
pdf.ln(5)

pdf.set_font('Helvetica', 'B', 12)
pdf.cell(0, 8, "3. Generation du rapport PDF :", 0, 1)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 6, "L'utilisateur genere un rapport PDF professionnel, filigrane NATURA AI, pret a etre partage. Le rapport contient les analyses de l'IA en francais et les resumes originaux.")

# --- PAGE 5 : OFFRE PILOTE ---
pdf.add_page()
pdf.slide_title("Offre Partenaire Pilote", "6 mois d'acces gratuit pour co-construire l'avenir")
pdf.set_font('Helvetica', '', 12)
pdf.multi_cell(0, 8, "Nous recherchons des partenaires (laboratoires, chercheurs, professionnels de sante) pour tester NATURA AI en conditions reelles.")
pdf.ln(5)

pdf.bullet_point("Acces VIP", "6 mois d'acces gratuit et illimite a toutes les fonctionnalites de l'application.")
pdf.bullet_point("Limite de test", "5 recherches par jour pour garantir la stabilite du systeme et le respect des quotas.")
pdf.bullet_point("Confidentialite", "Un accord de confidentialite mutuel garantit que vos recherches et vos donnees restent privees.")
pdf.bullet_point("Votre avis compte", "Nous avons besoin de vos retours d'experience pour orienter les developpements futurs de la version 1.0.")

# --- PAGE 6 : CONTACT ---
pdf.add_page()
pdf.ln(60)
pdf.set_font('Helvetica', 'B', 24)
pdf.set_text_color(34, 139, 34)
pdf.cell(0, 15, 'Pret a revolutionner votre recherche ?', 0, 1, 'C')
pdf.ln(10)
pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, 'Contactez-nous pour obtenir votre code d\'acces partenaire.', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Helvetica', 'B', 12)
pdf.cell(0, 10, 'Email : contact@natura-ai.fr', 0, 1, 'C')
pdf.cell(0, 10, 'Site web : natura-ai.streamlit.app', 0, 1, 'C')

# --- SAUVEGARDE ---
pdf.output("NATURA_AI_Presentation.pdf")
print("Document PDF genere avec succes : NATURA_AI_Presentation.pdf")