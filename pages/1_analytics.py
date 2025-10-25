import plotly.graph_objects as go
import streamlit as st
import pandas as pd

st.title("📊 Team Comparison Analytics")
st.markdown("<p style='text-align:center;'>Select two teams to compare EPA, touchdowns, and yards over the season.</p>", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_team_season(path="this_season.csv") -> pd.DataFrame:
    # expected columns: team, week, epa, touchdowns, yards
    return pd.read_csv(path)

try:
    df = load_team_season()
    teams = sorted(df["team"].unique().tolist())

    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        team_a = st.selectbox("Team A", teams, index=0)
    with col_sel2:
        team_b = st.selectbox("Team B", teams, index=1)

    team_a_df = df[df["team"] == team_a].sort_values("week")
    team_b_df = df[df["team"] == team_b].sort_values("week")

    # ---- KPI Row ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("Team Stats")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h3 style='color:#00FFFF;text-align:center'>{team_a}</h3>", unsafe_allow_html=True)
        st.metric("Average TDs", int(team_a_df["touchdown"].mean()))
        st.metric("Average Yards", int(team_a_df["yards_gained"].mean()))
        st.metric("Avg EPA", round(team_a_df["epa"].mean(), 3))

    with col2:
        st.markdown(f"<h3 style='color:#FF00FF;text-align:center'>{team_b}</h3>", unsafe_allow_html=True)
        st.metric("Average TDs", int(team_b_df["touchdown"].mean()))
        st.metric("Average Yards", int(team_b_df["yards_gained"].mean()))
        st.metric("Avg EPA", round(team_b_df["epa"].mean(), 3))

    # ---- EPA Trend Comparison ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("EPA Trend Comparison")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["epa"],
        mode="lines+markers",
        name=team_a,
        line=dict(color="#00FFFF", width=3),
        marker=dict(size=8, color="#00FFFF")
    ))
    fig.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["epa"],
        mode="lines+markers",
        name=team_b,
        line=dict(color="#FF00FF", width=3),
        marker=dict(size=8, color="#FF00FF")
    ))
    fig.update_layout(
        title=f"{team_a} vs {team_b} — EPA by Week",
        paper_bgcolor="#0A0A0F",
        plot_bgcolor="#0A0A0F",
        font=dict(color="#FFFFFF", family="Orbitron"),
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ---- Touchdowns & Yards Comparison ----
    st.subheader("Touchdowns & Yards Trend")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["touchdown"],
        mode="lines+markers", name=f"{team_a} TDs",
        line=dict(color="#00FFFF", dash="dot")
    ))
    fig2.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["touchdown"],
        mode="lines+markers", name=f"{team_b} TDs",
        line=dict(color="#FF00FF", dash="dot")
    ))
    fig2.add_trace(go.Scatter(
        x=team_a_df["week"], y=team_a_df["yards_gained"],
        mode="lines+markers", name=f"{team_a} Yards",
        line=dict(color="#00FFFF")
    ))
    fig2.add_trace(go.Scatter(
        x=team_b_df["week"], y=team_b_df["yards_gained"],
        mode="lines+markers", name=f"{team_b} Yards",
        line=dict(color="#FF00FF")
    ))
    fig2.update_layout(
        paper_bgcolor="#0A0A0F",
        plot_bgcolor="#0A0A0F",
        font=dict(color="#FFFFFF", family="Orbitron"),
        hovermode="x unified"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ---- Raw Data Display ----
    st.markdown("<hr class='hr-neon'/>", unsafe_allow_html=True)
    st.subheader("Raw Data (Selected Teams)")
    st.dataframe(pd.concat([team_a_df, team_b_df]).reset_index(drop=True), use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")


