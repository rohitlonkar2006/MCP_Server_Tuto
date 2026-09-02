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
            "command" : "uvx",
            "args" : ["duckduckgo-mcp-server"]
        },
        "data_fetch_mcp_http":{
            "transport" : "streamable-http",
            "url" : "http://localhost:8050/mcp"
        }
    }
    )
    
    #List The Tools
    tools = await client.get_tools()
    print("Available Tools:",len(tools))
    
    for tool in tools:
        print(tool.name)
        
    # result = await client.invoke("search",{"query":"what is the capital of france"})
    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query":"What Is The Capital Of France?"})
    print("Tool Result",result)
    
if __name__ == "__main__":
    asyncio.run(main())
