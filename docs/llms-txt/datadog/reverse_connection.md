# Source: https://docs.datadoghq.com/cloudprem/configure/reverse_connection.md

---
title: Reverse Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Reverse Connection
source_url: https://docs.datadoghq.com/configure/reverse_connection/index.html
---

# Reverse Connection

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

Reverse connection lets your CloudPrem cluster initiate a WebSocket connection with Datadog using your API key, without requiring adding a DNS record and configuring a public ingress. This setup is useful for environments with strict network policies which do not allow inbound requests.

## Helm chart configuration{% #helm-chart-configuration %}

1. Create a Kubernetes secret with your API key:

   ```
   kubectl create secret generic datadog-secret -n <NAMESPACE_NAME> --from-literal api-key=<DD_API_KEY>
   ```

Replace `<DD_API_KEY>` with your Datadog API key.

1. Configure the `datadog` section of your Helm chart values:

   ```yaml
   datadog:
     site: datadoghq.com
     apiKeyExistingSecret: datadog-secret
   ```

**Note**: Make sure to set `site` to the Datadog site you are using (for instance, `datadoghq.eu`).

## Proxies{% #proxies %}

To configure CloudPrem to use a forward proxy such as Squid, set the environment variable `HTTPS_PROXY`:

```yaml
environment:
  HTTPS_PROXY: <your HTTP proxy>
```

## Further reading{% #further-reading %}

- [CloudPrem Installation Prerequisites](https://docs.datadoghq.com/cloudprem/install/)
