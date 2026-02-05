from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent

search = GoogleSerperAPIWrapper()

llm= ChatGroq (model="openai/gpt-oss-20b")
agent= create_agent(llm,[search.run])
history= []

while True:
    query = input("user:")
    res = agent.invoke({"messages":[{"role":"user","content":query}]})
    print(f"Bot: {res['messages'][-1].content} \n")
