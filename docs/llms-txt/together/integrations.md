# Source: https://docs.together.ai/docs/integrations.md

> Use Together AI models through partner integrations.

# Integrations

Together AI seamlessly integrates with a wide range of tools and frameworks, making it easy to incorporate powerful open-source models into your existing workflows. Whether you're building AI agents, developing applications, managing vector databases, or monitoring LLM performance, our integrations help you get started quickly.

Our integrations span several categories:

* **Agent Frameworks**: Build sophisticated AI agents with LangGraph, CrewAI, PydanticAI, AutoGen, DSPy, and more
* **Development Tools**: Integrate with popular SDKs like Vercel AI SDK, LangChain, and LlamaIndex
* **Data & Vector Stores**: Connect to Pinecone, MongoDB, and Pixeltable for RAG applications
* **Observability**: Monitor and track your LLM usage with Helicone and Composio

## HuggingFace

*You can use Together AI models with Hugging Face Inference.*

Install the `huggingface_hub` library:

<CodeGroup>
  ```sh Shell theme={null}
  pip install huggingface_hub>=0.29.0
  ```

  ```sh Shell theme={null}
  npm install @huggingface/inference
  ```
</CodeGroup>

Chat Completion with Hugging Face Hub library

<CodeGroup>
  ```python Python theme={null}
  from huggingface_hub import InferenceClient

  ## Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)
  )

  ## Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  ## Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  ## Print the response

  print(completion.choices[0].message)
  ```

  ```typescript TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const chatCompletion = await client.chatCompletion({
      model: "deepseek-ai/DeepSeek-R1",  // Replace with your desired model
      messages: [
          {
              role: "user",
              content: "What is the capital of France?"
          }
      ],
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });

  // Log the response
  console.log(chatCompletion.choices[0].message);
  ```
</CodeGroup>

