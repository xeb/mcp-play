# 🧁 MCP Cupcake Chronicles

> *"Why build a todo app when you can build a cupcake order tracking system?"*

Welcome to the most deliciously unnecessary MCP (Model Context Protocol) server in existence! This project exists purely for fun, testing, and the noble pursuit of perfectly tracked cupcake orders.

## What Does This Thing Do?

This delightfully over-engineered system provides three incredibly important services:

1. **🕐 Time Telling** - Because apparently `date` command wasn't good enough
2. **🔍 Cupcake Search** - Find cupcakes by keyword (finally!)  
3. **📋 Order Fetching** - Retrieve detailed cupcake order information (life-changing!)

## Why Did We Build This?

Great question! The answer is: ¯\\_(ツ)_/¯

Actually, this project serves as a test bed for MCP server/client implementations. It's like a sandbox, but instead of sand, it's filled with virtual cupcakes and an inexplicable need to know what time it is in 47 different formats.

## Quick Start

Fire up the server:
```bash
uv run server.py
```

Test it with the client:
```bash
uv run client.py
```

Or connect to our remote demo server (updated periodically when we remember):
```bash
uv run client.py --host http://mcp.xeb.ai --port 8774
```

## Features That Nobody Asked For

- 🌐 **Web Interface**: Visit `http://localhost:8774` for a super welcoming message
- 📝 **Comprehensive Logging**: Every request is logged because we're very serious about cupcake accountability
- 🎯 **Smart Search**: Find that chocolate birthday cupcake order from 2 months ago
- 🛡️ **Error Handling**: Gracefully fails when you ask for cupcake order #999 (it doesn't exist, trust us)

## Remote Testing

Want to test against our remote server? It's running at `mcp.xeb.ai:8774` (when it's not broken). Perfect for testing your MCP client implementations or just seeing if our server can handle your wildest datetime format requests.

## Contributing

Found a bug? Want to add more ridiculous cupcake orders? PRs welcome! Just remember: this is serious cupcake business.

## License

This project is licensed under the "Do Whatever You Want With It" license. Use responsibly (or irresponsibly, we're not your boss).

---

*Built with 💜 and an unhealthy obsession with properly formatted timestamps*