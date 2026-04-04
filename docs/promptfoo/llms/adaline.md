# Adaline Gateway

Adaline Gateway is a fully local production-grade Super SDK that provides a simple, unified, and powerful interface for calling 300+ LLMs.

- Adaline Gateway runs locally within Promptfoo, it is not a proxy.
- Adaline Gateway uses custom types for config/parameters, prompts, tools that will work across LLMs. This allows users to set up their Promptfoo config prompts, tests, assertions just once and have them work flawlessly across providers.

Read more about Adaline Gateway: [https://github.com/adaline/gateway](https://github.com/adaline/gateway)

## Installation

Adaline Gateway packages are optional dependencies. Install them before using Adaline Gateway:

```bash
npm install @adaline/anthropic@latest @adaline/azure@latest @adaline/gateway@latest @adaline/google@latest @adaline/groq@latest @adaline/open-router@latest @adaline/openai@latest @adaline/provider@latest @adaline/together-ai@latest @adaline/types@latest @adaline/vertex@latest
```

The packages are loaded dynamically at runtime, so they will only be loaded when you actually use a specific provider. This means that if you only use OpenAI, only the OpenAI-related packages will be loaded.

## Provider format

The Adaline Gateway provider (aka adaline) can be used within Promptfoo config using the following format:

```yaml
adaline:<provider_name>:<model_type>:<model_name>
```

`provider_name` can be any of the following with these model types supported:

| provider_name | chat models | embedding models |
| --- | --- | --- |
| openai | ✅ | ✅ |
| anthropic | ✅ | ❌ |
| google | ✅ | ❌ |
| vertex | ✅ | ✅ |
| azureopenai | ✅ | ✅ |
| groq | ✅ | ❌ |
| togetherai | ✅ | ❌ |
| openrouter | ✅ | ❌ |
| voyage | ❌ | ✅ |

`model_type` can be any of the following:

- `chat`
- `embedding`

Note: In case of `azureopenai` the `<model_name>` is the name of your Azure OpenAI model deployment. You specify your Azure resource name using `apiHost` in `config`, check Azure examples.

### Example

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:anthropic:chat:claude-3-sonnet-20240620
    config:
      tools: [
        {
          type: function,
          function: {
            schema: {
              name: "get_weather_from_location",
              description: "Get the current weather of a location",
              parameters: {
                type: "object",
                properties: {
                  location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                  },
                },
                required: ["location"],
              },
            },
          },
        },
      ]
tests:
  - vars:
      system_message: file:////system_message.txt
      previous_messages: [
        {
          user: Who founded Facebook?
          assistant: Mark Zuckerberg
        },
        {
          user: What's his favorite food?
          assistant: Pizza
        },
      ]
    assert:
      - type: is-json
        value: output[0].name === "get_weather_from_location"
      - type: is-valid-openai-tools-call
      - type: javascript
        value: output[0].function.name === "get_current_weather"
      - type: similar
        value: Paris, France
        threshold: 0.5
        transform: JSON.parse(output[0].function.arguments).location
  - vars:
      system_message: file:////system_message.txt
      previous_messages: [
        {
          user: Who founded Facebook?
          assistant: Mark Zuckerberg
        },
        {
          user: What's his favorite food?
          assistant: Pizza
        },
      ]
    options:
      transformVars: |-
        return { ...vars, image_markdown: `![image](${vars.url})` }
    assert:
      - type: contains
        value: boardwalk
```

### Using OpenAI format

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:openai:chat:gpt-5.2
    config:
      tools: [
        {
          type: function,
          function: {
            schema: {
              name: "get_current_weather",
              description: "Get the current weather in a given location",
              parameters: {
                type: "object",
                properties: {
                  location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                  },
                },
                required: ["location"],
              },
            },
          },
        },
      ]
tests:
  - vars:
      question: What is the weather like in {{city}}">
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "billing"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "negative"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) >= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.length > 0 && output.suggested_actions.some(action => action.action.toLowerCase().includes("refund"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about being charged twice?"
        metric: SummaryAccuracy
  - vars:
      question: How do I change my password? I can't find the option in my account settings.
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "technical_issue"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "neutral"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("password"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about changing their password?"
        metric: SummaryAccuracy
  - vars:
      question: I love your new feature! It's made my work so much easier. Any plans to expand on it?
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "feature_request"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "positive"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 2
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("feedback"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's positive feedback and interest in feature expansion?"
        metric: SummaryAccuracy
derivedMetrics:
  - name: OverallAccuracy
    value: "(CategoryAccuracy + SentimentAccuracy + UrgencyAccuracy + ActionRelevance + SummaryAccuracy) / 5"
  - name: ResponseQuality
    value: "(ValidJSON + OverallAccuracy) / 2"
```

### Multi provider comparison

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:openai:chat:gpt-5.2
  - id: adaline:anthropic:chat:claude-opus-4-1-20250805
  - id: adaline:google:chat:gemini-2.5-pro
