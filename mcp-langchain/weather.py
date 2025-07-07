from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """
    Function return the weather for a location
    """ 
    return "It's a bright sunny day"

if __name__=="__main__":
    mcp.run(transport="streamable-http")

