# Source: https://docs.perplexity.ai/guides/chat-completions-sdk

## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#overview)
Overview
Generate AI responses with web-grounded knowledge using either the Python or TypeScript SDKs. Both SDKs provide full support for chat completions, streaming responses, async operations, and comprehensive error handling.
## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#quick-start)
Quick Start
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about the latest developments in AI",
        }
    ],
    model="sonar",
)
print(f"Response: {completion.choices[0].message.content}")

```

Example Output
Copy
Ask AI
```
Response: Based on the latest information, here are some key developments in AI for 2024:
**Large Language Models & Foundation Models:**
- GPT-4 and its variants continue to improve with better reasoning capabilities
- Open-source models like Llama 2 and Code Llama have gained significant traction
- Specialized models for coding, math, and scientific tasks have emerged
**Multimodal AI:**
- Vision-language models can now process images, text, and audio simultaneously
- Real-time image generation and editing capabilities have improved dramatically
**AI Safety & Alignment:**
- Constitutional AI and RLHF techniques are becoming standard practice
- Increased focus on AI governance and regulatory frameworks...
Request ID: req_123abc456def789

```

## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#features)
Features
### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#model-selection)
Model Selection
Choose from different Sonar models based on your needs:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# Standard Sonar model for general queries
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is quantum computing?"}],
    model="sonar"
)
# Sonar Pro for more complex queries
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Analyze the economic implications of renewable energy adoption"}],
    model="sonar-pro"
)
# Sonar Reasoning for complex analytical tasks
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Solve this complex mathematical problem step by step"}],
    model="sonar-reasoning"
)

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#conversation-context)
Conversation Context
Build multi-turn conversations with context:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
messages = [
    {"role": "system", "content": "You are a helpful research assistant."},
    {"role": "user", "content": "What are the main causes of climate change?"},
    {"role": "assistant", "content": "The main causes of climate change include..."},
    {"role": "user", "content": "What are some potential solutions?"}
]
completion = client.chat.completions.create(
    messages=messages,
    model="sonar"
)

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#web-search-options)
Web Search Options
Control how the model searches and uses web information:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "What are the latest developments in renewable energy?"}
    ],
    model="sonar",
    web_search_options={
        "search_recency_filter": "week",  # Focus on recent results
        "search_domain_filter": ["energy.gov", "iea.org", "irena.org"],  # Trusted sources
        "max_search_results": 10
    }
)

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#response-customization)
Response Customization
Customize response format and behavior:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Explain machine learning in simple terms"}
    ],
    model="sonar",
    max_tokens=500,  # Limit response length
    temperature=0.7,  # Control creativity
    top_p=0.9,       # Control diversity
    presence_penalty=0.1,  # Reduce repetition
    frequency_penalty=0.1
)

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#streaming-responses)
Streaming Responses
Get real-time response streaming for better user experience:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
stream = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Write a summary of recent AI breakthroughs"}
    ],
    model="sonar",
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

```

