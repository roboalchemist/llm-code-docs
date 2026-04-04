# Source: https://braintrust.dev/docs/integrations/sdk-integrations/langchain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain

[LangChain](https://www.langchain.com/) is a framework for developing applications powered by language models. Braintrust integrates with LangChain using callback handlers to automatically trace chains, agents, and LLM calls.

## Setup

Install the Braintrust LangChain integration alongside your LangChain packages:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @braintrust/langchain-js @langchain/core @langchain/openai
  # npm
  npm install braintrust @braintrust/langchain-js @langchain/core @langchain/openai
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust braintrust-langchain langchain-core langchain-openai
  ```
</CodeGroup>

## Trace with LangChain

Braintrust provides callback handlers that automatically capture LangChain operations including chains, agents, retrievers, and individual LLM calls.

To trace your LangChain application, configure the `BraintrustCallbackHandler`:

<CodeGroup dropdown>
  ```typescript title="trace-langchain.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { BraintrustCallbackHandler } from "@braintrust/langchain-js";
  import { ChatOpenAI } from "@langchain/openai";
  import { initLogger } from "braintrust";

  initLogger({
    projectName: "My Project",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const handler = new BraintrustCallbackHandler();

  async function main() {
    const model = new ChatOpenAI({ modelName: "gpt-4o-mini" });

    await model.invoke("What is the capital of France?", {
      callbacks: [handler],
    });
  }

  main();
  ```

  ```python title="trace-langchain.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import asyncio
  import os

  from braintrust import init_logger
  from braintrust_langchain import BraintrustCallbackHandler, set_global_handler
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_openai import ChatOpenAI

  async def main():
      init_logger(project="My Project", api_key=os.environ.get("BRAINTRUST_API_KEY"))

      handler = BraintrustCallbackHandler()
      set_global_handler(handler)

      # Initialize your LangChain components
      prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")
      model = ChatOpenAI()

      # Create a simple chain
      chain = prompt | model

      # Use LangChain as normal - all calls will be logged to Braintrust
      response = await chain.ainvoke({"number": "2"})

  if __name__ == "__main__":
      asyncio.run(main())
  ```
</CodeGroup>

## Resources

* [LangChain callback documentation](https://python.langchain.com/docs/how_to/#callbacks)
* [LangChain official documentation](https://python.langchain.com/docs/introduction/)
