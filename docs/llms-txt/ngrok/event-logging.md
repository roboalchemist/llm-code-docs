# Source: https://ngrok.com/docs/traffic-policy/examples/event-logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Logging Example

> Learn how to configure event logging in Traffic Policy to export logs to external services like Datadog for monitoring and troubleshooting.

With Traffic Policy, you can connect your API to ngrok's [log exporting system](/obs/) for smarter troubleshooting, testing, and integration of logging services like Datadog for your API gateway and upstream services.

This rule:

1. Checks if the response status code is not in the 200 range
2. Logs the unsuccessful request with a custom message and metadata

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
  - actions:
    - type: custom-response
      config:
        status_code: 503
        body: "<html><body><h1>Service Unavailable</h1><p>Our servers are currently
          down for maintenance. Please check back later.</p></body></html>"
        headers:
          content-type: text/html
  on_http_response:
  - name: Log unsuccessful requests
    expressions:
    - res.status_code < '200' && res.status_code >= '300'
    actions:
    - type: log
      config:
        metadata:
          message: Unsuccessful request
          edge_id: "<YOUR-NGROK-DOMAIN>"
          success: false
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 503,
              "body": "<html><body><h1>Service Unavailable</h1><p>Our servers are currently down for maintenance. Please check back later.</p></body></html>",
              "headers": {
                "content-type": "text/html"
              }
            }
          }
        ]
      }
    ],
    "on_http_response": [
      {
        "name": "Log unsuccessful requests",
        "expressions": [
          "res.status_code < '200' && res.status_code >= '300'"
        ],
        "actions": [
          {
            "type": "log",
            "config": {
              "metadata": {
                "message": "Unsuccessful request",
                "edge_id": "<YOUR-NGROK-DOMAIN>",
                "success": false
              }
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

See [the `log` Traffic Policy action docs](/traffic-policy/actions/log/) for more information.


Built with [Mintlify](https://mintlify.com).