🤖 Auto Code Builder (LangGraph + LLM)

An AI-powered multi-agent code generation system that automatically creates a complete project structure from a simple natural language prompt.

This system leverages a LangGraph agent pipeline, where multiple AI agents collaborate to:

Plan the project
Design the architecture
Generate production-ready code files

Users only need to describe their idea — the system generates a fully structured, ready-to-use codebase.

🚀 Project Demo
Application Interface

Generated Code Files

Features
AI-powered automatic code generation
Multi-agent architecture using LangGraph
Generates complete multi-file projects
Automatic project planning
Intelligent architecture design
Generates both frontend and backend code
Clean interactive Streamlit UI
Automatically saves generated code to project folder
System Architecture

The system follows a multi-agent workflow pipeline, where each agent performs a specialized task.

User Prompt
      ↓
Planner Agent
      ↓
Architect Agent
      ↓
Coder Agent
      ↓
Generated Code Files

Each agent communicates through a shared state, enabling seamless collaboration across the LangGraph pipeline.

Agents Overview
Planner Agent

The Planner Agent interprets the user's request and creates a high-level development plan.

Example Output:
Project goal
Key features
Suggested technologies
Architect Agent

The Architect Agent transforms the plan into a technical system design.

Example Output:
Project structure
Required files
Component responsibilities
Coder Agent

The Coder Agent generates the actual source code files based on the architecture.

Responsibilities:
Create project folders
Generate code for each file
Ensure modular and clean structure
📁 Project Structure
auto-code-builder
│
├── agents
│   ├── graph.py
│   ├── prompts.py
│
├── app
│   └── streamlit_app.py
│
├── generated_project
│
├── assets
│   ├── ui.png
│   └── files.png
│
├── requirements.txt
└── README.md
Live Demo

👉 https://ai-auto-code-builder-using-langgraph-and-llm-agents-cgvcvzsavp.streamlit.app/

⚙️ Installation
git clone https://github.com/your-username/auto-code-builder.git
cd auto-code-builder
pip install -r requirements.txt
streamlit run app/streamlit_app.py
Tech Stack
LangGraph
LLMs (Groq / OpenAI / Gemini)
Streamlit
Python
Future Improvements
Add support for more frameworks (React, FastAPI, etc.)
Improve code quality with testing agents
Add deployment automation
Enable real-time editing of generated code
👨‍💻 Author

Yugaram
Department of Artificial Intelligence and Data Science
