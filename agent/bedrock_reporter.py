import boto3
import json

def generate_incident_report(log_context: str, tool_used: str, result_data: str) -> str:
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    
    prompt = f"""
    You are an autonomous Cloud Incident Responder.
    System Log: {log_context}
    Action Taken: {tool_used}
    Execution Output: {result_data}
    
    Provide a concise technical incident summary and post-mortem mitigation note.
    """
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    })
    
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body=body
    )
    response_body = json.loads(response.get("body").read())
    return response_body["content"][0]["text"]