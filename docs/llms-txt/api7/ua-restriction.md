# Source: https://docs.api7.ai/hub/ua-restriction.md

# ua-restriction

The `ua-restriction` plugin supports restricting access to upstream resources through either configuring an allowlist or denylist of user agents. A common use case is to prevent web crawlers from overloading the upstream resources and causing service degradation.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `ua-restriction` for different scenarios.

### Reject Web Crawlers and Customize Error Message[â](#reject-web-crawlers-and-customize-error-message "Direct link to Reject Web Crawlers and Customize Error Message")

The following example demonstrates how you can configure the plugin to fend off unwanted web crawlers and customize the rejection message.

Create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ua-restriction-route",
    "uri": "/anything",
    "plugins": {
      "ua-restriction": {
        "bypass_missing": false,
        "denylist": [
          "(Baiduspider)/(\\d+)\\.(\\d+)",
          "bad-bot-1"
        ],
        "message": "Access denied"
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

â¶ Do not allow bypassing UA restriction rules.

â· Configure user agents that should not be able to access the upstream resource.

â¸ Customize the error message for when the access is denied.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send another request to the route with a disallowed user agent:

```
curl -i "http://127.0.0.1:9080/anything" -H 'User-Agent: Baiduspider/5.0'
```

You should receive an `HTTP/1.1 403 Forbidden` response with the following message:

```
{"message":"Access denied"}
```

### Bypass UA Restriction Checks[â](#bypass-ua-restriction-checks "Direct link to Bypass UA Restriction Checks")

The following example demonstrates how to configure the plugin to allow requests of a specific user agent to bypass the UA restriction.

Create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "ua-restriction-route",
    "uri": "/anything",
    "plugins": {
      "ua-restriction": {
        "bypass_missing": true,
        "allowlist": [
          "good-bot-1"
        ],
        "message": "Access denied"
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

â¶ Allow bypassing UA restriction rules.

â· Configure user agents that should be allowed to access the upstream resource.

Send a request to the route without modifying the user agent:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 403 Forbidden` response with the following message:

```
{"message":"Access denied"}
```

Send another request to the route with an empty user agent:

```
curl -i "http://127.0.0.1:9080/anything" -H 'User-Agent: '
```

You should receive an `HTTP/1.1 200 OK` response.
