# Langchain-PROMPTS

This project demonstrates core concepts of **LangChain**, including prompt engineering, chat templates, message handling, and building a simple chatbot workflow.

---

## 📁 Project Structure

```
├── chat_history.txt          # Stores chat history (user + AI messages)
├── chatbot.py                # Main chatbot implementation
├── chatpromptTemplate.py     # ChatPromptTemplate examples
├── message_placeholder.py    # MessagesPlaceholder usage
├── messages.py               # Message types (Human, AI, System)
├── prompt_generator.py       # Dynamic prompt generation
├── temperature.py            # LLM temperature experiments
├── template.json             # Prompt templates (JSON format)
├── ui.py                     # Simple UI (likely Streamlit)
```

---

## 🧠 Concepts Covered

* Prompt Engineering
* Static vs Dynamic Prompts
* `PromptTemplate`
* `ChatPromptTemplate`
* Message Types:

  * HumanMessage
  * AIMessage
  * SystemMessage
* `MessagesPlaceholder` (chat history handling)
* LLM parameters (like temperature)
* Basic chatbot pipeline

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

### 2. Install Dependencies

```bash
pip install langchain langchain-core langchain-openai python-dotenv streamlit
```

### 3. Set API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🚀 How to Run

### ▶ Run Chatbot

```bash
python chatbot.py
```

### ▶ Test Prompt Templates

```bash
python chatpromptTemplate.py
```

### ▶ Test Message Placeholder

```bash
python message_placeholder.py
```

### ▶ Run UI (if using Streamlit)

```bash
streamlit run ui.py
```

---

## 📌 Important Notes

* `MessagesPlaceholder` requires **list of message objects**, not strings.
* Chat history should ideally be stored in **structured format (JSON)** instead of plain text.
* Variable names in templates must match exactly (avoid typos like `chat_hsitory` ❌).

---

## 🎯 Learning Outcome

By working on this project, you will understand:

* How LLMs interact using structured prompts
* How to build dynamic and scalable prompt systems
* How to manage conversation flow in chat applications

---

