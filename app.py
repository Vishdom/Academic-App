import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. PRIMARY SOURCE BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {
        "title": "Ahrens, S. (2022). How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking.",
        "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"
    },
    "Williams (1990)": {
        "title": "Williams, J. M. (1990). Style: Toward Clarity and Grace.",
        "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"
    },
    "Graff & Birkenstein (2014)": {
        "title": "Graff, G., & Birkenstein, C. (2014). They Say / I Say: The Moves That Matter in Academic Writing.",
        "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"
    },
    "Neville (2010)": {
        "title": "Neville, C. (2010). The Complete Guide to Referencing and Avoiding Plagiarism.",
        "link": "https://www.amazon.in/Complete-Guide-Referencing-Avoiding-Plagiarism/dp/0335262023"
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
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.split()) > 5]
    heavy_starts = []
    for s in sentences:
        words_in_s = s.split()
        if sum(1 for w in words_in_s[:7] if any(suf in w.lower() for suf in zombie_suffixes)) >= 2:
            heavy_starts.append(" ".join(words_in_s[:7]))
    return zombies, heavy_starts

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding"])
    return has_they, has_pivot

# --- 4. NAVIGATION ---
st.sidebar.title("🎓 Residency Progress")

# Using a simplified list for selection to avoid string mismatch errors
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

# --- 6. MODULE I CONTENT ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.write("---")
        with st.expander("Sub-Module 1.1: The Principle of Atomicity", expanded=True):
            st.markdown("""
            - **Objective:** Extract 'Atomic' ideas from complex literature.
            - **Primary Reading:** Ahrens (2022), Chapters 2-4.
            - **Exercise:** Create a standalone proposition that functions as a truth without an author's name.
            """)
        with st.expander("Sub-Module 1.2: Elaborative Encoding"):
            st.markdown("""
            - **Objective:** Reconstructing theoretical arguments from memory.
            - **Primary Reading:** Neville (2010), Section on 'Structural Plagiarism'.
            - **Exercise:** The 15-Minute Blackout. Reconstruct an argument after 15 minutes of silence.
            """)

    with tab_worksheet:
        st.subheader("Worksheet I-A: Atomic Proposition Template")
        st.text_input("Full Bibliographic Citation (APA):")
        st.text_area("The Core Assertion (Standalone Truth):", height=100)
        st.text_area("Cross-Linkage: How does this connect to your existing knowledge base?", height=100)

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        col1, col2 = st.columns(2)
        with col1: src = st.text_area("1️⃣ Source Material:", height=200, key="s1")
        with col2: rew = st.text_area("2️⃣ Scholarly Synthesis:", height=200, key="r1")
        if src and rew:
            sim, tethers = ahrens_engine(src, rew)
            st.metric("Cognitive Independence Score", f"{100-sim:.0f}%")
            if sim > 40: st.error("❌ High Structural Mirroring detected.")
            if tethers: st.warning(f"⚠️ Rhetorical Tethering found: `{tethers}`.")

# --- 7. MODULE II CONTENT ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.write("---")
        with st.expander("Sub-Module 2.1: The Taxonomy of Obscurity", expanded=True):
            st.markdown("""
            - **Objective:** Identification of Nominalization (Zombie Nouns).
            - **Primary Reading:** Williams (1990), Chapter 3: 'Actions'.
            - **Exercise:** Transform abstract nouns into primary actions.
            """)
        with st.expander("Sub-Module 2.2: Agent-Action Proximity"):
            st.markdown("""
            - **Objective:** Bringing the 'Doer' and 'Action' to the front.
            - **Primary Reading:** Williams (1990), Chapter 4: 'Characters'.
            - **Exercise:** Ensure actions occur within the first 7 words.
            """)

    with tab_worksheet:
        st.subheader("Worksheet II-A: Stylistic Audit")
        st.text_area("Input Turgid Sentence:", key="w2_1")
        st.text_input("Identify the Primary Character (Subject):", key="w2_2")
        st.text_input("Identify the Primary Action (Verb):", key="w2_3")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        col1, col2 = st.columns(2)
        with col1: src_2 = st.text_area("1️⃣ Source Material:", height=200, key="s2")
        with col2: rew_2 = st.text_area("2️⃣ Scholarly Synthesis:", height=200, key="r2")
        if src_2 and rew_2:
            zombies, heavies = williams_engine(rew_2)
            st.metric("Nominalization (Zombie) Count", len(zombies))
            if zombies: st.warning(f"❌ Zombie Nouns Detected: `{set(zombies)}`.")
            if heavies: st.info(f"💡 Delayed Action: `{heavies[0]}...` ")

# --- 8. MODULE III CONTENT ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.write("---")
        with st.expander("Sub-Module 3.1: The Rhetorical Situation", expanded=True):
            st.markdown("""
            - **Objective:** Establishing the 'They Say' framework.
            - **Primary Reading:** Graff & Birkenstein (2014), Chapters 1-3.
            - **Exercise:** The Steel-Man Move. Articulate the opposition's strongest argument first.
            """)

    with tab_worksheet:
        st.subheader("Worksheet III-A: Dialectical Bridge")
        st.text_area("Current Scholarly Consensus (The 'They Say'):", key="w3_1")
        st.selectbox("Rhetorical Pivot:", ["Notwithstanding...", "Conversely...", "While I concur with..."], key="w3_2")
        st.text_area("Your Counter-Thesis (The 'I Say'):", key="w3_3")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        col1, col2 = st.columns(2)
        with col1: src_3 = st.text_area("1️⃣ Source Material:", height=200, key="s3")
        with col2: rew_3 = st.text_area("2️⃣ Scholarly Synthesis:", height=200, key="r3")
        if src_3 and rew_3:
            they, pivot = graff_engine(rew_3)
            c1, c2 = st.columns(2)
            if they: c1.success("✅ 'They Say' Detected")
            else: c1.error("❌ Missing Scholarly Attribution")
            if pivot: c2.success("✅ 'I Say' Pivot Detected")
            else: c2.error("❌ Missing Dialectical Pivot")
