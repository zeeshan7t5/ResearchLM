import streamlit as st

from config.settings import APP_NAME, APP_VERSION
from core.source_policy import SOURCE_MODES
from ui.sidebar import render_sidebar


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title=f"{APP_NAME} — AI Research Workspace",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------

if "notebook_name" not in st.session_state:
    st.session_state.notebook_name = "My Research Notebook"

if "source_mode" not in st.session_state:
    st.session_state.source_mode = "uploaded_only"

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main application */

    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }

    /* Cards */

    .feature-card {
        padding: 1.4rem;
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 14px;
        min-height: 150px;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-size: 1.1rem;
        font-weight: 650;
        margin-bottom: 0.5rem;
    }

    .feature-description {
        color: #6b7280;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    /* Status */

    .status-box {
        padding: 1rem 1.2rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 1rem;
    }

    .small-text {
        font-size: 0.85rem;
        color: #6b7280;
    }

    /* Hide Streamlit footer */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

render_sidebar()


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    f'<div class="main-title">📚 {APP_NAME}</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Your AI workspace for research, document analysis, "
    "verification, comparison, and learning."
    "</div>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Current workspace information
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Notebook",
        st.session_state.notebook_name,
    )

with col2:
    st.metric(
        "Sources",
        len(st.session_state.uploaded_files),
    )

with col3:
    mode_name = SOURCE_MODES[
        st.session_state.source_mode
    ]["label"]

    st.metric(
        "Source Mode",
        mode_name,
    )


st.divider()


# ---------------------------------------------------------
# Main workspace
# ---------------------------------------------------------

page = st.session_state.active_page


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.subheader("Welcome to ResearchLM")

    st.write(
        """
        ResearchLM is being built as an agentic research and
        learning workspace. You will be able to upload your
        research material, ask questions, compare sources,
        verify claims against the web, and generate study
        materials.
        """
    )

    st.markdown("### What you will be able to do")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📄 Analyze Documents</div>
                <div class="feature-description">
                    Upload PDFs, DOCX files, text files and
                    other supported research material.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">🔎 Verify Information</div>
                <div class="feature-description">
                    Compare information in your sources with
                    external web evidence when verification is enabled.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-title">📝 Generate</div>
                <div class="feature-description">
                    Create summaries, reports, flashcards,
                    quizzes and structured research outputs.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Start with your research material")

    uploaded_files = st.file_uploader(
        "Upload your research files",
        type=[
            "pdf",
            "docx",
            "txt",
            "md",
            "csv",
        ],
        accept_multiple_files=True,
        help=(
            "Your files will be processed by ResearchLM in "
            "later milestones."
        ),
    )

    if uploaded_files:

        st.session_state.uploaded_files = [
            {
                "name": file.name,
                "type": file.type,
                "size": file.size,
            }
            for file in uploaded_files
        ]

        st.success(
            f"{len(uploaded_files)} file(s) selected."
        )

        st.markdown("#### Selected sources")

        for file in uploaded_files:
            st.write(
                f"📄 **{file.name}** — "
                f"{file.size / 1024:.1f} KB"
            )

        st.info(
            "Document processing and RAG will be enabled in "
            "Milestone 2."
        )


# =========================================================
# NOTEBOOK
# =========================================================

elif page == "Notebook":

    st.subheader("📚 Research Notebook")

    notebook_name = st.text_input(
        "Notebook name",
        value=st.session_state.notebook_name,
    )

    if notebook_name:
        st.session_state.notebook_name = notebook_name

    st.markdown("### Sources")

    if st.session_state.uploaded_files:

        for file in st.session_state.uploaded_files:

            st.write(
                f"📄 **{file['name']}**"
            )

    else:

        st.info(
            "No sources have been added yet. "
            "Upload documents from the Home page."
        )

    st.markdown("### Conversations")

    st.info(
        "Conversation history will be implemented in a "
        "future milestone."
    )


# =========================================================
# ANALYZE
# =========================================================

elif page == "Analyze":

    st.subheader("🔬 Analyze")

    if not st.session_state.uploaded_files:

        st.warning(
            "Upload at least one document before starting an analysis."
        )

    else:

        analysis_type = st.selectbox(
            "Analysis type",
            [
                "General analysis",
                "Key findings",
                "Methods",
                "Results",
                "Important concepts",
                "Extract structured information",
            ],
        )

        question = st.text_area(
            "What would you like to analyze?",
            placeholder=(
                "Example: Identify the major findings "
                "reported across these papers."
            ),
        )

        if st.button(
            "Run Analysis",
            type="primary",
            use_container_width=True,
        ):

            st.info(
                "The analysis engine will be connected "
                "in the RAG and CrewAI milestones."
            )


# =========================================================
# VERIFY
# =========================================================

elif page == "Verify":

    st.subheader("🔎 Verify")

    st.write(
        """
        Verification will allow ResearchLM to examine claims
        in your uploaded material and optionally compare them
        with external web evidence.
        """
    )

    verification_type = st.selectbox(
        "Verification scope",
        [
            "Selected claim",
            "Document",
            "All important claims",
            "References and citations",
        ],
    )

    if st.button(
        "Start Verification",
        type="primary",
        use_container_width=True,
    ):

        st.info(
            "Web search, evidence retrieval and verification "
            "agents will be connected in a later milestone."
        )


# =========================================================
# COMPARE
# =========================================================

elif page == "Compare":

    st.subheader("⚖️ Compare")

    st.write(
        """
        Compare multiple documents, claims, findings,
        methodologies, or uploaded material against
        external evidence.
        """
    )

    comparison_type = st.selectbox(
        "Comparison type",
        [
            "Document vs Document",
            "Document vs Web",
            "Multiple Documents",
            "Claim vs Evidence",
        ],
    )

    st.selectbox(
        "Comparison output",
        [
            "Detailed comparison",
            "Comparison table",
            "Similarities and differences",
            "Contradictions",
        ],
    )

    if st.button(
        "Run Comparison",
        type="primary",
        use_container_width=True,
    ):

        st.info(
            "The comparison workflow will be implemented "
            "using RAG and CrewAI."
        )


# =========================================================
# GENERATE
# =========================================================

elif page == "Generate":

    st.subheader("📝 Generate")

    generation_type = st.selectbox(
        "What would you like to generate?",
        [
            "Summary",
            "Research Report",
            "Literature Review",
            "Flashcards",
            "Quiz",
            "Key Concepts",
            "Study Notes",
        ],
    )

    detail_level = st.selectbox(
        "Detail level",
        [
            "Short",
            "Medium",
            "Detailed",
        ],
    )

    if st.button(
        "Generate",
        type="primary",
        use_container_width=True,
    ):

        st.info(
            "Generation workflows will be connected "
            "after the RAG and CrewAI layers are implemented."
        )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    f"{APP_NAME} v{APP_VERSION} • "
    "Built with Streamlit • AI research workspace"
)