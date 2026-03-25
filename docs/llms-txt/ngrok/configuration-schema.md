# Source: https://ngrok.com/docs/ai-gateway/reference/configuration-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration Schema

> Complete reference for AI Gateway configuration options.

export const ConfigEnumOption = ({children}) => {
  return <div className="space-y-2 px-4 py-2 list-none">{children}</div>;
};

export const ConfigEnum = ({label, children}) => {
  return <div className="m-0 flex flex-shrink-0 list-none flex-col divide-y divide-gray-200 self-start rounded-md border border-gray-200 p-0 dark:divide-gray-800 dark:border-gray-800 [&_li+li]:mt-0 [&_li]:py-2 list-none">
      <div className="px-4 py-2 font-semibold list-none">
        {label ? label : "Possible enum values"}
      </div>
      {children}
    </div>;
};

export const ConfigField = ({title, type, cel = false, defaultValue = false, required = false, children}) => {
  const id = `config-${title.replace(/\.|\s|\*/g, "_")}`;
  return <div className="field pt-2.5 pb-5 my-2.5 border-gray-50 dark:border-gray-800/50 border-b" style={{
    scrollMarginTop: '120px'
  }} id={id}>
      <div className="flex font-mono group/param-head param-head break-all relative">
        <div className="flex-1 flex content-start py-0.5 mr-5">
          <div className="flex items-center flex-wrap gap-2">
            <div class="absolute -top-1.5">
              <a href={`#${id}`} className="-ml-10 flex items-center opacity-0 border-0 group-hover/param-head:opacity-100 py-2 [.expandable-content_&]:-ml-[2.1rem]" aria-label="Navigate to header">
                ​<div className="w-6 h-6 rounded-md flex items-center justify-center shadow-sm text-gray-400 dark:text-white/50 dark:bg-background-dark dark:brightness-[1.35] dark:ring-1 dark:hover::rightness-150 bg-white ring-1 ring-gray-400/30 dark:ring-gray-700/25 hover:ring-gray-400/60 dark:hover:ring-white/20">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="gray" height="12px" viewBox="0 0 576 512"><path d="M0 256C0 167.6 71.6 96 160 96h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C98.1 144 48 194.1 48 256s50.1 112 112 112h72c13.3 0 24 10.7 24 24s-10.7 24-24 24H160C71.6 416 0 344.4 0 256zm576 0c0 88.4-71.6 160-160 160H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c61.9 0 112-50.1 112-112s-50.1-112-112-112H344c-13.3 0-24-10.7-24-24s10.7-24 24-24h72c88.4 0 160 71.6 160 160zM184 232H392c13.3 0 24 10.7 24 24s-10.7 24-24 24H184c-13.3 0-24-10.7-24-24s10.7-24 24-24z"></path></svg>
                </div>
              </a>
            </div>
            <div className="font-semibold text-primary dark:text-primary-light overflow-wrap-anywhere">{title}</div>
            <div className="inline items-center gap-2 text-xs font-medium [&_div]:inline [&_div]:mr-2 [&_div]:leading-5 [&_a]:inline [&_a]:mr-2 [&_a]:leading-5">
              {type && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                <span className="text-gray-600 dark:text-gray-200 !font-medium">{type}</span>
              </div>}
              {defaultValue && <div className="flex items-center px-2 py-0.5 rounded-md bg-gray-100/50 dark:bg-white/5 break-all">
                  <span class="text-gray-400 dark:text-gray-500">default:</span>
                  <span className="text-gray-600 dark:text-gray-200 !font-medium">{defaultValue}</span>
                </div>}
              {required && <div className="px-2 py-0.5 rounded-md bg-red-100/50 dark:bg-red-400/10 whitespace-nowrap">
                <span className="text-red-600 dark:text-red-300 !font-medium">Required</span>
              </div>}
              {cel && <a className="px-2 py-0.5 rounded-md !border-none bg-blue-100/50 dark:bg-blue-400/10 whitespace-nowrap" href="/traffic-policy/concepts/cel-interpolation">
                <span className="text-blue-600 dark:text-blue-300 !font-medium">Supports CEL</span>
              </a>}
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4 prose-sm prose-gray dark:prose-invert [&_.prose>p:first-child]:mt-0 [&_.prose>p:last-child]:mb-0">
        {children}
      </div>
    </div>;
};

The [Traffic Policy](/traffic-policy/) configuration reference for the AI Gateway action.

<Note>
  When using [AI Gateway API Keys](/ai-gateway/concepts/api-keys), no provider configuration is needed—ngrok manages provider keys automatically. The `providers` and `api_keys` fields below are only required for [Bring Your Own Keys](/ai-gateway/concepts/bring-your-own-keys) setups.
</Note>

## Supported phases

`on_http_request`

## Type

`ai-gateway`

