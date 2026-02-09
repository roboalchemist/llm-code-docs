# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/no_ros_stack_policy.md

---
title: No ROS stack policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > No ROS stack policy
---

# No ROS stack policy

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `72ceb736-0aee-43ea-a191-3a69ab135681`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ros_stack)

### Description{% #description %}

A ROS stack should define a stack policy to protect resources from unintended changes during creation and update actions. Each `alicloud_ros_stack` resource must include either `stack_policy_body` or `stack_policy_url` for creation protection. For update protection, it must include either `stack_policy_during_update_body` or `stack_policy_during_update_url`. This rule reports a `MissingAttribute` issue when the corresponding attribute is not defined.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ros_stack" "neg2" {
  stack_name        = "tf-testaccstack"
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
  stack_policy_url = "oss://ros/stack-policy/demo"

  stack_policy_during_update_body = "oss://ros/stack-policy/demo"
}
```

```terraform
resource "alicloud_ros_stack" "neg1" {
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

  stack_policy_during_update_body = <<EOF
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
resource "alicloud_ros_stack" "pos2" {
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
resource "alicloud_ros_stack" "pos3" {
  stack_name        = "tf-testaccstack"
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
  stack_policy_during_update_body = <<EOF
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
resource "alicloud_ros_stack" "pos" {
  stack_name        = "tf-testaccstack"
  template_body     = <<EOF
    {
        "ROSTemplateFormatVersion": "2015-09-01"
    }
    EOF
}
```
