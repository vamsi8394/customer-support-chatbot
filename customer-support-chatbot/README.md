# 🤖 Customer Support Chatbot

A FastAPI-based conversational chatbot built using LangChain and GPT-4o for intelligent, real-time support interactions.

---

## 💡 Features

- ✅ Natural language understanding powered by OpenAI GPT-4o  
- 🧠 Contextual memory with LangChain’s `ConversationBufferMemory`  
- ⚡ FastAPI backend for quick deployment and easy API access  
- 🔐 Environment variable support with `.env` and `python-dotenv`

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **FastAPI** — for API routing
- **LangChain** — to manage conversation logic
- **OpenAI** — GPT-4o model
- **Uvicorn** — ASGI server
- **python-dotenv** — for secure API key management

---

## 🚀 Getting Started

### 🔧 Installation

```bash
# 1. Clone the repo
git clone https://github.com/vamsi8394/customer-support-chatbot.git
cd customer-support-chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

