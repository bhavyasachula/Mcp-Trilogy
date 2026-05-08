import random
from fastmcp import FastMCP

"""Instance of MCP"""
mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice:int = 1):
    """Roll the n_dice and return the result"""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add_num(a:float,b:float):
    """Adds the given number"""
    return (a+b);

if __name__ == "__main__":
    mcp.run()