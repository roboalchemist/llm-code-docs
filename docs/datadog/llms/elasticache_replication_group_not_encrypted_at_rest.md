# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticache_replication_group_not_encrypted_at_rest.md

---
title: ElastiCache replication group not encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ElastiCache replication group not encrypted at
  rest
---

# ElastiCache replication group not encrypted at rest

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `76976de7-c7b1-4f64-a94f-90c1345914c2`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group#at_rest_encryption_enabled)

### Description{% #description %}

AWS ElastiCache Replication Group stores sensitive data that should be protected from unauthorized access through encryption at rest. When at-rest encryption is disabled, any data stored in the cache is vulnerable to unauthorized access if the physical storage media is compromised, stolen, or improperly decommissioned. Enabling encryption ensures that all data written to disk is encrypted, protecting against data exposure and meeting compliance requirements for data protection. To secure your ElastiCache Replication Group, add the attribute `at_rest_encryption_enabled = true` to your configuration, as shown in the following example: ``` resource "aws_elasticache_replication_group" "example" { // other configurations at_rest_encryption_enabled = true }

````


## Compliant Code Examples
```terraform
resource "aws_elasticache_replication_group" "example3" {
  automatic_failover_enabled    = true
  availability_zones            = ["us-west-2a", "us-west-2b"]
  replication_group_id          = "tf-rep-group-1"
  replication_group_description = "test description"
  node_type                     = "cache.m4.large"
  number_cache_clusters         = 2
  port                          = 6379
  at_rest_encryption_enabled    = true
}
````

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_elasticache_replication_group" "example2" {
  automatic_failover_enabled    = true
  availability_zones            = ["us-west-2a", "us-west-2b"]
  replication_group_id          = "tf-rep-group-1"
  replication_group_description = "test description"
  node_type                     = "cache.m4.large"
  number_cache_clusters         = 2
  port                          = 6379
  at_rest_encryption_enabled    = false
}
```

```terraform
resource "aws_elasticache_replication_group" "example" {
  automatic_failover_enabled    = true
  availability_zones            = ["us-west-2a", "us-west-2b"]
  replication_group_id          = "tf-rep-group-1"
  replication_group_description = "test description"
  node_type                     = "cache.m4.large"
  number_cache_clusters         = 2
  port                          = 6379
}
```
