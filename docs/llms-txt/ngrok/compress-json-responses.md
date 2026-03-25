# Source: https://ngrok.com/docs/traffic-policy/examples/compress-json-responses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compress JSON Responses Example

> Learn how to compress JSON responses using Traffic Policy to improve performance and reduce bandwidth usage.

With Traffic Policy, you can ensure all JSON responses returned by your upstream services are [compressed](/traffic-policy/actions/compress-response) en route to the API consumer.

This rule compresses JSON responses using the `gzip`, `br`, `deflate`, and `compress` algorithms.

<Note>
  If your upstream service already handles compression, ngrok skips this step.
</Note>

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_response:
  - name: Add compression
    actions:
    - type: compress-response
      config:
        algorithms:
        - gzip
        - br
        - deflate
        - compress
  ```

  ```json policy.json theme={null}
  {
    "on_http_response": [
      {
        "name": "Add compression",
        "actions": [
          {
            "type": "compress-response",
            "config": {
              "algorithms": [
                "gzip",
                "br",
                "deflate",
                "compress"
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

See [the `compress-response` Traffic Policy action docs](/traffic-policy/actions/compress-response/) for more information.


Built with [Mintlify](https://mintlify.com).