"""Reusable Streamlit layout helpers (sidebar, header, chrome polish)."""

from __future__ import annotations

import streamlit as st

from src.config.settings import APP_NAME, APP_TAGLINE, MODULES
from src.ui.components.cta import navigate_to

# Complete elimination of Streamlit developer chrome for a true SaaS web experience
_CHROME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

/* Completely hide all Streamlit developer chrome, deploy button, status & hamburger */
#MainMenu {visibility: hidden !important; display: none !important;}
footer {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
[data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
.stDeployButton {display: none !important;}
#stDecoration {display: none !important;}
button[title="View fullscreen"] {display: none !important;}
.viewerBadge_container__1QSob {display: none !important;}
[data-testid="collapsedControl"] {top: 1rem !important; left: 1rem !important;}

/* Clean page container spacing */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

/* Base Typography */
html, body, [class*="css"], .stMarkdown, p, div, button {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif !important;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: #080C14 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
}

/* Primary Button Styling */
button[kind="primary"] {
    background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
button[kind="primary"]:hover {
    background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.55) !important;
    transform: translateY(-1.5px) !important;
}

/* Secondary Button Styling */
button[kind="secondary"] {
    background: rgba(19, 27, 46, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #CBD5E1 !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
button[kind="secondary"]:hover {
    background: rgba(30, 41, 59, 0.95) !important;
    border-color: rgba(99, 102, 241, 0.4) !important;
    color: #FFFFFF !important;
    transform: translateY(-1.5px) !important;
}

/* Card / Container Styling */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(19, 27, 46, 0.75) 0%, rgba(13, 19, 33, 0.85) 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
    backdrop-filter: blur(12px) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(99, 102, 241, 0.35) !important;
    box-shadow: 0 6px 24px rgba(99, 102, 241, 0.15) !important;
}

/* Metric Display Styling */
[data-testid="stMetricValue"] {
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

/* Progress bar */
[data-testid="stProgressBar"] > div {
    background: rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
}
[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #6366F1 0%, #06B6D4 100%) !important;
    border-radius: 8px !important;
    box-shadow: 0 0 12px rgba(99, 102, 241, 0.5) !important;
}

/* Alert Boxes */
.stAlert {
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(8px) !important;
}

/* Custom Nav Group Header */
.nav-category {
    font-size: 0.68rem;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin: 1.2rem 0 0.4rem 0.2rem;
}
</style>
"""


def inject_chrome_css() -> None:
    """Hide Streamlit's default chrome and style as a standalone production web app."""
    st.markdown(_CHROME_CSS, unsafe_allow_html=True)


def render_sidebar() -> None:
    """Render the production branded sidebar without developer clutter."""
    with st.sidebar:
        # App Logo & Brand Header
        st.markdown(
            f"""
            <div style="padding: 0.4rem 0 0.8rem 0;">
                <div style="display: flex; align-items: center; gap: 0.7rem;">
                    <div style="background: linear-gradient(135deg, #6366F1, #3B82F6); width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);">
                        ⚡
                    </div>
                    <div>
                        <div style="font-size: 1.25rem; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">
                            {APP_NAME}
                        </div>
                        <div style="font-size: 0.70rem; color: #94A3B8; font-weight: 500;">
                            {APP_TAGLINE}
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        current = st.session_state.get("selected_module", MODULES[0]["key"])

        # Navigation Groups
        groups = [
            ("COMMAND CENTER", ["dashboard"]),
            ("INTELLIGENCE & FIT", ["resume_intelligence", "jd_analysis", "skill_gap"]),
            ("GROWTH & COPILOT", ["career_roadmap", "application_copilot", "rag"]),
            ("INTERVIEW & OFFERS", ["voice_interview", "salary_negotiation", "evaluation_dashboard"]),
        ]

        mod_map = {m["key"]: m for m in MODULES}

        for category_title, module_keys in groups:
            st.markdown(f'<div class="nav-category">{category_title}</div>', unsafe_allow_html=True)
            for m_key in module_keys:
                module = mod_map.get(m_key)
                if not module:
                    continue
                is_active = module["key"] == current
                if st.button(
                    f"{module['icon']}  {module['name']}",
                    key=f"nav_{module['key']}",
                    use_container_width=True,
                    type="primary" if is_active else "secondary",
                ):
                    navigate_to(module["key"])

        st.divider()

        # Clean Production Status Footer (No dev/API clutter)
        st.markdown(
            """
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 0.7rem 0.9rem; display: flex; align-items: center; gap: 0.6rem; margin-top: 0.5rem;">
                <div style="width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, #6366F1, #38BDF8); display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; color: white;">
                    SE
                </div>
                <div>
                    <div style="font-size: 0.78rem; font-weight: 700; color: #F1F5F9;">Self Evaluator</div>
                    <div style="font-size: 0.68rem; color: #10B981; font-weight: 500;">● System Active</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_header(selected_key: str) -> None:
    """Render a polished module hero banner."""
    from src.config.settings import get_module

    module = get_module(selected_key) or MODULES[0]
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.7) 100%); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 1.2rem 1.6rem; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(12px);">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(59, 130, 246, 0.2)); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 12px; width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; font-size: 1.6rem;">
                    {module['icon']}
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 0.6rem;">
                        <span style="font-size: 1.4rem; font-weight: 800; color: #FFFFFF; letter-spacing: -0.3px;">{module['name']}</span>
                        <span style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #818CF8; font-size: 0.68rem; font-weight: 700; padding: 0.15rem 0.5rem; border-radius: 9999px; text-transform: uppercase;">Active</span>
                    </div>
                    <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.15rem;">{module['description']}</div>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 0.75rem; color: #64748B;">Self Evaluator</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Render a clean website footer."""
    st.markdown(
        """
        <div style="margin-top: 3.5rem; padding: 1.8rem 0; border-top: 1px solid rgba(255, 255, 255, 0.06); text-align: center; color: #64748B; font-size: 0.78rem;">
            © 2026 Self Evaluator · Intelligent Career Copilot & Evaluation Engine · All Rights Reserved
        </div>
        """,
        unsafe_allow_html=True,
    )
