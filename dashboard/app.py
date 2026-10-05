from pathlib import Path
from textwrap import dedent

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def render_html(body, **kwargs):
    """Render Streamlit markdown after removing Python indentation.

    Streamlit treats four leading spaces as a Markdown code block.
    Most of the dashboard HTML is inside indented Python triple-quoted
    strings, so dedenting before rendering prevents raw HTML from appearing
    as dark code boxes.
    """
    st.markdown(dedent(body).strip(), **kwargs)


st.set_page_config(
    page_title="H&M Pricing Intelligence",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Theme
# -----------------------------
CSS = """
<style>
:root {
    --bg:#FBF7F5; --surface:#FFFDFC; --soft:#F5ECEC;
    --rose:#C98291; --rose-dark:#9D5E6D; --mauve:#A58D9B;
    --plum:#5D4652; --text:#302A2D; --muted:#776E73;
    --line:#E9DDDF; --sage:#91A08F; --gold:#B99A62;
}
html, body, [class*="css"] { font-family:"Times New Roman", Times, serif !important; }
.stApp { background:var(--bg); color:var(--text); }
[data-testid="stHeader"] { background:rgba(251,247,245,.92); }
[data-testid="stSidebar"] { background:#F5ECEC; border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { font-family:"Times New Roman", Times, serif !important; }
[data-testid="stSidebar"] .block-container { padding-top:2rem; }

/* IMPORTANT: force sidebar radio text to the dark plum colour.
   Streamlit's radio component can otherwise inherit a white text colour. */
[data-testid="stSidebar"] div[role="radiogroup"] label,
[data-testid="stSidebar"] div[role="radiogroup"] label *,
[data-testid="stSidebar"] div[role="radiogroup"] label p,
[data-testid="stSidebar"] div[role="radiogroup"] label span,
[data-testid="stSidebar"] div[role="radiogroup"] [data-testid="stMarkdownContainer"],
[data-testid="stSidebar"] div[role="radiogroup"] [data-testid="stMarkdownContainer"] p {
    color:var(--plum) !important;
    opacity:1 !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size:1rem !important;
    font-weight:600 !important;
}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover,
[data-testid="stSidebar"] div[role="radiogroup"] label:hover * {
    color:var(--rose-dark) !important;
}

.brand { padding:.3rem 0 1.2rem; border-bottom:1px solid var(--line); margin-bottom:1.25rem; }
.brand-mark { color:var(--rose-dark); font-size:.78rem; letter-spacing:.18em; text-transform:uppercase; margin-bottom:.25rem; }
.brand-title { color:var(--plum); font-size:1.55rem; line-height:1.1; }
.brand-subtitle { color:var(--muted); font-size:.88rem; margin-top:.4rem; line-height:1.35; }
.nav-caption { color:var(--rose-dark); font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; margin:.6rem 0 .5rem; }

.hero { background:linear-gradient(135deg,#FFFDFC 0%,#F7EDEF 100%); border:1px solid var(--line); border-radius:24px; padding:2.2rem 2.4rem 2rem; margin-bottom:1.4rem; box-shadow:0 12px 35px rgba(100,70,80,.07); position:relative; overflow:hidden; }
.hero:after { content:"✦"; position:absolute; right:2.2rem; top:1.1rem; color:#D9AAB5; font-size:2.2rem; opacity:.75; }
.hero-eyebrow { color:var(--rose-dark); font-size:.76rem; text-transform:uppercase; letter-spacing:.16em; margin-bottom:.55rem; }
.hero-title { color:var(--plum); font-size:clamp(2.2rem,4vw,3.7rem); line-height:1.03; margin:0; }
.hero-subtitle { color:var(--muted); font-size:1.03rem; line-height:1.55; max-width:780px; margin-top:.8rem; }
.hero-note { color:var(--gold); font-size:.86rem; margin-top:1rem; }

.section-kicker { color:var(--rose-dark); font-size:.73rem; letter-spacing:.14em; text-transform:uppercase; margin-top:1.25rem; margin-bottom:.2rem; }
.section-title { color:var(--plum); font-size:1.75rem; margin:0; line-height:1.2; }
.section-description { color:var(--muted); font-size:.94rem; line-height:1.45; margin-top:.3rem; margin-bottom:.9rem; }
.card,.scenario-card { background:var(--surface); border:1px solid var(--line); border-radius:18px; padding:1.1rem 1.2rem; box-shadow:0 8px 24px rgba(100,70,80,.045); }
.kpi-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.85rem; margin-bottom:1.2rem; }
.kpi { background:var(--surface); border:1px solid var(--line); border-radius:17px; padding:1rem 1.1rem; min-height:110px; box-shadow:0 7px 22px rgba(100,70,80,.04); }
.kpi-label { color:var(--muted); font-size:.79rem; letter-spacing:.03em; }
.kpi-value { color:var(--plum); font-size:1.9rem; margin-top:.3rem; }
.kpi-detail { color:var(--rose-dark); font-size:.77rem; margin-top:.1rem; }
.insight { background:#F8EFF0; border-left:4px solid var(--rose); border-radius:12px; padding:.85rem 1rem; color:var(--text); line-height:1.5; margin:.8rem 0 1.1rem; }
.scenario-card { background:linear-gradient(145deg,#FFFDFC 0%,#F8EFF0 100%); border-radius:22px; }
.scenario-label { color:var(--rose-dark); font-size:.75rem; letter-spacing:.12em; text-transform:uppercase; }
.scenario-big { color:var(--plum); font-size:2rem; line-height:1.1; margin-top:.25rem; }
.small-muted { color:var(--muted); font-size:.84rem; line-height:1.5; }
.callout-title { color:var(--plum); font-weight:700; margin-bottom:.25rem; }
.footer { border-top:1px solid var(--line); margin-top:2.5rem; padding:1.2rem 0 .5rem; color:var(--muted); font-size:.78rem; text-align:center; }

.stSelectbox label,.stSlider label,.stRadio label,.stCheckbox label { color:var(--plum) !important; font-weight:600 !important; }
.stSelectbox div[data-baseweb="select"] > div { background:#FFFDFC; border-color:var(--line); border-radius:11px; }
.stDownloadButton button { background:#FFFDFC; color:var(--plum); border:1px solid var(--line); border-radius:10px; }
.stButton button { border-radius:10px; }

@media(max-width:900px){ .kpi-grid{grid-template-columns:repeat(2,1fr);} .hero{padding:1.5rem;} }
@media(max-width:600px){ .kpi-grid{grid-template-columns:1fr;} }
</style>
"""
render_html(CSS, unsafe_allow_html=True)

# -----------------------------
# Data
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dashboard_data"

@st.cache_data
def load_data():
    names = {
        "age":"age_diagnosis.csv",
        "category":"category_decisions.csv",
        "ladder":"ladder.csv",
        "monthly":"monthly_discount_share.csv",
        "robustness":"robustness.csv",
    }
    out, missing = {}, []
    for key, filename in names.items():
        path = DATA_DIR / filename
        if not path.exists():
            missing.append(str(path))
        else:
            out[key] = pd.read_csv(path)
    if missing:
        raise FileNotFoundError("Missing dashboard data files:\n" + "\n".join(missing))
    return out

try:
    data = load_data()
except Exception as exc:
    st.error("The dashboard could not load its CSV files.")
    st.code(str(exc))
    st.stop()

age = data["age"].copy()
category = data["category"].copy()
ladder = data["ladder"].copy()
monthly = data["monthly"].copy()
robustness = data["robustness"].copy()

for df in [age, category, ladder, monthly, robustness]:
    for col in df.columns:
        if col not in {"category","age_bucket","model","month"}:
            df[col] = pd.to_numeric(df[col], errors="coerce")

monthly["month"] = monthly["month"].astype(str)
monthly["month_date"] = pd.to_datetime(monthly["month"], errors="coerce")
monthly = monthly.sort_values("month_date")

TOTAL_REVENUE = category["revenue"].sum()
CATEGORY_COUNT = category["category"].nunique()
WEIGHTED_DISCOUNT_SHARE = monthly["disc_units"].sum() / monthly["units"].sum() if monthly["units"].sum() else np.nan
MEDIAN_ELASTICITY = category["elasticity"].median()

# -----------------------------
# Helpers
# -----------------------------
PLOT_FONT = "Times New Roman"
TEXT, MUTED, PLUM = "#302A2D", "#776E73", "#5D4652"
ROSE, MAUVE, BLUSH, SAGE, GOLD, GRID = "#C98291", "#A58D9B", "#E8C7CF", "#91A08F", "#B99A62", "#EEE3E5"

def base_layout(fig, height=420):
    fig.update_layout(
        height=height, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=PLOT_FONT,color=TEXT,size=13), margin=dict(l=20,r=20,t=55,b=35),
        hoverlabel=dict(font=dict(family=PLOT_FONT,size=13)),
        legend=dict(bgcolor="rgba(255,253,252,.75)",bordercolor=GRID,borderwidth=1,font=dict(family=PLOT_FONT)),
    )
    fig.update_xaxes(showline=False,gridcolor=GRID,zeroline=False,title_font=dict(family=PLOT_FONT,color=TEXT),tickfont=dict(family=PLOT_FONT,color=MUTED))
    fig.update_yaxes(showline=False,gridcolor=GRID,zeroline=False,title_font=dict(family=PLOT_FONT,color=TEXT),tickfont=dict(family=PLOT_FONT,color=MUTED))
    return fig

