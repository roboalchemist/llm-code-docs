# Source: https://dev.writer.com/home/knowledge-graph-query-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Knowledge Graph query parameters

This guide shows you how to customize Knowledge Graph query behavior using the `query_config` parameter. You can tune search algorithms, control response grounding, adjust content retrieval, and enable inline citations to configure Knowledge Graph responses for your specific use cases.

## Overview

The `query_config` parameter allows you to fine-tune how Knowledge Graphs search, rank, and retrieve content. You can control the balance between keyword and semantic search, adjust how closely responses match source material, set relevance thresholds, and enable inline citations for source verification.

You can use this parameter with:

* **Chat completions** with [Knowledge Graph tools](/home/kg-chat)
* **Direct Knowledge Graph queries** via the [`/v1/graphs/question`](/home/kg-query) endpoint

## Example

Here's a chat completion example that demonstrates various query configuration parameters to configure Knowledge Graph responses:

* `grounding_level: 0.2`: keeps responses closely tied to source material (20% creative interpretation allowed)
* `search_weight: 60`: balances keyword and semantic search (60% keyword search, 40% semantic search)
* `keyword_threshold: 0.6`: requires 60% keyword match for content to be included
* `semantic_threshold: 0.8`: requires 80% semantic similarity for content to be included

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST 'https://api.writer.com/v1/chat' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "model": "palmyra-x5",
      "messages": [
        {
          "role": "user",
          "content": "What are the key features of our product?"
        }
      ],
      "tools": [
        {
          "type": "graph",
          "function": {
            "description": "Search company knowledge base",
            "graph_ids": ["<GRAPH_ID>"],
            "subqueries": true,
            "query_config": {
              "grounding_level": 0.2,
              "search_weight": 60,
              "keyword_threshold": 0.6,
              "semantic_threshold": 0.8,
              "inline_citations": true
            }
          }
        }
      ]
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client
  client = Writer()

  # Configure Knowledge Graph tool with query parameters
  tools = [{
      "type": "graph",
      "function": {
          "description": "Search company knowledge base",
          "graph_ids": ["<GRAPH_ID>"],
          "subqueries": True,
          "query_config": {
              "grounding_level": 0.2,
              "search_weight": 60,
              "keyword_threshold": 0.6,
              "semantic_threshold": 0.8,
              "inline_citations": True
          }
      }
  }]

  messages = [{"role": "user", "content": "What are the key features of our product?"}]

  response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Configure Knowledge Graph tool with query parameters
  const tools = [{
      type: "graph",
      function: {
          description: "Search company knowledge base",
          graph_ids: ["<GRAPH_ID>"],
          subqueries: true,
          query_config: {
              grounding_level: 0.2,
              search_weight: 60,
              keyword_threshold: 0.6,
              semantic_threshold: 0.8,
              inline_citations: true
          }
      }
  }];

  const messages = [{ role: "user", content: "What are the key features of our product?" }];

  const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools,
      tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Configure request parameters

