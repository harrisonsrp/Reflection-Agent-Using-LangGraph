from dotenv import load_dotenv
import os
load_dotenv()
from langgraph.graph import END, MessageGraph
from langchain_core.messages import BaseMessage, HumanMessage
from nodes.designer_node import designer_node
from nodes.developer_node import developer_node
from consts import DESIGNER, DEVELOPER
from typing import List, Sequence

WorkFlow = MessageGraph()

# Adding nodes
WorkFlow.add_node(DESIGNER, designer_node)
WorkFlow.add_node(DEVELOPER, developer_node)

# Telling langGraph that starting node should be generating node
WorkFlow.set_entry_point(DESIGNER)

def should_continue(state: List[BaseMessage]):
    step_count = len(state)
    if step_count >= 6:
        return END
    return DESIGNER

#### ADDING EDGES ###
WorkFlow.add_edge(DESIGNER, DEVELOPER)
# Conditional Edge: this is and edge which help the LLM to reason if we should continue or not or which node it
# should go next now
WorkFlow.add_conditional_edges(DEVELOPER, should_continue)


#### COMPILE THE GRAPH ###
graph = WorkFlow.compile()

graph.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__ == "__main__":
    inputs = HumanMessage(content="""I want a portfolio website. I am an AI engineer""")
    response = graph.invoke(inputs)
    print(response)