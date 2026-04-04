# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-upstream-https.md

# Configure Upstream HTTPS

*TLS (Transport Layer Security)* is a cryptographic protocol designed to secure communication between two parties, such as a web browser and a web server. Services often require TLS if traffic between the API gateway and upstream services is not considered secure or private.

This guide will show you how to configure TLS between APISIX and an upstream service.

<br />

![TLS between APISIX and Upstream](https://static.api7.ai/uploads/2023/05/10/YEowzK2g_tls-apisix-upstream.jpg)

<br />

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Install and run APISIX, or follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Create a Route With TLS Enabled[â](#create-a-route-with-tls-enabled "Direct link to Create a Route With TLS Enabled")

Create a route to an example upstream [httpbin.org](https://httpbin.org) on its default HTTPS port `443`:

* Admin API
* ADC

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "quickstart-tls-upstream",
  "uri": "/ip",
  "upstream": {
    "scheme": "https",
    "nodes": {
      "httpbin.org:443":1
    },
    "type": "roundrobin"
  }
}'
```

â¶ Configure scheme as `https`

â· Configure port as `443`

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /ip
        name: quickstart-tls-upstream
    upstream:
      type: roundrobin
      scheme: https
      nodes:
        - host: httpbin.org
          port: 443
          weight: 1
```

â¶ Configure scheme as `https`

â· Configure port as `443`

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Test TLS between APISIX and Upstream[â](#test-tls-between-apisix-and-upstream "Direct link to Test TLS between APISIX and Upstream")

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/ip"
```

An `HTTP/1.1 200 OK` response verifies that APISIX has successfully established a connection and communicated with the upstream service over HTTPS.

## Next Steps[â](#next-steps "Direct link to Next Steps")

APISIX also supports TLS connection between clients and APISIX. See [configure HTTPS between Client and APISIX](https://docs.api7.ai/apisix/how-to-guide/traffic-management/tls-and-mtls/configure-https-between-client-and-apisix.md).
