# Source: https://js.langchain.com/v0.2/docs/integrations/text_embedding/jina/

Models - Docs by LangChain Skip to main content Docs by LangChain home page LangChain + LangGraph Search... ⌘ K
- Ask AI
- GitHub
- Try LangSmith
- Try LangSmith Search... Navigation Core components Models LangChain LangGraph Deep Agents Integrations Learn Reference Contribute
TypeScript

- Overview

##### Get started

- Install
- Quickstart
- Changelog
- Philosophy

##### Core components

- Agents
- Models
- Messages
- Tools
- Short-term memory
- Streaming
- Structured output

##### Middleware

- Overview
- Built-in middleware
- Custom middleware

##### Advanced usage

- Guardrails
- Runtime
- Context engineering
- Model Context Protocol (MCP)
- Human-in-the-loop
- Multi-agent
- Retrieval
- Long-term memory

##### Agent development

- LangSmith Studio
- Test
- Agent Chat UI

##### Deploy with LangSmith

- Deployment
- Observability On this page
- Basic usage
- Initialize a model
- Supported models
- Key methods
- Parameters
- Invocation
- Invoke
- Stream
- Batch
- Tool calling
- Structured output
- Advanced topics
- Model profiles
- Multimodal
- Reasoning
- Local models
- Prompt caching
- Server-side tool use
- Base URL or proxy
- Log probabilities
- Token usage
- Invocation config Core components

# Models Copy page Copy page LLMs are powerful AI tools that can interpret and generate text like humans. They’re versatile enough to write content, translate languages, summarize, and answer questions without needing specialized training for each task. In addition to text generation, many models support:

- Tool calling - calling external tools (like databases queries or API calls) and use results in their responses.
- Structured output - where the model’s response is constrained to follow a defined format.
- Multimodality - process and return data other than text, such as images, audio, and video.
- Reasoning - models perform multi-step reasoning to arrive at a conclusion. Models are the reasoning engine of agents . They drive the agent’s decision-making process, determining which tools to call, how to interpret results, and when to provide a final answer. The quality and capabilities of the model you choose directly impact your agent’s baseline reliability and performance. Different models excel at different tasks - some are better at following complex instructions, others at structured reasoning, and some support larger context windows for handling more information. LangChain’s standard model interfaces give you access to many different provider integrations, which makes it easy to experiment with and switch between models to find the best fit for your use case. For provider-specific integration information and capabilities, see the provider’s chat model page .

## ​ Basic usage Models can be utilized in two ways:

- With agents - Models can be dynamically specified when creating an agent .
- Standalone - Models can be called directly (outside of the agent loop) for tasks like text generation, classification, or extraction without the need for an agent framework. The same model interface works in both contexts, which gives you the flexibility to start simple and scale up to more complex agent-based workflows as needed.

### ​ Initialize a model The easiest way to get started with a standalone model in LangChain is to use `initChatModel `to initialize one from a chat model provider of your choice (examples below):

- OpenAI
- Anthropic
- Azure
- Google Gemini
- Bedrock Converse 👉 Read the OpenAI chat model integration docs npm pnpm yarn bun Copy

```text
`npm install @langchain/openai `
```

initChatModel Model Class Copy

```text
`import { initChatModel } from "langchain" ; process . env . OPENAI_API_KEY = "your-api-key" ; const model = await initChatModel ( "gpt-4.1" ); `
```

👉 Read the Anthropic chat model integration docs npm pnpm yarn pnpm Copy

```text
`npm install @langchain/anthropic `
```

initChatModel Model Class Copy

```text
`import { initChatModel } from "langchain" ; process . env . ANTHROPIC_API_KEY = "your-api-key" ; const model = await initChatModel ( "claude-sonnet-4-5-20250929" ); `
```

👉 Read the Azure chat model integration docs npm pnpm yarn bun Copy

```text
`npm install @langchain/azure `
```

initChatModel Model Class Copy

```text
`import { initChatModel } from "langchain" ; process . env . AZURE_OPENAI_API_KEY = "your-api-key" ; process . env . AZURE_OPENAI_ENDPOINT = "your-endpoint" ; process . env . OPENAI_API_VERSION = "your-api-version" ; const model = await initChatModel ( "azure_openai:gpt-4.1" ); `
```

👉 Read the Google GenAI chat model integration docs npm pnpm yarn bun Copy

