import streamlit as st
import time

st.set_page_config(page_title="Rapid Sentinel - Decider 2B Demo", layout="centered")

st.title("⚡ CloudOps Rapid Sentinel")
st.caption("Strands Decider 2B & Amazon Bedrock Agent Demo")

# User Input Simulation
incident_options = [
    "Database connection pool exhausted on port 5432",
    "API Gateway 504 Gateway Timeout spike on /checkout",
    "Pod OOMKilled in kubernetes cluster prod-us-east",
    "Unknown TLS certificate expiration alert"
]

selected_log = st.selectbox("Select or inspect an Incident Log:", incident_options)

if st.button("Trigger Autonomous Triage"):
    start_time = time.time()
    
    # Tool Selection Logic via Decider 2B simulation
    tool_mapping = {
        incident_options[0]: ("scale_db_pool", 0.94),
        incident_options[1]: ("restart_gateway_pods", 0.89),
        incident_options[2]: ("increase_pod_memory_limit", 0.96),
        incident_options[3]: ("escalate_human_operator", 0.65)
    }
    
    chosen_tool, confidence = tool_mapping[selected_log]
    latency = round((time.time() - start_time) * 1000 + 115, 2)
    
    st.markdown("---")
    st.subheader("1. Strands Decider 2B Decision")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Selected Action", chosen_tool)
    c2.metric("Confidence Score", f"{int(confidence * 100)}%")
    c3.metric("Latency", f"{latency} ms")
    
    if confidence >= 0.70:
        st.success(f"Action '{chosen_tool}' verified with high confidence. Executing fix...")
    else:
        st.warning(f"Confidence below threshold (70%). Routed to human-in-the-loop.")

    st.markdown("---")
    st.subheader("2. Amazon Bedrock Generative Summary")
    st.info(
        f"**Bedrock Claude 3.5 Sonnet Report:**\n\n"
        f"System state identified: `{selected_log}`. "
        f"Autonomous mitigation applied: `{chosen_tool}`. "
        f"Telemetry stabilized. Zero downtime logged."
    )
