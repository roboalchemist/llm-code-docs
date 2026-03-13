# Source: https://ngrok.com/docs/traffic-policy/examples/a-b-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to run an A/B test

> Learn how to run A/B tests using Traffic Policy by routing traffic to different endpoints based on random distribution.

With at least two endpoints and Traffic Policy, you can run simple A/B tests with using the [`rand.double()` macro](/traffic-policy/macros/#randdouble---double).

## Basic example

This rule:

1. Uses `rand.double()` to generate a random `double` between 0 and 1 when traffic reaches the endpoint
2. Checks if the value is less than or equal to 0.5
3. If so, it routes the traffic to a different [internal Agent Endpoint](/universal-gateway/internal-endpoints/).

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
  - expressions:
    - rand.double() <= 0.5
    actions:
    - type: forward-internal
      config:
        url: https://a.internal
  - actions:
    - type: forward-internal
      config:
        url: https://b.internal
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "rand.double() <= 0.5"
        ],
        "actions": [
          {
            "type": "forward-internal",
            "config": {
              "url": "https://a.internal"
            }
          }
        ]
      },
      {
        "actions": [
          {
            "type": "forward-internal",
            "config": {
              "url": "https://b.internal"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

<Tip>
  You can change the value the random number is checked against to split the traffic in different ratios. For example,`>=0.8` would send 80% of the traffic to one endpoint and 20% to the other.
</Tip>

See [the `forward-internal` Traffic Policy action docs](/traffic-policy/actions/forward-internal/) for more information.

## Using rewrites

You can also send the traffic to a different route using URL rewrites.

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
  - expressions:
    - rand.double() <= 0.5
    actions:
    - type: url-rewrite
      config:
        from: "/path/to/test"
        to: "/path/to/test-b"
  - actions:
    - type: forward-internal
      config:
        url: https://b.internal
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "expressions": [
          "rand.double() <= 0.5"
        ],
        "actions": [
          {
            "type": "url-rewrite",
            "config": {
              "from": "/path/to/test",
              "to": "/path/to/test-b"
            }
          }
        ]
      },
      {
        "actions": [
          {
            "type": "forward-internal",
            "config": {
              "url": "https://b.internal"
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

See [the URL Rewrite Example](/traffic-policy/examples/url-rewrites) for another example using rewrites.


Built with [Mintlify](https://mintlify.com).