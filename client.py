# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastmcp",
# ]
# ///
import asyncio
import argparse
from fastmcp import Client

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

async def main():
    """Connects to the server and calls the get_datetime tool."""
    parser = argparse.ArgumentParser(description="MCP Client")
    parser.add_argument("--host", default="http://0.0.0.0", help="The host to connect to.")
    parser.add_argument("--port", type=int, default=8774, help="The port to connect to.")
    args = parser.parse_args()

    url = f"{args.host}:{args.port}/sse"

    try:
        print(f"Connecting to server at {url}...")
        async with Client(url) as client:
            print("Connection successful. Testing all tools...")

            # Test get_datetime tool
            print("\n1. Testing 'get_datetime' tool:")
            formats_to_test = [
                "%Y-%m-%d %H:%M:%S",
                "%A, %B %d, %Y",
                "The current time is %I:%M:%S %p",
            ]

            for fmt in formats_to_test:
                print(f"  - Requesting with format: '{fmt}'")
                result = await client.call_tool("get_datetime", {"format": fmt})
                print(f"    Response: {result.data}")

            # Test search tool
            print("\n2. Testing 'search' tool:")
            search_queries = ["chocolate", "wedding", "birthday"]
            for query in search_queries:
                print(f"  - Searching for: '{query}'")
                result = await client.call_tool("search", {"query": query})
                print(f"    Found IDs: {result.data}")

            # Test fetch tool
            print("\n3. Testing 'fetch' tool:")
            test_ids = ["001", "002", "999"]
            for test_id in test_ids:
                print(f"  - Fetching ID: '{test_id}'")
                try:
                    result = await client.call_tool("fetch", {"id": test_id})
                    print(f"    Response: {result.data.get('title', 'No title')}")
                except Exception as e:
                    print(f"    Error: {e}")

        print(f"\n{GREEN}✔ All Good{RESET}")

    except Exception as e:
        print(f"\n{RED}❌ Uh Oh: An error occurred.{RESET}")
        print(f"   Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
