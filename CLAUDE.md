# Claude Code Technical Reference

This document contains technical details for working with this MCP test project.

## Project Structure

```
mcptest/
├── server.py          # FastMCP server with 3 tools
├── client.py          # Test client for all server tools
├── records.json       # Sample cupcake order data
├── server.log         # Server request/error logs
├── SPEC.md           # Original project specification
└── README.md         # Project documentation
```

## Commands for Development

### Server Management
```bash
# Start the MCP server
uv run server.py

# Server runs on http://0.0.0.0:8774/sse
# Web interface available at http://localhost:8774
```

### Client Testing
```bash
# Test against local server
uv run client.py

# Test against remote server
uv run client.py --host http://mcp.xeb.ai --port 8774

# Test with custom host/port
uv run client.py --host http://example.com --port 9000
```

### Dependencies
```bash
# Add server dependencies
uv add --script server.py "fastmcp"

# Add client dependencies  
uv add --script client.py "fastmcp"
```

## API Tools

### 1. get_datetime
- **Purpose**: Returns current datetime in specified format
- **Parameter**: `format` (string, default: "%Y-%m-%d %H:%M:%S")
- **Returns**: Formatted datetime string
- **Example**: `{"format": "Today is %A, %B %d, %Y"}` → `"Today is Saturday, August 16, 2025"`

### 2. search
- **Purpose**: Search records by keyword matching
- **Parameter**: `query` (string)
- **Returns**: `{"ids": ["001", "002"]}` 
- **Example**: `{"query": "chocolate"}` → `{"ids": ["001"]}`

### 3. fetch
- **Parameter**: `id` (string)
- **Returns**: Complete record object
- **Error**: Throws "Unknown ID" for invalid IDs
- **Example**: `{"id": "001"}` → Full cupcake order details

## Data Format (records.json)

Each record contains:
```json
{
  "id": "001",
  "title": "Order Title",
  "text": "Description of the order",
  "metadata": {
    "customer": "Customer Name",
    "quantity": "24", 
    "flavor": "chocolate",
    "frosting": "vanilla",
    "event": "birthday"
  }
}
```

## Testing Strategy

The client tests all functionality:
- ✅ 3 datetime format variations
- ✅ Search with multiple keywords
- ✅ Fetch valid records (001, 002)
- ✅ Error handling for invalid ID (999)

## Logging

All server activity is logged to `server.log`:
- Request details
- Tool executions
- Exceptions and errors
- Server startup/shutdown

## Remote Server

Demo server available at:
- **URL**: `mcp.xeb.ai:8774`
- **Status**: Updated periodically
- **Use**: Testing MCP clients against live server

## Troubleshooting

### Port Already in Use
```bash
# Kill existing processes on port 8774
lsof -ti:8774 | xargs kill -9
```

### Connection Issues
- Verify server is running: Check for "Uvicorn running" message
- Test local connection first before trying remote
- Check firewall settings for port 8774

### Tools Not Working
- Ensure `records.json` exists and is valid JSON
- Check `server.log` for detailed error information
- Verify FastMCP version compatibility