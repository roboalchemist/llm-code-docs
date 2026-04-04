# Source: https://docs.api7.ai/apisix/how-to-guide/traffic-management/traffic-mirroring.md

# Implement Traffic Mirroring

Traffic mirroring is a mechanism that duplicates the traffic flowing through the API gateway and forwards the duplicated traffic to a designated upstream, without interrupting the regular services. The mechanism benefits a few use cases, including troubleshooting, security inspection, analytics, and more.

This guide will walk you through the process of implementing traffic mirroring in APISIX using the [`proxy-mirror`](https://docs.api7.ai/hub/proxy-mirror.md) plugin.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker).
* Install [cURL](https://curl.se/) to send requests to the services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker or on Kubernetes.

## Start Sample Service to Receive Mirrored Traffic[â](#start-sample-service-to-receive-mirrored-traffic "Direct link to Start Sample Service to Receive Mirrored Traffic")

Start a sample NGINX server for receiving mirrored traffic:

```
docker run -p 8081:80 --name nginx nginx
```

You should see NGINX access log and error log on the terminal session.

## Configure APISIX[â](#configure-apisix "Direct link to Configure APISIX")

Create a route with the `proxy-mirror` plugin and configure the address for mirrored traffic. Update the address accordingly.

* Admin API
* ADC

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "traffic-mirror-route",
  "uri": "/get",
  "plugins": {
    "proxy-mirror": {
      "host": "http://192.168.42.145:8081"
    }
  },
  "upstream": {
    "nodes": {
      "httpbin.org": 1
    },
    "type": "roundrobin"
  }
}'
```

adc.yaml

```
services:
  - name: httpbin Service
    routes:
      - uris:
          - /get
        name: traffic-mirror-route
        plugins:
          proxy-mirror:
            host: http://192.168.42.145:8081
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

## Verify Mirroring[â](#verify-mirroring "Direct link to Verify Mirroring")

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/get"
```

You should receive an `HTTP/1.1 200 OK` response.

To verify, return to the NGINX terminal session (if running in Docker) or check the NGINX pod logs (if running on Kubernetes); you should see the corresponding access log entry:

```
172.17.0.1 - - [29/Jan/2024:23:11:01 +0000] "GET /get HTTP/1.1" 404 153 "-" "curl/7.64.1" "-"
```

The HTTP response status is `404` and expected, since the sample NGINX server does not implement the route. This verifies that APISIX has mirrored the request to the NGINX server.

## Next Steps[â](#next-steps "Direct link to Next Steps")

You have now learned how to mirror all ingress traffic to a different upstream. The `proxy-mirror` plugin also supports mirroring partial traffic and customization of the mirroring timeout values. See [plugin doc](https://docs.api7.ai/hub/proxy-mirror.md) for more information.
