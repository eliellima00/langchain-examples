from dotenv import load_dotenv
from typing import Dict, Any
from langchain.tools import tool
from tavily import TavilyClient
from langchain.agents import create_agent

load_dotenv()

tavilyClient = TavilyClient()

@tool
def search_recipes_by_ingredients(query: str) -> Dict[str, Any]:
    """Searchs recipes by ingredients from WEB"""
    return tavilyClient.search(query)


system_prompt = """
You are a cuisine chef. Analyze if the image contains food ingredients. 
If not, respond: IMAGE INVALID.
If yes, use the search tool to find recipes based on those ingredients.
"""

app = create_agent(
    model='gpt-5-nano', 
    tools=[search_recipes_by_ingredients],
    system_prompt=system_prompt,
)