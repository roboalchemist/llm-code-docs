# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/api-versioning.md

# Implement API Versioning

In the dynamic landscape of software development, maintaining a robust and flexible API is essential for building scalable and interoperable systems. As software evolves over time, it is inevitable that changes and updates will need to be made to APIs. API versioning provides a systematic approach to introduce breaking changes while preserving backward compatibility.

In this guide, you will understand a few different API versioning strategies and how to implement them in APISIX.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Path-Based Versioning[â](#path-based-versioning "Direct link to Path-Based Versioning")

Path-based versioning is one of the most popular approaches to API versioning that involves incorporating the version number directly into the URL path of the API endpoint, for example:

```
https://apis.yourdomain.com/v1/foo
https://apis.yourdomain.com/v2/foo
```

To implement this strategy in APISIX, create one route for each API version, such as the following:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v1",
  "uri": "/v1/*",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v2",
  "uri": "/v2/*",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

adc.yaml

```
services:
  - name: Version v1 Service
    routes:
      - uris:
          - /v1/*
        name: apis-v1
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
  - name: Version v2 Service
    routes:
      - uris:
          - /v2/*
        name: apis-v2
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Query-Based Versioning[â](#query-based-versioning "Direct link to Query-Based Versioning")

Query-based versioning is another API versioning approach, which involves incorporating the version number into the URL query parameters, for example:

```
https://apis.yourdomain.com/foo?version=1
https://apis.yourdomain.com/foo?version=2
```

To implement this strategy in APISIX, create one route for each API version and configure their matching criteria and priorities, such as the following:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v1",
  "uri": "/*",
  "vars": [[ "arg_version", "==", "1" ]],
  "priority": 2,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v2",
  "uri": "/*",
  "vars": [[ "arg_version", "==", "2" ]],
  "priority": 3,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

adc.yaml

```
services:
  - name: Version v1 Service
    routes:
      - uris:
          - /*
        name: apis-v1
        vars:
          - - arg_version
            - "=="
            - "1"
        priority: 2
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
  - name: Version v2 Service
    routes:
      - uris:
          - /*
        name: apis-v2
        vars:
          - - arg_version
            - "=="
            - "2"
        priority: 3
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

As both routes are configured to match the same URI, setting priorities would allow the route with higher priority to match requests first.

## Header-Based Versioning[â](#header-based-versioning "Direct link to Header-Based Versioning")

A third approach to API versioning is to version with the HTTP header. The version could be included in a custom header, for example:

```
GET /foo HTTP/1.1
...
Api-Version: 1
```

```
GET /foo HTTP/1.1
...
Api-Version: 2
```

To implement this strategy in APISIX, create one route for each API version and configure their matching criteria and priorities, such as the following:

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v1",
  "uri": "/*",
  "vars": [[ "http_api_version", "==", "1" ]],
  "priority": 2,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "apis-v2",
  "uri": "/*",
  "vars": [[ "http_api_version", "==", "2" ]],
  "priority": 3,
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "https://apis.yourdomain.com": 1
    },
    "pass_host": "node",
    "scheme": "https"
  }
}'
```

adc.yaml

```
services:
  - name: Version v1 Service
    routes:
      - uris:
          - /*
        name: apis-v1
        vars:
          - - http_api_version
            - "=="
            - "1"
        priority: 2
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
  - name: Version v2 Service
    routes:
      - uris:
          - /*
        name: apis-v2
        vars:
          - - http_api_version
            - "=="
            - "2"
        priority: 3
    upstream:
      type: roundrobin
      pass_host: node
      scheme: https
      nodes:
        - host: apis.yourdomain.com
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Adjust the header filtering criteria accordingly, such as when [content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#principles_of_content_negotiation) is used for versioning.

As both routes are configured to match the same URI, setting priorities would allow the route with higher priority to match requests first.

## Next Steps[â](#next-steps "Direct link to Next Steps")

When versioning APIs, oftentimes you would need to forward requests to different URI paths rather than the original request paths, or redirect requests from deprecated endpoints to the versioned endpoints. See the following plugins for more information:

* [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin
* `redirect` plugin (coming soon)
