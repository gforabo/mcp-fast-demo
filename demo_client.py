import requests

BASE = "http://127.0.0.1:8000"

def start_session():
    r = requests.post(f"{BASE}/mcp/start", json={"session_id": "demo-1", "input": {}})
    print("start =>", r.json())

def send_input(payload):
    r = requests.post(f"{BASE}/mcp/handle", json={"session_id": "demo-1", "input": payload})
    print("handle =>", r.json())

if __name__ == '__main__':
    start_session()
    send_input({"message": "hello MCP"})
