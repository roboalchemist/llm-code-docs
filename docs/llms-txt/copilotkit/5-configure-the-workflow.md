# 5. Configure the workflow
workflow = StateGraph(AgentState)
workflow.add_node("chat_node", chat_node)
workflow.add_node("interrupt_node", interrupt_node)
workflow.add_node("user_feedback_node", user_feedback_node)
workflow.add_edge("interrupt_node", "user_feedback_node")
workflow.set_entry_point("chat_node")