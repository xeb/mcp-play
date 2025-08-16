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

# Client
When run the client should connect to the server, run the get_datetime tool with three example formats and print out the response. It should then say All Good with a green font and green checkmark emoji. The client should have exception handling and print out any errors and end with an "Uh Oh" and red X if there is a problem.

# Testing
To make sure everything works, create server.py, run it in the background, run client.py, and then make sure the logs and output show no errors.
