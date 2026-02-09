# Source: https://docs.datadoghq.com/cloudprem/ingest_logs/datadog_agent.md

---
title: Send logs to CloudPrem with the Datadog Agent
description: Configure the Datadog Agent to send logs to your CloudPrem deployment
breadcrumbs: >-
  Docs > CloudPrem > Set up Log Ingestion > Send logs to CloudPrem with the
  Datadog Agent
source_url: https://docs.datadoghq.com/ingest_logs/datadog_agent/index.html
---

# Send logs to CloudPrem with the Datadog Agent

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

This document provides configuration steps for using the Datadog Agent to send logs to a Datadog CloudPrem deployment. Unlike the Datadog SaaS platform, CloudPrem requires specific Agent configurations to ensure logs are enriched with necessary host-level tags and sent to the correct endpoint. This guide covers how to set these configurations for the most common deployment methods.

## Key requirements{% #key-requirements %}

To send logs with the Datadog Agent to CloudPrem, you must configure two environment variables:

{% dl %}

{% dt %}
`DD_LOGS_CONFIG_LOGS_DD_URL`
{% /dt %}

{% dd %}
Set this to your CloudPrem indexer endpoint, usually `http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280`. This tells the Agent where to send the logs
{% /dd %}

{% dt %}
`DD_LOGS_CONFIG_EXPECTED_TAGS_DURATION`
{% /dt %}

{% dd %}
(Optional) This is an optional but highly recommended variable. Set it to a large value, like "100000" (approximately 5 years). This ensures the Agent adds host-level tags to every log it sends. The Datadog SaaS platform automatically enriches logs with these tags after ingestion, but CloudPrem requires the Agent to add them upfront.
{% /dd %}

{% /dl %}

### Proxy{% #proxy %}

If you have configured the Datadog Agent to use a proxy and CloudPrem is hosted in your internal network, you need to configure the `no_proxy` setting so the Agent can send logs directly to CloudPrem without passing through the proxy.

```yaml
# In the no_proxy section, add the CloudPrem DNS
no_proxy:
 - http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280
```

