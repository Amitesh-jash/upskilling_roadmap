

import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) 
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Upskilling Roadmap Generator", page_icon="🚀", layout="wide")

st.title("🚀 Upskilling Roadmap Generator")
st.write("Get a personalized upskilling roadmap with resources and tools tailored to your role, skills, and goals.")


job_title = st.text_input("💼 Enter your Job Title", placeholder="e.g., Data Analyst")
skills = st.text_area("🛠️ Enter your Current Skills (comma-separated)", placeholder="e.g., Excel, SQL, Python")

experience = st.selectbox(
    "📊 Select Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

timeline = st.radio(
    "⏳ Select Learning Timeline",
    ["3 months", "6 months", "1 year"],
    horizontal=True
)

focus_areas = st.multiselect(
    "🎯 Choose Areas of Focus",
    ["Programming", "Data Analytics", "AI/ML", "Cloud", "Cybersecurity", "Soft Skills", "Leadership"]
)


if st.button("✨ Generate My Roadmap"):
    if job_title.strip() == "" or skills.strip() == "":
        st.error("⚠️ Please enter both Job Title and Skills before generating.")
    else:
        prompt = f"""
        Create an upskilling roadmap for someone aiming to become a '{job_title}'.
        Current skills: {skills}.
        Experience level: {experience}.
        Learning timeline: {timeline}.
        Focus areas: {', '.join(focus_areas) if focus_areas else 'General Career Growth'}.

        Format the roadmap in Markdown with clear sections:
        - 📌 Phase 1 (Foundations)
        - 🚀 Phase 2 (Intermediate)
        - 🏆 Phase 3 (Advanced)

        Each phase should include:
        - Skills/Topics to Learn
        - Recommended Tools & Platforms
        - Suggested Resources (Coursera, Udemy, LinkedIn Learning, Kaggle, official docs, etc.)
        - Duration (aligned with timeline)

        Make it easy to follow, concise, and motivating.
        """

        with st.spinner("🧠 Generating your roadmap..."):
            response = model.generate_content(prompt)

        roadmap = response.text

        st.subheader("📋 Your Personalized Roadmap")
        st.markdown(roadmap)

