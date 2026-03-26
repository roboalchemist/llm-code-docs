# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md

# Implement Basic Authentication

Basic authentication is a widely used method to authenticate clients by validating a username and password combination sent in the request headers. It provides a simple and effective way to secure APIs and is suitable for use cases where ease of implementation is prioritized, such as internal tools, development environments, or APIs with limited access. However, because the credentials are transmitted with every request, basic authentication should always be used over [HTTPS](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-https-between-client-and-apisix.md) to prevent exposure. For scenarios requiring more robust security, such as multi-factor authentication or delegated access, more advanced protocols like OAuth are recommended.

In this guide, you will implement a scenario where there are two consumers using [basic authentication](https://docs.api7.ai/hub/basic-auth.md) to authenticate with APISIX, each with a different rate limiting quota. Once implemented, consumers should have access to the upstream service and forward consumer IDs to the upstream service, opening up options for additional business logic.

## Create Consumers[â](#create-consumers "Direct link to Create Consumers")

A consumer is an application or a developer who consumes the API. You should always create consumers when using APISIX built-in authentication methods.

* Admin API

Create a consumer `johndoe` with an optional custom ID and a rate limiting quota of one request in a 30-second window:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "johndoe",
    "labels": {
      "custom_id": "john-doe-junior"
    },
    "plugins": {
      "limit-count": {
        "count": 1,
        "time_window": 30,
        "rejected_code": 429
      }
    }
  }'
```

The custom ID will be forwarded to the upstream service, should you wish to implement additional business logic.

Create another consumer `janedoe` with an optional custom ID and a rate limiting quota of two requests in a 30-second window:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "janedoe",
    "labels": {
      "custom_id": "jane-doe-senior"
    },
    "plugins": {
      "limit-count": {
        "count": 2,
        "time_window": 30,
        "rejected_code": 429
      }
    }
  }'
```

## Create Consumer Credentials[â](#create-consumer-credentials "Direct link to Create Consumer Credentials")

Credentials are used to configure authentication credentials associated with consumers.

Create `basic-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-basic-auth",
    "plugins": {
      "basic-auth": {
        "username": "johndoe",
        "password": "john-key"
      }
    }
  }'
```

Create `basic-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-basic-auth",
    "plugins": {
      "basic-auth": {
        "username": "janedoe",
        "password": "jane-key"
      }
    }
  }'
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route and enable `basic-auth`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "basic-auth-route",
    "uri": "/anything",
    "plugins": {
      "basic-auth": {}
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with `john`'s key:

```
curl "http://127.0.0.1:9080/anything" -u johndoe:john-key
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {},
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    ...
    "X-Consumer-Username": "johndoe",
    "X-Credential-Identifier": "cred-john-basic-auth",
    "X-Consumer-Custom-Id": "john-doe-junior",
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Generate three requests to the route with `john`'s key:

```
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -u johndoe:john-key -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 3 requests, 1 request was successful while the others were rejected:

```
200:    1, 429:    2
```

Generate three requests to the route with `jane`'s key:

```
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -u janedoe:jane-key -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 3 requests, 2 requests were successful while the other was rejected:

```
200:    2, 429:    1
```

Finally, send a request with an invalid key:

```
curl -i "http://127.0.0.1:9080/anything" -u johndoe:wrong-key
```

You should see an `HTTP/1.1 401 Unauthorized` response with the following message:

```
{"message":"Invalid user authorization"}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to implement basic authentication. APISIX supports other built-in authentication methods, such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
