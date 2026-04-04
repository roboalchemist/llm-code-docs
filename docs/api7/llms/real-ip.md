# Source: https://docs.api7.ai/hub/real-ip.md

# real-ip

The `real-ip` plugin allows APISIX to set the client's real IP by IP address passed in the HTTP header or HTTP query string. This is particularly useful when APISIX is behind a reverse proxy, since the proxy could act as the request originating client otherwise.

The plugin is functionally similar to NGINX's [ngx\_http\_realip\_module](https://nginx.org/en/docs/http/ngx_http_realip_module.html) but offers more flexibilities.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure `real-ip` in different scenarios.

### Obtain Real Client Address From URI Parameter[â](#obtain-real-client-address-from-uri-parameter "Direct link to Obtain Real Client Address From URI Parameter")

The following example demonstrates how to update client IP address with an URI parameter.

Create a route as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "real-ip-route",
    "uri": "/get",
    "plugins": {
      "real-ip": {
        "source": "arg_realip",
        "trusted_addresses": ["127.0.0.0/24"]
      },
      "response-rewrite": {
        "headers": {
          "remote_addr": "$remote_addr",
          "remote_port": "$remote_port"
        }
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

â¶ Configure `source` to obtain value from the URL parameter `realip` using the [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md).

â· Use the `response-rewrite` plugin to set response headers to verify if the client IP and port were actually updated.

Send a request to the route with real IP and port in the URL parameter:

```
curl -i "http://127.0.0.1:9080/get?realip=1.2.3.4:9080"
```

You should see the response includes the following header:

```
remote-addr: 1.2.3.4
remote-port: 9080
```

### Obtain Real Client Address From Header[â](#obtain-real-client-address-from-header "Direct link to Obtain Real Client Address From Header")

The following example shows how to set the real client IP when APISIX is behind a reverse proxy, such as a load balancer, when the proxy exposes the real client IP in the [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header.

Create a route as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "real-ip-route",
    "uri": "/get",
    "plugins": {
      "real-ip": {
        "source": "http_x_forwarded_for",
        "trusted_addresses": ["127.0.0.0/24"]
      },
      "response-rewrite": {
        "headers": {
          "remote_addr": "$remote_addr"
        }
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

â¶ Configure `source` to obtain value from the request header `X-Forwarded-For` using the [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md).

â· Use the `response-rewrite` plugin to set a response header to verify if the client IP was actually updated.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/get"
```

You should see a response including the following header:

```
remote-addr: 10.26.3.19
```

The IP address should correspond to the IP address of the request originating client.

### Obtain Real Client Address Behind Multiple Proxies[â](#obtain-real-client-address-behind-multiple-proxies "Direct link to Obtain Real Client Address Behind Multiple Proxies")

The following example shows how to get the real client IP when APISIX is behind multiple proxies, which causes [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header to include a list of proxy IP addresses.

Create a route as follows:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
  "id": "real-ip-route",
  "uri": "/get",
  "plugins": {
    "real-ip": {
      "source": "http_x_forwarded_for",
      "recursive": true,
      "trusted_addresses": ["192.128.0.0/16", "127.0.0.0/24"]
    },
    "response-rewrite": {
      "headers": {
        "remote_addr": "$remote_addr"
      }
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

â¶ Configure `source` to obtain value from the request header `X-Forwarded-For` using the [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md).

â· Set `recursive` to `true` so that the original client address that matches one of the trusted addresses is replaced by the last non-trusted address sent in the configured `source`.

â¸ Use the `response-rewrite` plugin to set a response header to verify if the client IP was actually updated.

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/get" \
  -H "X-Forwarded-For: 127.0.0.2, 192.128.1.1, 127.0.0.1" 
```

You should see a response including the following header:

```
remote-addr: 127.0.0.2
```
