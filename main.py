from Agents.ReflectionAgent.graph.graph import graph
from langchain_core.messages import HumanMessage


inputs = HumanMessage(content="""I want a portfolio website. I am an AI engineer""")
response = graph.invoke(inputs)
print(response)