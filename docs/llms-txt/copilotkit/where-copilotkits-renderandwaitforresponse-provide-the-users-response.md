#    where CopilotKit's renderAndWaitForResponse provide the user's response.
def user_feedback_node(state: AgentState, config: RunnableConfig) -> Command[Literal["chat_node"]]:

    # 3.1 Get the last message from the state, this will be
    #     what is returned by respond() in the frontend
    last_message = state["messages"][-1]

    # 3.2 If the user declined the essay, ask them how they'd like to improve it
    if last_message.content != "SEND":
        return Command(goto="chat_node", update={
            "messages": [SystemMessage(content="The user declined they essay, please ask them how they'd like to improve it")]
        })

    # 3.3 If the user approved the essay, ask them if they'd like anything else
    return Command(goto="chat_node", update={
        "messages": [SystemMessage(content="The user approved the essay, ask them if they'd like anything else")]
    })