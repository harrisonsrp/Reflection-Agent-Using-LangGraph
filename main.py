from Agents.ReflectionAgent.graph.graph import graph
from langchain_core.messages import HumanMessage


inputs = HumanMessage(content="""Generate a website portfolio for me. I am an AI engineer. make the design minimal and creative with animations""")
response = graph.invoke(inputs)
print(response)
