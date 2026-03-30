# Source: https://docs.api7.ai/hub/chaitin-waf.md

# chaitin-waf

The `chaitin-waf` plugin integrates with the Chaitin WAF (SafeLine) service to provide advanced detection and prevention of web-based threats, enhancing application security and protecting sensitive user data.

<!-- -->

## Response Headers[â](#response-headers "Direct link to Response Headers")

The plugin can add the following response headers, depending on the configuration of `append_waf_resp_header` and `append_waf_debug_header`:

| Header                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `X-APISIX-CHAITIN-WAF`        | Indicates whether APISIX forwarded the request to the WAF server.<br />â¢ `yes`: Request was forwarded to the WAF server.<br />â¢ `no`: Request was not forwarded to the WAF server.<br />â¢ `unhealthy`: Request matches the configured rules, but no WAF service is available.<br />â¢ `err`: An error occurred during plugin execution. The `X-APISIX-CHAITIN-WAF-ERROR` header is also included with details.<br />â¢ `waf-err`: Error while interacting with the WAF server. The `X-APISIX-CHAITIN-WAF-ERROR` header is also included with details.<br />â¢ `timeout`: Request to the WAF server timed out. |
| `X-APISIX-CHAITIN-WAF-TIME`   | Round-trip time (RTT) in milliseconds for the request to the Chaitin WAF server, including both network latency and WAF server processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `X-APISIX-CHAITIN-WAF-STATUS` | Status code returned to APISIX by the WAF server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `X-APISIX-CHAITIN-WAF-ACTION` | Action returned to APISIX by the WAF server.<br />â¢ `pass`: Request was allowed by the WAF service.<br />â¢ `reject`: Request was blocked by the WAF service.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `X-APISIX-CHAITIN-WAF-ERROR`  | Debug header. Contains WAF error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `X-APISIX-CHAITIN-WAF-SERVER` | Debug header. Indicates which WAF server was selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `chaitin-waf` plugin for different scenarios.

Before proceeding, make sure you have installed [Chaitin WAF (SafeLine)](https://docs.waf.chaitin.com/en/GetStarted/Deploy).

### Block Malicious Requests on a Route[â](#block-malicious-requests-on-a-route "Direct link to Block Malicious Requests on a Route")

The following example demonstrates how to integrate with Chaitin WAF to protect traffic on a route, rejecting malicious requests immediately.

Configure the Chaitin WAF connection details using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) (update the address accordingly):

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/chaitin-waf" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "nodes": [
      {
        "host": "172.22.222.5",
        "port": 8000
      }
    ]
  }'
```

Create a route and enable `chaitin-waf` on the route to block requests identified to be malicious:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "chaitin-waf-route",
    "uri": "/anything",
    "plugins": {
      "chaitin-waf": {
        "mode": "block",
        "append_waf_resp_header": true,
        "append_waf_debug_header": true
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

â¶ Set `mode` to `block` to block requests identified to be malicious.

â· Set `append_waf_resp_header` to `true` to include WAF-related standard response headers.

â¸ Set `append_waf_debug_header` to `true` to include WAF-related debugging response headers.

Send a standard request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a request with SQL injection to the route:

```
curl -i "http://127.0.0.1:9080/anything" -d 'a=1 and 1=1'
```

You should see an `HTTP/1.1 403 Forbidden` response similar to the following:

```
...
X-APISIX-CHAITIN-WAF-STATUS: 403
X-APISIX-CHAITIN-WAF-ACTION: reject
X-APISIX-CHAITIN-WAF-SERVER: 172.22.222.5
X-APISIX-CHAITIN-WAF: yes
X-APISIX-CHAITIN-WAF-TIME: 3
...

{"code": 403, "success":false, "message": "blocked by Chaitin SafeLine Web Application Firewall", "event_id": "276be6457d8447a4bf1f792501dfba6c"}
```

### Monitor Requests for Malicious Intent[â](#monitor-requests-for-malicious-intent "Direct link to Monitor Requests for Malicious Intent")

This example shows how to integrate with Chaitin WAF to monitor all routes with `chaitin-waf` without rejection, and to reject potentially malicious requests on a specific route.

Configure the Chaitin WAF connection details using [plugin metadata](https://docs.api7.ai/apisix/key-concepts/plugin-metadata.md) (update the address accordingly) and configure the mode:

```
curl "http://127.0.0.1:9180/apisix/admin/plugin_metadata/chaitin-waf" -X PUT \
  -H 'X-API-KEY: ${ADMIN_API_KEY}' \
  -d '{
    "nodes": [
      {
        "host": "172.22.222.5",
        "port": 8000
      }
    ],
    "mode": "monitor"
  }'
```

â¶ Set `mode` to `monitor` in the plugin metadata. This applies to all `chaitin-waf` plugin instances if `mode` is not specified on a route.

Create a route and enable `chaitin-waf` without any configuration on the route:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "chaitin-waf-route",
    "uri": "/anything",
    "plugins": {
      "chaitin-waf": {}
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Send a standard request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a request with SQL injection to the route:

```
curl -i "http://127.0.0.1:9080/anything" -d 'a=1 and 1=1'
```

You should also receive an `HTTP/1.1 200 OK` response as the request is not blocked in the `monitor` mode, but observe the following in the log entry:

```
2025/09/09 11:44:08 [warn] 115#115: *31683 [lua] chaitin-waf.lua:385: do_access(): chaitin-waf monitor mode: request would have been rejected, event_id: 49bed20603e242f9be5ba6f1744bba4b, client: 172.20.0.1, server: _, request: "POST /anything HTTP/1.1", host: "127.0.0.1:9080"
```

If you explicitly configure the `mode` on a route, it will take precedence over the configuration in the plugin metadata. For instance, if you create a route like this:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "chaitin-waf-route",
    "uri": "/anything",
    "plugins": {
      "chaitin-waf": {
        "mode": "block"
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

Send a standard request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a request with SQL injection to the route:

```
curl -i "http://127.0.0.1:9080/anything" -d 'a=1 and 1=1'
```

You should see an `HTTP/1.1 403 Forbidden` response similar to the following:

```
...
X-APISIX-CHAITIN-WAF-STATUS: 403
X-APISIX-CHAITIN-WAF-ACTION: reject
X-APISIX-CHAITIN-WAF: yes
X-APISIX-CHAITIN-WAF-TIME: 3
...

{"code": 403, "success":false, "message": "blocked by Chaitin SafeLine Web Application Firewall", "event_id": "c3eb25eaa7ae4c0d82eb8ceebf3600d0"}
```
