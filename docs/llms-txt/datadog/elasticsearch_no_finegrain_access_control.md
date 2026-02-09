# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticsearch_no_finegrain_access_control.md

---
title: Fine-grained access control disabled for OpenSearch/Elasticsearch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Fine-grained access control disabled for
  OpenSearch/Elasticsearch
---

# Fine-grained access control disabled for OpenSearch/Elasticsearch

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b4c6d7e8-f9a1-4bcd-89ef-01234abcd567`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opensearch_domain#advanced_security_options)

### Description{% #description %}

Fine-grained access control in AWS OpenSearch and Elasticsearch domains enables administrators to restrict access to specific indices, documents, and fields based on user permissions, significantly enhancing security. Without this control enabled, your domain could be vulnerable to unauthorized access, data breaches, and potential exfiltration of sensitive information stored in your search clusters. Both the `enabled` and `internal_user_database_enabled` parameters must be set to `true` within the `advanced_security_options` block to properly secure the domain, as shown in the following secure configuration:

```terraform
resource "aws_opensearch_domain" "good_example" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = true
    internal_user_database_enabled = true
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_elasticsearch_domain" "good_example" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = true # â Fine-grained access control is enabled
    internal_user_database_enabled = true # â Internal user database is enabled
  }
}
```

```terraform
resource "aws_opensearch_domain" "good_example" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = true # â Fine-grained access control is enabled
    internal_user_database_enabled = true # â Internal user database is enabled
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_opensearch_domain" "bad_example" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = false # â Fine-grained access control is disabled
    internal_user_database_enabled = false # â Internal user database is disabled
  }
}

resource "aws_elasticsearch_domain" "bad_example2" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = false # â Fine-grained access control is disabled
    internal_user_database_enabled = false # â Internal user database is disabled
  }
}

resource "aws_elasticsearch_domain" "bad_example3" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = true
    internal_user_database_enabled = false
  }
}

resource "aws_elasticsearch_domain" "bad_example4" {
  domain_name = "example"

  advanced_security_options {
    enabled                        = false
    internal_user_database_enabled = true
  }
}

resource "aws_elasticsearch_domain" "bad_example5" {
  domain_name = "example"

                                              # â No advanced_security_options block
}
```
