from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(title="MCP Fast Demo")

class MCPRequest(BaseModel):
    session_id: str | None = None
    input: Dict[str, Any]

@app.post("/mcp/start")
async def start_mcp(req: MCPRequest):
    return {"status": "started", "session_id": req.session_id or "demo-session"}

@app.post("/mcp/handle")
async def handle_mcp(req: MCPRequest):
    # Minimal echoing MCP handler — replace with real model integration
    inp = req.input
    return {"session_id": req.session_id or "demo-session", "output": {"echo": inp}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
