# Google AI / Gemini

The `google` provider enables integration with Google AI Studio and the Gemini API. It provides access to Google's state-of-the-art language models with support for text, images, and video inputs through Google AI Studio API for comprehensive multimodal LLM testing and evaluation.

If you are using Vertex AI instead of Google AI Studio, see the `vertex` provider documentation.

## Available Models

### Chat and Multimodal Models

- `google:gemini-3-flash-preview` - Gemini 3.0 Flash with frontier intelligence, Pro-grade reasoning at Flash-level speed, thinking, and grounding ($0.50/1M input, $3/1M output)
- `google:gemini-3-pro-preview` - Gemini 3.0 Pro with advanced reasoning and agentic capabilities
- `google:gemini-2.5-pro` - Gemini 2.5 Pro model with enhanced reasoning, coding, and multimodal understanding
- `google:gemini-2.5-flash` - Gemini 2.5 Flash model with enhanced reasoning and thinking capabilities
- `google:gemini-2.5-flash-lite` - Cost-efficient and fast model for high-volume, latency-sensitive tasks
- `google:gemini-2.0-flash` - Best for fast, efficient responses and general tasks

### Embedding Models

- `google:embedding:text-embedding-004` - Google text embedding model
- `google:embedding:embedding-001` - Google embedding model

### Image Generation Models

- `google:video:veo-3.1-generate-preview` - Latest Veo 3.1 model with video extension support
- `google:video:veo-3.1-fast-preview` - Fast Veo 3.1 model
- `google:video:veo-3-generate` - Veo 3.0 standard model
- `google:video:veo-3-fast` - Veo 3.0 fast model
- `google:video:veo-2-generate` - Veo 2.0 model

### Video Generation Models (Veo)

- `google:video:veo-3.1-generate-preview` - Latest Veo 3.1 model with video extension support
- `google:video:veo-3.1-fast-preview` - Fast Veo 3.1 model
- `google:video:veo-3-generate` - Veo 3.0 standard model
- `google:video:veo-3-fast` - Veo 3.0 fast model
- `google:video:veo-2-generate` - Veo 2.0 model

## Basic Configuration

The provider supports various configuration options that can be used to customize the behavior of the model:

### For all test cases using `defaultTest`:

```yaml
defaultTest:
  options:
    provider:
      text:
        id: google:gemini-2.0-flash
        config:
          temperature: 0.7
      embedding:
        id: google:embedding:text-embedding-004
```

### For individual assertions:

```yaml
assert:
  - type: similar
    value: Expected response
    threshold: 0.8
    provider:
      id: google:embedding:text-embedding-004
```

### For specific tests:

```yaml
tests:
  - vars:
      puzzle: What is 2 + 2?
    options:
      provider:
        text:
          id: google:gemini-2.0-flash
        embedding:
          id: google:embedding:text-embedding-004
    assert:
      - type: similar
        value: The answer is 4
```

## Function Calling

Enable your model to interact with external systems through defined functions:

```yaml
providers:
  - id: google:gemini-2.5-pro-preview-06-05
    config:
      tools:
        function_declarations:
          - name: get_weather
            description: Get current weather for a location
            parameters:
              type: object
              properties:
                location:
                  type: string
                  description: City name or coordinates
                units:
                  type: string
                  enum: ["celsius", "fahrenheit"]
              required: ["location"]
```

