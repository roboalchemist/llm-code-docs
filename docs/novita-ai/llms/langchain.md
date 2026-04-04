# Source: https://novita.ai/docs/guides/langchain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain

> Integrate Novita AI with LangChain to build intelligent, language model-driven applications. Learn setup, API usage, and function calling workflows.

This guide will walk you through the process of integrating Novita AI with LangChain. You’ll be able to use Novita AI’s powerful language models with LangChain’s robust tools for building language model-driven applications.

## What is LangChain?

LangChain is a framework for developing applications powered by language models. It enables applications that:

* **Are context-aware**: LangChain connects a language model to sources of context (such as prompt instructions, few-shot examples, content to ground its response in, etc.).
* **Reason**: LangChain allows language models to reason—whether it’s determining how to answer based on provided context or deciding what actions to take.

With LangChain, you can build complex workflows, enhance model behavior with external knowledge, and create intelligent systems that can interact dynamically with users and data sources.

## Prerequisites

Before you start, make sure you have the following:

* **Novita AI LLM API Key**:
  * Visit [Novita AI’s website](https://novita.ai/) and create an account.
  * After logging in, go to the [**Key Management**](https://novita.ai/settings/key-management) page to generate your **API Key**. This key is required to connect Novita AI’s models to LangChain.

    <Frame>
      ![Novita AI key management](https://mintlify.s3.us-west-1.amazonaws.com/novitaai/images/third-party/dify-1.png)
    </Frame>
* A basic understanding of Node.js, JavaScript, and how to use environment variables.

## Integration

### Step 1: Set the API Key

For most environments, set the environment variable `NOVITA_API_KEY` as follows:

```bash  theme={"system"}
export NOVITA_API_KEY="your-api-key"
```

Make sure to replace `your-api-key` with the actual key you got from Novita AI.

### Step 2: Install the Required Packages

To integrate Novita AI with LangChain, you need to install the `@langchain-community` package, which includes the Novita AI integration.

Choose one of the following commands to install the necessary packages:

**Using npm:**

```bash  theme={"system"}
npm install @langchain/community @langchain/core
```

**Using yarn:**

```bash  theme={"system"}
yarn add @langchain/community @langchain/core
```

**Using pnpm:**

```bash  theme={"system"}
pnpm add @langchain/community @langchain/core
```

### Step 3: Instantiate the Novita AI Model

Once you’ve installed the necessary packages, you can instantiate the Novita AI model using the `ChatNovitaAI` class.

Here’s an example that demonstrates how to do that:

```javascript  theme={"system"}
import { ChatNovitaAI } from "@langchain/community/chat_models/novita";

const llm = new ChatNovitaAI({
  model: "deepseek/deepseek-r1", // You can choose the model you want to use
  temperature: 0, // Optional: Controls randomness. 0 is deterministic.
  // other parameters can be set here...
});
```

### Step 4: Invoke the Model for Chat Completion

Once the model is instantiated, you can use it to generate chat completions by invoking it with a message.

Here's an example of how to send a message and get a response:

```javascript  theme={"system"}
const aiMsg = await llm.invoke([
  {
    role: "system",
    content: "You are a helpful assistant that translates English to French. Translate the user sentence.",
  },
  {
    role: "human",
    content: "I love programming.",
  },
]);

console.log(aiMsg.content); // The model’s response will be printed here
```

### Step 5: Chain Model with Prompt Templates

LangChain allows you to create powerful workflows by chaining models together with prompt templates. This can be especially useful when you want to reuse the same format for multiple inputs.

Here’s an example where we chain the Novita AI model with a custom prompt template for translating between languages:

```javascript  theme={"system"}
import { ChatPromptTemplate } from "@langchain/core/prompts";

// Create a template for translating languages
const prompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    "You are a helpful assistant that translates {input_language} to {output_language}.",
  ],
  ["human", "{input}"],
]);

// Chain the prompt with the model
const chain = prompt.pipe(llm);

// Invoke the chain with inputs for translation
const result = await chain.invoke({
  input_language: "English",
  output_language: "German",
  input: "I love programming.",
});

console.log(result.content); // The translated text will be printed here
```

### Step 6: Customize the Workflow

You can modify the temperature, add more messages, or tweak other parameters depending on your use case. LangChain is highly flexible, allowing you to design complex interactions by chaining multiple prompts, adding conditional logic, or working with different models.

## Function Calling with Novita AI and LangChain

To implement function calling (or tool usage) with Novita AI's LLM API, LangChain can serve as a convenient framework. In this example, we’ll create a simple math application that allows the model to perform addition and multiplication operations via function calls.

💡 While this guide uses LangChain for convenience, implementing function calling doesn’t require any specific framework. The key is designing the right prompts to make the model understand and correctly invoke functions. LangChain is used here simply to streamline the implementation.

### Prerequisites

First, install the required packages:

```bash  theme={"system"}
pip install langchain-openai python-dotenv
```

### Setting Up the Environment

Create a `.env` file in your project root and add your Novita AI API key:

```
NOVITA_API_KEY=your_api_key_here
```

### Implementation Steps

1. **Define the Tools**

First, let’s create two simple mathematical tools using LangChain's `@tool` decorator:

```python  theme={"system"}
from langchain_core.tools import tool

@tool
def multiply(x: float, y: float) -> float:
    """Multiply two numbers together."""
    return x * y

@tool
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

tools = [multiply, add]
```

2. **Create the Tool Execution Function**

Next, implement a function to execute the tools:

```python  theme={"system"}
from typing import Any, Dict, Optional, TypedDict
from langchain_core.runnables import RunnableConfig

class ToolCallRequest(TypedDict):
    name: str
    arguments: Dict[str, Any]

def invoke_tool(
    tool_call_request: ToolCallRequest, 
    config: Optional[RunnableConfig] = None
):
    """Execute the specified tool with given arguments."""
    tool_name_to_tool = {tool.name: tool for tool in tools}
    name = tool_call_request["name"]
    requested_tool = tool_name_to_tool[name]
    return requested_tool.invoke(tool_call_request["arguments"], config=config)
```

3. **Set Up the LangChain Pipeline**

Create a chain that uses Novita AI's LLM to select and prepare tool calls:

```python  theme={"system"}
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import render_text_description
import os

def create_chain():
    """Create a chain that uses the specified LLM model to select and prepare tool calls."""
    model = ChatOpenAI(
        model="meta-llama/llama-3.3-70b-instruct",
        api_key=os.getenv("NOVITA_API_KEY"),
        base_url="https://api.novita.ai/openai",
    )
    
    rendered_tools = render_text_description(tools)
    system_prompt = f"""\
    You are an assistant that has access to the following set of tools. 
    Here are the names and descriptions for each tool:

    {rendered_tools}

    Given the user input, return the name and input of the tool to use. 
    Return your response as a JSON blob with 'name' and 'arguments' keys.

    The `arguments` should be a dictionary, with keys corresponding 
    to the argument names and the values corresponding to the requested values.
    """

    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", "{input}")]
    )

    return prompt | model | JsonOutputParser()
```

4. **Create the Main Processing Function**

Implement the main function that processes mathematical queries:

```python  theme={"system"}
def process_math_query(query: str):
    """Process a mathematical query by using an LLM to select the appropriate tool and execute it."""
    chain = create_chain()
    message = chain.invoke({"input": query})
    result = invoke_tool(message, config=None)
    return message, result
```

5. **Usage Example**

Here’s how to use the implementation:

```python  theme={"system"}
if __name__ == "__main__":
    message, result = process_math_query(
        "meta-llama/llama-3.3-70b-instruct", 
        "what's 3 plus 1132"
    )
    print(result)  # Output: 1135
```


Built with [Mintlify](https://mintlify.com).