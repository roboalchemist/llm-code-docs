# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/use_lts_spark_version.md

---
title: Beta - Databricks cluster uses non-LTS Spark version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Databricks cluster uses non-LTS Spark
  version
---

# Beta - Databricks cluster uses non-LTS Spark version

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5a627dfa-a4dd-4020-a4c6-5f3caf4abcd6`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/spark_version)

### Description{% #description %}

Flags use of non-LTS Spark versions. This rule applies to:

- `databricks_spark_version` resources not marked as `long_term_support`
- `databricks_cluster` resources with a `spark_version` that is not an approved LTS version
- Clusters whose `spark_version` does not reference a `data.databricks_spark_version` resource

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
data "databricks_node_type" "negative2_with_gpu" {
  local_disk  = true
  min_cores   = 16
  gb_per_core = 1
  min_gpus    = 1
}

resource "databricks_cluster" "negative2_research" {
  cluster_name            = "Research Cluster"
  spark_version           = "3.2.1"
  node_type_id            = data.databricks_node_type.negative2_with_gpu.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
}
```

```terraform
data "databricks_node_type" "negative1_with_gpu" {
  local_disk  = true
  min_cores   = 16
  gb_per_core = 1
  min_gpus    = 1
}

data "databricks_spark_version" "negative1_gpu_ml" {
  gpu = true
  ml  = true
  long_term_support = true
}

resource "databricks_cluster" "negative1_research" {
  cluster_name            = "Research Cluster"
  spark_version           = data.databricks_spark_version.negative1_gpu_ml.id
  node_type_id            = data.databricks_node_type.negative1_with_gpu.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
data "databricks_node_type" "positive2_with_gpu" {
  local_disk  = true
  min_cores   = 16
  gb_per_core = 1
  min_gpus    = 1
}

data "databricks_spark_version" "positive2_gpu_ml" {
  gpu = true
  ml  = true
  long_term_support = false
}

resource "databricks_cluster" "positive2_research" {
  cluster_name            = "Research Cluster"
  spark_version           = data.databricks_spark_version.positive2_gpu_ml.id
  node_type_id            = data.databricks_node_type.positive2_with_gpu.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
}
```

```terraform
data "databricks_node_type" "positive3_with_gpu" {
  local_disk  = true
  min_cores   = 16
  gb_per_core = 1
  min_gpus    = 1
}

resource "databricks_cluster" "positive3_research" {
  cluster_name            = "Research Cluster"
  spark_version           = "3.3.1"
  node_type_id            = data.databricks_node_type.positive2_with_gpu.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
}
```

```terraform
data "databricks_node_type" "postive1_with_gpu" {
  local_disk  = true
  min_cores   = 16
  gb_per_core = 1
  min_gpus    = 1
}

data "databricks_spark_version" "postive1_gpu_ml" {
  gpu = true
  ml  = true
}

resource "databricks_cluster" "positive1_research" {
  cluster_name            = "Research Cluster"
  spark_version           = data.databricks_spark_version.postive1_gpu_ml.id
  node_type_id            = data.databricks_node_type.postive1_with_gpu.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
}
```
