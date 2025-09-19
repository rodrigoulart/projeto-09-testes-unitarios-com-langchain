from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def criar_cadeia():
    prompt = PromptTemplate.from_file("agent/prompts/test_prompt.txt", input_variables=["code"])

    llm = ChatOpenAI(
        model_name="mistralai/mistral-7b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return prompt | llm
