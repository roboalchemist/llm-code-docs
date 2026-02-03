# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/redshift_cluster_without_vpc.md

---
title: Redshift cluster without VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redshift cluster without VPC
---

# Redshift cluster without VPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `0a494a6a-ebe2-48a0-9d77-cf9d5125e1b3`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/redshift_cluster#vpc_security_group_ids)

### Description{% #description %}

Amazon Redshift clusters should be deployed within an Amazon VPC to ensure network isolation and control over access to the cluster. If the `vpc_security_group_ids` and `cluster_subnet_group_name` attributes are not specified, the cluster is created outside a VPC and could be exposed to the public internet, increasing the risk of unauthorized access and data breaches. A secure configuration includes the following attributes:

```
resource "aws_redshift_cluster" "secure_example" {
  // other attributes
  vpc_security_group_ids     = [aws_security_group.redshift.id]
  cluster_subnet_group_name  = aws_redshift_subnet_group.redshift_subnet_group.id
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_redshift_cluster" "negative1" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = "mydb"
  master_username    = "foo"
  master_password    = "Mustbe8characters"
  node_type          = "dc1.large"
  cluster_type       = "single-node"
  logging {
      enable = true
      bucket_name = "nameOfAnExistingS3Bucket"
  }
  vpc_security_group_ids = [
    aws_security_group.redshift.id
  ]
  cluster_subnet_group_name = aws_redshift_subnet_group.redshift_subnet_group.id
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_redshift_cluster" "positive1" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = "mydb"
  master_username    = "foo"
  master_password    = "Mustbe8characters"
  node_type          = "dc1.large"
  cluster_type       = "single-node"
  logging {
      enable = true
      bucket_name = "nameOfAnExistingS3Bucket"
  }
}
```
