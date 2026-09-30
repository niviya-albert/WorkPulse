"""
WorkPulse – Unemployment Trends & Economic Insights
Editorial Macroeconomic Monitor & Analytical Terminal
Design Theme: Swiss Editorial / Financial Times Macro-Journal
Author: Niviya Albert | CodeAlpha Data Science Internship Task 2
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# -------------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------------
st.set_page_config(
    page_title="WorkPulse • National Labour & Economic Monitor",
    page_icon="🗞️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# SWISS EDITORIAL / FINANCIAL MACRO-JOURNAL CSS
# -------------------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;0,9..144,800;1,9..144,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

<style>
    /* Global Canvas */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background-color: #F8F6F0;
        color: #1A1A18;
    }
    
    /* Top Masthead */
    .masthead-container {
        border-top: 4px solid #141413;
        border-bottom: 2px solid #141413;
        padding: 1.5rem 0 1rem 0;
        margin-bottom: 1.5rem;
        background-color: transparent;
    }
    
    .masthead-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #D5CEBF;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        color: #635F56;
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }
    
    .masthead-title {
        font-family: 'Fraunces', serif;
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #141413;
        line-height: 1;
        margin: 0;
        text-align: center;
    }
    
    .masthead-tagline {
        font-family: 'Fraunces', serif;
        font-style: italic;
        font-size: 1.15rem;
        color: #555148;
        text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }
    
    /* Live Market Ticker */
    .ticker-bar {
        background: #141413;
        color: #F8F6F0;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        font-family: 'Space Mono', monospace;
        font-size: 0.78rem;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 2rem;
        letter-spacing: 0.05em;
    }
    
    .ticker-item b {
        color: #E2A03F;
    }
    
    /* Editorial Stat Card */
    .editorial-card {
        background: #FFFFFF;
        border: 1px solid #DDD6C6;
        border-radius: 0px;
        padding: 1.4rem;
        position: relative;
        box-shadow: 3px 3px 0px rgba(20, 20, 19, 0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .editorial-card:hover {
        transform: translate(-2px, -2px);
        box-shadow: 5px 5px 0px rgba(20, 20, 19, 0.15);
    }
    
    .editorial-kicker {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #8C827A;
        letter-spacing: 0.1em;
        margin-bottom: 0.4rem;
    }
    
    .editorial-num {
        font-family: 'Fraunces', serif;
        font-size: 2.3rem;
        font-weight: 800;
        color: #141413;
        line-height: 1.1;
    }
    
    .editorial-sub {
        font-size: 0.82rem;
        color: #555148;
        margin-top: 0.4rem;
        border-top: 1px dotted #D5CEBF;
        padding-top: 0.4rem;
    }
    
    /* Editorial Content Boxes */
    .dispatch-box {
        background: #FFFFFF;
        border: 1px solid #DDD6C6;
        border-left: 5px solid #1B365D;
        padding: 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 2px 2px 0px rgba(20, 20, 19, 0.05);
    }
    
    .dispatch-box h4 {
        font-family: 'Fraunces', serif;
        color: #1B365D;
        margin-top: 0;
        margin-bottom: 0.4rem;
    }
    
    .policy-brief-box {
        background: #FFFFFF;
        border: 1px solid #DDD6C6;
        border-left: 5px solid #C04E22;
        padding: 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 2px 2px 0px rgba(20, 20, 19, 0.05);
    }
    
    .policy-brief-box h4 {
        font-family: 'Fraunces', serif;
        color: #C04E22;
        margin-top: 0;
        margin-bottom: 0.4rem;
    }
    
    /* Editorial Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background-color: transparent;
        border-bottom: 2px solid #141413;
        padding: 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 0px;
        color: #555148;
        font-family: 'Space Mono', monospace;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        padding: 10px 18px;
        border: 1px solid transparent;
        border-bottom: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        color: #141413 !important;
        border: 2px solid #141413 !important;
        border-bottom: 2px solid #FFFFFF !important;
        margin-bottom: -2px;
    }
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------------
# DATA LOADING & CACHING
# -------------------------------------------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    f1 = os.path.join(base_dir, "data", "cleaned_unemployment_data.csv")
    f2 = os.path.join(base_dir, "data", "cleaned_unemployment_regional.csv")
    
    df1 = pd.read_csv(f1)
    df1["Date"] = pd.to_datetime(df1["Date"])
    
    df2 = pd.read_csv(f2)
    df2["Date"] = pd.to_datetime(df2["Date"])
    
    def get_phase(dt):
        if dt < pd.Timestamp("2020-03-01"):
            return "Pre-COVID Baseline"
        elif dt <= pd.Timestamp("2020-05-31"):
            return "Lockdown Peak Phase"
        else:
            return "Post-Lockdown Recovery"
            
    df1["COVID_Phase"] = df1["Date"].apply(get_phase)
    df2["COVID_Phase"] = df2["Date"].apply(get_phase)
    
    return df1, df2


df_primary, df_regional = load_data()

# EDITORIAL PLOTLY THEME
EDITORIAL_THEME = {
    "layout": {
        "paper_bgcolor": "#FFFFFF",
        "plot_bgcolor": "#FAF8F5",
        "font": {"color": "#141413", "family": "Plus Jakarta Sans"},
        "xaxis": {"gridcolor": "#E8E3D9", "zerolinecolor": "#141413", "linecolor": "#141413"},
        "yaxis": {"gridcolor": "#E8E3D9", "zerolinecolor": "#141413", "linecolor": "#141413"},
        "margin": {"l": 40, "r": 30, "t": 40, "b": 40}
    }
}


# -------------------------------------------------------------
# MASTHEAD / TOP NEWSPAPER BANNER
# -------------------------------------------------------------
st.markdown("""
<div class="masthead-container">
    <div class="masthead-meta">
        <span>ESTABLISHED • MAY 2019 – OCT 2020</span>
        <span>NATIONAL LABOUR INTELLIGENCE DISPATCH</span>
        <span>CODEALPHA TASK II • NIVIYA ALBERT</span>
    </div>
    <h1 class="masthead-title">WORKPULSE</h1>
    <p class="masthead-tagline">A Quantitative Empirical Review of Indian Labour Force Dynamics, Pandemic Shocks & Rebound</p>
