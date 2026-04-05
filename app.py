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
    # Detects the "They Say" move (attribution)
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    # Detects the "I Say" move (the pivot)
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue", "consequently"])
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

# --- 6. MODULE I CONTENT ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.write("---")
        with st.expander("Sub-Module 1.1: The Principle of Atomicity", expanded=True):
            st.markdown("Focus on Ahrens (2022) and the extraction of atomic propositions.")

# --- 7. MODULE II CONTENT ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.write("---")
        with st.expander("Sub-Module 2.1: The Taxonomy of Obscurity", expanded=True):
            st.markdown("Focus on Williams (1990) and the removal of nominalizations.")

# --- 8. MODULE III CONTENT (CONCEPTS & VERBATIM TEXT) ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.write("---")

        st.subheader("\"They Say / I Say\": The Moves That Matter in Academic Writing by Gerald Graff and Cathy Birkenstein")

        st.info("""
        This influential textbook aims to demystify academic discourse by reframing writing as a social act of entering ongoing conversations.
        The authors argue that effective persuasion requires writers to first summarize the views of others—the "they say"—to establish a
        meaningful context for their own original arguments, or the "I say." To assist students in mastering these rhetorical maneuvers,
        the book provides practical templates that model sophisticated transitions, summaries, and responses. This specific edition introduces
        new guidance on writing about literature, navigating digital communication, and using templates as a tool for substantive revision.
        Ultimately, the text seeks to empower students by showing that critical thinking is an accessible, conversational process rather
        than a mysterious or isolated task.
        """)

        st.markdown("### The Core Logic: The 'Internal DNA' of Argument")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **1. The Primacy of "They Say"**
            * **Motivation:** You write because you are responding to something.
            * **Listening:** Summarize views in a way others would recognize.
            * **Placement:** Establish the context early.
            """)
        with col2:
            st.markdown("""
            **2. The Response of "I Say"**
            * **Moves:** Agree, disagree, or a combination of both.
            * **Nuance:** The "Yes/No" approach allows for complex frameworks.
            * **Voice:** Blend formal academic terms with popular expressions.
            """)

        with st.expander("Sub-Module 3.1: Entering the Conversation", expanded=True):
            st.markdown("""
            - **The Burkian Parlor:** Listen to the tenor of the argument, then "put in your oar."
            - **Mapping Claims:** Map your claims relative to others.
            - **Demystifying Moves:** Using templates as a generative tool for invention.
            """)

    with tab_worksheet:
        st.subheader("Worksheet III-A: Dialectical Bridge")
        st.text_area("Current Scholarly Consensus (The 'They Say'):",
                     placeholder="Identifying and summarizing the views of another group...",
                     key="w3_they")
        st.selectbox("Rhetorical Pivot (The 'Yes/No' Move):",
                     ["Notwithstanding...", "Conversely...", "While I concur with X, I depart on Y...", "However..."],
                     key="w3_pivot")
        st.text_area("Your Counter-Thesis (The 'I Say'):",
                     placeholder="Offering your own argument as a response...",
                     key="w3_isay")

    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        st.caption("This lab checks for the 'Internal DNA' of your argument.")
        col1, col2 = st.columns(2)
        with col1: src3 = st.text_area("1️⃣ Source Material (The Conversation):", height=200, key="lab_s3")
        with col2: rew3 = st.text_area("2️⃣ Scholarly Synthesis (Your Oar):", height=200, key="lab_r3")

        if src3 and rew3:
            they, pivot = graff_engine(rew3)
            c1, c2 = st.columns(2)
            if they: c1.success("✅ 'They Say' move detected.")
            else: c1.error("❌ Missing scholarly context.")

            if pivot: c2.success("✅ 'I Say' pivot detected.")
            else: c2.warning("⚠️ Missing dialectical pivot.")
