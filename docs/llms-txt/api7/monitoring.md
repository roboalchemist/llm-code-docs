# Source: https://docs.api7.ai/enterprise/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.7.x/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.6.x/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.5.x/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.4.x/api-observability/monitoring.md

# Source: https://docs.api7.ai/enterprise/3.3.x/api-observability/monitoring.md

# Monitor API Metrics

API7 Gateway supports exposing a comprehensive set of metrics to the monitoring system with minimal delay, facilitating ongoing monitoring and diagnostics.

API7 Gateway's monitoring and alerting framework is built on Prometheus, a widely used system monitoring and alerting toolkit. Prometheus gathers and stores multidimensional time series data, including metrics annotated with key-value labels.

This guide explains how to enable the Prometheus plugin to integrate with the monitoring system, allowing you to collect and visualize HTTP metrics.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a running API on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).

## Monitor All Services[â](#monitor-all-services "Direct link to Monitor All Services")

It is recommended to enable the `prometheus` plugin as a global rule. This ensures that all services and routes are consistently monitored and tracked.

* Dashboard
* ADC
* Ingress Controller

1. Select **Plugin Settings** of your gateway group from the side navigation bar.
2. Select the **Plugin Global Rules** tab, then click **Enable Plugin**.
3. Search for the `prometheus` plugin, then click **Enable**.
4. In the dialog box that appeared, click **Enable**, no extra configuration needed.
5. Make some API calls to test the monitoring.
6. Select **Monitoring** from the side navigation bar to view the metrics.

To use ADC to enable monitoring, create the following configuration:

adc.yaml

```
global_rules:
  prometheus:
    _meta:
      disable: false
```

Synchronize the configuration to API7 Gateway:

```
adc sync -f adc.yaml
```

note

ADC uses the configuration files as the single source of truth. Make sure to pass all configuration files to the `adc sync` command using the `-f` flag.

In the API7 Enterprise Dashboard, select **Monitoring** from the side navigation bar to view the metrics.

Create a manifest file to enable the Prometheus plugin globally for all routes:

global-observability.yaml

```
apiVersion: apisix.apache.org/v2
kind: ApisixGlobalRule
metadata:
  name: global-observability
  # namespace: api7    # replace with your namespace
spec:
  monitoring:
    prometheus:
      enable: true
```

Apply the configuration to your cluster:

```
kubectl apply -f global-observability.yaml
```

In the API7 Enterprise Dashboard, select **Monitoring** from the side navigation bar to view the metrics.
