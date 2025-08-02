import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Jawad Ali", page_icon="💻", layout="centered")

# Profile image
image = Image.open("assets/jawad.jpeg")  # Replace with your photo
st.image(image, width=180)

# Name and Title
st.title("Jawad Ali")
st.subheader("AI Engineer | Web Developer | Photographer")
st.markdown("📍 Karachi, Pakistan | 📧 jawadali2020189@gmail.com")  # Replace with real email

st.markdown("---")

# About Me
st.header("👋 About Me")
st.write("""
I am a Bachelor’s graduate in Artificial Intelligence from GIKI, currently working as a Programmer Analyst at Aga Khan University, Karachi.  
I enjoy solving real-world problems using AI and web technologies. I also have a passion for photography and freelancing.
""")

# Skills
st.header("🧠 Skills & Technologies")
st.markdown("""
- **Languages:** Python, C++, JavaScript  
- **Libraries:** OpenCV, NLTK, Mediapipe, YOLO  
- **Frameworks:** Django, Streamlit, React, Tkinter  
- **Tools:** Git, Excel, LaTeX, Web Scraping
""")

# Projects
st.header("💼 Projects & Experience")

st.markdown("### 🧍 AI Attendance System (Internship @ GIK Institute)")
st.write("Developed a face recognition-based attendance system using OpenCV, Excel, and Tkinter.")

st.markdown("### 🍽️ Indian Food Data Collection (Data Analyst Intern)")
st.write("Collected global Indian food shop data using Python-based web scraping.")

st.markdown("### 🧠 Final Year Project – Smart Lecture Translator")
st.write("Website to translate non-native language lectures using Azure speech services and AI chatbot (RAG + LLMs).")

st.markdown("### 💪 AI Webcam Gym")
st.write("Pose-based workout form correction using Mediapipe.")

st.markdown("### 🛏️ Drowsiness Detection System")
st.write("Built with YOLOv5 to detect sleepy drivers via eye-tracking.")

st.markdown("### 🧳 Tourist Guide Console App (C++)")
st.write("Suggests optimized routes within a given budget.")

# Photography
st.header("📸 Photography")
st.write("In my free time, I love capturing landscapes of Gilgit-Baltistan. More coming soon!")

# Contact
st.header("📫 Connect with Me")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/jawad-ali-021394211/)
- [GitHub](https://https://github.com/AliJawad123/) 
- Email: jawadali2020189@gmail.com 
""")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

