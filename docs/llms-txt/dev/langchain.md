# Source: https://dev.writer.com/home/integrations/langchain.md

# Using Writer with LangChain

The [Writer LangChain integration](https://github.com/writer/langchain-writer) allows you to leverage Writer's capabilities within the LangChain ecosystem, making it easy to build sophisticated AI applications. In this tutorial, you'll explore each component of the integration and understand how they work.

## Prerequisites

Before you begin, make sure you have:

* Python 3.9 or higher installed
* A [Writer AI Studio](https://app.writer.com/register) account
* A Writer API key. See instructions in the [API Quickstart](/home/quickstart).
* Basic familiarity with Python and [LangChain concepts](https://python.langchain.com/docs/concepts/)

## Installation and setup

First, install the necessary packages:

```bash  theme={null}
pip install langchain-writer python-dotenv
```

Next, create a `.env` file with `WRITER_API_KEY` set to your Writer API key:

```
WRITER_API_KEY=<your-api-key>
```

## Components of the Writer LangChain integration

The `langchain-writer` package provides several key components:

1. `ChatWriter` for text generation
2. Tool calling capabilities, including:
   * `GraphTool` for Knowledge Graph integration
   * `NoCodeAppTool` for no-code applications
   * `LLMTool` for specialized model delegation
3. Additional tools like `PDFParser` for parsing PDFs and `WriterTextSplitter` for intelligent text splitting

## ChatWriter

`ChatWriter` is a LangChain chat model that provides access to Writer's AI capabilities for text generation. It supports streaming, non-streaming, batching, and asynchronous operations. You can use any of the [Palmyra chat models](/home/models) available in AI Studio.

See the [full documentation](https://github.com/writer/langchain-writer/blob/main/docs/chat_writer.md#parameters) for `ChatWriter` to learn more about the available parameters.

### Usage

This example uses `ChatWriter` to ask the Palmyra X5 model to explain what LangChain is in plain terms.

```python  theme={null}
from langchain_writer import ChatWriter
from dotenv import load_dotenv

load_dotenv()

# Initialize the chat model
# These are optional parameters with default values listed here
chat = ChatWriter(
    model="palmyra-x5",  # default model
    temperature=0.7,        # controls randomness (0-1)
    max_tokens=None,        # maximum number of tokens to generate
    timeout=None,           # request timeout
    max_retries=2          # number of retries on failure
)

# Generate a response
response = chat.invoke("Explain what LangChain is in simple terms.")
print(response.content)
```

### Streaming

Streaming allows you to receive the generated text in chunks as it's being produced. This example shows how to stream a response from the Palmyra X5 model using synchronous streaming:

```python  theme={null}
from langchain_writer import ChatWriter
import asyncio
from dotenv import load_dotenv

load_dotenv()

chat = ChatWriter()

# Streaming (synchronous)
for chunk in chat.stream("Write a short poem about artificial intelligence."):
    print(chunk.content, end="")
```

You can also use asynchronous streaming with the `async for` loop and the `astream` method:

```python  theme={null}
from langchain_writer import ChatWriter
import asyncio
from dotenv import load_dotenv

load_dotenv()

chat = ChatWriter()

# Streaming (asynchronous)
async def async_stream():
    async for chunk in chat.astream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="")

asyncio.run(async_stream())
```

### Batch processing

You can batch process multiple prompts for efficient processing. The following example batches three individual LLM invocations and runs them in parallel:

```python  theme={null}
from langchain_writer import ChatWriter
from dotenv import load_dotenv

load_dotenv()

chat = ChatWriter()

questions = [
    "What is a three-sentence definition of retrieval-augmented generation?",
    "When did transformer architecture first appear in the literature?",
    "What are 3 benefits of using AI to assist in software development?"
]

# Process multiple prompts in parallel
responses = chat.batch(questions)

for question, response in zip(questions, responses):
    print(f"Q: {question}")
    print(f"A: {response.content}\n")
```

Note that `batch` returns results in the same order as the inputs. You can use `batch_as_completed` to return results as they complete. Results may arrive out of order, but each includes the input index for matching.

You can also optionally set the `max_concurrency` parameter to control the number of concurrent requests, which can be useful when you want to limit the number of parallel calls to prevent overloading a server or API:

```python  theme={null}
responses = chat.batch(questions,
    config={"max_concurrency": 2}
)
```

See the LangChain documentation on [parallel execution](https://python.langchain.com/docs/concepts/runnables/#optimized-parallel-execution-batch) for more information.

## Tool calling

`ChatWriter` supports tool calling, which allows the model to use external functions to enhance its capabilities. Tool calling is available with Palmyra X4 and later.

### Tool calling basics

To use tool calling, follow these steps:

1. Define a function that will be called by the model and decorate it with the `@tool` decorator.
2. Bind the tool to the chat model using the `bind_tools` method.
3. Use the tool in a chat and append the response to the messages list.
4. Execute the tool call with the arguments given by the model and append the response to the messages list.
5. Invoke the chat model with the updated messages list to receive the final response.

Here's an example of how to use tool calling:

```python  theme={null}
from langchain_writer import ChatWriter
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location."""
    # In a real application, you would call a weather API here
    return f"The weather in {location} is sunny and 75°F"

chat = ChatWriter()
chat_with_tools = chat.bind_tools([get_weather])

messages = [
    HumanMessage(
        "What's the weather like in San Francisco?"
    )
]

response = chat_with_tools.invoke(messages)
messages.append(response)

for tool_call in response.tool_calls:
    selected_tool = {
        "get_weather": get_weather,
    }[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)

response = chat_with_tools.invoke(messages)
print(response.content)
```

### GraphTool

`GraphTool` is a LangChain tool that allows you to retrieve information from a Knowledge Graph to enhance its responses. The tool executes remotely, so you simply need to provide the IDs of the Knowledge Graph you want to use. For more details on the built-in Knowledge Graph chat tool in Writer, see the [Knowledge Graph chat support guide](/home/kg-chat).

#### Usage

```python  theme={null}
from langchain_writer import ChatWriter
from langchain_writer.tools import GraphTool
from dotenv import load_dotenv

load_dotenv()

# Initialize the chat model
chat = ChatWriter()

# Create a graph tool with your knowledge graph ID
graph_tool = GraphTool(graph_ids=["your-knowledge-graph-id"])

# Bind the tool to the chat model
chat_with_tools = chat.bind_tools([graph_tool])

# Ask a question that can be answered using the knowledge graph
response = chat_with_tools.invoke("What information do you have about product X?")
print(response.content)
```

### NoCodeAppTool

`NoCodeAppTool` is a specialized tool that enables access to Writer's no-code applications as LLM tools. This tool allows language models to interact with pre-built applications to enhance their responses.

The tool is designed as a standard "function" type tool and requires manual execution. Unlike the `GraphTool` and `LLMTool` which are executed remotely by Writer's servers, you'll need to handle the execution of the `NoCodeAppTool` in your code.

When initializing the tool, you must provide an `app_id` (either directly or using an environment variable) that corresponds to a no-code application created in your Writer account. The tool automatically retrieves the input parameters for the app during initialization, so you don't need to specify them manually.

You can customize the tool's name (default is "No-code application") and description (default is "No-code application powered by Palmyra") to provide better context to the model. The API key is typically read from environment variables but can also be provided directly.

When working with the tool, remember that all required inputs must be provided when invoking it, or a `ValueError` will be raised. Input values can be either strings or lists of strings, depending on what the no-code application expects.

This tool is particularly useful for generating content, performing specialized data transformations, creating custom outputs based on user inputs, integrating with domain-specific applications, enhancing responses with formatted content, or leveraging pre-built applications for common tasks.

#### Usage

Here's an example of how to use the `NoCodeAppTool`:

```python  theme={null}
from langchain_writer import ChatWriter
from langchain_writer.tools import NoCodeAppTool
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

chat = ChatWriter()

# Create a NoCodeAppTool
app_tool = NoCodeAppTool(
    app_id=os.getenv("APP_ID"), 
    name="Social post generator", 
    description="No-code app that generates social posts from product descriptions"
)

# Bind the tool ChatWriter
chat_with_tools = chat.bind_tools([app_tool])

product_description = "The Terra running shoe is a high-performance, lightweight shoe that offers a comfortable and durable experience. The shoe is also lightweight and easy to carry, making it an ideal option for runners looking for a new pair of shoes."

# Create a conversation
messages = [
    HumanMessage("Can you help me generate a social post about a new running shoe? Here is the product description:\n\n" + product_description)
]

# Get the model's response
response = chat_with_tools.invoke(messages)
messages.append(response)

# If the model requests to use the tool
if response.tool_calls:
    for tool_call in response.tool_calls:
        print("\nTool call:", tool_call)
        
        # Dynamically build the inputs dictionary from the args
        inputs = {}
        for arg in tool_call['args']:
            inputs[arg] = tool_call['args'][arg]
        
        # Execute the tool call
        try:
            tool_response = app_tool.run(tool_input={"inputs": inputs})
            messages.append(tool_response.suggestion)
        except Exception as e:
            print(f"Error running tool: {e}")
    
    # Get the final response
    try:
        final_response = chat_with_tools.invoke(messages)
        print("\nFinal response:", final_response.content)
    except Exception as e:
        print(f"Error getting final response: {e}")
else:
    print("No tool calls were requested.")
```

When providing inputs to the tool, you'll need to format them as a dictionary:

```python  theme={null}
# Example of providing inputs to the tool
inputs = {
    "Input name": "Input value",
    "Another input name": ["List", "of", "string", "values"]
}

# Invoke the tool with the inputs
result = app_tool.run(tool_input={"inputs": inputs})
```

### LLMTool

`LLMTool` is a specialized tool that enables delegation to specific Writer models. This tool allows language models to delegate calls to different Palmyra model types to enhance their responses.

Unlike most LangChain tools that use the standard "function" type, the `LLMTool` has a type of `llm` and is designed specifically for use within the Writer environment. Due to its remote execution nature, this tool doesn't support direct invocation through the `_run` method—attempting to call this method will raise a `NotImplementedError`.

When initializing the tool, you can specify which Palmyra model to delegate to using the `model_name` parameter. Options include general-purpose models like `palmyra-x5`, as well as domain-specific models such as `palmyra-med` for medical content, `palmyra-fin` for financial analysis, and `palmyra-creative` for creative content generation. The default model is `palmyra-x5`. The `description` parameter plays a crucial role in helping the model understand when to use this tool.

When the model uses the LLM tool, the execution happens remotely on Writer's servers, and the response includes additional data in the `additional_kwargs["llm_data"]` field that you can access in your application.

This tool is particularly valuable when you need specialized domain knowledge. For example, you might delegate medical questions to the `palmyra-med` model, use `palmyra-creative` for generating creative content, or leverage `palmyra-fin` for financial analysis.

#### Usage

Here's an example of how to use the `LLMTool`:

```python  theme={null}
from langchain_writer import ChatWriter
from langchain_writer.tools import LLMTool
from dotenv import load_dotenv

load_dotenv()

chat = ChatWriter()

# Create an LLMTool
llm_tool = LLMTool(
    model_name="palmyra-med",
    description="A medical model that can answer questions about the human body and extract ICD-10 codes."
)

# Bind the tool to the ChatWriter
chat_with_tools = chat.bind_tools([llm_tool])

# Now the model can delegate to the specialized LLM in its responses
response = chat_with_tools.invoke([
    ("system", "You are a helpful assistant with access to medical knowledge."),
    ("human", "Can you explain the symptoms of hypertension and provide the ICD-10 code?")
])

print(response.content)

# The LLM data is available in the response
print(response.additional_kwargs["llm_data"])
```

## Additional tools

### PDFParser

`PDFParser` is a document loader that uses Writer's PDF parsing capabilities to extract text from PDF documents. It converts PDFs into LangChain Document objects that can be used in your applications. For more details on the underlying API, see the [PDF parser API reference](/api-reference/tool-api/pdf-parser).

#### Usage

Here's an example of how to use the `PDFParser`:

```python  theme={null}
from langchain_writer import PDFParser
from langchain_core.documents.base import Blob
from dotenv import load_dotenv

load_dotenv()

# Initialize the PDF parser with the desired output format
parser = PDFParser(output_format="markdown")  # Options: "text", "markdown"

# Load a PDF file
file = Blob.from_path("path/to/your/document.pdf")

parsed_pages = parser.parse(blob=file)
print(parsed_pages)
```

#### Output formats

The `PDFParser` supports different output formats:

* `text`: Plain text extraction
* `markdown`: Structured markdown with preserved formatting

```python  theme={null}
# For markdown output
markdown_parser = PDFParser(output_format="markdown")
markdown_docs = markdown_parser.load("path/to/your/document.pdf")
```

### WriterTextSplitter (Deprecated)

<Warning>
  The `WriterTextSplitter` component has been deprecated as of November 18, 2025, as the underlying Writer API endpoint for context-aware text splitting has been removed.

  If you need text splitting capabilities in LangChain, consider using LangChain's built-in text splitters such as `RecursiveCharacterTextSplitter` or `TokenTextSplitter`. See the [LangChain text splitting documentation](https://python.langchain.com/docs/how_to/split_by_token/) for more information.
</Warning>

## Conclusion

In this tutorial, you've explored the LangChain integration with Writer, covering each of its components:

1. `ChatWriter` for text generation
2. Tool calling capabilities, including:
   * `GraphTool` for Knowledge Graph integration
   * `NoCodeAppTool` for no-code applications
   * `LLMTool` for specialized model delegation
3. Additional tools like `PDFParser` for parsing PDFs

This integration provides a foundation for building AI applications with Writer and LangChain. Check out the package [README](https://github.com/writer/langchain-writer) and [documentation](https://github.com/writer/langchain-writer/tree/main/docs), as well as the [LangChain Documentation](https://python.langchain.com/docs/) for more information on how to use LangChain with Writer.
