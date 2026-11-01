"""Branding components — modern hero banner shown on the dashboard."""

from __future__ import annotations

import streamlit as st

from src.config.settings import APP_NAME, APP_TAGLINE, APP_VERSION


def brand_hero() -> None:
    """Render the high-impact CareerOS AI branded command center hero."""
    st.markdown(
        f"""
        <div style="background: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.25) 0%, rgba(30, 27, 75, 0.4) 40%, rgba(11, 15, 25, 0.8) 100%), linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.95) 100%); border: 1px solid rgba(99, 102, 241, 0.25); border-radius: 20px; padding: 2.2rem 2.4rem; margin-bottom: 1.8rem; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35); backdrop-filter: blur(16px); position: relative; overflow: hidden;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
                <div style="max-width: 720px;">
                    <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.8rem;">
                        <span style="background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.4); color: #A5B4FC; font-size: 0.72rem; font-weight: 700; padding: 0.25rem 0.65rem; border-radius: 9999px; letter-spacing: 0.5px; text-transform: uppercase;">
                            ✨ Next-Gen Career Intelligence
                        </span>
                        <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); color: #34D399; font-size: 0.72rem; font-weight: 700; padding: 0.25rem 0.65rem; border-radius: 9999px; letter-spacing: 0.5px;">
                            ⚡ Gemini 1.5 Powered
                        </span>
                    </div>
                    <h1 style="font-size: 2.6rem; font-weight: 800; color: #FFFFFF; line-height: 1.15; margin: 0 0 0.6rem 0; letter-spacing: -0.8px;">
                        {APP_NAME} <span style="background: linear-gradient(135deg, #818CF8 0%, #38BDF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Intelligence Hub</span>
                    </h1>
                    <p style="font-size: 1.05rem; color: #CBD5E1; margin: 0 0 1.2rem 0; line-height: 1.5; font-weight: 400;">
                        {APP_TAGLINE} — Optimize resumes, decode job specs, close skill gaps, rehearse voice interviews, and win top offers with verified AI precision.
                    </p>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.8rem;">
                        <span style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.3rem 0.7rem; font-size: 0.78rem; color: #E2E8F0; font-weight: 500;">
                            📄 ATS Resume Intelligence
                        </span>
                        <span style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.3rem 0.7rem; font-size: 0.78rem; color: #E2E8F0; font-weight: 500;">
                            🎯 Job Fit Signal Extraction
                        </span>
                        <span style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.3rem 0.7rem; font-size: 0.78rem; color: #E2E8F0; font-weight: 500;">
                            🎙️ Real-time Mock Coach
                        </span>
                        <span style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.3rem 0.7rem; font-size: 0.78rem; color: #E2E8F0; font-weight: 500;">
                            💰 Salary Negotiator
                        </span>
                        <span style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 8px; padding: 0.3rem 0.7rem; font-size: 0.78rem; color: #A5B4FC; font-weight: 500;">
                            ⚡ CareerOS AI Engine
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
