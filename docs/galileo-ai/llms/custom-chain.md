# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/integrations/custom-chain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging Workflows

> No matter how you're orchestrating your workflows, we have an interface to help you upload them to Galileo.

To log your runs with Galileo, you'd start with the same typical flow of logging into Galileo:

```py  theme={null}
import promptquality as pq

pq.login()
```

Next you can construct your [EvaluateRun](https://promptquality.docs.rungalileo.io/#promptquality.EvaluateRun) object:

```py  theme={null}
from promptquality import EvaluateRun

metrics = [pq.Scorers.context_adherence_plus, pq.Scorers.prompt_injection]

evaluate_run = EvaluateRun(run_name="my_run", project_name="my_project", scorers=metrics)
```

Then you can generate your workflows.
A workflow starts with a user input, could contain multiple AI / tool / retriever nodes, and usually ends with an LLM node summarizing the entire turn to the user.
Datasets should also be constructed in such a way that a sample represents the entry to one workflow (i.e., one user input).
An evaluate run typically consists of multiple workflows, or multiple AI turns.
Here's an example of how you can log your workflows using your llm app:

```py  theme={null}
def my_llm_app(input, evaluate_run):
    context = " ... [text explaining hallucinations] ... "
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    wf = evaluate_run.add_workflow(input=input)
    # Get response from your llm.
    prompt = template.format(context=context, question=input)
    llm_response = llm.call(prompt) # Pseudo-code, replace with your LLM call.
    # Log llm step to Galileo
    wf.add_llm(input=prompt, output=llm_response, model=<model_name>)
    # Conclude the workflow and add the final output.
    wf.conclude(output=llm_response)
    return llm_response

# Your evaluation dataset.
eval_set = [
    "What are hallucinations?",
    "What are intrinsic hallucinations?",
    "What are extrinsic hallucinations?"
]
for input in eval_set:
    my_llm_app(input, evaluate_run)
```

Finally, log your Evaluate run to Galileo:

```py  theme={null}
evaluate_run.finish()
```

## Logging RAG Workflows

If you're looking to log RAG workflows it's easy to add a retriever step. Here's an example with RAG:

```py  theme={null}
def my_llm_app(input, evaluate_run):
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    wf = evaluate_run.add_workflow(input=input)
    # Fetch documents from your retriever
    documents = retriever.retrieve(input) # Pseudo-code, replace with your real retriever.
    # Log retriever step to Galileo
    wf.add_retriever(input=input, documents=documents)
    # Get response from your llm.
    prompt = template.format(context="\n".join(documents), question=input)
    llm_response = llm.call(prompt) # Pseudo-code, replace with your LLM call.
    # Log llm step to Galileo
    wf.add_llm(input=prompt, output=llm_response, model=<model_name>)
    # Conclude the workflow and add the final output.
    wf.conclude(output=llm_response)
    return llm_response

# Your evaluation dataset.
eval_set = [
    "What are hallucinations?",
    "What are intrinsic hallucinations?",
    "What are extrinsic hallucinations?"
]
context = "You're an AI assistant helping a user with hallucinations."
for input in eval_set:
    my_llm_app(input, evaluate_run)
```

## Logging Agent Workflows

We also support logging Agent workflows. As above, a workflow starts with a user message, contains various steps taken by the system and ends with a response to the user. \
When logging entire sessions, such as multi-turn conversations between a user and an agent, the session should be split into a sequence of Workflows, delimited by the user's messages.

Below is an example on how to log an agentic workflow (say in the middle of a multi-turn conversation) made of the following steps:

* the user query
* an LLM call with tools, and the LLM decides to call tools
* a tool execution
* an LLM call without tools, where the LLM responds back to the user.

```py  theme={null}
# Initiate the agentic workflow with the last user message as input
last_user_message = chat_history[-1].content
agent_wf = evaluate_run.add_agent_workflow(input=last_user_message)

# Call the LLM (which select tools)
# input = LLM input = chat history until now
# output = LLM output = LLM call to tools
llm_response = llm_call(chat_history, tools=tools)
agent_wf.add_llm(
    input=chat_history,
    output=llm_response.tool_call,
    tools=tools_dict
)
llm_message = llm_response_to_llm_message(llm_response)
chat_history.append(llm_message)

# Execute the tool call
# input = Tool input = arguments
# output = Tool output = function's return value
tool_response = execute_tool(llm_response.tool_call)
agent_wf.add_tool(
    input=llm_response.tool_call.arguments,
    output=tool_response,
    name=llm_response.tool_call.name
)
tool_message = tool_response_to_tool_message(tool_response)
chat_history.append(tool_message)

# Call the LLM to respond to the user
# input = LLM input = chat history until now
# output = LLM output = LLM response to the user
llm_response = llm_call(chat_history)
agent_wf.add_llm(
    input=chat_history,
    output=llm_response.content,
)
chat_history.append(llm_response)

# Conclude the agentic workflow with the last response
agent_wf.conclude(output=llm_response.content)
```

## Logging Retriever and LLM Metadata

If you want to log more complex inputs and outputs to your nodes, we provide support for that as well.
For retriever outputs we support the [Document](https://promptquality.docs.rungalileo.io/#promptquality.Document) object.

```py  theme={null}
wf = evaluate_run.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_retriever(
    input="Who's a good bot?",
    documents=[pq.Document(content="Research shows that I am a good bot.", metadata={"length": 35})],
    duration_ns=1000
)
```

For LLM inputs and outputs we support the [Message](https://promptquality.docs.rungalileo.io/#promptquality.Message) object.

```py  theme={null}
wf = evaluate_run.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_llm(
    input=pq.Message(content="Given this context: Research shows that I am a good bot. answer this: Who's a good bot?"),
    output=pq.Message(content="I am!", role=pq.MessageRole.assistant),
    model=pq.Models.chat_gpt,
    input_tokens=25,
    output_tokens=3,
    total_tokens=28,
    duration_ns=1000
)
```

Often times an llm interaction consists of multiple messages. You can log these as well.

```py  theme={null}
wf = evaluate_run.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_llm(
    input=[
        pq.Message(content="You're a good bot that answers questions.", role=pq.MessageRole.system),
        pq.Message(content="Given this context: Research shows that I am a good bot. answer this: Who's a good bot?"),
    ],
    output=pq.Message(content="I am!", role=pq.MessageRole.assistant),
    model=pq.Models.chat_gpt,
)
```

## Logging Nested Workflows

If you have more complex workflows that involve nesting workflows within workflows, we support that too.
Here's an example of how you can log nested workflow using conclude to step out of the nested workflow, back into the base workflow:

```py  theme={null}
wf = evaluate_run.add_workflow("input", "output", duration_ns=100)
# Add a workflow inside the base workflow.
nested_wf = wf.add_sub_workflow(input="inner input")
# Add an LLM step inside the nested workflow.
nested_wf.add_llm(input="prompt", output="response", model=pq.Models.chat_gpt, duration_ns=60)
# Conclude the nested workflow and step back into the base workflow.
nested_wf.conclude(output="inner output", duration_ns=60)
# Add another LLM step in the base workflow.
wf.add_llm("outer prompt", "outer response", "chatgpt", duration_ns=40)
```
