# Source: https://docs.datadoghq.com/dashboards/widgets/retention.md

# Source: https://docs.datadoghq.com/cloudprem/configure/retention.md

---
title: Retention Policy
description: Learn how to configure data retention for CloudPrem
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > Retention Policy
---

# Retention Policy

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

The retention policy specifies how long data is stored before being deleted. By default, the retention period is set to 30 days. Data is automatically removed daily by the janitor, which deletes splits (index files) older than the defined retention threshold.

To change the retention period, update the `cloudprem.index.retention` parameter in the Helm chart values file, then upgrade the Helm release and optionally restart the janitor pod to apply the changes immediately:

1. Update the retention period in the Helm chart values file with a human-readable string (for example, `15 days`, `6 months`, or `3 years`):

In the `datadog-values.yaml` file:

   ```yaml
   cloudprem:
     index:
       retention: 6 months
```



1. Upgrade the Helm chart release:

   ```shell
   helm upgrade <RELEASE_NAME> datadog/cloudprem \
     -n <NAMESPACE_NAME> \
     -f datadog-values.yaml
   ```

1. Restart the janitor pod (optional but recommended for immediate effect):

   ```shell
   kubectl delete pod -l app.kubernetes.io/component=janitor -n <NAMESPACE_NAME>
   ```
