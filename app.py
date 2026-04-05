import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {"title": "How to Take Smart Notes", "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"},
    "Williams (1990)": {"title": "Style: Toward Clarity and Grace", "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"},
    "Graff & Birkenstein (2014)": {"title": "They Say / I Say", "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"},
    "Neville (2016)": {"title": "Referencing & Avoiding Plagiarism", "link": "https://www.amazon.com/COMPLETE-GUIDE-REFERENCING-AVOIDING-PLAGIARISM/dp/0335262023"}
}

# --- 3. ENGINES ---
def ahrens_engine(original, rewrite):
    return SequenceMatcher(None, original, rewrite).ratio() * 100

def williams_engine(text):
    zombies = ["tion", "ment", "ance", "ence", "ity", "ness", "ization"]
    return [w.strip(",.;:") for w in text.split() if any(s in w.lower() for s in zombies)]

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue"])
    return has_they, has_pivot

# --- 4. SIDEBAR & SOCIALS ---
st.sidebar.title("🎓 Academic Residency")
st.sidebar.markdown("Welcome to the **Synthesis Lab**. Refine your research from design to dialectic.")

st.sidebar.divider()
phase = st.sidebar.selectbox("Active Module:", ["Module I: Epistemological Retrieval", "Module II: Stylistic Surgery", "Module III: Dialectical Positioning"])

st.sidebar.divider()
st.sidebar.subheader("🔗 Connect with Vishdom")
st.sidebar.page_link("https://www.linkedin.com/in/vishpatil/", label="LinkedIn", icon="🌐")
st.sidebar.page_link("https://github.com/Vishdom", label="GitHub", icon="💻")

st.sidebar.divider()
st.sidebar.subheader("📚 Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

# --- 5. MAIN INTERFACE ---
tab_course, tab_worksheet, tab_lab = st.tabs(["📖 COURSEWORK & SYLLABUS", "📝 RESEARCH WORKSHEETS", "🧪 ANALYTICAL LAB"])

# [Logic for Modules I, II, and III remains consistent as per previous versions]
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.subheader("Syllabus & Theory")
        st.markdown("Sönke Ahrens argues that successful writing depends on a systematic workflow. Use permanent notes to build arguments from the bottom up.")
    with tab_worksheet:
        st.text_area("Draft your Permanent Note:", key="w1")
    with tab_lab:
        src = st.text_area("Source Text:", key="ls1")
        rew = st.text_area("Your Paraphrase:", key="lr1")
        if rew: st.metric("Independence", f"{100-ahrens_engine(src, rew):.0f}%")

elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.markdown("Eliminate **Nominalizations** to restore agency to your prose.")
    with tab_worksheet:
        st.text_input("Analyze sentence:", key="w2")
    with tab_lab:
        rew2 = st.text_area("Input research prose:", key="lr2")
        if rew2:
            zombies = williams_engine(rew2)
            if zombies: st.warning(f"Zombies: {', '.join(zombies)}")
            else: st.success("✅ Clean!")

elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.markdown("Establish the 'They Say' context before the 'I Say' pivot.")
    with tab_worksheet:
        st.text_area("They Say:", key="w3_t")
        st.text_area("I Say:", key="w3_i")
    with tab_lab:
        rew3 = st.text_area("Scholarly Synthesis:", key="lr3")
        if rew3:
            they, pivot = graff_engine(rew3)
            if they and pivot: st.success("✅ Move detected!")
            else: st.error("❌ Missing context/pivot.")

# --- 6. CONTACT FORM & FOOTER ---
st.divider()
st.subheader("📩 Feedback & Collaboration")
contact_form = """
<form action="https://formsubmit.co/vishpatilwork@gmail.com" method="POST">
     <input type="hidden" name="_tracker" value="Academic Residency App">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; padding: 5px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; padding: 5px;">
     <textarea name="message" placeholder="Your feedback or research inquiry..." required style="width: 100%; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; padding: 5px;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; color: grey; font-size: 12px; margin-top: 50px;">
        Created by <b>Vishdom</b> | Academic Synthesis Residency © 2026
    </div>
    """,
    unsafe_allow_html=True
)
