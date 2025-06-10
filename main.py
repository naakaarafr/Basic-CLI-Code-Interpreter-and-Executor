#!/usr/bin/env python3
"""
Main entry point for the CLI CrewAI application using Gemini 2.0 Flash
"""

import os
from crew import run_crew

def main():
    """Main function to run the CLI crew"""
    # Check if Google API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable is not set.")
        print("Please set your Google API key:")
        print("export GOOGLE_API_KEY='your-api-key-here'")
        return
    
    print("Starting CLI Crew with Gemini 2.0 Flash...")
    print("=" * 50)
    
    try:
        result = run_crew()
        print("\n" + "=" * 50)
        print("CREW EXECUTION COMPLETED")
        print("=" * 50)
        print(result)
    except Exception as e:
        print(f"Error running crew: {str(e)}")
        print("Make sure you have all required dependencies installed:")
        print("- pip install crewai")
        print("- pip install langchain-google-genai")
        print("- pip install open-interpreter (optional)")

if __name__ == "__main__":
    main()