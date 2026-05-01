# 🚀 Real-Time AI Agent System
```
🧠 Overview

This project is a real-time AI agent system that performs intelligent reasoning, dynamic tool selection
and live web search to generate accurate, context-aware responses.

Unlike basic chatbots, this system simulates autonomous decision-making using multi-step workflows
and tool chaining, making it closer to production-grade AI agents.

✨ Features
  ⚡ Real-time response generation with low latency
  🧠 Multi-step reasoning using agent workflows
  🌐 Live web search for up-to-date information
  🔄 Dynamic tool selection and execution
  📡 Context-aware conversation handling
  🏗️ Scalable and modular backend architecture

🧰 Tech Stack
  🧠 AI / LLM Frameworks
    LangChain – LLM pipelines and tool integration
    LangGraph – Stateful agent workflow orchestration
  🔍 Search & Retrieval
    Tavily Search API – Real-time web search capability
  🤖 Model
    LLaMA – Large Language Model for response generation
  ⚙️ Backend
    FastAPI – High-performance API framework for real-time interaction
  🧩 System Design
    Agent-based architecture
    Async & streaming support
    Tool-calling mechanism


🏗️ Architecture
        User Query
            ↓
        FastAPI Endpoint
            ↓
        LangGraph Agent Workflow
            ↓
        Decision Layer (LLM)
            ↓
        Tool Calling (Search / LLM)
            ↓
        Response Generation
            ↓
        Real-Time Output
```
# Project Setup

### Clone git repo 
```bash
"git clone https://github.com/kaiser-ahmed-siyam/Ai_Agents-" 
```
### Create virtual Environment
```bash
python3.11 -m venv venv
```
### Activate virtual environment
```bash
venv\Scripts\Activate.ps1
```
### Install requirements
```bash
pip install -r requirements.txt
```
### Run the app locally
```bash
uvicorn app:app --reload
```
### Web Application
<a href="https://ai-agents-n59d.onrender.com">Chat-agent<a/>
