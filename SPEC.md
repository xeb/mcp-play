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

The docstring for the tool should have a few examples of formats that work including a string like "Today is {reasonable_format}" 

The server should listen on port 8774 and host 0.0.0.0.

The server should log exceptions, requests and everything from the FastMCP server to "server.log" and append to that log.

Use SSE for hosting

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

# Client
When run the client should connect to the server, run the get_datetime tool with three example formats and print out the response. It should then say All Good with a green font and green checkmark emoji. The client should have exception handling and print out any errors and end with an "Uh Oh" and red X if there is a problem.

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

# Testing
To make sure everything works, create server.py, run it in the background, run client.py, and then make sure the logs and output show no errors.



