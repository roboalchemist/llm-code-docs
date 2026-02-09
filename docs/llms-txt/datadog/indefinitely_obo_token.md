# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/indefinitely_obo_token.md

---
title: Beta - Databricks OBO token has indefinite lifetime
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Databricks OBO token has indefinite
  lifetime
---

# Beta - Databricks OBO token has indefinite lifetime

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `23e1f5f0-12b7-4d7e-9087-f60f42ccd514`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/obo_token)

### Description{% #description %}

`databricks_obo_token` has an indefinite lifetime. OBO tokens must include a `lifetime_seconds` attribute to enforce a finite validity period. This rule flags any `databricks_obo_token` resource that does not set `lifetime_seconds`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "databricks_obo_token" "negative" {
  depends_on       = [databricks_group_member.this]
  application_id   = databricks_service_principal.this.application_id
  comment          = "PAT on behalf of ${databricks_service_principal.this.display_name}"
  lifetime_seconds = 3600
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_obo_token" "positive" {
  depends_on       = [databricks_group_member.this]
  application_id   = databricks_service_principal.this.application_id
  comment          = "PAT on behalf of ${databricks_service_principal.this.display_name}"
}
```
