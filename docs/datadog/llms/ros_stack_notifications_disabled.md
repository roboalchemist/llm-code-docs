# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ros_stack_notifications_disabled.md

---
title: ROS stack notifications disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ROS stack notifications disabled
---

# ROS stack notifications disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9ef08939-ea40-489c-8851-667870b2ef50`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ros_stack#notification_urls)

### Description{% #description %}

The `alicloud_ros_stack` resource must include the `notification_urls` attribute with at least one URL to receive stack-related events. Without a defined, non-empty `notification_urls`, the stack will not receive lifecycle notifications such as create, update, or rollback.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ros_stack" "example" {
  stack_name        = "tf-testaccstack"
  notification_urls = ["oss://ros/stack-notification/demo"]
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
  stack_policy_body = <<EOF
    {
        "Statement": [{
            "Action": "Update:Delete",
            "Resource": "*",
            "Effect": "Allow",
            "Principal": "*"
        }]
    }
    EOF
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_ros_stack" "example" {
  stack_name        = "tf-testaccstack"
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
  stack_policy_body = <<EOF
    {
        "Statement": [{
            "Action": "Update:Delete",
            "Resource": "*",
            "Effect": "Allow",
            "Principal": "*"
        }]
    }
    EOF
}
```

```terraform
resource "alicloud_ros_stack" "example" {
  stack_name        = "tf-testaccstack"
  notification_urls = []
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
  stack_policy_body = <<EOF
    {
        "Statement": [{
            "Action": "Update:Delete",
            "Resource": "*",
            "Effect": "Allow",
            "Principal": "*"
        }]
    }
    EOF
}
```
