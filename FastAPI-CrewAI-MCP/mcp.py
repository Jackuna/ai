from main import app
from fastapi_mcp import FastApiMCP


# Add MCP server to the FastAPI app
mcp = FastApiMCP(
    app,
    name="Item API MCP",
    description="MCP server with FAST API",
    describe_full_response_schema=True,  # Describe the full response JSON-schema instead of just a response example
    describe_all_responses=True,  # Describe all the possible responses instead of just the success (2XX) response
)
# Mount the MCP server to the FastAPI app
mcp.mount()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)