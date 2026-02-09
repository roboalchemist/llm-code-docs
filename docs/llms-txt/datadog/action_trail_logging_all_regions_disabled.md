# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/action_trail_logging_all_regions_disabled.md

---
title: Action trail logging for all regions disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Action trail logging for all regions disabled
---

# Action trail logging for all regions disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c065b98e-1515-4991-9dca-b602bd6a2fbb`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/actiontrail_trail#trail_region)

### Description{% #description %}

ActionTrail logging must be enabled for all regions. This rule checks that each `alicloud_actiontrail_trail` resource:

- Includes the `oss_bucket_name` attribute
- Sets both `event_rw` and `trail_region` attributes to `All`

Missing attributes trigger a `MissingAttribute` issue. Incorrect values trigger an `IncorrectValue` issue, with suggested remediation to add or correct the attribute.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_actiontrail_trail" "actiontrail1" {
  trail_name         = "action-trail"
  oss_write_role_arn = "acs:ram::1182725xxxxxxxxxxx"
  oss_bucket_name    = "bucket_name"
  event_rw           = "All"
  trail_region       = "All"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_actiontrail_trail" "actiontrail7" {
  trail_name         = "action-trail"
  oss_write_role_arn = "acs:ram::1182725xxxxxxxxxxx"
  oss_bucket_name    = "bucket_name"
  event_rw           = "Write"
  trail_region       = "cn-beijing"
}
```

```terraform
resource "alicloud_actiontrail_trail" "actiontrail3" {
  trail_name         = "action-trail"
  oss_write_role_arn = "acs:ram::1182725xxxxxxxxxxx"
  oss_bucket_name    = "bucket_name"
  event_rw           = "Read"
  trail_region       = "cn-hangzhou"
}
```

```terraform
resource "alicloud_actiontrail_trail" "actiontrail4" {
  trail_name         = "action-trail"
  oss_write_role_arn = "acs:ram::1182725xxxxxxxxxxx"
  oss_bucket_name    = "bucket_name"
  event_rw           = "Write"
  trail_region       = "cn-hangzhou"
}
```