def section(kicker,title,description=None):
    desc = f'<div class="section-description">{description}</div>' if description else ""
    render_html(f'<div class="section-kicker">{kicker}</div><div class="section-title">{title}</div>{desc}',unsafe_allow_html=True)

def euro(value):
    return "—" if pd.isna(value) else f"€{value:,.0f}"

def pct(value, decimals=1):
    return "—" if pd.isna(value) else f"{value*100:.{decimals}f}%"

def signed_pct(value, decimals=1):
    return "—" if pd.isna(value) else f"{value:+.{decimals}f}%"

def show_chart(fig):
    st.plotly_chart(fig,use_container_width=True,config={"displayModeBar":False})

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    render_html(
        '<div class="brand"><div class="brand-mark">Pricing Analytics · Fashion</div>'
        '<div class="brand-title">H&M Pricing<br>Intelligence</div>'
        '<div class="brand-subtitle">An interactive exploration of demand, discounts, elasticity and pricing scenarios.</div></div>'
        '<div class="nav-caption">Explore the analysis</div>',
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Navigation",
        ["Overview","Discount Behaviour","Elasticity Analysis","Category Decisions","Pricing Scenario","Model Diagnostics"],
        label_visibility="collapsed",
    )
    render_html("<br>",unsafe_allow_html=True)
    render_html(
        '<div class="small-muted"><b>Project focus</b><br>How pricing and discounting relate to demand in H&M transaction data.'
        '<br><br><b>Note</b><br>Scenario outputs are analytical estimates, not guaranteed future results.</div>',
        unsafe_allow_html=True,
    )

