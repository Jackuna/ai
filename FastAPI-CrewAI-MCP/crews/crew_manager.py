import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
#load_dotenv()
# Optional: Use environment variables for API keys

ollama_llm = LLM(
		model="ollama/qwen3:1.7b",
		base_url="http://localhost:11434"
	)
def create_crew():
    # Define agents
    researcher = Agent(
        role='Researcher',
        goal='Conduct thorough research on {topic}',
        verbose=True,
        memory=True,
        backstory='A diligent researcher passionate about uncovering insights.',
        llm=ollama_llm
    )

    writer = Agent(
        role='Writer',
        goal='Write a compelling article about {topic}',
        verbose=True,
        memory=True,
        backstory='A creative writer who simplifies complex topics.',
        llm=ollama_llm
    )

    # Define tasks
    research_task = Task(
        description=(
            "Research the topic and gather key points."
            "Your report should include the pros and cons."
        ),
        expected_output='A detailed summary of the topic.',
        agent=researcher,
    )

    write_task = Task(
        description=(
            "Write an article based on the research."
            "Make it engaging and informative."
        ),
        expected_output='A 500-word article in markdown format.',
        agent=writer,
    )

    # Define crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    return crew

# Send payload in UI
def kickoff_crew(inputs):
    crew = create_crew()
    return crew.kickoff(inputs=inputs)

#kickoff_crew({"topic": "Java Moss"})