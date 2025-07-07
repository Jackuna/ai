from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)-> int:
    """
    Function to add two numbers and return their product
    """
    return a+b

@mcp.tool()
def myultiply(a:int, b:int)-> int:
    """
    Function to multiply two numbers and return their product
    """
    return a*b

if __name__=="__main__":
    # transport="stdio", this argument tells the mcp server to
    # use standard input/outupt (stdin and stdout) to receive and respond
    # to function calls interactively
    mcp.run(transport="stdio")

