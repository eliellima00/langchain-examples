from dotenv import load_dotenv
load_dotenv()

from langchain.tools import tool

# Defition 1
@tool
def square_root(x: float) -> float:
  """Calculate the square of a number"""
  return x ** 0.5

# Definition 2
# @tool("square_root")
# def tool1(x: float) -> float:
#     """Calculate the square root of a number"""
#     return x ** 0.5

# Definition 3
# @tool("square_root", description="Calculate the square root of a number")
# def tool1(x: float) -> float:
#     return x ** 0.5

print(square_root.invoke({"x": 20}))