For practical examples of function calling with Google AI models, see the [google-vertex-tools example](https://github.com/promptfoo/promptfoo/tree/main/examples/google-vertex-tools) which demonstrates both basic tool declarations and callback execution patterns that work with Google AI Studio models.

## Structured Output

You can constrain the model to output structured JSON responses in two ways:

### 1. Using Response Schema Configuration

```yaml
providers:
  - id: google:gemini-2.5-pro-preview-06-05
    config:
      generationConfig:
        response_mime_type: application/json
        response_schema:
          type: object
          properties:
            title:
              type: string
            summary:
              type: string
            tags:
              type: array
              items:
                type: string
          required: ["title", "summary"]
```

### 2. Using Response Schema File

```yaml
providers:
  - id: google:gemini-2.5-pro-preview-06-05
    config:
      responseSchema: file://path/to/schema.json
```

For more details, see the [Gemini API documentation](https://ai.google.dev/docs/gemini_api/grounding).

## Search Grounding

Search grounding allows Gemini models to access the internet for up-to-date information, enhancing responses about recent events and real-time data.

### Basic Usage

To enable Search grounding:

```yaml
providers:
  - id: google:gemini-2.5-flash
    config:
      tools:
        - googleSearch: {}
```

### Combining with Other Features

You can combine Search grounding with thinking capabilities for better reasoning:

```yaml
providers:
  - id: google:gemini-2.5-pro-preview-06-05-05
    config:
      generationConfig:
        thinkingConfig:
          thinkingBudget: 1024
      tools:
        - googleSearch: {}
```

### Supported Models

Search grounding works with most recent Gemini models including:

- Gemini 2.5 Flash and Pro models
- Gemini 2.0 Flash and Pro models
- Gemini 1.5 Flash and Pro models

### Use Cases

Search grounding is particularly valuable for:

- Current events and news
- Recent developments
- Stock prices and market data
- Sports results
- Technical documentation updates

### Working with Response Metadata

When using Search grounding, the API response includes additional metadata:

- `groundingMetadata` - Contains information about search results used
- `groundingChunks` - Web sources that informed the response
- `webSearchQueries` - Queries used to retrieve information

### Limitations and Requirements

- Search results may vary by region and time
- Results may be subject to Google Search rate limits
- Search grounding may incur additional costs beyond normal API usage
- Search will only be performed when the model determines it's necessary
- **Important**: Per Google's requirements, applications using Search grounding must display Google Search Suggestions included in the API response metadata

For more details, see the [Google AI Studio documentation on Grounding with Google Search](https://ai.google.dev/docs/gemini_api/grounding).

## Code Execution

Code execution allows Gemini models to write and execute Python code to solve computational problems, perform calculations, and generate data visualizations.

### Basic Usage

To enable code execution:

```yaml
providers:
  - id: google:gemini-2.5-flash-preview-05-20
    config:
      tools:
        - codeExecution: {}
```

### Example Use Cases

Code execution is particularly valuable for:

- Mathematical computations and calculations
- Data analysis and visualization

For more details, see the [Google AI Studio documentation on Code Execution](https://ai.google.dev/gemini-api/docs/code-execution).

## URL Context

URL context allows Gemini models to extract and analyze content from web URLs, enabling them to understand and work with information from specific web pages.

### Basic Usage

To enable URL context:

```yaml
providers:
  - id: google:gemini-2.5-flash
    config:
      tools:
        - urlContext: {}
```

### Example Use Cases

URL context is particularly valuable for:

- Analyzing specific web page content
- Extracting information from documentation
- Comparing information across multiple URLs

For more details, see the [Google AI Studio documentation on URL Context](https://ai.google.dev/gemini-api/docs/url-context).

For complete working examples of the search grounding, code execution, and url context features, see the [google-aistudio-tools examples](https://github.com/promptfoo/promptfoo/tree/main/examples/google-aistudio-tools).

## Google Live API

Promptfoo now supports Google's WebSocket-based Live API, which enables low-latency bidirectional voice and video interactions with Gemini models. This API provides real-time interactive capabilities beyond what's available in the standard REST API.

### Using the Live Provider

Access the Google Live API by specifying the model with the `live` service type:

```yaml
providers:
  - id: google:live:gemini-2.0-flash-exp
    config:
      generationConfig:
        response_modalities: ["text"]
      timeoutMs: 10000
```

### Key Features

- **Real-time bidirectional communication**: Uses WebSockets for faster responses
- **Multimodal capabilities**: Can process text, audio, and video inputs
- **Built-in tools**: Supports function calling, code execution, and Google Search integration
- **Low-latency interactions**: Optimized for conversational applications
- **Session memory**: The model retains context throughout the session

### Function Calling Example

The Google Live API supports function calling, allowing you to define tools that the model can use:

```yaml
providers:
  - id: google:live:gemini-2.0-flash-exp
    config:
      tools: file://tools.json
      generationConfig:
        response_modalities: ["text"]
      timeoutMs: 10000
```

Where `tools.json` contains function declarations and built-in tools:

```json
[
  {
    "functionDeclarations": [
      {
        "name": "get_weather",
        "description": "Get current weather information for a city",
        "parameters": {
          "type": "OBJECT",
          "properties": {
            "city": {
              "type": "STRING",
              "description": "The name of the city to get weather for"
            }
          },
          "required": ["city"]
        }
      }
    ]
  },
  {
    "codeExecution": {}
  },
  {
    "googleSearch": {}
  }
]
```

### Built-in Tools

The Google Live API includes several built-in tools:

1. **Code Execution**: Execute Python code directly in the model's runtime

```yaml
{
  "codeExecution": {}
}
```

2. **Google Search**: Perform real-time web searches

```yaml
{
  "googleSearch": {}
}
```

### Audio Generation

Evaluate audio generation with the Google Live provider:

1. **Basic audio generation**

```yaml
providers:
  - id: google:live:gemini-2.0-flash-live-001
    config:
      generationConfig:
        response_modalities: ["audio"]
        outputAudioTranscription: {}
      speechConfig:
        voiceConfig:
          prebuiltVoiceConfig:
            voiceName: Charon
      timeoutMs: 30000
```

2. **Specifying additional options, such as enabling affective dialog**

```yaml
providers:
  - id: google:live:gemini-2.5-flash-exp-native-audio-thinking-dialog
    config:
      apiVersion: v1alpha
      generationConfig:
        response_modalities: ["audio"]
        enableAffectiveDialog: true
```

Other configuration options are available, such as setting proactive audio, setting the language code, and more. Read more about sending and receiving audio for Gemini in the [Google Live API documentation](https://ai.google.dev/gemini-api/docs/live-guide#send-receive-audio).

### Getting Started

Try the examples:

```sh
# Basic text-only example
promptfoo init --example google-live

# Function calling and tools example
promptfoo init --example google-live-tools

# Audio generation example
promptfoo init --example google-live-audio
```

### Limitations

- Sessions are limited to 15 minutes for audio or 2 minutes of audio and video
- Token counting is not supported
- Rate limits of 3 concurrent sessions per API key apply
- Maximum of 4M tokens per minute

For more details, see the [Google Live API documentation](https://ai.google.dev/gemini-api/docs/live).

## See Also

- [Vertex AI Provider](https://www.promptfoo.dev/docs/providers/vertex/) - For enterprise features and advanced Google AI capabilities
- [Google Examples](https://github.com/promptfoo/promptfoo/tree/main/examples) - Browse working examples for Google AI Studio
- [Gemini API Documentation](https://ai.google.dev/docs) - Official Google AI documentation
- [Configuration Reference](https://www.promptfoo.dev/docs/configuration/reference/) - Complete configuration options for promptfoo