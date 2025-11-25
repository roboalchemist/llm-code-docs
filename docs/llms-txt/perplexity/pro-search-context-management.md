# Source: https://docs.perplexity.ai/guides/pro-search-context-management.md

# Context Management

> Learn how to use threading and context management with Perplexity's sonar-pro model to maintain conversation continuity across multiple API calls.

## Overview

Context Management enables you to maintain conversation context across multiple API calls using Perplexity's advanced threading system. This feature is **exclusively available for the sonar-pro model** and allows for natural follow-up questions and contextual conversations.

<Info>
  Threading and context management features are only available with the `sonar-pro` model. Other models do not support these parameters.
</Info>

## How Threading Works

When you enable threading with `use_threads: true`, Perplexity creates a conversation thread that maintains context between API calls. You can then reference this thread in subsequent requests using the `thread_id` parameter, allowing the model to understand follow-up questions and maintain conversational continuity.

### Key Features

* **Automatic Context Preservation**: Previous messages and search results are retained across calls
* **Natural Follow-up Questions**: Ask clarifying questions without repeating context
* **Conversational Flow**: Build complex multi-turn conversations
* **Search Continuity**: References from previous searches remain available

## Basic Usage

### Starting a New Thread

Begin a conversation with threading enabled by setting `use_threads: true`:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --data '{
      "model": "sonar-pro",
      "use_threads": true,
      "messages": [
        {
          "role": "user",
          "content": "Which movie won the Cannes film festival special jury prize in 1996?"
        }
      ],
      "stream": false,
      "web_search_options": {
        "search_type": "pro"
      }
    }'
  ```

  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.perplexity.ai"
  )

  response = client.chat.completions.create(
      model="sonar-pro",
      use_threads=True,
      messages=[
          {
              "role": "user",
              "content": "Which movie won the Cannes film festival special jury prize in 1996?"
          }
      ],
      stream=False,
      web_search_options={
          "search_type": "pro"
      }
  )

  print("Response:", response.choices[0].message.content)
  print("Thread ID:", response.thread_id)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: "YOUR_API_KEY",
    baseURL: "https://api.perplexity.ai"
  });

  const response = await client.chat.completions.create({
    model: "sonar-pro",
    use_threads: true,
    messages: [
      {
        role: "user",
        content: "Which movie won the Cannes film festival special jury prize in 1996?"
      }
    ],
    stream: false,
    web_search_options: {
      search_type: "pro"
    }
  });

  console.log("Response:", response.choices[0].message.content);
  console.log("Thread ID:", response.thread_id);
  ```
</CodeGroup>

<ResponseExample>
  ```json  theme={null}
  {
    "id": "12345678-1234-1234-1234-123456789012",
    "object": "chat.completion",
    "created": 1641234567,
    "model": "sonar-pro",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "The movie that won the Cannes Film Festival Special Jury Prize in 1996 was \"Breaking the Waves\" directed by Lars von Trier. This Danish drama film starred Emily Watson and was notable for being von Trier's breakthrough film that helped establish him as a major international filmmaker..."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 45,
      "completion_tokens": 128,
      "total_tokens": 173
    },
    "thread_id": "3947452d-7cc0-48b3-afe7-d053c1083b78"
  }
  ```
</ResponseExample>

<Check>
  The response includes a `thread_id` field that you'll use for follow-up questions in the same conversational context.
</Check>

### Continuing a Thread

