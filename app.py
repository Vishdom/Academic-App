import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. 4-SOURCE BIBLIOGRAPHY ---
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
    },
    "Seely (2005)": {
        "title": "The Oxford Guide to Effective Writing and Speaking.",
        "link": "https://www.amazon.in/Oxford-Guide-Effective-Writing-Speaking/dp/019965285X"
    }
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
st.sidebar.subheader("📚 Primary Source Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

tab_course, tab_worksheet, tab_lab = st.tabs(["📖 COURSEWORK & SYLLABUS", "📝 RESEARCH WORKSHEETS", "🧪 ANALYTICAL LAB"])

# --- 5. MODULE I: AHRENS ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower... [Full Text Restored]

        **The Core Types of Notes**
        * **Fleeting Notes:** Quick reminders captured on the fly.
        * **Literature Notes:** Capturing the gist of a text in your own words.
        * **Permanent Notes:** Self-contained ideas written in full sentences.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        1. **Independence:** Does the note make sense without the original source?
        2. **Atomicity:** Does the note contain exactly *one* idea?
        3. **Connectivity:** Is there a unique address or link to a previous thought?
        """)

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
        st.subheader("Syllabus & Theory")
        st.markdown("Academic writing is often plagued by 'nominalization'—the turning of useful verbs into heavy nouns. Module II focuses on identifying these 'Zombie Nouns' and restoring agency to the sentence.")
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        1. **Verbal Vitality:** Are the primary actions expressed as verbs rather than nouns?
        2. **Character Agency:** Is it clear *who* is doing the action?
        3. **Clarity Score:** Elimination of at least 80% of identified nominalizations.
        """)
    with tab_worksheet:
        st.subheader("Worksheet II: Action Identification")
        st.text_input("Identify the Primary Action (Verb):", key="w2")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        rew2 = st.text_area("Input your writing:", key="lr2")
        if rew2:
            zombies = williams_engine(rew2)
            if zombies: st.warning(f"Zombie Nouns found: {', '.join(zombies)}")
            else: st.success("✅ No Zombie Nouns found!")

# --- 7. MODULE III: GRAFF & BIRKENSTEIN ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        This influential textbook aims to demystify academic discourse by reframing writing as a social act of entering ongoing conversations... [Full Text Restored]
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        1. **Attribution:** Is the 'They Say' clearly stated and attributed?
        2. **The Pivot:** Does the transition to 'I Say' use a clear contrastive marker?
        3. **Synthesis:** Does the argument 'put in an oar' into an existing scholarly parlor?
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