# -----------------------------
# Header + KPIs
# -----------------------------
render_html(
    '<div class="hero"><div class="hero-eyebrow">Pricing Analytics · Fashion · Data</div>'
    '<div class="hero-title">H&M Pricing Intelligence</div>'
    '<div class="hero-subtitle">Exploring how price, discounts, product age and category characteristics shape demand — and turning statistical analysis into a practical pricing story.</div>'
    '<div class="hero-note">✦ Interactive dashboard · category-level insights · scenario analysis</div></div>',
    unsafe_allow_html=True,
)

render_html(
    f'<div class="kpi-grid">'
    f'<div class="kpi"><div class="kpi-label">Total category revenue</div><div class="kpi-value">{euro(TOTAL_REVENUE)}</div><div class="kpi-detail">Across {CATEGORY_COUNT} analysed categories</div></div>'
    f'<div class="kpi"><div class="kpi-label">Categories analysed</div><div class="kpi-value">{CATEGORY_COUNT}</div><div class="kpi-detail">Category-level pricing view</div></div>'
    f'<div class="kpi"><div class="kpi-label">Units sold on discount</div><div class="kpi-value">{pct(WEIGHTED_DISCOUNT_SHARE)}</div><div class="kpi-detail">Weighted across the monthly data</div></div>'
    f'<div class="kpi"><div class="kpi-label">Median category elasticity</div><div class="kpi-value">{MEDIAN_ELASTICITY:.3f}</div><div class="kpi-detail">Estimated from category results</div></div>'
    f'</div>',unsafe_allow_html=True)

