# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticsearch_domain_not_encrypted_node_to_node.md

---
title: Elasticsearch domain not encrypted node to node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Elasticsearch domain not encrypted node to
  node
---

# Elasticsearch domain not encrypted node to node

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `967eb3e6-26fc-497d-8895-6428beb6e8e2`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticsearch_domain#node_to_node_encryption)

### Description{% #description %}

Enabling node-to-node encryption for an Elasticsearch domain ensures that data transferred between nodes in the Elasticsearch cluster is securely encrypted, preventing unauthorized access to data in transit. If the `node_to_node_encryption` block is omitted, sensitive data could be intercepted by attackers during communication between cluster nodes. To secure the domain, configure:

```
node_to_node_encryption {
  enabled = true
}
```

This ensures that all internal communications within the cluster is encrypted, reducing the risk of data exposure.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_elasticsearch_domain" "negative1" {
  domain_name           = "example"
  elasticsearch_version = "1.5"

  cluster_config {
    instance_type = "r4.large.elasticsearch"
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }

  node_to_node_encryption {
    enabled = true
  }

  tags = {
    Domain = "TestDomain"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_elasticsearch_domain" "positive1" {
  domain_name           = "example"
  elasticsearch_version = "1.5"

  cluster_config {
    instance_type = "r4.large.elasticsearch"
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }

  node_to_node_encryption {
    enabled = false
  }

  tags = {
    Domain = "TestDomain"
  }
}
```

```terraform
resource "aws_elasticsearch_domain" "positive1" {
  domain_name           = "example"
  elasticsearch_version = "1.5"

  cluster_config {
    instance_type = "r4.large.elasticsearch"
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }

  tags = {
    Domain = "TestDomain"
  }
}
```
