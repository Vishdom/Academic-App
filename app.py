import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. THE CORRECT 4-SOURCE BIBLIOGRAPHY ---
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
    "Neville (2016)": {
        "title": "The Complete Guide to Referencing and Avoiding Plagiarism (Colin Neville).",
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
        Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower. By converting fleeting thoughts into permanent entries, writers develop arguments from the bottom up.

        **The Core Types of Notes:**
        * **Fleeting Notes:** Temporary reminders to be processed quickly.
        * **Literature Notes:** Capturing the essence of a text in your own words.
        * **Permanent Notes:** Atomic, self-contained ideas filed for the long-term.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        * **Atomicity:** Does the note contain exactly one idea?
        * **Independence:** Is the note readable without the original source context?
        * **Connectivity:** Is it linked to at least one existing note in your web?
        """)
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

# --- 6. MODULE II: WILLIAMS ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.subheader("Syllabus & Theory")
        st.markdown("Focus on identifying **Nominalizations** (Zombie Nouns)—verbs turned into heavy nouns that hide agency and slow down the reader. Restoration of verbs is the key to 'Clarity and Grace'.")
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        * **Action Restoration:** Are the main actions expressed as active verbs?
        * **Character Clarity:** Is the 'subject' of every sentence clearly defined?
        * **Clarity Ratio:** Aim for a high verb-to-noun density.
        """)
    with tab_worksheet:
        st.subheader("Worksheet II: Action Identification")
        st.text_input("Sentence to analyze:", key="w2")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        rew2 = st.text_area("Input your research prose:", key="lr2")
        if rew2:
            zombies = williams_engine(rew2)
            if zombies: st.warning(f"Zombie Nouns detected: {', '.join(zombies)}")
            else: st.success("✅ Clean prose! No significant nominalizations found.")

# --- 7. MODULE III: GRAFF & BIRKENSTEIN ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        Academic writing is a social act. You must summarize the 'They Say' (the context/other views) before asserting your 'I Say'. This creates a conversation rather than a lecture.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("""
        * **Attribution:** Is the existing scholarly conversation acknowledged?
        * **The Pivot:** Is there a clear linguistic bridge (e.g., 'However', 'Conversely')?
        * **Synthesis:** Does your argument add new value to the discussion?
        """)
    with tab_worksheet:
        st.subheader("Worksheet III: The Pivot")
        st.text_area("They Say (The Context):", key="w3_t")
        st.text_area("I Say (Your Argument):", key="w3_i")
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        rew3 = st.text_area("Scholarly Synthesis:", placeholder="Paste your draft here...", key="lr3")
        if rew3:
            they, pivot = graff_engine(rew3)
            if they and pivot: st.success("✅ Dialectical 'Move' detected! You have established a conversation.")
            else: st.error("❌ Missing 'They Say' context or 'I Say' pivot marker.")
