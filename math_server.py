from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    summary
    Add two numbers
    """
    return a + b

@mcp.tool()
def sub(a: int, b: int) -> int:
    return a - b


if __name__ == "__main__":
    mcp.run(transport="stdio")   