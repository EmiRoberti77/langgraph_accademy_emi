# LangGraph Academy - Project Documentation

## 🌟 Introduction

The **LangGraph Academy** repository is an advanced framework built using Python, designed to streamline the creation and management of **stateful workflows** for conversational AI applications. The project leverages libraries like `langgraph`, `langchain`, and `pydantic` to construct modular, scalable, and interactive workflows. It also incorporates tools for integrating external APIs, handling memory states, and dynamically managing logical decision-making in conversations.

This repository demonstrates various use cases, such as building chatbots, creating dynamic decision graphs, and integrating external tools for tasks like mathematical operations, holiday booking, and web searches.

## ✨ Features

The repository is rich in features, including:

1. **State Graph Construction**:

   - Build stateful workflows using `StateGraph` from the `langgraph` library.
   - Define nodes, edges, and conditional logic for dynamic conversational flows.

2. **LLM Integration**:

   - Seamless integration with OpenAI's GPT models (`gpt-4o`) via the `langchain_openai` library.
   - Support for tool-based reasoning and chained tool invocations.

3. **External Memory Management**:

   - Store and retrieve conversation history using SQLite-backed memory.

4. **Multi-Tool Support**:

   - Tools for mathematical operations, holiday booking, and data fetching (e.g., Wikipedia & Tavily search).

5. **Dynamic Logic Handling**:

   - Decision-making based on random probabilities or user-defined conditions.

6. **Validation and Configuration**:

   - Use of `pydantic` for schema validation and `dataclasses` for data modeling.

7. **Graph Visualization**:

   - Visualize workflows using Mermaid diagrams.

8. **Streaming and Interruptions**:

   - Real-time conversational streaming with the ability to handle interruptions.

9. **Flexible APIs**:
   - Modular nodes for custom workflows and reusable components.

---

## 🛠️ Requirements

To run the project, ensure the following dependencies are installed:

Python `3.11`
Libraries:

- `langgraph`
- `langgraph-sdk`
- `langgraph-checkpoint-sqlite`
- `langsmith`
- `langchain-community`
- `langchain-core`
- `langchain-openai`
- `tavily-python`
- `wikipedia`
- `trustcall`
- `python-dotenv`
- `ipython`
- `notebook`

Install the dependencies using the `requirements.txt` file provided in each module or the root directory.

---

## 📦 Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/EmiRoberti77/langgraph_accademy_emi.git
   cd langgraph_accademy_emi
   ```

Emi Roberti - Happy Langchain coding
