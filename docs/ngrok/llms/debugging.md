# Source: https://ngrok.com/docs/ai-gateway/guides/debugging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Debugging

> Inspect AI Gateway action results to diagnose request failures and understand routing decisions.

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

When troubleshooting AI Gateway issues, you can access detailed information about what happened during request processing using action result variables. This page explains how to capture and interpret this data.

## Action result variables

After the `ai-gateway` action runs, detailed results are available in `${actions.ngrok.ai_gateway}`. This includes:

* Model selection process and filtering steps
* Every model and request attempted
* API key selection details
* Token counts
* Latency measurements
* Error details for failed attempts

### Schema

<ConfigField title="actions.ngrok.ai_gateway.status" type="string">
  Overall outcome of the action: `"success"` or `"error"`.
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.error" type="object">
  Error details, only present if status is `"error"`.

  * `code` - Error code (for example, `"ERR_NGROK_3807"`)
  * `message` - Error message describing the failure
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.client" type="object">
  Information about the client request.

  * `method` - HTTP method from the client request
  * `path` - Request path from the client
  * `request_headers` - Client request headers (API key/auth headers trimmed)
  * `user_agent` - User-Agent header from the client
  * `model` - Client-requested model field
  * `models` - Client-requested models field
  * `api_key_hash` - Trimmed API key from the client
  * `rejected_models` - Models the client requested but were excluded (each with `model` and `reason`)
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.input_ngrok_tokens" type="integer">
  Estimated input token count calculated by ngrok (used for billing).
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.output_ngrok_tokens" type="integer">
  Estimated output token count calculated by ngrok (used for billing).
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.gateway_latency_ms" type="integer">
  Time added by gateway logic in milliseconds. Excludes time the gateway spent waiting on the upstream to respond to requests.
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.model_selection" type="array">
  Details about the model selection process (if applicable). Each entry contains:

  * `strategy` - The resolved strategy expression
  * `error` - Error if strategy evaluation failed
  * `candidates_returned` - Models that the strategy returned
  * `candidates_after_allowed_filter` - Above list of models after ones that are not allowed by the gateway config have been removed.
  * `candidates_after_client_filter` - Above list of models after filtering out ones that the client did not want (if applicable).
  * `models_to_try` - Final list of models to try
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.models_tried" type="array">
  Models attempted in chronological order. Each entry contains:

  * `model` - Model identifier
  * `provider` - Provider identifier
  * `author` - Author identifier (may be empty)
  * `api_key_selection` - Details about API key selection (strategy, error, keys\_to\_try)
  * `requests_made` - Array of request attempts for this model
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.models_tried[].requests_made" type="array">
  List of requests made for a specific model. Each request contains:

  * `status` - Request outcome: `"success"` or `"error"`
  * `error` - Error message if request failed
  * `upstream_input_tokens` - Input tokens counted by the provider
  * `upstream_output_tokens` - Output tokens counted by the provider
  * `request` - `url` and `api_key` of the request made to the upstream. Api key is trimmed to avoid leaking.
  * `response` - `status_code`, `headers`, `body_on_error` capture details of the response.
  * `upstream_latency` - Latency measurements (`time_to_first_byte_ms`, `total_ms`)
</ConfigField>

<ConfigField title="actions.ngrok.ai_gateway.success" type="object">
  Details of the successful model, only present when status is `"success"`.

  * `model_index` - Index into models\_tried array for the successful model
  * `request_index` - Index into requests\_made array for the successful request
  * `model` - Model id used in the successful request
  * `provider` - Provider id used in the successful request
  * `author` - Author id used in the successful request (may be empty)
</ConfigField>

### Accessing action results

To access action results, configure `on_error: "continue"` so subsequent actions can inspect the data:

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      on_error: continue
  - type: log
    config:
      metadata:
        ai_gateway_result: ${actions.ngrok.ai_gateway}
  - type: deny
```

<Note>
  Cloud Endpoints require a terminal action such as `deny`, `custom-response`, `redirect`, or `forward-internal` to complete the request. See [Cloud Endpoints](/universal-gateway/cloud-endpoints#differences-from-agent-endpoints) for more details.
</Note>

## Debugging patterns

### Return results as response (development)

During development, return the full action result to the client for inspection:

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      on_error: continue
  - type: custom-response
    config:
      status_code: 503
      headers:
        content-type: application/json
      body: ${actions.ngrok.ai_gateway}
```

**Example response:**

