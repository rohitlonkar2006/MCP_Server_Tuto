
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


{
    "mcpServers": {
        "ddg-search": {
            "command": "uvx",
            "args": ["duckduckgo-mcp-server"]
        }
    }
}


async def main():
    
    #Create Instance of The MultiServerMCPClient
    client = MultiServerMCPClient(
    #MCP Server Config (JSON)
    {
        "data_fetch_mcp_stdio":{
            "transport" : "stdio",
            "command" : r"C:\Users\Samarth\Desktop\MCP_Server_Tuto\.venv\Scripts\python.exe",
            "args" : [r"C:\Users\Samarth\Desktop\MCP_Server_Tuto\CH-1_CreateMCP\1_first_mcp_server_stdio.py"]
        },
        "data_fetch_mcp_http":{
            "transport" : "streamable-http",
            "url" : "http://localhost:8050/mcp"
        }
    }
    )
    
    #List The Tools
    tools = await client.get_tools()
    print("Available Tools:",tools)
    
if __name__ == "__main__":
    asyncio.run(main())
