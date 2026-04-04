# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/autoscale_badly_setup.md

---
title: Beta - Databricks autoscale configuration incomplete
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Databricks autoscale configuration
  incomplete
---

# Beta - Databricks autoscale configuration incomplete

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `953c0cc6-5f30-44cb-a803-bf4ef2571be8`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Medium

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/cluster)

### Description{% #description %}

Databricks clusters must define both `autoscale.min_workers` and `autoscale.max_workers`. This rule flags `databricks_cluster` resources where either attribute is missing or unset. Defining both ensures predictable autoscaling and prevents resource overuse or unexpected costs.

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
  aws_attributes {
    availability           = "SPOT_WITH_FALLBACK"
    zone_id                = "auto"
    first_on_demand        = 1
    spot_bid_price_percent = 100
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_cluster" "positive2" {
  cluster_name            = "Shared Autoscaling"
  spark_version           = data.databricks_spark_version.latest.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    max_workers = 50
  }
  aws_attributes {
    availability           = "SPOT"
    zone_id                = "us-east-1"
    first_on_demand        = 1
    spot_bid_price_percent = 100
  }
}
```

```terraform
resource "databricks_cluster" "positive1" {
  cluster_name            = "Shared Autoscaling"
  spark_version           = data.databricks_spark_version.latest.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
  }
  aws_attributes {
    availability           = "SPOT"
    zone_id                = "us-east-1"
    first_on_demand        = 1
    spot_bid_price_percent = 100
  }
}
```
