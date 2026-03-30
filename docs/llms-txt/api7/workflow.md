# Source: https://docs.api7.ai/hub/workflow.md

# workflow

The `workflow` plugin supports the conditional execution of user-defined actions to client traffic based a given set of rules, defined using [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md). This provides a granular approach to traffic management.

If you would like to apply more complex matching conditions and actions, see the [`traffic-label`](https://docs.api7.ai/hub/traffic-label.md) plugin.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrates how you can use the `workflow` plugin for different scenarios.

### Return Response HTTP Status Code Conditionally[â](#return-response-http-status-code-conditionally "Direct link to Return Response HTTP Status Code Conditionally")

The following example demonstrates a simple rule with one matching condition and one associated action to return HTTP status code conditionally.

Create a route with the `workflow` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "workflow-route",
    "uri": "/anything/*",
    "plugins": {
      "workflow":{
        "rules":[
          {
            "case":[
              ["uri", "==", "/anything/rejected"]
            ],
            "actions":[
              [
                "return",
                {"code": 403}
              ]
            ]
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

â¶ Trigger the action only when the request's URI path is `/anything/rejected`.

â· Return HTTP status code 403 when the rule is matched.

Send a request that matches none of the rules:

```
curl -i "http://127.0.0.1:9080/anything/anything"
```

You should receive an `HTTP/1.1 200 OK` response.

Send a request that matches the configured rule:

```
curl -i "http://127.0.0.1:9080/anything/rejected"
```

You should receive an `HTTP/1.1 403 Forbidden` response of following:

```
{"error_msg":"rejected by workflow"}
```

### Apply Rate Limiting Conditionally by URI and Query Parameter[â](#apply-rate-limiting-conditionally-by-uri-and-query-parameter "Direct link to Apply Rate Limiting Conditionally by URI and Query Parameter")

The following example demonstrates a rule with two matching conditions and one associated action to rate limit requests conditionally.

Create a route with the `workflow` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "workflow-route",
    "uri": "/anything/*",
    "plugins":{
      "workflow":{
        "rules":[
          {
            "case":[
              ["uri", "==", "/anything/rate-limit"],
              ["arg_env", "==", "v1"]
            ],
            "actions":[
              [
                "limit-count",
                {
                  "count":1,
                  "time_window":60,
                  "rejected_code":429
                }
              ]
            ]
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

â¶ Match URI path `/anything/rate-limit`.

â· Match query parameter `env` whose value being `v1`. See [built-in variables](https://docs.api7.ai/hub/apisix/reference/built-in-variables) for more variables to help construct conditions.

â¸ Apply rate limiting when both of the conditions are matched.

Generate two consecutive requests that matches the second rule:

```
curl -i "http://127.0.0.1:9080/anything/rate-limit?env=v1"
```

You should receive an `HTTP/1.1 200 OK` response and an `HTTP 429 Too Many Requests` response.

Generate requests that do not match the condition:

```
curl -i "http://127.0.0.1:9080/anything/anything?env=v1"
```

You should receive `HTTP/1.1 200 OK` responses for all requests, as they are not rate limited.

### Apply Rate Limiting Conditionally by Consumers[â](#apply-rate-limiting-conditionally-by-consumers "Direct link to Apply Rate Limiting Conditionally by Consumers")

The following example demonstrates how to configure the plugin to perform rate limiting based on the following specifications:

* consumer `john` should have a quota of 5 requests within a 30-second window
* consumer `jane` should have a quota of 3 requests within a 30-second window
* all other consumers should have a quota of 2 requests within a 30-second window

While this example will be using [`key-auth`](https://docs.api7.ai/hub/key-auth.md), you can easily replace it with other authentication plugins.

Create a consumer `john`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "john"
  }'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/john/credentials" -X PUT \
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

Create a second consumer `jane`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "jane"
  }'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/jane/credentials" -X PUT \
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

Create a third consumer `jimmy`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "username": "jimmy"
  }'
```

Create `key-auth` credential for the consumer:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/jimmy/credentials" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "cred-jimmy-key-auth",
    "plugins": {
      "key-auth": {
        "key": "jimmy-key"
      }
    }
  }'
```

Create a route with the `workflow` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "workflow-route",
    "uri": "/anything",
    "plugins":{
      "key-auth": {},
      "workflow":{
        "rules":[
          {
            "actions": [
              [
                "limit-count",
                {
                  "count": 5,
                  "key": "consumer_john",
                  "key_type": "constant",
                  "rejected_code": 429,
                  "time_window": 30,
                  "policy": "local"
                }
              ]
            ],
            "case": [
              [
                "consumer_name",
                "==",
                "john"
              ]
            ]
          },
          {
            "actions": [
              [
                "limit-count",
                {
                  "count": 3,
                  "key": "consumer_jane",
                  "key_type": "constant",
                  "rejected_code": 429,
                  "time_window": 30,
                  "policy": "local"
                }
              ]
            ],
            "case": [
              [
                "consumer_name",
                "==",
                "jane"
              ]
            ]
          },
          {
            "actions": [
              [
                "limit-count",
                {
                  "count": 2,
                  "key": "$consumer_name",
                  "key_type": "var",
                  "rejected_code": 429,
                  "time_window": 30,
                  "policy": "local"
                }
              ]
            ]
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

â¶ Enable `key-auth` on the route.

â· Match consumer `john` and apply a rate limiting quota of 5 requests within a 30-second window.

â¸ Match consumer `jane` and apply a rate limiting quota of 3 requests within a 30-second window.

â¹ Match all other consumers and apply a rate limiting quota of 2 requests within a 30-second window, per consumer.

To verify, send 6 consecutive requests with `john`'s key:

```
resp=$(seq 6 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H 'apikey: john-key' -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 6 requests, 5 requests were successful (status code 200) while the others were rejected (status code 429).

```
200:    5, 429:    1
```

Send 6 consecutive requests with `jane`'s key:

```
resp=$(seq 6 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H 'apikey: jane-key' -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 6 requests, 3 requests were successful (status code 200) while the others were rejected (status code 429).

```
200:    3, 429:    3
```

Send 3 consecutive requests with `jimmy`'s key:

```
resp=$(seq 3 | xargs -I{} curl "http://127.0.0.1:9080/anything" -H 'apikey: jimmy-key' -o /dev/null -s -w "%{http_code}\n") && \
  count_200=$(echo "$resp" | grep "200" | wc -l) && \
  count_429=$(echo "$resp" | grep "429" | wc -l) && \
  echo "200": $count_200, "429": $count_429
```

You should see the following response, showing that out of the 3 requests, 2 requests were successful (status code 200) while the others were rejected (status code 429).

```
200:    2, 429:    1
```

### Apply Advanced Rate Limiting with Sliding Window[â](#apply-advanced-rate-limiting-with-sliding-window "Direct link to Apply Advanced Rate Limiting with Sliding Window")

The following example demonstrates how to configure `workflow` with the Enterprise `limit-count-advanced` plugin to perform rate limiting conditionally, using the sliding window algorithm.

Create a route with the `workflow` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "workflow-route",
    "uri": "/anything/*",
    "plugins":{
      "workflow":{
        "rules":[
          {
            "case": [
              ["uri", "==", "/anything/rate-limit-advanced"]
            ],
            "actions": [
              [
                "limit-count-advanced",
                {
                  "count": 5,
                  "time_window": 10,
                  "rejected_code": 429,
                  "policy": "local",
                  "key_type": "var",
                  "key": "remote_addr",
                  "window_type": "sliding"
                }
              ]
            ]
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

â¶ Match URI path `/anything/rate-limit-advanced`.

â· Apply rate limiting when the condition is matched.

â¸ Set the rate limiting algorithm to sliding window.

Generate 7 requests to the route that matches the condition every other second:

```
for i in $(seq 7); do
  (curl -I "http://127.0.0.1:9080/anything/rate-limit-advanced" &)
  sleep 1
done
```

You should receive `HTTP/1.1 200 OK` responses for most requests, with the remainder being `HTTP 429 Too Many Requests responses`.

If you send requests to the route with other paths, such as:

```
curl -i "http://127.0.0.1:9080/anything/else"
```

You should not observe any rate limiting in effect as the condition is not matched.