</div>
""", unsafe_allow_html=True)

# Ticker Strip
mean_rate = df_primary["Unemployment_Rate_Pct"].mean()
pre_rate = df_primary[df_primary["COVID_Phase"] == "Pre-COVID Baseline"]["Unemployment_Rate_Pct"].mean()
peak_rate = df_primary[df_primary["COVID_Phase"] == "Lockdown Peak Phase"]["Unemployment_Rate_Pct"].mean()
recov_rate = df_primary[df_primary["COVID_Phase"] == "Post-Lockdown Recovery"]["Unemployment_Rate_Pct"].mean()

st.markdown(f"""
<div class="ticker-bar">
    <div class="ticker-item">● PRE-COVID BASELINE: <b>{pre_rate:.2f}%</b></div>
    <div class="ticker-item">▲ LOCKDOWN PEAK: <b>{peak_rate:.2f}%</b></div>
    <div class="ticker-item">▼ INITIAL RECOVERY: <b>{recov_rate:.2f}%</b></div>
    <div class="ticker-item">■ SAMPLE SIZE: <b>740 RECORDS</b></div>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------------------
# EDITORIAL KPI CARDS
# -------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="editorial-card">
        <div class="editorial-kicker">Benchmark Mean</div>
        <div class="editorial-num">{mean_rate:.2f}%</div>
        <div class="editorial-sub">National Overall Average</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="editorial-card">
        <div class="editorial-kicker">Pre-Shock Normal</div>
        <div class="editorial-num" style="color: #1B365D;">{pre_rate:.2f}%</div>
        <div class="editorial-sub">May 2019 – Feb 2020</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="editorial-card">
        <div class="editorial-kicker">Lockdown Shock</div>
        <div class="editorial-num" style="color: #C04E22;">{peak_rate:.2f}%</div>
        <div class="editorial-sub">+107% Above Baseline</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    max_rec = df_primary.loc[df_primary["Unemployment_Rate_Pct"].idxmax()]
    st.markdown(f"""
    <div class="editorial-card">
        <div class="editorial-kicker">Historic Peak</div>
        <div class="editorial-num" style="color: #8A2B0E;">{max_rec['Unemployment_Rate_Pct']:.1f}%</div>
        <div class="editorial-sub">{max_rec['State']} (May '20)</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    lp_mean = df_primary["Labour_Participation_Rate_Pct"].mean()
    st.markdown(f"""
    <div class="editorial-card">
        <div class="editorial-kicker">Labour Force Part.</div>
        <div class="editorial-num" style="color: #2D5A27;">{lp_mean:.1f}%</div>
        <div class="editorial-sub">Workforce Participation</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# -------------------------------------------------------------
# EDITORIAL TAB NAVIGATION
# -------------------------------------------------------------
tab_overview, tab_timeline, tab_geo, tab_duel, tab_covid, tab_policy, tab_data = st.tabs([
    "I. EXECUTIVE BRIEFING",
    "II. TIME SERIES TRAJECTORY",
    "III. GEOGRAPHIC RANKINGS",
    "IV. STATE DUEL MATRIX",
    "V. PANDEMIC SHOCK",
    "VI. POLICY WHITEPAPER",
    "VII. DATA ARCHIVE"
])


# =============================================================
# TAB I: EXECUTIVE BRIEFING
# =============================================================
with tab_overview:
    col_brief_l, col_brief_r = st.columns([3, 2])
    
    with col_brief_l:
        st.markdown("### 📊 Distribution of Unemployment: Rural vs. Urban Economies")
        fig_hist = px.histogram(
            df_primary,
            x="Unemployment_Rate_Pct",
            color="Area_Type",
            marginal="box",
            nbins=35,
            color_discrete_map={"Rural": "#2D5A27", "Urban": "#C04E22"},
            labels={"Unemployment_Rate_Pct": "Unemployment Rate (%)", "Area_Type": "Sector"}
        )
        fig_hist.update_layout(EDITORIAL_THEME["layout"])
        fig_hist.update_layout(
            bargap=0.08,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col_brief_r:
        st.markdown("### 📋 Macroeconomic Summary Matrix")
        summary_tbl = df_primary.groupby("Area_Type").agg({
            "Unemployment_Rate_Pct": ["mean", "median", "max"],
            "Labour_Participation_Rate_Pct": "mean",
            "Employed_Count": "mean"
        }).round(2)
        summary_tbl.columns = ["Mean Rate (%)", "Median (%)", "Peak Spike (%)", "Labour Part. (%)", "Avg Employed"]
        st.dataframe(summary_tbl, use_container_width=True)
        
        st.markdown("""
        <div class="dispatch-box">
            <h4>Dispatch Summary:</h4>
            <p style="margin: 0; font-size: 0.9rem; color: #44403C; line-height: 1.5;">
            The dataset reveals an acute right-skewed shock. While pre-crisis unemployment hovered steadily near 9.5%, the strict lockdown created sudden urban friction (+7.19% gap over rural areas in May 2020) due to physical retail and factory closures.
            </p>
        </div>
        """, unsafe_allow_html=True)


# =============================================================
# TAB II: TIME SERIES TRAJECTORY
# =============================================================
with tab_timeline:
    st.markdown("### 📈 Longitudinal Unemployment Trajectory (May 2019 – June 2020)")
    
    states_all = sorted(df_primary["State"].unique().tolist())
    def_states = ["Maharashtra", "Tamil Nadu", "Delhi", "Bihar", "Gujarat", "Haryana"]
    
    c_flt1, c_flt2 = st.columns([3, 1])
    with c_flt1:
        chosen_states = st.multiselect("Select Target States to Chart", states_all, default=[s for s in def_states if s in states_all])
    with c_flt2:
        chosen_sector = st.selectbox("Sector Breakdown", ["All (Combined)", "Rural", "Urban"])
        
    df_ts = df_primary.copy()
    if chosen_sector != "All (Combined)":
        df_ts = df_ts[df_ts["Area_Type"] == chosen_sector]
    if chosen_states:
        df_ts = df_ts[df_ts["State"].isin(chosen_states)]
        
    ts_data = df_ts.groupby(["Date", "State"])["Unemployment_Rate_Pct"].mean().reset_index()
    
    fig_ts = px.line(
        ts_data,
        x="Date",
        y="Unemployment_Rate_Pct",
        color="State",
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    fig_ts.add_vrect(
        x0="2020-03-24", x1="2020-05-31",
        fillcolor="rgba(192, 78, 34, 0.15)",
        layer="below", line_width=1, line_dash="dash", line_color="#C04E22",
        annotation_text="NATIONAL LOCKDOWN INTERVENTION",
        annotation_position="top left",
        annotation_font_color="#C04E22"
    )
    fig_ts.update_layout(EDITORIAL_THEME["layout"])
    fig_ts.update_layout(hovermode="x unified")
    st.plotly_chart(fig_ts, use_container_width=True)
    
    # Sectoral Divergence Area
    st.markdown("### 🌾 Rural vs. 🏙️ Urban Divergence Over Time")
    ru_monthly = df_primary.groupby(["Date", "Area_Type"])["Unemployment_Rate_Pct"].mean().reset_index()
    fig_ru_line = px.line(
        ru_monthly,
        x="Date",
        y="Unemployment_Rate_Pct",
        color="Area_Type",
        markers=True,
        color_discrete_map={"Rural": "#2D5A27", "Urban": "#C04E22"}
    )
    fig_ru_line.update_layout(EDITORIAL_THEME["layout"])
    st.plotly_chart(fig_ru_line, use_container_width=True)


# =============================================================
# TAB III: GEOGRAPHIC RANKINGS
# =============================================================
with tab_geo:
    st.markdown("### 🗺️ State-Wise Unemployment Rankings & Geographic Dispersion")
    
    st_ranks = df_primary.groupby("State").agg({
        "Unemployment_Rate_Pct": ["mean", "max", "min", "std"],
        "Labour_Participation_Rate_Pct": "mean"
    }).reset_index()
    st_ranks.columns = ["State", "Avg_Unemployment", "Peak_Spike", "Min_Rate", "Volatility", "Labour_Part"]
    st_ranks = st_ranks.sort_values(by="Avg_Unemployment", ascending=False)
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.markdown("##### 🔴 10 Most Vulnerable States (Highest Average Rate)")
        fig_top10 = px.bar(
            st_ranks.head(10),
            x="Avg_Unemployment",
            y="State",
            orientation="h",
            color="Avg_Unemployment",
            color_continuous_scale="Reds",
            text="Avg_Unemployment"
        )
        fig_top10.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_top10.update_layout(EDITORIAL_THEME["layout"])
        fig_top10.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_top10, use_container_width=True)
        
    with g_col2:
        st.markdown("##### 🟢 10 Most Resilient States (Lowest Average Rate)")
        fig_bot10 = px.bar(
            st_ranks.tail(10).sort_values(by="Avg_Unemployment", ascending=True),
            x="Avg_Unemployment",
            y="State",
            orientation="h",
            color="Avg_Unemployment",
            color_continuous_scale="Greens_r",
            text="Avg_Unemployment"
        )
        fig_bot10.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig_bot10.update_layout(EDITORIAL_THEME["layout"])
        fig_bot10.update_layout(yaxis={"categoryorder": "total descending"})
        st.plotly_chart(fig_bot10, use_container_width=True)
        
    # Spatial Bubble Map
    st.markdown("##### 📍 Spatial Macro-Intensity Bubble Map")
    geo_pts = df_regional.groupby("State").agg({
        "Unemployment_Rate_Pct": "mean",
        "Latitude": "first",
        "Longitude": "first",
        "Zone": "first"
    }).reset_index()
    
    fig_spatial = px.scatter_geo(
        geo_pts,
        lat="Latitude",
        lon="Longitude",
        color="Unemployment_Rate_Pct",
        size="Unemployment_Rate_Pct",
        hover_name="State",
        hover_data={"Zone": True, "Unemployment_Rate_Pct": ":.2f%"},
        color_continuous_scale="Thermal",
        scope="asia",
        center={"lat": 22.0, "lon": 79.0}
    )
    fig_spatial.update_geos(fitbounds="locations", visible=False, bgcolor="#FAF8F5")
    fig_spatial.update_layout(EDITORIAL_THEME["layout"])
    st.plotly_chart(fig_spatial, use_container_width=True)


# =============================================================
# TAB IV: STATE DUEL MATRIX
# =============================================================
with tab_duel:
    st.markdown("### ⚔️ State Duel: Comparative Bilateral Analysis")
    st.markdown("Select two states to contrast baseline stability, peak vulnerability, and recovery momentum.")
    
    cd1, cd2 = st.columns(2)
    with cd1:
        state_1 = st.selectbox("Primary State", states_all, index=states_all.index("Maharashtra") if "Maharashtra" in states_all else 0)
    with cd2:
        state_2 = st.selectbox("Comparison State", states_all, index=states_all.index("Tamil Nadu") if "Tamil Nadu" in states_all else 1)
        
    df_s1 = df_primary[df_primary["State"] == state_1]
    df_s2 = df_primary[df_primary["State"] == state_2]
    
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric(f"{state_1} Mean Rate", f"{df_s1['Unemployment_Rate_Pct'].mean():.2f}%")
    with k2:
        st.metric(f"{state_1} Peak Shock", f"{df_s1['Unemployment_Rate_Pct'].max():.2f}%")
    with k3:
        st.metric(f"{state_2} Mean Rate", f"{df_s2['Unemployment_Rate_Pct'].mean():.2f}%")
    with k4:
        st.metric(f"{state_2} Peak Shock", f"{df_s2['Unemployment_Rate_Pct'].max():.2f}%")
        
    duel_monthly = df_primary[df_primary["State"].isin([state_1, state_2])].groupby(["Date", "State"])["Unemployment_Rate_Pct"].mean().reset_index()
    fig_duel_line = px.line(
        duel_monthly,
        x="Date",
        y="Unemployment_Rate_Pct",
        color="State",
        markers=True,
        color_discrete_map={state_1: "#1B365D", state_2: "#C04E22"},
        title=f"Head-to-Head Trend: {state_1} vs {state_2}"
    )
    fig_duel_line.add_vrect(
        x0="2020-03-24", x1="2020-05-31",
        fillcolor="rgba(192, 78, 34, 0.15)",
        layer="below", line_width=1, line_dash="dash", line_color="#C04E22"
    )
    fig_duel_line.update_layout(EDITORIAL_THEME["layout"])
    st.plotly_chart(fig_duel_line, use_container_width=True)


# =============================================================
# TAB V: PANDEMIC SHOCK
# =============================================================
with tab_covid:
    st.markdown("### 🦠 COVID-19 Pandemic Shock & Structural Shift")
    
    covid_stat_df = df_primary.groupby("COVID_Phase").agg({
        "Unemployment_Rate_Pct": ["mean", "median", "max", "std"],
        "Labour_Participation_Rate_Pct": "mean",
        "Employed_Count": "mean"
    }).round(2)
    covid_stat_df.columns = ["Mean Unemp (%)", "Median (%)", "Peak Spike (%)", "Std Dev", "Labour Part. (%)", "Avg Employed"]
    st.dataframe(covid_stat_df, use_container_width=True)
    
    cp1, cp2 = st.columns(2)
    with cp1:
        st.markdown("##### 📦 Phase Variation Boxplot")
        fig_cp_box = px.box(
            df_primary,
            x="COVID_Phase",
            y="Unemployment_Rate_Pct",
            color="COVID_Phase",
            color_discrete_map={"Pre-COVID Baseline": "#1B365D", "Lockdown Peak Phase": "#C04E22", "Post-Lockdown Recovery": "#2D5A27"}
        )
        fig_cp_box.update_layout(EDITORIAL_THEME["layout"])
        fig_cp_box.update_layout(showlegend=False)
        st.plotly_chart(fig_cp_box, use_container_width=True)
        
    with cp2:
        st.markdown("##### 📉 Labour Participation vs Unemployment")
        fig_scat_p = px.scatter(
            df_primary,
            x="Labour_Participation_Rate_Pct",
            y="Unemployment_Rate_Pct",
            color="COVID_Phase",
            hover_name="State",
            color_discrete_map={"Pre-COVID Baseline": "#1B365D", "Lockdown Peak Phase": "#C04E22", "Post-Lockdown Recovery": "#2D5A27"}
        )
        fig_scat_p.update_layout(EDITORIAL_THEME["layout"])
        st.plotly_chart(fig_scat_p, use_container_width=True)


# =============================================================
# TAB VI: POLICY WHITEPAPER
# =============================================================
with tab_policy:
    st.markdown("### 💡 Policy Whitepaper & Empirical Strategic Framework")
    
    w_col1, w_col2 = st.columns(2)
    with w_col1:
        st.markdown("#### 📌 I. Observed Empirical Facts")
        st.markdown("""
        <div class="dispatch-box">
            <h4>1. Unprecedented Sudden Disruption</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            National average unemployment doubled from <b>9.51%</b> in the pre-crisis baseline to <b>24.88%</b> in May 2020.
            </p>
        </div>
        <div class="dispatch-box">
            <h4>2. Asymmetric Urban Penalty</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            Urban unemployment touched <b>28.40%</b> during peak lockdown vs. <b>21.21%</b> in rural regions (+7.19% gap) as services were physically frozen.
            </p>
        </div>
        <div class="dispatch-box">
            <h4>3. Labour Force Contraction</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            Workforce participation declined by <b>4.96 percentage points</b> as millions temporarily stopped active job searches due to travel barriers.
            </p>
        </div>
        <div class="dispatch-box">
            <h4>4. V-Shaped Initial Rebound</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            By June 2020, national unemployment plummeted back to <b>11.90%</b> as unlock guidelines allowed informal activities to resume.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with w_col2:
        st.markdown("#### 🏛️ II. Policy & Institutional Prescriptions")
        st.markdown("""
        <div class="policy-brief-box">
            <h4>1. National Urban Livelihood Guarantee</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            Deploy an urban equivalent to MGNREGA to protect informal urban wage earners against localized containment shocks.
            </p>
        </div>
        <div class="policy-brief-box">
            <h4>2. Structural State Industrial Clustering</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            High baseline unemployment states (Tripura, Haryana, Jharkhand, Bihar) require structural industrial clustering and skilling corridors.
            </p>
        </div>
        <div class="policy-brief-box">
            <h4>3. Informal Enterprise Emergency Liquidity</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            Liquidity backstops prevent temporary mobility restrictions from triggering permanent micro-enterprise bankruptcies.
            </p>
        </div>
        <div class="policy-brief-box">
            <h4>4. High-Frequency Real-Time Monitoring</h4>
            <p style="font-size: 0.88rem; color: #44403C; line-height: 1.5; margin: 0;">
            Institutionalize monthly real-time labor tracking to deploy swift targeted fiscal relief instead of delayed quarterly reports.
            </p>
        </div>
        """, unsafe_allow_html=True)


# =============================================================
# TAB VII: DATA ARCHIVE
# =============================================================
with tab_data:
    st.markdown("### 📁 Primary Data Archive & Export")
    st.dataframe(df_primary, use_container_width=True)
    
    csv_bytes = df_primary.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cleaned Dataset (.CSV)",
        data=csv_bytes,
        file_name="cleaned_unemployment_data.csv",
        mime="text/csv"
    )

st.markdown("<br><hr style='border-color: #D5CEBF;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: \"Space Mono\", monospace; font-size: 0.75rem; color: #8C827A;'>WORKPULSE DISPATCH • CODEALPHA DATA SCIENCE INTERNSHIP TASK 2 • RESEARCH ARCHIVE</p>", unsafe_allow_html=True)