# -----------------------------
# Overview
# -----------------------------
if page == "Overview":
    section("01 · Overview","The pricing story at a glance","A high-level view of revenue contribution, discount exposure and the structure of the analysis.")
    c1,c2 = st.columns([1.25,.75],gap="large")
    with c1:
        d=category.sort_values("revenue",ascending=True)
        fig=go.Figure(go.Bar(x=d["revenue"],y=d["category"],orientation="h",marker=dict(color=ROSE,line=dict(color="#B66F7F",width=.5)),hovertemplate="%{y}<br>Revenue: €%{x:,.0f}<extra></extra>"))
        fig.update_layout(title="Revenue by category"); fig.update_xaxes(title="Revenue"); fig.update_yaxes(title=""); base_layout(fig,450); show_chart(fig)
    with c2:
        render_html('<div class="card"><div class="callout-title">What this dashboard connects</div><div class="small-muted">'
                    '<b>Discount behaviour</b><br>Tracks how frequently units are sold on discount over time.<br><br>'
                    '<b>Elasticity</b><br>Examines how estimated demand responds to price changes.<br><br>'
                    '<b>Category decisions</b><br>Brings elasticity, markdown depth and revenue together at category level.<br><br>'
                    '<b>Pricing scenario</b><br>Lets you test a proposed markdown using the measured category elasticity.<br><br>'
                    '<b>Diagnostics</b><br>Shows how estimates change across model specifications and samples.</div></div>',unsafe_allow_html=True)
        top=category.nlargest(5,"revenue")[["category","revenue","elasticity"]].copy(); top["revenue"]=top["revenue"].map(euro); top["elasticity"]=top["elasticity"].map(lambda x:f"{x:.3f}")
        render_html("**Largest category revenue contributions**")
        st.dataframe(top.rename(columns={"category":"Category","revenue":"Revenue","elasticity":"Elasticity"}),use_container_width=True,hide_index=True)
    render_html('<div class="insight"><b>Reading the numbers:</b> category revenue and pricing responsiveness are different dimensions. A large revenue category is not automatically the category with the largest estimated response to price. The dashboard therefore keeps commercial scale, markdown exposure and elasticity visible together.</div>',unsafe_allow_html=True)

# -----------------------------
# Discount Behaviour
# -----------------------------
elif page == "Discount Behaviour":
    section("02 · Discount Behaviour","How discount exposure changes over time","The monthly series shows the share of units sold on discount, while the age view helps connect markdowns with product lifecycle.")
    c1,c2=st.columns(2,gap="large")
    with c1:
        fig=go.Figure(go.Scatter(x=monthly["month_date"],y=monthly["share_on_discount"]*100,mode="lines+markers",line=dict(color=ROSE,width=3),marker=dict(color=ROSE,size=7),fill="tozeroy",fillcolor="rgba(201,130,145,.10)",hovertemplate="%{x|%b %Y}<br>Discounted units: %{y:.1f}%<extra></extra>"))
        fig.add_hline(y=WEIGHTED_DISCOUNT_SHARE*100,line_dash="dot",line_color=MAUVE,annotation_text=f"Weighted average: {WEIGHTED_DISCOUNT_SHARE*100:.1f}%",annotation_font=dict(family=PLOT_FONT,color=MUTED))
        fig.update_layout(title="Monthly share of units sold on discount"); fig.update_xaxes(title="Month"); fig.update_yaxes(title="Share of units (%)",ticksuffix="%"); base_layout(fig,430); show_chart(fig)
    with c2:
        fig=go.Figure(go.Bar(x=age["age_bucket"],y=age["avg_discount"]*100,marker_color=MAUVE,hovertemplate="Age %{x}<br>Average discount: %{y:.1f}%<extra></extra>"))
        fig.update_layout(title="Average discount by product age"); fig.update_xaxes(title="Product age bucket"); fig.update_yaxes(title="Average discount (%)",ticksuffix="%"); base_layout(fig,430); show_chart(fig)
    c3,c4=st.columns(2,gap="large")
    with c3:
        fig=go.Figure(go.Bar(x=age["age_bucket"],y=age["share_of_weeks_30pct_off"]*100,marker_color=BLUSH,hovertemplate="Age %{x}<br>Weeks ≥30% off: %{y:.1f}%<extra></extra>"))
        fig.update_layout(title="Frequency of deeper markdowns"); fig.update_xaxes(title="Product age bucket"); fig.update_yaxes(title="Share of weeks (%)",ticksuffix="%"); base_layout(fig,390); show_chart(fig)
    with c4:
        fig=go.Figure(go.Scatter(x=age["age_bucket"],y=age["median_units"],mode="lines+markers",line=dict(color=SAGE,width=3),marker=dict(size=8,color=SAGE),hovertemplate="Age %{x}<br>Median units: %{y:,.0f}<extra></extra>"))
        fig.update_layout(title="Median units by product age"); fig.update_xaxes(title="Product age bucket"); fig.update_yaxes(title="Median units"); base_layout(fig,390); show_chart(fig)
    render_html('<div class="insight"><b>Business interpretation:</b> the age analysis is descriptive. It shows how markdown exposure and median unit sales vary across product-age buckets; it does not by itself establish that age causes the change.</div>',unsafe_allow_html=True)

