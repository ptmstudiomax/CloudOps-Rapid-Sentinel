# ⚡ CloudOps Rapid Sentinel

Autonomous Cloud Incident Triage Agent powered by **AWS Strands Decider 2B** and **Amazon Bedrock**.

Tags: `#strands-decider-2b` `#tool-selection`

## Overview
Traditional large language models (LLMs) introduce 1.5s–3.0s of latency when selecting tools in mission-critical environments. CloudOps Rapid Sentinel utilizes **Strands Decider 2B** to perform sub-120ms tool classification with calibrated confidence scoring, escalating ambiguous events to humans while resolving confirmed operational alerts via Amazon Bedrock synthesis.

## Decision Pattern: Fast Tool Router (`#tool-selection`)
Located in `patterns/decider_tool_router.py`.

- **State Input**: System telemetry and alert logs
- **Decision**: Immediate remediation action (`scale_db_pool`, `restart_gateway_pods`, `increase_pod_memory_limit`, or human escalation)
- **Latency**: ~115ms
- **Calibrated Confidence**: Threshold set at 70%

## Quickstart

```bash
pip install -r requirements.txt
streamlit run agent/app.py