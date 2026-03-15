from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP(name="Datetime-MCP")

@mcp.tool()
def get_current_datetime() -> str:
    """Return current datetime"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
