from fastmcp import FastMCP
import asyncio

mcp = FastMCP()

@mcp.tool()
async def fetch():
    """Use This Tool To Fetch Data from a source"""
    return {"data":"Hello,MCP!"}

@mcp.tool()
async def process(path:str):
    """Use This Tool To Process Data from a source"""
    return {"processed_data":"Data Has Been Processed at path: "+path}

if __name__ == "__main__":
    mcp.run(transport = "streamable-http",host = "0.0.0.0",port = 8050)