For comprehensive streaming documentation including metadata collection, error handling, advanced patterns, and raw HTTP examples, see the [Streaming Guide](https://docs.perplexity.ai/guides/streaming-responses).
## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#async-chat-completions)
Async Chat Completions
Async chat completions are only available for the sonar-deep-research model.
For long-running or batch processing tasks, use the async endpoints:
### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#creating-async-requests)
Creating Async Requests
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# Start an async completion request
async_request = client.async_.chat.completions.create(
    messages=[
        {"role": "user", "content": "Write a comprehensive analysis of renewable energy trends"}
    ],
    model="sonar-deep-research",
    max_tokens=2000
)
print(f"Request submitted with ID: {async_request.request_id}")
print(f"Status: {async_request.status}")

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#checking-request-status)
Checking Request Status
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# Check the status of an async request
request_id = "req_123abc456def789"
status = client.async_.chat.completions.get(request_id)
print(f"Status: {status.status}")
if status.status == "completed":
    print(f"Response: {status.result.choices[0].message.content}")
elif status.status == "failed":
    print(f"Error: {status.error}")

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#listing-async-requests)
Listing Async Requests
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# List recent async requests
requests = client.async_.chat.completions.list(
    limit=10,
    status="completed"
)
for request in requests.data:
    print(f"ID: {request.id}, Status: {request.status}")

```

## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#advanced-usage)
Advanced Usage
### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#error-handling)
Error Handling
Handle chat-specific errors:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
import perplexity
try:
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "What is AI?"}],
        model="sonar",
        max_tokens=50000  # Exceeds limit
    )
except perplexity.BadRequestError as e:
    print(f"Invalid request parameters: {e}")
except perplexity.RateLimitError as e:
    print("Rate limit exceeded, please retry later")
except perplexity.APIStatusError as e:
    print(f"API error: {e.status_code}")

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#custom-instructions)
Custom Instructions
Use system messages for consistent behavior:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
system_prompt = """You are an expert research assistant specializing in technology and science. 
Always provide well-sourced, accurate information and cite your sources. 
Format your responses with clear headings and bullet points when appropriate."""
completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Explain quantum computing applications"}
    ],
    model="sonar-pro"
)

```

### 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#concurrent-operations)
Concurrent Operations
Handle multiple conversations efficiently:
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
async def handle_multiple_chats(user_messages):
    client = AsyncPerplexity()
    tasks = [
        client.chat.completions.create(
            messages=[{"role": "user", "content": msg}],
            model="sonar-deep-reseach"
        )
        for msg in user_messages
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)

```

## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#best-practices)
Best Practices
1
Use appropriate models
Choose the right model for your use case: `sonar` for general queries, `sonar-pro` for complex analysis, `sonar-reasoning` for analytical tasks.
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# For quick factual queries
simple_query = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    model="sonar"
)
# For complex analysis
complex_query = client.chat.completions.create(
    messages=[{"role": "user", "content": "Analyze the economic impact of AI on employment"}],
    model="sonar-pro"
)

```

2
Implement streaming for long responses
Use streaming for better user experience with lengthy responses.
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
def stream_response(query):
    stream = client.chat.completions.create(
        messages=[{"role": "user", "content": query}],
        model="sonar",
        stream=True
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            response += content
    return response

```

3
Handle rate limits gracefully
Implement exponential backoff for production applications.
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
import time
import random
def chat_with_retry(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                messages=messages,
                model="sonar"
            )
        except perplexity.RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)

```

4
Optimize for specific use cases
Configure parameters based on your application’s needs.
  * Python SDK
  * TypeScript SDK


Copy
Ask AI
```
# For factual Q&A
factual_config = {
    "temperature": 0.1,  # Low creativity for accuracy
    "top_p": 0.9,
    "search_recency_filter": "month"
}
# For creative writing
creative_config = {
    "temperature": 0.8,  # Higher creativity
    "top_p": 0.95,
    "presence_penalty": 0.1,
    "frequency_penalty": 0.1
}
# Usage
factual_response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is the current inflation rate?"}],
    model="sonar",
    **factual_config
)

```

## 
[​](https://docs.perplexity.ai/guides/chat-completions-sdk#resources)
Resources
  * [The Perplexity SDK Guide](https://docs.perplexity.ai/guides/perplexity-sdk) - The Perplexity SDK guide
  * [OpenAI Compatibility](https://docs.perplexity.ai/guides/chat-completions-guide) - OpenAI compatibility guide
  * [Streaming Responses](https://docs.perplexity.ai/guides/streaming-responses) - Complete streaming guide with advanced patterns
  * [API Reference - Chat Completions](https://docs.perplexity.ai/api-reference/chat-completions-post) - Chat Completions API Reference
  * [API Reference - Async Chat Completions](https://docs.perplexity.ai/api-reference/async-chat-completions-post) - Async API Reference
  * [Structured Outputs](https://docs.perplexity.ai/guides/structured-outputs) - Formatted response generation


