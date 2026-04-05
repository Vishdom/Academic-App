import streamlit as st
from difflib import SequenceMatcher
import re

# --- 1. CORE CONFIG ---
st.set_page_config(page_title="Academic Synthesis Residency", layout="wide")

# --- 2. PRIMARY SOURCE BIBLIOGRAPHY ---
BIBLIOGRAPHY = {
    "Ahrens (2022)": {
        "title": "How to Take Smart Notes (Sönke Ahrens)",
        "link": "https://www.amazon.in/How-Take-Smart-Notes-Technique/dp/3982438802"
    },
    "Williams (1990)": {
        "title": "Style: Toward Clarity and Grace (Joseph Williams)",
        "link": "https://www.amazon.com/Style-Lessons-Clarity-Grace-12th/dp/0134080416"
    },
    "Graff & Birkenstein (2014)": {
        "title": "They Say / I Say (Graff & Birkenstein)",
        "link": "https://www.amazon.in/They-Say-Matter-Academic-Writing/dp/0393631672"
    }
}

# --- 3. ANALYTICAL ENGINES ---
def zettel_check(text):
    sentences = re.split(r'[.!?]+', text)
    full_sentences = [s for s in sentences if len(s.split()) > 5]
    return len(full_sentences) > 0

def ahrens_engine(original, rewrite):
    sim = SequenceMatcher(None, original, rewrite).ratio() * 100
    return sim

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
st.sidebar.subheader("📚 Bibliography")
for key, info in BIBLIOGRAPHY.items():
    st.sidebar.page_link(info["link"], label=info["title"])

# --- 5. TAB SYSTEM ---
tab_course, tab_worksheet, tab_lab = st.tabs([
    "📖 COURSEWORK & SYLLABUS",
    "📝 RESEARCH WORKSHEETS",
    "🧪 ANALYTICAL LAB"
])

# --- 6. MODULE I: EPISTEMOLOGICAL RETRIEVAL ---
if phase == "Module I: Epistemological Retrieval":
    with tab_course:
        st.header("Module I: Epistemological Retrieval")
        st.subheader("How to Take Smart Notes by Sönke Ahrens")
        st.markdown("""
        Sönke Ahrens argues that successful writing and learning depend on a systematic workflow rather than raw willpower or isolated brainstorming. He introduces the Zettelkasten, or slip-box method, a technique used by sociologist Niklas Luhmann to build a decentralized network of interconnected ideas over several decades. By converting fleeting thoughts and reading notes into permanent, self-contained entries, writers can develop complex arguments from the bottom up rather than facing the "myth of the blank page." This approach treats writing as the primary medium of thinking, allowing researchers to externalize their memory and focus their mental energy on making creative connections. Ultimately, Ahrens emphasizes that a simple, tool-agnostic structure enables flow and expertise by breaking down the amorphous task of authorship into manageable, interlocking steps.
        """)

        st.divider()
        st.subheader("The Concept: The Slip-box Method (Zettelkasten)")
        st.markdown("""
        The Slip-box Method (also known as the Zettelkasten) is a decentralized, bottom-up system for note-taking and knowledge management designed to turn thoughts and research into a productive "dialogue partner." Originally perfected by the social scientist Niklas Luhmann, the method focuses on creating a web of interconnected ideas rather than just archiving isolated facts.

        **The Core Types of Notes**
        * **Fleeting Notes:** Quick reminders or ideas captured on the fly. They are temporary and meant to be processed and deleted within a day or two once their content is moved into more permanent forms.
        * **Literature Notes:** Taken while reading, these notes capture the gist of a text in your own words, accompanied by bibliographic details. They are kept in a reference management system.
        * **Permanent Notes:** These are the heart of the system. Each note contains a single, self-contained idea, written in full sentences as if for publication. These are filed into the slip-box and never thrown away.

        **Key Mechanics of the Method**
        * **Standardization:** All notes are in the same format, which allows them to be shuffled, combined, and compared easily.
        * **Unique Addressing:** Every note has a fixed, permanent number. This allows for bi-directional linking.
        * **Note Sequences:** If a new idea follows up on an existing one, it is filed directly "behind" it (e.g., note 22a follows note 22). This allows branches of thought to grow indefinitely and organically.
        * **The Index:** Unlike a book index that points to everything, the slip-box index serves only as an "entry point" to specific clusters or lines of thought.

        **The Philosophy: Thinking Outside the Brain**
        The method is based on the idea that writing is the medium of thinking, not just a record of it. By externalizing ideas into a reliable system, you free up your short-term memory to focus on high-level tasks like making connections and generating insights.
        """)

# --- 7. MODULE II: STYLISTIC SURGERY ---
elif phase == "Module II: Stylistic Surgery":
    with tab_course:
        st.header("Module II: Stylistic Surgery")
        st.subheader("Style: Toward Clarity and Grace by Joseph M. Williams")
        st.markdown("""
        Academic writing is often plagued by "nominalization"—the turning of useful verbs into heavy nouns (e.g., 'Implementation' instead of 'Implement'). Module II focuses on identifying these "Zombie Nouns" and restoring agency to the sentence.
        """)

# --- 8. MODULE III: DIALECTICAL POSITIONING ---
elif phase == "Module III: Dialectical Positioning":
    with tab_course:
        st.header("Module III: Dialectical Positioning")
        st.subheader("\"They Say / I Say\": The Moves That Matter in Academic Writing by Gerald Graff and Cathy Birkenstein")
        st.markdown("""
        This influential textbook aims to demystify academic discourse by reframing writing as a social act of entering ongoing conversations. The authors argue that effective persuasion requires writers to first summarize the views of others—the "they say"—to establish a meaningful context for their own original arguments, or the "I say." To assist students in mastering these rhetorical maneuvers, the book provides practical templates that model sophisticated transitions, summaries, and responses. This specific edition introduces new guidance on writing about literature, navigating digital communication, and using templates as a tool for substantive revision. Ultimately, the text seeks to empower students by showing that critical thinking is an accessible, conversational process rather than a mysterious or isolated task.
        """)

        st.divider()
        st.subheader("The Concept: The 'Internal DNA' of Argument")
        st.markdown("""
        "They Say / I Say" logic represents the deep, underlying structure—the "internal DNA"—of all effective argument. At its core, it is the idea that writing well means entering into a conversation with others rather than simply expressing ideas in a vacuum.

        **1. The Primacy of "They Say"**
        The "they say" stage involves identifying and summarizing the views of some other person or group to set the stage for your own argument.
        * **Motivation for Writing:** Writers make arguments because someone else has said something and they feel the need to respond.
        * **Listening Closely:** Summarize views in a way they would recognize.

        **2. The Response of "I Say"**
        Once context is established, you offer your own argument as a response.
        * **Ways of Responding:** Agreeing, disagreeing, or a combination of both ("Yes, but...").
        * **Using Your Own Voice:** Blending formal academic terms with everyday language.

        **3. Entering the Conversation**
        Intellectual exchange is a "Burkian Parlor"—a never-ending conversation where you listen until you understand the tenor and then "put in your oar." Writing is treated as a social act.

        **4. Demystifying the "Moves"**
        The logic is put into practice through templates that act as a generative tool for invention, helping you find something to say by considering what others might think or how a naysayer might object.
        """)

# --- Shared Lab/Worksheet logic for all modules ---
with tab_worksheet:
    st.info("Record your progress for the selected module here.")
with tab_lab:
    st.info("Use the Analytical Lab to test your prose against the residency requirements.")
