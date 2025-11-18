# Source: https://docs.perplexity.ai/guides/chat-completions-sdk.md

# Chat Completions SDK

> Use the Perplexity SDKs to access the Chat Completions API with type safety, streaming support, and modern language features.

## Overview

Generate AI responses with web-grounded knowledge using either the Python or TypeScript SDKs. Both SDKs provide full support for chat completions, streaming responses, async operations, and comprehensive error handling.

## Quick Start

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    const completion = await client.chat.completions.create({
      messages: [
        {
          role: "user",
          content: "Tell me about the latest developments in AI",
        }
      ],
      model: "sonar",
    });

    console.log(`Response: ${completion.choices[0].message.content}`);
    ```
  </Tab>
</Tabs>

<Accordion title="Example Output">
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
</Accordion>

## Features

### Model Selection

Choose from different Sonar models based on your needs:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    // Standard Sonar model for general queries
    const completion = await client.chat.completions.create({
      messages: [{ role: "user", content: "What is quantum computing?" }],
      model: "sonar"
    });

    // Sonar Pro for more complex queries
    const completion = await client.chat.completions.create({
      messages: [{ role: "user", content: "Analyze the economic implications of renewable energy adoption" }],
      model: "sonar-pro"
    });

    // Sonar Reasoning for complex analytical tasks
    const completion = await client.chat.completions.create({
      messages: [{ role: "user", content: "Solve this complex mathematical problem step by step" }],
      model: "sonar-reasoning"
    });
    ```
  </Tab>
</Tabs>

### Conversation Context

Build multi-turn conversations with context:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    const messages: Perplexity.ChatMessage[] = [
      { role: "system", content: "You are a helpful research assistant." },
      { role: "user", content: "What are the main causes of climate change?" },
      { role: "assistant", content: "The main causes of climate change include..." },
      { role: "user", content: "What are some potential solutions?" }
    ];

    const completion = await client.chat.completions.create({
      messages,
      model: "sonar"
    });
    ```
  </Tab>
</Tabs>

### Web Search Options

Control how the model searches and uses web information:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    const completion = await client.chat.completions.create({
      messages: [
        { role: "user", content: "What are the latest developments in renewable energy?" }
      ],
      model: "sonar",
      search_recency_filter: "week",  // Focus on recent results
      search_domain_filter: ["energy.gov", "iea.org", "irena.org"],  // Trusted sources
      return_images: true,  // Include image URLs
      return_related_questions: true  // Get follow-up questions
    });
    ```
  </Tab>
</Tabs>

### Response Customization

Customize response format and behavior:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    const completion = await client.chat.completions.create({
      messages: [
        { role: "user", content: "Explain machine learning in simple terms" }
      ],
      model: "sonar",
      max_tokens: 500,  // Limit response length
      temperature: 0.7,  // Control creativity (0-2)
      top_p: 0.9,       // Control diversity (0-1)
      presence_penalty: 0.1,  // Reduce repetition (-2 to 2)
      frequency_penalty: 0.1  // Reduce repetition (-2 to 2)
    });
    ```
  </Tab>
</Tabs>

### Streaming Responses

Get real-time response streaming for better user experience:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    const stream = await client.chat.completions.create({
      messages: [
        { role: "user", content: "Write a summary of recent AI breakthroughs" }
      ],
      model: "sonar",
      stream: true
    });

    for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
      }
    }
    ```
  </Tab>
</Tabs>

<Info>
  For comprehensive streaming documentation including metadata collection, error handling, advanced patterns, and raw HTTP examples, see the [Streaming Guide](/guides/streaming-responses).
</Info>

## Async Chat Completions

<Tip>
  Async chat completions are only available for the sonar-deep-research model.
</Tip>

For long-running or batch processing tasks, use the async endpoints:

### Creating Async Requests

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    // Start an async completion request
    const asyncRequest = await client.async.chat.completions.create({
      messages: [
        { role: "user", content: "Write a comprehensive analysis of renewable energy trends" }
      ],
      model: "sonar-deep-reasearch",
      max_tokens: 2000
    });

    console.log(`Request submitted with ID: ${asyncRequest.request_id}`);
    console.log(`Status: ${asyncRequest.status}`);
    ```
  </Tab>
</Tabs>

### Checking Request Status

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    # Check the status of an async request
    request_id = "req_123abc456def789"
    status = client.async_.chat.completions.get(request_id)

    print(f"Status: {status.status}")
    if status.status == "completed":
        print(f"Response: {status.result.choices[0].message.content}")
    elif status.status == "failed":
        print(f"Error: {status.error}")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    // Check the status of an async request
    const requestId = "req_123abc456def789";
    const status = await client.async.chat.completions.get(requestId);

    console.log(`Status: ${status.status}`);
    if (status.status === "completed") {
      console.log(`Response: ${status.result?.choices[0]?.message?.content}`);
    } else if (status.status === "failed") {
      console.log(`Error: ${status.error}`);
    }
    ```
  </Tab>
</Tabs>

