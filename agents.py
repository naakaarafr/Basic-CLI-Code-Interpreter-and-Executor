from crewai import Agent
from config import get_llm
from tools import execute_cli_command

def create_cli_agent():
    """Create and return a CLI Agent configured with Gemini"""
    llm = get_llm()
    
    cli_agent = Agent(
        role='Software Engineer',
        goal='Always use Executor Tool. Ability to perform CLI operations, write programs and execute using Executor Tool',
        backstory='Expert in command line operations, creating and executing code using Gemini AI.',
        tools=[execute_cli_command],
        verbose=True,
        llm=llm
    )
    
    return cli_agent