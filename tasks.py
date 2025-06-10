from crewai import Task
from tools import execute_cli_command

def create_cli_task(agent):
    """Create and return a CLI Task"""
    cli_task = Task(
        description='Identify the OS and then empty my recycle bin',
        agent=agent,
        tools=[execute_cli_command],
        expected_output="A report on the OS identification and confirmation that the recycle bin has been emptied"
    )
    
    return cli_task

def create_custom_task(agent, description, expected_output=None):
    """Create a custom task with the given description"""
    task = Task(
        description=description,
        agent=agent,
        tools=[execute_cli_command],
        expected_output=expected_output or f"Completion report for: {description}"
    )
    
    return task