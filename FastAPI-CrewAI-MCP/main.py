from fastapi import FastAPI
from crews.crew_manager import kickoff_crew
from crews.blogger_crew import kickoff_blogger_crew


app = FastAPI(title="Agentic AI API")

@app.post("/kickoff/")
async def kickoff_crew_endpoint(inputs: dict):
    result = kickoff_crew(inputs)
    return {"result": result}

@app.post("/blogger")
async def kickoff_blogger_crew_endpoint(inputs: dict):
    result =  kickoff_blogger_crew(inputs)
    return {"result": result}