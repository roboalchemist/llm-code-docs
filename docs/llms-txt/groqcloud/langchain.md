# Source: https://console.groq.com/docs/langchain

---
description: Learn how to use LangChain with Groq to build blazing-fast, composable LLM applications with advanced chains, memory, and tool use.
title: LangChain + Groq: Fast, Composable LLM Apps - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [🦜️🔗 LangChain + Groq](#-langchain--groq)

While you could use the Groq SDK directly, [LangChain](https://www.langchain.com/) is a framework that makes it easy to build sophisticated applications with LLMs. Combined with Groq API for fast inference speed, you can leverage LangChain components such as:

* **Chains:** Compose multiple operations into a single workflow, connecting LLM calls, prompts, and tools together seamlessly (e.g., prompt → LLM → output parser)
* **Prompt Templates:** Easily manage your prompts and templates with pre-built structures to consisently format queries that can be reused across different models
* **Memory:** Add state to your applications by storing and retrieving conversation history and context
* **Tools:** Extend your LLM applications with external capabilities like calculations, external APIs, or data retrievals
* **Agents:** Create autonomous systems that can decide which tools to use and how to approach complex tasks

### [Quick Start (3 minutes to hello world)](#quick-start-3-minutes-to-hello-world)

#### [1\. Install the package:](#1-install-the-package)

curl

```
pip install langchain-groq
```

#### [2\. Set up your API key:](#2-set-up-your-api-key)

curl

```
export GROQ_API_KEY="your-groq-api-key"
```

#### [3\. Create your first LangChain assistant:](#3-create-your-first-langchain-assistant)

Running the below code will create a simple chain that calls a model to extract product information from text and output it as structured JSON. The chain combines a prompt that tells the model what information to extract, a parser that ensures the output follows a specific JSON format, and `llama-3.3-70b-versatile` to do the actual text processing.

Python

```
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Define the expected JSON structure
parser = JsonOutputParser(pydantic_object={
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "price": {"type": "number"},
        "features": {
            "type": "array",
            "items": {"type": "string"}
        }
    }
})

# Create a simple prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """Extract product details into JSON with this structure:
        {{
            "name": "product name here",
            "price": number_here_without_currency_symbol,
            "features": ["feature1", "feature2", "feature3"]
        }}"""),
    ("user", "{input}")
])

# Create the chain that guarantees JSON output
chain = prompt | llm | parser

def parse_product(description: str) -> dict:
    result = chain.invoke({"input": description})
    print(json.dumps(result, indent=2))

        
# Example usage
description = """The Kees Van Der Westen Speedster is a high-end, single-group espresso machine known for its precision, performance, 
and industrial design. Handcrafted in the Netherlands, it features dual boilers for brewing and steaming, PID temperature control for 
consistency, and a unique pre-infusion system to enhance flavor extraction. Designed for enthusiasts and professionals, it offers 
customizable aesthetics, exceptional thermal stability, and intuitive operation via a lever system. The pricing is approximatelyt $14,499 
depending on the retailer and customization options."""

parse_product(description)
```

**Challenge:** Make the above code your own! Try extending it to include memory with conversation history handling via LangChain to enable users to ask follow-up questions.

For more information on how to build robust, realtime applications with LangChain and Groq, see:

* [Official Documentation: LangChain](https://python.langchain.com/docs/integrations/chat/groq)
* [Groq API Cookbook: Benchmarking a RAG Pipeline with LangChain and LLama](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/benchmarking-rag-langchain/benchmarking%5Frag.ipynb)
* [Webinar: Build Blazing-Fast LLM Apps with Groq, Langflow, & LangChain](https://youtu.be/4ukqsKajWnk?si=ebbbnFH0DySdoWbX)