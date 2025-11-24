# Source: https://dev.writer.com/home/integrations/strands.md

# Using Writer with AWS Strands Agents

Writer's models are available on [AWS Strands Agents](https://strandsagents.com/latest/).

Strands Agents SDK from AWS is an open-source framework that enables developers to build and deploy AI agents using a model-driven approach. This integration allows you to use Writer models within the Strands agent ecosystem, from local development to production deployment.

## Available models

Writer offers several specialized Palmyra models:

| Model            | Model ID (Writer API) | Model ID (Bedrock)          | Context Window | Availability                                                                               | Description                                                                                        |
| ---------------- | --------------------- | --------------------------- | -------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Palmyra X5       | `palmyra-x5`          | `us.writer.palmyra-x5-v1:0` | 1M tokens      | [Writer API](#writer-api-configuration) or [Amazon Bedrock](#amazon-bedrock-configuration) | Latest model with 1 million token context for complex workflows, supports vision and multi-content |
| Palmyra X4       | `palmyra-x4`          | `us.writer.palmyra-x4-v1:0` | 128k tokens    | [Writer API](#writer-api-configuration) or [Amazon Bedrock](#amazon-bedrock-configuration) | Advanced model for workflow automation and tool calling                                            |
| Palmyra Fin      | `palmyra-fin`         | Not available               | 128k tokens    | [Writer API](#writer-api-configuration) only                                               | Finance-specialized model                                                                          |
| Palmyra Med      | `palmyra-med`         | Not available               | 32k tokens     | [Writer API](#writer-api-configuration) only                                               | Healthcare-specialized model for medical analysis                                                  |
| Palmyra Creative | `palmyra-creative`    | Not available               | 128k tokens    | [Writer API](#writer-api-configuration) only                                               | Creative writing and brainstorming model                                                           |

See the [Writer models guide](/home/models) for more details and use cases.

<Note>
  The above Bedrock models IDs for Palmyra X5 and Palmyra X4 are using [cross-region inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html). Check which AWS Regions support Writer models before selecting an inference profile.
</Note>

## Prerequisites

Before you begin, make sure you have:

* Python 3.10 or higher installed
* Basic familiarity with Python and [AWS Strands](https://strandsagents.com/latest/)

## Writer API configuration

### Prerequisites

Before you configure the WRITER API client for Strands Agent SDK, make sure you have:

* A [Writer AI Studio](https://app.writer.com/register) account
* A Writer API key. See instructions in the [API Quickstart](/home/quickstart)

### Installation

To use Writer models with Strands Agents, install the optional Writer dependency:

```bash  theme={null}
pip install 'strands-agents[writer]'
```

<Note>
  To follow along with the examples in this guide, you'll also need the [Strands Agent Tools package](https://github.com/strands-agents/tools). Install the package with `pip install strands-agents-tools`.
</Note>

### Client configuration

You can pass additional arguments to the Writer client via `client_args`:

```python  theme={null}
model = WriterModel(
    client_args={
        "api_key": "<WRITER_API_KEY>",
        "timeout": 30,
        "base_url": "https://api.writer.com/v1",
        # Additional client configuration options
    },
    model_id="palmyra-x5"
)
```

### Environment variables

You can set your Writer API key as an environment variable instead of passing it directly:

```bash  theme={null}
export WRITER_API_KEY="your_api_key_here"
```

Then initialize the model without the `client_args["api_key"]` parameter:

```python  theme={null}
model = WriterModel(model_id="palmyra-x5")
```

### Usage

After installing, you can import and initialize the Writer provider in Strands Agents:

```python  theme={null}
from strands import Agent
from strands.models.writer import WriterModel
from strands_tools import calculator

model = WriterModel(
    client_args={"api_key": "<WRITER_API_KEY>"},
    model_id="palmyra-x5",
)

agent = Agent(model=model, tools=[calculator])
response = agent("What is 2+2")
print(response)
```

<Note>
  By default, Strands Agents use a `PrintingCallbackHandler` that streams responses to `stdout` as they're generated. When you call `agent("What is 2+2")`, you'll see the response appear in real-time as it's being generated. The `print(response)` above also shows the final collected result after the response is complete. See [Callback Handlers](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/streaming/callback-handlers/?h=callback) in the Strands documentation for more details.
</Note>

## Amazon Bedrock configuration

You can also use Writer models through Amazon Bedrock, which provides a managed service for accessing foundation models.

### Prerequisites

Before you configure the Amazon Bedrock client for Strands Agent SDK, follow the [Bedrock integration guide](/home/integrations/bedrock) to set up AWS credentials, enable Writer models in your region, and set up the required IAM permissions.

### Installation

Install the base Strands Agents package:

```bash  theme={null}
pip install strands-agents
```

Bedrock is the default model provider in Strands Agents, so no additional model provider installation is required. The `BedrockModel` class is available by default.

<Note>
  To follow along with the examples in this guide, you'll also need the [Strands Agent Tools package](https://github.com/strands-agents/tools). Install the package with `pip install strands-agent-tools`.
  To follow along with the examples in this guide, you'll also need the [Strands Agent Tools package](https://github.com/strands-agents/tools). Install the package with `pip install strands-agents-tools`.
</Note>

### Client configuration

The following client configuration uses the `us.writer.palmyra-x5-v1:0` model ID, which is the ID for the [cross-region inference profile for Palmyra X5](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html). Check which AWS Regions support Writer models before selecting an inference profile.

```python  theme={null}
# Configure Bedrock model with Writer model ID
model = BedrockModel(
    model_id="us.writer.palmyra-x5-v1:0",
    region_name="us-west-2",  # Your preferred AWS region
    # Additional client configuration options
)
```

### Usage

After configuring the Bedrock model, you can use it with Strands Agents:

```python  theme={null}
from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import calculator

# Configure Bedrock model with Writer model ID
model = BedrockModel(
    model_id="us.writer.palmyra-x5-v1:0",
    region_name="us-west-2"
)

agent = Agent(model=model, tools=[calculator])
response = agent("What is 2+2")
print(response)
```

## Model configuration

The `WriterModel` accepts configuration parameters as keyword arguments to the model constructor:

| Parameter        | Type                              | Description                                                                                                                                                                                             | Default                                                              | Options                                                                     |
| ---------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `model_id`       | `str`                             | Model name to use (`palmyra-x5`, `palmyra-x4`, etc.)                                                                                                                                                    | Required                                                             | [reference](/home/models)                                                   |
| `max_tokens`     | `Optional[int]`                   | Maximum number of tokens to generate                                                                                                                                                                    | See the Context Window for [each available model](#available-models) | [reference](/api-reference/completion-api/chat-completion#body-max-tokens)  |
| `stop`           | `Optional[Union[str, List[str]]]` | A token or sequence of tokens that, when generated, causes the model to stop producing further content. This can be a single token or an array of tokens, acting as a signal to end the output.         | `None`                                                               | [reference](/api-reference/completion-api/chat-completion#body-stop)        |
| `stream_options` | `Dict[str, Any]`                  | Additional options for streaming. Specify `include_usage` to include usage information in the response, in the `accumulated_usage` field. If you don't specify this, `accumulated_usage`for each value. | `None`                                                               | [reference](/api-reference/completion-api/chat-completion#body-stream)      |
| `temperature`    | `Optional[float]`                 | What sampling temperature to use (0.0 to 2.0). A higher temperature produces more random output.                                                                                                        | `1`                                                                  | [reference](/api-reference/completion-api/chat-completion#body-temperature) |
| `top_p`          | `Optional[float]`                 | Threshold for "nucleus sampling"                                                                                                                                                                        | `None`                                                               | [reference](/api-reference/completion-api/chat-completion#body-top_p)       |

## Examples

### Writer API integration

#### Enterprise workflow automation

```python  theme={null}
from strands import Agent
from strands.models.writer import WriterModel
from my_tools import web_search, email_sender  # Custom tools from your local module

model = WriterModel(
    client_args={"api_key": "<WRITER_API_KEY>"},
    model_id="palmyra-x5",
)

agent = Agent(
    model=model,
    tools=[web_search, email_sender],
    system_prompt="You are an enterprise assistant that helps automate business workflows."
)

response = agent("Research our competitor's latest product launch and draft a summary email for the leadership team")
```

<Note>
  The `web_search` and `email_sender` tools in this example are custom tools that you would need to define. See [Python Tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/python-tools/?h=python+tools) for guidance on creating custom tools, or use existing tools from the [`strands_tools` package](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/example-tools-package/).
</Note>

#### Financial analysis with Palmyra Fin

```python  theme={null}
from strands import Agent
from strands.models.writer import WriterModel

# Use specialized finance model for financial analysis
model = WriterModel(
    client_args={"api_key": "<WRITER_API_KEY>"},
    model_id="palmyra-fin"
)

agent = Agent(
    model=model,
    system_prompt="You are a financial analyst assistant. Provide accurate, data-driven analysis."
)

# Replace the placeholder with your actual financial report content
actual_report = """
[Your quarterly earnings report content would go here - this could include:
- Revenue figures
- Profit margins
- Growth metrics
- Risk factors
- Market analysis
- Any other financial data you want analyzed]
"""

response = agent(f"Analyze the key financial risks in this quarterly earnings report: {actual_report}")
```

#### Long-context document processing

```python  theme={null}
from strands import Agent
from strands.models.writer import WriterModel

# Use Palmyra X5 for processing very long documents
model = WriterModel(
    client_args={"api_key": "<WRITER_API_KEY>"},
    model_id="palmyra-x5",
    temperature=0.2
)

agent = Agent(
    model=model,
    system_prompt="You are a document analysis assistant that can process and summarize lengthy documents."
)

# Can handle documents up to 1M tokens
# Replace the placeholder with your actual document content
actual_transcripts = """
[Meeting transcript content would go here - this could be thousands of lines of text
from meeting recordings, documents, or other long-form content that you want to analyze]
"""

response = agent(f"Summarize the key decisions and action items from these meeting transcripts: {actual_transcripts}")
```

#### Vision and image analysis

Palmyra X5 supports vision capabilities, allowing you to analyze images and extract information from visual content.

```python  theme={null}
from strands import Agent
from strands.models.writer import WriterModel

# Use Palmyra X5 for vision tasks
model = WriterModel(
    client_args={"api_key": "<WRITER_API_KEY>"},
    model_id="palmyra-x5"
)

agent = Agent(
    model=model,
    system_prompt="You are a visual analysis assistant. Provide detailed, accurate descriptions of images and extract relevant information."
)

# Read the image file
with open("path/to/image.png", "rb") as image_file:
    image_data = image_file.read()

messages = [
    {
        "role": "user",
        "content": [
            {
                "image": {
                    "format": "png",
                    "source": {
                        "bytes": image_data
                    }
                }
            },
            {
                "text": "Analyze this image and describe what you see. What are the key elements, colors, and any text or objects visible?"
            }
        ]
    }
]

# Create an agent with the image message
vision_agent = Agent(model=model, messages=messages)

# Analyze the image
response = vision_agent("What are the main features of this image and what might it be used for?")

print(response)
```

### Bedrock integration

#### Structured output generation

Palmyra X5 and X4 support structured output generation using [Pydantic models](https://docs.pydantic.dev/latest/) through Bedrock. This is useful for ensuring consistent, validated responses.

<Note>
  Structured output disables streaming and returns the complete response at once, unlike regular chat completions, which stream by default. See [Callback Handlers](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/streaming/callback-handlers/?h=callback) for more details.
</Note>

```python  theme={null}
import os
from boto3 import session
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from strands import Agent
from strands.models import BedrockModel

load_dotenv()

# Define a structured schema for marketing campaign
class MarketingCampaign(BaseModel):
    campaign_name: str
    target_audience: str
    key_messages: List[str]
    channels: List[str]
    budget_allocation: str
    success_metrics: List[str]
    timeline: str
    call_to_action: str

# Use Writer Palmyra X5 through Bedrock
bedrock_model = BedrockModel(
    model_id='us.writer.palmyra-x5-v1:0',
    boto_session=session.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
        aws_session_token=os.getenv("AWS_SESSION_TOKEN", ""),
        region_name="us-west-2",
    ),
    streaming=False,
)

agent = Agent(
    model=bedrock_model,
    system_prompt="You are a marketing strategist. Create comprehensive marketing campaigns with structured data for enterprise clients."
)

# Generate structured marketing campaign
response = agent.structured_output(
    output_model=MarketingCampaign,
    prompt="Create a B2B marketing campaign for a cloud infrastructure platform targeting enterprise IT decision-makers and CTOs."
)

print(f"Campaign: {response.campaign_name}\nTarget Audience: {response.target_audience}\nKey Messages: {response.key_messages}\nChannels: {response.channels}\nBudget: {response.budget_allocation}\nMetrics: {response.success_metrics}\nTimeline: {response.timeline}\nCall to Action: {response.call_to_action}")
```

#### Memory agent

This example demonstrates how to use Writer models through Bedrock with memory capabilities. The `mem0_memory` tool from `strands_tools` provides persistent, long-term memory that stores information using [Mem0's memory architecture](https://strandsagents.com/latest/documentation/docs/examples/python/memory_agent/), allowing the agent to remember user preferences, facts, and context across multiple sessions. The memory system uses semantic search to retrieve relevant information and can store, list, and retrieve memories based on user queries.

```python  theme={null}
import os
import logging

from boto3 import session
from dotenv import load_dotenv

from strands import Agent
from strands.models import BedrockModel
from strands_tools import mem0_memory, use_llm

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

USER_ID = "mem0_user"

# System prompt for the memory agent
MEMORY_SYSTEM_PROMPT = f"""You are a personal assistant that maintains context by remembering user details.

Capabilities:
- Store new information using mem0_memory tool (action="store")
- Retrieve relevant memories (action="retrieve")
- List all memories (action="list")
- Provide personalized responses

Key Rules:
- Always include user_id={USER_ID} in tool calls
- Be conversational and natural in responses
- Format output clearly
- Acknowledge stored information
- Only share relevant information
- Politely indicate when information is unavailable
"""

# Use Writer Palmyra X5 through Bedrock
bedrock_model = BedrockModel(
    model_id='us.writer.palmyra-x5-v1:0',
    boto_session=session.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
        aws_session_token=os.getenv("AWS_SESSION_TOKEN", ""),
        region_name="us-west-2",
    ),
    streaming=False,
)

# Create an agent with memory capabilities
memory_agent = Agent(
    model=bedrock_model,
    system_prompt=MEMORY_SYSTEM_PROMPT,
    tools=[mem0_memory, use_llm],
)

def initialize_demo_memories():
    """Initialize some demo memories to showcase functionality."""
    content = """My name is Alex. I like to travel and stay in Airbnbs rather than hotels. I am planning a trip to Japan next spring. I enjoy hiking and outdoor photography as hobbies. I have a dog named Max. My favorite cuisine is Italian food."""
    memory_agent.tool.mem0_memory(action="store", content=content, user_id=USER_ID)

# Example usage
if __name__ == "__main__":
    print("\n🧠 Memory Agent 🧠\n")
    
    # Initialize demo memories
    initialize_demo_memories()
    print("Demo memories initialized!")
    
    # Example interactions
    print("\nExample: What do you know about me?")
    response = memory_agent("What do you know about me?")
    print(f"Response: {response}")
    
    print("\nExample: Remember that I prefer window seats on flights")
    response = memory_agent("Remember that I prefer window seats on flights")
    print(f"Response: {response}")
    
    print("\nExample: What are my travel preferences?")
    response = memory_agent("What are my travel preferences?")
    print(f"Response: {response}")
```

## Additional resources

See more information and examples below:

* [Additional code examples for Strands Agents](https://github.com/writer/aws-examples/tree/main/strands-examples)
* [Strands Agents GitHub repository](https://github.com/strands-agents/sdk-python)
* [Writer models](/home/models)
