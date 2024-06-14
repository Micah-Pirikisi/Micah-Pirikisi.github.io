import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CV - Full Stack Engineer",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Personal Information
st.title("Your Name")
st.subheader("Full Stack Engineer")
st.write("Location: Your City, Country")
st.write("Email: your.email@example.com")
st.write("LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)")
st.write("GitHub: [Your GitHub Profile](https://github.com/yourusername)")

# Professional Summary
st.header("Professional Summary")
st.write("""
    Experienced Full Stack Engineer with expertise in developing web applications using 
    modern technologies. Proficient in front-end and back-end development, with a strong 
    focus on delivering high-quality, user-centric solutions.
""")

# Skills
st.header("Skills")
st.write("**Programming Languages:** Python, JavaScript, HTML, CSS, SQL")
st.write("**Frameworks and Libraries:** React, Node.js, Express, Django, Flask")
st.write("**Databases:** MySQL, PostgreSQL, MongoDB")
st.write("**Tools and Platforms:** Git, Docker, Kubernetes, AWS, GCP")

# Projects
st.header("Projects")
st.subheader("Project 1: Your Project Name")
st.write("""
    Description of the project. Highlight the technologies used, your role, and the impact of the project.
    [GitHub Repository](https://github.com/yourusername/project1)
""")
st.subheader("Project 2: Another Project Name")
st.write("""
    Description of the project. Highlight the technologies used, your role, and the impact of the project.
    [GitHub Repository](https://github.com/yourusername/project2)
""")

# Work Experience
st.header("Work Experience")
st.subheader("Job Title - Company Name")
st.write("**Date:** Start Date - End Date")
st.write("""
    Responsibilities and achievements in this role.
    - Task 1
    - Task 2
    - Task 3
""")
st.subheader("Previous Job Title - Previous Company Name")
st.write("**Date:** Start Date - End Date")
st.write("""
    Responsibilities and achievements in this role.
    - Task 1
    - Task 2
    - Task 3
""")

# Education
st.header("Education")
st.write("**Degree:** Your Degree")
st.write("**Institution:** Your University")
st.write("**Date:** Graduation Date")

# Certifications
st.header("Certifications")
st.write("**Certification Name:** Issuing Organization")
st.write("**Date:** Date of Issuance")

# Contact Information
st.header("Contact Information")
st.write("Feel free to reach out to me through email or LinkedIn for any opportunities or collaborations.")
