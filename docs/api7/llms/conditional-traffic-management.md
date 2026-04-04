# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/conditional-traffic-management.md

# Manage Traffic Conditionally

Conditional traffic management refers to the ability to execute specific actions based on certain characteristics of each request, such as request headers, URI parameters, or URI paths. This enables one to implement dynamic and flexible routing, rate limiting, or other actions, allowing for granular control and customization of the gateway's behavior based on the specific needs of the application or system.

This guide will show you how you can manage traffic conditionally in APISIX using the [`traffic-split`](https://docs.api7.ai/hub/traffic-split.md), [`traffic-label`](https://docs.api7.ai/hub/traffic-label.md), and [`workflow`](https://docs.api7.ai/hub/workflow.md) plugins.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Forward Traffic Conditionally and Proportionally[â](#forward-traffic-conditionally-and-proportionally "Direct link to Forward Traffic Conditionally and Proportionally")

In this section, you will learn how to forward traffic to different upstream services conditionally and by weights, using the `traffic-split` plugin.

Create a route as such:

* Admin API
* ADC

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

â¶ Execute the plugin to redirect traffic only when the request contains a URL parameter `name=jack`, a header `user-id` with its value greater than 23, and another header `apisix-key` with its value composed of lowercase English letters.

adc.yaml

```
services:
  - name: Mock Service
    routes:
      - uris:
          - /headers
        name: traffic-split-route
        plugins:
          traffic-split:
            rules:
              - match:
                  - vars:
                      - [arg_name, "==", "jack"]
                      - [http_user-id, ">", "23"]
                      - [http_apisix-key, "~~", "[a-z]+"]
                weighted_upstreams:
                  - upstream:
                      type: roundrobin
                      scheme: https
                      pass_host: node
                      nodes:
                        'httpbin.org:443': 1
                    weight: 3
                  - weight: 2
    upstream:
      type: roundrobin
      scheme: https
      pass_host: node
      nodes:
        - host: mock.api7.ai
          port: 443
          weight: 1
```

â¶ Execute the plugin to redirect traffic only when the request contains a URL parameter `name=jack`, a header `user-id` with its value greater than 23, and another header `apisix-key` with its value composed of lowercase English letters.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

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

A common use case of the `traffic-split` plugin is to implement release strategies, such as canary release and blue-green deployment. For more plugin usage, see the [plugin doc](https://docs.api7.ai/hub/traffic-split.md).

## Label Traffic by Headers Conditionally and Proportionally[â](#label-traffic-by-headers-conditionally-and-proportionally "Direct link to Label Traffic by Headers Conditionally and Proportionally")

In this section, you will learn how to add headers to requests conditionally and by weights, using the enterprise [`traffic-label`](https://docs.api7.ai/hub/traffic-label.md) plugin.

Create a route as such:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "traffic-label-route",
    "uri":"/headers",
    "plugins":{
      "traffic-label": {
        "rules": [
          {
            "match": [
              ["uri", "==", "/headers"]
            ],
            "actions": [
              {
                "set_headers": {
                  "X-Server-Id": 100
                },
                "weight": 3
              },
              {
                "set_headers": {
                  "X-API-Version": "v2"
                },
                "weight": 2
              },
              {
                "weight": 5
              }
            ]
          }
        ]
      }
    },
    "upstream":{
      "type":"roundrobin",
      "nodes":{
        "httpbin.org:80":1
      }
    }
  }'
```

â¶ 30% of the requests should have the `X-Server-Id: 100` request header.

â· 20% of the requests should have the `X-API-Version: v2` request header.

â¸ 50% of the requests should not have any action performed on them.

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /headers
        name: traffic-label-route
        plugins:
          traffic-label:
            rules:
              - match:
                  - [uri, "==", "/headers"]
                actions:
                  - set_headers:
                      X-Server-Id: 100
                    weight: 3
                  - set_headers:
                      X-API-Version: v2
                    weight: 2
                  - weight: 5
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ 30% of the requests should have the `X-Server-Id: 100` request header.

â· 20% of the requests should have the `X-API-Version: v2` request header.

â¸ 50% of the requests should not have any action performed on them.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

â¶ 30% of the requests should have the `X-Server-Id: 100` request header.

â· 20% of the requests should have the `X-API-Version: v2` request header.

â¸ 50% of the requests should not have any action performed on them.

Generate 50 consecutive requests to verify the weighted actions:

```
resp=$(seq 50 | xargs -I{} curl "http://127.0.0.1:9080/headers" -sL) && \
  count_w3=$(echo "$resp" | grep "X-Server-Id" | wc -l) && \
  count_w2=$(echo "$resp" | grep "X-API-Version" | wc -l) && \
  echo X-Server-Id: $count_w3, X-API-Version: $count_w2
```

The response shows that headers are added to requests in a weighted manner:

```
X-Server-Id: 15, X-API-Version: 10
```

For more plugin usage, see the [plugin doc](https://docs.api7.ai/hub/traffic-label.md).

## Rate Limit Traffic Conditionally[â](#rate-limit-traffic-conditionally "Direct link to Rate Limit Traffic Conditionally")

In this section, you will learn how to implement rate limiting by count conditionally, using the `workflow` plugin.

Create a route as such:

* Admin API
* ADC

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

â¶ Execute the plugin to rate limit only when the request's URI path is `/anything/rate-limit` and it contains a URL parameter `env=v1`.

â· Apply rate limiting when the rule is matched.

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /anything/*
        name: workflow-route
        plugins:
          workflow:
            rules:
              - case:
                  - [uri, "==", "/anything/rate-limit"]
                  - [arg_env, "==", "v1"]
                actions:
                  - - limit-count
                    - count: 1
                      time_window: 60
                      rejected_code: 429
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

â¶ Execute the plugin to rate limit only when the request's URI path is `/anything/rate-limit` and it contains a URL parameter `env=v1`.

â· Apply rate limiting when the rule is matched.

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Generate two consecutive requests that match the condition:

```
curl -i "http://127.0.0.1:9080/anything/rate-limit?env=v1"
```

You should receive an `HTTP/1.1 200 OK` response and an `HTTP 429 Too Many Requests` response.

Generate requests that do not match the condition:

```
curl -i "http://127.0.0.1:9080/anything/anything?env=v1"
```

You should receive `HTTP/1.1 200 OK` responses for all requests, as they are not rate limited.

For more plugin usage, see the [plugin doc](https://docs.api7.ai/hub/workflow.md).

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned the various ways APISIX supports conditional traffic management, using the [`traffic-split`](https://docs.api7.ai/hub/traffic-split.md), [`traffic-label`](https://docs.api7.ai/hub/traffic-label.md), and [`workflow`](https://docs.api7.ai/hub/workflow.md) plugins.

To meet more complex conditional traffic management requirements, see how you can [create a custom plugin](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md), or use [serverless function plugins](https://docs.api7.ai/hub/serverless-functions.md) to execute custom code at runtime.
