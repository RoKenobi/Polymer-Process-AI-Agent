import streamlit as st
import pandas as pd
import plotly.express as px
from agent_core import ProcessAgent

st.set_page_config(page_title="Ultem Plant AI Agent", layout="wide")

@st.cache_resource
def load_agent():
    agent = ProcessAgent()
    agent.load_model()
    return agent

@st.cache_data
def load_data():
    return pd.read_csv('plant_data.csv')

agent = load_agent()
df = load_data()

# Train model if not exists
if not agent.is_trained:
    agent.train(df)

# Run Detection
df = agent.detect_anomalies(df)

# --- UI Layout ---
st.title("🏭 Ultem Polymer Plant AI Assistant")
st.markdown("Real-time anomaly detection and operational insights.")

# KPI Metrics
col1, col2, col3 = st.columns(3)
anomaly_count = df['Anomaly_Predicted'].sum()
avg_temp = df['Temp_C'].mean()
avg_visc = df['Viscosity'].mean()

col1.metric("Anomalies Detected", anomaly_count)
col2.metric("Avg Temp (°C)", f"{avg_temp:.2f}")
col3.metric("Avg Viscosity", f"{avg_visc:.2f}")

# Charts
st.subheader("Process Trends")
fig = px.line(df, x='Timestamp', y='Temp_C', title="Extruder Temperature History", color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig, use_container_width=True)

# AI Insights Table
st.subheader("🤖 AI Agent Insights")
anomalies_df = df[df['Anomaly_Predicted'] == 1].copy()
if not anomalies_df.empty:
    anomalies_df['Insight'] = anomalies_df.apply(agent.generate_insight, axis=1)
    st.dataframe(anomalies_df[['Timestamp', 'Temp_C', 'Pressure_Bar', 'Insight']], use_container_width=True)
else:
    st.success("No recent anomalies. Process is stable.")

# Sidebar for Documentation
st.sidebar.header("Documentation")
st.sidebar.info("This agent uses Isolation Forest for unsupervised anomaly detection. Logic documented in `Control_Philosophy.pdf`.")