# Source: https://docs.api7.ai/hub/opa.md

# OPA

The `opa` plugin supports the integration with [Open Policy Agent (OPA)](https://www.openpolicyagent.org), a unified policy engine and framework that helps defining and enforcing authorization policies. Authorization logics are defined in [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) and stored in OPA.

Once configured, the OPA engine will evaluate the client request to a protected route to determine whether the request should have access to the upstream resource based on the defined policies.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can work with the `opa` plugin for different scenarios.

Before proceeding, you should have a running OPA server, or start a new one in Docker:

```
docker run -d --name opa-server -p 8181:8181 openpolicyagent/opa:1.6.0 run --server --addr :8181 --log-level debug
```

* `run -s` starts OPA as a server.
* `--log-level debug` prints debug information to examine the data APISIX pushes to OPA.

To verify that the OPA server is installed and port is exposed properly, run:

```
curl http://127.0.0.1:8181 | grep Version
```

You should see a response similar to the following:

```
Version: 1.6.0
```

### Implement a Basic Policy[â](#implement-a-basic-policy "Direct link to Implement a Basic Policy")

The following example implements a basic authorization policy in OPA to allow only GET requests.

Create an OPA policy that only allows HTTP GET requests:

```
curl "http://127.0.0.1:8181/v1/policies/getonly" -X PUT  \
  -H "Content-Type: text/plain" \
  -d '
package getonly

default allow = false

allow if {
    input.request.method == "GET"
}'
```

Create a route with the `opa` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "opa-route",
    "uri": "/anything",
    "plugins": {
      "opa": {
        "host": "http://192.168.2.104:8181",
        "policy": "getonly"
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

â¶ Configure the OPA server address. Replace with your IP address.

â· Set the authorization policy to be `getonly`.

To verify the policy, send a GET request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send another request to the route using PUT:

```
curl -i "http://127.0.0.1:9080/anything" -X PUT
```

You should receive an `HTTP/1.1 403 Forbidden` response.

### Understand Data Format[â](#understand-data-format "Direct link to Understand Data Format")

The following example helps you understand the data and the format APISIX pushes to OPA to support authorization logic writing. The example continues with the policy and the route in the [last example](#implement-a-basic-policy)

Suppose your OPA server is started with `--log-level debug` and you have completed the verification steps in the [last example](#implement-a-basic-policy) sending requests to the sample route.

Navigate to the OPA server log. You should see an entry similar to the following:

```
{
  "client_addr": "192.168.215.1:58467",
  "level": "info",
  "msg": "Received request.",
  "req_body": "{\"input\":{\"type\":\"http\",\"var\":{\"server_port\":\"9080\",\"timestamp\":1752400020,\"server_addr\":\"192.168.107.3\",\"remote_port\":\"58544\",\"remote_addr\":\"192.168.107.1\"},\"request\":{\"host\":\"127.0.0.1\",\"path\":\"/anything\",\"headers\":{\"host\":\"127.0.0.1:9080\",\"accept\":\"*/*\",\"user-agent\":\"curl/8.6.0\"},\"query\":{},\"port\":9080,\"scheme\":\"http\",\"method\":\"PUT\"}}}",
  "req_id": 12,
  "req_method": "POST",
  "req_params": {},
  "req_path": "/v1/data/getonly",
  "time": "2025-07-14T15:07:00Z"
}
```

where the `req_body` shows the data APISIX pushed:

```
{
  "input": {
    "type": "http",
    "var": {
      "server_port": "9080",
      "timestamp": 1752400020,
      "server_addr": "192.168.107.3",
      "remote_port": "58544",
      "remote_addr": "192.168.107.1"
    },
    "request": {
      "host": "127.0.0.1",
      "path": "/anything",
      "headers": {
        "host": "127.0.0.1:9080",
        "accept": "*/*",
        "user-agent": "curl/8.6.0"
      },
      "query": {},
      "port": 9080,
      "scheme": "http",
      "method": "PUT"
    }
  }
}
```

Now, update the plugin on the [previously created route](#implement-a-basic-policy) to include route information:

```
curl "http://127.0.0.1:9180/apisix/admin/routes/opa-route" -X PATCH \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "plugins": {
      "opa": {
        "with_route": true
      }
    }
  }'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

In the OPA server log, you should see a new entry:

```
{
  "client_addr": "192.168.215.1:43706",
  "level": "info",
  "msg": "Received request.",
  "req_body": "{\"input\":{\"route\":{\"id\":\"opa-route\",\"uri\":\"/anything\",\"update_time\":1752395758,\"plugins\":{\"opa\":{\"keepalive_pool\":5,\"keepalive_timeout\":60000,\"host\":\"http://172.17.1.196:8181\",\"ssl_verify\":true,\"with_route\":true,\"with_service\":false,\"with_consumer\":false,\"timeout\":3000,\"keepalive\":true,\"policy\":\"getonly\"}},\"priority\":0,\"status\":1,\"create_time\":1752393063},\"type\":\"http\",\"var\":{\"server_port\":\"9080\",\"timestamp\":1752396233,\"server_addr\":\"192.168.107.3\",\"remote_port\":\"47838\",\"remote_addr\":\"192.168.107.1\"},\"request\":{\"host\":\"127.0.0.1\",\"path\":\"/anything\",\"headers\":{\"host\":\"127.0.0.1:9080\",\"accept\":\"*/*\",\"user-agent\":\"curl/8.6.0\"},\"query\":{},\"port\":9080,\"scheme\":\"http\",\"method\":\"GET\"}}}",
  "req_id": 14,
  "req_method": "POST",
  "req_params": {},
  "req_path": "/v1/data/getonly",
  "time": "2025-07-13T08:43:53Z"
}
```

The `req_body` now includes route information:

```

{
  "input": {
    "route": {
      "id": "opa-route",
      "uri": "/anything",
      "update_time": 1752395758,
      "plugins": {
        "opa": {
          "keepalive_pool": 5,
          "keepalive_timeout": 60000,
          "host": "http://172.17.1.196:8181",
          "ssl_verify": true,
          "with_route": true,
          "with_service": false,
          "with_consumer": false,
          "timeout": 3000,
          "keepalive": true,
          "policy": "getonly"
        }
      },
      "priority": 0,
      "status": 1,
      "create_time": 1752393063
    },
    "type": "http",
    "var": {
      "server_port": "9080",
      "timestamp": 1752396233,
      "server_addr": "192.168.107.3",
      "remote_port": "47838",
      "remote_addr": "192.168.107.1"
    },
    "request": {
      "host": "127.0.0.1",
      "path": "/anything",
      "headers": {
        "host": "127.0.0.1:9080",
        "accept": "*/*",
        "user-agent": "curl/8.6.0"
      },
      "query": {},
      "port": 9080,
      "scheme": "http",
      "method": "GET"
    }
  }
}
```

### Return Custom Response[â](#return-custom-response "Direct link to Return Custom Response")

The following example demonstrates how you can return custom response code and message when the request is unauthorized.

Create an OPA policy that only allows HTTP GET requests and return `302` with a custom message the request is unauthorized:

```
curl "127.0.0.1:8181/v1/policies/customresp" -X PUT \
  -H "Content-Type: text/plain" \
  -d '
package customresp

default allow = false

allow if {
  input.request.method == "GET"
}

reason := "The resource has temporarily moved. Please follow the new URL." if {
  not allow
}

headers := {
  "Location": "http://example.com/auth"
} if {
  not allow
}

status_code := 302 if {
  not allow
}
'
```

Create a route with the `opa` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "opa-route",
    "uri": "/anything",
    "plugins": {
      "opa": {
        "host": "http://192.168.2.104:8181",
        "policy": "customresp"
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

â¶ Configure the OPA server address. Replace with your IP address.

â· Set the authorization policy to be `customresp`.

Send a GET request to the route:

```
curl -i "http://127.0.0.1:9080/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a POST request to the route:

```
curl -i "http://127.0.0.1:9080/anything" -X POST
```

You should receive an `HTTP/1.1 302 Moved Temporarily` response:

```
HTTP/1.1 302 Moved Temporarily
...
Location: http://example.com/auth

The resource has temporarily moved. Please follow the new URL.
```

### Implement RBAC[â](#implement-rbac "Direct link to Implement RBAC")

The following example demonstrates how to implement authentication and RBAC using the [`jwt-auth`](https://docs.api7.ai/hub/jwt-auth.md) and `opa` plugins. You will be implementing RBAC logics such that:

* An `user` role can only read the upstream resources.
* An `admin` role can read and write the upstream resources.

Create an OPA policy for RBAC of two example consumers, where `john` has the `user` role and `jane` has the `admin` role:

```
curl "http://127.0.0.1:8181/v1/policies/rbac" -X PUT \
  -H "Content-Type: text/plain" \
  -d '
package rbac

# Assign roles to users
user_roles := {
  "john": ["user"],
  "jane": ["admin"]
}

# Map permissions to HTTP methods
permission_methods := {
  "read": "GET",
  "write": "POST"
}

# Assign role permissions
role_permissions := {
  "user": ["read"],
  "admin": ["read", "write"]
}

# Get JWT authorization token
bearer_token := t if {
  t := input.request.headers.authorization
}

# Decode the token to get role and permission
token := {"payload": payload} if {
  [_, payload, _] := io.jwt.decode(bearer_token)
}

# Normalize permission to a list
normalized_permissions := ps if {
  ps := token.payload.permission
  not is_string(ps)
}

normalized_permissions := [ps] if {
  ps := token.payload.permission
  is_string(ps)
}

# Implement RBAC logic
default allow = false

allow if {
  # Look up the list of roles for the user
  roles := user_roles[input.consumer.username]

  # For each role in that list
  r := roles[_]

  # Look up the permissions list for the role
  permissions := role_permissions[r]

  # For each permission
  p := permissions[_]

  # Check if the permission matches the request method
  permission_methods[p] == input.request.method

  # Check if the normalized permissions include the permission
  p in normalized_permissions
}
'
```

Create two consumers `john` and `jane` in APISIX:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "john"
}'
```

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "jane"
}'
```

Configure the `jwt-auth` credentials for the consumers, using the default algorithm `HS256`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT \
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

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/jane/credentials" -X PUT \
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

Create a route and configure the `jwt-auth` and `opa` plugins as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "opa-route",
    "methods": ["GET", "POST"],
    "uris": ["/get","/post"],
    "plugins": {
      "jwt-auth": {},
      "opa": {
        "host": "http://192.168.2.104:8181",
        "policy": "rbac",
        "with_consumer": true
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

â¶ Enable the `jwt-auth` plugin on the route.

â· Configure the OPA server address. Replace with your IP address.

â¸ Set the authorization policy to be `rbac`.

â¹ Set `with_consumer` to true to send cnosumer information.

#### Verify as `john`[â](#verify-as-john "Direct link to verify-as-john")

To issue a JWT for `john`, you could use [JWT.io's JWT encoder](https://jwt.io) or other utilities. If you are using [JWT.io's JWT encoder](https://jwt.io), do the following:

* Fill in `HS256` as the algorithm.
* Update the secret in the **Valid secret** section to be `john-hs256-secret-that-is-very-long`.
* Update payload with role `user`, permission `read`, and consumer key `john-key`; as well as `exp` or `nbf` in UNIX timestamp.

note

If you are using API7 Enterprise, the requirement of `exp` or `nbf` is not mandatory. You can optionally include these claims and use the `claims_to_verify` parameter to configure which claim to verify.

Your payload should look similar to the following:

```
{
  "role": "user",
  "permission": "read",
  "key": "john-key",
  "nbf": 1729132271
}
```

Copy the generated JWT and save to a variable:

```
export john_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsInBlcm1pc3Npb24iOiJyZWFkIiwia2V5Ijoiam9obi1rZXkiLCJuYmYiOjE3MjkxMzIyNzF9.rAHMTQfnnGFnKYc3am_lpE9pZ9E8EaOT_NBQ5Ss8pk4
```

Send a GET request to the route with the JWT of `john`:

```
curl -i "http://127.0.0.1:9080/get" -H "Authorization: ${john_jwt_token}"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a POST request to the route with the same JWT:

```
curl -i "http://127.0.0.1:9080/post" -X POST -H "Authorization: ${john_jwt_token}"
```

You should receive an `HTTP/1.1 403 Forbidden` response.

#### Verify as `jane`[â](#verify-as-jane "Direct link to verify-as-jane")

Similarly, to issue a JWT for `jane`, you could use [JWT.io's JWT encoder](https://jwt.io) or other utilities. If you are using [JWT.io's JWT encoder](https://jwt.io), do the following:

* Fill in `HS256` as the algorithm.
* Update the secret in the **Valid secret** section to be `jane-hs256-secret-that-is-very-long`.
* Update payload with role `admin`, permission `["read","write"]`, and consumer key `jane-key`; as well as `exp` or `nbf` in UNIX timestamp.

note

If you are using API7 Enterprise, the requirement of `exp` or `nbf` is not mandatory. You can optionally include these claims and use the `claims_to_verify` parameter to configure which claim to verify.

Your payload should look similar to the following:

```
{
  "role": "admin",
  "permission": ["read","write"],
  "key": "jane-key",
  "nbf": 1729132271
}
```

Copy the generated JWT and save to a variable:

```
export jane_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJwZXJtaXNzaW9uIjpbInJlYWQiLCJ3cml0ZSJdLCJrZXkiOiJqYW5lLWtleSIsIm5iZiI6MTcyOTEzMjI3MX0.meZ-AaGHUPwN_GvVOE3IkKuAJ1wqlCguaXf3gm3Ww8s
```

Send a GET request to the route with the JWT of `jane`:

```
curl -i "http://127.0.0.1:9080/get" -H "Authorization: ${jane_jwt_token}"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a POST request to the route with the same JWT:

```
curl -i "http://127.0.0.1:9080/post" -X POST -H "Authorization: ${jane_jwt_token}"
```

You should also receive an `HTTP/1.1 200 OK` response.

tip

To examine whether the authorization decision comes from OPA, you should observe the following log in the OPA server if you have set `--log-level debug`:

```
{
  "result":{
    "allow": true,
    "bearer_token": "eyJ...",
    ...
  }
}
```
