# Source: https://docs.api7.ai/enterprise/best-practices/gateway-error-log-kubernetes-splunk.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/gateway-error-log-kubernetes-splunk.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/gateway-error-log-kubernetes-splunk.md

# Forward Error Logs from Kubernetes to Splunk

In a production environment, timely collection and analysis of error logs are essential for maintaining system stability and facilitating troubleshooting.

This guide explains how to collect error logs from multiple API7 Gateway instances running in a Kubernetes environment and send them to Splunk for centralized log management. To achieve this, you will use Splunk OpenTelemetry Collector for Kubernetes, a dedicated solution for collecting logs from Kubernetes pods.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. Deploy API7 Gateways in Kubernetes cluster.
2. Install [Splunk](https://www.splunk.com).

## Deploy Splunk[â](#deploy-splunk "Direct link to Deploy Splunk")

You can choose to use Splunk's cloud service or deploy Splunk locally. If you have already deployed Splunk, you can skip to the next step to [Create Splunk HEC Token](#create-splunk-hec-token).

Create a docker-compose file for Splunk:

docker-compose.yaml

```
services:
  splunk:
    image: splunk/splunk:8.2.3
    container_name: splunk
    hostname: splunk
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_PASSWORD=yourpassword123
      - SPLUNK_HEC_TOKEN=your-hec-token
    ports:
      - "8000:8000"
      - "8088:8088"
      - "8089:8089"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
```

Start Splunk:

```
docker compose up -d
```

## Create Splunk HEC Token[â](#create-splunk-hec-token "Direct link to Create Splunk HEC Token")

Go to **Settings > Data inputs**:

![go to settings and data input in splunk](https://static.api7.ai/uploads/2025/04/11/JXaUsQ2U_1280X1280.PNG)

Select **HTTP Event Collector**:

![select HTTP event collector](https://static.api7.ai/uploads/2025/04/11/bDQw0RJe_1280X1280-2.PNG)

Create a new token:

![create a new token](https://static.api7.ai/uploads/2025/04/11/RcreFm1h_1280X1280-3.PNG)

## Create Splunk Index[â](#create-splunk-index "Direct link to Create Splunk Index")

To create an index in Splunk to collect error logs, go to **Indexes**:

![Go to indexes](https://static.api7.ai/uploads/2025/04/11/bPypUEUw_Screenshot%20at%20Apr%2011%2015-37-47.png)

For example, you can create an index named `gateway_error_logs`:

![Create a new index](https://static.api7.ai/uploads/2025/04/11/EtQz4LdH_output.png)

## Deploy Splunk OpenTelemetry Collector for Kubernetes[â](#deploy-splunk-opentelemetry-collector-for-kubernetes "Direct link to Deploy Splunk OpenTelemetry Collector for Kubernetes")

Create a values file for the Helm chart:

values.yaml

```
clusterName: "my-cluster"

splunkPlatform:
  endpoint: "https://{Your_Splunk_Host}:8088/services/collector/event"
  token: "your-hec-token"
  index: "gateway_error_logs"
  insecureSkipVerify: true

  logsEnabled: true
  metricsEnabled: false
  tracesEnabled: false

logsEngine: "otel"
logsCollection:
  containers:
    enabled: true
    excludeAgentLogs: true
    extraOperators:
    # https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/pkg/stanza/docs/operators/README.md
      - type: "filter"
        expr: 'not (body matches "(?i)(error|exception|fail|fatal)")'

agent:
  resources:
    limits:
      cpu: 1
      memory: 512Mi
    requests:
      cpu: 200m
      memory: 256Mi
```

To learn more about advanced Splunk OpenTelemetry Collector for Kubernetes configurations, refer to the [official Helm chart configuration file](https://github.com/signalfx/splunk-otel-collector-chart/blob/main/helm-charts/splunk-otel-collector/values.yaml).

Install Splunk OpenTelemetry Collector for Kubernetes:

```
helm repo add splunk-otel-collector https://signalfx.github.io/splunk-otel-collector-chart
helm repo update
helm upgrade --install my-splunk-otel-collector -n logging --create-namespace -f values.yaml splunk-otel-collector-chart/splunk-otel-collector
```

## Verify Log Collection[â](#verify-log-collection "Direct link to Verify Log Collection")

Generate any error log in the API7 Gateway. In the Splunk management console, search for `index="gateway_error_logs" "[error]"` to view the corresponding error logs:

![error log in splunk](https://static.api7.ai/uploads/2025/04/14/PfmCJu9Q_output-3.png)
