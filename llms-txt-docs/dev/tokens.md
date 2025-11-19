# Source: https://dev.writer.com/home/tokens.md

# Understand tokens

Tokens are the atomic units that language models use to process text. Language models understand tokens rather than characters or bytes. Each token represents a single unit of meaning, like a word or a group of words.

The Writer API processes all text input and output in terms of tokens. See the maximum number of tokens for each model in the [models overview](/home/models) page.

## Tokenization

Tokenization is the process of breaking input text down into smaller units. Depending on the tokenization method the model uses, a single word can be represented by one token or may be broken down into multiple sub-word tokens.

Here's how different text types typically tokenize:

```python  theme={null}
"hello world"           → ["hello", " world"]           # 2 tokens
"API"                   → ["API"]                       # 1 token
"tokenization"          → ["token", "ization"]          # 2 tokens
"www.writer.com"        → ["www", "writer", "com"]      # 3 tokens
```

## Input and output token usage

Every API call consumes tokens for both the prompt you send and the response generated:

```python  theme={null}
# Example API call
response = client.chat.completions.create(
  model="palmyra-x5",
  messages=[
    {"role": "user", "content": "Write a product description for a cozy sweater"},  # ~8 tokens
  ],
  max_tokens=150,  # Maximum tokens to include in the response
)

# Total token usage = prompt tokens + response tokens
```

## Inspect token usage

You can inspect the [`usage`](/api-reference/completion-api/chat-completion#response-usage) information from the API response to see the token usage for each response.

<Info>
  The prompt tokens reported in the response include the tokens used for the model's system prompt.
</Info>

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.chat.chat(
    model="palmyra-x5",
    messages=[{"role": "user", "content": "Write a product description for a cozy sweater"}],
    max_tokens=150,
  )

  # Log token usage to understand patterns
  print(f"Prompt tokens: {response.usage.prompt_tokens}")
  print(f"Response tokens: {response.usage.completion_tokens}")
  print(f"Total tokens: {response.usage.total_tokens}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer()

  const response = await client.chat.chat({
    model: "palmyra-x5",
    messages: [
      { role: "user", content: "Write a product description for a cozy sweater" },
    ],
    maxTokens: 150,
  });

  // Log token usage to understand patterns
  console.log(`Prompt tokens: ${response.usage.prompt_tokens}`);
  console.log(`Response tokens: ${response.usage.completion_tokens}`);
  console.log(`Total tokens: ${response.usage.total_tokens}`);
  ```
</CodeGroup>

You can view your organization's overall token usage and spend in the [Consumption dashboard](/home/observability).