Learn more in our [Together AI - HuggingFace Guide](https://docs.together.ai/docs/quickstart-using-hugging-face-inference).

## Vercel AI SDK

*The Vercel AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.*

Install both the Vercel AI SDK and Together.ai's Vercel package.

```shell Shell theme={null}
npm i ai @ai-sdk/togetherai
```

Import the Together.ai provider and call the generateText function with Kimi K2 to generate some text.

```typescript TypeScript theme={null}
import { togetherai } from "@ai-sdk/togetherai";
import { generateText } from "ai";

async function main() {
  const { text } = await generateText({
    model: togetherai("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

Learn more in our [Together AI - Vercel AI SDK Guide](https://docs.together.ai/docs/using-together-with-vercels-ai-sdk).

## Langchain

*LangChain is a framework for developing context-aware, reasoning applications powered by language models.*

To install the LangChain x Together library, run:

```text Shell theme={null}
pip install --upgrade langchain-together
```

Here's sample code to get you started with Langchain + Together AI:

```python Python theme={null}
from langchain_together import ChatTogether

chat = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf")

for m in chat.stream("Tell me fun things to do in NYC"):
    print(m.content, end="", flush=True)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-langchain?_gl=1*exkmyi*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LangChain.

* [LangChain TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together)
* [LangChain Together](https://python.langchain.com/docs/integrations/llms/together)

## LlamaIndex

*LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs).*

Install `llama-index`

```shell Shell theme={null}
pip install llama-index
```

Here's sample code to get you started with Llama Index + Together AI:

```python Python theme={null}
from llama_index.llms import OpenAILike

llm = OpenAILike(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    api_base="https://api.together.xyz/v1",
    api_key="TOGETHER_API_KEY",
    is_chat_model=True,
    is_function_calling_model=True,
    temperature=0.1,
)

response = llm.complete(
    "Write up to 500 words essay explaining Large Language Models"
)

print(response)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-llamaindex?_gl=1*1t16mh2*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LlamaIndex.

* [LlamaIndex TogetherEmbeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together.html)
* [LlamaIndex TogetherLLM](https://docs.llamaindex.ai/en/stable/examples/llm/together.html)

## CrewAI

*CrewAI is an open source framework for orchestrating AI agent systems.*

Install `crewai`

```shell Shell theme={null}
pip install crewai
export TOGETHER_API_KEY=***
```

Build a multi-agent workflow:

```python Python theme={null}
import os
from crewai import LLM, Task, Agent, Crew

llm = LLM(
    model="together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)

research_agent = Agent(
    llm=llm,
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    verbose=True,  # Enable logging for debugging
)

research_task = Task(
    description="Conduct a thorough research about AI Agents.",
    expected_output="A list with 10 bullet points of the most relevant information about AI Agents",
    agent=research_agent,
)

## Execute the crew
crew = Crew(agents=[research_agent], tasks=[research_task], verbose=True)

result = crew.kickoff()

## Accessing the task output
task_output = research_task.output

print(task_output)
```

Learn more in our [CrewAI guide](https://docs.together.ai/docs/crewai).

## LangGraph

*LangGraph is an OSS library for building stateful, multi-actor applications with LLMs*

Install `langgraph`

```shell Shell theme={null}
pip install -U langgraph langchain-together
export TOGETHER_API_KEY=***
```

Build a tool-using agent:

```python Python theme={null}
import os
from langchain_together import ChatTogether

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_key=os.getenv("TOGETHER_API_KEY"),
)


## Define a tool
def multiply(a: int, b: int) -> int:
    return a * b


## Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

## Invoke the LLM with input that triggers the tool call
msg = llm_with_tools.invoke("What is 2 times 3?")

## Get the tool call
msg.tool_calls
```

Learn more in our [LangGraph Guide](https://docs.together.ai/docs/langgraph) including:

* [Agentic RAG Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/Agentic_RAG_LangGraph.ipynb)
* [Planning Agent Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/LangGraph_Planning_Agent.ipynb)

## PydanticAI

*PydanticAI is an agent framework created by the Pydantic team to simplify building agent workflows.*

Install `pydantic-ai`

```shell Shell theme={null}
pip install pydantic-ai
export TOGETHER_API_KEY=***
```

Build PydanticAI agents using Together AI models

```python Python theme={null}
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

## Connect PydanticAI to LLMs on Together
model = OpenAIModel(
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    provider=OpenAIProvider(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ.get("TOGETHER_API_KEY"),
    ),
)

## Setup the agent
agent = Agent(
    model,
    system_prompt="Be concise, reply with one sentence.",
)

result = agent.run_sync('Where does "hello world" come from?')
print(result.data)
```

Learn more in our [PydanticAI Guide](https://docs.together.ai/docs/pydanticai) and explore our [PydanticAI Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/PydanticAI/PydanticAI_Agents.ipynb).

## Arcade.dev

*Arcade is a platform that lets AI securely use tools like email, files, and APIs to take real action—not just chat. Build powerful assistants in minutes with ready-to-use integrations or a custom SDK.*

Our guide demonstrates how to integrate Together AI's language models with Arcade's tools to create an AI agent that can send emails.

Prerequisites:

* Together AI API key - see here [https://api.together.ai/](https://api.together.ai/)
* Arcade API key - see here [https://arcade.dev/](https://arcade.dev/)
* Gmail account to connect via OAuth

```shell Shell theme={null}
## install the required packages
!pip install -qU together arcadepy
```

Gmail Configuration:

<CodeGroup>
  ```shell Shell theme={null}
  import os
  from arcadepy import Arcade
  from together import Together

  ## Set environment variables
  os.environ["TOGETHER_API_KEY"] = "XXXXXXXXXXXXX"  # Replace with your actual Together API key
  os.environ["ARCADE_API_KEY"] = "arc_XXXXXXXXXXX"    # Replace with your actual Arcade API key

  ## Initialize clients
  together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
  arcade_client = Arcade()  # Automatically finds the ARCADE_API_KEY env variable

  ## Set up user ID (your email)
  USER_ID = "your_email@example.com"  # Change this to your email

  ## Authorize Gmail access
  auth_response = arcade_client.tools.authorize(
      tool_name="Google.SendEmail",
      user_id=USER_ID,
  )

  if auth_response.status != "completed":
      print(f"Click this link to authorize: {auth_response.url}")
      # Wait for the authorization to complete
      arcade_client.auth.wait_for_completion(auth_response)

  print("Authorization completed!")
  ```
</CodeGroup>

Learn more in our [Arcade guide](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Arcade.dev/Agents_Arcade.ipynb) notebook.

## DSPy

*DSPy is a framework that enables you to build modular AI systems with code instead of hand-crafted prompting*

Install `dspy`

```shell Shell theme={null}
pip install -U dspy
export TOGETHER_API_KEY=***
```

Build a question answering agent

```python Python theme={null}
import dspy

# Configure dspy with a LLM from Together AI
lm = dspy.LM(
    "together_ai/togethercomputer/llama-2-70b-chat",
    api_key=os.environ.get("TOGETHER_API_KEY"),
    api_base="https://api.together.xyz/v1",
)

# Configure dspy to use the LLM
dspy.configure(lm=lm)


## Gives the agent access to a python interpreter
def evaluate_math(expression: str):
    return dspy.PythonInterpreter({}).execute(expression)


## Gives the agent access to a wikipedia search tool
def search_wikipedia(query: str):

    results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(
        query, k=3
    )
    return [x["text"] for x in results]


## setup ReAct module with question and math answer signature
react = dspy.ReAct(
    "question -> answer: float",
    tools=[evaluate_math, search_wikipedia],
)

pred = react(
    question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
)

print(pred.answer)
```

Learn more in our [DSPy Guide](https://docs.together.ai/docs/dspy) and explore our [DSPy Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DSPy/DSPy_Agents.ipynb).

## AutoGen(AG2)

*AG2 (formerly AutoGen) is an open-source framework for building and orchestrating AI agents.*

Install `autogen`

```shell Shell theme={null}
pip install autogen
export TOGETHER_API_KEY=***
```

Build a coding agent

```python Python theme={null}
import os
from pathlib import Path
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

config_list = [
    {
        # Let's choose the Mixtral 8x7B model
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        # Provide your Together.AI API key here or put it into the TOGETHER_API_KEY environment variable.
        "api_key": os.environ.get("TOGETHER_API_KEY"),
        # We specify the API Type as 'together' so it uses the Together.AI client class
        "api_type": "together",
        "stream": False,
    }
]

## Setting up the code executor
workdir = Path("coding")
workdir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=workdir)

