# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/llm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Large Language Model (LLM)

> Learn how to use Tavus-optimized LLMs or integrate your own custom LLM.

The **LLM Layer** in Tavus enables your persona to generate intelligent, context-aware responses. You can use Tavus-hosted models or connect your own OpenAI-compatible LLM.

## Tavus-Hosted Models

### 1. `model`

Select one of the available models:

* `tavus-gpt-oss` (Recommended)
* `tavus-gpt-4o`
* `tavus-gpt-4o-mini`

<Note>
  **Context Window Limit**

  * All Tavus-hosted models have a **limit of 32,000 tokens**.
  * Contexts over **25,000 tokens** will experience noticeable performance degradation (slow response times).

  **Tip**: 1 token ≈ 4 characters, therefore 32,000 tokens ≈ 128,000 characters (including spaces and punctuation).
</Note>

```json  theme={null}
"model": "tavus-gpt-oss"
```

### 2. `tools`

Optionally enable tool calling by defining functions the LLM can invoke.

<Note>
  Please see [LLM Tool Calling](/sections/conversational-video-interface/persona/llm-tool) for more details.
</Note>

### 3. `speculative_inference`

When set to `true`, the LLM begins processing speech transcriptions before user input ends, improving responsiveness.

```json  theme={null}
"speculative_inference": true
```

<Note>
  This is field is optional, but recommended for better performance.
</Note>

### 4. `extra_body`

Add parameters to customize the LLM request. For Tavus-hosted models, you can pass `temperature` and `top_p`:

```json  theme={null}
"extra_body": {
  "temperature": 0.7,
  "top_p": 0.9
}
```

<Note>
  This field is optional.
</Note>

### Example Configuration

```json  theme={null}
{
  "persona_name": "Health Coach",
  "system_prompt": "You provide wellness tips and encouragement for people pursuing a healthy lifestyle.",
  "context": "You specialize in daily routines, diet advice, and motivational support.",
  "pipeline_mode": "full",
  "default_replica_id": "r665388ec672",
  "layers": {
    "llm": {
      "model": "tavus-gpt-4o",
      "speculative_inference": true,
      "extra_body": {
        "temperature": 0.7,
        "top_p": 0.9
      }
    }
  }
}
```

## Custom LLMs

### Prerequisites

To use your own OpenAI-compatible LLM, you'll need:

* Model name
* Base URL
* API key

Ensure your LLM:

* Streamable (ie. via SSE)
* Uses the `/chat/completions` endpoint

### 1. `model`

Name of the custom model you want to use.

```json  theme={null}
"model": "gpt-3.5-turbo"
```

### 2. `base_url`

Base URL of your LLM endpoint.

<Note>
  Do not include route extensions in the `base_url`.
</Note>

```json  theme={null}
"base_url": "https://your-llm.com/api/v1"
```

### 3. `api_key`

API key to authenticate with your LLM provider.

```json  theme={null}
"api_key": "your-api-key"
```

<Tip>
  `base_url` and `api_key` are required only when using a custom model.
</Tip>

### 4. `tools`

Optionally enable tool calling by defining functions the LLM can invoke.

<Note>
  Please see [LLM Tool Calling](/sections/conversational-video-interface/persona/llm-tool) for more details.
</Note>

### 5. `speculative_inference`

When set to `true`, the LLM begins processing speech transcriptions before user input ends, improving responsiveness.

```json  theme={null}
"speculative_inference": true
```

<Note>
  This is field is optional, but recommended for better performance.
</Note>

### 6. `headers`

Optional headers for authenticating with your LLM.

```json  theme={null}
"headers": {
  "Authorization": "Bearer your-api-key"
}
```

<Note>
  This field is optional, depending on your LLM model.
</Note>

### 7. `extra_body`

Add parameters to customize the LLM request. You can pass any parameters that your LLM provider supports:

```json  theme={null}
"extra_body": {
  "temperature": 0.5,
  "top_p": 0.9,
  "frequency_penalty": 0.5
}
```

<Note>
  This field is optional.
</Note>

### 8. `default_query`

Add default query parameters that get appended to the base URL when making requests to the `/chat/completions` endpoint.

```json  theme={null}
"default_query": {
  "api-version": "2024-02-15-preview"
}
```

<Note>
  This field is optional. Useful for LLM providers that require query parameters for authentication or versioning.
</Note>

### Example Configuration

```json  theme={null}
{
  "persona_name": "Storyteller",
  "system_prompt": "You are a storyteller who entertains people of all ages.",
  "context": "Your favorite stories include Little Red Riding Hood and The Three Little Pigs.",
  "pipeline_mode": "full",
  "default_replica_id": "r665388ec672",
  "layers": {
    "llm": {
      "model": "gpt-4o",
      "base_url": "https://your-azure-openai.openai.azure.com/openai/deployments/gpt-4o",
      "api_key": "your-api-key",
      "speculative_inference": true,
      "default_query": {
        "api-version": "2024-02-15-preview"
      }
    }
  }
}
```

<Note>
  Refer to the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for a full list of supported fields.
</Note>

### Perception

When using the `raven-0` perception model with a custom LLM, your LLM will receive system messages containing visual context extracted from the user's video input.

```json  theme={null}
{
    "role": "system",
    "content": "<user_appearance>...</user_appearance> <user_emotions>...</user_emotions> <user_screenshare>...</user_screenshare>"
}
```

#### Basic Perception model

If you use the Basic perception model, your LLM will receive the following user messages (instead of a system message):

```json  theme={null}
{
    "role": "user",
    "content": "USER_SPEECH: ... VISUAL_SCENE: ..."
}
```

#### Disabled Perception model

If you disable the perception model, your LLM will not receive any special messages.
