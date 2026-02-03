# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/redis_disabled.md

---
title: Redis disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redis disabled
---

# Redis disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4bd15dd9-8d5e-4008-8532-27eb0c3706d3`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_cluster#engine)

### Description{% #description %}

ElastiCache clusters should have the Redis engine enabled (`engine = "redis"`) to ensure compliance with strict security and compliance regulations, including FedRAMP, HIPAA, and PCI DSS. Using the default `memcached` engine (`engine = "memcached"`) does not provide the advanced security and access control features available in Redis, and may result in non-compliance with these frameworks. If the ElastiCache engine is left as Memcached, organizations risk exposing sensitive or regulated data to unauthorized access, potentially leading to regulatory penalties and data breaches. It is important to review ElastiCache configurations to ensure that the Redis engine is explicitly selected when required for compliance.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "aws_elasticache_cluster" "negative1" {
  cluster_id           = "cluster-example"
  engine               = "redis"
  node_type            = "cache.m4.large"
  num_cache_nodes      = 2
  port                 = 11211
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "aws_elasticache_cluster" "positive1" {
  cluster_id           = "cluster-example"
  engine               = "memcached"
  node_type            = "cache.m4.large"
  num_cache_nodes      = 1
  engine_version       = "3.2.10"
  port                 = 6379
}
```
