# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ros_stack_without_template.md

---
title: ROS stack without template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ROS stack without template
---

# ROS stack without template

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `92d65c51-5d82-4507-a2a1-d252e9706855`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Build Process

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ros_stack)

### Description{% #description %}

An `alicloud_ros_stack` resource must define a template using either the `template_url` or `template_body` attribute. At least one of these must be present to describe the stack template. If both are missing, the rule reports a `MissingAttribute` issue indicating that one of the two must be set. This ensures ROS has a template to provision resources.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ros_stack" "example1" {
  stack_name        = "tf-testaccstack1"
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
