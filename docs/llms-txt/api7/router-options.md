# Source: https://docs.api7.ai/apisix/reference/router-options.md

# Router Options

In APISIX, there are three HTTP router options:

1. `radixtree_host_uri` routes requests by hosts and URI paths, prioritizing hostnames over URI paths during matching. This is the default setting and the behaviour is the same as NGINX.

2. `radixtree_uri` routes requests by hosts and URI paths, prioritizing URI paths over hostnames during matching.

3. `radixtree_uri_with_parameter` supports the use of parameters in path matching.

These router options can be configured in `conf/config.yaml` under `apisix.router.http`.

## `radixtree_host_uri`[â](#radixtree_host_uri "Direct link to radixtree_host_uri")

This is the default router setting, which prioritizes hostnames over URI paths when route matching. If you would like to explicitly configure the option, add the following block to your configuration file:

config.yaml

```
apisix:
  router:
    http: radixtree_host_uri
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

Configuring two routes with the same URI but different matching hosts is useful for scenarios like multi-tenant SaaS platforms, where each tenant is served through a custom subdomain. For example, both tenants may access the same endpoint, but the requests are routed to different upstream services based on the host.

To do so, you can configure two routes with the same matching URI but different matching hosts and upstream services:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "httpbin-host-test1",
    "uri": "/get",
    "host": "test1.com",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "postman-host-test2",
    "uri": "/get",
    "host": "test2.com",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "postman-echo.com:80": 1
      }
    }
  }'
```

Send a request that matches the host of the first route:

```
curl "http://127.0.0.1:9080/get" -H 'host: test1.com'
```

You should see a response from `httpbin.org`:

```
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "test1.com", 
    "User-Agent": "curl/8.6.0", 
    "X-Amzn-Trace-Id": "Root=1-6746c0bf-653fac896be8818275f1e8da", 
    "X-Forwarded-Host": "test1.com"
  }, 
  "origin": "192.168.65.1, 43.252.208.90", 
  "url": "http://test1.com/get"
}
```

Send a request that matches the host of the second route:

```
curl "http://127.0.0.1:9080/get" -H 'host: test2.com'
```

You should see a response from `postman-echo.com`:

```
{
  "args": {},
  "headers": {
    "host": "test2.com",
    "x-request-start": "t=1732834286",
    "connection": "close",
    "x-forwarded-proto": "http",
    "x-forwarded-port": "80",
    "x-amzn-trace-id": "Root=1-6746c0ca-2b0b323902e784f512051ef6",
    "x-forwarded-host": "test2.com",
    "user-agent": "curl/8.6.0",
    "accept": "*/*"
  },
  "url": "http://test2.com/get"
}
```

To understand the behaviour more, create a third route that matches all requests:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mock-api7-all",
    "uri": "/*",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "mock.api7.ai:443": 1
      },
      "scheme": "https",
      "pass_host": "node"
    }
  }'
```

Send a request with a random host name:

```
curl "http://127.0.0.1:9080/get" -H 'host: random.com'
```

You should see the request is forwarded to the third route:

```
API7.ai, the creator of Apache APISIX, delivers a cloud-native API Gateway solution for the Enterprise, to help you maximize the value of APIs.
```

Send another request that matches the host of the first route:

```
curl "http://127.0.0.1:9080/get" -H 'host: test1.com'
```

You should see the request is forwarded to the `httpbin.org` upstream. This demonstrates how the router prioritizes hostnames in routing when it is set to `radixtree_host_uri`.

## `radixtree_uri`[â](#radixtree_uri "Direct link to radixtree_uri")

`radixtree_uri` prioritizes URI paths over hostnames when route matching. To use `radixtree_uri` as the HTTP router setting, add the following block to your configuration file:

config.yaml

```
apisix:
  router:
    http: radixtree_uri
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

To understand the behaviour, create a route that matches `test1.com` host and all URI paths:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "httpbin-host-test1",
    "uri": "/*",
    "host": "test1.com",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Create another route that matches requests to `/get`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "mock-api7-all",
    "uri": "/get",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "mock.api7.ai:443": 1
      },
      "scheme": "https",
      "pass_host": "node"
    }
  }'