```text
`npm install @langchain/google-genai `
```

initChatModel Model Class Copy

```text
`import { initChatModel } from "langchain" ; process . env . GOOGLE_API_KEY = "your-api-key" ; const model = await initChatModel ( "google-genai:gemini-2.5-flash-lite" ); `
```

👉 Read the AWS Bedrock chat model integration docs npm pnpm yarn bun Copy

```text
`npm install @langchain/aws `
```

initChatModel Model Class Copy

```text
`import { initChatModel } from "langchain" ; // Follow the steps here to configure your credentials: // https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html const model = await initChatModel ( "bedrock:gpt-4.1" ); `
```

Copy

```text
`const response = await model . invoke ( "Why do parrots talk?" ); `
```

See `initChatModel `for more detail, including information on how to pass model parameters .

### ​ Supported models LangChain supports all major model providers, including OpenAI, Anthropic, Google, Azure, AWS Bedrock, and more. Each provider offers a variety of models with different capabilities. For a full list of supported models in LangChain, see the integrations page .

### ​ Key methods

## Invoke The model takes messages as input and outputs messages after generating a complete response.

## Stream Invoke the model, but stream the output as it is generated in real-time.

## Batch Send multiple requests to a model in a batch for more efficient processing. In addition to chat models, LangChain provides support for other adjacent technologies, such as embedding models and vector stores. See the integrations page for details.

## ​ Parameters A chat model takes parameters that can be used to configure its behavior. The full set of supported parameters varies by model and provider, but standard ones include: ​ model string required The name or identifier of the specific model you want to use with a provider. You can also specify both the model and its provider in a single argument using the ’ : ’ format, for example, ‘openai:o1’. ​ apiKey string The key required for authenticating with the model’s provider. This is usually issued when you sign up for access to the model. Often accessed by setting an environment variable . ​ temperature number Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic. ​ maxTokens number Limits the total number of tokens in the response, effectively controlling how long the output can be. ​ timeout number The maximum time (in seconds) to wait for a response from the model before canceling the request. ​ maxRetries number The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits. Using `initChatModel `, pass these parameters as inline parameters: Initialize using model parameters Copy

```text
`const model = await initChatModel ( "claude-sonnet-4-5-20250929" , { temperature: 0.7 , timeout: 30 , max_tokens: 1000 } ) `
```

Each chat model integration may have additional params used to control provider-specific functionality. For example, `ChatOpenAI `has `use_responses_api `to dictate whether to use the OpenAI Responses or Completions API. To find all the parameters supported by a given chat model, head to the chat model integrations page.

## ​ Invocation A chat model must be invoked to generate an output. There are three primary invocation methods, each suited to different use cases.

### ​ Invoke The most straightforward way to call a model is to use `invoke() `with a single message or a list of messages. Single message Copy

```text
`const response = await model . invoke ( "Why do parrots have colorful feathers?" ); console . log ( response ); `
```

A list of messages can be provided to a chat model to represent conversation history. Each message has a role that models use to indicate who sent the message in the conversation. See the messages guide for more detail on roles, types, and content. Object format Copy

```text
`const conversation = [ { role: "system" , content: "You are a helpful assistant that translates English to French." }, { role: "user" , content: "Translate: I love programming." }, { role: "assistant" , content: "J'adore la programmation." }, { role: "user" , content: "Translate: I love building applications." }, ]; const response = await model . invoke ( conversation ); console . log ( response ); // AIMessage("J'adore créer des applications.") `
```

Message objects Copy

```text
`import { HumanMessage , AIMessage , SystemMessage } from "langchain" ; const conversation = [ new SystemMessage ( "You are a helpful assistant that translates English to French." ), new HumanMessage ( "Translate: I love programming." ), new AIMessage ( "J'adore la programmation." ), new HumanMessage ( "Translate: I love building applications." ), ]; const response = await model . invoke ( conversation ); console . log ( response ); // AIMessage("J'adore créer des applications.") `
```

If the return type of your invocation is a string, ensure that you are using a chat model as opposed to a LLM. Legacy, text-completion LLMs return strings directly. LangChain chat models are prefixed with “Chat”, e.g., `ChatOpenAI `(/oss/integrations/chat/openai).

### ​ Stream Most models can stream their output content while it is being generated. By displaying output progressively, streaming significantly improves user experience, particularly for longer responses. Calling `stream() `returns an iterator that yields output chunks as they are produced. You can use a loop to process each chunk in real-time: Basic text streaming Stream tool calls, reasoning, and other content Copy

```text
`const stream = await model . stream ( "Why do parrots have colorful feathers?" ); for await ( const chunk of stream ) { console . log ( chunk . text ) } `
```

As opposed to `invoke() `, which returns a single `AIMessage `after the model has finished generating its full response, `stream() `returns multiple `AIMessageChunk `objects, each containing a portion of the output text. Importantly, each chunk in a stream is designed to be gathered into a full message via summation: Construct AIMessage Copy

```text
`let full : AIMessageChunk | null = null ; for await ( const chunk of stream ) { full = full ? full . concat ( chunk ) : chunk ; console . log ( full . text ); } // The // The sky // The sky is // The sky is typically // The sky is typically blue // ... console . log ( full . contentBlocks ); // [{"type": "text", "text": "The sky is typically blue..."}] `
```

The resulting message can be treated the same as a message that was generated with `invoke() `– for example, it can be aggregated into a message history and passed back to the model as conversational context. Streaming only works if all steps in the program know how to process a stream of chunks. For instance, an application that isn’t streaming-capable would be one that needs to store the entire output in memory before it can be processed.
Advanced streaming topics

Streaming events
LangChain chat models can also stream semantic events using
[ `streamEvents() `][BaseChatModel.streamEvents]. This simplifies filtering based on event types and other metadata, and will aggregate the full message in the background. See below for an example. Copy

```text
`const stream = await model . streamEvents ( "Hello" ); for await ( const event of stream ) { if ( event . event === "on_chat_model_start" ) { console . log ( `Input: ${ event . data . input } ` ); } if ( event . event === "on_chat_model_stream" ) { console . log ( `Token: ${ event . data . chunk . text } ` ); } if ( event . event === "on_chat_model_end" ) { console . log ( `Full message: ${ event . data . output . text } ` ); } } `
```

Copy

```text
`Input: Hello Token: Hi Token:  there Token: ! Token:  How Token:  can Token:  I ... Full message: Hi there! How can I help today? `
```

See the `streamEvents() `reference for event types and other details.
"Auto-streaming" chat models
LangChain simplifies streaming from chat models by automatically enabling streaming mode in certain cases, even when you’re not explicitly calling the streaming methods. This is particularly useful when you use the non-streaming invoke method but still want to stream the entire application, including intermediate results from the chat model. In LangGraph agents , for example, you can call `model.invoke() `within nodes, but LangChain will automatically delegate to streaming if running in a streaming mode.

#### ​ How it works When you `invoke() `a chat model, LangChain will automatically switch to an internal streaming mode if it detects that you are trying to stream the overall application. The result of the invocation will be the same as far as the code that was using invoke is concerned; however, while the chat model is being streamed, LangChain will take care of invoking `on_llm_new_token `events in LangChain’s callback system. Callback events allow LangGraph `stream() `and `streamEvents() `to surface the chat model’s output in real-time.

### ​ Batch Batching a collection of independent requests to a model can significantly improve performance and reduce costs, as the processing can be done in parallel: Batch Copy

```text
`const responses = await model . batch ([ "Why do parrots have colorful feathers?" , "How do airplanes fly?" , "What is quantum computing?" , "Why do parrots have colorful feathers?" , "How do airplanes fly?" , "What is quantum computing?" , ]); for ( const response of responses ) { console . log ( response ); } `
```

When processing a large number of inputs using `batch() `, you may want to control the maximum number of parallel calls. This can be done by setting the `maxConcurrency `attribute in the `RunnableConfig `dictionary. Batch with max concurrency Copy

```text
`model . batch ( listOfInputs , { maxConcurrency: 5 , // Limit to 5 parallel calls } ) `
```

See the `RunnableConfig `reference for a full list of supported attributes. For more details on batching, see the reference .

## ​ Tool calling Models can request to call tools that perform tasks such as fetching data from a database, searching the web, or running code. Tools are pairings of:

- A schema, including the name of the tool, a description, and/or argument definitions (often a JSON schema)
- A function or coroutine to execute. You may hear the term “function calling”. We use this interchangeably with “tool calling”. Here’s the basic tool calling flow between a user and a model: To make tools that you have defined available for use by a model, you must bind them using `bindTools `. In subsequent invocations, the model can choose to call any of the bound tools as needed. Some model providers offer built-in tools that can be enabled via model or invocation parameters (e.g. `ChatOpenAI `, `ChatAnthropic `). Check the respective provider reference for details. See the tools guide for details and other options for creating tools. Binding user tools Copy

```text
`import { tool } from "langchain" ; import * as z from "zod" ; import { ChatOpenAI } from "@langchain/openai" ; const getWeather = tool ( ( input ) => `It's sunny in ${ input . location } .` , { name: "get_weather" , description: "Get the weather at a location." , schema: z . object ({ location: z . string (). describe ( "The location to get the weather for" ), }), }, ); const model = new ChatOpenAI ({ model: "gpt-4.1" }); const modelWithTools = model . bindTools ([ getWeather ]); const response = await modelWithTools . invoke ( "What's the weather like in Boston?" ); const toolCalls = response . tool_calls || []; for ( const tool_call of toolCalls ) { // View tool calls made by the model console . log ( `Tool: ${ tool_call . name } ` ); console . log ( `Args: ${ tool_call . args } ` ); } `
```

When binding user-defined tools, the model’s response includes a request to execute a tool. When using a model separately from an agent , it is up to you to execute the requested tool and return the result back to the model for use in subsequent reasoning. When using an agent , the agent loop will handle the tool execution loop for you. Below, we show some common ways you can use tool calling.
Tool execution loop
When a model returns tool calls, you need to execute the tools and pass the results back to the model. This creates a conversation loop where the model can use tool results to generate its final response. LangChain includes agent abstractions that handle this orchestration for you. Here’s a simple example of how to do this: Tool execution loop Copy

```text
`// Bind (potentially multiple) tools to the model const modelWithTools = model . bindTools ([ get_weather ]) // Step 1: Model generates tool calls const messages = [{ "role" : "user" , "content" : "What's the weather in Boston?" }] const ai_msg = await modelWithTools . invoke ( messages ) messages . push ( ai_msg ) // Step 2: Execute tools and collect results for ( const tool_call of ai_msg . tool_calls ) { // Execute the tool with the generated arguments const tool_result = await get_weather . invoke ( tool_call ) messages . push ( tool_result ) } // Step 3: Pass results back to model for final response const final_response = await modelWithTools . invoke ( messages ) console . log ( final_response . text ) // "The current weather in Boston is 72°F and sunny." `
```

Each `ToolMessage `returned by the tool includes a `tool_call_id `that matches the original tool call, helping the model correlate results with requests.
Forcing tool calls
By default, the model has the freedom to choose which bound tool to use based on the user’s input. However, you might want to force choosing a tool, ensuring the model uses either a particular tool or any tool from a given list: Force use of any tool Force use of specific tools Copy

```text
`const modelWithTools = model . bindTools ([ tool_1 ], { toolChoice: "any" }) `
```

Parallel tool calls
Many models support calling multiple tools in parallel when appropriate. This allows the model to gather information from different sources simultaneously. Parallel tool calls Copy

```text
`const modelWithTools = model . bind_tools ([ get_weather ]) const response = await modelWithTools . invoke ( "What's the weather in Boston and Tokyo?" ) // The model may generate multiple tool calls console . log ( response . tool_calls ) // [ //   { name: 'get_weather', args: { location: 'Boston' }, id: 'call_1' }, //   { name: 'get_time', args: { location: 'Tokyo' }, id: 'call_2' } // ] // Execute all tools (can be done in parallel with async) const results = [] for ( const tool_call of response . tool_calls || []) { if ( tool_call . name === 'get_weather' ) { const result = await get_weather . invoke ( tool_call ) results . push ( result ) } } `
```

The model intelligently determines when parallel execution is appropriate based on the independence of the requested operations. Most models supporting tool calling enable parallel tool calls by default. Some (including OpenAI and Anthropic ) allow you to disable this feature. To do this, set `parallel_tool_calls=False `: Copy

```text
`model.bind_tools([get_weather], parallel_tool_calls = False ) `
```

Streaming tool calls
When streaming responses, tool calls are progressively built through `ToolCallChunk `. This allows you to see tool calls as they’re being generated rather than waiting for the complete response. Streaming tool calls Copy

```text
`const stream = await modelWithTools . stream ( "What's the weather in Boston and Tokyo?" ) for await ( const chunk of stream ) { // Tool call chunks arrive progressively if ( chunk . tool_call_chunks ) { for ( const tool_chunk of chunk . tool_call_chunks ) { console . log ( `Tool: ${ tool_chunk . get ( 'name' , '' ) } ` ) console . log ( `Args: ${ tool_chunk . get ( 'args' , '' ) } ` ) } } } // Output: // Tool: get_weather // Args: // Tool: // Args: {"loc // Tool: // Args: ation": "BOS"} // Tool: get_time // Args: // Tool: // Args: {"timezone": "Tokyo"} `
```

You can accumulate chunks to build complete tool calls: Accumulate tool calls Copy

```text
`let full : AIMessageChunk | null = null const stream = await modelWithTools . stream ( "What's the weather in Boston?" ) for await ( const chunk of stream ) { full = full ? full . concat ( chunk ) : chunk console . log ( full . contentBlocks ) } `
```

## ​ Structured output Models can be requested to provide their response in a format matching a given schema. This is useful for ensuring the output can be easily parsed and used in subsequent processing. LangChain supports multiple schema types and methods for enforcing structured output. To learn about structured output, see Structured output .

- Zod
- JSON Schema A zod schema is the preferred method of defining an output schema. Note that when a zod schema is provided, the model output will also be validated against the schema using zod’s parse methods. Copy

```text
`import * as z from "zod" ; const Movie = z . object ({ title: z . string (). describe ( "The title of the movie" ), year: z . number (). describe ( "The year the movie was released" ), director: z . string (). describe ( "The director of the movie" ), rating: z . number (). describe ( "The movie's rating out of 10" ), }); const modelWithStructure = model . withStructuredOutput ( Movie ); const response = await modelWithStructure . invoke ( "Provide details about the movie Inception" ); console . log ( response ); // { //   title: "Inception", //   year: 2010, //   director: "Christopher Nolan", //   rating: 8.8, // } `
```

For maximum control or interoperability, you can provide a raw JSON Schema. Copy

```text
`const jsonSchema = { "title" : "Movie" , "description" : "A movie with details" , "type" : "object" , "properties" : { "title" : { "type" : "string" , "description" : "The title of the movie" , }, "year" : { "type" : "integer" , "description" : "The year the movie was released" , }, "director" : { "type" : "string" , "description" : "The director of the movie" , }, "rating" : { "type" : "number" , "description" : "The movie's rating out of 10" , }, }, "required" : [ "title" , "year" , "director" , "rating" ], } const modelWithStructure = model . withStructuredOutput ( jsonSchema , { method: "jsonSchema" }, ) const response = await modelWithStructure . invoke ( "Provide details about the movie Inception" ) console . log ( response ) // {'title': 'Inception', 'year': 2010, ...} `
```

Key considerations for structured output:
- Method parameter : Some providers support different methods ( `'jsonSchema' `, `'functionCalling' `, `'jsonMode' `)
- Include raw : Use `includeRaw: true `to get both the parsed output and the raw `AIMessage `
- Validation : Zod models provide automatic validation, while JSON Schema requires manual validation See your provider’s integration page for supported methods and configuration options.
Example: Message output alongside parsed structure
It can be useful to return the raw `AIMessage `object alongside the parsed representation to access response metadata such as token counts . To do this, set `include_raw=True `when calling `with_structured_output `: Copy

```text
`import * as z from "zod" ; const Movie = z . object ({ title: z . string (). describe ( "The title of the movie" ), year: z . number (). describe ( "The year the movie was released" ), director: z . string (). describe ( "The director of the movie" ), rating: z . number (). describe ( "The movie's rating out of 10" ), title: z . string (). describe ( "The title of the movie" ), year: z . number (). describe ( "The year the movie was released" ), director: z . string (). describe ( "The director of the movie" ), rating: z . number (). describe ( "The movie's rating out of 10" ), }); const modelWithStructure = model . withStructuredOutput ( Movie , { includeRaw: true }); const response = await modelWithStructure . invoke ( "Provide details about the movie Inception" ); console . log ( response ); // { //   raw: AIMessage { ... }, //   parsed: { title: "Inception", ... } // } `
```

Example: Nested structures
Schemas can be nested: Copy

```text
`import * as z from "zod" ; const Actor = z . object ({ name: str role : z . string (), }); const MovieDetails = z . object ({ title: z . string (), year: z . number (), cast: z . array ( Actor ), genres: z . array ( z . string ()), budget: z . number (). nullable (). describe ( "Budget in millions USD" ), }); const modelWithStructure = model . withStructuredOutput ( MovieDetails ); `
```

## ​ Advanced topics

### ​ Model profiles Model profiles require `langchain>=1.1 `. LangChain chat models can expose a dictionary of supported features and capabilities through a `.profile `property: Copy

```text
`model . profile ; // { //   maxInputTokens: 400000, //   imageInputs: true, //   reasoningOutput: true, //   toolCalling: true, //   ... // } `
```

Refer to the full set of fields in the API reference . Much of the model profile data is powered by the models.dev project, an open source initiative that provides model capability data. This data is augmented with additional fields for purposes of use with LangChain. These augmentations are kept aligned with the upstream project as it evolves. Model profile data allow applications to work around model capabilities dynamically. For example:
- Summarization middleware can trigger summarization based on a model’s context window size.
- Structured output strategies in `createAgent `can be inferred automatically (e.g., by checking support for native structured output features).
- Model inputs can be gated based on supported modalities and maximum input tokens.
Modify profile data
Model profile data can be changed if it is missing, stale, or incorrect. Option 1 (quick fix) You can instantiate a chat model with any valid profile: Copy

```text
`const customProfile = { maxInputTokens: 100_000 , toolCalling: true , structuredOutput: true , // ... }; const model = initChatModel ( "..." , { profile: customProfile }); `
```

Option 2 (fix data upstream) The primary source for the data is the models.dev project. These data are merged with additional fields and overrides in LangChain integration packages and are shipped with those packages. Model profile data can be updated through the following process:
- (If needed) update the source data at models.dev through a pull request to its repository on GitHub .
- (If needed) update additional fields and overrides in `langchain-<package>/profiles.toml `through a pull request to the LangChain integration package . Model profiles are a beta feature. The format of a profile is subject to change.

### ​ Multimodal Certain models can process and return non-textual data such as images, audio, and video. You can pass non-textual data to a model by providing content blocks . All LangChain chat models with underlying multimodal capabilities support:

- Data in the cross-provider standard format (see our messages guide )
- OpenAI chat completions format
- Any format that is native to that specific provider (e.g., Anthropic models accept Anthropic native format) See the multimodal section of the messages guide for details. Some models can return multimodal data as part of their response. If invoked to do so, the resulting `AIMessage `will have content blocks with multimodal types. Multimodal output Copy

```text
`const response = await model . invoke ( "Create a picture of a cat" ); console . log ( response . contentBlocks ); // [ //   { type: "text", text: "Here's a picture of a cat" }, //   { type: "image", data: "...", mimeType: "image/jpeg" }, // ] `
```

See the integrations page for details on specific providers.

### ​ Reasoning Many models are capable of performing multi-step reasoning to arrive at a conclusion. This involves breaking down complex problems into smaller, more manageable steps. If supported by the underlying model, you can surface this reasoning process to better understand how the model arrived at its final answer. Stream reasoning output Complete reasoning output Copy

```text
`const stream = model . stream ( "Why do parrots have colorful feathers?" ); for await ( const chunk of stream ) { const reasoningSteps = chunk . contentBlocks . filter ( b => b . type === "reasoning" ); console . log ( reasoningSteps . length > 0 ? reasoningSteps : chunk . text ); } `
```

Depending on the model, you can sometimes specify the level of effort it should put into reasoning. Similarly, you can request that the model turn off reasoning entirely. This may take the form of categorical “tiers” of reasoning (e.g., `'low' `or `'high' `) or integer token budgets. For details, see the integrations page or reference for your respective chat model.

### ​ Local models LangChain supports running models locally on your own hardware. This is useful for scenarios where either data privacy is critical, you want to invoke a custom model, or when you want to avoid the costs incurred when using a cloud-based model. Ollama is one of the easiest ways to run chat and embedding models locally.

### ​ Prompt caching Many providers offer prompt caching features to reduce latency and cost on repeat processing of the same tokens. These features can be implicit or explicit :

- Implicit prompt caching: providers will automatically pass on cost savings if a request hits a cache. Examples: OpenAI and Gemini .
- Explicit caching: providers allow you to manually indicate cache points for greater control or to guarantee cost savings. Examples:
- `ChatOpenAI `(via `prompt_cache_key `)
- Anthropic’s `AnthropicPromptCachingMiddleware `
- Gemini .
- AWS Bedrock Prompt caching is often only engaged above a minimum input token threshold. See provider pages for details. Cache usage will be reflected in the usage metadata of the model response.

### ​ Server-side tool use Some providers support server-side tool-calling loops: models can interact with web search, code interpreters, and other tools and analyze the results in a single conversational turn. If a model invokes a tool server-side, the content of the response message will include content representing the invocation and result of the tool. Accessing the content blocks of the response will return the server-side tool calls and results in a provider-agnostic format: Copy

```text
`import { initChatModel } from "langchain" ; const model = await initChatModel ( "gpt-4.1-mini" ); const modelWithTools = model . bindTools ([{ type: "web_search" }]) const message = await modelWithTools . invoke ( "What was a positive news story from today?" ); console . log ( message . contentBlocks ); `
```

This represents a single conversational turn; there are no associated ToolMessage objects that need to be passed in as in client-side tool-calling . See the integration page for your given provider for available tools and usage details.

### ​ Base URL or proxy For many chat model integrations, you can configure the base URL for API requests, which allows you to use model providers that have OpenAI-compatible APIs or to use a proxy server.

Base URL
Many model providers offer OpenAI-compatible APIs (e.g., Together AI , vLLM ). You can use `initChatModel `with these providers by specifying the appropriate `base_url `parameter: Copy

```text
`model = initChatModel( "MODEL_NAME" , { modelProvider: "openai" , baseUrl: "BASE_URL" , apiKey: "YOUR_API_KEY" , } ) `
```

When using direct chat model class instantiation, the parameter name may vary by provider. Check the respective reference for details.

### ​ Log probabilities Certain models can be configured to return token-level log probabilities representing the likelihood of a given token by setting the `logprobs `parameter when initializing the model: Copy

```text
`const model = new ChatOpenAI ({ model: "gpt-4.1" , logprobs: true , }); const responseMessage = await model . invoke ( "Why do parrots talk?" ); responseMessage . response_metadata . logprobs . content . slice ( 0 , 5 ); `
```

### ​ Token usage A number of model providers return token usage information as part of the invocation response. When available, this information will be included on the `AIMessage `objects produced by the corresponding model. For more details, see the messages guide. Some provider APIs, notably OpenAI and Azure OpenAI chat completions, require users opt-in to receiving token usage data in streaming contexts. See the streaming usage metadata section of the integration guide for details.

### ​ Invocation config When invoking a model, you can pass additional configuration through the `config `parameter using a `RunnableConfig `object. This provides run-time control over execution behavior, callbacks, and metadata tracking. Common configuration options include: Invocation with config Copy

```text
`const response = await model . invoke ( "Tell me a joke" , { runName: "joke_generation" , // Custom name for this run tags: [ "humor" , "demo" ], // Tags for categorization metadata: { "user_id" : "123" }, // Custom metadata callbacks: [ my_callback_handler ], // Callback handlers } ) `
```

These configuration values are particularly useful when:
- Debugging with LangSmith tracing
- Implementing custom logging or monitoring
- Controlling resource usage in production
- Tracking invocations across complex pipelines
Key configuration attributes
​ runName string Identifies this specific invocation in logs and traces. Not inherited by sub-calls. ​ tags string[] Labels inherited by all sub-calls for filtering and organization in debugging tools. ​ metadata object Custom key-value pairs for tracking additional context, inherited by all sub-calls. ​ maxConcurrency number Controls the maximum number of parallel calls when using `batch() `. ​ callbacks CallbackHandler[] Handlers for monitoring and responding to events during execution. ​ recursion_limit number Maximum recursion depth for chains to prevent infinite loops in complex pipelines. See full `RunnableConfig `reference for all supported attributes. Edit this page on GitHub or file an issue . Connect these docs to Claude, VSCode, and more via MCP for real-time answers.
Was this page helpful?
Yes No Agents Previous Messages Next ⌘ I Docs by LangChain home page github x linkedin youtube
Resources
Forum Changelog LangChain Academy Trust Center
Company
About Careers Blog github x linkedin youtube Powered by