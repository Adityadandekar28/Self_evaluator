"""Reusable card-style components for the CareerOS UI.

All helpers use Streamlit native primitives (``st.container(border=True)``,
``st.metric``, ``st.caption`` …) enhanced with modern SaaS styling.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st

PLACEHOLDER: str = "--"


def metric_card(
    label: str,
    value: str = PLACEHOLDER,
    hint: Optional[str] = None,
) -> None:
    """A bordered metric card with modern SaaS styling."""
    with st.container(border=True):
        st.metric(label=label, value=value, border=False)
        if hint:
            st.caption(f"💡 {hint}")


def section_header(title: str, subtitle: Optional[str] = None) -> None:
    """A section heading with modern typography and an optional muted subtitle."""
    st.subheader(title)
    if subtitle:
        st.caption(subtitle)


def empty_state_panel(title: str, hint: str) -> None:
    """A helpful empty-state card with visual polish."""
    with st.container(border=True):
        st.markdown(
            f"""
            <div style="padding: 1.2rem 0.8rem; text-align: center;">
                <div style="font-size: 1.8rem; margin-bottom: 0.4rem;">✨</div>
                <div style="font-size: 1rem; font-weight: 700; color: #E2E8F0; margin-bottom: 0.25rem;">
                    {title}
                </div>
                <div style="font-size: 0.82rem; color: #94A3B8; max-width: 480px; margin: 0 auto;">
                    {hint}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def step_row(index: int, label: str, target_module: str, completed: bool = False) -> None:
    """An onboarding step row with status indicator, label, and action button."""
    with st.container(border=True):
        status_col, label_col, button_col = st.columns([0.10, 0.65, 0.25])
        with status_col:
            if completed:
                st.markdown("<span style='font-size: 1.2rem; color: #10B981;'>✅</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='font-size: 1.2rem; color: #6366F1;'>🔵</span>", unsafe_allow_html=True)
        with label_col:
            st.markdown(f"**Step {index}** · {label}")
            if completed:
                st.caption("Completed and active in session")
            else:
                st.caption("Action recommended")
        with button_col:
            btn_label = "View" if completed else "Start"
            if st.button(
                btn_label,
                key=f"step_{target_module}_{index}",
                use_container_width=True,
                type="secondary" if completed else "primary",
            ):
                from src.ui.components.cta import navigate_to
                navigate_to(target_module)
