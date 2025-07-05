from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0.2)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(query: Query):
    response = conversation.run(query.message)
    return {"response": response}