# -----------------------------
# Elasticity
# -----------------------------
elif page == "Elasticity Analysis":
    section("03 · Elasticity Analysis","Estimated price responsiveness by category","Negative elasticity estimates indicate an inverse estimated relationship between price and demand in the category model.")
    d=category.sort_values("elasticity",ascending=True).copy(); d["err_plus"]=d["ci_high"]-d["elasticity"]; d["err_minus"]=d["elasticity"]-d["ci_low"]
    fig=go.Figure(go.Bar(x=d["elasticity"],y=d["category"],orientation="h",marker_color=ROSE,error_x=dict(type="data",symmetric=False,array=d["err_plus"],arrayminus=d["err_minus"],color=PLUM,thickness=1.5,width=5),customdata=np.column_stack([d["ci_low"],d["ci_high"]]),hovertemplate="%{y}<br>Elasticity: %{x:.3f}<br>95% CI: [%{customdata[0]:.3f}, %{customdata[1]:.3f}]<extra></extra>"))
    fig.add_vline(x=0,line_color=PLUM,line_width=1); fig.update_layout(title="Category elasticity estimates with 95% confidence intervals"); fig.update_xaxes(title="Estimated elasticity"); fig.update_yaxes(title="Category"); base_layout(fig,520); show_chart(fig)
    c1,c2=st.columns(2,gap="large")
    with c1:
        strongest=category.loc[category["elasticity"].idxmin()]; weakest=category.loc[category["elasticity"].idxmax()]
        render_html(f'<div class="card"><div class="callout-title">How to read elasticity</div><div class="small-muted">An elasticity of <b>-0.20</b>, for example, means a 1% increase in price is associated with an estimated 0.20% decrease in units, under the model assumptions.<br><br>In this dataset, the most negative category estimate is <b>{strongest["category"]}</b> ({strongest["elasticity"]:.3f}), while the least negative is <b>{weakest["category"]}</b> ({weakest["elasticity"]:.3f}).</div></div>',unsafe_allow_html=True)
    with c2:
        s=category[["category","elasticity","ci_low","ci_high"]].copy(); s["elasticity"]=s["elasticity"].map(lambda x:f"{x:.3f}"); s["95% CI"]=s.apply(lambda r:f"[{r['ci_low']:.3f}, {r['ci_high']:.3f}]",axis=1); s=s[["category","elasticity","95% CI"]].rename(columns={"category":"Category","elasticity":"Elasticity"}); st.dataframe(s,use_container_width=True,hide_index=True)

# -----------------------------
# Category Decisions
# -----------------------------
elif page == "Category Decisions":
    section("04 · Category Decisions","Putting scale, markdown and responsiveness together","This view helps compare categories without reducing the analysis to a single metric.")
    fig=px.scatter(category,x="avg_markdown",y="elasticity",size="revenue",color="share_units_on_discount",text="category",hover_data={"revenue":":,.0f","avg_markdown":":.1%","share_units_on_discount":":.1%","elasticity":":.3f"},color_continuous_scale=["#EBD9DD",ROSE,PLUM])
    fig.update_traces(textposition="top center",marker=dict(line=dict(width=1,color="#FFFDFC"))); fig.update_layout(title="Category positioning: markdown depth vs. elasticity"); fig.update_xaxes(title="Average markdown",tickformat=".0%"); fig.update_yaxes(title="Elasticity"); base_layout(fig,510); show_chart(fig)
    cols=["category","revenue","elasticity","ci_low","ci_high","share_units_on_discount","avg_markdown","revenue_share_%","rev_effect_at_measured_%"]
    t=category[cols].sort_values("revenue",ascending=False).copy(); t["revenue"]=t["revenue"].map(euro); t["elasticity"]=t["elasticity"].map(lambda x:f"{x:.3f}"); t["95% CI"]=t.apply(lambda r:f"[{r['ci_low']:.3f}, {r['ci_high']:.3f}]",axis=1); t["share_units_on_discount"]=t["share_units_on_discount"].map(lambda x:f"{x:.1%}"); t["avg_markdown"]=t["avg_markdown"].map(lambda x:f"{x:.1%}"); t["revenue_share_%"]=t["revenue_share_%"].map(lambda x:f"{x:.1f}%"); t["rev_effect_at_measured_%"]=t["rev_effect_at_measured_%"].map(lambda x:f"{x:.1f}%"); t=t.drop(columns=["ci_low","ci_high"]).rename(columns={"category":"Category","revenue":"Revenue","elasticity":"Elasticity","share_units_on_discount":"Units on discount","avg_markdown":"Avg markdown","revenue_share_%":"Revenue share","rev_effect_at_measured_%":"Measured revenue effect"})
    st.dataframe(t,use_container_width=True,hide_index=True)
    st.download_button("Download category decision table",data=t.to_csv(index=False).encode("utf-8"),file_name="hm_category_decisions_dashboard.csv",mime="text/csv")

