import streamlit as st
from difflib import SequenceMatcher

# --- 1. CORE CONFIG & SESSION STATE ---
st.set_page_config(page_title="Academic Writing Synthesis Lab", layout="wide")

# Persistent memory keys
input_keys = ["w1", "ls1", "lr1", "w2", "lr2", "w3_t", "w3_i", "lr3"]
for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = ""

# --- 2. THE BIBLIOGRAPHY ---
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
    zombies = ["tion", "ment", "ance", "ence", "ity", "ness", "ization"]
    return [w.strip(",.;:") for w in text.split() if any(s in w.lower() for s in zombies)]

def graff_engine(text):
    has_they = any(t in text.lower() for t in ["assert", "postulate", "contend", "theorize", "according to", "summarize", "claims", "argues"])
    has_pivot = any(p in text.lower() for p in ["nonetheless", "conversely", "however", "whereas", "notwithstanding", "but I argue"])
    return has_they, has_pivot

# --- 4. SIDEBAR ---
st.sidebar.title("🎓 Academic Writing Synthesis Lab")
st.sidebar.markdown("""
Welcome to the **Synthesis Lab**. Refine your research from design to dialectic.
This environment is designed to bridge the gap between formal research and functional prose.
""")
st.sidebar.divider()

phase = st.sidebar.selectbox("Active Module:",
    ["Module I: Epistemological Retrieval",
     "Module II: Stylistic Surgery",
     "Module III: Dialectical Positioning"])

st.sidebar.divider()
st.sidebar.subheader("📚 Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

# Small-font social links at the bottom
st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.divider()
st.sidebar.markdown("""
<div style="font-size: 11px; color: grey;">
    Connect with Vishdom:<br>
    <a href="https://www.linkedin.com/in/vishpatil/" target="_blank" style="color: grey; text-decoration: none;">🔗 LinkedIn</a> |
    <a href="https://github.com/Vishdom" target="_blank" style="color: grey; text-decoration: none;">💻 GitHub</a>
</div>
""", unsafe_allow_html=True)

# --- 5. MAIN INTERFACE ---
tab_course, tab_worksheet, tab_lab = st.tabs(["📖 COURSEWORK & SYLLABUS", "📝 RESEARCH WORKSHEETS", "🧪 ANALYTICAL LAB"])

if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        Sönke Ahrens argues that successful writing and learning depend on a systematic workflow. By converting fleeting thoughts into permanent entries, writers develop arguments from the bottom up.

        **The Core Types of Notes:**
        * **Fleeting Notes:** Temporary reminders.
        * **Literature Notes:** Capturing the essence of a text in your own words.
        * **Permanent Notes:** Atomic, self-contained ideas.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Atomicity:** One idea per note.\n* **Independence:** Readable without the original source.\n* **Connectivity:** Linked to your existing web of knowledge.")
    with tab_worksheet:
        st.session_state.w1 = st.text_area("Draft your Permanent Note:", value=st.session_state.w1)
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase I")
        st.session_state.ls1 = st.text_area("Source Text:", value=st.session_state.ls1)
        st.session_state.lr1 = st.text_area("Your Paraphrase:", value=st.session_state.lr1)
        if st.session_state.lr1:
            st.metric("Cognitive Independence", f"{100-ahrens_engine(st.session_state.ls1, st.session_state.lr1):.0f}%")

elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        Focus on identifying **Nominalizations** (Zombie Nouns)—verbs turned into heavy nouns that hide agency. Restoration of verbs is the key to 'Clarity and Grace' as proposed by Joseph Williams.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Action Restoration:** Main actions expressed as active verbs.\n* **Character Clarity:** The 'subject' is clearly defined.\n* **Clarity Ratio:** High verb-to-noun density.")
    with tab_worksheet:
        st.session_state.w2 = st.text_input("Sentence to analyze:", value=st.session_state.w2)
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase II")
        st.session_state.lr2 = st.text_area("Input research prose:", value=st.session_state.lr2)
        if st.session_state.lr2:
            zombies = williams_engine(st.session_state.lr2)
            if zombies: st.warning(f"Zombie Nouns detected: {', '.join(zombies)}")
            else: st.success("✅ Clean prose! Agency restored.")

elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.subheader("Syllabus & Theory")
        st.markdown("""
        Academic writing is a social act. You must summarize the **'They Say'** (the context) before asserting your **'I Say'**. This creates a conversation rather than a lecture.
        """)
        st.divider()
        st.subheader("🎯 Module Rubric")
        st.markdown("* **Attribution:** Scholarly conversation acknowledged.\n* **The Pivot:** Clear linguistic bridge (e.g., 'However', 'Conversely').\n* **Synthesis:** Your argument adds new value.")
    with tab_worksheet:
        st.session_state.w3_t = st.text_area("They Say (Context):", value=st.session_state.w3_t)
        st.session_state.w3_i = st.text_area("I Say (Argument):", value=st.session_state.w3_i)
    with tab_lab:
        st.header("🧪 Analytical Lab: Phase III")
        st.session_state.lr3 = st.text_area("Scholarly Synthesis:", value=st.session_state.lr3)
        if st.session_state.lr3:
            they, pivot = graff_engine(st.session_state.lr3)
            if they and pivot: st.success("✅ Dialectical 'Move' detected!")
            else: st.error("❌ Missing context or pivot marker.")

# --- 6. PINNED FOOTER ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: grey;
        text-align: center;
        padding: 10px 0;
        font-size: 11px;
        z-index: 1000;
        border-top: 1px solid #f0f2f6;
    }
    </style>
    <div class="footer">
        Created by <b>Vishdom</b> | Academic Writing Synthesis Lab © 2026
    </div>
    """,
    unsafe_allow_html=True
)
