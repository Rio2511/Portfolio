import streamlit as st
import base64

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Portfolio - Arkoprovo Gupta", layout="wide")

# Theme toggle
mode = st.sidebar.radio("🌗 Choose Theme", ["🌞 Light Mode", "🌙 Dark Mode"], index=1)
bg_color = "#0e1117" if mode == "🌙 Dark Mode" else "#ffffff"
text_color = "#ffffff" if mode == "🌙 Dark Mode" else "#000000"

st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {bg_color};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {bg_color};
        }}
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Arkoprovo Gupta.jpg", width=150)  # Add your photo to the project directory
with col2:
    st.markdown(f"<h1 style='color:{text_color}'>Arkoprovo Gupta</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:{text_color}'>Senior SQL Analyst | MBA (Business Analytics & Data Science)</h4>", unsafe_allow_html=True)

with st.expander("🔗 Connect with Me"):
    st.markdown("""
    - 📧 [arkoprovo.gupta24-26@bibs.co.in](mailto:arkoprovo.gupta24-26@bibs.co.in)  
    - 💼 [LinkedIn](https://linkedin.com/in/arkoprovo-gupta-data-analyst)  
    - 🐙 [GitHub](https://github.com/Rio2511/SelfProject)  
    """)

# ---------------- TABS ----------------
tabs = st.tabs(["🧾 Summary", "🎓 Education", "💼 Experience", "🧰 Skills", "📈 Projects", "📜 Certifications", "🏅 Achievements", "🎯 Hobbies", "📄 Resume"])

# ---------------- CONTENT ----------------

with tabs[0]:  # Summary
    st.markdown("### 🧾 Professional Summary")
    st.info("""
    Innovative and results-driven Senior SQL Analyst with experience in database optimization, team leadership, and problem-solving.
    Passionate about using data to drive business decisions. Skilled in SQL, Python, and machine learning.
    Currently pursuing an MBA in Business Analytics & Data Science to expand business domain expertise.
    """)

with tabs[1]:  # Education
    st.markdown("### 🎓 Education")
    st.write("""
    **MBA – Business Analytics & Data Science**  
    Bengal Institute of Business Studies | 2024 – Present

    **Master of Computer Application (MCA)**  
    Heritage Institute of Technology | 2018 – 2021 | CGPA: 6.94

    **Bachelor of Computer Application (BCA)**  
    The Heritage Academy | 2015 – 2018 | CGPA: 7.29

    **St. Patrick's H.S School, Asansol**  
    ICSE 2013 (10th), ISC 2015 (12th Science - PCMB)
    """)

with tabs[2]:  # Experience
    st.markdown("### 💼 Professional Experience")
    st.write("""
    **Senior SQL Database Analyst**  
    Movate Pvt Technologies (formerly CSS Corp) | Dec 2021 – July 2024 | Bangalore  
    - Led a 10-member team as Senior Analyst, specializing in Level 2 SQL support  
    - Improved query execution time by 50%, boosting data retrieval by 30%  
    - Worked with Kibana, Elastic, and handled server configurations (Voice Gateways, CISCO switches)  
    - Earned multiple Quarterly Recognition Awards
    """)

with tabs[3]:  # Skills
    st.markdown("### 🧰 Skills")
    st.write("""
    - **Languages/Tools:** SQL, Python, Java, Excel  
    - **Database & Analytics:** MySQL, Ticketing Tools, Elastic Stack  
    - **ML/DS:** Machine Learning with Python  
    - **Soft Skills:** Team Leadership, Analytical Thinking, Communication
    """)

with tabs[4]:  # Projects
    st.markdown("### 📈 Projects")
    st.write("""
    **Self Project Repository**  
    Collection of self-initiated analytics and coding projects.  
    [GitHub](https://github.com/Rio2511/SelfProject)

    *(Please add individual project titles/descriptions to your GitHub for recruiters to view clearly.)*
    """)

with tabs[5]:  # Certifications
    st.markdown("### 📜 Certifications")
    st.markdown("📁 [View Certificates Folder](https://drive.google.com/drive/folders/1QhpWBpC0TmyanxID1pb2M8sM1Zz5pOCW?usp=drive_link)")

with tabs[6]:  # Achievements
    st.markdown("### 🏅 Achievements")
    st.write("""
    - Multiple Quarterly Awards at Movate Pvt Ltd  
    - Successfully transitioned to networking tools team for Target project  
    - Optimized SQL processes for enterprise-grade databases
    """)

with tabs[7]:  # Hobbies
    st.markdown("### 🎯 Hobbies & Interests")
    st.write("""
    - 📊 Exploring SQL performance tuning challenges  
    - 🧠 Learning AI for business use cases  
    - 🎮 Gaming and coding side projects  
    - ✍️ Reading about data science and tech innovation
    """)

with tabs[8]:  # Resume
    st.markdown("### 📄 Resume")

    with st.expander("📑 View & Download My Resume"):
        with open("My Resume (3).pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        base64_pdf = base64.b64encode(PDFbyte).decode("utf-8")
        pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Resume",
            data=PDFbyte,
            file_name="My Resume (3).pdf",
            mime="application/pdf"
        )

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2025 Arkoprovo Gupta | Portfolio | Built with Streamlit")
