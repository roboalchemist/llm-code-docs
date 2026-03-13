# Source: https://ngrok.com/docs/traffic-policy/examples/enforce-tls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enforce TLS Example

> Learn how to enforce minimum TLS version requirements using Traffic Policy to reject connections using outdated TLS versions.

With Traffic Policy, you can prevent obsolete and potentially vulnerable browsers, SDKs, or CLI tools like `curl` from attempting to access your API.

This rule:

1. Uses [the `conn.tls.version` connection variable](/traffic-policy/variables/connection/#conntlsversion) to check the incoming request's TLS version.
2. Rejects versions below `1.3` with a `401 Unauthorized` response.

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
  - name: Reject requests using old TLS versions
    expressions:
    - conn.tls.version < '1.3'
    actions:
    - type: custom-response
      config:
        status_code: 401
        body: 'Unauthorized: TLS version too old'
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "name": "Reject requests using old TLS versions",
        "expressions": [
          "conn.tls.version < '1.3'"
        ],
        "actions": [
          {
            "type": "custom-response",
            "config": {
              "status_code": 401,
              "body": "Unauthorized: TLS version too old"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

See [the `custom-response` Traffic Policy action docs](/traffic-policy/actions/custom-response/) for more information.


Built with [Mintlify](https://mintlify.com).