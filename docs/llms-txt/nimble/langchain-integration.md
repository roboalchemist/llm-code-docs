# Source: https://docs.nimbleway.io/ai-agents/langchain-integration.md

# LangChain Integration

### Overview

The [`langchain-nimble`](https://pypi.org/project/langchain-nimble/) package provides production-grade LangChain integrations for Nimble's Search and Extract APIs, enabling developers to build RAG applications and AI agents that can search, access, and retrieve online information from anywhere on the web.

The package includes **two retrievers** and **two tools** for comprehensive web data access:

**Retrievers:**

* `NimbleSearchRetriever` - Web search with deep mode, LLM answers, and filtering
* `NimbleExtractRetriever` - Direct URL content extraction

**Tools (for AI Agents):**

* `NimbleSearchTool` - Agent-integrated web search
* `NimbleExtractTool` - Agent-integrated content extraction

#### Key Features

* **Fast + Deep mode** - Quick metadata retrieval or comprehensive content extraction
* **Smart filtering** - Domain and date filtering, topic-based routing
* **Multiple parsing formats** - Plain text, markdown (default), or simplified HTML
* **Full async support** - Both sync and async operations
* **Production-ready** - Retry logic, connection pooling, comprehensive error handling

If you'd like to learn more about the underlying Nimble Search APIs, visit the [documentation here](https://docs.nimbleway.com/nimble-sdk/search-apiw).

***

### Quick Start

#### Installation

```bash
pip install -U langchain langchain-nimble langchain-openai
```

#### Setup

Get your API credentials from [Nimble's dashboard](https://app.nimbleway.com/signup?returnTo=/pipelines/nimbleapi) (free trial available) and set as an environment variable:

```bash
export NIMBLE_API_KEY="your-api-key"
```

#### Build an AI Agent with Web Search

```python
from langchain.agents import create_agent
from langchain_nimble import NimbleSearchTool, NimbleExtractTool
from langchain_openai import ChatOpenAI

# Initialize tools
search_tool = NimbleSearchTool()
extract_tool = NimbleExtractTool()

# Create agent with multiple tools
agent = create_agent(
    model=ChatOpenAI(model="gpt-5"),
    tools=[search_tool, extract_tool],
    system_prompt=(
        "You are a helpful research assistant with access to "
        "real-time web information. You can search the web and "
        "extract content from specific URLs."
    )
)

# Use the agent
response = agent.invoke({
    "messages": [(
        "user",
        "What are the latest developments in AI agents? "
        "Summarize key findings."
    )]
})

print(response["messages"][-1].content)
```

***

### RAG with Knowledge Base

Extract specific URLs as your knowledge base and use them for RAG:

```python
from langchain_nimble import NimbleExtractRetriever
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Extract your knowledge base from specific URLs
retriever = NimbleExtractRetriever(
    urls=[
        "https://python.langchain.com/docs/concepts/retrievers/",
        "https://python.langchain.com/docs/concepts/tools/",
        "https://python.langchain.com/docs/tutorials/agents/"
    ],
    parsing_type="markdown"
)

# Build RAG chain
llm = ChatOpenAI(model="gpt-5", temperature=0)
prompt = ChatPromptTemplate.from_template(
    """Answer based only on the provided documentation.

Documentation: {context}

Question: {question}"""
)

chain = (
    {"context": retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)),
     "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Ask questions about your knowledge base
answer = chain.invoke("What are the key differences between retrievers and tools in LangChain?")
print(answer)
```

***

### Additional Resources

* [GitHub Repository](https://github.com/Nimbleway/langchain-nimble)
* [PyPI Package](https://pypi.org/project/langchain-nimble/)
* [Example Cookbook](https://github.com/Nimbleway/cookbook)
