"""
Source policies for controlling where ResearchLM
is allowed to obtain information.
"""


SOURCE_MODES = {
    "uploaded_only": {
        "label": "📚 Uploaded material only",
        "description": (
            "Use only the documents and data provided "
            "by the user."
        ),
        "documents": True,
        "web": False,
    },

    "uploaded_and_web": {
        "label": "📚 + 🌐 Uploaded material + Web",
        "description": (
            "Use uploaded material and external web "
            "sources for research and verification."
        ),
        "documents": True,
        "web": True,
    },

    "web_only": {
        "label": "🌐 Web research only",
        "description": (
            "Use external web sources without relying "
            "on uploaded documents."
        ),
        "documents": False,
        "web": True,
    },
}


def get_source_policy(mode: str) -> dict:
    """
    Return the source policy associated with a mode.

    Raises:
        ValueError: If the requested mode does not exist.
    """

    if mode not in SOURCE_MODES:
        raise ValueError(
            f"Unknown source mode: {mode}"
        )

    return SOURCE_MODES[mode]