### Listing Async Requests

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    # List recent async requests
    requests = client.async_.chat.completions.list(
        limit=10,
        status="completed"
    )

    for request in requests.data:
        print(f"ID: {request.id}, Status: {request.status}")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    // List recent async requests
    const requests = await client.async.chat.completions.list({
      limit: 10,
      status: "completed"
    });

    requests.data.forEach(request => {
      console.log(`ID: ${request.id}, Status: ${request.status}`);
    });
    ```
  </Tab>
</Tabs>

## Advanced Usage

### Error Handling

Handle chat-specific errors:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    try {
      const completion = await client.chat.completions.create({
        messages: [{ role: "user", content: "What is AI?" }],
        model: "sonar",
        max_tokens: 50000  // Exceeds limit
      });
    } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
        console.error(`Invalid request parameters: ${error.message}`);
      } else if (error instanceof Perplexity.RateLimitError) {
        console.error("Rate limit exceeded, please retry later");
      } else if (error instanceof Perplexity.APIError) {
        console.error(`API error ${error.status}: ${error.message}`);
      }
    }
    ```
  </Tab>
</Tabs>

### Custom Instructions

Use system messages for consistent behavior:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    const systemPrompt = `You are an expert research assistant specializing in technology and science. 
    Always provide well-sourced, accurate information and cite your sources. 
    Format your responses with clear headings and bullet points when appropriate.`;

    const completion = await client.chat.completions.create({
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: "Explain quantum computing applications" }
      ],
      model: "sonar-pro"
    });
    ```
  </Tab>
</Tabs>

### Concurrent Operations

Handle multiple conversations efficiently:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
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
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    async function processQuestions(questions: string[]) {
      const tasks = questions.map(question =>
        client.chat.completions.create({
          messages: [{ role: "user", content: question }],
          model: "sonar-deep-research"
        })
      );
      
      const results = await Promise.all(tasks);
      return results.map(result => result.choices[0].message.content);
    }

    const questions = [
      "What is artificial intelligence?",
      "How does machine learning work?",
      "What are neural networks?"
    ];

    const answers = await processQuestions(questions);
    ```
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Use appropriate models">
    Choose the right model for your use case: `sonar` for general queries, `sonar-pro` for complex analysis, `sonar-reasoning` for analytical tasks.

    <Tabs>
      <Tab title="Python SDK">
        ```python  theme={null}
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
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript  theme={null}
        // For quick factual queries
        const simpleQuery = await client.chat.completions.create({
          messages: [{ role: "user", content: "What is the capital of France?" }],
          model: "sonar"
        });

        // For complex analysis
        const complexQuery = await client.chat.completions.create({
          messages: [{ role: "user", content: "Analyze the economic impact of AI on employment" }],
          model: "sonar-pro"
        });
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Implement streaming for long responses">
    Use streaming for better user experience with lengthy responses.

    <Tabs>
      <Tab title="Python SDK">
        ```python  theme={null}
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
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript  theme={null}
        async function streamResponse(query: string): Promise<string> {
          const stream = await client.chat.completions.create({
            messages: [{ role: "user", content: query }],
            model: "sonar",
            stream: true
          });
          
          let response = "";
          for await (const chunk of stream) {
            if (chunk.choices[0]?.delta?.content) {
              const content = chunk.choices[0].delta.content;
              process.stdout.write(content);
              response += content;
            }
          }
          
          return response;
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Handle rate limits gracefully">
    Implement exponential backoff for production applications.

    <Tabs>
      <Tab title="Python SDK">
        ```python  theme={null}
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
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript  theme={null}
        async function chatWithRetry(
          messages: Perplexity.ChatMessage[], 
          maxRetries: number = 3
        ): Promise<Perplexity.Chat.CompletionCreateResponse> {
          for (let attempt = 0; attempt < maxRetries; attempt++) {
            try {
              return await client.chat.completions.create({
                messages,
                model: "sonar"
              });
            } catch (error) {
              if (error instanceof Perplexity.RateLimitError && attempt < maxRetries - 1) {
                const delay = Math.pow(2, attempt) * 1000 + Math.random() * 1000;
                await new Promise(resolve => setTimeout(resolve, delay));
                continue;
              }
              throw error;
            }
          }
          throw new Error("Max retries exceeded");
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Optimize for specific use cases">
    Configure parameters based on your application's needs.

    <Tabs>
      <Tab title="Python SDK">
        ```python  theme={null}
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
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript  theme={null}
        // For factual Q&A
        const factualConfig = {
          temperature: 0.1,  // Low creativity for accuracy
          top_p: 0.9,
          search_recency_filter: "month" as const
        };

        // For creative writing
        const creativeConfig = {
          temperature: 0.8,  // Higher creativity
          top_p: 0.95,
          presence_penalty: 0.1,
          frequency_penalty: 0.1
        };

        // Usage
        const factualResponse = await client.chat.completions.create({
          messages: [{ role: "user", content: "What is the current inflation rate?" }],
          model: "sonar",
          ...factualConfig
        });
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Resources

* [The Perplexity SDK Guide](/guides/perplexity-sdk) - The Perplexity SDK guide
* [OpenAI Compatibility](/guides/chat-completions-guide) - OpenAI compatibility guide
* [Streaming Responses](/guides/streaming-responses) - Complete streaming guide with advanced patterns
* [API Reference - Chat Completions](/api-reference/chat-completions-post) - Chat Completions API Reference
* [API Reference - Async Chat Completions](/api-reference/async-chat-completions-post) - Async API Reference
* [Structured Outputs](/guides/structured-outputs) - Formatted response generation
