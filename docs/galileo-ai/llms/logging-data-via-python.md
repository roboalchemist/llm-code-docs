# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/logging-data-via-python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging Data Via Python

> Learn how to manually log your data via our Python Logger

<Info>If you use Langchain in your production app, we recommend integrating via our [Langchain callback](/galileo/gen-ai-studio-products/galileo-observe/getting-started#integrating-with-langchain).</Info>

You can use our Python Logger to log your data to Galileo with the [ObserveWorkflows](https://observe.docs.rungalileo.io/#galileo_observe.ObserveWorkflows) module.

Here's an example of how to integrate the logger into your llm app:

First you can create your ObserveWorkflows object with your existing project.

```py  theme={null}
from galileo_observe import ObserveWorkflows

observe_logger = ObserveWorkflows(project_name="my_first_project")
```

Then you can use the workflows object to log your workflows.

```py  theme={null}
def my_llm_app(input, observe_logger):
    template = "You're a helpful AI assistant, answer the following question. Question: {question}"
    wf = observe_logger.add_workflow(input=input)
    # Get response from your llm.
    prompt = template.format(question=input)
    llm_response = llm.call(prompt) # Pseudo-code, replace with your LLM call.
    # Log llm step to Galileo
    wf.add_llm(input=prompt, output=llm_response, model=<model_name>)
    # Conclude the worfklow by adding the final output.
    wf.conclude(output=llm_response)
    # log the workflow to Galileo.
    observe_logger.upload_workflows()
    return llm_response
```

You can also do this with your RAG workflows:

```py  theme={null}
def my_llm_app(input, observe_logger):
    template = "Given the following context answer the question. \n Context: {context} \n Question: {question}"
    wf = observe_logger.add_workflow(input=input)
    # Fetch documents from your retriever
    documents = retriever.retrieve(input) # Pseudo-code, replace with your retriever call.
    # Log retriever step to Galileo
    wf.add_retriever(input=input, documents=documents)
    # Get response from your llm.
    prompt = template.format(context="\n".join(documents), question=input)
    llm_response = llm.call(prompt) # Pseudo-code, replace with your LLM call.
    # Log llm step to Galileo
    wf.add_llm(input=prompt, output=llm_response, model=<model_name>)
    # Conclude the worfklow by adding the final output.
    wf.conclude(output=llm_response)
    # log the workflow to Galileo.
    observe_logger.upload_workflows()
    return llm_response
```

## Logging Agent Workflows

We also support logging Agent workflows. Here's an example of how you can log an Agent workflow:

```py  theme={null}
agent_wf = evaluate_run.add_agent_workflow(input=<input>)
# Log a Tool-Calling LLM step
agent_wf.add_llm(input=<prompt>, output=<output>, tools=<tools_json>, model=<model_name>)
# Log a Tool Execution
agent_wf.add_tool(input=<tool query>, output=<tool response>, duration_ns=50)
agent_wf.conclude(output=<output>)
```

## Logging Retriever and LLM Metadata

If you want to log more complex inputs and outputs to your nodes, we provide support for that as well.
For retriever outputs we support the [Document](https://promptquality.docs.rungalileo.io/#promptquality.Document) object.

```py  theme={null}
from galileo_observe import Document

wf = observe_logger.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_retriever(
    input="Who's a good bot?",
    documents=[Document(content="Research shows that I am a good bot.", metadata={"length": 35})],
    duration_ns=1000
)
```

For LLM inputs and outputs we support the [Message](https://promptquality.docs.rungalileo.io/#promptquality.Message) object.

```py  theme={null}
from galileo_observe import Message, MessageRole
wf = observe_logger.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_llm(
    input=Message(content="Given this context: Research shows that I am a good bot. answer this: Who's a good bot?"),
    output=Message(content="I am!", role=MessageRole.assistant),
    model="GPT-4o",
    input_tokens=25,
    output_tokens=3,
    total_tokens=28,
    duration_ns=1000
)
```

Often times an llm interaction consists of multiple messages. You can log these as well.

```py  theme={null}
wf = observe_logger.add_workflow(input="Who's a good bot?", output="I am!", duration_ns=2000)
wf.add_llm(
    input=[
        Message(content="You're a good bot that answers questions.", role=MessageRole.system),
        Message(content="Given this context: Research shows that I am a good bot. answer this: Who's a good bot?"),
    ],
    output=Message(content="I am!", role=MessageRole.assistant),
    model="GPT-4o",
)
```

## Logging Nested Workflows

If you have more complex workflows that involve nesting workflows within workflows, we support that too.
Here's an example of how you can log nested workflow using conclude to step out of the nested workflow, back into the base workflow:

```py  theme={null}
wf = observe_logger.add_workflow("input", "output", duration_ns=100)
# Add a workflow inside the base workflow.
nested_wf = wf.add_sub_workflow(input="inner input")
# Add an LLM step inside the nested workflow.
nested_wf.add_llm(input="prompt", output="response", model="GPT-4o", duration_ns=60)
# Conclude the nested workflow and step back into the base workflow.
nested_wf.conclude(output="inner output", duration_ns=60)
# Add another LLM step in the base workflow.
wf.add_llm("outer prompt", "outer response", "chatgpt", duration_ns=40)
```
