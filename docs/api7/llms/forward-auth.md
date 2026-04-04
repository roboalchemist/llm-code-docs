# Source: https://docs.api7.ai/hub/forward-auth.md

# forward-auth

The `forward-auth` plugin supports the integration with an external authorization service for authentication and authorization. If the authentication fails, a customizable error message will be returned to the client. If the authentication succeeds, the request will be forwarded to the upstream service along with the following request headers that APISIX added:

* `X-Forwarded-Proto`: scheme
* `X-Forwarded-Method`: HTTP method
* `X-Forwarded-Host`: host
* `X-Forwarded-Uri`: URI
* `X-Forwarded-For`: source IP

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can use `forward-auth` for different scenarios.

To follow along the first two examples, please have your external authorization service set up, or create a mock auth service using the [serverless function plugin](https://docs.api7.ai/hub/serverless-functions.md) as shown below:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "auth-mock",
    "uri": "/auth",
    "plugins": {
      "serverless-pre-function": {
        "phase": "rewrite",
        "functions": [
          "return function (conf, ctx)
            local core = require(\"apisix.core\");
            local authorization = core.request.header(ctx, \"Authorization\");
            if authorization == \"123\" then
              core.response.exit(200);
            elseif authorization == \"321\" then
              core.response.set_header(\"X-User-ID\", \"i-am-user\");
              core.response.exit(200);
            else core.response.set_header(\"X-Forward-Auth\", \"Fail\");
              core.response.exit(403);
            end
          end"
        ]
      }
    }
  }'
```

The function above implements the following logics:

â¶ If the `Authorization` header has a value of `123`, respond with `200 OK`;

â· If the `Authorization` header has a value of `321`, set a header `X-User-ID: i-am-user` and respond with `200 OK`;

â¸ Otherwise, set a header `X-Forward-Auth: Fail` and respond with `403 Forbidden`.

### Forward Designated Headers to Upstream Resource[â](#forward-designated-headers-to-upstream-resource "Direct link to Forward Designated Headers to Upstream Resource")

The following example demonstrates how to set up `forward-auth` on a route to regulate client access to the resources upstream based on a value in the request header. It also allows passing a specific header from the authorization service to the upstream resource.

Create a route with the `forward-auth` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "forward-auth-route",
    "uri": "/headers",
    "plugins": {
      "forward-auth": {
        "uri": "http://127.0.0.1:9080/auth",
        "request_headers": ["Authorization"],
        "upstream_headers": ["X-User-ID"]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ The URI of the authorization service.

â· The request header that should be forwarded to the authorization service.

â¸ The request header set by the authorization service that should be forwarded to the upstream resource when the authorization succeeds.

Send a request to the route with authorization detail in the header:

```
curl "http://127.0.0.1:9080/headers" -H 'Authorization: 123'
```

You should see an `HTTP/1.1 200 OK` response of the following:

```
{
  "headers": {
    "Accept": "*/*", 
    "Authorization": "123", 
    ...
  }
}
```

To verify if the `X-User-ID` header set by the authorization service will be forwarded to the upstream service, send a request to the route with the corresponding authorization detail:

```
curl "http://127.0.0.1:9080/headers" -H 'Authorization: 321'
```

You should see an `HTTP/1.1 200 OK` response of the following, showing the header is forwarded to the upstream:

```
{
  "headers": {
    "Accept": "*/*", 
    "Authorization": "123",
    "X-User-ID": "i-am-user",
    ...
  }
}
```

### Return Designated Headers to Clients on Authentication Failure[â](#return-designated-headers-to-clients-on-authentication-failure "Direct link to Return Designated Headers to Clients on Authentication Failure")

The following example demonstrates how you can configure `forward-auth` on a route to regulate client access to the upstream resources. It also passes a specific header returned by the authorization service to the client when the authentication fails.

Create a route with the `forward-auth` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "forward-auth-route",
    "uri": "/headers",
    "plugins": {
      "forward-auth": {
        "uri": "http://127.0.0.1:9080/auth",
        "request_headers": ["Authorization"],
        "client_headers": ["X-Forward-Auth"]
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ Pass the `X-Forward-Auth` header from the authorization service back to the client when authentication fails.

Send a request without any authentication information:

```
curl -i "http://127.0.0.1:9080/headers"
```

You should receive an `HTTP/1.1 403 Forbidden` response:

```
...
X-Forward-Auth: Fail
Server: APISIX/3.x.x

<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>openresty</center>
<p><em>Powered by <a href="https://apisix.apache.org/">APISIX</a>.</em></p></body>
</html>
```

### Authorize Based on POST Body[â](#authorize-based-on-post-body "Direct link to Authorize Based on POST Body")

This example demonstrates how to configure the `forward-auth` plugin to control access based on POST body data, pass values as headers to the authorization service, and reject the request when authorization failed per the body data.

Please have your external authorization service set up, or create a mock auth service using the [serverless function plugin](https://docs.api7.ai/hub/serverless-functions.md). The function checks if the `tenant_id` header is `123` and returns `200 OK` if it is, otherwise it returns 403 with an error message.

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "auth-mock",
    "uri": "/auth",
    "plugins": {
      "serverless-pre-function": {
        "phase": "rewrite",
        "functions": [
          "return function(conf, ctx)
            local core = require(\"apisix.core\")
            local tenant_id = core.request.header(ctx, \"tenant_id\")
            if tenant_id == \"123\" then
              core.response.exit(200);
          else
            core.response.exit(403, \"tenant_id is \"..tenant_id .. \" but expecting 123\");
          end
        end"
        ]
      }
    }
  }'
```

Create a route with the `forward-auth` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "forward-auth-route",
    "uri": "/post",
    "methods": ["POST"],
    "plugins": {
      "forward-auth": {
        "uri": "http://127.0.0.1:9080/auth",
        "request_method": "GET",
        "extra_headers": {"tenant_id": "$post_arg.tenant_id"}
      }
    },
    "upstream": {
      "nodes": {
        "httpbin.org:80": 1
      },
      "type": "roundrobin"
    }
  }'
```

â¶ Set an extra header `tenant_id` using the value from the POST parameter `tenant_id`.

Send a POST request with `tenant_id` in the body:

```
curl -i "http://127.0.0.1:9080/post" -X POST -d '
{
  "tenant_id": "123"
}'
```

You should receive an `HTTP/1.1 200 OK` response.

Send a POST request with `tenant_id` in the body:

```
curl -i "http://127.0.0.1:9080/post" -X POST -d '
{
  "tenant_id": "000"
}'
```

You should receive an `HTTP/1.1 403 Forbidden` response of the following:

```
tenant_id is 000 but expecting 123
```