```json  theme={null}
{
  "status": "error",
  "error": {
    "code": "ERR_NGROK_3807",
    "message": "All AI providers failed to respond successfully."
  },
  "client": {
    "method": "POST",
    "path": "/v1/chat/completions",
    "user_agent": "curl/8.17.0",
    "model": "gpt-4o",
    "models": ["gpt-4.1", "gpt-5"],
    "api_key_hash": "sk-proj...7890" // If the actual key was sk-proj-abcdefghijklmnopqrstuvwxyz1234567890
  },
  "input_ngrok_tokens": 150,
  "gateway_latency_ms": 45,
  "model_selection": [
    {
      "strategy": "ai.models.filter(x, x.id in [\"gpt-4o\", \"claude-3-5-sonnet-20241022\"])",
      "candidates_returned": ["gpt-4o", "claude-3-5-sonnet-20241022"],
      "candidates_after_allowed_filter": ["gpt-4o"],
      "candidates_after_client_filter": ["gpt-4o"],
      "models_to_try": ["gpt-4o"]
    }
  ],
  "models_tried": [
    {
      "model": "gpt-4o",
      "provider": "openai",
      "author": "openai",
      "api_key_selection": [
        {
          "strategy": "ai.keys",
          "keys_to_try": ["sk-proj...2315"]
        }
      ],
      "requests_made": [
        {
          "status": "error",
          "error": "rate limit exceeded",
          "upstream_input_tokens": 0,
          "upstream_output_tokens": 0,
          "request": {
            "url": "https://api.openai.com/v1/chat/completions",
            "api_key": "sk-proj...2315"
          },
          "response": {
            "status_code": 429,
            "headers": {"content-type": ["application/json"]},
            "body_on_error": "{\"error\":{\"message\":\"Rate limit exceeded\",\"type\":\"rate_limit_error\"}}"
          },
          "upstream_latency": {
            "time_to_first_byte_ms": 120,
            "total_ms": 125
          }
        }
      ]
    }
  ]
}
```

### Send to log exports (production)

In production, send action results to your logging infrastructure:

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      on_error: continue
  - type: log
    config:
      metadata:
        ai_gateway_result: ${actions.ngrok.ai_gateway}
  - type: deny
```

This fires a log event that can be exported to your observability platform. See [Log Exporting](/ai-gateway/observability/log-exporting) for setup.

### Combined approach

Log the results and return a user-friendly error:

```yaml  theme={null}
on_http_request:
  - type: ai-gateway
    config:
      on_error: continue
  - type: log
    config:
      metadata:
        ai_gateway_result: ${actions.ngrok.ai_gateway}
  - type: custom-response
    config:
      status_code: 503
      headers:
        content-type: application/json
      body: |
        {
          "error": "AI service temporarily unavailable",
          "code": "${actions.ngrok.ai_gateway.error.code}"
        }
```

## Interpreting results

### Identifying rate limits

Look for `status_code: 429` in request responses:

```json  theme={null}
{
  "models_tried": [
    {
      "model": "gpt-4o",
      "provider": "openai",
      "requests_made": [
        {
          "status": "error",
          "response": {
            "status_code": 429,
            "body_on_error": "{\"error\":{\"type\":\"rate_limit_error\"}}"
          },
          "request": {
            "api_key": "sk-proj...2315"
          }
        }
      ]
    }
  ]
}
```

**Solution:** Add more API keys or configure key rotation with `api_key_selection`.

### Identifying model filtering issues

When you get `ERR_NGROK_3804` or want to understand what the gateway did, check `model_selection` to understand how models were filtered:

```json  theme={null}
{
  "status": "error",
  "model_selection": [
    {
      "strategy": "round-robin",
      "candidates_returned": ["gpt-4o", "claude-3-5-sonnet-20241022"],
      "candidates_after_allowed_filter": ["gpt-4o"],
      "candidates_after_client_filter": [], // After filtering by client model/models we have no remaining models
      "models_to_try": []
    }
  ],
  "models_tried": [],
  "error": {
    "code": "ERR_NGROK_3804",
    "message": "Unable to route request - no models matched"
  }
}
```

**Solution:** The client requested models that didn't survive filtering. Check `client.model` and adjust your configuration or the client request. Model names/spelling may be wrong. Try adding the provider prefix for new models or models not in the gateway config or model catalog.

### Identifying timeout issues

Look for attempts without a `status_code` or with timeout errors:

```json  theme={null}
{
  "models_tried": [
    {
      "model": "gpt-4o",
      "provider": "openai",
      "requests_made": [
        {
          "status": "error",
          "error": "context deadline exceeded",
          "response": {
            "status_code": 0
          }
        }
      ]
    }
  ]
}
```

**Solution:** Increase `per_request_timeout` or investigate provider latency using `upstream_latency` metrics.

### Understanding latency

Use the latency measurements to identify bottlenecks:

```json  theme={null}
{
  "gateway_latency_ms": 45,
  "models_tried": [
    {
      "requests_made": [
        {
          "upstream_latency": {
            "time_to_first_byte_ms": 2500,
            "total_ms": 8000
          }
        }
      ]
    }
  ]
}
```

**Solution:** High `time_to_first_byte_ms`/`total_ms` indicates slow provider response. High `gateway_latency_ms` indicates gateway processing overhead. Increase `per_request_timeout`/`total_timeout` or investigate provider latency.

## Next steps

<CardGroup cols={2}>
  <Card title="Troubleshooting" icon="circle-exclamation" href="/ai-gateway/reference/error-codes">
    Error codes and solutions
  </Card>

  <Card title="Log Exporting" icon="file-export" href="/ai-gateway/observability/log-exporting">
    Export logs to your observability platform
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).