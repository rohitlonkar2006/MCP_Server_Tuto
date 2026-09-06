from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

async def main():
    
    #Create Instance of The MultiServerMCPClient
    client = MultiServerMCPClient(
    #MCP Server Config (JSON)
    {
        "agentic_terminal":{
            "transport" : "stdio",
            "command" : "uvx",
            "args" : ["agentic_terminal"]
        }
    }
    )
    
    #List The Tools
    tools = await client.get_tools()
    print("Available Tools:",len(tools))
    
    for tool in tools:
        print(tool.name)
        
    
if __name__ == "__main__":
    asyncio.run(main())
