import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool

# Optional: Use environment variables for API keys

ollama_llm = LLM(
		model="ollama/qwen3:1.7b",
		base_url="http://localhost:11434"
	)
def create_blogger_crew():
    # Define agents
    researcher = Agent(
        role='Researcher',
        goal='Search the internet and Conduct thorough research on {topic} for year {year}',
        verbose=True,
        tools=[SerperDevTool()],
        memory=True,
        backstory='''You're a seasoned researcher with a knack for uncovering the latest
                     developments in {topic}. Known for your ability to find the most relevant
                     information and present it in a clear and concise manne''',
                     
        llm=ollama_llm
    )
    website_scrapper = Agent(
        role='Website Content Scrapper',
        goal='Scrape the website for latest information on {topic}',
        verbose=True,
        tools=[ScrapeWebsiteTool()],
        memory=True,
        backstory='''You're a skilled web scraper with a knack for extracting valuable information
                     from websites. Known for your attention to detail and ability to navigate
                     complex websites to find the most relevant content.''',
        llm=ollama_llm
        
    )
    writer = Agent(
        role='Writer',
        goal='Write a compelling article about {topic}',
        verbose=True,
        memory=True,
        backstory='A creative writer who simplifies complex topics.',
        llm=ollama_llm,
        tools=[FileWriterTool()]
        
    )

    # Define tasks
    research_task = Task(
        description=(
            "Search the internet, Research about the topic and then gather key points with the most relevant information about {topic} for year {year}."
            "Do add refrence link along with the key points."
        ),
        expected_output='The list of 10 websites with the most relevant information about {topic} for year {year}',
        agent=researcher,
    )

    website_scrappe_task = Task(
        description=(
            "Scrape the websites to gather the latest information"
        ),
        expected_output='Fully scraped websites about {topic} with title, url and snippet',
        agent=website_scrapper,
    )

    write_task = Task(
        description=(
            "Write an article."
            "Make it engaging and informative."
        ),
        expected_output='An article in markdown format not exceeding 1000 words',
        output_file='news/report.md',
        agent=writer,
    )
 

    # Define crew
    crew = Crew(
        agents=[researcher, website_scrapper, writer],
        tasks=[research_task, website_scrappe_task, write_task],
        process=Process.sequential,
    )

    return crew

# Send payload in UI
def kickoff_blogger_crew(inputs):
    crew = create_blogger_crew()
    response = crew.kickoff(inputs=inputs)
    return response