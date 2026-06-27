from config.llm import llm
from tools.all_tools import tools

llm_with_tools = llm.bind_tools(tools)

def chat_node(state):

    messages = state["messages"][-20:]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [response]
    }