tests:
  - vars:
      question: Do you think you can solve 1 + 0.5 + 0.25 + 0.125 + 0.0625 + 0.03125 + 0.015625 .... till 0?
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "billing"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "negative"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) >= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.length > 0 && output.suggested_actions.some(action => action.action.toLowerCase().includes("refund"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about being charged twice?"
        metric: SummaryAccuracy
  - vars:
      question: How do I change my password? I can't find the option in my account settings.
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "technical_issue"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "neutral"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("password"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about changing their password?"
        metric: SummaryAccuracy
  - vars:
      question: I love your new feature! It's made my work so much easier. Any plans to expand on it?
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "feature_request"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "positive"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 2
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("feedback"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's positive feedback and interest in feature expansion?"
        metric: SummaryAccuracy
derivedMetrics:
  - name: OverallAccuracy
    value: "(CategoryAccuracy + SentimentAccuracy + UrgencyAccuracy + ActionRelevance + SummaryAccuracy) / 5"
  - name: ResponseQuality
    value: "(ValidJSON + OverallAccuracy) / 2"
```

### Structured output

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:openai:chat:gpt-5.2
    config:
      seed: 322431
      responseFormat: json_schema
      responseSchema:
        name: customer_support_analysis
        strict: true
        description: "output schema for analysis of a customer support query"
        schema:
          type: object
          properties:
            query_summary:
              type: string
              description: "A brief summary of the customer's query"
            category:
              type: string
              enum: ["billing", "technical_issue", "product_inquiry", "complaint", "feature_request", "other"]
              description: "The main category of the customer's query"
            sentiment:
              type: string
              enum: ["positive", "neutral", "negative"]
              description: "The overall sentiment of the customer's query"
            urgency:
              type: string
              enum: ["1", "2", "3", "4", "5"]
              description: "The urgency level of the query, where 1 is lowest and 5 is highest"
            suggested_actions:
              type: array
              items:
                type: object
                properties:
                  action:
                    type: string
                    description: "A specific action to be taken"
                  priority:
                    type: string
                    enum: ["low", "medium", "high"]
                required: ["action", "priority"]
                additionalProperties: false
            estimated_resolution_time:
              type: string
              description: "Estimated time to resolve the query (e.g., '2 hours', '1 day')"
          required: ["query_summary", "category", "sentiment", "urgency", "suggested_actions", "estimated_resolution_time"]
          additionalProperties: false
tests:
  - vars:
      question: I've been charged twice for my subscription this month. Can you please refund the extra charge?
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "billing"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "negative"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) >= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("refund"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about being charged twice?"
        metric: SummaryAccuracy
  - vars:
      question: How do I change my password? I can't find the option in my account settings.
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "technical_issue"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "neutral"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 3
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("password"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's issue about changing their password?"
        metric: SummaryAccuracy
  - vars:
      question: I love your new feature! It's made my work so much easier. Any plans to expand on it?
    assert:
      - type: is-json
        metric: ValidJSON
      - type: javascript
        value: output.category === "feature_request"
        metric: CategoryAccuracy
      - type: javascript
        value: output.sentiment === "positive"
        metric: SentimentAccuracy
      - type: javascript
        value: parseInt(output.urgency) <= 2
        metric: UrgencyAccuracy
      - type: javascript
        value: output.suggested_actions.some(action => action.action.toLowerCase().includes("feedback"))
        metric: ActionRelevance
      - type: llm-rubric
        value: "Does the query summary accurately reflect the customer's positive feedback and interest in feature expansion?"
        metric: SummaryAccuracy
derivedMetrics:
  - name: OverallAccuracy
    value: "(CategoryAccuracy + SentimentAccuracy + UrgencyAccuracy + ActionRelevance + SummaryAccuracy) / 5"
  - name: ResponseQuality
    value: "(ValidJSON + OverallAccuracy) / 2"
```

### Vision

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:openai:chat:gpt-5.2
tests:
  - vars:
      question: What do you see?
      url: https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg
    options:
      transformVars: |-
        return { ...vars, image_markdown: `![image](${vars.url})` }
    assert:
      - type: contains
        value: boardwalk
```

```yaml
prompt.json
[{
  "role": "user",
  "content": [
    {
      "modality": "text",
      "value": "{{question}}"
    },
    {
      "modality": "image",
      "detail": "auto",
      "value": {
        "type": "url",
        "url": "{{url}}"
      }
    }
  ]
}]
```

### Embedding similarity

```yaml
promptfooconfig.yaml
prompts:
  - file:////prompt.json
providers:
  - id: adaline:anthropic:chat:claude-3-5-sonnet-20240620
    config:
      maxTokens: 120
defaultTest:
  vars:
    system_message: file:////system_message.txt
    previous_messages: [
      {
        user: Who founded Facebook?
        assistant: Mark Zuckerberg
      },
    ]
tests:
  - vars:
      question: What is his role at Internet.org?
    assert:
      - type: similar
        value: Founder and CEO
        threshold: 0.25
        provider: gateway:openai:embedding:text-embedding-3-large
  - vars:
      question: Is he still connected with Facebook?
    assert:
      - type: similar
        value: Yes
        threshold: 0.5
        provider: gateway:openai:embedding:text-embedding-3-small
```

```yaml
prompt.json
[{
  "role": "system",
  "content": [
    {
      "modality": "text",
      "value": {{ system_message | dump }}
    }
  ],
  {% for message in previous_messages %}
    {% for role, content in message %}
      {
        "role": "{{ role }}",
        "content": [
          {
            "modality": "text",
            "value": {{ content | dump }}
          }
        ]
      },
    {% endfor %}
  {% endfor %}
  {
    "role": "user",
    "content": [
      {
        "modality": "text",
        "value": {{ question | dump }}
      }
    ]
  }
}]
```

```yaml
system_message.txt
You are a helpful assistant. You answer extremely concisely.