Use the `thread_id` from the initial response to ask follow-up questions:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --data '{
      "model": "sonar-pro",
      "use_threads": true,
      "thread_id": "3947452d-7cc0-48b3-afe7-d053c1083b78",
      "messages": [
        {
          "role": "user",
          "content": "What else has that director made?"
        }
      ],
      "stream": false,
      "web_search_options": {
        "search_type": "pro"
      }
    }'
  ```

  ```python Python theme={null}
  # Continue the conversation using the thread_id
  follow_up = client.chat.completions.create(
      model="sonar-pro",
      use_threads=True,
      thread_id="3947452d-7cc0-48b3-afe7-d053c1083b78",
      messages=[
          {
              "role": "user",
              "content": "What else has that director made?"
          }
      ],
      stream=False,
      web_search_options={
          "search_type": "pro"
      }
  )

  print("Follow-up Response:", follow_up.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  // Continue the conversation using the thread_id
  const followUp = await client.chat.completions.create({
    model: "sonar-pro",
    use_threads: true,
    thread_id: "3947452d-7cc0-48b3-afe7-d053c1083b78",
    messages: [
      {
        role: "user",
        content: "What else has that director made?"
      }
    ],
    stream: false,
    web_search_options: {
      search_type: "pro"
    }
  });

  console.log("Follow-up Response:", followUp.choices[0].message.content);
  ```
</CodeGroup>

<Info>
  Notice that the follow-up question "What else has that director made?" doesn't specify which director, but the model understands from the thread context that you're referring to Lars von Trier.
</Info>

## Advanced Usage

### Building Multi-Turn Conversations

You can continue building conversations by adding messages to the thread:

<CodeGroup>
  ```python Python theme={null}
  def threaded_conversation_example():
      client = OpenAI(
          api_key="YOUR_API_KEY",
          base_url="https://api.perplexity.ai"
      )
      
      # Start the conversation
      response1 = client.chat.completions.create(
          model="sonar-pro",
          use_threads=True,
          messages=[
              {
                  "role": "user", 
                  "content": "What are the latest developments in quantum computing in 2024?"
              }
          ],
          web_search_options={"search_type": "pro"}
      )
      
      thread_id = response1.thread_id
      print(f"Initial response: {response1.choices[0].message.content[:100]}...")
      
      # Ask a follow-up question
      response2 = client.chat.completions.create(
          model="sonar-pro",
          use_threads=True,
          thread_id=thread_id,
          messages=[
              {
                  "role": "user",
                  "content": "Which companies are leading in this field?"
              }
          ],
          web_search_options={"search_type": "pro"}
      )
      
      print(f"Follow-up response: {response2.choices[0].message.content[:100]}...")
      
      # Ask another related question
      response3 = client.chat.completions.create(
          model="sonar-pro",
          use_threads=True,
          thread_id=thread_id,
          messages=[
              {
                  "role": "user",
                  "content": "What are the main challenges they're facing?"
              }
          ],
          web_search_options={"search_type": "pro"}
      )
      
      print(f"Third response: {response3.choices[0].message.content[:100]}...")
      
      return thread_id

  # Run the conversation
  thread_id = threaded_conversation_example()
  ```

  ```typescript TypeScript theme={null}
  async function threadedConversationExample() {
    const client = new OpenAI({
      apiKey: "YOUR_API_KEY",
      baseURL: "https://api.perplexity.ai"
    });
    
    // Start the conversation
    const response1 = await client.chat.completions.create({
      model: "sonar-pro",
      use_threads: true,
      messages: [
        {
          role: "user",
          content: "What are the latest developments in quantum computing in 2024?"
        }
      ],
      web_search_options: { search_type: "pro" }
    });
    
    const threadId = response1.thread_id;
    console.log(`Initial response: ${response1.choices[0].message.content.substring(0, 100)}...`);
    
    // Ask a follow-up question
    const response2 = await client.chat.completions.create({
      model: "sonar-pro",
      use_threads: true,
      thread_id: threadId,
      messages: [
        {
          role: "user",
          content: "Which companies are leading in this field?"
        }
      ],
      web_search_options: { search_type: "pro" }
    });
    
    console.log(`Follow-up response: ${response2.choices[0].message.content.substring(0, 100)}...`);
    
    // Ask another related question
    const response3 = await client.chat.completions.create({
      model: "sonar-pro",
      use_threads: true,
      thread_id: threadId,
      messages: [
        {
          role: "user",
          content: "What are the main challenges they're facing?"
        }
      ],
      web_search_options: { search_type: "pro" }
    });
    
    console.log(`Third response: ${response3.choices[0].message.content.substring(0, 100)}...`);
    
    return threadId;
  }

  // Run the conversation
  const threadId = await threadedConversationExample();
  ```
</CodeGroup>

### Error Handling for Threads

Handle thread-specific errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  from openai import BadRequestError, NotFoundError

  client = OpenAI(
      api_key="YOUR_API_KEY",
      base_url="https://api.perplexity.ai"
  )

  def safe_threaded_request(thread_id=None, message_content=""):
      try:
          response = client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              thread_id=thread_id,  # May be None for new threads
              messages=[{"role": "user", "content": message_content}],
              web_search_options={"search_type": "pro"}
          )
          return response
          
      except BadRequestError as e:
          if "thread_id" in str(e):
              print("Invalid thread ID - starting new thread")
              # Start a new thread instead
              return client.chat.completions.create(
                  model="sonar-pro",
                  use_threads=True,
                  messages=[{"role": "user", "content": message_content}],
                  web_search_options={"search_type": "pro"}
              )
          else:
              raise
              
      except NotFoundError as e:
          print("Thread not found - starting new thread")
          return client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              messages=[{"role": "user", "content": message_content}],
              web_search_options={"search_type": "pro"}
          )

  # Example usage
  response = safe_threaded_request(
      thread_id="invalid-thread-id",
      message_content="What is machine learning?"
  )
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: "YOUR_API_KEY",
    baseURL: "https://api.perplexity.ai"
  });

  async function safeThreadedRequest(threadId?: string, messageContent: string = "") {
    try {
      return await client.chat.completions.create({
        model: "sonar-pro",
        use_threads: true,
        thread_id: threadId, // May be undefined for new threads
        messages: [{ role: "user", content: messageContent }],
        web_search_options: { search_type: "pro" }
      });
      
    } catch (error) {
      if (error instanceof OpenAI.BadRequestError && error.message.includes("thread_id")) {
        console.log("Invalid thread ID - starting new thread");
        // Start a new thread instead
        return client.chat.completions.create({
          model: "sonar-pro",
          use_threads: true,
          messages: [{ role: "user", content: messageContent }],
          web_search_options: { search_type: "pro" }
        });
      } else if (error instanceof OpenAI.NotFoundError) {
        console.log("Thread not found - starting new thread");
        return client.chat.completions.create({
          model: "sonar-pro",
          use_threads: true,
          messages: [{ role: "user", content: messageContent }],
          web_search_options: { search_type: "pro" }
        });
      } else {
        throw error;
      }
    }
  }

  // Example usage
  const response = await safeThreadedRequest(
    "invalid-thread-id",
    "What is machine learning?"
  );
  ```
</CodeGroup>

## Parameters Reference

### Required Parameters

<ParamField body="model" type="string" required>
  Must be set to `"sonar-pro"`. Threading is not available for other models.
</ParamField>

<ParamField body="use_threads" type="boolean" required>
  Set to `true` to enable threading functionality. When enabled, the response will include a `thread_id` for subsequent requests.
</ParamField>

<ParamField body="messages" type="array" required>
  Array of message objects in the standard chat format with `role` and `content` fields.
</ParamField>

### Optional Parameters

<ParamField body="thread_id" type="string">
  UUID string identifying an existing conversation thread. Omit this parameter to start a new thread. Include it to continue an existing conversation.
</ParamField>

<ParamField body="web_search_options" type="object">
  Configure search behavior within the thread. Commonly used with `{"search_type": "pro"}` for enhanced search capabilities.
</ParamField>

### Response Fields

<ResponseField name="thread_id" type="string">
  UUID identifying the conversation thread. Use this value in subsequent requests to maintain context.
</ResponseField>

<ResponseField name="choices[].message.content" type="string">
  The assistant's response, which includes context from previous messages in the thread.
</ResponseField>

## Best Practices

### Thread Management

<Steps>
  <Step title="Store Thread IDs Securely">
    Thread IDs are sensitive identifiers that provide access to conversation history. Store them securely and associate them with the appropriate users in your application.

    ```python  theme={null}
    # Example: Storing thread IDs with user sessions
    user_threads = {}

    def get_user_thread(user_id):
        return user_threads.get(user_id)

    def set_user_thread(user_id, thread_id):
        user_threads[user_id] = thread_id
    ```
  </Step>

  <Step title="Handle Thread Expiration">
    Threads may expire after extended periods of inactivity. Always handle cases where a thread\_id becomes invalid:

    ```python  theme={null}
    def resilient_chat(user_id, message):
        thread_id = get_user_thread(user_id)
        
        response = safe_threaded_request(thread_id, message)
        
        # Update stored thread ID if we got a new one
        if not thread_id or response.thread_id != thread_id:
            set_user_thread(user_id, response.thread_id)
        
        return response
    ```
  </Step>

  <Step title="Optimize for Context Length">
    While threads maintain context automatically, be mindful of context limits. For very long conversations, consider summarizing early parts of the conversation:

    <Tip>
      Threads automatically manage context, but extremely long conversations may hit context limits. The model will intelligently summarize or truncate older context as needed.
    </Tip>
  </Step>
</Steps>

### Performance Optimization

<AccordionGroup>
  <Accordion title="Managing Multiple Concurrent Threads">
    When handling multiple user conversations simultaneously:

    ```python  theme={null}
    import asyncio
    from concurrent.futures import ThreadPoolExecutor

    async def handle_multiple_conversations(conversations):
        """Handle multiple threaded conversations concurrently"""
        
        async def process_conversation(user_id, message, thread_id):
            response = await safe_threaded_request(thread_id, message)
            return user_id, response
        
        # Process conversations concurrently
        tasks = [
            process_conversation(conv['user_id'], conv['message'], conv['thread_id'])
            for conv in conversations
        ]
        
        results = await asyncio.gather(*tasks)
        return results
    ```
  </Accordion>

  <Accordion title="Thread Lifecycle Management">
    Implement proper thread lifecycle management:

    ```python  theme={null}
    class ThreadManager:
        def __init__(self):
            self.active_threads = {}
            self.thread_timestamps = {}
        
        def start_thread(self, user_id, initial_message):
            response = client.chat.completions.create(
                model="sonar-pro",
                use_threads=True,
                messages=[{"role": "user", "content": initial_message}],
                web_search_options={"search_type": "pro"}
            )
            
            thread_id = response.thread_id
            self.active_threads[user_id] = thread_id
            self.thread_timestamps[thread_id] = time.time()
            
            return response
        
        def continue_thread(self, user_id, message):
            thread_id = self.active_threads.get(user_id)
            if not thread_id:
                return self.start_thread(user_id, message)
            
            try:
                response = client.chat.completions.create(
                    model="sonar-pro",
                    use_threads=True,
                    thread_id=thread_id,
                    messages=[{"role": "user", "content": message}],
                    web_search_options={"search_type": "pro"}
                )
                
                # Update timestamp
                self.thread_timestamps[thread_id] = time.time()
                return response
                
            except (BadRequestError, NotFoundError):
                # Thread expired or invalid, start new one
                return self.start_thread(user_id, message)
        
        def cleanup_old_threads(self, max_age_hours=24):
            """Remove references to threads older than max_age_hours"""
            current_time = time.time()
            cutoff_time = current_time - (max_age_hours * 3600)
            
            expired_threads = [
                thread_id for thread_id, timestamp in self.thread_timestamps.items()
                if timestamp < cutoff_time
            ]
            
            for thread_id in expired_threads:
                # Find and remove user associations
                users_to_update = [
                    user_id for user_id, tid in self.active_threads.items()
                    if tid == thread_id
                ]
                
                for user_id in users_to_update:
                    del self.active_threads[user_id]
                
                del self.thread_timestamps[thread_id]
    ```
  </Accordion>
</AccordionGroup>

## Common Use Cases

### Research Assistant

Build a research assistant that maintains context across multiple queries:

<CodeGroup>
  ```python Python theme={null}
  class ResearchAssistant:
      def __init__(self, api_key):
          self.client = OpenAI(
              api_key=api_key,
              base_url="https://api.perplexity.ai"
          )
          self.current_thread = None
      
      def start_research(self, topic):
          """Start a new research session"""
          response = self.client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              messages=[
                  {
                      "role": "user",
                      "content": f"I'm researching {topic}. Can you provide an overview of the current state and recent developments?"
                  }
              ],
              web_search_options={"search_type": "pro"}
          )
          
          self.current_thread = response.thread_id
          return response.choices[0].message.content
      
      def ask_followup(self, question):
          """Ask a follow-up question in the current research context"""
          if not self.current_thread:
              raise ValueError("No active research session. Call start_research() first.")
          
          response = self.client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              thread_id=self.current_thread,
              messages=[{"role": "user", "content": question}],
              web_search_options={"search_type": "pro"}
          )
          
          return response.choices[0].message.content
      
      def deep_dive(self, aspect):
          """Deep dive into a specific aspect of the research topic"""
          return self.ask_followup(
              f"Can you provide more detailed information about {aspect}? "
              f"Include recent studies, key players, and future outlook."
          )

  # Example usage
  assistant = ResearchAssistant("YOUR_API_KEY")

  # Start research
  overview = assistant.start_research("quantum computing applications in cryptography")
  print("Research Overview:", overview)

  # Ask follow-up questions
  companies = assistant.ask_followup("Which companies are leading in this area?")
  print("Leading Companies:", companies)

  challenges = assistant.ask_followup("What are the main technical challenges?")
  print("Challenges:", challenges)

  # Deep dive into specific aspects
  timeline = assistant.deep_dive("implementation timeline and milestones")
  print("Timeline Analysis:", timeline)
  ```
</CodeGroup>

### Educational Q\&A System

Create an educational assistant that builds on previous explanations:

<CodeGroup>
  ```python Python theme={null}
  class EducationalAssistant:
      def __init__(self, api_key):
          self.client = OpenAI(
              api_key=api_key,
              base_url="https://api.perplexity.ai"
          )
          self.learning_threads = {}
      
      def start_lesson(self, student_id, subject):
          """Start a new learning session for a subject"""
          response = self.client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              messages=[
                  {
                      "role": "user",
                      "content": f"I want to learn about {subject}. Please start with the fundamentals and explain concepts clearly for a beginner."
                  }
              ],
              web_search_options={"search_type": "pro"}
          )
          
          self.learning_threads[student_id] = response.thread_id
          return response.choices[0].message.content
      
      def ask_question(self, student_id, question):
          """Ask a question in the context of the ongoing lesson"""
          thread_id = self.learning_threads.get(student_id)
          if not thread_id:
              raise ValueError("No active lesson for this student.")
          
          response = self.client.chat.completions.create(
              model="sonar-pro",
              use_threads=True,
              thread_id=thread_id,
              messages=[{"role": "user", "content": question}],
              web_search_options={"search_type": "pro"}
          )
          
          return response.choices[0].message.content
      
      def request_examples(self, student_id, concept):
          """Request examples for a specific concept"""
          return self.ask_question(
              student_id,
              f"Can you provide practical examples of {concept} that we've been discussing? "
              f"Please relate them to what we've already covered."
          )
      
      def check_understanding(self, student_id):
          """Ask the AI to check student's understanding based on the conversation"""
          return self.ask_question(
              student_id,
              "Based on our conversation so far, can you create a few questions to test my understanding? "
              "Please make them progressively more challenging."
          )

  # Example usage
  teacher = EducationalAssistant("YOUR_API_KEY")

  # Start learning about machine learning
  lesson_start = teacher.start_lesson("student_123", "machine learning basics")
  print("Lesson Introduction:", lesson_start)

  # Ask clarifying questions
  clarification = teacher.ask_question("student_123", "What's the difference between supervised and unsupervised learning?")
  print("Clarification:", clarification)

  # Request examples
  examples = teacher.request_examples("student_123", "supervised learning algorithms")
  print("Examples:", examples)

  # Check understanding
  quiz = teacher.check_understanding("student_123")
  print("Understanding Check:", quiz)
  ```
</CodeGroup>

## Troubleshooting

### Common Issues

<AccordionGroup>
  <Accordion title="Thread ID Not Found">
    **Problem**: Getting a "thread not found" error when using a previously valid thread ID.

    **Solution**: Threads may expire after extended periods of inactivity. Implement fallback logic to start a new thread:

    ```python  theme={null}
    def handle_expired_thread(thread_id, message):
        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                use_threads=True,
                thread_id=thread_id,
                messages=[{"role": "user", "content": message}],
                web_search_options={"search_type": "pro"}
            )
            return response
        except NotFoundError:
            # Thread expired, start a new one
            print("Previous thread expired, starting new conversation")
            return client.chat.completions.create(
                model="sonar-pro",
                use_threads=True,
                messages=[{"role": "user", "content": message}],
                web_search_options={"search_type": "pro"}
            )
    ```
  </Accordion>

  <Accordion title="Model Not Supported">
    **Problem**: Threading parameters are ignored or cause errors with other models.

    **Solution**: Threading is exclusively available for `sonar-pro`. Ensure you're using the correct model:

    ```python  theme={null}
    # ✅ Correct - threading supported
    response = client.chat.completions.create(
        model="sonar-pro",
        use_threads=True,
        messages=[{"role": "user", "content": "Hello"}]
    )

    # ❌ Incorrect - threading not supported
    response = client.chat.completions.create(
        model="sonar",  # Wrong model
        use_threads=True,
        messages=[{"role": "user", "content": "Hello"}]
    )
    ```
  </Accordion>

  <Accordion title="Context Length Limitations">
    **Problem**: Very long conversations may hit context limits.

    **Solution**: The model automatically manages context, but you can implement conversation summarization for extremely long threads:

    ```python  theme={null}
    def summarize_conversation(thread_id):
        """Request a summary of the conversation so far"""
        response = client.chat.completions.create(
            model="sonar-pro",
            use_threads=True,
            thread_id=thread_id,
            messages=[
                {
                    "role": "user",
                    "content": "Can you provide a concise summary of our conversation so far, highlighting the key points and conclusions?"
                }
            ]
        )
        return response.choices[0].message.content
    ```
  </Accordion>
</AccordionGroup>

<Warning>
  Always validate thread IDs before using them in production applications. Invalid or expired thread IDs will cause API errors that should be handled gracefully.
</Warning>

## Next Steps

Now that you understand context management with threading:

<CardGroup cols={2}>
  <Card title="Chat Completions Guide" icon="comments" href="/guides/chat-completions-guide">
    Learn more about the chat completions API and advanced features
  </Card>

  <Card title="Streaming Responses" icon="stream" href="/guides/streaming-responses">
    Implement real-time streaming with threaded conversations
  </Card>

  <Card title="Search Control" icon="magnifying-glass" href="/guides/search-control-guide">
    Fine-tune search behavior within your threaded conversations
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/chat-completions-post">
    Complete API documentation and parameter reference
  </Card>
</CardGroup>