# -----------------------------
# Pricing Scenario
# -----------------------------
elif page == "Pricing Scenario":
    section("05 · Pricing Scenario","Test a proposed markdown","Use the measured category elasticity to explore how a change in markdown could translate into an estimated demand and revenue response.")
    render_html('<div class="insight"><b>Scenario model:</b> this is a constant-elasticity what-if calculation. It is designed to make the estimated relationship intuitive, not to predict an actual future sales result. It assumes the selected category elasticity remains constant and other conditions remain unchanged.</div>',unsafe_allow_html=True)
    left,right=st.columns([.9,1.1],gap="large")
    with left:
        selected=st.selectbox("Choose a category",category["category"].tolist(),index=0)
        row=category.loc[category["category"]==selected].iloc[0]; base_md=float(row["avg_markdown"]); elasticity=float(row["elasticity"]); base_rev=float(row["revenue"])
        proposed=st.slider("Proposed markdown",0,60,int(round(base_md*100)),1,format="%d%%")/100
        render_html(f'<div class="card"><div class="callout-title">Selected category: {selected}</div><div class="small-muted">Current average markdown: <b>{base_md:.1%}</b><br>Proposed markdown: <b>{proposed:.1%}</b><br>Measured elasticity: <b>{elasticity:.3f}</b><br>Current category revenue: <b>{euro(base_rev)}</b></div></div>',unsafe_allow_html=True)
    base_price=max(1-base_md,.001); new_price=max(1-proposed,.001); price_ratio=new_price/base_price; unit_ratio=price_ratio**elasticity; revenue_ratio=price_ratio*unit_ratio
    unit_change=unit_ratio-1; revenue_change=revenue_ratio-1; scenario_rev=base_rev*revenue_ratio; revenue_delta=scenario_rev-base_rev
    with right:
        render_html("**Scenario output**"); m1,m2,m3=st.columns(3)
        with m1: render_html(f'<div class="scenario-card"><div class="scenario-label">Estimated unit change</div><div class="scenario-big">{signed_pct(unit_change*100)}</div><div class="small-muted">relative to current average markdown</div></div>',unsafe_allow_html=True)
        with m2: render_html(f'<div class="scenario-card"><div class="scenario-label">Estimated revenue change</div><div class="scenario-big">{signed_pct(revenue_change*100)}</div><div class="small-muted">constant-elasticity scenario</div></div>',unsafe_allow_html=True)
        with m3: render_html(f'<div class="scenario-card"><div class="scenario-label">Scenario revenue</div><div class="scenario-big">{euro(scenario_rev)}</div><div class="small-muted">change: {euro(revenue_delta)}</div></div>',unsafe_allow_html=True)
    render_html("### Scenario sensitivity")
    sens=pd.DataFrame({"markdown":np.linspace(0,.60,61)}); sens["price_ratio"]=(1-sens["markdown"])/base_price; sens["unit_ratio"]=sens["price_ratio"]**elasticity; sens["revenue_index"]=sens["price_ratio"]*sens["unit_ratio"]
    fig=go.Figure(go.Scatter(x=sens["markdown"]*100,y=sens["revenue_index"]*100,mode="lines",line=dict(color=ROSE,width=3),fill="tozeroy",fillcolor="rgba(201,130,145,.10)",hovertemplate="Markdown: %{x:.0f}%<br>Revenue index: %{y:.1f}<extra></extra>"))
    fig.add_vline(x=base_md*100,line_dash="dot",line_color=MAUVE,annotation_text="Current avg.",annotation_font=dict(family=PLOT_FONT,color=MUTED)); fig.add_vline(x=proposed*100,line_dash="dash",line_color=PLUM,annotation_text="Scenario",annotation_font=dict(family=PLOT_FONT,color=PLUM)); fig.add_hline(y=100,line_dash="dot",line_color=GRID)
    fig.update_layout(title=f"Revenue sensitivity for {selected}"); fig.update_xaxes(title="Markdown (%)",ticksuffix="%"); fig.update_yaxes(title="Revenue index (current = 100)"); base_layout(fig,470); show_chart(fig)
    render_html(f'<div class="card"><div class="callout-title">How to interpret this scenario</div><div class="small-muted">Moving the slider changes the assumed effective price. Because the selected elasticity is <b>{elasticity:.3f}</b>, the model estimates the corresponding unit response using <b>Q₁/Q₀ = (P₁/P₀)<sup>elasticity</sup></b>. Revenue is then estimated as price × units.<br><br>This is useful for comparing hypothetical markdown levels, but it should not be treated as a causal forecast because the calculation does not model inventory, seasonality, competition, product mix, promotion timing or other operational factors.</div></div>',unsafe_allow_html=True)

