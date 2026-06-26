# MCP Fast Demo

This repository contains a minimal demo MCP server built with FastAPI and a tiny demo client.

Quick start

1. Create a virtualenv and install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the server:

```bash
python server.py
```

3. In another terminal run the demo client:

```bash
python demo_client.py
```

Notes

- `server.py` provides two endpoints: `/mcp/start` and `/mcp/handle` that echo inputs.
- Replace the handler with real model integration to implement a full MCP server.
