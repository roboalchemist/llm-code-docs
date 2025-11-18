# Source: https://docs.openpipe.ai/features/request-logs/exporting-logs.md

# Exporting Logs

>  Export your past requests as a JSONL file in their raw form.

## Request logs export

Once your request logs are recorded, you can export them at any time. The exported jsonl contains all the data that we've collected from your logged calls, including tags and errors.

<Frame>![](https://mintlify.s3.us-west-1.amazonaws.com/openpipe/images/features/request-logs/exporting-logs.png)</Frame>

### Fields

* **`Input`:** The complete chat creation request.
* **`Output`:** Whatever output was generated, including errors.
* **`Tags`:** Any metadata tags that you included when making the request.

### Example

```jsonl
{"input":{"model":"openpipe:test-tool-calls-ft","tools":[{"type":"function","function":{"name":"get_current_weather","parameters":{"type":"object","required":["location"],"properties":{"unit":{"enum":["celsius","fahrenheit"],"type":"string"},"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"}}},"description":"Get the current weather in a given location"}}],"messages":[{"role":"system","content":"tell me the weather in SF and Orlando"}]},"output":{"id":"c7670af0d71648b0bd829fa1901ac6c5","model":"openpipe:test-tool-calls-ft","usage":{"total_tokens":106,"prompt_tokens":47,"completion_tokens":59},"object":"chat.completion","choices":[{"index":0,"message":{"role":"assistant","content":null,"tool_calls":[{"id":"","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"San Francisco, CA\", \"unit\": \"celsius\"}"}},{"id":"","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\": \"Orlando, FL\", \"unit\": \"celsius\"}"}}]},"finish_reason":"stop"}],"created":1702666185703},"tags":{"prompt_id":"test_sync_tool_calls_ft","$sdk":"python","$sdk.version":"4.1.0"}}
{"input":{"model":"openpipe:test-content-ft","messages":[{"role":"system","content":"count to 3"}]},"output":{"id":"47116eaa9dad4238bf12e32135f9c147","model":"openpipe:test-content-ft","usage":{"total_tokens":38,"prompt_tokens":29,"completion_tokens":9},"object":"chat.completion","choices":[{"index":0,"message":{"role":"assistant","content":"1, 2, 3"},"finish_reason":"stop"}],"created":1702666036923},"tags":{"prompt_id":"test_sync_content_ft","$sdk":"python","$sdk.version":"4.1.0"}}
```

If you'd like to see how it works, try exporting some logs from our [public demo](https://app.openpipe.ai/p/BRZFEx50Pf/request-logs).
