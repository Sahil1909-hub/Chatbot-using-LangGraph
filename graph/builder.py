from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from .state import ChatState
from .nodes import chat_node

from tools.all_tools import tools
from config.database import checkpointer

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_node(
    "tools",
    ToolNode(tools)
)

graph.add_edge(
    START,
    "chat_node"
)

graph.add_conditional_edges(
    "chat_node",
    tools_condition
)

graph.add_edge(
    "tools",
    "chat_node"
)

chatbot = graph.compile(
    checkpointer=checkpointer
)