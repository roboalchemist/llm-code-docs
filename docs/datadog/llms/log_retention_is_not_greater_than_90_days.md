# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/log_retention_is_not_greater_than_90_days.md

---
title: Log retention is not greater than 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Log retention is not greater than 90 days
---

# Log retention is not greater than 90 days

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ed6cf6ff-9a1f-491c-9f88-e03c0807f390`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/log_store#retention_period)

### Description{% #description %}

The OSS Log Store must have `retention_period` set to at least 90 days to ensure sufficient visibility into resource and object activity.If `retention_period` is undefined, the default is 30 days, which is insufficient.Resources of type `alicloud_log_store` should explicitly set `retention_period` to 90 or more days (for example, `100`).This rule flags `alicloud_log_store` resources that either omit `retention_period` or set it to less than 90 days.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_log_project" "example1" {
  name        = "tf-log"
  description = "created by terraform"
}

resource "alicloud_log_store" "example1" {
  project               = alicloud_log_project.example.name
  name                  = "tf-log-store"
  retention_period      = 91
  shard_count           = 3
  auto_split            = true
  max_split_shard_count = 60
  append_meta           = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_log_project" "example4" {
  name        = "tf-log"
  description = "created by terraform"
}

resource "alicloud_log_store" "example4" {
  project               = alicloud_log_project.example.name
  name                  = "tf-log-store"
  retention_period      = 60
  shard_count           = 3
  auto_split            = true
  max_split_shard_count = 60
  append_meta           = true
}
```

```terraform
resource "alicloud_log_project" "example2" {
  name        = "tf-log"
  description = "created by terraform"
}

resource "alicloud_log_store" "example2" {
  project               = alicloud_log_project.example.name
  name                  = "tf-log-store"
  shard_count           = 3
  auto_split            = true
  max_split_shard_count = 60
  append_meta           = true
}
```
