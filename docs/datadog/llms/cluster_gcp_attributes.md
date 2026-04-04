# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/cluster_gcp_attributes.md

---
title: Beta - check Databricks cluster GCP attribute best practices
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - check Databricks cluster GCP attribute
  best practices
---

# Beta - check Databricks cluster GCP attribute best practices

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `539e4557-d2b5-4d57-a001-cb01140a4e2d`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.databricks.com/clusters/cluster-config-best-practices.html)

### Description{% #description %}

The rule flags `databricks_cluster` resources where `gcp_attributes.availability` is set to `PREEMPTIBLE_GCP`, which violates best practices. Clusters should use a non-preemptible availability setting.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "databricks_cluster" "negative" {
  cluster_name            = "Shared Autoscaling"
  spark_version           = data.databricks_spark_version.latest.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
  gcp_attributes {
    availability           = "PREEMPTIBLE_WITH_FALLBACK_GCP"
    zone_id                = "auto"
    first_on_demand        = 1
    spot_bid_price_percent = 100
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_cluster" "positive" {
  cluster_name            = "data"
  spark_version           = data.databricks_spark_version.latest.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
  gcp_attributes {
    availability           = "PREEMPTIBLE_GCP"
    zone_id                = "AUTO"
  }
}
```