| Name                 | Type    | Range              | Default | Description                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ------- | ------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_subquestions`   | Integer | 1-10               | 6       | Maximum number of sub-questions to generate when processing complex queries. Set higher to improve detail, set lower to reduce response time. See [Max sub-questions](#max-sub-questions) for details.                                                                                                                                                    |
| `search_weight`      | Integer | 0-100              | 50      | Controls the balance between keyword and semantic search in ranking results. See [Search weight](#search-weight) for details.                                                                                                                                                                                                                             |
| `grounding_level`    | Number  | 0.0-1.0            | 0.0     | Controls how closely responses must match to source material. Set lower for grounded outputs, higher for creativity. See [Grounding level](#grounding-level) for details.                                                                                                                                                                                 |
| `max_snippets`       | Integer | 5-25 (recommended) | 30      | Maximum number of text snippets to retrieve from the Knowledge Graph for context. Works in concert with `search_weight` to control best matches vs broader coverage. **Note**: While technically supports 1-60, values below 5 may return no results due to RAG implementation. Recommended range is 5-25. See [Max snippets](#max-snippets) for details. |
| `max_tokens`         | Integer | 100-8000           | 4000    | Maximum number of tokens the model can generate in the response. See [Max tokens](#max-tokens) for details.                                                                                                                                                                                                                                               |
| `keyword_threshold`  | Number  | 0.0-1.0            | 0.7     | Threshold for keyword-based matching when searching Knowledge Graph content. Set higher for stricter relevance, lower for broader range. See [Keyword threshold](#keyword-threshold) for details.                                                                                                                                                         |
| `semantic_threshold` | Number  | 0.0-1.0            | 0.7     | Threshold for semantic similarity matching when searching Knowledge Graph content. Set higher for stricter relevance, lower for broader range. See [Semantic threshold](#semantic-threshold) for details.                                                                                                                                                 |
| `inline_citations`   | Boolean | True/False         | False   | Whether to include inline citations within the response text. This is only available when making direct Knowledge Graph queries via the `/v1/graphs/question` endpoint. See [Work with inline citations in Knowledge Graph responses](/home/inline-citations) for details.                                                                                |

## Parameter details

### Inline citations

When you enable `inline_citations: true`, the response includes source references directly in the text as `[filename.pdf](cite_id)` links. These citations correspond to entries in the `references` array, allowing you to verify information and trace claims back to their origins.

**Key features**:

* **Source verification**: Each citation links to specific source material
* **Transparency**: Users can see exactly which sources support each claim
* **Traceability**: Citations include unique identifiers for programmatic processing

For detailed information about working with inline citations, see [Work with inline citations in Knowledge Graph responses](/home/inline-citations).

### Max sub-questions

Maximum number of sub-questions to generate when processing complex queries. Higher values allow the system to break down complex questions into more detailed sub-queries.

**How it works**:

* **Higher values**: Improve detail by generating more sub-questions for thorough analysis
* **Lower values**: Reduce response time by generating fewer sub-questions

**When to adjust**:

* **Increase** for complex, multi-part questions that need thorough analysis
* **Decrease** for simple, direct questions to reduce processing time

### Search weight

Controls the balance between keyword and semantic search in ranking results.

**How it works**:

* **Higher values (closer to 100)**: Prioritize keyword-based matching
* **Lower values (closer to 0)**: Prioritize semantic similarity matching

**When to adjust**:

* **Increase** for searches where exact keyword matches matter most
* **Decrease** for searches where conceptual similarity is more important

### Grounding level

Controls how closely responses must be tied to source material. This is different from typical LLM temperature parameters. It specifically controls grounding to Knowledge Graph sources.

**How it works**:

* **Higher values**: Higher creativity - allow more creative interpretation of source material
* **Lower values (closer to 0.0)**: Grounded outputs - stick closely to source material with minimal creativity

**Examples**:

* `0.0`: "According to the documentation, the API supports JSON responses" (direct quote/paraphrase)
* `0.5`: "The API documentation indicates that JSON responses are supported, which suggests additional capabilities" (interpretive)
* `1.0`: "Based on the available information, users can expect JSON responses, though other formats might be possible" (highly interpretive)

**When to adjust**:

* **Increase** for higher creativity when you want more interpretive responses
* **Decrease** for grounded outputs when factual reporting or accuracy is critical

### Max snippets

Maximum number of text snippets to retrieve from the Knowledge Graph for context. Works in concert with `search_weight` to control best matches vs broader coverage.

**How it works**:

* **Lower values (5-15)**: Best matches - retrieve fewer, more relevant snippets
* **Higher values (15-25)**: Broader coverage - retrieve more snippets for comprehensive context
* **Values below 5**: May return no results due to RAG implementation limitations

**Important notes**:

* **Recommended range**: 5-25 (default is 30, which is higher than recommended)
* **Edge case**: Due to RAG system behavior, you may see more snippets than requested. Use the recommended range unless you have a measured need to change it.

**When to adjust**:

* **Increase** for broader coverage when you need comprehensive research or more context
* **Decrease** for best matches when you want focused queries or concise results

### Max tokens

Maximum number of tokens the model can generate in the response. This controls the length of the AI's answer.

**How it works**:

* **Higher values**: Allow longer, more detailed responses
* **Lower values**: Generate shorter, more concise responses

**When to adjust**:

* **Increase** for detailed analysis or comprehensive answers
* **Decrease** for quick summaries or when you need faster responses

### Keyword threshold

Threshold for keyword-based matching when searching Knowledge Graph content.

**How it works**:

* **Higher values**: Stricter relevance - require stronger keyword matches
* **Lower values**: Broader range - allow more lenient keyword matching

**When to adjust**:

* **Increase** for stricter relevance when you want very precise keyword matches
* **Decrease** for broader range when you want to include content with related but not exact keywords

### Semantic threshold

Threshold for semantic similarity matching when searching Knowledge Graph content.

**How it works**:

* **Higher values**: Stricter relevance - require stronger semantic similarity
* **Lower values**: Broader range - allow more lenient semantic matching

**Examples**:

* `0.9`: Very strict - only content with high semantic similarity (for example, searching "user authentication" only finds content about "user authentication", "login", "sign-in")
* `0.7`: Moderate - includes conceptually related content (for example, searching "user authentication" finds "authentication", "security", "access control", "user management")
* `0.3`: Lenient - includes tangentially related content (for example, searching "user authentication" finds "authentication", "security", "user management", "database", "API", "web development")

**When to adjust**:

* **Increase** for stricter relevance when you want very semantically similar content
* **Decrease** for broader range when you want to include tangentially related content

## Parameter interactions and performance

### How parameters work together

Some parameters interact in ways that affect both results and performance:

* **`max_snippets` and `search_weight`**: Work together to control best matches vs broader coverage. `max_snippets` controls how many snippets are fed to the LLM in RAG.
* **`max_snippets` and `max_tokens`**: `max_snippets` controls input context size, while `max_tokens` controls output response length.
* **`keyword_threshold` and `semantic_threshold`**: Both filters are applied - content must pass both thresholds to be included.
* **Search weight and thresholds**: Higher thresholds reduce the candidate pool, then search weight determines the balance between keyword and semantic ranking of remaining results.

#### Search weight versus semantic threshold

These two parameters work at different stages of the search process:

* Semantic threshold is applied during the initial search phase, before ranking
* Search weight is applied after filtering, when ranking the remaining results

Semantic threshold acts as a gatekeeper that determines which content gets included, while search weight controls the balance between keyword and semantic scoring in final ranking.

**Example**: with `semantic_threshold = 0.8` and `search_weight = 30`, you get a small set of very relevant documents ranked more by semantic similarity than keyword matching.

### Performance considerations

* **Higher `max_tokens`**: Increases processing time and cost
* **Lower thresholds**: May return more results but with lower relevance
* **Higher `max_subquestions`**: Increases processing time for complex queries
* **`inline_citations: true`**: Minimal performance impact, slight increase in response size

### Recommended starting values

For most use cases, use the default values and adjust only if you need specific behavior. The defaults are designed to work well for general Knowledge Graph queries.

## Usage examples

### Chat completions with Knowledge Graph tool

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST 'https://api.writer.com/v1/chat' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "model": "palmyra-x5",
      "messages": [
        {
          "role": "user",
          "content": "What are the key features of our product?"
        }
      ],
      "tools": [
        {
          "type": "graph",
          "function": {
            "description": "Search company knowledge base",
            "graph_ids": ["<GRAPH_ID>"],
            "subqueries": true,
            "query_config": {
              "grounding_level": 0.2,
              "search_weight": 60,
              "keyword_threshold": 0.6,
              "semantic_threshold": 0.8,
              "inline_citations": true
            }
          }
        }
      ]
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client
  client = Writer()

  # Configure Knowledge Graph tool with query parameters
  tools = [{
      "type": "graph",
      "function": {
          "description": "Search company knowledge base",
          "graph_ids": ["<GRAPH_ID>"],
          "subqueries": True,
          "query_config": {
              "grounding_level": 0.2,
              "search_weight": 60,
              "keyword_threshold": 0.6,
              "semantic_threshold": 0.8,
              "inline_citations": True
          }
      }
  }]

  messages = [{"role": "user", "content": "What are the key features of our product?"}]

  response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Configure Knowledge Graph tool with query parameters
  const tools = [{
      type: "graph",
      function: {
          description: "Search company knowledge base",
          graph_ids: ["<GRAPH_ID>"],
          subqueries: true,
          query_config: {
              grounding_level: 0.2,
              search_weight: 60,
              keyword_threshold: 0.6,
              semantic_threshold: 0.8,
              inline_citations: true
          }
      }
  }];

  const messages = [{ role: "user", content: "What are the key features of our product?" }];

  const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools,
      tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

### Direct Knowledge Graph query

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST 'https://api.writer.com/v1/graphs/question' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "graph_ids": ["<GRAPH_ID>"],
      "question": "What are the key features of our product?",
      "query_config": {
        "grounding_level": 0.2,
        "keyword_threshold": 0.6,
        "semantic_threshold": 0.8,
        "inline_citations": true
      }
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client
  client = Writer()

  # Query Knowledge Graph with configuration parameters
  response = client.graphs.question(
      graph_ids=["<GRAPH_ID>"],
      question="What are the key features of our product?",
      query_config={
          "grounding_level": 0.2,
          "keyword_threshold": 0.6,
          "semantic_threshold": 0.8,
          "inline_citations": True
      }
  )

  print(f"Answer: {response.answer}")
  print(f"References: {response.references}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Query Knowledge Graph with configuration parameters
  const response = await client.graphs.question({
      graph_ids: ["<GRAPH_ID>"],
      question: "What are the key features of our product?",
      query_config: {
          grounding_level: 0.2,
          keyword_threshold: 0.6,
          semantic_threshold: 0.8,
          inline_citations: true
      }
  });

  console.log(`Answer: ${response.answer}`);
  console.log(`References: ${response.references}`);
  ```
</CodeGroup>

## Common configuration patterns

### Research and analysis

Use this configuration for comprehensive research tasks where you need thorough analysis with source verification. Higher sub-questions and snippets provide more context, while inline citations help track sources.

```json  theme={null}
{
  "max_subquestions": 8,
  "search_weight": 60,
  "grounding_level": 0.1,
  "max_snippets": 50,
  "max_tokens": 7000,
  "keyword_threshold": 0.6,
  "semantic_threshold": 0.7,
  "inline_citations": true
}
```

### Quick answers

Use this configuration for fast, focused responses where speed and precision matter more than comprehensive analysis. Strict thresholds ensure high relevance with minimal processing time.

```json  theme={null}
{
  "max_subquestions": 3,
  "search_weight": 80,
  "grounding_level": 0.0,
  "max_snippets": 15,
  "max_tokens": 2000,
  "keyword_threshold": 0.8,
  "semantic_threshold": 0.8,
  "inline_citations": false
}
```

### Creative content generation

Use this configuration when you want the AI to interpret and build upon source material creatively. Lower thresholds allow more diverse content, while higher grounding level enables interpretive responses.

```json  theme={null}
{
  "max_subquestions": 6,
  "search_weight": 40,
  "grounding_level": 0.6,
  "max_snippets": 30,
  "max_tokens": 5000,
  "keyword_threshold": 0.5,
  "semantic_threshold": 0.6,
  "inline_citations": false
}
```

## Best practices

1. **Start with defaults**: Begin with the default configuration and adjust based on your specific needs
2. **Test incrementally**: Change one parameter at a time to understand its effect
3. **Consider your use case**: Different applications, like research, Q\&A, and content generation, benefit from different configurations
4. **Monitor performance**: Track how different configurations affect response quality and processing time
5. **Balance precision and recall**: Higher thresholds give more precise results but may miss relevant content

## Next steps

* Learn how to [work with inline citations](/home/inline-citations) for source verification and traceability
* Explore [Knowledge Graph tools](/home/kg-chat) for chat completions
* Check out [direct Knowledge Graph queries](/home/kg-query) for programmatic access
* See [Knowledge Graph management](/home/knowledge-graph) for creating and organizing your graphs
