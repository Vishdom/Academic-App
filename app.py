import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. PRIMARY SOURCE BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {
        "title": "How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking.",
        "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"
    },
    "Williams (1990)": {
        "title": "Style: Toward Clarity and Grace.",
        "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"
    },
    "Graff & Birkenstein (2014)": {
        "title": "They Say / I Say: The Moves That Matter in Academic Writing.",
        "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"
    }
}

# --- 3. ANALYTICAL ENGINES ---
def ahrens_engine(original, rewrite):
    sim = SequenceMatcher(None, original, rewrite).ratio() * 100
    tethers = ["the author", "the text", "claims that", "suggests that"]
    found_tethers = [t for t in tethers if t in rewrite.lower()]
    return sim, found_tethers

def williams_engine(text):
    zombie_suffixes = ["tion", "ment", "ance", "ence", "ity", "ness", "ization"]
    words = text.split()
    zombies = [w.strip(",.;:") for w in words if any(s in w.lower() for s in zombie_suffixes)]
    return zombies

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue"])
    return has_they, has_pivot

# --- 4. NAVIGATION ---
st.sidebar.title("🎓 Residency Progress")

module_options = [
    "Module I: Epistemological Retrieval",
    "Module II: Stylistic Surgery",
    "Module III: Dialectical Positioning"
]
phase = st.sidebar.selectbox("Active Module:", options=module_options)

st.sidebar.divider()
st.sidebar.subheader("📚 Primary Source Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

# --- 5. TAB SYSTEM ---
tab_course, tab_worksheet, tab_lab = st.tabs([
    "📖 COURSEWORK & SYLLABUS",
    "📝 RESEARCH WORKSHEETS",
    "🧪 ANALYTICAL LAB"
])

# --- 6. MODULE I CONTENT (VERBATIM AHRENS) ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.write("---")

        st.subheader("How to Take Smart Notes by Sönke Ahrens")

        st.info("""
        Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower
        or isolated brainstorming. He introduces the Zettelkasten, or slip-box method, a technique used by sociologist
        Niklas Luhmann to build a decentralized network of interconnected ideas over several decades. By converting
        fleeting thoughts and reading notes into permanent, self-contained entries, writers can develop complex
        arguments from the bottom up rather than facing the "myth of the blank page." This approach treats writing
        as the primary medium of thinking, allowing researchers to externalize their memory and focus their mental
        energy on making creative connections. Ultimately, Ahrens emphasizes that a simple, tool-agnostic structure
        enables flow and expertise by breaking down the amorphous task of authorship into manageable, interlocking steps.
        """)

        with st.expander("Sub-Module 1.1: The Principle of Atomicity", expanded=True):
            st.markdown("""
            - **Objective:** Externalize memory through self-contained entries.
            - **Primary Reading:** Ahrens (2022), Chapters 2-4.
            - **Key Concept:** Writing as the primary medium of thinking.
            """)

    with tab_worksheet:
        st.subheader("Worksheet I-A: Permanent Note Template")
        st.text_input("Source Reference:", key="w1_ref")
        st.text_area("The Atomic Idea (Self-Contained Entry):",
                     placeholder="Externalize the thought here so it survives without the original context...",
                     key="w1_atom")
        st.text_area("Connection: How does this interlock with existing notes?", key="w1_connect")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        st.caption("Testing for Cognitive Independence and Retrieval Effort.")
        col1, col2 = st.columns(2)
        with col1: src1 = st.text_area("1️⃣ Source Material:", height=200, key="lab_s1")
        with col2: rew1 = st.text_area("2️⃣ Elaborative Encoding (Your Note):", height=200, key="lab_r1")

        if src1 and rew1:
            sim, tethers = ahrens_engine(src1, rew1)
            st.metric("Cognitive Independence", f"{100-sim:.0f}%")
            if sim > 45: st.error("❌ High Structural Mirroring: This is a fleeting note, not a permanent one.")
            else: st.success("✅ Atomic Independence achieved.")

# --- 7. MODULE II CONTENT ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.write("---")
        with st.expander("Sub-Module 2.1: The Taxonomy of Obscurity", expanded=True):
            st.markdown("Focus on Williams (1990) and the removal of nominalizations.")

# --- 8. MODULE III CONTENT ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.write("---")
        st.subheader("\"They Say / I Say\" by Gerald Graff and Cathy Birkenstein")
        # (Content from previous update remains here)
