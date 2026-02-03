# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/github/github_organization_webhook_with_ssl_disabled.md

---
title: Github organization webhook with SSL disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Github organization webhook with SSL disabled
---

# Github organization webhook with SSL disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ce7c874e-1b88-450b-a5e4-cb76ada3c8a9`

**Cloud Provider:** GitHub

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/github/latest/docs/resources/organization_webhook)

### Description{% #description %}

Check whether insecure SSL is used in GitHub organization webhooks.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "github_organization_webhook" "negative1" {
  name = "web"

  configuration {
    url          = "https://google.de/"
    content_type = "form"
    insecure_ssl = false
  }

  active = false

  events = ["issues"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "github_organization_webhook" "positive1" {
  name = "web"

  configuration {
    url          = "https://google.de/"
    content_type = "form"
    insecure_ssl = true
  }

  active = false

  events = ["issues"]
}
```
