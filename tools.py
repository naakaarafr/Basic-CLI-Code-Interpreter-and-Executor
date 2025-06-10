from langchain.tools import tool
from config import execute_command

class CLITool:
    @staticmethod
    @tool("Executor")
    def execute_cli_command(command: str) -> str:
        """Create and Execute code using Open Interpreter or fallback execution."""
        try:
            result = execute_command(command)
            return str(result)
        except Exception as e:
            return f"Error executing command: {str(e)}"

# Export the tool function for easy import
execute_cli_command = CLITool.execute_cli_command