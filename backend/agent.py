import os 
from dotenv import load_dotenv, find_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage  , SystemMessage

from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq

_ = load_dotenv(find_dotenv())  # Load environment variables from .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY


search = TavilySearch(max_results=3)


def get_agent():
    chatModel = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct"
    )
    tools = [search]  # add tools later
    agent = create_agent(chatModel, tools)
    return agent

