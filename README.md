# 🚀 Multi-Agent AI Research Assistant

An intelligent multi-agent system built using LangChain and Ollama that simulates collaborative AI reasoning.

## 🧠 Architecture

This system uses multiple AI agents working together:

- 🧭 Planner → Breaks problem into steps  
- 🔍 Researcher → Retrieves knowledge (RAG using FAISS)  
- 🧠 Critic → Validates and improves responses  
- 📝 Summarizer → Produces final answer  

## ⚙️ Tech Stack

- Python  
- LangChain  
- FAISS (Vector Database)  
- Ollama (Local LLM)  

## 🔥 Features

- Multi-agent orchestration  
- Retrieval-Augmented Generation (RAG)  
- Self-reflection loop (Critic agent)  
- Modular architecture  

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
