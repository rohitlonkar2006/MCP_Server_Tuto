from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

async def main():
    
    #Create Instance of The MultiServerMCPClient
    client = MultiServerMCPClient(
    #MCP Server Config (JSON)
    {
        "data_fetch_mcp_stdio":{
            "transport" : "stdio",
            "command" : r"C:\Users\Samarth\Desktop\MCP_Server_Tuto\.venv\Scripts\python.exe",
            "args" : [r"C:\Users\Samarth\Desktop\MCP_Server_Tuto\CH-1_CreateMCP\1_first_mcp_server_stdio.py"]
        }
    }
    )
    
    #List The Tools
    tools = await client.get_tools()
    print("Available Tools:",tools)
    
if __name__ == "__main__":
    asyncio.run(main())