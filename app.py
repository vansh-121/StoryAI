from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain Sever",
    version="1.0",
    description="API Server",
)

llm = Ollama(model= "llama3.1")

prompt = ChatPromptTemplate.from_template("Write me a story on {topic} in 300 words")

add_routes(
    app,
    prompt|llm,
    path= "/story"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
