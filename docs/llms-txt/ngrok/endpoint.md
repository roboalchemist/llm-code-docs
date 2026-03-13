# Source: https://ngrok.com/docs/traffic-policy/variables/endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Endpoint Variables

> Reference documentation for endpoint variables in Traffic Policy that provide metadata about the endpoint processing the request.

## Endpoint Variables

The following variables are available under the `endpoint` namespace:

| Name                                     | Type     | Description                                                                                     |
| ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| [`endpoint.addr`](#endpointaddr)         | `string` | The address for this endpoint.                                                                  |
| [`endpoint.host`](#endpointhost)         | `string` | The hostname for this endpoint.                                                                 |
| [`endpoint.id`](#endpointid)             | `string` | The endpoint that serviced this connection.                                                     |
| [`endpoint.port`](#endpointport)         | `int32`  | The port for this endpoint.                                                                     |
| [`endpoint.protocol`](#endpointprotocol) | `string` | The protocol for this endpoint. Current supported values are `http`, `https`, `tcp`, and `tls`. |
| [`endpoint.url`](#endpointurl)           | `string` | The URL for this endpoint.                                                                      |

### `endpoint.addr`

The address for this endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.addr == 'my-subdomain.ngrok.app:443'"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.addr == 'my-subdomain.ngrok.app:443'"
    ]
  }
  ```
</CodeGroup>

### `endpoint.host`

The hostname for this endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.host == 'my-subdomain.ngrok.app'"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.host == 'my-subdomain.ngrok.app'"
    ]
  }
  ```
</CodeGroup>

### `endpoint.id`

The id for this endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.id == 'ep_2iL8LRbQilSCKYjaslRoqBwJcfT'"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.id == 'ep_2iL8LRbQilSCKYjaslRoqBwJcfT'"
    ]
  }
  ```
</CodeGroup>

### `endpoint.port`

The port for this endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.port == 443"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.port == 443"
    ]
  }
  ```
</CodeGroup>

### `endpoint.protocol`

The protocol for this endpoint. Current supported values are `http`, `https`, `tcp`, and `tls`.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.protocol == 'https'"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.protocol == 'https'"
    ]
  }
  ```
</CodeGroup>

### `endpoint.url`

The URL for this endpoint.

<CodeGroup>
  ```yaml policy.yml theme={null}
  expressions:
    - "endpoint.url == 'https://my-subdomain.ngrok.app'"
  ```

  ```json policy.json theme={null}
  {
    "expressions": [
      "endpoint.url == 'https://my-subdomain.ngrok.app'"
    ]
  }
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).