from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class CapitalInfo(BaseModel):
  name: str
  location: str
  vibe: str
  economy: str

system_prompt = """

You are a science fiction writer, create a space capital city at the users request.

Please keep to the below structure.

Name: The name of the capital city

Location: Where it is based

Vibe: 2-3 words to describe its vibe

Economy: Main industries

"""
question = HumanMessage(content="What's the capital of the moon?")

scifi_agent = create_agent(
  model='gpt-5-nano',
  system_prompt=system_prompt,
  response_format=CapitalInfo
)

response = scifi_agent.invoke(
  {"messages":[question]}
)

print(response["structured_response"])