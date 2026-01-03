# Source: https://docs.lunary.ai/docs/integrations/langchain.md

# LangChain Integration

We provide callback handler that can be used to track LangChain calls, chains and agents.

## Setup

First, install the relevant `lunary` and `langchain` packages:

<Tabs>
  <Tab title="Python">
    ```bash  theme={null}
    pip install lunary
    pip install langchain
    ```
  </Tab>

  <Tab title="Javascript">
    ```bash  theme={null}
    npm install lunary
    npm install langchain
    ```
  </Tab>
</Tabs>

Then, set the `LUNARY_PUBLIC_KEY` environment variable to your app tracking id.

```bash  theme={null}
LUNARY_PUBLIC_KEY="0x0"
```

If you'd prefer not to set an environment variable, you can pass the key directly when initializing the callback handler:

<Tabs>
  <Tab title="Python">
    ```py  theme={null}
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler(app_id="0x0")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { LunaryHandler } from "lunary/langchain"

    const handler = new LunaryHandler({
      appId: "0x0",
    })
    ```
  </Tab>
</Tabs>

## Usage with LLM calls

You can use the callback handler with any LLM or Chat class from LangChain.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain_openai import ChatOpenAI
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
    )
    chat.invoke("Say test")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { LunaryHandler } from "lunary/langchain"

    const model = new ChatOpenAI({
      callbacks: [new LunaryHandler()],
    })
    ```
  </Tab>
</Tabs>

## Usage with chains (LCEL)

You can also use the callback handler with LCEL, LangChain Expression Language.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import RunnablePassthrough, RunnableConfig
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    import lunary

    # Initialize the Lunary handler
    handler = lunary.LunaryCallbackHandler()
    config = RunnableConfig({"callbacks": [handler]})

    prompt = ChatPromptTemplate.from_template(
      "Tell me a short joke about {topic}"
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-4")
    chain = (
      {"topic": RunnablePassthrough()} 
      | prompt
      | model
      | output_parser
    )

    chain.invoke("ice cream", config=config) # You need to pass the config each time you call `.invoke()`
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { ChatOpenAI } from "@langchain/openai";
    import { ChatPromptTemplate } from "@langchain/core/prompts";
    import { StringOutputParser } from "@langchain/core/output_parsers";
    import { LunaryHandler } from "lunary/langchain";

    const handler = new LunaryHandler();

    const prompt = ChatPromptTemplate.fromMessages([
      ["human", "Tell me a short joke about {topic}"],
    ]);
    const model = new ChatOpenAI({});
    const outputParser = new StringOutputParser();

    const chain = prompt.pipe(model).pipe(outputParser);

    const response = await chain.invoke({
      topic: "ice cream",
    }, {
      callbacks: [handler]
    })
    console.log(response);
    ```
  </Tab>
</Tabs>

## Usage with agents

The callback handler works seamlessly with LangChain agents and chains.

For agents, it is recommended to pass a name in the metadatas to track them in the dashboard.

<Alert title="Note">
  When tracking agents, make sure to add the handler to the agent's `run`
  method, otherwise the LLM calls and tools will not be automatically tracked.
</Alert>

Example:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.agents import AgentExecutor, create_openai_tools_agent
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables import RunnableConfig
    from langchain_openai import ChatOpenAI

    # Initialize the Lunary handler
    from lunary import LunaryCallbackHandler

    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant"),
      MessagesPlaceholder("chat_history", optional=True),
      ("human", "{input}"),
      MessagesPlaceholder("agent_scratchpad"),
    ])

    tools = [TavilySearchResults(max_results=1)]

    # Initialize the Lunary handler
    handler = LunaryCallbackHandler()
    config = RunnableConfig({"callbacks": [handler]})

    llm = ChatOpenAI(model="gpt-4")
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)

    agent_executor.invoke({"input": "what is LangChain?"}, config)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { initializeAgentExecutorWithOptions } from "langchain/agents"
    import { ChatOpenAI } from "langchain/chat_models/openai"
    import { Calculator } from "langchain/tools/calculator"
    import { LunaryHandler } from "lunary/langchain"

    const tools = [new Calculator()]
    const chat = new ChatOpenAI()

    const executor = await initializeAgentExecutorWithOptions(tools, chat, {
      agentType: "openai-functions",
    })

    const result = await executor.run(
      "What is the approximate result of 78 to the power of 5?",
      {
        callbacks: [new LunaryHandler()], // Add the handler to the agent
        metadata: { agentName: "SuperCalculator" }, // Identify the agent in the Lunary dashboard
      }
    )
    ```
  </Tab>
</Tabs>

## Usage with custom agents

If you're partially using LangChain, you can use the callback handler combined with the `lunary` module to track custom agents:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.schema.messages import HumanMessage, SystemMessage
    from langchain_openai import ChatOpenAI
    import lunary

    handler = lunary.LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
    )

    @lunary.agent()
    def TranslatorAgent(query):
      messages = [ 
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content="What is the purpose of model regularization?"),
      ]

      return chat.invoke(messages)

    res = TranslatorAgent("Good morning")
    ```
  </Tab>

  <Tab title="Javascript">
    ```js  theme={null}
    import { ChatOpenAI } from "langchain/chat_models/openai"
    import { HumanMessage, SystemMessage } from "langchain/schema"

    import { LunaryHandler } from "lunary/langchain"
    import lunary from "lunary"

    const chat = new ChatOpenAI({
      callbacks: [new LunaryHandler()], // <- Add the Lunary Callback Handler here
    })

    async function TranslatorAgent(query) {
      const res = await chat.call([
        new SystemMessage(
          "You are a translator agent that hides jokes in each translation."
        ),
        new HumanMessage(
          `Translate this sentence from English to French: ${query}`
        ),
      ])

      return res.content
    }

    // By wrapping the agent with wrapAgent, we automatically track all input, outputs and errors
    // And tools and logs will be tied to the correct agent
    const translate = lunary.wrapAgent(TranslatorAgent)

    const res = await translate("Good morning")
    ```
  </Tab>
</Tabs>

## Usage with LangServe

You can use the callback handler to track all calls to your LangServe server.

### Server

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from fastapi import FastAPI
    from langchain_openai import ChatOpenAI
    from langchain.schema.runnable import (
        ConfigurableField,
    )
    from langserve import add_routes
    from lunary import LunaryCallbackHandler

    handler = LunaryCallbackHandler()

    app = FastAPI(
        title="LangChain Server",
        version="1.0",
        description="Spin up a simple api server using Langchain's Runnable interfaces",
    )

    model = ChatOpenAI(callbacks=[handler]).configurable_fields(
        metadata=ConfigurableField(
            id="metadata",
            name="Metadata",
            description=("Custom metadata"),
        ),
    )

    add_routes(app, model, path="/openai", config_keys=["metadata"])

    if __name__ == "__main__":
        import uvicorn

        uvicorn.run(app, host="localhost", port=8000)

    ```
  </Tab>
</Tabs>

### Client

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from langchain.schema import SystemMessage, HumanMessage
    from langserve import RemoteRunnable

    openai = RemoteRunnable("http://localhost:8000/openai/")

    prompt = [
      SystemMessage(content="Act like either a cat or a parrot."),
      HumanMessage(content="Hello!"),
    ]

    res = openai.invoke("Hello", config={"metadata": {
                        "user_id": "123", "tags": ["user1"]}})
    print(res)
    ```
  </Tab>
</Tabs>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt