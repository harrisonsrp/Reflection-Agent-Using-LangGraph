from Agents.ReflectionAgent.graph.chains.feedback import feedback_chain
from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage


def feedback_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = feedback_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]
