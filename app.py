# app.py
import streamlit as st
import numpy as np
import pandas as pd
import datetime

# Page config optimized for widescreen desktop monitors
st.set_page_config(
    page_title="Multimedia Control Center",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark industrial IDE-style theme overrides
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    div.stAlert { background-color: #161b22; border: 1px solid #30363d; color: #58a6ff; }
    .chat-container {
        background-color: #161b22; padding: 15px; border-radius: 8px;
        border: 1px solid #30363d; height: 250px; overflow-y: auto; margin-bottom: 10px;
    }
    .chat-bubble { margin-bottom: 8px; padding: 8px 12px; border-radius: 6px; background-color: #21262d; }
    .chat-user { color: #58a6ff; font-weight: bold; }
    .chat-timestamp { color: #8b949e; font-size: 0.75rem; float: right; }
    </style>
""", unsafe_allow_html=True)

# Session state initialization
if "workspace_logs" not in st.session_state:
    st.session_state.workspace_logs = [
        {"user": "system", "text": "Core systems deployed on cloud node successfully.", "time": "10:00 AM"},
        {"user": "system", "text": "Secure socket interface initialized.", "time": "10:01 AM"}
    ]

if "current_stream" not in st.session_state:
    st.session_state.current_stream = "production-logs"

st.title("🖥️ Real-Time Multimedia Workspace Control Center")
st.caption("Production Ready • High Fidelity Real-Time Architecture Engine")

# Sidebar channels navigation panel
with st.sidebar:
    st.image("https://unsplash.com", use_container_width=True)
    st.markdown("### 💬 ACTIVE WORKSPACES")
    
    for stream in ["production-logs", "backend-api-stream", "client-feed-debug"]:
        if st.button(f"#️⃣ {stream}", use_container_width=True, type="primary" if st.session_state.current_stream == stream else "secondary"):
            st.session_state.current_stream = stream
            st.rerun()
        
    st.markdown("---")
    st.metric(label="Server Latency Status", value="12 ms", delta="-2 ms")
    st.success("🟢 Connected to System Host")

# Main dynamic responsive grid layout
col_canvas, col_telemetry = st.columns([2, 1.5], gap="large")

with col_canvas:
    st.subheader(f"📺 Channel Stream Vector: #{st.session_state.current_stream}")
    st.markdown("**@edognba_** • *Live Stream Ingesting*")
    st.image("https://unsplash.com", use_container_width=True)
    
    st.markdown("#### 💬 Communications Log")
    chat_html = '<div class="chat-container">'
    for log in st.session_state.workspace_logs:
        chat_html += f'<div class="chat-bubble"><span class="chat-timestamp">{log["time"]}</span><span class="chat-user">@{log["user"]}:</span> <span>{log["text"]}</span></div>'
    chat_html += '</div>'
    st.markdown(chat_html, unsafe_allow_html=True)
    
    with st.form("message_broker_form", clear_on_submit=True):
        input_col, btn_col = st.columns([4, 1])
        with input_col:
            msg_packet = st.text_input("Send message...", placeholder="Send packet updates down the pipeline...", label_visibility="collapsed")
        with btn_col:
            if st.form_submit_with_button("Send ✈️", use_container_width=True) and msg_packet.strip():
                st.session_state.workspace_logs.append({
                    "user": "edognba_", "text": msg_packet, "time": datetime.datetime.now().strftime("%I:%M %p")
                })
                st.rerun()

with col_telemetry:
    st.subheader("🎵 Audio Spectrum Diagnostics")
    frequency_bands = [f"Band {i+1}" for i in range(24)]
    dataframe_matrix = pd.DataFrame({"Frequency Amplitude (%)": np.random.randint(10, 95, size=24)}, index=frequency_bands)
    st.bar_chart(dataframe_matrix, color="#58a6ff", height=320)
    
    st.markdown("#### ⚙️ Host Infrastructure Specifications")
    metrics_l, metrics_r = st.columns(2)
    metrics_l.metric(label="GPU Compute Node Load", value="44.2 %", delta="1.4 %")
    metrics_r.metric(label="Audio Buffer Ingestion Rate", value="48.0 kHz", delta="Stable")
    
    if st.button("Force Re-sync Matrix Loops 🔄", use_container_width=True):
        st.rerun()
