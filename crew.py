from crewai import Crew, Process
from config import get_llm
from agents import create_cli_agent
from tasks import create_cli_task

def create_cli_crew():
    """Create and return a CLI-focused Crew with Gemini"""
    llm = get_llm()
    
    # Create agent
    cli_agent = create_cli_agent()
    
    # Create task
    cli_task = create_cli_task(cli_agent)
    
    # Create crew
    cli_crew = Crew(
        agents=[cli_agent],
        tasks=[cli_task],
        process=Process.sequential,
        manager_llm=llm,
        verbose=True
    )
    
    return cli_crew

def run_crew():
    """Create and run the CLI crew"""
    crew = create_cli_crew()
    result = crew.kickoff()
    return result