# Academic Residency App - Version 1.1
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
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize"])
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

# --- 6. MODULE I CONTENT (AHRENS) ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.write("---")
        with st.expander("Sub-Module 1.1: The Principle of Atomicity", expanded=True):
            st.markdown("""
            **Objective:** Extract 'Atomic' ideas from complex literature.

            **The Logic:** Based on Sönke Ahrens (2022), writing is not the result of thinking; it is the medium in which thinking takes place.
            Highlighting is the enemy of learning because it avoids the "Retrieval Effort" required to move information into long-term memory.

            **Exercise:** Create a standalone proposition from a text. It must remain a "truth" even if the author's name is removed.
            """)


    with tab_worksheet:
        st.subheader("Worksheet I-A: Atomic Proposition Template")
        st.text_input("Full Bibliographic Citation (APA):", key="w1_cite")
        st.text_area("The Core Assertion (Standalone Truth):", height=100, key="w1_assert")
        st.text_area("Cross-Linkage: How does this connect to your existing knowledge?", height=100, key="w1_link")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        col1, col2 = st.columns(2)
        with col1: src1 = st.text_area("1️⃣ Source Material:", height=200, key="lab_s1")
        with col2: rew1 = st.text_area("2️⃣ Scholarly Synthesis:", height=200, key="lab_r1")
        if src1 and rew1:
            sim, tethers = ahrens_engine(src1, rew1)
            st.metric("Cognitive Independence Score", f"{100-sim:.0f}%")
            if sim > 40: st.error("❌ High Structural Mirroring: You are patchwriting.")

# --- 7. MODULE II CONTENT (WILLIAMS) ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.write("---")
        with st.expander("Sub-Module 2.1: The Taxonomy of Obscurity", expanded=True):
            st.markdown("""
            **Objective:** Identification and removal of Nominalization (Zombie Nouns).

            **The Logic:** Based on Joseph Williams (1990), clarity is achieved when the 'Character' of a sentence is the 'Subject',
            and the 'Action' is the 'Verb'.

            **Exercise:** Verb Resurrection. Locate abstract nouns ending in *-tion* or *-ment* and transform them back into primary actions.
            """)


    with tab_worksheet:
        st.subheader("Worksheet II-A: Stylistic Audit")
        st.text_area("Input Turgid Sentence:", key="w2_turgid")
        st.text_input("Identify the Primary Character (Subject):", key="w2_char")
        st.text_input("Identify the Primary Action (Verb):", key="w2_act")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        col1, col2 = st.columns(2)
        with col1: src2 = st.text_area("1️⃣ Source Material:", height=200, key="lab_s2")
        with col2: rew2 = st.text_area("2️⃣ Scholarly Synthesis:", height=200, key="lab_r2")
        if src2 and rew2:
            zombies, heavies = williams_engine(rew2)
            st.metric("Nominalization (Zombie) Count", len(zombies))
            if zombies: st.warning(f"❌ Zombie Nouns Detected: `{set(zombies)}`.")

# --- 8. MODULE III CONTENT (GRAFF & BIRKENSTEIN) ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.write("---")

        st.subheader("The 'They Say / I Say' Framework")
        st.markdown("""
        **The Internal DNA of Argument:** Writing well means entering into a conversation with others rather than simply expressing ideas in a vacuum.

        **1. The Primacy of 'They Say':** Identify and summarize the views of others to set the stage for your own argument.
        Arguments need a "reason for being"—a response to someone else.

        **2. The Response of 'I Say':** Once context is established, offer your argument by agreeing, disagreeing, or a nuanced combination of both.

        **3. Entering the 'Burkian Parlor':** Intellectual exchange is a never-ending conversation. You listen until you understand the tenor, then "put in your oar."
        """)


        with st.expander("Sub-Module 3.1: The Rhetorical Situation", expanded=True):
            st.markdown("""
            - **Objective:** Demystify academic discourse by reframing writing as a social act.
            - **Primary Reading:** Graff & Birkenstein (2014), Chapters 1-3.
            - **Exercise:** The Steel-Man Move. Articulate the strongest version of an opposing viewpoint using Graff's templates before introducing your counter-thesis.
            """)

    with tab_worksheet:
        st.subheader("Worksheet III-A: Dialectical Bridge")
        st.text_area("Current Scholarly Consensus (The 'They Say'):", key="w3_they", help="Establish the 'They Say' to give your argument a reason for being.")
        st.selectbox("Rhetorical Pivot:", ["Notwithstanding...", "Conversely...", "While I concur with the premise of X, I depart on Y...", "Contrary to the view that..."], key="w3_pivot")
        st.text_area("Your Counter-Thesis (The 'I Say'):", key="w3_isay", help="Map your claims relative to the claims of others.")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        col1, col2 = st.columns(2)
        with col1: src3 = st.text_area("1️⃣ Source Material (The Conversation):", height=200, key="lab_s3")
        with col2: rew3 = st.text_area("2️⃣ Scholarly Synthesis (Your Oar):", height=200, key="lab_r3")
        if src3 and rew3:
            they, pivot = graff_engine(rew3)
            c1, c2 = st.columns(2)
            if they: c1.success("✅ 'They Say' Move Detected")
            else: c1.error("❌ Missing Scholarly Attribution")
            if pivot: c2.success("✅ 'I Say' Pivot Detected")
            else: c2.error("❌ Missing Dialectical Pivot")