```

Send a request to `/get` with `test1.com` host:

```
curl "http://127.0.0.1:9080/get" -H 'host: test1.com'
```

You should see the request is forwarded to `mock.api7.ai`

```
API7.ai, the creator of Apache APISIX, delivers a cloud-native API Gateway solution for the Enterprise, to help you maximize the value of APIs.
```

This shows the hostname is not being prioritized when router operates in `radixtree_uri` mode and full path matching takes the [priority](#matching-priority).

Send another request to `/anything` with `test1.com` host:

```
curl "http://127.0.0.1:9080/anything" -H 'host: test1.com'
```

You should see the request is forwarded to the `httpbin.org` upstream.

## `radixtree_uri_with_parameter`[â](#radixtree_uri_with_parameter "Direct link to radixtree_uri_with_parameter")

`radixtree_uri_with_parameter` supports the use of parameters when route matching. To use `radixtree_uri_with_parameter` as the HTTP router setting, add the following block to your configuration file:

config.yaml

```
apisix:
  router:
    http: radixtree_uri_with_parameter
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

A common use case is extracting a part of the URI path and using it to construct the request sent to upstream services. This can be used to rewrite the URL path or set a custom header, enabling flexible dynamic routing and request customization based on client input. The matched URI path can be easily extracted with `uri_param_<parameter_name>`.

For example, you can match a URI path like `/user/123/profile`, extract the user ID `123`, and forward the value to the upstream service in a new header.

To do so, create a route as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "httpbin",
    "uri": "/anything/user/:user_id/profile",
    "plugins":{
      "proxy-rewrite": {
        "headers": {
          "set": {
            "X-User-ID": "$uri_param_user_id"
          }
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

â¶ Match requests to `/anything/user/:user_id/profile` where `user_id` is a parameter.

â· Assign the `user_id` parameter value to a new header `X-User-ID`.

To verify, send a request to the route:

```
curl "http://127.0.0.1:9080/anything/user/123/profile"
```

You should see the following response:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*",
    "Host": "127.0.0.1",
    "User-Agent": "curl/8.6.0",
    "X-Amzn-Trace-Id": "Root=1-68873cf5-7248f64d19d607ea50aa9735",
    "X-Forwarded-Host": "127.0.0.1",
    "X-User-Id": "123"
  }, 
  ...
}
```

The route parameter can also accept URL-encoded string. For instance, if you send a request as such:

```
curl -i "http://127.0.0.1:9080/anything/user/123%20456/profile"
```

The user ID would be extracted as `123 456`:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "127.0.0.1", 
    "User-Agent": "curl/8.6.0",
    "X-Amzn-Trace-Id": "Root=1-68873d37-7634825b20d05dee3a852cb9",
    "X-Forwarded-Host": "127.0.0.1",
    "X-User-Id": "123 456"
  }, 
  ...
}
```

## Understand Route Matching[â](#understand-route-matching "Direct link to Understand Route Matching")

APISIX leverages the [luaradixtree](https://github.com/api7/lua-resty-radixtree) library for routing, an adaptive radix tree implemented in Lua for OpenResty. It utilizes the Foreign Function Interface (FFI) to integrate with [rax](https://github.com/antirez/rax), ensuring efficient and high-performance routing.

There are several ways of route matching.

### Full Path[â](#full-path "Direct link to Full Path")

Suppose the route URI is:

```
/anything/foo
```

The route will only match requests to `/anything/foo`.

### Wildcard[â](#wildcard "Direct link to Wildcard")

Suppose the route URI is:

```
/anything/*
```

The route will match any request to sub-paths of `/anything`, such as `/anything/foo` and `/anything/bar`. Note that it will not match requests to `/anything`.

The wildcard does not need to be at the end of the URI. You can also have a route URI as such:

```
/*/*/test
```

This will match requests with URIs like `/anything/foo/test`.

### Matching Priority[â](#matching-priority "Direct link to Matching Priority")

Full path matching has a higher priority than wildcard matching. Suppose you have two routes with URI `/anything/foo` and `/anything/*` respectively. The request to `/anything/foo` will be matched by the `/anything/foo` route, instead of the `/anything/*` route.
