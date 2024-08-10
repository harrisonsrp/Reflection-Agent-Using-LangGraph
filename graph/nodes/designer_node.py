from Agents.ReflectionAgent.graph.chains.designer import designer_chain
from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage


def designer_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    return designer_chain.invoke({"messages": messages})
