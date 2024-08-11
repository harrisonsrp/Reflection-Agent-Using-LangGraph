from Agents.ReflectionAgent.graph.chains.developer import developer_chain
from typing import List, Sequence
from langchain_core.messages import BaseMessage


def developer_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    return developer_chain.invoke({"messages": messages})
