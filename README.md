# 💻 Auto Code Builder

An **AI-powered multi-agent code generation system** that converts natural language ideas into a complete, working codebase.

Built using **LangGraph + LLM agents**, this project simulates a real-world software development workflow where multiple agents collaborate to plan, design, and generate code.

---

## 🚀 Live Demo

👉 [https://aiagentproject-1.streamlit.app/](https://aiagentproject-1.streamlit.app/)

---

## 📸 Preview

### 🖥️ Application UI

![UI](assets/ui.png)

### 📂 Generated Code Output

![Output](assets/files.png)

---

## ✨ Features

* 🤖 AI-powered code generation from simple text prompts
* 🧠 Multi-agent system (Planner → Architect → Coder)
* 📁 Generates complete multi-file projects
* 🏗️ Automatic project planning and architecture design
* 🌐 Supports frontend and backend generation
* 🎨 Clean Streamlit-based UI
* 💾 Automatically saves generated files locally

---

## 🧠 How It Works

```
User Prompt
     ↓
Planner Agent
     ↓
Architect Agent
     ↓
Coder Agent
     ↓
Generated Code Files
```

Each agent contributes to building the final project step-by-step.

---

## 🤖 Agents

### Planner Agent

* Understands the user prompt
* Creates a high-level plan

### Architect Agent

* Designs project structure
* Defines components and responsibilities

### Coder Agent

* Generates actual code files
* Produces ready-to-run code

---

## 📂 Project Structure

```
auto-code-builder/
│
├── app.py
├── graph.py
├── prompts.py
├── generated_project/
│
├── assets/
│   ├── ui.png
│   └── files.png
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/auto-code-builder.git
cd auto-code-builder

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example

```
Build a blog app with FastAPI backend and React frontend with authentication.
```

## 🚧 Future Improvements

* Download generated code as ZIP
* More frameworks support
* Deployment-ready projects

---

