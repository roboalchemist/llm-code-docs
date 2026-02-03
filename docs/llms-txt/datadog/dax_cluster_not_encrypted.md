# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/dax_cluster_not_encrypted.md

---
title: DAX cluster not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DAX cluster not encrypted
---

# DAX cluster not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f11aec39-858f-4b6f-b946-0a1bf46c0c87`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dax_cluster#enabled)

### Description{% #description %}

This check verifies that AWS DynamoDB Accelerator (DAX) clusters have server-side encryption enabled to protect data at rest. Without encryption, sensitive data stored in DAX clusters could be exposed if unauthorized access to the storage media occurs, potentially leading to data breaches and compliance violations.

To secure a DAX cluster, you must include a `server_side_encryption` block with `enabled = true`, as shown below:

```
resource "aws_dax_cluster" "secure_example" {
  cluster_name       = "cluster-example"
  // other configuration...
  
  server_side_encryption {
    enabled = true
  }
}
```

Insecure configurations either omit the `server_side_encryption` block entirely, include an empty block, or explicitly set `enabled = false`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_dax_cluster" "bar" {
  cluster_name       = "cluster-example"
  iam_role_arn       = data.aws_iam_role.example.arn
  node_type          = "dax.r4.large"
  replication_factor = 1

  server_side_encryption {
    enabled = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_dax_cluster" "bar_1" {
  cluster_name       = "cluster-example"
  iam_role_arn       = data.aws_iam_role.example.arn
  node_type          = "dax.r4.large"
  replication_factor = 1
}

resource "aws_dax_cluster" "bar_2" {
  cluster_name       = "cluster-example"
  iam_role_arn       = data.aws_iam_role.example.arn
  node_type          = "dax.r4.large"
  replication_factor = 1

  server_side_encryption {
  }
}

resource "aws_dax_cluster" "bar_3" {
  cluster_name       = "cluster-example"
  iam_role_arn       = data.aws_iam_role.example.arn
  node_type          = "dax.r4.large"
  replication_factor = 1

  server_side_encryption {
    enabled = false
  }
}
```
