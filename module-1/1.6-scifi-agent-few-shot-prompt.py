from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

system_prompt = """

You are a science fiction writer, create a space capital city at the users request.

User: What is the capital of mars?
Scifi Writer: Marsialis

User: What is the capital of Venus?
Scifi Writer: Venusovia

"""

question = HumanMessage(content="What's the capital of the moon?")

scifi_agent = create_agent(
  model='gpt-5-nano',
  system_prompt=system_prompt
)

response = scifi_agent.invoke(
  {"messages":[question]}
)

print(response['messages'][1].content)