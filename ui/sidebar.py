import streamlit as st

from config.settings import APP_NAME, APP_VERSION
from core.source_policy import SOURCE_MODES


def render_sidebar():
    """
    Render the main ResearchLM sidebar.
    """

    with st.sidebar:

        st.markdown(
            f"""
            # 📚 {APP_NAME}

            <div style="
                color: #6b7280;
                font-size: 0.85rem;
                margin-bottom: 1rem;
            ">
                AI Research Workspace
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # -------------------------------------------------
        # Navigation
        # -------------------------------------------------

        st.markdown("### Workspace")

        pages = {
            "🏠 Home": "Home",
            "📚 Notebook": "Notebook",
            "🔬 Analyze": "Analyze",
            "🔎 Verify": "Verify",
            "⚖️ Compare": "Compare",
            "📝 Generate": "Generate",
        }

        for label, page_name in pages.items():

            if st.button(
                label,
                key=f"nav_{page_name}",
                use_container_width=True,
            ):
                st.session_state.active_page = page_name

        st.divider()

        # -------------------------------------------------
        # Source Mode
        # -------------------------------------------------

        st.markdown("### 🔐 Source Mode")

        mode_options = list(SOURCE_MODES.keys())

        current_mode = st.session_state.get(
            "source_mode",
            "uploaded_only",
        )

        current_index = mode_options.index(
            current_mode
        )

        selected_mode = st.radio(
            "Information sources",
            options=mode_options,
            index=current_index,
            format_func=lambda mode: SOURCE_MODES[
                mode
            ]["label"],
        )

        st.session_state.source_mode = selected_mode

        st.caption(
            SOURCE_MODES[selected_mode]["description"]
        )

        st.divider()

        # -------------------------------------------------
        # Current Notebook
        # -------------------------------------------------

        st.markdown("### 📓 Current Notebook")

        st.caption(
            st.session_state.get(
                "notebook_name",
                "My Research Notebook",
            )
        )

        st.divider()

        # -------------------------------------------------
        # Status
        # -------------------------------------------------

        st.markdown("### System")

        st.success("Application online")

        st.caption(
            f"ResearchLM v{APP_VERSION}"
        )