# -----------------------------
# Diagnostics
# -----------------------------
elif page == "Model Diagnostics":
    section("06 · Model Diagnostics","How stable are the estimates?","The robustness and model-ladder views show how the estimated coefficient changes as the sample or specification changes.")
    c1,c2=st.columns(2,gap="large")
    with c1:
        rb=robustness.copy(); rb["err_plus"]=rb["ci_high"]-rb["elasticity"]; rb["err_minus"]=rb["elasticity"]-rb["ci_low"]
        fig=go.Figure(go.Bar(x=rb["elasticity"],y=rb["model"],orientation="h",marker_color=MAUVE,error_x=dict(type="data",symmetric=False,array=rb["err_plus"],arrayminus=rb["err_minus"],color=PLUM,thickness=1.5,width=5),hovertemplate="%{y}<br>Elasticity: %{x:.3f}<extra></extra>"))
        fig.add_vline(x=0,line_color=PLUM,line_width=1); fig.update_layout(title="Robustness checks"); fig.update_xaxes(title="Estimated elasticity"); fig.update_yaxes(title="Model / sample"); base_layout(fig,500); show_chart(fig)
    with c2:
        ld=ladder.dropna(subset=["elasticity"]).copy()
        fig=go.Figure(go.Scatter(x=ld["elasticity"],y=ld["model"],mode="lines+markers",line=dict(color=ROSE,width=3),marker=dict(color=ROSE,size=9),hovertemplate="%{y}<br>Coefficient: %{x:.3f}<extra></extra>"))
        fig.update_layout(title="Model ladder"); fig.update_xaxes(title="Estimated coefficient"); fig.update_yaxes(title="Model specification"); base_layout(fig,500); show_chart(fig)
    render_html("### Robustness table")
    rb_table=robustness.copy(); rb_table["elasticity"]=rb_table["elasticity"].map(lambda x:f"{x:.3f}"); rb_table["std_error"]=rb_table["std_error"].map(lambda x:f"{x:.3f}"); rb_table["95% CI"]=rb_table.apply(lambda r:f"[{r['ci_low']:.3f}, {r['ci_high']:.3f}]",axis=1); rb_table=rb_table[["model","rows","elasticity","std_error","95% CI"]].rename(columns={"model":"Model","rows":"Rows","elasticity":"Elasticity","std_error":"Std. error"}); st.dataframe(rb_table,use_container_width=True,hide_index=True)
    render_html('<div class="insight"><b>Why this matters:</b> a pricing estimate is more informative when its direction and magnitude are examined across reasonable modelling choices. These diagnostics do not prove that one specification is the single correct model; they show how sensitive the reported coefficient is to the chosen setup.</div>',unsafe_allow_html=True)

render_html('<div class="footer">Built as an individual pricing analytics project using H&M transaction data · Designed for exploration, interpretation and transparent scenario thinking ✦</div>',unsafe_allow_html=True)
