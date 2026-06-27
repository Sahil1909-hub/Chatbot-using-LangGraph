# 🤖 AI Chatbot with LangGraph

An intelligent, multi-functional AI chatbot built using **LangGraph**, featuring real-time streaming responses, persistent conversation memory, intelligent tool calling, and containerized deployment using Docker.

Designed to provide a seamless conversational experience while demonstrating practical implementations of Agentic AI concepts.

---

## 🚀 Features

### 💬 Real-Time Streaming Responses

* Token-by-token response streaming for a smooth conversational experience.
* Interactive and responsive chat interface built with Streamlit.

### 🧠 Persistent Chat Memory

* Stores conversations using SQLite.
* Maintains context across sessions.
* Resume previous conversations anytime.

### 📜 Chat History & Resume Chat

* View previous conversations.
* Continue chats without losing context.
* Persistent conversation management using LangGraph checkpoints.

### 🛠️ Intelligent Tool Calling

The chatbot automatically determines when to use external tools.

#### ➕ Calculator Tool

* Perform arithmetic calculations.
* Supports addition, subtraction, multiplication, and division.

#### 📈 Stock Price Tool

* Retrieve the latest stock prices using the Alpha Vantage API.

#### 🔍 DuckDuckGo Search Tool

* Search the web for up-to-date information.
* Enhance responses with external knowledge.

### ⚡ LangGraph Workflow

* Built using LangGraph's graph-based architecture.
* Supports dynamic reasoning and tool execution.
* Easily extensible with additional tools.

### 🎨 Streamlit User Interface

* Clean and user-friendly interface.
* Real-time streaming responses.
* Interactive chat experience.

### 🐳 Docker Support

* Containerized application using Docker.
* Easy setup with a single build and run command.
* Consistent development environment across different operating systems.

---

## 🏗️ Tech Stack

* Python
* LangGraph
* LangChain
* Streamlit
* SQLite
* Docker
* DuckDuckGo Search
* Alpha Vantage API
* Groq LLM

---

## 🎯 Use Cases

* AI Assistant
* Research Assistant
* Financial Information Lookup
* Educational Chatbot
* Personal Productivity Assistant
* Tool-Augmented AI Applications

---

## 🔄 Workflow

1. User sends a message.
2. LangGraph processes the request.
3. The agent determines whether a tool is required.
4. Appropriate tools are executed when needed.
5. The LLM generates a context-aware response.
6. Responses are streamed back to the user in real time.
7. Conversations are stored in SQLite for future sessions.

---

## 🌟 Key Highlights

* ✅ LangGraph Agent Workflow
* ✅ Real-Time Streaming Responses
* ✅ Persistent SQLite Memory
* ✅ Resume Previous Conversations
* ✅ Intelligent Tool Calling
* ✅ Calculator Tool
* ✅ Stock Price Retrieval
* ✅ DuckDuckGo Search Integration
* ✅ Modern Streamlit UI
* ✅ Docker Support
* ✅ Modular Python Architecture
* ✅ Easily Extensible Design

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker build -t langgraph-chatbot .
```

Run the container:

```bash
docker run -p 8501:8501 --env-file .env langgraph-chatbot
```

The application will be available at:

```
http://localhost:8501
```

---

## 📸 Demo

Chat with an AI assistant, perform calculations, search the web, retrieve stock prices, and continue previous conversations—all through a single interactive interface.

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome. Feel free to open an issue or submit a pull request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports future development.

---

Built with ❤️ using **LangGraph**, **Streamlit**, **Python**, and **Docker**.
