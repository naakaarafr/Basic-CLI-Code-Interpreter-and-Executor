import os
import subprocess
import platform

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False
    print("Warning: langchain_google_genai not available")

try:
    from interpreter import interpreter
    INTERPRETER_AVAILABLE = True
    print("Open-interpreter loaded successfully")
except (ImportError, AttributeError, Exception) as e:
    INTERPRETER_AVAILABLE = False
    print(f"Warning: open-interpreter not available ({e}), falling back to subprocess")

# Configuration for Gemini 2.0 Flash
def get_llm():
    """Initialize and return Gemini 2.0 Flash LLM"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required")
    
    if LANGCHAIN_AVAILABLE:
        try:
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-exp",
                temperature=0.1,
                google_api_key=api_key
            )
            return llm
        except Exception as e:
            print(f"Warning: Could not initialize langchain Gemini LLM: {e}")
            raise
    else:
        raise ImportError("langchain_google_genai is required")

def setup_interpreter():
    """Setup open-interpreter with Gemini"""
    if INTERPRETER_AVAILABLE:
        try:
            interpreter.auto_run = True
            interpreter.llm.model = "gemini-2.0-flash-exp"
            interpreter.llm.api_key = os.getenv("GOOGLE_API_KEY")
            return True
        except Exception as e:
            print(f"Warning: Could not setup interpreter: {e}")
            return False
    return False

def execute_command(command):
    """Execute command using open-interpreter or fallback to subprocess"""
    if INTERPRETER_AVAILABLE and setup_interpreter():
        try:
            result = interpreter.chat(command)
            return str(result)
        except Exception as e:
            print(f"Interpreter failed, falling back to subprocess: {e}")
    
    # Fallback to subprocess execution
    try:
        # Handle special OS detection and recycle bin commands
        if "identify the os" in command.lower() or "recycle bin" in command.lower():
            os_name = platform.system()
            result = f"Operating System: {os_name}"
            
            if os_name == "Windows":
                try:
                    subprocess.run(['powershell', '-Command', 'Clear-RecycleBin -Force'], 
                                 check=True, capture_output=True, text=True)
                    result += "\nRecycle bin emptied successfully."
                except Exception as e:
                    result += f"\nFailed to empty recycle bin: {str(e)}"
            
            elif os_name == "Darwin":  # macOS
                try:
                    subprocess.run(['rm', '-rf', os.path.expanduser('~/.Trash/*')], 
                                 shell=True, check=True)
                    result += "\nTrash emptied successfully."
                except Exception as e:
                    result += f"\nFailed to empty trash: {str(e)}"
            
            elif os_name == "Linux":
                try:
                    trash_dirs = [
                        os.path.expanduser('~/.local/share/Trash/files/*'),
                        os.path.expanduser('~/.local/share/Trash/info/*')
                    ]
                    for trash_dir in trash_dirs:
                        subprocess.run(['rm', '-rf', trash_dir], shell=True, check=True)
                    result += "\nTrash emptied successfully."
                except Exception as e:
                    result += f"\nFailed to empty trash: {str(e)}"
            
            return result
        
        # For other commands, execute safely
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"
    
    except subprocess.TimeoutExpired:
        return f"Command timed out: {command}"
    except Exception as e:
        return f"Error executing command '{command}': {str(e)}"