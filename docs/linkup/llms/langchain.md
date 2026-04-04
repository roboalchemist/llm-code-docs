# Source: https://docs.linkup.so/pages/integrations/langchain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Langchain

> How to use Linkup with our Langchain SDK

## Overview

Linkup can be used with [LangChain](https://www.langchain.com/) as a [Retriever](https://python.langchain.com/api_reference/core/retrievers.html). This integration allows you to build powerful applications that retrieve contextual information from the internet.

## Getting Started with Linkup in LangChain

<Steps>
  <Step title="Install the LangChain integration">
    ```shell  theme={null}
    pip install langchain-linkup
    ```
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Create and use the Linkup Retriever">
    ```python  theme={null}
    from langchain_linkup import LinkupSearchRetriever
    import os

    os.environ["LINKUP_API_KEY"] = "PASTE_YOUR_API_KEY_HERE"

    retriever = LinkupSearchRetriever(
    depth="deep",  # "standard" or "deep"
    )

    # Perform a search query
    documents = retriever.invoke(input="What is Linkup, the new French AI startup?")
    print(documents)
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th style={{ color: '#FFFFFF' }}>Parameter</th>
            <th style={{ color: '#FFFFFF' }}>Options</th>
            <th style={{ color: '#FFFFFF' }}>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>
</Steps>

## Example Project: RAG Pipeline with OpenAI

<Steps>
  <Step title="Install dependencies">
    ```shell  theme={null}
    pip install langchain-openai python-dotenv
    ```
  </Step>

  <Step title="Set up API keys">
    <Info>
      You need API keys for both Linkup and OpenAI. You can get an OpenAI API key [here](https://openai.com/index/openai-api/).
    </Info>

    ```python  theme={null}
    import os
    from dotenv import load_dotenv

    # Load from .env file if available
    load_dotenv()

    # Or set manually
    os.environ["LINKUP_API_KEY"] = "YOUR_LINKUP_API_KEY"
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    ```
  </Step>

  <Step title="Create the RAG pipeline">
    ```python  theme={null}
    from typing import Any, Literal
    from langchain_core.documents import Document
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
    from langchain_openai import ChatOpenAI
    from langchain_linkup import LinkupSearchRetriever

    # Configuration
    query: str = "What is Linkup, the new French AI startup?"
    linkup_depth: Literal["standard", "deep"] = "standard"
    open_ai_model: str = "gpt-4o-mini"

    # Initialize retriever
    retriever = LinkupSearchRetriever(depth=linkup_depth)

    # Format documents helper function
    def format_retrieved_documents(docs: list[Document]) -> str:
        return "\n\n".join(
            [
                f"{document.metadata['name']} ({document.metadata['url']}):\n{document.page_content}"
                for document in docs
            ]
        )

    # Debug helper function
    def inspect_context(state: dict[str, Any]) -> dict[str, Any]:
        print(f"Context: {state['context']}\n\n")
        return state

    # Create prompt and model
    generation_prompt_template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(generation_prompt_template)
    model = ChatOpenAI(model=open_ai_model)
    ```
  </Step>

  <Step title="Run the pipeline">
    ```python  theme={null}
    # Build and execute the chain
    chain: Runnable[Any, str] = (
        {"context": retriever | format_retrieved_documents, "question": RunnablePassthrough()}
        | RunnableLambda(inspect_context)
        | prompt
        | model
        | StrOutputParser()
    )

    # Get response
    response = chain.invoke(input=query)
    print(f"Response: {response}")
    ```

    **Example Response**

    ```
    Context: Linkup (https://www.linkup.fr):
    Linkup is a French AI startup that provides a search API for LLMs, enabling them to search the web and access up-to-date information.

    Response: Linkup is a French AI startup that has developed a search API specifically designed for Large Language Models (LLMs). Their technology allows LLMs to search the web and access current information, which helps overcome the limitation of outdated training data that many AI models face. This enables applications built with LLMs to provide more accurate and up-to-date responses by connecting them to real-time information from the internet.
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).