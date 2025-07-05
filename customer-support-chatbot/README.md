# 🤖 Customer Support Chatbot

A FastAPI-based chatbot using GPT and LangChain.

## 💡 Features
- Conversational memory with LangChain
- FastAPI backend
- GPT-4o via OpenAI

## 🚀 Usage

Run the app:
    uvicorn app.main:app --reload

Send a POST request to `/chat`:
    {
      "message": "Hi, I need help"
    }

## 🛠 Requirements

Install dependencies:
    pip install -r requirements.txt

## 📄 License

MIT
