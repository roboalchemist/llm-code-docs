# Source: https://docs.api7.ai/apisix/how-to-guide/authentication/implement-jwt-auth.md

# Implement JWT Authentication

JWT authentication is a secure and stateless method for authenticating API clients using JSON Web Tokens (JWTs). It involves issuing a signed token to a client after successful authentication, which the client includes in subsequent requests. JWTs encapsulate claims such as user identity and roles, enabling APIs to validate requests without querying a backend database. This approach is ideal for scalable, distributed applications requiring lightweight and fast authentication. However, since JWTs remain valid until they expire, care must be taken to use short expiration times or implement token revocation for added security.

In this guide, you will implement a scenario where there are two consumers using [JWT authentication](https://docs.api7.ai/hub/jwt-auth.md) to authenticate with APISIX, each with a different rate limiting quota. Once implemented, consumers should have access to the upstream service and forward consumer IDs to the upstream service, opening up options for additional business logic.

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

* Admin API

Create `jwt-auth` credential for `johndoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/johndoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-john-jwt-auth",
    "plugins": {
      "jwt-auth": {
        "key": "john-key",
        "secret": "john-hs256-secret-that-is-very-long"
      }
    }
  }'
```

Create `jwt-auth` credential for `janedoe`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/janedoe/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jane-jwt-auth",
    "plugins": {
      "jwt-auth": {
        "key": "jane-key",
        "secret": "jane-hs256-secret-that-is-very-long"
      }
    }
  }'
```

## Create a Route[â](#create-a-route "Direct link to Create a Route")

Create a route and enable `jwt-auth`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "jwt-auth-route",
    "uri": "/anything",
    "plugins": {
      "jwt-auth": {}
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

## Issue JWT[â](#issue-jwt "Direct link to Issue JWT")

To issue a JWT for `johndoe`, you could use [JWT.io's JWT encoder](https://jwt.io) or other utilities. If you are using [JWT.io's JWT encoder](https://jwt.io), do the following:

* Fill in `HS256` as the algorithm.
* Update the secret in the **Valid secret** section to be `john-hs256-secret-that-is-very-long`.
* Update payload with consumer key `john-key`; and add `exp` or `nbf` as a UNIX timestamp.

note

If you are using API7 Enterprise, the requirement of `exp` or `nbf` is not mandatory. You can optionally include these claims and use the `claims_to_verify` parameter to configure which claim to verify.

Your payload should look similar to the following:

```
{
  "key": "john-key",
  "nbf": 1729132271
}
```

Copy the generated JWT and save to a variable:

```
export john_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJqb2huLWtleSIsIm5iZiI6MTcyOTEzMjI3MX0.TgoM2efMEaSX7KrIWujGLGK5dpPGS2nbaiinmVVjKKw
```

Repeat the step for `janedoe` and save the generated JWT to `jane_jwt_token`.

## Verify[â](#verify "Direct link to Verify")

Send a request to the route with `john`'s key:

```
curl -i "http://127.0.0.1:9080/anything" -H "Authorization: ${john_jwt_token}"
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJqb2huLWtleSIsIm5iZiI6MTcyOTEzMjI3MX0.TgoM2efMEaSX7KrIWujGLGK5dpPGS2nbaiinmVVjKKw", 
    "Host": "127.0.0.1", 
    "User-Agent": "curl/8.6.0", 
    "X-Amzn-Trace-Id": "Root=1-6873b51b-5502cfcd72380323266c22e8", 
    "X-Consumer-Custom-Id": "john-doe-junior", 
    "X-Consumer-Username": "johndoe", 
    "X-Credential-Identifier": "cred-john-jwt-auth", 
    "X-Forwarded-Host": "127.0.0.1"
  }, 
  ...
}
```

Generate three requests to the route with `john`'s key:

```
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H "Authorization: ${john_jwt_token}" -o /dev/null -s -w "%{http_code}\n") && \
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
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H "Authorization: ${jane_jwt_token}" -o /dev/null -s -w "%{http_code}\n") && \
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
curl -i "http://127.0.0.1:9080/anything" -H 'Authorization: somewrongkey'
```

You should see an `HTTP/1.1 401 Unauthorized` response with the following message:

```
{"message":"JWT token invalid"}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to implement basic authentication. APISIX supports other built-in authentication methods, such as [key authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-key-auth.md), [basic authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md), and [HMAC authentication](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-hmac-auth.md).