## Basic structure

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      max_input_tokens: 4096
      max_output_tokens: 8192
      headers: {}
      query_params: {}
      body: {}
      on_error: "halt"
      total_timeout: "5m"
      per_request_timeout: "30s"
      providers: []
      only_allow_configured_providers: false
      only_allow_configured_models: false
      model_selection:
        strategy: []
      api_key_selection:
        strategy: []
```

## Configuration fields

<ConfigField title="max_input_tokens" type="integer">
  <p>Maximum number of tokens allowed in the prompt and context. Requests exceeding this limit will be rejected.</p>
  <p>No limit is applied if not specified. Maximum allowed value is 500,000.</p>

  ```yaml  theme={null}
  max_input_tokens: 4096
  ```
</ConfigField>

<ConfigField title="max_output_tokens" type="integer">
  <p>Maximum number of tokens allowed in the completion response.</p>
  <p>No limit is applied if not specified. Maximum allowed value is 500,000.</p>

  ```yaml  theme={null}
  max_output_tokens: 2048
  ```
</ConfigField>

<ConfigField title="headers" type="object" cel={true}>
  <p>Additional HTTP headers to include in requests to AI providers.</p>

  ```yaml  theme={null}
  headers:
    X-Custom-Header: "value"
    X-Request-ID: "${req.id}"
  ```
</ConfigField>

<ConfigField title="query_params" type="object" cel={true}>
  <p>Additional query parameters to append to provider requests.</p>

  ```yaml  theme={null}
  query_params:
    api_version: "2023-10-01"
  ```
</ConfigField>

<ConfigField title="body" type="object" cel={true}>
  <p>Additional JSON fields to merge into the request body.</p>

  ```yaml  theme={null}
  body:
    temperature: 0.7
    top_p: 0.9
  ```
</ConfigField>

<ConfigField title="on_error" type="enum" defaultValue="halt">
  <p>Behavior when all failover attempts are exhausted.</p>

  <ConfigEnum label="Supported values">
    <ConfigEnumOption>`halt` (default) - Stop processing and return error to client</ConfigEnumOption>
    <ConfigEnumOption>`continue` - Continue to next action in Traffic Policy</ConfigEnumOption>
  </ConfigEnum>

  ```yaml  theme={null}
  on_error: "continue"
  ```
</ConfigField>

<ConfigField title="total_timeout" type="string" defaultValue="5m">
  <p>Maximum total time for all failover attempts across all models and keys. Must be specified as a duration string (for example, <code>"2m"</code>, <code>"90s"</code>).</p>

  ```yaml  theme={null}
  total_timeout: "2m"
  ```
</ConfigField>

<ConfigField title="per_request_timeout" type="string" defaultValue="30s">
  <p>Timeout for a single request to a provider. Must be specified as a duration string (for example, <code>"45s"</code>, <code>"1m"</code>).</p>

  ```yaml  theme={null}
  per_request_timeout: "45s"
  ```
</ConfigField>

<ConfigField title="providers" type="array">
  <p>List of AI provider configurations. Not required when using <a href="/ai-gateway/concepts/api-keys">AI Gateway API Keys</a>—ngrok manages provider keys automatically. When empty, all built-in providers are allowed.</p>
  <p>See <a href="#provider-configuration">Provider Configuration</a> below for detailed field definitions.</p>

  ```yaml  theme={null}
  providers:
    - id: "openai"
      api_keys:
        - value: ${secrets.get('openai', 'key-one')}
  ```
</ConfigField>

<ConfigField title="only_allow_configured_providers" type="boolean" defaultValue="false">
  <p>When <code>true</code>, only providers explicitly listed in <code>providers</code> are allowed. Requests to other providers are rejected with an error.</p>

  ```yaml  theme={null}
  only_allow_configured_providers: true
  ```
</ConfigField>

<ConfigField title="only_allow_configured_models" type="boolean" defaultValue="false">
  <p>When <code>true</code>, only models explicitly listed in provider configurations are allowed. Requests for other models are rejected.</p>

  ```yaml  theme={null}
  only_allow_configured_models: true
  ```
</ConfigField>

<ConfigField title="model_selection" type="object">
  <p>Strategy for selecting model candidates using CEL expressions. The first strategy that returns models wins—subsequent strategies are only used if previous ones return no models.</p>
  <p>See <a href="/ai-gateway/guides/model-selection-strategies">Model Selection Strategies</a> for details and <a href="/ai-gateway/reference/cel-functions">CEL Functions Reference</a> for available functions.</p>

  ```yaml  theme={null}
  model_selection:
    strategy:
      - "ai.models.filter(m, m.provider_id == 'openai')"
      - "ai.models"
  ```
</ConfigField>

<ConfigField title="api_key_selection" type="object">
  <p>Strategy for selecting API keys using CEL expressions. Enables intelligent key selection based on metrics like quota usage and error rates.</p>
  <p>When not specified, keys are tried in the order listed. See <a href="/ai-gateway/reference/cel-functions#api-key-selection">CEL Functions Reference</a> for available functions.</p>

  ```yaml  theme={null}
  api_key_selection:
    strategy:
      - "ai.keys.filter(k, k.quota.remaining_requests > 100)"
      - "ai.keys.filter(k, k.error_rate.rate_limit < 0.1)"
      - "ai.keys"
  ```
</ConfigField>

## Provider configuration

Each provider in the `providers` array supports these fields:

<ConfigField title="providers[].id" type="string" required>
  <p>Provider identifier. Use built-in names (<code>openai</code>, <code>anthropic</code>, <code>google</code>, <code>deepseek</code>) or custom names for self-hosted providers.</p>

  ```yaml  theme={null}
  - id: "openai"
  ```
</ConfigField>

<ConfigField title="providers[].id_aliases" type="array of strings">
  <p>Alternative identifiers for this provider. Allows clients to reference the same provider by different names.</p>

  ```yaml  theme={null}
  - id: "custom-openai"
    id_aliases: ["openai", "gpt"]
  ```
</ConfigField>

<ConfigField title="providers[].base_url" type="string">
  <p>Custom endpoint URL for self-hosted or alternative provider endpoints. Required for custom providers.</p>

  ```yaml  theme={null}
  - id: "ollama"
    base_url: "https://ollama.internal.company.com"
  ```
</ConfigField>

<ConfigField title="providers[].display_name" type="string">
  <p>Human-readable name for the provider.</p>
</ConfigField>

<ConfigField title="providers[].description" type="string">
  <p>Description of the provider.</p>
</ConfigField>

<ConfigField title="providers[].website" type="string">
  <p>Provider's website URL.</p>
</ConfigField>

<ConfigField title="providers[].disabled" type="boolean" defaultValue="false">
  <p>Temporarily disable this provider without removing its configuration.</p>

  ```yaml  theme={null}
  - id: "openai"
    disabled: true
  ```
</ConfigField>

<ConfigField title="providers[].metadata" type="object">
  <p>Custom metadata for tracking and organization. Not sent to providers. Available in selection strategies via <code>m.getMetadata()</code>.</p>

  ```yaml  theme={null}
  - id: "openai"
    metadata:
      team: "ml-platform"
      environment: "production"
  ```
</ConfigField>

<ConfigField title="providers[].api_keys" type="array">
  <p>List of API keys for this provider. Keys are tried in order for automatic failover.</p>

  ```yaml  theme={null}
  api_keys:
    - value: ${secrets.get('openai', 'primary')}
    - value: ${secrets.get('openai', 'backup')}
  ```
</ConfigField>

<ConfigField title="providers[].models" type="array">
  <p>List of model configurations for this provider. See <a href="#model-configuration">Model Configuration</a> below.</p>
</ConfigField>

<ConfigField title="providers[].supported_api_surfaces" type="array">
  <p>List of API formats this provider supports. Possible values are <code>openai</code> and <code>anthropic</code>. Default is <code>openai</code>.</p>
  <p>Each entry optionally includes a <code>surface</code> (the specific endpoint, such as <code>chat-completions</code> or <code>responses</code>) and a <code>supported\_params</code> list. When <code>supported\_params</code> is non-empty, any top-level request body parameter not on the list is automatically removed before the request is forwarded to the provider. For official providers, this information is maintained automatically.</p>

  <ConfigField title="providers[].supported_api_surfaces" type="array<object>">
    <p>Lists the API surfaces supported by this provider.</p>
    <p>Each entry must include <code>format</code>, and may include <code>surface</code> and <code>supported\_params</code>.</p>

    <ConfigField title="providers[].supported_api_surfaces[].format" type="string" required>
      <p>The API format for this entry. Allowed values: <code>openai</code>, <code>anthropic</code>.</p>
    </ConfigField>

    <ConfigField title="providers[].supported_api_surfaces[].surface" type="string">
      <p>Optional endpoint surface for this format entry (for example <code>chat-completions</code>, <code>responses</code>, or <code>messages</code>).</p>
    </ConfigField>

    <ConfigField title="providers[].supported_api_surfaces[].supported_params" type="array<string>">
      <p>Optional allowlist of top-level request body keys.  You must set <code>surface</code> in order to set this field.</p>
    </ConfigField>
  </ConfigField>

  ```yaml  theme={null}
  supported_api_surfaces:
    - format: openai
      surface: chat-completions
      supported_params:
        - name: model
        - name: messages
        - name: temperature
        - name: stream
    - format: anthropic
  ```
</ConfigField>

## API key configuration

Each API key in `providers[].api_keys` supports:

<ConfigField title="providers[].api_keys[].value" type="string" required>
  <p>The API key value. Use <code>secrets.get()</code> for secure storage.</p>

  ```yaml  theme={null}
  api_keys:
    - value: ${secrets.get('openai', 'key-one')}
  ```
</ConfigField>

## Model configuration

Each model in `providers[].models` supports:

<ConfigField title="providers[].models[].id" type="string" required>
  <p>Model identifier as recognized by the provider.</p>

  ```yaml  theme={null}
  models:
    - id: "gpt-4o"
  ```
</ConfigField>

<ConfigField title="providers[].models[].id_aliases" type="array of strings">
  <p>Alternative identifiers for this model.</p>

  ```yaml  theme={null}
  models:
    - id: "gpt-4o-2024-11-20"
      id_aliases: ["gpt-4o", "gpt-4-latest"]
  ```
</ConfigField>

<ConfigField title="providers[].models[].author_id" type="string">
  <p>ID of the model author (for third-party models).</p>
</ConfigField>

<ConfigField title="providers[].models[].display_name" type="string">
  <p>Human-readable name for the model.</p>
</ConfigField>

<ConfigField title="providers[].models[].description" type="string">
  <p>Description of the model.</p>
</ConfigField>

<ConfigField title="providers[].models[].disabled" type="boolean" defaultValue="false">
  <p>Temporarily disable this model.</p>

  ```yaml  theme={null}
  models:
    - id: "gpt-3.5-turbo"
      disabled: true
  ```
</ConfigField>

<ConfigField title="providers[].models[].metadata" type="object">
  <p>Custom metadata for the model. Available in selection strategies.</p>

  ```yaml  theme={null}
  models:
    - id: "gpt-4o"
      metadata:
        tier: "premium"
        approved: true
  ```
</ConfigField>

<ConfigField title="providers[].models[].input_modalities" type="array of strings">
  <p>Input types supported by the model (for example, "text", "image", "audio").</p>
</ConfigField>

<ConfigField title="providers[].models[].output_modalities" type="array of strings">
  <p>Output types supported by the model.</p>
</ConfigField>

<ConfigField title="providers[].models[].max_context_window" type="integer">
  <p>Maximum context window size in tokens.</p>
</ConfigField>

<ConfigField title="providers[].models[].max_output_tokens" type="integer">
  <p>Maximum output tokens the model can generate.</p>
</ConfigField>

<ConfigField title="providers[].models[].supported_features" type="array of strings">
  <p>Features supported by the model (for example, "tool-calling", "coding").</p>
</ConfigField>

<ConfigField title="providers[].models[].unsupported_params" type="array of objects">
  <p>A denylist of top-level request body parameters that this model does not support. When a request is forwarded to this model, any listed parameters are automatically removed from the request body before it is sent to the provider.</p>
  <p>Each entry requires a <code>name</code> field with the parameter name. This is useful for custom models that reject parameters that clients commonly include.</p>
  <p>For official models in the ngrok model catalog, this information is maintained automatically—no configuration required.</p>

  ```yaml  theme={null}
  models:
    - id: "my-model"
      unsupported_params:
        - name: parallel_tool_calls
        - name: response_format
  ```
</ConfigField>

## Complete example

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      max_input_tokens: 4096
      max_output_tokens: 2048
      total_timeout: "3m"
      per_request_timeout: "30s"
      on_error: "halt"
      only_allow_configured_providers: true
      only_allow_configured_models: true
      
      providers:
        - id: "openai"
          metadata:
            team: "ml"
          api_keys:
            - value: ${secrets.get('openai', 'primary')}
            - value: ${secrets.get('openai', 'backup')}
            - value: ${secrets.get('openai', 'emergency')}
          models:
            - id: "gpt-4o"
              metadata:
                approved: true
            - id: "gpt-4o-mini"
              metadata:
                approved: true
        
        - id: "anthropic"
          api_keys:
            - value: ${secrets.get('anthropic', 'key')}
          models:
            - id: "claude-3-5-sonnet-20241022"
        
        - id: "ollama-internal"
          base_url: "https://ollama.company.internal"
          models:
            - id: "llama3-70b"
      
      model_selection:
        strategy:
          - "ai.models.filter(m, m.provider_id == 'openai')"
          - "ai.models.filter(m, m.provider_id == 'anthropic')"
          - "ai.models.filter(m, m.provider_id == 'ollama-internal')"
      
      api_key_selection:
        strategy:
          # Prefer keys with remaining quota
          - "ai.keys.filter(k, k.quota.remaining_requests > 100)"
          # Fall back to keys with low error rates
          - "ai.keys.filter(k, k.error_rate.rate_limit < 0.1)"
          # Fall back to all keys
          - "ai.keys"
```


Built with [Mintlify](https://mintlify.com).