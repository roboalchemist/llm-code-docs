#    decide if it needs to call the writeEssay tool
async def chat_node(state: AgentState, config: RunnableConfig) -> Command[Literal["user_feedback_node", "__end__"]]:
    # 2.1 Define the model and bind CopilotKit's actions as tools
    model = ChatOpenAI(model="gpt-4o")
    model_with_tools = model.bind_tools([*state.get("copilotkit", {}).get("actions", [])])

    # 2.2 Define the system message
    system_message = SystemMessage(
        content="You write essays. Use your tools to write an essay, don't just write it in plain text."
    )

    # 2.3 Run the model to generate a response
    response = await model_with_tools.ainvoke([\
        system_message,\
        *state["messages"],\
    ], config)


    # 2.4 Check for the writeEssay tool call and, if found, go  to the
    #     user_feedback_node to handle the user's response
    if isinstance(response, AIMessage) and response.tool_calls:
        if response.tool_calls[0].get("name") == "writeEssay":
            return Command(goto="interrupt_node", update={"messages": response})

    # 2.5 If no tool call is found, end the agent
    return Command(goto=END, update={"messages": response})