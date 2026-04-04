# Source: https://docs.api7.ai/hub/proxy-mirror.md

# proxy-mirror

The `proxy-mirror` plugin duplicates ingress traffic to APISIX and forwards them to a designated upstream, without interrupting the regular services. You can configure the plugin to mirror all traffic or only a portion. The mechanism benefits a few use cases, including troubleshooting, security inspection, analytics, and more.

Note that APISIX ignores any response from the upstream host receiving mirrored traffic.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how to configure `proxy-mirror` for different scenarios.

### Mirror Partial Traffic[â](#mirror-partial-traffic "Direct link to Mirror Partial Traffic")

The following example demonstrates how you can configure `proxy-mirror` to mirror 50% of the traffic to a route and forward them to another upstream service.

Start a sample NGINX server for receiving mirrored traffic:

* Docker
* Kubernetes

```
docker run -p 8081:80 --name nginx nginx
```

You should see NGINX access log and error log on the terminal session.

Create a Kubernetes manifest file for the NGINX deployment:

nginx-deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: aic
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: nginx
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

Apply the manifest to your cluster:

```
kubectl apply -f nginx-deployment.yaml
```

Open a new terminal session and create a route with `proxy-mirror`:

* Admin API
* ADC
* Ingress Controller

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -d '{
    "id": "traffic-mirror-route",
    "uri": "/get",
    "plugins": {
      "proxy-mirror": {
        "host": "http://127.0.0.1:8081",
        "sample_ratio": 0.5
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
  - name: proxy-mirror-service
    routes:
      - name: traffic-mirror-route
        uris:
          - /get
        plugins:
          proxy-mirror:
            host: "http://127.0.0.1:8081"
            sample_ratio: 0.5
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to the gateway:

```
adc sync -f adc.yaml
```

* Gateway API
* APISIX CRD

proxy-mirror-ic.yaml

```
apiVersion: v1
kind: Service
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  type: ExternalName
  externalName: httpbin.org
---
apiVersion: apisix.apache.org/v1alpha1
kind: PluginConfig
metadata:
  namespace: aic
  name: proxy-mirror-plugin-config
spec:
  plugins:
    - name: proxy-mirror
      config:
        host: "http://nginx.aic.svc"
        sample_ratio: 0.5
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  namespace: aic
  name: traffic-mirror-route
spec:
  parentRefs:
    - name: apisix
  rules:
    - matches:
        - path:
            type: Exact
            value: /get
      filters:
        - type: ExtensionRef
          extensionRef:
            group: apisix.apache.org
            kind: PluginConfig
            name: proxy-mirror-plugin-config
      backendRefs:
        - name: httpbin-external-domain
          port: 80
```

proxy-mirror-ic.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixUpstream
metadata:
  namespace: aic
  name: httpbin-external-domain
spec:
  ingressClassName: apisix
  externalNodes:
  - type: Domain
    name: httpbin.org
---
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  namespace: aic
  name: traffic-mirror-route
spec:
  ingressClassName: apisix
  http:
    - name: traffic-mirror-route
      match:
        paths:
          - /get
      upstreams:
      - name: httpbin-external-domain
      plugins:
      - name: proxy-mirror
        enable: true
        config:
          host: "http://nginx.aic.svc"
          sample_ratio: 0.5
```

Apply the configuration to your cluster:

```
kubectl apply -f proxy-mirror-ic.yaml
```

â¶ `host`: configure the scheme and host address to forward the mirrored traffic to.

â· `sample_ratio`: configure the sampling ratio to 0.5 to mirror 50% of the traffic.

Send a few requests to the route:

```
curl -i "http://127.0.0.1:9080/get"
```

You should receive `HTTP/1.1 200 OK` responses for all requests.

Navigating back to the NGINX terminal session, you should see a number of access log entries, roughly half the number of requests generated:

```
172.17.0.1 - - [29/Jan/2024:23:11:01 +0000] "GET /get HTTP/1.1" 404 153 "-" "curl/7.64.1" "-"
```

This suggests APISIX has mirrored the request to the NGINX server. Here, the HTTP response status is `404` since the sample NGINX server does not implement the route.

### Configure Mirroring Timeouts[â](#configure-mirroring-timeouts "Direct link to Configure Mirroring Timeouts")

The following example demonstrates how you can update the default connect, read, and send timeouts for the plugin. This could be useful when mirroring traffic to a very slow backend service.

As the request mirroring was implemented as sub-requests, excessive delays in the sub-requests could lead to the blocking of the original requests. By default, the connect, read, and send timeouts are set to 60 seconds. To update these values, you can configure them in the `plugin_attr` section of the [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md#configyaml-and-configyamlexample) as such:

conf/config.yaml

```
plugin_attr:
  proxy-mirror:
    timeout:
      connect: 2000ms
      read: 2000ms
      send: 2000ms
```

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.
