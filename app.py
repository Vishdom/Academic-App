import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. THE CORRECT 4-SOURCE BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {
        "title": "How to Take Smart Notes (Sönke Ahrens)",
        "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"
    },
    "Williams (1990)": {
        "title": "Style: Toward Clarity and Grace (Joseph M. Williams)",
        "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"
    },
    "Graff & Birkenstein (2014)": {
        "title": "They Say / I Say (Graff & Birkenstein)",
        "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"
    },
    "Neville (2016)": {
        "title": "Referencing & Avoiding Plagiarism (Colin Neville)",
        "link": "https://www.amazon.com/COMPLETE-GUIDE-REFERENCING-AVOIDING-PLAGIARISM/dp/0335262023"
    }
}

# --- 3. ENGINES ---
def ahrens_engine(original, rewrite):
    return SequenceMatcher(None, original, rewrite).ratio() * 100

def williams_engine(text):
    zombie_suffixes = ["tion", "ment", "ance", "ence", "ity", "ness", "ization"]
    words = text.split()
    zombies = [w.strip(",.;:") for w in words if any(s in w.lower() for s in zombie_suffixes)]
    return zombies

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue"])
    return has_they, has_pivot

# --- 4. SIDEBAR & INTRODUCTION ---
st.sidebar.title("🎓 Academic Residency")
st.sidebar.markdown("""
**Welcome to the Synthesis Lab.** This environment is designed to bridge the gap between formal research and functional prose. Through three progressive modules, you will refine your epistemological retrieval, stylistic clarity, and dialectical positioning.
""")
st.sidebar.divider()

phase = st.sidebar.selectbox("Active Module:", ["Module I: Epistemological Retrieval", "Module II: Stylistic Surgery", "Module III: Dialectical Positioning"])

st.sidebar.divider()
st.sidebar.subheader("📚 Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

# --- 5. MAIN INTERFACE ---
tab_course, tab_worksheet, tab_lab = st.tabs(["📖 COURSEWORK & SYLLABUS", "📝 RESEARCH WORKSHEETS", "🧪 ANALYTICAL LAB"])

# --- MODULE I: AHRENS ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.subheader("Syllabus & Theory")
        st.markdown("Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower. By converting fleeting thoughts into permanent entries, writers develop arguments from the bottom up.")
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Atomicity:** One idea per note.\n* **Independence:** Readable without context.\n* **Connectivity:** Linked to the web.")
    with tab_worksheet:
        st.subheader("Worksheet I: Note Maturation")
        st.text_area("Draft your Permanent Note here:", key="w1")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        src = st.text_area("Source Text:", key="ls1")
        rew = st.text_area("Your Paraphrase:", key="lr1")
        if rew:
            sim = ahrens_engine(src, rew)
            st.metric("Cognitive Independence", f"{100-sim:.0f}%")

# --- MODULE II: WILLIAMS ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.subheader("Syllabus & Theory")
        st.markdown("Focus on identifying **Nominalizations** (Zombie Nouns)—verbs turned into heavy nouns that hide agency and slow down the reader.")
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Action Restoration:** Use active verbs.\n* **Character Clarity:** Defined subjects.\n* **Clarity Ratio:** High verb density.")
    with tab_worksheet:
        st.subheader("Worksheet II: Action Identification")
        st.text_input("Sentence to analyze:", key="w2")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        rew2 = st.text_area("Input your research prose:", key="lr2")
        if rew2:
            zombies = williams_engine(rew2)
            if zombies: st.warning(f"Zombie Nouns: {', '.join(zombies)}")
            else: st.success("✅ Clean prose!")

# --- MODULE III: GRAFF & BIRKENSTEIN ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.subheader("Syllabus & Theory")
        st.markdown("Academic writing is a social act. Summarize the 'They Say' before asserting your 'I Say' to create a conversation.")
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Attribution:** Scholar acknowledgment.\n* **The Pivot:** Clear linguistic bridge.\n* **Synthesis:** Added value.")
    with tab_worksheet:
        st.subheader("Worksheet III: The Pivot")
        st.text_area("They Say:", key="w3_t")
        st.text_area("I Say:", key="w3_i")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        rew3 = st.text_area("Scholarly Synthesis:", placeholder="Paste your draft here...", key="lr3")
        if rew3:
            they, pivot = graff_engine(rew3)
            if they and pivot: st.success("✅ Dialectical 'Move' detected!")
            else: st.error("❌ Missing context or pivot marker.")

# --- 6. FOOTER ---
st.divider()
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: grey;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    <div class="footer">
        <p>Created by <b>Vishdom</b> | Academic Synthesis Residency © 2026</p>
    </div>
    """,
    unsafe_allow_html=True
)
