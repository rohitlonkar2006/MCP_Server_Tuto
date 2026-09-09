from fastmcp import FastMCP
from fastmcp.server import create_proxy

mcp = FastMCP("MCP Gateway")

@mcp.tool()
async def fetch_http():
    """Use This Tool To Fetch Data from a source"""
    return {"data": "Hello, MCP!"}

@mcp.tool()
async def process_http(path: str):
    """Use This Tool To Process Data from a source"""
    return {"processed_data": "Data Has Been Processed at path: " + path}


mcp.mount(
    create_proxy({
        "mcpServers": {
            "ddg_mcp": {
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
    }),
    namespace="ddg_mcp"
)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8050
    )