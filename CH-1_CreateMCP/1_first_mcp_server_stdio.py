from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetch():
    """Use This Tool To Fetch Data from a source"""
    return {"data":"Hello,MCP!"}

@mcp.tool()
def process():
    """Use This Tool To Process Data from a source"""
    return {"processed_data":"Data Has Been Processed!"}

if __name__ == "__main__":
    mcp.run(transport = "stdio")