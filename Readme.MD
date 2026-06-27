# 🤖 AI Chatbot with LangGraph

An intelligent, multi-functional AI chatbot built using **LangGraph**, featuring real-time streaming responses, persistent conversation memory, and intelligent tool calling.

Designed to provide a seamless conversational experience while demonstrating practical implementations of agentic AI concepts.

---

## 🚀 Features

### 💬 Real-Time Streaming Responses
- Token-by-token response streaming for a smooth user experience.
- Interactive and responsive chat interface built with Streamlit.

### 🧠 Persistent Chat Memory
- Stores conversations using SQLite.
- Maintains context across sessions.
- Enables users to resume previous conversations anytime.

### 📜 Chat History & Resume Chat
- View previous conversations.
- Continue past chats without losing context.
- Organized conversation management.

### 🛠️ Tool Calling Support

The chatbot intelligently decides when to invoke external tools based on the user's request.

#### ➕ Calculator Tool
- Perform mathematical calculations.
- Solve arithmetic expressions instantly.

#### 📈 Stock Price Tool
- Retrieve current stock market information.

#### 🔍 DuckDuckGo Search Tool
- Search the web for up-to-date information.
- Enhance responses with external knowledge.

### 🎨 Streamlit User Interface
- Clean and intuitive interface.
- Interactive chat experience.
- Real-time response rendering.

### ⚡ LangGraph Workflow
- Built using LangGraph's graph-based architecture.
- Supports agent reasoning and dynamic tool execution.
- Easily extensible with additional tools and workflows.

---

## 🏗️ Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **Streamlit**
- **SQLite**
- **DuckDuckGo Search**
- **Stock Data API**

---

## 🎯 Use Cases

- General-purpose AI assistant
- Research assistant
- Financial information lookup
- Educational chatbot
- Personal productivity assistant

---

## 🔄 Workflow

1. User sends a message.
2. LangGraph processes the request.
3. The agent determines whether a tool is required.
4. Relevant tools are executed when needed.
5. The LLM generates a context-aware response.
6. The response is streamed back to the user in real time.
7. The conversation is stored in SQLite for future sessions.

---

## 🌟 Key Highlights

- ✅ Real-time streaming responses
- ✅ Persistent memory with SQLite
- ✅ Resume previous conversations
- ✅ Intelligent tool calling
- ✅ Calculator Tool
- ✅ Stock Price Tool
- ✅ DuckDuckGo Search Integration
- ✅ Modern Streamlit UI
- ✅ LangGraph Agent Workflow
- ✅ Easily extensible architecture

---

## 📸 Demo

Chat with an AI assistant, perform calculations, search the web, check stock prices, and continue previous conversations—all from a single interface.

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome. Feel free to open an issue or submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports future development.

---

Built with ❤️ using **LangGraph**, **Streamlit**, and **Python**.