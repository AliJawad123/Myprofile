import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Jawad Ali | GIPHY Creator", page_icon="🎨", layout="centered")

# Profile image
image = Image.open("assets/jawad.jpeg")
st.image(image, width=180)

# Name and Title
st.title("Jawad Ali")
st.subheader("GIPHY Creator | AI Engineer | Photographer")
st.markdown("📍 Karachi, Pakistan | 📧 jawadali2020189@gmail.com")

st.markdown("---")

# About Me
st.header("👋 Hello!")
st.write("""
I’m Jawad Ali, a tech-savvy visual creator and AI engineer, blending art and code to tell compelling digital stories.  
Raised in the breathtaking landscapes of Hunza and Gilgit – Gilgit-Baltistan, my creative eye was shaped by nature and sharpened by technology.

Currently, I work as a Programmer Analyst at Aga Khan University in Karachi, where I develop intelligent systems and smart tools. But beyond the screen, I channel my creativity through GIFs, stickers, and photography that reflect emotion, culture, and fun in motion.
""")

# GIPHY Creator Highlight
st.header("🎨 My GIPHY Creations")
st.write("""
I’ve created a unique series of animated GIFs and line art stickers inspired by real-life moments, emotions, and cultural stories.  
Check out my GIPHY work: [GIPHY Profile](https://giphy.com/channel/YourChannelHere) *(Update this link when live)*  
You’ll find looping animations, minimalist yellow-line artwork, and expressive storytelling through motion design.
""")

# Creative Tools
st.header("🛠️ Creative & Technical Skills")
st.markdown("""
- **Design & Animation:** Line Art, Looping Stickers, Motion Graphics  
- **GIF Creation Tools:** Procreate, Photoshop, Canva, After Effects  
- **Programming:** Python, JavaScript, C++  
- **AI Libraries:** OpenCV, Mediapipe, YOLO, NLTK  
- **Frameworks:** Django, Streamlit, Tkinter, React  
- **Other Tools:** Git, LaTeX, Excel, Web Scraping
""")

# Featured Projects (with creative spin)
st.header("💡 Featured Tech + Art Projects")

st.markdown("### ✨ Yellow Line Art Series")
st.write("Created a set of minimalist couple animations using vibrant yellow lines, expressing movement, emotion, and connection.")

st.markdown("### 📷 Visual AI: Drowsiness Detection System")
st.write("Fused machine learning with visual inputs to build a YOLOv5-based drowsiness alert system.")

st.markdown("### 🧍 AI Attendance System")
st.write("Engineered a face recognition-based attendance tracker—automated, interactive, and user-friendly.")

st.markdown("### 🎓 Final Year Project – Smart Lecture Translator")
st.write("Merged AI + UX to design a multilingual lecture translator using Azure APIs and RAG-based chatbots.")

# Photography
st.header("📸 Visual Storytelling")
st.write("""
Outside the screen, I’m often behind the lens, capturing the serene beauty of Gilgit-Baltistan.  
My visual style carries into my GIFs and stickers—simple, emotional, and authentic.
""")

# Contact & Socials
st.header("📫 Let’s Connect")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/jawad-ali-021394211/)  
- [GitHub](https://github.com/AliJawad123/)  
- [GIPHY](https://giphy.com/channel/Jawadali123) 
- Email: jawadali2020189@gmail.com  
""")

st.markdown("---")
st.caption("Crafted with ❤️ for the GIPHY Creator Community using Streamlit.")
