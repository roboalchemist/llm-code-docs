# Source: https://docs.api7.ai/hub/mocking.md

# mocking

The `mocking` plugin allows you to simulate API responses without forwarding requests to upstream services. The plugin supports the customization of the response status code, body, headers, and more. This is particularly useful during development, testing, or debugging phases, where the actual upstream service might be unavailable, under maintenance, or expensive to call. By providing mock responses in a predefined format, the plugin enables you to test client-side integrations, validate request handling, and debug issues without relying on the upstream infrastructure.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `mocking` plugin for different scenarios.

### Generate Specific Mock Responses[â](#generate-specific-mock-responses "Direct link to Generate Specific Mock Responses")

The following example demonstrates how to configure the plugin to generate a specific mock response and response status code without forwarding the request to the upstream service.

Create a route using the `mocking` plugin and define a response body for the expected mock responses:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mocking-route",
    "uri": "/anything",
    "plugins": {
      "mocking": {
        "response_status":201,
        "response_example":"{\"Lastname\":\"Brown\",\"Age\":56}"
      }
    }
  }'
```

â¶ Configure the expected mock response status code to be `201`.

â· Configure the expected mock response body to be `{"Lastname":"Brown","Age":56}`.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 201 Created` mock response and see the following response body:

```
{"Lastname":"Brown","Age":56}
```

### Generate Mock Response Headers[â](#generate-mock-response-headers "Direct link to Generate Mock Response Headers")

The following example demonstrates how to configure the plugin to generate mock response headers and use a [built-in variable](https://docs.api7.ai/apisix/reference/built-in-variables.md) in the response body.

Create a route using the `mocking` plugin, define response headers, and response body for the expected mock responses:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mocking-route",
    "uri": "/anything",
    "plugins": {
      "mocking": {
        "response_headers": {
          "X-User-Id": 100,
          "X-Product-Id": "apac-398-472"
        },
        "response_example":"Client IP: $remote_addr"
      }
    }
  }'
```

â¶ Configure the expected mock response header `X-User-Id: 100`.

â· Configure the expected mock response header `X-Product-Id: apac-398-472`.

â¸ Configure the expected mock response body to display the client IP address.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive a response similar to the following:

```
HTTP/1.1 200 OK
...
X-Product-Id: apac-398-472
X-User-Id: 100

Client IP: 192.168.65.1
```

### Generate Mock Responses using JSON Schema[â](#generate-mock-responses-using-json-schema "Direct link to Generate Mock Responses using JSON Schema")

The following example demonstrates how to configure the plugin to generate mock responses following a specific [JSON schema](https://json-schema.org).

Create a route using the `mocking` plugin and define a JSON schema for the expected mock responses:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mocking-route",
    "uri": "/anything",
    "plugins": {
      "mocking": {
        "response_schema": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "example": "abcd"
            },
            "ip": {
              "type": "number",
              "example": 192.168.0.10
            },
            "random_str_arr": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "nested_obj": {
              "type": "object",
              "properties": {
                "random_str": {
                  "type": "string"
                },
                "child_nested_obj": {
                  "type": "object",
                  "properties": {
                    "random_bool": {
                      "type": "boolean",
                      "example": true
                    },
                    "random_int_arr": {
                      "type": "array",
                      "items": {
                        "type": "integer",
                        "example": 155
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org": 1
      }
    }
  }'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should see a mock response similar to the following, without the actual response from the upstream service:

```
{
  "ip":192.168.0.10,
  "random_str_arr":[
    "fb","lyquibkwc","r"
  ],
  "id":"abcd",
  "nested_obj":{
    "random_str":"bzbb",
    "child_nested_obj":{
      "random_bool":true,
      "random_int_arr":[155,155,155]
    }
  }
}
```
