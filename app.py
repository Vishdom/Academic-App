import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {"title": "How to Take Smart Notes (Ahrens)", "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"},
    "Williams (1990)": {"title": "Style: Toward Clarity and Grace (Williams)", "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"},
    "Graff & Birkenstein (2014)": {"title": "They Say / I Say (Graff & Birkenstein)", "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"}
}

# --- 3. ENGINES ---
def zettel_check(text):
    return len([s for s in re.split(r'[.!?]+', text) if len(s.split()) > 5]) > 0

def ahrens_engine(original, rewrite):
    return SequenceMatcher(None, original, rewrite).ratio() * 100

def williams_engine(text):
    zombies = ["tion", "ment", "ance", "ence", "ity", "ness", "ization"]
    return [w.strip(",.;:") for w in text.split() if any(s in w.lower() for s in zombies)]

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue"])
    return has_they, has_pivot

# --- 4. NAVIGATION ---
st.sidebar.title("🎓 Residency Progress")
phase = st.sidebar.selectbox("Active Module:", ["Module I: Epistemological Retrieval", "Module II: Stylistic Surgery", "Module III: Dialectical Positioning"])
st.sidebar.divider()
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

tab_course, tab_worksheet, tab_lab = st.tabs(["📖 COURSEWORK & SYLLABUS", "📝 RESEARCH WORKSHEETS", "🧪 ANALYTICAL LAB"])

# --- 5. MODULE I: AHRENS ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.markdown("Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower... [Full Text Restored]")
    with tab_worksheet:
        st.subheader("Worksheet I: Permanent Note Maturation")
        st.text_area("The Self-Contained Assertion:", key="w1")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        src1 = st.text_area("Source Context:", key="ls1")
        rew1 = st.text_area("Permanent Note Draft:", key="lr1")
        if rew1:
            sim = ahrens_engine(src1, rew1)
            st.metric("Cognitive Independence", f"{100-sim:.0f}%")

# --- 6. MODULE II: WILLIAMS ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.markdown("Focus on restoring agency to the sentence by removing Zombie Nouns.")
    with tab_worksheet:
        st.text_input("Identify the Primary Action (Verb):", key="w2")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        rew2 = st.text_area("Input your writing:", key="lr2")
        if rew2:
            zombies = williams_engine(rew2)
            st.warning(f"Zombie Nouns found: {', '.join(zombies)}" if zombies else "✅ No Zombie Nouns found!")

# --- 7. MODULE III: GRAFF & BIRKENSTEIN ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.markdown("""
        "They Say / I Say" logic represents the deep, underlying structure—the "internal DNA"—of all effective argument.
        Writing well means entering into a conversation with others rather than simply expressing ideas in a vacuum.
        """)
    with tab_worksheet:
        st.subheader("Worksheet III: The Pivot")
        st.text_area("The 'They Say' (Summary):", key="w3_t")
        st.text_area("The 'I Say' (Assertion):", key="w3_i")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        rew3 = st.text_area("Scholarly Synthesis:", placeholder="Paste your 'They Say / I Say' draft here...", key="lr3")
        if rew3:
            they, pivot = graff_engine(rew3)
            if they and pivot: st.success("✅ Dialectical 'Move' successful!")
            else: st.error("❌ Missing 'They Say' context or 'I Say' pivot.")
