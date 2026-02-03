# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/indefinitely_token.md

---
title: Beta - Databricks token has indefinite lifetime
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Databricks token has indefinite
  lifetime
---

# Beta - Databricks token has indefinite lifetime

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7d05ca25-91b4-42ee-b6f6-b06611a87ce8`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/token)

### Description{% #description %}

The `databricks_token` resource is missing the `lifetime_seconds` attribute, resulting in a token with an indefinite lifetime. This attribute defines the token's validity period and should be set to enforce expiration.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "databricks_token" "negative" {
  provider = databricks.created_workspace
  comment  = "Terraform Provisioning"
  // 100 day token
  lifetime_seconds = 8640000
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_token" "positive" {
  provider = databricks.created_workspace
  comment  = "Terraform Provisioning"
}
```
