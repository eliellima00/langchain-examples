from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient 
from pprint import pprint

load_dotenv()
tavily_client = TavilyClient()

@tool()
def web_search (query: str): 
  """Search the web for information"""
  return tavily_client.search(query)

agent  = create_agent(
  model="gpt-5-nano",
  tools=[web_search]
)

question = HumanMessage(content="Who is the president of Brazil?")

response = agent.invoke(
  {"messages": [question]}
)

pprint(response['messages'])