## Setting up the agents

## The UserProxyAgent will execute the code that the AssistantAgent provides
user_proxy_agent = UserProxyAgent(
    name="User",
    code_execution_config={"executor": code_executor},
    is_termination_msg=lambda msg: "FINISH" in msg.get("content"),
)

system_message = """You are a helpful AI assistant who writes code and the user executes it.
Solve tasks using your coding and language skills.
"""

## The AssistantAgent, using Together.AI's Code Llama model, will take the coding request and return code
assistant_agent = AssistantAgent(
    name="Together Assistant",
    system_message=system_message,
    llm_config={"config_list": config_list},
)

## Start the chat, with the UserProxyAgent asking the AssistantAgent the message
chat_result = user_proxy_agent.initiate_chat(
    assistant_agent,
    message="Provide code to count the number of prime numbers from 1 to 10000.",
)
```

Learn more in our [Autogen Guide](https://docs.together.ai/docs/autogen).

## Agno

*Agno is an open-source library for creating multimodal agents.*

Install `agno`

```shell Shell theme={null}
pip install -U agno duckduckgo-search
```

Build a search and answer agent

```python Python theme={null}
from agno.agent import Agent
from agno.models.together import Together
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)
agent.print_response("What's happening in New York?", stream=True)
```

Learn more in our [Agno Guide](https://docs.together.ai/docs/agno) including code a notebook.

## MongoDB

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-mongodb?_gl=1*13iu8zj*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and MongoDB.

## Pinecone

*Pinecone is a vector database that helps companies build RAG applications.*

Here's some sample code to get you started with Pinecone + Together AI:

```python Python theme={null}
from pinecone import Pinecone, ServerlessSpec
from together import Together

pc = Pinecone(api_key="PINECONE_API_KEY", source_tag="TOGETHER_AI")
client = Together()

## Create an index in pinecone
index = pc.create_index(
    name="serverless-index",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-west-2"),
)

## Create an embedding on Together AI
textToEmbed = (
    "Our solar system orbits the Milky Way galaxy at about 515,000 mph"
)
embeddings = client.embeddings.create(
    model="togethercomputer/m2-bert-80M-8k-retrieval", input=textToEmbed
)

## Use index.upsert() to insert embeddings and index.query() to query for similar vectors
```

## Helicone

*Helicone is an open source LLM observability platform.*

Here's some sample code to get started with using Helicone + Together AI:

```python Python theme={null}
import os
from together import Together

client = Together(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://together.hconeai.com/v1",
    supplied_headers={
        "Helicone-Auth": f"Bearer {os.environ.get('HELICONE_API_KEY')}",
    },
)

stream = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {
            "role": "user",
            "content": "What are some fun things to do in New York?",
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

## Composio

*Composio allows developers to integrate external tools and services into their AI applications.*

Install `composio-togetherai`

```shell Shell theme={null}
pip install together composio-togetherai
export TOGETHER_API_KEY=***
export COMPOSIO_API_KEY=***
```

Get Together AI models to use integrated tools

```python Python theme={null}
from composio_togetherai import ComposioToolSet, App
from together import Together

client = Together()
toolset = ComposioToolSet()

request = toolset.initiate_connection(app=App.GITHUB)
print(f"Open this URL to authenticate: {request.redirectUrl}")

tools = toolset.get_tools(apps=[App.GITHUB])

response = client.chat.completions.create(
    tools=tools,
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": "Star the repo 'togethercomputer/together-cookbook'",
        }
    ],
)

res = toolset.handle_tool_calls(response)
print(res)
```

Learn more in our [Composio Guide](https://docs.together.ai/docs/composio) and explore our [Composio cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Composio/Agents_Composio.ipynb).

## Pixeltable

See [this tutorial blog](https://docs.together.ai/docs/embeddings-rag#:~:text=Using%20Pixeltable,Together%20and%20Pixeltable.) for the RAG implementation details using Together and Pixeltable.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt