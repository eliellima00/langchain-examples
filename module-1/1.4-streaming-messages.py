from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
from langchain.messages import  HumanMessage

agent = create_agent(model='gpt-5-nano')

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="Tell me all about Luna City, the capital of the Moon")]},
    stream_mode="messages"
):
    # token is a message chunk with token content
    # metadata contains which node produced the token
    
    if token.content:  # Check if there's actual content
        print(token.content, end="", flush=True)  # Print token

