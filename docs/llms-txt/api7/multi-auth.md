# Source: https://docs.api7.ai/hub/multi-auth.md

# multi-auth

The `multi-auth` plugin allows consumers using different authentication methods to share the same route or service. It supports the configuration of multiple authentication plugins, so that a request would be allowed through if it authenticates successfully against any configured authentication method.

## Examples[â](#examples "Direct link to Examples")

### Allow Different Authentications on the Same Route[â](#allow-different-authentications-on-the-same-route "Direct link to Allow Different Authentications on the Same Route")

The following example demonstrates how to have one consumer using basic authentication, while another consumer using key authentication, both sharing the same route.

Create two consumers:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username":"consumer1"
  }'
```

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username":"consumer2"
  }'
```

Configure basic authentication credential for `consumer1`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/consumer1/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "basic-auth": {
        "username":"consumer1",
        "password":"consumer1_pwd"
      }
    }
  }'
```

Configure key authentication credential for `consumer2`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/consumer2/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "key-auth": {
        "key":"consumer2_pwd"
      }
    }
  }'
```

Create a route with `multi-auth` and configure the two authentication plugins that consumers use:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "multi-auth-route",
    "uri": "/anything",
    "plugins": {
      "multi-auth":{
        "auth_plugins":[
          {
            "basic-auth":{}
          },
          {
            "key-auth":{
              "hide_credentials":true,
              "header":"apikey",
              "query":"apikey"
            }
          }
        ]
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

Send a request to the route with `consumer1` basic authentication credentials:

```
curl -i "http://127.0.0.1:9080/anything" -u consumer1:consumer1_pwd
```

You should receive an `HTTP/1.1 200 OK` response.

Send another request to the route with `consumer2` key authentication credential:

```
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: consumer2_pwd'
```

You should again receive an `HTTP/1.1 200 OK` response.

Send a request to the route without any credential:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 401 Unauthorized` response.

This shows that consumers using different authentication methods are able to authenticate and access the resource behind the same route.
