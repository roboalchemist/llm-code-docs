# Source: https://docs.openpipe.ai/features/request-logs/exporting-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Logs

>  Export your past requests as a JSONL file in their raw form.

## Request logs export

Once your request logs are recorded, you can export them at any time. The exported jsonl contains all the data that we've collected from your logged calls, including tags and errors.

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=5fa564d3a55fe1c13376cab3f3c90489" alt="" data-og-width="2266" width="2266" data-og-height="792" height="792" data-path="images/features/request-logs/exporting-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=1957a143d62dff6b51c278c0a22d2eb0 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=cef51c2cad92e4c0b0fc98ae59d5bfd4 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=86db2b4f76fd1d6a60652c3029c85064 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=407042348dfddd494b83ebe6521dd5b4 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=a16e3b7e008d709fdcd18d3f1694c3fe 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/request-logs/exporting-logs.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=62b142961923816744cf863bac22dec4 2500w" /></Frame>

### Fields

* **`Input`:** The complete chat creation request.
* **`Output`:** Whatever output was generated, including errors.
* **`Tags`:** Any metadata tags that you included when making the request.

### Example

```jsonl  theme={null}
{"input":{"model":"openpipe:test-tool-calls-ft","tools":[{"type":"function","function":{"name":"get_current_weather","parameters":{"type":"object","required":["location"],"properties":{"unit":{"enum":["celsius","fahrenheit"],"type":"string"},"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"}}},"description":"Get the current weather in a given location"}}],"messages":[{"role":"system","content":"tell me the weather in SF and Orlando"}]},"output":{"id":"c7670af0d71648b0bd829fa1901ac6c5","model":"openpipe:test-tool-calls-ft","usage":{"total_tokens":106,"prompt_tokens":47,"completion_tokens":59},"object":"chat.completion","choices":[{"index":0,"message":{"role":"assistant","content":null,"tool_calls":[{"id":"","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"San Francisco, CA\", \"unit\": \"celsius\"}"}},{"id":"","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"Orlando, FL\", \"unit\": \"celsius\"}"}}]},"finish_reason":"stop"}],"created":1702666185703},"tags":{"prompt_id":"test_sync_tool_calls_ft","$sdk":"python","$sdk.version":"4.1.0"}}
{"input":{"model":"openpipe:test-content-ft","messages":[{"role":"system","content":"count to 3"}]},"output":{"id":"47116eaa9dad4238bf12e32135f9c147","model":"openpipe:test-content-ft","usage":{"total_tokens":38,"prompt_tokens":29,"completion_tokens":9},"object":"chat.completion","choices":[{"index":0,"message":{"role":"assistant","content":"1, 2, 3"},"finish_reason":"stop"}],"created":1702666036923},"tags":{"prompt_id":"test_sync_content_ft","$sdk":"python","$sdk.version":"4.1.0"}}
```

If you'd like to see how it works, try exporting some logs from our [public demo](https://app.openpipe.ai/p/BRZFEx50Pf/request-logs).
