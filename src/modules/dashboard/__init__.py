"""Dashboard module — the CareerOS AI command center.

Renders the high-impact SaaS-style landing dashboard:
branding hero, live dynamic score cards, interactive career-progress
indicator, onboarding checklist with dynamic completion states,
real recent-activity feed, and quick action cards.
"""

from __future__ import annotations

import streamlit as st

from src.ui.components.branding import brand_hero
from src.ui.components.cards import (
    empty_state_panel,
    metric_card,
    section_header,
    step_row,
)
from src.ui.components.cta import nav_cta

MODULE_NAME: str = "Dashboard"
MODULE_KEY: str = "dashboard"
MODULE_DESCRIPTION: str = "Your career command center."

_ONBOARDING_STEPS: list[tuple[str, str, str]] = [
    ("Upload & optimize your resume", "resume_intelligence", "resume_analysis"),
    ("Target and match a job description", "jd_analysis", "match_analysis"),
    ("Assess your skill gaps & priorities", "skill_gap", "skill_gap_report"),
    ("Generate your personalized career roadmap", "career_roadmap", "career_roadmap"),
    ("Practice a simulated AI mock interview", "voice_interview", "interview_session"),
]

_TOTAL_STEPS: int = len(_ONBOARDING_STEPS)


def render() -> None:
    """Render the modern CareerOS AI command center."""
    brand_hero()
    _render_score_cards()
    _render_career_progress()
    _render_onboarding_and_activity()
    _render_quick_actions()


def _get_completed_steps() -> list[bool]:
    """Check session state for actual completed steps."""
    completed = []
    # 1. Resume
    completed.append(bool(st.session_state.get("resume_analysis") or st.session_state.get("resume_text")))
    # 2. Job Match
    completed.append(bool(st.session_state.get("match_analysis") or st.session_state.get("job_analysis")))
    # 3. Skill Gap
    completed.append(bool(st.session_state.get("skill_gap_report")))
    # 4. Roadmap
    completed.append(bool(st.session_state.get("career_roadmap")))
    # 5. Interview
    completed.append(bool(st.session_state.get("interview_session") or st.session_state.get("interview_report")))
    return completed


def _render_score_cards() -> None:
    section_header("Live Career Snapshot", "Real-time metrics derived from your active session data.")
    col_a, col_b, col_c = st.columns(3)

    # 1. Resume Score
    resume = st.session_state.get("resume_analysis")
    if resume and hasattr(resume, "overall_score"):
        resume_val = f"{resume.overall_score} / 100"
        resume_hint = f"{len(getattr(resume, 'skills', []))} skills · {len(getattr(resume, 'strengths', []))} strengths"
    elif st.session_state.get("resume_text"):
        resume_val = "Parsed"
        resume_hint = "Text extracted · Ready to analyze"
    else:
        resume_val = "--"
        resume_hint = "Upload a resume to score ATS fit."

    # 2. Job Match Score
    match = st.session_state.get("match_analysis")
    if match and hasattr(match, "match_score"):
        match_val = f"{match.match_score}%"
        match_hint = "Profile aligned to target role requirements."
    elif st.session_state.get("job_analysis"):
        match_val = "Parsed"
        match_hint = "Job criteria extracted · Ready to match."
    else:
        match_val = "--"
        match_hint = "Add a target role to measure match."

    # 3. Career Readiness Score
    completed = _get_completed_steps()
    completed_count = sum(completed)
    if completed_count > 0:
        readiness_pct = int((completed_count / _TOTAL_STEPS) * 100)
        readiness_val = f"{readiness_pct}%"
        readiness_hint = f"{completed_count} of {_TOTAL_STEPS} career modules active."
    else:
        readiness_val = "--"
        readiness_hint = "Complete onboarding steps to build readiness."

    with col_a:
        metric_card("Resume Score", resume_val, hint=resume_hint)
    with col_b:
        metric_card("Job Match", match_val, hint=match_hint)
    with col_c:
        metric_card("Career Readiness", readiness_val, hint=readiness_hint)


def _render_career_progress() -> None:
    section_header("Career Progress", "Tracks completion across core career intelligence pillars.")
    completed = _get_completed_steps()
    completed_count = sum(completed)
    ratio = completed_count / float(_TOTAL_STEPS)
    pct = int(ratio * 100)

    st.progress(ratio, text=f"{completed_count} of {_TOTAL_STEPS} onboarding pillars complete ({pct}%)")


def _render_onboarding_and_activity() -> None:
    left, right = st.columns([1.1, 0.9])
    completed = _get_completed_steps()

    with left:
        section_header("Getting Started", "Structured roadmap to optimize your job application pipeline.")
        for index, (label, target, _state_key) in enumerate(_ONBOARDING_STEPS, start=1):
            step_row(index, label, target, completed=completed[index - 1])

    with right:
        section_header("Recent Activity", "Live history of items configured in your current session.")
        has_any_activity = any(completed) or bool(st.session_state.get("resume_text"))

        if not has_any_activity:
            empty_state_panel(
                title="No activity yet",
                hint="Start by uploading your resume or matching a target job description on the left.",
            )
        else:
            with st.container(border=True):
                if st.session_state.get("resume_analysis"):
                    st.markdown("✅ **Resume Analyzed** · ATS report ready")
                elif st.session_state.get("resume_text"):
                    st.markdown("📄 **Resume Text Extracted** · Ready for AI analysis")

                if st.session_state.get("match_analysis"):
                    st.markdown("✅ **Job Fit Analyzed** · Match score calculated")
                elif st.session_state.get("job_analysis"):
                    st.markdown("🎯 **Job Description Parsed** · Signals extracted")

                if st.session_state.get("skill_gap_report"):
                    st.markdown("🧠 **Skill Gap Report** · Priorities quantified")

                if st.session_state.get("career_roadmap"):
                    st.markdown("🗺️ **Career Roadmap** · Milestones configured")

                if st.session_state.get("interview_session") or st.session_state.get("interview_report"):
                    st.markdown("🎤 **Mock Interview Session** · Feedback recorded")


def _render_quick_actions() -> None:
    section_header("Quick Actions", "Instant access to core AI career copilot tools.")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        nav_cta("Upload Resume", "resume_intelligence", key="cta_resume")
    with col_b:
        nav_cta("Match a Job", "jd_analysis", key="cta_jd")
    with col_c:
        nav_cta("Practice Interview", "voice_interview", key="cta_interview")
