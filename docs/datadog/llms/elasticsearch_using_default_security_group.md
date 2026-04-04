# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticsearch_using_default_security_group.md

---
title: Elasticsearch uses default security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Elasticsearch uses default security group
---

# Elasticsearch uses default security group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d3e1f5a9-bb45-4c89-b97c-12d34ef56789`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticsearch_domain#vpc_options)

### Description{% #description %}

AWS Elasticsearch and OpenSearch domains should be assigned explicit security groups instead of relying on the default security group. When no security group is specified or an empty list is provided, the default security group is automatically assigned, which typically allows broad inbound/outbound traffic within the VPC and potentially exposes the service to unintended access from other resources. This vulnerability could lead to unauthorized access to sensitive data, potential data breaches, or service disruption.

To remediate this issue, always specify at least one security group ID in the `security_group_ids` list:

```
resource "aws_elasticsearch_domain" "good_example" {
  domain_name = "example"

  vpc_options {
    security_group_ids = ["sg-12345678"] // Explicit security group
  }
}
```

Avoid empty security group lists or omitting the security_group_ids attribute.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_elasticsearch_domain" "good_example" {
  domain_name = "example"

  vpc_options {

  }
}
```

```terraform
resource "aws_opensearch_domain" "good_example" {
  domain_name = "example"

  vpc_options {
    security_group_ids = ["sg-87654321"] # â Explicit security group assigned
  }
}
```

```terraform
resource "aws_elasticsearch_domain" "good_example" {
  domain_name = "example"

  vpc_options {
    security_group_ids = ["sg-12345678"] # â Explicit security group assigned
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_elasticsearch_domain" "bad_example" {
  domain_name = "example"

  vpc_options {
    security_group_ids = []
  }
}

resource "aws_opensearch_domain" "bad_example" {
  domain_name = "example"

  vpc_options {
    security_group_ids = []
  }
}
```
