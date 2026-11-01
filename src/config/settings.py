"""Application configuration & module registry.

Centralizes app metadata and the ordered list of navigation modules. The
sidebar is rendered *data-driven* from :data:`MODULES`, so updating the
list here automatically updates the sidebar (see ``src/ui/layout.py``).

Adding / reordering modules is a one-place change: edit :data:`MODULES`,
create a package under ``src/modules/<key>/`` exposing ``render()``, and
register it in ``src/modules/__init__.py``'s dispatcher.
"""

from __future__ import annotations

APP_NAME: str = "Self Evaluator"
APP_TAGLINE: str = "AI Career Intelligence & Evaluation Copilot"
APP_VERSION: str = "1.0.0"

# Ordered module registry — order defines sidebar navigation order.
# Each entry: {key, name, icon, description, status}
MODULES: list[dict[str, str]] = [
    {
        "key": "dashboard",
        "name": "Dashboard",
        "icon": "🏠",
        "description": "Your career command center — scores, readiness, and next steps at a glance.",
        "status": "Ready",
    },
    {
        "key": "resume_intelligence",
        "name": "Resume Intelligence",
        "icon": "📄",
        "description": "Parse, analyze, and optimize resumes for ATS compatibility and recruiter readability.",
        "status": "Active",
    },
    {
        "key": "jd_analysis",
        "name": "Job Match",
        "icon": "🎯",
        "description": "Analyze job descriptions and measure match against your profile.",
        "status": "Active",
    },
    {
        "key": "skill_gap",
        "name": "Skill Gap",
        "icon": "🧠",
        "description": "Compare your skills against target roles to surface actionable gaps.",
        "status": "Active",
    },
    {
        "key": "career_roadmap",
        "name": "Career Roadmap",
        "icon": "🗺️",
        "description": "Generate tailored, milestone-based career growth plans with learning resources.",
        "status": "Active",
    },
    {
        "key": "application_copilot",
        "name": "Application Copilot",
        "icon": "✍️",
        "description": "Draft tailored cover letters, outreach messages, and application materials.",
        "status": "Active",
    },
    {
        "key": "rag",
        "name": "RAG",
        "icon": "📚",
        "description": "Ground AI responses in your uploaded documents for accurate, citation-backed answers.",
        "status": "Active",
    },
    {
        "key": "voice_interview",
        "name": "AI Interview",
        "icon": "🎤",
        "description": "Practice realistic mock interviews with live feedback and scoring.",
        "status": "Active",
    },
    {
        "key": "salary_negotiation",
        "name": "Salary Negotiator",
        "icon": "💰",
        "description": "Benchmark compensation and rehearse data-backed negotiation scripts.",
        "status": "Active",
    },
    {
        "key": "evaluation_dashboard",
        "name": "Evaluation",
        "icon": "📊",
        "description": "Track your progress, AI answer quality, and engagement over time.",
        "status": "Active",
    },
]


def get_module(key: str) -> dict[str, str] | None:
    """Return the module descriptor for ``key`` or ``None``."""
    return next((m for m in MODULES if m["key"] == key), None)


# Fallback entrypoint if Streamlit Cloud is configured with main module: src/config/settings.py
if __name__ == "__main__":
    import sys
    from pathlib import Path

    _root = Path(__file__).resolve().parent.parent.parent
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

    import app
    app.main()

