from dotenv import load_dotenv
import os
load_dotenv()
from langgraph.graph import END, MessageGraph
from langchain_core.messages import BaseMessage
from Agents.ReflectionAgent.graph.nodes.feedback_node import feedback_node
from Agents.ReflectionAgent.graph.nodes.developer_node import developer_node
from Agents.ReflectionAgent.graph.consts import FEEDBACK, DEVELOPER
from typing import List, Sequence

WorkFlow = MessageGraph()

# Adding nodes
WorkFlow.add_node(FEEDBACK, feedback_node)
WorkFlow.add_node(DEVELOPER, developer_node)

# Telling langGraph that starting node should be generating node
WorkFlow.set_entry_point(DEVELOPER)

def should_continue(state: List[BaseMessage]):
    step_count = len(state)
    if step_count >= 6:
        return END
    return DEVELOPER

#### ADDING EDGES ###
WorkFlow.add_edge(DEVELOPER, FEEDBACK)
# Conditional Edge: this is and edge which help the LLM to reason if we should continue or not or which node it
# should go next now
WorkFlow.add_conditional_edges(FEEDBACK, should_continue)


#### COMPILE THE GRAPH ###
graph = WorkFlow.compile()

graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

