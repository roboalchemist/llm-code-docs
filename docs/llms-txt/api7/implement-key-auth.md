# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md

# Implement Key Authentication

Key authentication is a lightweight and effective method for controlling access to APIs. By issuing unique API keys to consumers, APISIX can identify and authenticate requests without requiring complex token exchanges or user credentials. This method is ideal for use cases where simplicity is a priority, such as protecting internal APIs, enabling access for trusted partners, or logging usage per consumer. However, it should generally be avoided for highly sensitive or public-facing APIs where stronger authentication methods, like OAuth, are more suitable.

In this guide, you will implement a scenario where there are two consumers using [key authentication](https://docs.api7.ai/hub/key-auth.md) to authenticate with APISIX, each with a different rate limiting quota. Once implemented, consumers should have access to the upstream service and forward consumer IDs to the upstream service, opening up options for additional business logics.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* InstallÂ [Docker](https://docs.docker.com/get-docker/).
* InstallÂ [cURL](https://curl.se/)Â to send requests to the services for validation.
* Follow theÂ [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md)Â to start a new APISIX instance in Docker or on Kubernetes.

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

The custom ID will be forwarded to the upstream service, should you wish to implement additional business logics.

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

* Admin API

Create `key-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-key-auth",
    "plugins": {
      "key-auth": {
        "key": "john-key"
      }
    }
  }'
```

Create `key-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-key-auth",
    "plugins": {
      "key-auth": {
        "key": "jane-key"
      }
    }
  }'
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route and enable `key-auth`:

* Admin API

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "key-auth-route",
    "uri": "/anything",
    "plugins": {
      "key-auth": {}
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
curl "http://127.0.0.1:9080/anything" -H 'apikey: john-key'
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
    "X-Credential-Identifier": "cred-john-key-auth",
    "X-Consumer-Custom-Id": "john-doe-junior",
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Generate three requests to the route with `john`'s key:

```
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H 'apikey: john-key' -o /dev/null -s -w "%{http_code}\n") && \
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
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H 'apikey: jane-key' -o /dev/null -s -w "%{http_code}\n") && \
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
curl -i "http://127.0.0.1:9080/anything" -H 'apikey: wrong-key'
```

You should see an `HTTP/1.1 401 Unauthorized` response with the following message:

```
{"message":"Invalid API key in request"}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to implement key authentication. APISIX supports other built-in authentication methods, such as [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), [JWT authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
