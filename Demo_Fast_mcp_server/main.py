from fastmcp import FastMCP
import random

"""Instance of MCP"""
mcp = FastMCP(name="Demo Server")

@mcp.tool()
def roll_dice(n_dice:int = 1):
    """Roll the n_dice and return the result"""
    return [random.randint(1,6) for _ in range(n_dice)]


@mcp.tool()
def add_num(a:float,b:float):
    """Adds the given number"""
    return (a+b);
@mcp.tool()
def Generate_random_given_num(min_value:int = 1,max_value:int = 100):
    """Generate the number between min_value and max_value

    Args:
        min_value:minimum value default = 1
        max_value:maximum value default = 100

        if the number is not given use the default min and max value"""
    return random.randint(min_value,max_value);

if __name__ == "__main__":
    mcp.run(transport="stdio")

"""
    Default path of claude should be Appdata/Roaming/Claude
    Otherwise i will give u an 
    error:can find the main.py
    first run :-
    'uv run fastmcp install claude-desktop filename(In my case main.py)'
    if this doesn't work use
    uvx run fastmcp install filename(main.py)
"""