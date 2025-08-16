# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastmcp",
# ]
# ///

import json
import logging
from datetime import datetime
from fastmcp import FastMCP
from fastapi.responses import HTMLResponse
from starlette.requests import Request

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("server.log", mode="a"),
    ],
)

# Load records
with open("records.json", "r", encoding="utf-8") as f:
    RECORDS = json.load(f)

LOOKUP = {r["id"]: r for r in RECORDS}

mcp = FastMCP("DateTime Server 🚀")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>MCP Server</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            font-size: 3em;
        }
    </style>
</head>
<body>
    <h1>private MCP server. go away</h1>
</body>
</html>
"""

@mcp.custom_route("/", methods=["GET"])
async def read_root(request: Request):
    return HTMLResponse(content=html_content)

@mcp.tool
def get_datetime(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Returns the current datetime formatted as a string.

    Args:
        format: A strftime format string.
                Defaults to "%Y-%m-%d %H:%M:%S".

    Examples of format strings:
    - "%Y-%m-%d" -> "2025-08-16"
    - "%I:%M %p" -> "11:30 AM"
    - "Today is %A, %B %d, %Y" -> "Today is Saturday, August 16, 2025"
    """
    try:
        return datetime.now().strftime(format)
    except Exception as e:
        logging.exception("Error formatting datetime")
        return f"Error: {e}"

@mcp.tool
async def search(query: str):
    """
    Search for records - keyword match.
    """
    toks = query.lower().split()
    ids = []
    for r in RECORDS:
        hay = " ".join([
            r.get("title", ""),
            r.get("text", ""),
            " ".join(r.get("metadata", {}).values()),
        ]).lower()
        if any(t in hay for t in toks):
            ids.append(r["id"])
    return {"ids": ids}

@mcp.tool
async def fetch(id: str):
    """
    Fetch a record by ID.
    """
    if id not in LOOKUP:
        raise ValueError("Unknown ID")
    return LOOKUP[id]

if __name__ == "__main__":
    logging.info("Starting FastMCP server")
    mcp.run(transport="sse", host="0.0.0.0", port=8774)
