from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 10, "MAHISHI ARORA", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "Aspiring Marketing & Media Professional", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 10)
        self.cell(0, 6, "mahishiaroraa@gmail.com | +91 95869 78000 | LinkedIn: in/mahishi-arora-0662b8378 | Instagram: @mahishiaroraa_", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def section_title(self, title):
        self.set_font("helvetica", "B", 14)
        self.set_text_color(0, 150, 136) # Turquoise-like
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def body_text(self, text):
        self.set_font("helvetica", "", 11)
        self.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def experience_item(self, title, company, date, bullets):
        self.set_font("helvetica", "B", 12)
        if date:
            self.cell(120, 6, title, new_x="RIGHT")
            self.set_font("helvetica", "I", 11)
            self.cell(0, 6, date, align="R", new_x="LMARGIN", new_y="NEXT")
        else:
            self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 11)
        if company:
            self.cell(0, 6, company, new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 11)
        for bullet in bullets:
            self.multi_cell(0, 6, f"- {bullet}", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

pdf = PDF()
pdf.add_page()

pdf.section_title("PROFESSIONAL SUMMARY")
pdf.body_text("I am a passionate marketing professional with a keen interest in digital media, brand strategy, and storytelling. With hands-on experience managing social media and executing content-driven campaigns, I thrive on analyzing audience behavior to foster meaningful engagement. Combining strong communication skills with creative problem-solving, I am eager to contribute to innovative marketing and media initiatives while continuously learning and growing in the field.")

pdf.section_title("EXPERIENCE")
pdf.experience_item(
    "Junior Marketing Manager (Branding)",
    "AIESEC (Remote)",
    "Feb 2026 - Jul 2026",
    [
        "Conceptualized and produced dynamic digital content, including social media posts and reels, to enhance brand visibility.",
        "Directed client outreach initiatives to foster strategic partnerships and expand audience reach.",
        "Managed daily branding operations, ensuring a consistent and compelling brand narrative."
    ]
)
pdf.experience_item(
    "Marketing Intern",
    "Mango Marketing Solutions",
    "May 2026 - Jun 2026",
    [
        "Assisted in the development, execution, and monitoring of digital marketing campaigns.",
        "Supported the marketing team in tracking analytics and optimizing content strategies."
    ]
)
pdf.experience_item(
    "Marketing Intern",
    "Kathaa (Leather Works Brand)",
    "Apr 2025 - Jun 2025",
    [
        "Contributed to content ideas, campaign planning, and audience engagement.",
        "Assisted with the launch of the Summer 2025 collection."
    ]
)

pdf.section_title("PROJECTS & ACHIEVEMENTS")
pdf.experience_item(
    "Saathi Event",
    "AIESEC Branding Department",
    "",
    ["Served as Junior Event Manager, coordinating event promotion and ensuring seamless execution."]
)
pdf.experience_item(
    "Kathaa Summer Collection 2025",
    "",
    "",
    ["Part of the team for the Kathaa Summer Collection 2025 release."]
)

pdf.section_title("EDUCATION")
pdf.experience_item(
    "B.A. in Multimedia & Mass Communication",
    "UPG College of Commerce and Arts, Mumbai",
    "2025 - 2028 (Expected)",
    []
)
pdf.experience_item(
    "Commerce Stream",
    "DPS Surat",
    "2025",
    ["Score: 88.4%"]
)

pdf.section_title("SKILLS")
pdf.body_text("Marketing & Social Media Management - Communication Skills - Creativity & Content Creation - Problem-Solving - Adaptability & Organisation - Customer Engagement - Creative Writing")

pdf.output("Mahishi_Arora_Resume.pdf")
