# Source: https://docs.api7.ai/hub/data-mask.md

# data-mask

The `data-mask` plugin masks sensitive information in request headers, bodies, and URL queries when using logging plugins. Note that it does not modify the actual request or response traffic.

To mask sensitive information in the gatewayâs access log, see [Mask Sensitive Data in Access Log](https://docs.api7.ai/enterprise/best-practices/data-masking-access-log.md).

About Plugin Execution Order

The plugin can be configured on routes, services, or as a global plugin. However, be aware that [global plugins are always executed before route- or service-level plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order), so data masking may occur after logging.

For instance, if a logging plugin is configured globally while `data-mask` is applied at the route level, requests will be logged before masking occurs, and sensitive data will appear in plaintext.

To ensure the intended behavior, it is recommended to configure both plugins at the same level:

1. Both at the global level (recommended if suitable for your use case)
2. Both at the route or service level

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can use the `data-mask` plugin for different scenarios.

While all examples use the `file-logger` plugin for logging, the plugin is used only to demonstrate the results of data masking. Select the logging plugin that best suits your environment.

### Mask Sensitive Information in URL Query[â](#mask-sensitive-information-in-url-query "Direct link to Mask Sensitive Information in URL Query")

The following example demonstrates how you can mask sensitive information in the request URL queries, before the request is logged to a local file by the `file-logger` plugin.

Create a route with the `file-logger` plugin to log requests and the `data-mask` plugin with three data masking rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "data-mask-route",
    "uri": "/anything",
    "plugins": {
      "data-mask": {
        "request": [
          {
            "action": "remove",
            "name": "password",
            "type": "query"
          },
          {
            "action": "replace",
            "name": "token",
            "type": "query",
            "value": "*****"
          },
          {
            "action": "regex",
            "name": "card",
            "regex": "(\\d+)\\-\\d+\\-\\d+\\-(\\d+)",
            "type": "query",
            "value": "$1-****-****-$2"
          }
        ]
      },
      "file-logger": {
        "path": "/tmp/mask-query.log"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ data masking rule to remove `password` URL query from the request.

â· data masking rule to replace the value of `token` URL query with `*****`.

â¸ data masking rule that matches card number in the URL query with RegEx and mask the middle portion of the card number.

â¹ path to the log file on the filesystem where logs should be saved.

Send a request to the route with sensitive information in URL queries:

```
curl -i "http://127.0.0.1:9080/anything?password=abc&token=xyz&card=1234-1234-1234-1234"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigating to the `/tmp/mask-query.log` file and examining the log content, you should see a log entry similar to the following:

```
{
  "request": {
    "uri": "/anything?token=*****&card=1234-****-****-1234",
    "method": "GET",
    "url": "http://127.0.0.1:9080/anything?token=*****&card=1234-****-****-1234",
    "querystring": {
      "token": "*****",
      "card": "1234-****-****-1234"
    }
  }
}
```

### Mask Sensitive Information in Request Headers[â](#mask-sensitive-information-in-request-headers "Direct link to Mask Sensitive Information in Request Headers")

The following example demonstrates how you can mask sensitive information in request headers, before the request is logged to a local file by the `file-logger` plugin.

Create a route with the `file-logger` plugin to log requests and the `data-mask` plugin with three data masking rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "data-mask-route",
    "uri": "/anything",
    "plugins": {
      "data-mask": {
        "request": [
          {
            "action": "remove",
            "name": "password",
            "type": "header"
          },
          {
            "action": "replace",
            "name": "token",
            "type": "header",
            "value": "*****"
          },
          {
            "action": "regex",
            "name": "card",
            "regex": "(\\d+)\\-\\d+\\-\\d+\\-(\\d+)",
            "type": "header",
            "value": "$1-****-****-$2"
          }
        ]
      },
      "file-logger": {
        "path": "/tmp/mask-header.log"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ data masking rule to remove `password` header from the request.

â· data masking rule to replace the value of `token` request header with `*****`.

â¸ data masking rule that matches card number in the request header with RegEx and mask the middle portion of the card number.

â¹ path to the log file on the filesystem where logs should be saved.

Send a POST request to the route with sensitive information in headers:

```
curl -i "http://127.0.0.1:9080/anything" -X POST \
  -H "password: abc" \
  -H "token: xyz" \
  -H "card: 1234-1234-1234-1234"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigating to the `/tmp/mask-header.log` file and examining the log content, you should see a log entry similar to the following:

```
{
  "request": {
    "uri": "/anything",
    "method": "GET",
    "url": "http://127.0.0.1:9080/anything",
    "headers": {
      "user-agent": "curl/8.6.0",
      "token": "*****",
      "card": "1234-****-****-1234"
    }
  }
}
```

### Mask Sensitive Information in URL-Encoded Request Bodies[â](#mask-sensitive-information-in-url-encoded-request-bodies "Direct link to Mask Sensitive Information in URL-Encoded Request Bodies")

The following example demonstrates how you can mask sensitive information in URL-encoded request bodies, before the request is logged to a local file by the `file-logger` plugin.

Create a route with the `file-logger` plugin to log requests and the `data-mask` plugin with three data masking rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "data-mask-route",
    "uri": "/anything",
    "plugins": {
      "data-mask": {
        "request": [
          {
            "action": "remove",
            "body_format": "urlencoded",
            "name": "password",
            "type": "body"
          },
          {
            "action": "replace",
            "body_format": "urlencoded",
            "name": "token",
            "type": "body",
            "value": "*****"
          },
          {
            "action": "regex",
            "body_format": "urlencoded",
            "name": "card",
            "regex": "(\\d+)\\-\\d+\\-\\d+\\-(\\d+)",
            "type": "body",
            "value": "$1-****-****-$2"
          }
        ]
      },
      "file-logger": {
        "include_req_body": true,
        "path": "/tmp/mask-urlencoded-body.log"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ data masking rule to remove `password` information from the request body.

â· data masking rule to replace `token` information in the request body with `*****`.

â¸ data masking rule that matches card number in the request body with RegEx and mask the middle portion of the card number.

â¹ path to the log file on the filesystem where logs should be saved.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything" \
  --data-urlencode "password=abc" \
  --data-urlencode "token=xyz" \
  --data-urlencode "card=1234-1234-1234-1234"
```

You should receive an `HTTP/1.1 200 OK` response.

Navigating to the `/tmp/mask-urlencoded-body.log` file and examining the log content, you should see a log entry similar to the following:

```
{
  "request": {
    "uri": "/anything",
    "body": "token=*****&card=1234-****-****-1234",
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything"
  }
}
```

### Mask Sensitive Information in JSON-Encoded Request Bodies[â](#mask-sensitive-information-in-json-encoded-request-bodies "Direct link to Mask Sensitive Information in JSON-Encoded Request Bodies")

The following example demonstrates how you can mask sensitive information in JSON-encoded request bodies using [JSON path](https://goessner.net/articles/JsonPath) syntax in the plugin to look for the target field, before the request is logged to a local file by the `file-logger` plugin.

Create a route with the `file-logger` plugin to log requests and the `data-mask` plugin with three data masking rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "data-mask-route",
    "uri": "/anything",
    "plugins": {
      "data-mask": {
        "request": [
          {
            "action": "remove",
            "body_format": "json",
            "name": "$.password",
            "type": "body"
          },
          {
            "action": "replace",
            "body_format": "json",
            "name": "users[*].token",
            "type": "body",
            "value": "*****"
          },
          {
            "action": "regex",
            "body_format": "json",
            "name": "$.users[*].credit.card",
            "regex": "(\\d+)\\-\\d+\\-\\d+\\-(\\d+)",
            "type": "body",
            "value": "$1-****-****-$2"
          }
        ]
      },
      "file-logger": {
        "path": "/tmp/mask-json-body.log"
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

â¶ data masking rule to remove `password` information from the request body.

â· data masking rule to replace `token` information in the request body with `*****`.

â¸ data masking rule that matches card number in the request body with RegEx and mask the middle portion of the card number.

â¹ path to the log file on the filesystem where logs should be saved.

Send a request to the route with sensitive information in the request body:

```
curl -i "http://127.0.0.1:9080/anything" -X POST -d '
{
  "password": "abc",
  "users": [
    {
      "token": "xyz",
      "credit": {
        "card": "1234-1234-1234-1234"
      }
    },
    {
      "token": "xyz",
      "credit": {
        "card": "1234-1234-1234-1234"
      }
    }
  ]
}'
```

You should receive an `HTTP/1.1 200 OK` response.

Navigating to the `/tmp/mask-json-body.log` file and examining the log content, you should see a log entry similar to the following:

```
{
  "request": {
    "uri": "/anything",
    "body": "{\"users\":[{\"token\":\"*****\",\"credit\":{\"card\":\"1234-****-****-1234\"}},{\"token\":\"*****\",\"credit\":{\"card\":\"1234-****-****-1234\"}}]}",
    "method": "POST",
    "url": "http://127.0.0.1:9080/anything"
  }
}
```