Additionally, you need to set `DD_NO_PROXY_NONEXACT_MATCH` to true. For more details, see [Datadog Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy/#proxy-server-setup-examples).

## Send Kubernetes logs with the Datadog Operator{% #send-kubernetes-logs-with-the-datadog-operator %}

To deploy the Agent on Kubernetes using the Datadog Operator, follow the [Getting Started with Datadog Operator](https://docs.datadoghq.com/getting_started/containers/datadog_operator/#installation-and-deployment) guide. When you reach Step 3, use the following `datadog-agent.yaml` configuration instead of the example provided in the guide.

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  global:
    clusterName: <CLUSTER_NAME>
    site: datadoghq.com
    credentials:
      apiSecret:
        secretName: datadog-secret
        keyName: api-key
    env:
      - name: DD_LOGS_CONFIG_LOGS_DD_URL
        value: http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280
      - name: DD_LOGS_CONFIG_EXPECTED_TAGS_DURATION
        value: "100000"

  features:
    logCollection:
      enabled: true
      containerCollectAll: true

    otlp:
      receiver:
        protocols:
          grpc:
            enabled: true
            endpoint: 0.0.0.0:4417

    prometheusScrape:
      enabled: true
      enableServiceEndpoints: true
```

## Configuration options{% #configuration-options %}

### Endpoint configuration{% #endpoint-configuration %}

The Datadog Agent can be configured to send logs to CloudPrem using different endpoints:

{% collapsible-section %}
#### Internal cluster endpoint

Recommended for in-cluster agents:

```
DD_LOGS_CONFIG_LOGS_DD_URL=http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280
```

{% /collapsible-section %}

{% collapsible-section %}
#### Internal ingress endpoint

For Agents outside the cluster:

```
DD_LOGS_CONFIG_LOGS_DD_URL=https://cloudprem-internal.your-domain.com
```

{% /collapsible-section %}

### Additional Agent configuration{% #additional-agent-configuration %}

You can also configure additional features to send cluster metadata to Datadog:

{% collapsible-section %}
#### Prometheus metrics scraping

```yaml
features:
  prometheusScrape:
    enabled: true
    enableServiceEndpoints: true
```

{% /collapsible-section %}

{% collapsible-section %}
#### OTLP logs collection

To send Agent logs to Datadog:

```yaml
features:
  otlp:
    receiver:
      protocols:
        grpc:
          enabled: true
          endpoint: 0.0.0.0:4417
```

{% /collapsible-section %}

## Alternative deployment methods{% #alternative-deployment-methods %}

If you are not using the Datadog Operator, you can deploy the Agent using one of these common methods:

### Helm chart deployment{% #helm-chart-deployment %}

Run the following command to deploy the Agent using the Helm chart, setting the log-specific environment variables directly.

```shell
helm install datadog-agent datadog/datadog \
  --set datadog.apiKey=<YOUR_API_KEY> \
  --set datadog.logs.enabled=true \
  --set datadog.logs.containerCollectAll=true \
  --set datadog.logsConfigContainerCollectAll=true \
  --set agents.containers.agent.env[0].name=DD_LOGS_CONFIG_LOGS_DD_URL \
  --set agents.containers.agent.env[0].value=http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280
```

### DaemonSet deployment{% #daemonset-deployment %}

For custom deployments, set the environment variable in your DaemonSet:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: datadog-agent
spec:
  template:
    spec:
      containers:
      - name: agent
        image: gcr.io/datadoghq/agent:latest
        env:
        - name: DD_API_KEY
          value: <YOUR_API_KEY>
        - name: DD_LOGS_ENABLED
          value: "true"
        - name: DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL
          value: "true"
        - name: DD_LOGS_CONFIG_LOGS_DD_URL
          value: "http://<RELEASE_NAME>-indexer.<NAMESPACE_NAME>.svc.cluster.local:7280"
```

## Verification{% #verification %}

After the Agent is deployed, you can verify that logs are being sent and received correctly.

### Check Agent status{% #check-agent-status %}

Use `kubectl exec` to check the Agent's status and confirm it is configured to send logs.

```shell
# Check Agent status and logs configuration
kubectl exec -it <datadog-agent-pod> -- agent status | grep -A 10 "Logs Agent"

# Check Agent logs for CloudPrem connection
kubectl logs <datadog-agent-pod> | grep -i cloudprem
```

### Check logs are indexed in CloudPrem{% #check-logs-are-indexed-in-cloudprem %}

Run this command to query the CloudPrem searcher and verify that it's indexing the JSON logs.

```shell
kubectl exec -it <RELEASE_NAME>-searcher-0 -n <NAMESPACE_NAME> -- curl 'http://localhost:7280/api/v1/datadog/search?query='
```

## Troubleshooting{% #troubleshooting %}

**Agent not sending logs**:

- Verify the `DD_LOGS_CONFIG_LOGS_DD_URL` environment variable is set correctly
- Check Agent pod logs: `kubectl logs <datadog-agent-pod>`
- Ensure log collection is enabled: `DD_LOGS_ENABLED=true`

**CloudPrem not receiving logs**:

- Check CloudPrem indexer logs: `kubectl logs -n <NAMESPACE_NAME> -l app=<RELEASE_NAME>-indexer`
- Verify network connectivity between Agent and CloudPrem indexer
- Confirm CloudPrem service is running: `kubectl get pods -n <NAMESPACE_NAME>`

## Further reading{% #further-reading %}

- [Observability Pipelines Integration](https://docs.datadoghq.com/cloudprem/ingest_logs/observability_pipelines/)
- [REST API Integration](https://docs.datadoghq.com/cloudprem/ingest_logs/rest_api/)
- [Datadog Operator Guide](https://docs.datadoghq.com/getting_started/containers/datadog_operator/)
