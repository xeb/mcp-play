Create a server and a client Python MCP server.

# Runtime for Both
The server and the client should noth run using 'uv run' and have dependencies install with 'uv add --script'

For example:
```
uv run server.py
uv run client.py
uv add --script server.py "fastmcp"
uv add --script client.py "requests"
```

# Server
The server should host a FastMCP server that has one tool: "get_datetime" that accepts a parameter string of "format" and then returns the current datetime in that format. It should default the format to a default reasonable value. And it should return a single string.

Actually, have two other tools "search" and "fetch" that basically just get data from a records.json file. Create a records.json file as an example if it doesn't exist already.

The docstring for the tool should have a few examples of formats that work including a string like "Today is {reasonable_format}" 

The server should listen on port 8774 and host 0.0.0.0.

The server should log exceptions, requests and everything from the FastMCP server to "server.log" and append to that log.

Use SSE for hosting

# Root Endpoint
The server should serve a simple HTML page on the `/` route. This page should display the text "private MCP server. go away" in large, white, sans-serif text on a black background. The text should be centered on the page.

## Example

```
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
	mcp.run(transport="sse", host="127.0.0.1", port=8000)
```

## Example Search and Fetch

```
import json
from fastmcp import FastMCP

# Load your cupcake order records
with open("records.json", "r", encoding="utf-8") as f:
    RECORDS = json.load(f)

LOOKUP = {r["id"]: r for r in RECORDS}

def create_server():
    mcp = FastMCP(name="Cupcake MCP", instructions="Search cupcake orders")

    @mcp.tool()
    async def search(query: str):
        """
        Search for cupcake orders – keyword match.
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

    @mcp.tool()
    async def fetch(id: str):
        """
        Fetch a cupcake order by ID.
        """
        if id not in LOOKUP:
            raise ValueError("Unknown ID")
        return LOOKUP[id]

    return mcp

if __name__ == "__main__":
    # Start FastMCP server using SSE transport at /sse endpoint
    create_server().run(
        transport="sse",
        host="0.0.0.0",
        port=8000,
        path="/sse"
    )
```

# Client
When run the client should connect to the server, run the get_datetime tool with three example formats and print out the response. It should also test the search and fetch tools with example queries and IDs. It should then say All Good with a green font and green checkmark emoji. The client should have exception handling and print out any errors and end with an "Uh Oh" and red X if there is a problem.

The client should test:
1. **get_datetime tool** - with 3 different format strings
2. **search tool** - with sample queries like "chocolate", "wedding", "birthday"  
3. **fetch tool** - with valid IDs (001, 002) and invalid ID (999) to test error handling

## Example
```
from fastmcp import Client

async def main():
    # Connect via SSE
    async with Client("http://localhost:8000/sse") as client:
        # ... use the client
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result.text}")
        pass
```

## Remote Client
The remote client should support connecting to servers on different hosts and ports via command line arguments:
- `--host` parameter to specify the server host (defaults to http://0.0.0.0)
- `--port` parameter to specify the server port (defaults to 8774)

This allows testing the MCP server from remote machines or different network configurations.

# Testing
To make sure everything works, create server.py, run it in the background, run client.py, and then make sure the logs and output show no errors.



