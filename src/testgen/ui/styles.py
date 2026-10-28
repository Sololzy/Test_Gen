import streamlit as st


def apply_custom_styles():
    st.html(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
        :root {
            --bg-soft: #f4f7ff;
            --surface: #ffffff;
            --surface-2: #f8faff;
            --line: #dbe4f0;
            --line-soft: #edf2f7;
            --text-main: #172033;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-soft: #dbeafe;
            --accent: #06b6d4;
            --note-soft: #eef4ff;
            --warn-soft: #fff7ed;
            --danger-soft: #fff1f2;
            --success: #16a34a;
            --warning: #f59e0b;
            --danger: #dc2626;
        }

        /* ── Base ── */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }
        .stApp {
            background: linear-gradient(160deg, var(--bg-soft) 0%, #f7faff 50%, #ffffff 100%);
            color: var(--text-main);
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1360px;
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: #f8fbff;
            border-right: 1px solid var(--line);
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 0.9rem;
        }

        /* ── Hero banner ── */
        .dashboard-shell {
            margin-top: 1.3rem;
            margin-bottom: 1.2rem;
        }

        .dashboard-hero {
            display: grid;
            grid-template-columns: 2.2fr 1fr;
            gap: 1rem;
            border: 1px solid rgba(148, 163, 184, 0.35);
            border-radius: 22px;
            background: linear-gradient(135deg, #ffffff 0%, #eef6ff 52%, #dfeeff 100%);
            padding: 1.2rem 1.3rem;
            box-shadow: 0 14px 28px rgba(37, 99, 235, 0.08);
        }
        .hero-copy {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .eyebrow {
            display: inline-block;
            font-size: 0.72rem;
            letter-spacing: 0.16em;
            font-weight: 700;
            color: #2563eb;
            margin-bottom: 0.5rem;
        }
        .hero-title {
            font-size: clamp(2rem, 3vw, 2.9rem);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.06em;
            color: #172033;
            margin-bottom: 0.45rem;
        }
        .hero-subtitle {
            color: var(--text-muted);
            line-height: 1.6;
            font-size: 0.98rem;
            max-width: 52rem;
        }
        .hero-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.9rem;
        }
        .hero-badge {
            display: inline-block;
            background: rgba(37, 99, 235, 0.08);
            color: var(--primary);
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-radius: 999px;
            padding: 0.38rem 0.75rem;
            font-size: 0.74rem;
            font-weight: 700;
        }
        .hero-panel {
            border: 1px solid rgba(148, 163, 184, 0.45);
            border-radius: 16px;
            background: rgba(255,255,255,0.78);
            backdrop-filter: blur(10px);
            padding: 0.9rem 1rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .panel-label {
            font-size: 0.7rem;
            font-weight: 800;
            color: #475569;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }
        .panel-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.8rem;
            font-size: 0.85rem;
            padding: 0.55rem 0;
            border-bottom: 1px solid rgba(148, 163, 184, 0.22);
        }
        .panel-row:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
        .panel-row span {
            color: var(--text-muted);
        }
        .panel-row strong {
            color: #172033;
            font-weight: 700;
        }

        .quick-card {
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.8);
            padding: 1rem 0.9rem;
            min-height: 150px;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.03);
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }
        .quick-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 26px rgba(37, 99, 235, 0.08);
        }
        .quick-icon {
            font-size: 1.5rem;
            margin-bottom: 0.55rem;
        }
        .quick-title {
            font-size: 1rem;
            font-weight: 800;
            color: #172033;
            margin-bottom: 0.35rem;
        }
        .quick-desc {
            font-size: 0.78rem;
            line-height: 1.5;
            color: var(--text-muted);
        }
        .metric-box {
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.82);
            padding: 0.8rem 0.9rem;
            margin-top: 0.75rem;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.02);
        }
        .metric-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 0.35rem;
        }
        .metric-value {
            font-size: 1rem;
            font-weight: 800;
            color: #172033;
        }

        /* ── Section note ── */
        .section-note {
            border: 1px solid #d6e4ff;
            border-radius: 10px;
            background: var(--note-soft);
            padding: 0.65rem 0.85rem;
            font-size: 0.89rem;
            color: #2d4a8a;
            margin-bottom: 0.8rem;
        }

        /* ── Flow cards ── */
        .flow-card {
            border: 1px solid var(--line);
            border-radius: 14px;
            background: var(--surface);
            padding: 0.95rem 1.05rem 0.9rem;
            margin-bottom: 0.9rem;
            box-shadow: 0 2px 12px rgba(37, 99, 235, 0.05);
            transition: box-shadow 0.2s ease;
        }
        .flow-card:hover {
            box-shadow: 0 6px 22px rgba(37, 99, 235, 0.12);
        }
        .flow-title {
            font-size: 1rem;
            font-weight: 700;
            color: #1e3a8a;
            margin-bottom: 0.2rem;
        }
        .flow-desc {
            color: var(--text-muted);
            font-size: 0.88rem;
            line-height: 1.5;
            margin-bottom: 0.75rem;
        }

        /* ── Action bar ── */
        .action-bar {
            border: 1px solid var(--line);
            border-radius: 12px;
            background: var(--surface-2);
            padding: 0.7rem 0.85rem;
            margin-top: 0.3rem;
            margin-bottom: 0.8rem;
        }
        .action-title {
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 0.2rem;
        }
        .action-desc {
            color: var(--text-muted);
            font-size: 0.83rem;
            line-height: 1.45;
        }

        /* ── Inputs ── */
        div[data-testid="stTextArea"] textarea {
            min-height: 240px;
            line-height: 1.55;
            border-radius: 10px;
            border-color: var(--line) !important;
            font-size: 0.92rem;
        }
        div[data-testid="stFileUploaderDropzone"] {
            border-radius: 12px;
        }

        /* ── Metric ── */
        [data-testid="stMetricValue"] {
            font-size: 1.08rem;
            font-weight: 700;
            color: var(--text-main);
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.77rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* ── Status boxes (sidebar) ── */
        .status-box {
            border: 1px solid var(--line-soft);
            border-radius: 10px;
            padding: 0.55rem 0.72rem;
            background: var(--surface);
            margin-bottom: 0.48rem;
        }
        .status-label {
            color: var(--text-muted);
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            margin-bottom: 0.1rem;
        }
        .status-value {
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.35;
            overflow-wrap: anywhere;
            word-break: break-word;
        }

        /* ── Verdict badge ── */
        .verdict-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            border-radius: 10px;
            padding: 0.45rem 0.9rem;
            font-size: 0.92rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .verdict-pass   { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
        .verdict-warn   { background: #fef9c3; color: #a16207; border: 1px solid #fde047; }
        .verdict-danger { background: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5; }

        /* ── Score pillar bar ── */
        .pillar-bar-wrap { margin-bottom: 0.25rem; }
        .pillar-bar-label {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 0.18rem;
            display: flex;
            justify-content: space-between;
        }
        .pillar-bar-track {
            height: 7px;
            border-radius: 999px;
            background: var(--line-soft);
            overflow: hidden;
        }
        .pillar-bar-fill {
            height: 100%;
            border-radius: 999px;
            transition: width 0.4s ease;
        }
        .pillar-green  { background: #22c55e; }
        .pillar-yellow { background: #f59e0b; }
        .pillar-red    { background: #ef4444; }

        /* ── Role cards ── */
        .role-card {
            border-radius: 12px;
            padding: 0.75rem 0.9rem;
            margin-bottom: 0.7rem;
            border: 1px solid var(--line);
        }
        .role-card-source {
            background: var(--primary-soft);
            border-color: rgba(37, 99, 235, 0.25);
        }
        .role-card-test {
            background: var(--warn-soft);
            border-color: rgba(196, 122, 34, 0.22);
        }
        .role-card-title {
            font-size: 0.88rem;
            font-weight: 800;
            margin-bottom: 0.15rem;
            color: var(--text-main);
        }
        .role-card-body {
            font-size: 0.83rem;
            line-height: 1.5;
            color: var(--text-muted);
        }

        /* ── Compact note ── */
        .compact-note {
            color: var(--text-muted);
            font-size: 0.88rem;
            line-height: 1.5;
        }

        /* ── Dataframe ── */
        div[data-testid="stDataFrame"] {
            border-radius: 10px;
            overflow: hidden;
        }

        /* ── Tabs ── */
        button[data-baseweb="tab"] {
            font-weight: 600;
            font-size: 0.88rem;
        }


        /* ── AI-tech blue interaction polish ── */
        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button {
            border-radius: 10px;
            border: 1px solid var(--primary);
            background: var(--primary);
            color: #ffffff;
            font-weight: 700;
            transition: all 0.2s ease;
        }

        div.stButton > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {
            border-color: var(--primary-hover);
            background: var(--primary-hover);
            color: #ffffff;
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.18);
            transform: translateY(-1px);
        }

        div[data-testid="stTextArea"] textarea:focus,
        div[data-testid="stTextInput"] input:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.10) !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: var(--primary) !important;
        }

        [data-baseweb="tab-highlight"] {
            background-color: var(--primary) !important;
        }

        a {
            color: var(--primary);
        }

        a:hover {
            color: var(--primary-hover);
        }


        /* ── Sidebar AI-tech enhanced ── */
        section[data-testid="stSidebar"] {
            background:
                radial-gradient(circle at 15% 0%, rgba(6, 182, 212, 0.08), transparent 26%),
                linear-gradient(180deg, #f8fbff 0%, #f4f7ff 58%, #eef4ff 100%);
            border-right: 1px solid #dbe4f0;
        }

        section[data-testid="stSidebar"] .block-container {
            padding: 1.15rem 1rem 1.5rem;
        }

        .sidebar-header {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            margin: 0.15rem 0 1rem;
            padding: 0.72rem 0.78rem;
            border: 1px solid #dbeafe;
            border-radius: 14px;
            background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(239,246,255,0.92));
            box-shadow: 0 5px 18px rgba(37, 99, 235, 0.06);
        }

        .sidebar-header-icon {
            width: 36px;
            height: 36px;
            flex: 0 0 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 11px;
            color: #ffffff;
            background: linear-gradient(135deg, #2563eb 0%, #06b6d4 100%);
            box-shadow: 0 5px 14px rgba(37, 99, 235, 0.20);
            font-size: 1rem;
        }

        .sidebar-header-title {
            color: #172033;
            font-size: 1rem;
            font-weight: 800;
            letter-spacing: -0.2px;
            line-height: 1.2;
        }

        .sidebar-header-subtitle {
            margin-top: 0.16rem;
            color: #64748b;
            font-size: 0.72rem;
            line-height: 1.3;
        }

        .sidebar-section-label {
            margin: 0.95rem 0 0.42rem;
            color: #334155;
            font-size: 0.80rem;
            font-weight: 800;
            letter-spacing: 0.15px;
        }

        section[data-testid="stSidebar"] label {
            color: #334155;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] {
            gap: 0.15rem;
            padding: 0.15rem 0 0.35rem;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            padding: 0.18rem 0.28rem;
            border-radius: 8px;
            transition: background 0.18s ease;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: rgba(37, 99, 235, 0.055);
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            min-height: 46px;
            border: 1px solid #dbe4f0;
            border-radius: 12px;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.045);
            transition: border-color 0.18s ease, box-shadow 0.18s ease;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
            border-color: #93c5fd;
            box-shadow: 0 5px 14px rgba(37, 99, 235, 0.08);
        }

        .sidebar-info-card {
            margin: 0.55rem 0 0.65rem;
            padding: 0.7rem 0.78rem;
            border: 1px solid #dbeafe;
            border-radius: 12px;
            background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
            box-shadow: 0 3px 12px rgba(37, 99, 235, 0.045);
        }

        .sidebar-info-title {
            color: #1e3a8a;
            font-size: 0.80rem;
            font-weight: 800;
            margin-bottom: 0.14rem;
        }

        .sidebar-info-text {
            color: #64748b;
            font-size: 0.75rem;
            line-height: 1.42;
        }

        .sidebar-divider {
            height: 1px;
            margin: 0.82rem 0;
            background: linear-gradient(90deg, transparent, #cbdcf5 15%, #cbdcf5 85%, transparent);
        }

        section[data-testid="stSidebar"] details {
            border: 1px solid #dbe4f0;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.78);
            overflow: hidden;
            transition: border-color 0.18s ease, box-shadow 0.18s ease;
        }

        section[data-testid="stSidebar"] details:hover {
            border-color: #93c5fd;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.06);
        }

        section[data-testid="stSidebar"] details summary {
            color: #334155;
            font-weight: 700;
        }

        /* ── Expander ── */
        details summary {
            font-weight: 600;
            font-size: 0.9rem;
        }
        </style>
        """
    )


def verdict_badge_html(verdict: str) -> str:
    """Render một badge HTML cho verdict."""
    cls_map = {
        "Đạt": "verdict-pass",
        "Hoàn hảo": "verdict-pass",
        "Cần sửa": "verdict-warn",
        "Cần cải thiện": "verdict-warn",
        "Rủi ro cao": "verdict-danger",
        "Cần xem log": "verdict-warn",
    }
    icon_map = {
        "Đạt": "✅",
        "Hoàn hảo": "✅",
        "Cần sửa": "⚠️",
        "Cần cải thiện": "⚠️",
        "Rủi ro cao": "❌",
        "Cần xem log": "⚠️",
    }
    css_cls = cls_map.get(verdict, "verdict-warn")
    icon = icon_map.get(verdict, "❓")
    from html import escape
    return f'<span class="verdict-badge {css_cls}">{icon} {escape(verdict)}</span>'


def pillar_bar_html(label: str, score: int, max_score: int) -> str:
    """Render 1 thanh mini-progress cho 1 Pillar."""
    pct = int(score / max_score * 100) if max_score else 0
    if pct >= 75:
        color_cls = "pillar-green"
    elif pct >= 40:
        color_cls = "pillar-yellow"
    else:
        color_cls = "pillar-red"
    from html import escape
    return (
        '<div class="pillar-bar-wrap">'
        f'<div class="pillar-bar-label"><span>{escape(label)}</span><span>{score}/{max_score}</span></div>'
        '<div class="pillar-bar-track">'
        f'<div class="pillar-bar-fill {color_cls}" style="width:{pct}%"></div>'
        '</div></div>'
    )
