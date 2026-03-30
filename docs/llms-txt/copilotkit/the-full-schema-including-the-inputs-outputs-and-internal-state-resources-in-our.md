# The full schema, including the inputs, outputs and internal state ("resources" in our case)
class OverallState(InputState, OutputState):
  resources: List[str]

async def answer_node(state: OverallState, config: RunnableConfig):
  """
  Standard chat node, meant to answer general questions.
  """

  model = ChatOpenAI()

  # add the input question in the system prompt so it's passed to the LLM
  system_message = SystemMessage(
    content=f"You are a helpful assistant. Answer the question: {state.get('question')}"
  )

  response = await model.ainvoke([\
    system_message,\
    *state["messages"],\
  ], config)

  # ...add the rest of the agent implementation

  # extract the answer, which will be assigned to the state soon
  answer = response.content

  return {
     "messages": response,
      # include the answer in the returned state
     "answer": answer
  }