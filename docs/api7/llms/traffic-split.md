# Source: https://docs.api7.ai/hub/traffic-split.md

# traffic-split

The `traffic-split` plugin directs traffic to various upstream services based on conditions and/or weights. It provides a dynamic and flexible approach to implement release strategies and manage traffic.

## Examples[â](#examples "Direct link to Examples")

The examples below shows different use cases for using the `traffic-split` plugin.

### Implement Canary Release[â](#implement-canary-release "Direct link to Implement Canary Release")

The following example demonstrates how to implement canary release with this plugin.

Canary release is a gradual deployment in which an increasing percentage of traffic is directed to a new release, allowing for a controlled and monitored rollout. This method ensures that any potential issues or bugs in the new release can be identified and addressed early on, before fully redirecting all traffic.

Create a route and configure `traffic-split` plugin with the following rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/headers",
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                },
                "weight": 3
              },
              {
                "weight": 2
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "mock.api7.ai:443":1
      }
    }
  }'
```

The proportion of traffic to each upstream is determined by the weight of the upstream relative to the total weight of all upstreams. Here, the total weight is calculated as: 3 + 2 = 5.

Therefore:

â¶ 60% of the traffic are expected to be forwarded to `httpbin.org`.

â· 40% of the traffic are expected to be forwarded to `mock.api7.ai`.

Send 10 consecutive requests to the route to verify:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/headers" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a response similar to the following:

```
httpbin.org: 6, mock.api7.ai: 4
```

Adjust the upstream weights accordingly to complete the canary release.

### Implement Blue-Green Deployment[â](#implement-blue-green-deployment "Direct link to Implement Blue-Green Deployment")

The following example demonstrates how to implement blue-green deployment with this plugin.

Blue-green deployment is a deployment strategy that involves maintaining two identical environments: the *blue* and the *green*. The blue environment refers to the current production deployment and the green environment refers to the new deployment. Once the green environment is tested to be ready for production, traffic will be routed to the green environment, making it the new production deployment.

Create a route and configure `traffic-split` plugin with the following rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/headers",
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "match": [
              {
                "vars": [
                  ["http_release","==","new_release"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                }
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "mock.api7.ai:443":1
      }
    }
  }'
```

â¶ Execute the plugin to redirect traffic only when the request contains a header `release: new_release`.

Send a request to the route with the `release` header:

```
curl "http://127.0.0.1:9080/headers" -H 'release: new_release'
```

You should see a response similar to the following:

```
{
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    ...
  }
}
```

Send a request to the route without any additional header:

```
curl "http://127.0.0.1:9080/headers"
```

You should see a response similar to the following:

```
{
  "headers": {
    "accept": "*/*",
    "host": "mock.api7.ai",
    ...
  }
}
```

### Define Matching Condition for POST Request With APISIX Expressions[â](#define-matching-condition-for-post-request-with-apisix-expressions "Direct link to Define Matching Condition for POST Request With APISIX Expressions")

The following example demonstrates how to use [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md) in rules to conditionally execute the plugin when certain condition of a POST request is satisfied.

Create a route and configure `traffic-split` plugin with the following rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/post",
    "methods": ["POST"],
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "match": [
              {
                "vars": [
                  ["post_arg_id", "==", "1"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                }
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "mock.api7.ai:443":1
      }
    }
  }'
```

Send a POST request with body `id=1`:

```
curl "http://127.0.0.1:9080/post" -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'id=1'
```

â¶ You can specify charset in the `Content-Type` as well, such as `Content-Type: application/x-www-form-urlencoded;charset=UTF-8`.

You should see a response similar to the following:

```
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "id": "1"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "4", 
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org", 
    ...
  }, 
  ...
}
```

Send a POST request without `id=1` in the body:

```
curl "http://127.0.0.1:9080/post" -X POST \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'random=string'
```

You should see that the request was forwarded to `mock.api7.ai`.

### Define AND Matching Conditions With APISIX Expressions[â](#define-and-matching-conditions-with-apisix-expressions "Direct link to Define AND Matching Conditions With APISIX Expressions")

The following example demonstrates how to use [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md) in rules to conditionally execute the plugin when multiple conditions are satisfied.

Create a route and configure `traffic-split` plugin with the following matching rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/headers",
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "match": [
              {
                "vars": [
                  ["arg_name","==","jack"],
                  ["http_user-id",">","23"],
                  ["http_apisix-key","~~","[a-z]+"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                },
                "weight": 3
              },
              {
                "weight": 2
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "mock.api7.ai:443":1
      }
    }
  }'
```

â¶ Execute the plugin to redirect traffic only when all three conditions are satisfied.

