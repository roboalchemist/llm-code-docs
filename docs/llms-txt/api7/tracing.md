# Source: https://docs.api7.ai/enterprise/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-observability/tracing.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-observability/tracing.md

# Trace API Traffic

Traces are one of the three pillars of observability, along with metrics and logs. A trace tracks the journey of a request as it traverses through various parts of a system. It is an effective mechanism that helps developers and administrators monitor system performance, identify bottlenecks, and improve user experience.

This tutorial guides you through creating tracing using the [`opentelemetry`](https://docs.api7.ai/hub/opentelemetry.md) plugin, which instruments the Gateway and sends traces to the OpenTelemetry collector based on the OpenTelemetry specification, in binary-encoded OTLP over HTTP. Below is an interactive demo providing a hands-on introduction to the following use cases.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Have a running API on the gateway group and create a route](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Install OpenTelemetry[â](#install-opentelemetry "Direct link to Install OpenTelemetry")

While the steps in this section use specific OpenTelemetry collectors, you may use other distributions of collectors, such as [SigNoz OpenTelemetry Collector](https://github.com/SigNoz/signoz-otel-collector), which all handle telemetry data but vary in focus, features, and flexibility for integration.

* Docker
* Kubernetes

Start an OpenTelemetry collector instance:

```
docker run -d --name otel-collector -p 4318:4318 otel/opentelemetry-collector-contrib
```

Install `cert-manager` as a dependency:

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.1/cert-manager.yaml
```

Install OpenTelemetry operator:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/latest/download/opentelemetry-operator.yaml
```

Install an OpenTelemetry instance:

```
kubectl apply -f - <<EOF
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: simplest
spec:
  config: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
    processors:

    exporters:
      debug:

    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: []
          exporters: [debug]
EOF
```

## Configure OpenTelemetry Metadata[â](#configure-opentelemetry-metadata "Direct link to Configure OpenTelemetry Metadata")

In this section, you will be configuring the metadata for `opentelemetry` plugin, which specifies the connection interface and other parameters.

* Dashboard
* ADC
* Ingress Controller

1. Select **Plugin Settings** of your gateway group from the side navigation bar.

2. Select the **Plugin Metadata** tab, then click **Add Plugin Metadata**.

3. Search for the `opentelemetry` plugin, then click **Add Metadata**.

4. In the dialog box that appeared, add the following configuration to the **JSON Editor** and replace the collector address with your IP:

   ```
   {
     "trace_id_source": "x-request-id",
     "resource": {
       "service.name": "API7"
     },
     "collector": {
       "address": "192.168.2.106:4318",
       "request_timeout": 3,
       "request_headers": {
         "Authorization": "token"
       }
     },
     "batch_span_processor": {
       "drop_on_queue_full": false,
       "max_queue_size": 1024,
       "batch_timeout": 2,
       "inactive_timeout": 1,
       "max_export_batch_size": 16
     },
     "set_ngx_var": true
   }
   ```

5. Click **Save**.

To use ADC to update plugin metadata, create the following configuration:

otel-metadata.yaml

```
plugin_metadata:
  opentelemetry:
    batch_span_processor:
      batch_timeout: 2
      drop_on_queue_full: false
      inactive_timeout: 1
      max_export_batch_size: 16
      max_queue_size: 1024
    collector:
      address: 192.168.2.106:4318
      request_headers:
        Authorization: token
      request_timeout: 3
    resource:
      service.name: API7
    set_ngx_var: true
    trace_id_source: x-request-id
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f otel-metadata.yaml
```

Create a ConfigMap:

otel-cm.yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel
data:
  config.yaml: |
    - cluster: default
      plugins:
      - name: opentelemetry
        metadata:
          trace_id_source: x-request-id
          resource:
            service.name: API7
          collector:
            address: simplest-collector:4318
            request_timeout: 3
            request_headers:
              Authorization: token
          batch_span_processor:
            drop_on_queue_full: false
            max_queue_size: 1024
            batch_timeout: 2
            inactive_timeout: 1
            max_export_batch_size: 16
          set_ngx_var: true
```

â¶ Configure the name of the ConfigMap.

â· Configure the address for the OpenTelemetry collector, where `simplest-collector` is the service name. Adjust accordingly for your applications.

â¸ Export OpenTelemetry variables to built-in variables, which can be used in access logging.

Apply the ConfigMap to your cluster:

```
kubectl apply -f otel-cm.yaml
```

To apply the ConfigMap to your ingress controller, go to Dashboard and navigate to your ingress controller gateway group. Click the **Actions** dropdown at the upper-right corner and **Regenerate Deploy Script**. Copy the script, manually add `config.pluginMetadataCM=otel` to the flag and run the command to upgrade the chart. Your command should look similar to the following:

```
helm repo add api7 https://charts.api7.ai
helm repo update
helm upgrade --install api7-ingress api7/api7-ingress-controller \
  --set "config.dashboard.adminKey=a7adm-12I3k81Axxdmfx2b487POib6l461Q4X33RBES1Ej3I822vU591-35a2ef9fbfb04740ab72452789f527ae" \
  --set "config.dashboard.baseURL=https://192.168.2.103:7443"
  --set "config.pluginMetadataCM=otel"
```

Go to the dashboard and under **Plugin Settings > Plugin Metadata**, you should see the plugin metadata updated with the `opentelemetry` plugin and its metadata.

## Configure OpenTelemetry as a Global Plugin[â](#configure-opentelemetry-as-a-global-plugin "Direct link to Configure OpenTelemetry as a Global Plugin")

In this example, you will be configuring `opentelemetry` as a global plugin that traces all requests.

* Dashboard
* ADC
* Ingress Controller

1. Select **Plugin Settings** of your gateway group from the side navigation bar.
2. Select the **Plugin Global Rules** tab, then click **Enable Plugin**.
3. Search for the `opentelemetry` plugin, then click **Enable**.
4. In the dialog box that appeared, add the following configuration to the **JSON Editor**:

```
  {
    "opentelemetry": {
      "sampler": {
        "name": "always_on"
      }
    }
  }
```

5. Click **Enable**.

To use ADC to update a plugin globally, create the following configuration:

otel-global-plugin.yaml

```
global_rules:
  opentelemetry:
    _meta:
      disable: false
    opentelemetry:
      sampler:
        name: always_on
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f otel-global-plugin otel-metadata.yaml
```

Create a Kubernetes manifest file to configure `opentelemetry` plugin using the ApisixGlobalRule custom resource:

global-rule-otel.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixGlobalRule
metadata:
  # namespace: api7   # replace with your namespace
  name: global-obs-otel
spec:
  plugins:
  - name: opentelemetry
    enable: true
    config:
      sampler:
        name: always_on
```

Apply the configuration to your cluster:

```
kubectl apply -f global-rule-otel.yaml
```

Once applied, you should see the `opentelemetry` plugin appear under the **Plugin Settings** on the dashboard.

Suppose you have completed steps in [launch your first API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md) to create a sample route, and an upstream httpbin if you are using Kubernetes.

Send a few requests to the route:

```
curl "http://127.0.0.1:9080/ip"
```

In the OpenTelemetry collector's log, you should see traces collected from the gateway traffic:

```
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
```

## Configure OpenTelemetry on a Route[â](#configure-opentelemetry-on-a-route "Direct link to Configure OpenTelemetry on a Route")

In this example, you will be configuring `opentelemetry` plugin on a single route, which only traces requests visiting this route.

* Dashboard
* ADC
* Ingress Controller

1. Click into your service to create a new route or update the existing `/ip` route.
2. click **Enable Plugin**.
3. Search for the `opentelemetry` plugin, then click **Enable**.
4. In the dialog box that appeared, add the following configuration to the **JSON Editor**:

```
  {
    "opentelemetry": {
      "sampler": {
        "name": "always_on"
      }
    }
  }
```

5. Click **Enable**.

To use ADC to update a plugin globally, create the following configuration:

otel-route.yaml

```
services:
  - name: httpbin
    upstream:
      name: httpbin
      scheme: http
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 100
    routes:
      - uris:
          - /ip
        name: get-ip
        methods:
          - GET
        plugins:
          opentelemetry:
            _meta:
              disable: false
            opentelemetry:
              sampler:
                name: always_on
```

Synchronize the configuration to API7 Enterprise:

```
adc sync -f otel-route.yaml otel-metadata.yaml
```

Create a Kubernetes manifest file to configure `opentelemetry` plugin on a route using the ApisixRoute custom resource:

route-otel.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: route-otel
  # namespace: api7   # replace with your namespace
spec:
  http:
    - name: get-ip
      match:
        paths:
          - /ip
      backends:
        - serviceName: httpbin
          servicePort: 80
      plugins:
      - name: opentelemetry
        enable: true 
        config:
          sampler:
            name: always_on
```

Apply the configuration to your cluster:

```
kubectl apply -f route-otel.yaml
```

Once applied, you should see the `opentelemetry` plugin appear under the corresponding **Routes**.

Send a few requests to the route:

```
curl "http://127.0.0.1:9080/ip"
```

In the OpenTelemetry collector's log, you should see traces collected from the gateway traffic:

```
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
{"kind": "exporter", "data_type": "traces", "name": "debug", "resource spans": 1, "spans": 1}
```

## Use Trace Variables in Gateway Access Logging[â](#use-trace-variables-in-gateway-access-logging "Direct link to Use Trace Variables in Gateway Access Logging")

In this example, you will be updating the Gateway's configuration to configure the access log to show OpenTelemetry tracing information. Make sure the `set_ngx_var` has been set to `true` in the [plugin metadata](#configure-opentelemetry-metadata).

* Docker
* Kubernetes

Update the logging format configurations in the gateway's configuration file:

```
docker exec <api7-ee-gateway-container-name> /bin/sh -c "echo '
nginx_config:
  http:
    enable_access_log: true
    access_log_format: \"{\\\"time\\\": \\\"\$time_iso8601\\\",\\\"opentelemetry_context_traceparent\\\": \\\"\$opentelemetry_context_traceparent\\\",\\\"opentelemetry_trace_id\\\": \\\"\$opentelemetry_trace_id\\\",\\\"opentelemetry_span_id\\\": \\\"\$opentelemetry_span_id\\\",\\\"remote_addr\\\": \\\"\$remote_addr\\\"}\"
    access_log_format_escape: json
' > /usr/local/apisix/conf/config.yaml"
```

Reload the container for configuration changes to take effect:

```
docker exec <api7-ee-gateway-container-name> apisix reload
```

Update the logging format configurations in the gateway's ConfigMap:

```
kubectl edit cm api7-ee-3-gateway
```

The following parameters should already exist with different initial values. Update the corresponding fields to the following values:

```
nginx_config:
  http:
    enable_access_log: true
    access_log_format: '{"time": "$time_iso8601","opentelemetry_context_traceparent": "$opentelemetry_context_traceparent","opentelemetry_trace_id": "$opentelemetry_trace_id","opentelemetry_span_id": "$opentelemetry_span_id","remote_addr": "$remote_addr"}'
    access_log_format_escape: json
```

Save the ConfigMap and restart the resource:

```
kubectl rollout restart deployment api7-ee-3-gateway
```

Suppose you have completed steps in [launch your first API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md) to create a sample route, and an upstream httpbin if you are using Kubernetes.

Send a few requests to the route:

```
curl "http://127.0.0.1:9080/ip"
```

In the Gateway's log, you should see access logs similar to the following:

```
{"time": "2024-11-11T09:21:45+00:00","opentelemetry_context_traceparent": "00-3a142e5c18c01a5ff84f844f14ca8bd8-d3915c694505a6f3-01","opentelemetry_trace_id": "3a142e5c18c01a5ff84f844f14ca8bd8","opentelemetry_span_id": "d3915c694505a6f3","remote_addr": "127.0.0.1"}
{"time": "2024-11-11T09:21:46+00:00","opentelemetry_context_traceparent": "00-4766edec58af12c47eddefa775fe3cbb-fc6ca6cdd7f4d501-01","opentelemetry_trace_id": "4766edec58af12c47eddefa775fe3cbb","opentelemetry_span_id": "fc6ca6cdd7f4d501","remote_addr": "127.0.0.1"}
{"time": "2024-11-11T09:21:46+00:00","opentelemetry_context_traceparent": "00-dde5b4987a2ab2cce63559cb48945054-4def031b882e0ad2-01","opentelemetry_trace_id": "dde5b4987a2ab2cce63559cb48945054","opentelemetry_span_id": "4def031b882e0ad2","remote_addr": "127.0.0.1"}
```
