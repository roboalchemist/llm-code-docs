# Source: https://docs.datadoghq.com/agent/configuration/dual-shipping.md

---
title: Dual Shipping
description: >-
  Configure the Datadog Agent to send metrics, logs, and traces to multiple
  Datadog organizations simultaneously.
breadcrumbs: Docs > Agent > Agent Configuration > Dual Shipping
---

# Dual Shipping

{% alert level="warning" %}
Dual shipping can impact billing if you are sending data to multiple Datadog organizations. For more information about the impact of this configuration, contact [Datadog Support](https://docs.datadoghq.com/help/).
{% /alert %}

## Overview{% #overview %}

This document provides examples of Agent configurations for dual shipping different types of data (for example, APM, logs, Cluster Agent metrics, and so on) to multiple Datadog organizations.

**Note**: Use [Observability Pipelines](https://docs.datadoghq.com/observability_pipelines/) if you want to dual ship logs or split log traffic across different logging vendors, cloud storages, or SIEM providers.

For a full list of network traffic destinations, see [Network Traffic](https://docs.datadoghq.com/agent/configuration/network/).

## Metrics and service checks{% #metrics-and-service-checks %}

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

### YAML configuration{% #yaml-configuration %}

Requires Agent version >= 6.17 or 7.17.

In `datadog.yaml`:

```yaml
additional_endpoints:
  "https://app.datadoghq.com":
  - apikey2
  - apikey3
  "https://app.datadoghq.eu":
  - apikey4
```

### Environment variable configuration{% #environment-variable-configuration %}

Requires Agent version >= 6.18 or 7.18.

```bash
DD_ADDITIONAL_ENDPOINTS='{\"https://app.datadoghq.com\": [\"apikey2\", \"apikey3\"], \"https://app.datadoghq.eu\": [\"apikey4\"]}'
```

## APM{% #apm %}

### YAML configuration{% #yaml-configuration-1 %}

Requires Agent version >= 6.7.0.

In `datadog.yaml`:

```yaml
apm_config:
  [...]
  additional_endpoints:
    "https://trace.agent.datadoghq.com":
    - apikey2
    - apikey3
    "https://trace.agent.datadoghq.eu":
    - apikey4
```

### Environment variable configuration{% #environment-variable-configuration-1 %}

Requires Agent version >= 6.19 or 7.19.

```bash
DD_APM_ADDITIONAL_ENDPOINTS='{\"https://trace.agent.datadoghq.com\": [\"apikey2\", \"apikey3\"], \"https://trace.agent.datadoghq.eu\": [\"apikey4\"]}'
```

## Continuous Profiler{% #continuous-profiler %}

### YAML configuration{% #yaml-configuration-2 %}

Requires Agent version >= 6.7.0.

In `datadog.yaml`:

```yaml
apm_config:
  [...]
  profiling_additional_endpoints:
    "https://intake.profile.datadoghq.com/api/v2/profile":
    - apikey2
    - apikey3
    "https://intake.profile.datadoghq.eu/api/v2/profile":
    - apikey4
```

### Environment variable configuration{% #environment-variable-configuration-2 %}

Requires Agent version >= 6.19 or 7.19.

```bash
DD_APM_PROFILING_ADDITIONAL_ENDPOINTS='{\"https://intake.profile.datadoghq.com/api/v2/profile\": [\"apikey2\", \"apikey3\"], \"https://intake.profile.datadoghq.eu/api/v2/profile\": [\"apikey4\"]}'
```

**Note:** Uploads to additional endpoints for the Continuous Profiler product are done through best-effort delivery.

- The main endpoint has the highest priority. Uploads to additional endpoints are only handled after uploads to the main endpoint have completed successfully.
- Responses from additional endpoints are not forwarded back to the profiler. Any errors during delivery to additional endpoints are logged in the Agent error logs.

## Live Processes{% #live-processes %}

### YAML configuration{% #yaml-configuration-3 %}

Requires Agent version >= 6.4.0.

In `datadog.yaml`:

```yaml
process_config:
  [...]
  additional_endpoints:
    "https://process.datadoghq.com":
    - apikey2
    - apikey3
    "https://process.datadoghq.eu":
    - apikey4
```

### Environment variable configuration{% #environment-variable-configuration-3 %}

Requires Agent version >= 6.20 or 7.20.

```bash
DD_PROCESS_ADDITIONAL_ENDPOINTS='{\"https://process.datadoghq.com\": [\"apikey2\", \"apikey3\"], \"https://process.datadoghq.eu\": [\"apikey4\"]}'
```

## Cluster Agent metrics{% #cluster-agent-metrics %}

Configure the Agent to send Cluster Agent metrics, such as Kubernetes State Metrics Core, to additional endpoints.

### HELM configuration{% #helm-configuration %}

In Datadog `values.yaml`:

```yaml
clusterAgent:
  env:
    - name: DD_ADDITIONAL_ENDPOINTS
      value: '{"https://app.datadoghq.com": ["apikey2"]}'
```

### Cluster Agent metrics provider{% #cluster-agent-metrics-provider %}

To ensure autoscaling is resilient to failure, configure the Cluster Agent to run your metric queries for the HPA against your multiple Datadog regions with dual-shipped data. Configure the Datadog Cluster Agent manifest with several endpoints:

In the `cluster-agent-deployment.yaml` file:

```yaml
external_metrics_provider:
  endpoints:
  - api_key: <DATADOG_API_KEY>
    app_key: <DATADOG_APP_KEY>
    url: https://app.datadoghq.eu
  - api_key: <DATADOG_API_KEY>
    app_key: <DATADOG_APP_KEY>
    url: https://app.datadoghq.com
```

## Orchestrator{% #orchestrator %}

### HELM configuration{% #helm-configuration-1 %}

In Datadog `values.yaml`:

```yaml
agents:
  customAgentConfig:
    process_config:
      additional_endpoints:
        "https://process.datadoghq.com":
        - apikey2
    orchestrator_explorer:
      orchestrator_additional_endpoints:
        "https://orchestrator.datadoghq.com":
        - apikey2

clusterAgent:
...
  datadog_cluster_yaml:
    orchestrator_explorer:
      orchestrator_additional_endpoints:
        "https://orchestrator.ddog-gov.com":
        - apikey2
```

### Environment variable configuration{% #environment-variable-configuration-4 %}

```bash
DD_ORCHESTRATOR_EXPLORER_ORCHESTRATOR_ADDITIONAL_ENDPOINTS='{\"https://orchestrator.datadoghq.com\": [\"apikey2\", \"apikey3\"], \"https://orchestrator.datadoghq.eu\": [\"apikey4\"]}'
```

## CI Visibility{% #ci-visibility %}

### YAML configuration{% #yaml-configuration-4 %}

Requires Agent >= 6.38 or 7.38.

In `datadog.yaml`:

```yaml
evp_proxy_config:
  [...]
  additional_endpoints:
    "https://<VERSION>-app.agent.datadoghq.com":
    - apikey2
    - apikey3
    "https://<VERSION>-app.agent.datadoghq.eu":
    - apikey4
```

### Environment variable configuration{% #environment-variable-configuration-5 %}

```bash
DD_EVP_PROXY_CONFIG_ADDITIONAL_ENDPOINTS='{\"https://<VERSION>-app.agent.datadoghq.com\": [\"apikey2\", \"apikey3\"], \"https://<VERSION>-app.agent.datadoghq.eu\": [\"apikey4\"]}'
```

## Logs{% #logs %}

Use the Agent if you want to dual ship logs to multiple Datadog organizations. Use [Observability Pipelines](https://docs.datadoghq.com/agent/configuration/network/) if you want to send logs to Datadog and external destinations.

TCP requires Agent version >= 6.6.HTTPS requires Agent version >= 6.13.

### YAML configuration{% #yaml-configuration-5 %}

In `datadog.yaml`:

```yaml
logs_config:
  force_use_http: true
  additional_endpoints:
  - api_key: "apiKey2"
    Host: "agent-http-intake.logs.datadoghq.com"
    Port: 443
    is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-6 %}

Requires Agent >= 6.18 or 7.18.

```bash
DD_LOGS_CONFIG_FORCE_USE_HTTP=true
DD_LOGS_CONFIG_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"agent-http-intake.logs.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Database Monitoring{% #database-monitoring %}

### YAML configuration{% #yaml-configuration-6 %}

Requires Agent >= 6.29 or 7.29.

In `datadog.yaml`:

```yaml
database_monitoring:
  samples:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "dbm-metrics-intake.datadoghq.com"
      Port: 443
      is_reliable: true
  activity:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "dbquery-intake.datadoghq.com"
      Port: 443
      is_reliable: true
  metrics:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "dbm-metrics-intake.datadoghq.com"
      Port: 443
      is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-7 %}

```bash
DD_DATABASE_MONITORING_SAMPLES_USE_HTTP=true
DD_DATABASE_MONITORING_SAMPLES_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"dbm-metrics-intake.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
DD_DATABASE_MONITORING_ACTIVITY_USE_HTTP=true
DD_DATABASE_MONITORING_ACTIVITY_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"dbquery-intake.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
DD_DATABASE_MONITORING_METRICS_USE_HTTP=true
DD_DATABASE_MONITORING_METRICS_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"dbm-metrics-intake.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Network Devices{% #network-devices %}

### YAML configuration{% #yaml-configuration-7 %}

Requires Agent >= 6.29 or 7.29.

In `datadog.yaml`:

```yaml
network_devices:
  metadata:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "ndm-intake.datadoghq.com"
      Port: 443
      is_reliable: true
  snmp_traps:
    forwarder:
      force_use_http: true
      additional_endpoints:
      - api_key: "apiKey2"
        Host: "ndm-intake.datadoghq.com"
        Port: 443
        is_reliable: true
  netflow:
    forwarder:
      force_use_http: true
      additional_endpoints:
      - api_key: "apiKey2"
        Host: "ndm-intake.datadoghq.com"
        Port: 443
        is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-8 %}

```bash
DD_NETWORK_DEVICES_METADATA_USE_HTTP=true
DD_NETWORK_DEVICES_METADATA_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"ndm-intake.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Network Path{% #network-path %}

### YAML configuration{% #yaml-configuration-8 %}

Requires Agent >= 6.55 or 7.55.

In `datadog.yaml`:

```yaml
network_path:
  forwarder:
    use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "netpath-intake.datadoghq.com"
      Port: 443
      is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-9 %}

```bash
DD_NETWORK_PATH_FORWARDER_USE_HTTP=true
DD_NETWORK_PATH_FORWARDER_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"netpath-intake.datadoghq.com\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Cloud Security Misconfigurations{% #cloud-security-misconfigurations %}

### YAML configuration{% #yaml-configuration-9 %}

In `datadog.yaml`:

```yaml
compliance_config:
  endpoints:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "https://<VERSION>-app.agent.datadoghq.eu"
      Port: 443
      is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-10 %}

```bash
DD_COMPLIANCE_CONFIG_ENDPOINTS_USE_HTTP=true
DD_COMPLIANCE_CONFIG_ENDPOINTS_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"https://<VERSION>-app.agent.datadoghq.eu\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Workload Protection{% #workload-protection %}

### YAML configuration{% #yaml-configuration-10 %}

In `datadog.yaml`:

```yaml
runtime_security_config:
  endpoints:
    force_use_http: true
    additional_endpoints:
    - api_key: "apiKey2"
      Host: "https://<VERSION>-app.agent.datadoghq.eu"
      Port: 443
      is_reliable: true
```

### Environment variable configuration{% #environment-variable-configuration-11 %}

```bash
DD_RUNTIME_SECURITY_CONFIG_ENDPOINTS_USE_HTTP=true
DD_RUNTIME_SECURITY_CONFIG_ENDPOINTS_ADDITIONAL_ENDPOINTS="[{\"api_key\": \"apiKey2\", \"Host\": \"https://<VERSION>-app.agent.datadoghq.eu\", \"Port\": 443, \"is_reliable\": true}]"
```

When setting up additional endpoints, you must explicitly set `use_http` to tell the Agent which transport to use. The same transport configuration is shared among all additional endpoints.

The `is_reliable` setting (First available in Agent `7.34.0`) tells the Agent to treat this endpoint with the same priority as the primary endpoint. The primary endpoint is always reliable. This ensures that data is not missed if a destination becomes unavailable.

For example, if you're sending data to the main endpoint and an additional endpoint with `is_reliable: true`, and one endpoint becomes unavailable, data continues to flow to the other endpoint. If both endpoints become unavailable, the Agent stops reading and sending data until at least one endpoint recovers. This ensures all data makes it to at least one reliable endpoint.

The `is_reliable` setting defaults to `true` in Agent `7.37.0+`. Unreliable endpoints only send data if at least one reliable endpoint is available. You may define multiple additional endpoints with a mixed usage of `is_reliable` values. Datadog recommends that you use the default `is_reliable` setting.

You can add the YAML configuration to your `datadog.yaml` or launch the Agent with the appropriate environment variables.

## Dual shipping in Kubernetes{% #dual-shipping-in-kubernetes %}

{% tab title="Helm" %}
If you're using the [Datadog Agent Helm chart](https://github.com/DataDog/helm-charts), you can configure these settings with a configmap. In the `values.yaml`, set `useConfigMap: true` and add the relevant settings to `customAgentConfig`.

```yaml
# agents.useConfigMap -- Configures a configmap to provide the agent configuration. Use this in combination with the `agents.customAgentConfig` parameter.
  useConfigMap:  true

  # agents.customAgentConfig -- Specify custom contents for the datadog agent config (datadog.yaml)
  ## ref: https://docs.datadoghq.com/agent/configuration/agent-configuration-files/?tab=agentv6
  ## ref: https://github.com/DataDog/datadog-agent/blob/main/pkg/config/config_template.yaml
  ## Note the `agents.useConfigMap` needs to be set to `true` for this parameter to be taken into account.
  customAgentConfig:
    additional_endpoints:
      "https://app.datadoghq.com":
      - apikey2
      - apikey3
      "https://app.datadoghq.eu":
      - apikey4

    logs_config:
      force_use_http: true
      additional_endpoints:
      - api_key: "apiKey2"
        Host: "agent-http-intake.logs.datadoghq.com"
        Port: 443
        is_reliable: true
```

To avoid exposing your API key(s) in clear text inside the `ConfigMap`, you can also use the environment variable configuration and reference a Kubernetes secret. Here is an example to send metrics to an additional region:

1. Create a Kubernetes secret with your environment variable configuration value from this guide:
   ```bash
   kubectl create -n <DATADOG AGENT NAMESPACE> secret generic dual-shipping --from-literal metrics='{"https://app.datadoghq.eu": ["apikey4"]}'
   ```
1. Use the [Helm chart parameters](https://github.com/DataDog/helm-charts/blob/e1ec85127de74c8b876eef6a81bb1579d17b49bf/charts/datadog/values.yaml#L563-L578) `datadog.env` or `datadog.envFrom` to reference this secret in your configuration:
   ```yaml
   datadog:
     [...]
     env:
     - name: DD_ADDITIONAL_ENDPOINTS
       valueFrom:
         secretKeyRef:
           name: dual-shipping
           key: metrics
   ```

{% /tab %}

{% tab title="Datadog Operator" %}
If you're using the [Datadog Agent operator](https://github.com/DataDog/datadog-operator), you can set the `[key].customConfigurations.[key].configData` [override](https://github.com/DataDog/datadog-operator/blob/main/docs/configuration.v2alpha1.md) key to set these settings. The example below replaces the `datadog.yaml` configuration file of the node Agent to send metrics and logs to additional regions.

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  override:
    nodeAgent:
      customConfigurations:
        datadog.yaml:
          configData: |-
            additional_endpoints:
              "https://app.datadoghq.com":
              - apikey2
              - apikey3
              "https://app.datadoghq.eu":
              - apikey4
            logs_config:
              force_use_http: true
              additional_endpoints:
              - api_key: "apiKey2"
                Host: "agent-http-intake.logs.datadoghq.com"
                Port: 443
                is_reliable: true
```

To avoid exposing your API key(s) in clear text inside the `ConfigMap`, you can also use the environment variable configuration and reference a Kubernetes secret. Here is an example to send metrics to an additional region:

1. Create a Kubernetes secret with your environment variable configuration value from this guide:
   ```bash
   kubectl create -n <DATADOG AGENT NAMESPACE> secret generic dual-shipping --from-literal metrics='{"https://app.datadoghq.eu": ["apikey4"]}'
   ```
1. Use the `[key].env` parameter to reference this secret in your configuration:
   ```yaml
   apiVersion: datadoghq.com/v2alpha1
   kind: DatadogAgent
   metadata:
     name: datadog
   spec:
     override:
       nodeAgent:
         env:
         - name: DD_ADDITIONAL_ENDPOINTS
           valueFrom:
             secretKeyRef:
               name: dual-shipping
               key: metrics
   ```

{% /tab %}

## Further reading{% #further-reading %}

- [Centralize and govern your OpenTelemetry pipeline with the DDOT gateway](https://www.datadoghq.com/blog/ddot-gateway)
- [Network Traffic](https://docs.datadoghq.com/agent/configuration/network/)
- [Send logs to external destinations with Observability Pipelines](https://docs.datadoghq.com/observability_pipelines/)