If conditions are satisfied, 60% of the traffic should be directed to `httpbin.org` and the other 40% should be directed to `mock.api7.ai`. If conditions are not satisfied, all traffic should be directed to `mock.api7.ai`.

Send 10 consecutive requests that satisfy all conditions to verify:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/headers?name=jack" -H 'user-id: 30' -H 'apisix-key: helloapisix' -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a response similar to the following:

```
httpbin.org: 6, mock.api7.ai: 4
```

Send 10 consecutive requests that do not satisfy the conditions to verify:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/headers?name=random" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a response similar to the following:

```
httpbin.org: 0, mock.api7.ai: 10
```

### Define OR Matching Conditions With APISIX Expressions[â](#define-or-matching-conditions-with-apisix-expressions "Direct link to Define OR Matching Conditions With APISIX Expressions")

The following example demonstrates how to use [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md) in rules to conditionally execute the plugin when either set of the condition is satisfied.

Create a route and configure `traffic-split` plugin with the following matching rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/headers",
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "match": [
              {
                "vars": [
                  ["arg_name","==","jack"],
                  ["http_user-id",">","23"],
                  ["http_apisix-key","~~","[a-z]+"]
                ]
              },
              {
                "vars": [
                  ["arg_name2","==","rose"],
                  ["http_user-id2","!",">","33"],
                  ["http_apisix-key2","~~","[a-z]+"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                },
                "weight": 3
              },
              {
                "weight": 2
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "scheme": "https",
      "pass_host": "node",
      "nodes": {
        "mock.api7.ai:443":1
      }
    }
  }'
```

â¶ and â·: Execute the plugin to redirect traffic when either set of the conditions are satisfied.

Alternatively, you can also use the OR operator in the [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md#logical-operators) for these conditions.

If conditions are satisfied, 60% of the traffic should be directed to `httpbin.org` and the other 40% should be directed to `mock.api7.ai`. If conditions are not satisfied, all traffic should be directed to `mock.api7.ai`.

Send 10 consecutive requests that satisfy the second set of conditions to verify:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/headers?name2=rose" -H 'user-id:30' -H 'apisix-key2: helloapisix' -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a response similar to the following:

```
httpbin.org: 6, mock.api7.ai: 4
```

Send 10 consecutive requests that do not satisfy any set of conditions to verify:

```
resp=$(seq 10 | xargs -I{} curl "http://127.0.0.1:9080/headers?name=random" -sL) && \
  count_httpbin=$(echo "$resp" | grep "httpbin.org" | wc -l) && \
  count_mockapi7=$(echo "$resp" | grep "mock.api7.ai" | wc -l) && \
  echo httpbin.org: $count_httpbin, mock.api7.ai: $count_mockapi7
```

You should see a response similar to the following:

```
httpbin.org: 0, mock.api7.ai: 10
```

### Configure Different Rules for Different Upstreams[â](#configure-different-rules-for-different-upstreams "Direct link to Configure Different Rules for Different Upstreams")

The following example demonstrates how to set one-to-one mapping between rule sets and upstreams.

Create a route and configure `traffic-split` plugin with the following matching rules:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "uri": "/headers",
    "id": "traffic-split-route",
    "plugins": {
      "traffic-split": {
        "rules": [
          {
            "match": [
              {
                "vars": [
                  ["http_x-api-id","==","1"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "httpbin.org:443":1
                  }
                },
                "weight": 1
              }
            ]
          },
          {
            "match": [
              {
                "vars": [
                  ["http_x-api-id","==","2"]
                ]
              }
            ],
            "weighted_upstreams": [
              {
                "upstream": {
                  "type": "roundrobin",
                  "scheme": "https",
                  "pass_host": "node",
                  "nodes": {
                    "mock.api7.ai:443":1
                  }
                },
                "weight": 1
              }
            ]
          }
        ]
      }
    },
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "postman-echo.com:443": 1
      },
      "scheme": "https",
      "pass_host": "node"
    }
  }'
```

â¶ Execute the plugin to redirect traffic only when the request contains a header `x-api-id: 1`.

â· Execute the plugin to redirect traffic only when the request contains a header `x-api-id: 2`.

Send a request with header `x-api-id: 1`:

```
curl "http://127.0.0.1:9080/headers" -H 'x-api-id: 1'
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    ...
  }
}
```

Send a request with header `x-api-id: 2`:

```
curl "http://127.0.0.1:9080/headers" -H 'x-api-id: 2'
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  "headers": {
    "accept": "*/*",
    "host": "mock.api7.ai",
    ...
  }
}
```

Send a request without any additional header:

```
curl "http://127.0.0.1:9080/headers"
```

You should see a response similar to the following:

```
{
  "headers": {
    "accept": "*/*",
    "host": "postman-echo.com",
    ...
  }
}
```
