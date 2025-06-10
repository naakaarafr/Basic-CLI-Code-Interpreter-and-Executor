# Basic CLI Code Interpreter and Executor

A powerful command-line interface application built with CrewAI framework that leverages Google's Gemini 2.0 Flash AI model to perform automated CLI operations, code execution, and system management tasks.

## 🚀 Features

- **AI-Powered CLI Operations**: Execute command-line operations through natural language instructions
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Intelligent Code Execution**: Create and execute code using open-interpreter or fallback subprocess execution
- **System Management**: Built-in OS detection and system cleanup capabilities (recycle bin/trash management)
- **Gemini 2.0 Flash Integration**: Utilizes Google's latest Gemini 2.0 Flash model for enhanced performance
- **Flexible Architecture**: Modular design with separate agents, tasks, and tools

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini 2.0 Flash
- Operating System: Windows, macOS, or Linux

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install required dependencies:**
   ```bash
   pip install crewai
   pip install langchain-google-genai
   pip install open-interpreter  # Optional but recommended
   ```

3. **Set up your Google API Key:**
   ```bash
   # On Linux/macOS
   export GOOGLE_API_KEY='your-api-key-here'
   
   # On Windows (Command Prompt)
   set GOOGLE_API_KEY=your-api-key-here
   
   # On Windows (PowerShell)
   $env:GOOGLE_API_KEY="your-api-key-here"
   ```

   To get a Google API Key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Gemini
   - Copy and set it as an environment variable

## 🚦 Quick Start

Run the application with the default task (OS identification and recycle bin cleanup):

```bash
python main.py
```

## 📁 Project Structure

```
├── main.py          # Entry point of the application
├── config.py        # Configuration and LLM setup
├── agents.py        # Agent definitions and creation
├── tasks.py         # Task definitions and management
├── tools.py         # Custom tools for CLI execution
└── crew.py          # Crew orchestration and execution
```

## 🔧 Core Components

### 1. **Agent (agents.py)**
- **Role**: Software Engineer
- **Goal**: Perform CLI operations and execute code using the Executor Tool
- **Backstory**: Expert in command-line operations with Gemini AI integration
- **Tools**: CLI execution capabilities

### 2. **Tasks (tasks.py)**
- **Default Task**: OS identification and recycle bin cleanup
- **Custom Tasks**: Flexible task creation for various CLI operations
- **Expected Output**: Detailed reports on task completion

### 3. **Tools (tools.py)**
- **Executor Tool**: Primary tool for command execution
- **Dual Execution**: Uses open-interpreter when available, falls back to subprocess
- **Error Handling**: Comprehensive error management and reporting

### 4. **Configuration (config.py)**
- **LLM Setup**: Gemini 2.0 Flash model configuration
- **Interpreter Setup**: Open-interpreter integration
- **Command Execution**: Cross-platform command execution with safety measures

## 🎯 Default Functionality

The application comes with a pre-configured task that:

1. **Identifies the operating system** (Windows, macOS, or Linux)
2. **Empties the recycle bin/trash**:
   - **Windows**: Uses PowerShell `Clear-RecycleBin`
   - **macOS**: Removes files from `~/.Trash/`
   - **Linux**: Cleans `~/.local/share/Trash/`

## 🔄 Customization

### Creating Custom Tasks

You can create custom tasks by modifying `tasks.py` or using the `create_custom_task` function:

```python
from tasks import create_custom_task
from agents import create_cli_agent

# Create agent
agent = create_cli_agent()

# Create custom task
custom_task = create_custom_task(
    agent=agent,
    description="List all Python files in the current directory",
    expected_output="A list of all .py files with their details"
)
```

### Modifying the Default Task

Edit the `create_cli_task` function in `tasks.py`:

```python
def create_cli_task(agent):
    cli_task = Task(
        description='Your custom task description here',
        agent=agent,
        tools=[execute_cli_command],
        expected_output="Your expected output description"
    )
    return cli_task
```

## ⚙️ Configuration Options

### Environment Variables

- `GOOGLE_API_KEY`: Required for Gemini 2.0 Flash access

### Model Configuration

The application uses Gemini 2.0 Flash with these settings:
- **Model**: `gemini-2.0-flash-exp`
- **Temperature**: 0.1 (for more deterministic outputs)
- **Auto-run**: Enabled for open-interpreter

## 🛡️ Safety Features

- **Command Timeout**: 30-second timeout for subprocess execution
- **Error Handling**: Comprehensive exception handling
- **Safe Execution**: Controlled command execution environment
- **Cross-platform Compatibility**: OS-specific command handling

## 🐛 Troubleshooting

### Common Issues

1. **Missing Google API Key**
   ```
   Error: GOOGLE_API_KEY environment variable is not set.
   ```
   **Solution**: Set your Google API key as an environment variable

2. **Import Errors**
   ```
   Warning: langchain_google_genai not available
   ```
   **Solution**: Install required dependencies
   ```bash
   pip install langchain-google-genai
   ```

3. **Open-interpreter Issues**
   ```
   Warning: open-interpreter not available
   ```
   **Solution**: Install open-interpreter (optional)
   ```bash
   pip install open-interpreter
   ```

### Debug Mode

The application runs in verbose mode by default. You can see detailed execution logs in the console output.

## 📊 Example Output

```
Starting CLI Crew with Gemini 2.0 Flash...
==================================================

[Agent Execution Details...]

==================================================
CREW EXECUTION COMPLETED
==================================================

Operating System: Windows
Recycle bin emptied successfully.

Task completed successfully with OS identification and recycle bin cleanup.
```

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 👨‍💻 Author

**naakaarafr** - Project Creator and Maintainer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

## 🔗 Dependencies

- **crewai**: Multi-agent framework for AI collaboration
- **langchain-google-genai**: Google Gemini integration for LangChain
- **open-interpreter**: Optional code execution environment

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Review the error messages for specific guidance
- Ensure all dependencies are properly installed
- Verify your Google API key is valid and has Gemini access

---

**Note**: This application can execute system commands. Use with caution and ensure you understand the commands being executed, especially when creating custom tasks.
