# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ros_stack_retention_disabled.md

---
title: ROS stack retention disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ROS stack retention disabled
---

# ROS stack retention disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4bb06fa1-2114-4a00-b7b5-6aeab8b896f0`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ros_stack_instance#retain_stacks)

### Description{% #description %}

The `retain_stacks` attribute should be enabled to preserve the stack when deleting a stack instance from a stack group. If `retain_stacks` is undefined or set to `false`, the underlying `alicloud_ros_stack_instance` is deleted when the instance is removed. Set `retain_stacks = true` to retain the stack.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ros_stack_instance" "example" {
  stack_group_name          = alicloud_ros_stack_group.example.stack_group_name
  stack_instance_account_id = "example_value"
  stack_instance_region_id  = data.alicloud_ros_regions.example.regions.0.region_id
  operation_preferences     = "{\"FailureToleranceCount\": 1, \"MaxConcurrentCount\": 2}"
  retain_stacks             = true
  parameter_overrides {
    parameter_value = "VpcName"
    parameter_key   = "VpcName"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_ros_stack_instance" "example" {
  stack_group_name          = alicloud_ros_stack_group.example.stack_group_name
  stack_instance_account_id = "example_value"
  stack_instance_region_id  = data.alicloud_ros_regions.example.regions.0.region_id
  operation_preferences     = "{\"FailureToleranceCount\": 1, \"MaxConcurrentCount\": 2}"
  parameter_overrides {
    parameter_value = "VpcName"
    parameter_key   = "VpcName"
  }
}
```

```terraform
resource "alicloud_ros_stack_instance" "example" {
  stack_group_name          = alicloud_ros_stack_group.example.stack_group_name
  stack_instance_account_id = "example_value"
  stack_instance_region_id  = data.alicloud_ros_regions.example.regions.0.region_id
  operation_preferences     = "{\"FailureToleranceCount\": 1, \"MaxConcurrentCount\": 2}"
  retain_stacks             = false
  parameter_overrides {
    parameter_value = "VpcName"
    parameter_key   = "VpcName"
  }
}
```
