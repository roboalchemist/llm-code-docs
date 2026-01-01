# Source: https://braintrust.dev/docs/integrations/sdk-integrations/langgraph.md

# LangGraph

[LangGraph](https://langchain-ai.github.io/langgraph/) is a library for building stateful, multi-actor applications with LLMs. Braintrust traces LangGraph applications using LangChain callback handlers to capture graph execution, node transitions, and LLM interactions.

## Setup

Install LangGraph alongside the Braintrust LangChain integration:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @braintrust/langchain-js @langchain/core @langchain/langgraph @langchain/openai
  # npm
  npm install braintrust @braintrust/langchain-js @langchain/core @langchain/langgraph @langchain/openai
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust braintrust-langchain langchain-core langgraph langchain-openai
  ```
</CodeGroup>

## Trace with LangGraph

Configure a global LangChain callback handler to automatically trace all graph operations:

<CodeGroup dropdown>
  ```typescript title="trace-langgraph.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import {
    BraintrustCallbackHandler,
    setGlobalHandler,
  } from "@braintrust/langchain-js";
  import { END, START, StateGraph, StateGraphArgs } from "@langchain/langgraph";
  import { ChatOpenAI } from "@langchain/openai";
  import { initLogger } from "braintrust";

  const logger = initLogger({
    projectName: "My Project",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const handler = new BraintrustCallbackHandler({ logger });
  setGlobalHandler(handler);

  // Define the state structure for the graph
  type HelloWorldGraphState = Record<string, any>;

  const graphStateChannels: StateGraphArgs<HelloWorldGraphState>["channels"] = {};

  const model = new ChatOpenAI({
    model: "gpt-4o-mini",
  });

  async function sayHello(state: HelloWorldGraphState) {
    const res = await model.invoke("Say hello");
    return { message: res.content };
  }

  function sayBye(state: HelloWorldGraphState) {
    console.log(`From the 'sayBye' node: Bye world!`);
    return {};
  }

  async function main() {
    const graphBuilder = new StateGraph({ channels: graphStateChannels })
      .addNode("sayHello", sayHello)
      .addNode("sayBye", sayBye)
      .addEdge(START, "sayHello")
      .addEdge("sayHello", "sayBye")
      .addEdge("sayBye", END);

    const helloWorldGraph = graphBuilder.compile();

    // Execute the graph - all operations will be logged to Braintrust
    await helloWorldGraph.invoke({});
  }

  main();
  ```

  ```python title="trace-langgraph.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import asyncio
  import os
  from typing import Dict

  from braintrust import init_logger
  from braintrust_langchain import BraintrustCallbackHandler, set_global_handler
  from langchain_openai import ChatOpenAI
  from langgraph.graph import END, START, StateGraph

  async def main():
      init_logger(project="My Project", api_key=os.environ.get("BRAINTRUST_API_KEY"))

      handler = BraintrustCallbackHandler()
      set_global_handler(handler)

      # Initialize your LangChain components
      model = ChatOpenAI(model="gpt-4o-mini")

      def say_hello(state: Dict[str, str]):
          response = model.invoke("Say hello")
          return response.content

      def say_bye(state: Dict[str, str]):
          print("From the 'sayBye' node: Bye world!")
          return "Bye"

      # Create the state graph
      workflow = (
          StateGraph(state_schema=Dict[str, str])
          .add_node("sayHello", say_hello)
          .add_node("sayBye", say_bye)
          .add_edge(START, "sayHello")
          .add_edge("sayHello", "sayBye")
          .add_edge("sayBye", END)
      )

      graph = workflow.compile()

      # Execute the graph - all operations will be logged to Braintrust
      await graph.ainvoke({})

  if __name__ == "__main__":
      asyncio.run(main())
  ```
</CodeGroup>

<img src="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=8cb010ea0d1f2d86e566f0d95c88ea97" alt="LangGraph trace visualization in Braintrust showing the execution flow of nodes and their relationships" data-og-width="1053" width="1053" data-og-height="743" height="743" data-path="images/integrations/langgraph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=280&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=5f4b582b3fbab0fe31f1e1c2c183bdc9 280w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=560&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=af71fb6737bb5b68c91966058f2d45eb 560w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=840&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=32d9638fe98638febd452d01eb7e62c3 840w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=1100&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=9fb2376da971e3f4b20268d31dc6b8de 1100w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=1650&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=e8f1a8f14481b02f217c7314024b2b61 1650w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/langgraph.png?w=2500&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=3e465a0eca5120611ed44b50bf5c0f30 2500w" />

## Resources

* [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
* [LangChain integration](/integrations/sdk-integrations/langchain)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt