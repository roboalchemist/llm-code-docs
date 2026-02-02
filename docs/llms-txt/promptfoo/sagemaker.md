# Amazon SageMaker AI

The `sagemaker` provider allows you to use Amazon SageMaker AI endpoints in your evals. This enables testing and evaluation of any model deployed on SageMaker AI, including models from Hugging Face, custom-trained models, foundation models from Amazon SageMaker JumpStart, and more. For AWS-managed foundation models without custom endpoints, you might also consider the [AWS Bedrock provider](/docs/providers/aws-bedrock/).

## Setup

1. Ensure you have deployed the desired models as SageMaker AI endpoints.
2. Install the `@aws-sdk/client-sagemaker-runtime` package:
    ```bash
    npm install @aws-sdk/client-sagemaker-runtime
    ```
3. The AWS SDK will automatically pull credentials from the following locations:
    - IAM roles on EC2, Lambda, or SageMaker Studio
    - `~/.aws/credentials` or `~/.aws/config` files
    - `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables
    - Edit your configuration file to point to the SageMaker provider. Here's an example:
        ```yaml
        providers:
          - id: sagemaker:my-sagemaker-endpoint
            config:
              accessKeyId: YOUR_ACCESS_KEY_ID
              secretAccessKey: YOUR_SECRET_ACCESS_KEY
              region: us-east-1
              modelType: jumpstart
              maxTokens: 256
              temperature: 0.7
              maxRetries: 3
        ```
4. Additional config parameters are passed like so:
    ```yaml
    providers:
      - id: sagemaker:my-sagemaker-endpoint
        config:
          region: us-east-1
          modelType: huggingface
          temperature: 0.7
          maxTokens: 256
          topP: 0.9
          contentType: application/json
          acceptType: application/json
          responseFormat:
            path: json-generated_text
    ```
5. The SageMaker provider supports several syntax patterns:
    1. Basic endpoint specification:
        ```yaml
        sagemaker: my-endpoint-name
        ```
    2. Model type specification (for common model formats):
        ```yaml
        sagemaker:model-type:endpoint-name
        ```
        This specifies a format handler to properly structure requests and parse responses for the model container type deployed on your endpoint.
        ```yaml
        providers:
          - id: sagemaker:my-sagemaker-endpoint
            config:
              region: us-east-1
              modelType: jumpstart
              temperature: 0.7
              maxTokens: 256
              topP: 0.9
              contentType: application/json
              acceptType: application/json
              responseFormat:
                path: json-generated_text
        ```
    3. Embedding endpoint specification:
        ```yaml
        sagemaker: embedding: my-embedding-endpoint
        ```
        For endpoints that generate embeddings rather than text completions.
        ```yaml
        providers:
          - id: sagemaker:my-sagemaker-endpoint
            config:
              region: us-east-1
              modelType: huggingface
              temperature: 0.7
              maxTokens: 256
              topP: 0.9
              contentType: application/json
              acceptType: application/json
              responseFormat:
                path: json-generated_text
        ```
    4. JumpStart model specification:
        ```yaml
        sagemaker: jumpstart: my-jumpstart-endpoint
        ```
        For AWS JumpStart foundation models that require specific input/output formats.
        ```yaml
        providers:
          - id: sagemaker:my-sagemaker-endpoint
            config:
              region: us-east-1
              modelType: huggingface
              temperature: 0.7
              maxTokens: 256
              topP: 0.9
              contentType: application/json
              acceptType: application/json
              responseFormat:
                path: json-generated_text
        ```

The provider will auto-detect JumpStart endpoints if `jumpstart` is in the name, but manual `modelType` specification is recommended for clarity.

## Model Types

The SageMaker provider supports various model types to properly format requests and parse responses. Specify the model type in the provider ID or in the configuration:

```yaml
providers:
  - id: sagemaker:my-sagemaker-endpoint
    config:
      modelType: custom
```

Supported model types:

| Model Type | Description | JavaScript Expression for Results |
| --- | --- | --- |
| `llama` | Llama-compatible interface models | Standard format |
| `huggingface` | Hugging Face models (like Mistral) | `json[0].generated_text` |
| `jumpstart` | AWS JumpStart foundation models | `json-generated_text` |
| `custom` | Custom model formats (default) | Depends on model |

### Important clarification about model types

The `modelType` setting helps format requests and responses according to specific patterns expected by different model containers deployed on SageMaker.

Different model types return results in different response formats. Configure the appropriate JavaScript expression for extraction:

- **JumpStart models** (Llama): Use `responseFormat.path: "json-generated_text"` for JSON payloads.
- **Hugging Face models** (Mistral): Use `responseFormat.path: "json[0].generated_text"` for JSON responses.

For more complex extraction logic, use a file-based transformer:

```yaml
providers:
  - id: sagemaker:my-sagemaker-endpoint
    config:
      responseFormat:
        path: file://transforms/extract-baseball-info.js
```

See the [Response Path Expressions](#response-path-expressions) section for more details on using JavaScript expressions and file-based transformers.

## Input/Output Format

SageMaker endpoints expect the request in the format that the model container was designed for. For most text-generation models (e.g., Hugging Face Transformers or JumpStart LLMs), this means sending a JSON payload with an `inputs` key (and optional `parameters` for generation settings).

For example:

- A Hugging Face LLM container typically expects: `{ "inputs": "your prompt", "parameters": {...}}`
- A JumpStart model expects a similar structure, often returning `{ "generated_text": "the output"}`

The provider's `modelType` setting will try to format the request appropriately, but ensure your input matches what the model expects. You can provide a custom transformer if needed (see [Transforming Prompts](#transforming-prompts)).

## Configuration Options

Common configuration options for SageMaker endpoints:

| Option | Description | Default |
| --- | --- | --- |
| `endpoint` | SageMaker endpoint name | (from provider ID) |
| `region` | AWS region | `us-east-1` |
| `modelType` | Model type for request/response formatting | `custom` |
| `maxTokens` | Maximum number of tokens to generate | `1024` |
| `temperature` | Controls randomness (0.0 to 1.0) | `0.7` |
| `topP` | Nucleus sampling parameter | `1.0` |
| `stopSequences` | Array of sequences where generation stops | `[]` |
| `contentType` | Content type for SageMaker request | `application/json` |
| `acceptType` | Accept type for SageMaker response | `application/json` |
| `delay` | Delay between API calls in milliseconds | `0` |
| `transform` | Function to transform prompts before sending | N/A |

### Stop Sequences Example

```yaml
providers:
  - id: sagemaker:jumpstart:my-llama-endpoint
    config:
      region: us-east-1
      maxTokens: 100
      stopSequences: ["\nHuman:", "<|endoftext|>"]
```

These will be passed to the model (if supported) to halt generation when encountered. For instance, JumpStart Hugging Face LLM containers accept a `stop` parameter as a list of strings.

## Content Type and Accept Headers

Ensure the `contentType` and `acceptType` match your model's expectations:

- For most LLM endpoints, use `application/json` (the default)
- If your model consumes raw text or returns plain text, use `text/plain`

The default is JSON because popular SageMaker LLM containers (Hugging Face, JumpStart) use JSON payloads. If your endpoint returns a non-JSON response, you may need to adjust these settings accordingly.

## Response Parsing with JavaScript Expressions

For endpoints with unique response formats, you can use JavaScript expressions to extract specific fields from the response:

```yaml
providers:
  - id: sagemaker:my-custom-endpoint
    config:
      responseFormat:
        path: json.custom.nested.responseField
```

This will extract the value at the specified path from the JSON response using JavaScript property access. The JSON response is available as the `json` variable in your expression.

For more complex parsing needs, you can use a file-based transformer:

```yaml
providers:
  - id: sagemaker:my-custom-endpoint
    config:
      responseFormat:
        path: file://transformers/custom-parser.js
```

See the [Response Path Expressions](#response-path-expressions) section for more details on using JavaScript expressions and file-based transformers.

## Embeddings

To use SageMaker embedding endpoints:

```yaml
providers:
  - id: sagemaker:embedding:my-embedding-endpoint
    config:
      region: us-east-1
      modelType: huggingface
```

When using an embedding endpoint, the request should typically be formatted similarly to a text model (JSON with an `inputs` string). Ensure your SageMaker container returns embeddings in a JSON format (e.g., a list of floats). For example, a Hugging Face sentence-transformer model will output a JSON array of embeddings.

If the model returns a specific structure, you may need to specify a path:

```yaml
providers:
  - id: sagemaker:embedding:my-embedding-endpoint
    config:
      region: us-west-2
      contentType: application/json
      acceptType: application/json
      responseFormat:
        path: json.embedding
```

Or if it returns a raw array:

```yaml
responseFormat:
  path: json[0] # first element of the returned array
```

The `embedding:` prefix tells Promptfoo to treat the output as an embedding vector rather than text. This is useful for similarity metrics. You should deploy an embedding model to SageMaker that outputs numerical vectors.

For assertions that require embeddings (like similarity comparisons), you can specify a SageMaker embedding provider:

```yaml
defaultTest:
  options:
    provider:
      embedding:
        id: sagemaker:embedding:my-embedding-endpoint
        config:
          region: us-east-1
```

## Environment Variables

Promptfoo will also read certain environment variables to set default generation parameters:

- `AWS_REGION` or `AWS_DEFAULT_REGION`: Default region for SageMaker API calls
- `AWS_SAGEMAKER_MAX_TOKENS`: Default maximum number of tokens to generate
- `AWS_SAGEMAKER_TEMPERATURE`: Default temperature for generation
- `AWS_SAGEMAKER_TOP_P`: Default top_p value for generation
- `AWS_SAGEMAKER_MAX_RETRIES`: Number of retry attempts for failed API calls (default: 3)

These serve as global defaults for your eval runs. You can use them to avoid repetition in config files. Any values set in the provider's YAML config will override these environment defaults.

## Caching Support

The SageMaker provider fully supports the promptfoo caching system, which can significantly speed up evaluations and reduce costs when running repeated tests:

```yaml
# Caching is enabled by default. To explicitly configure it:
evaluateOptions:
  cache: true

providers:
  - id: sagemaker:my-endpoint
    config:
      region: us-east-1
```

When caching is enabled:

- Responses for identical prompts are stored and reused
- Token usage statistics are maintained with a `cached` flag
- Debug mode will bypass the cache when needed

Caching is enabled by default. To disable caching for specific test runs:

```bash
promptfoo eval --no-cache
```

## Rate Limiting with Delays

SageMaker endpoints will process requests as fast as the underlying instance allows. If you send too many requests in rapid succession, you may saturate the endpoint's capacity and get latency spikes or errors. To avoid this, you can configure a delay between calls.

For example, `delay: 1000` will wait 1 second between each request to the endpoint. This is especially useful to prevent hitting concurrency limits on your model or to avoid invoking autoscaling too aggressively.

```yaml
providers:
  - id: sagemaker:my-endpoint
    config:
      region: us-east-1
      delay: 1000 # Add a 1000ms (1 second) delay between API calls
```

You can also specify the delay directly at the provider level:

```yaml
providers:
  - id: sagemaker:my-endpoint
    delay: 1000 # 1 second delay
    config:
      region: us-east-1
```

Spacing out requests can help avoid bursty usage that might scale up more instances (or, if using a pay-per-request model, it simply spreads out the load). It does not reduce the per-call cost, but it can make the usage more predictable.

Note that delays are only applied for actual API calls, not when responses are retrieved from cache.

## Transforming Prompts

The SageMaker provider supports transforming prompts before they're sent to the endpoint. This is especially useful for:

- Formatting prompts specifically for a particular model type
- Adding system instructions or context
- Converting between different prompt formats
- Preprocessing text for specialized models

You can specify a transform function in your configuration:

```yaml
providers:
  - id: sagemaker:my-endpoint
    config:
      region: us-east-1
      transform: |
        // Transform the prompt before sending to SageMaker
        return `&lt;s&gt;[INST] ${prompt} [/INST]`
```

For more complex transformations, use a file:

```yaml
providers:
  - id: sagemaker:jumpstart:my-llama-endpoint
    config:
      region: us-west-2
      modelType: jumpstart
      transform: file://transform.js
```

Where `transform.js` might contain:

```javascript
// Transform function for formatting Llama prompts
module.exports = function (prompt, context) {
  return {
    inputs: prompt,
    parameters: {
      max_new_tokens: context.config?.maxTokens || 256,
      temperature: context.config?.temperature || 0.7,
      top_p: context.config?.topP || 0.9,
      do_sample: true,
    },
  };
};
```

You can specify the transform at the provider's top level or within the `config`. Both achieve the same effect; use whatever makes your config clearer. In YAML, using a `file://` path is recommended for complex logic.

Transformed prompts maintain proper caching and include metadata about the transformation in the response.

## Response Path Expressions

The `responseFormat.path` configuration option allows you to extract specific fields from the SageMaker endpoint response using JavaScript expressions or custom transformer functions from files.

### JavaScript Expressions

You can use JavaScript expressions to access nested properties in the response. Use `json` to refer to the response JSON object in the path expression:

```yaml
providers:
  - id: sagemaker:jumpstart:your-jumpstart-endpoint
    label: "JumpStart model"
    config:
      region: us-east-1
      modelType: jumpstart
      temperature: 0.7
      maxTokens: 256
      responseFormat:
        path: json-generated_text
```

### Response Format Issues

If you're getting unusual responses from your endpoint, try:

1. Setting `modelType` to match your model (or `custom` if unique)
2. Using the `responseFormat.path` option to extract the correct field:
   - For Llama models (JumpStart): Use `responseFormat.path: "json-generated_text"`
   - For Mistral models (Hugging Face): Use `responseFormat.path: "json[0].generated_text"`
3. Checking that your endpoint is correctly processing the input format
4. Adding a delay parameter (e.g., `delay: 500`) to prevent endpoint saturation