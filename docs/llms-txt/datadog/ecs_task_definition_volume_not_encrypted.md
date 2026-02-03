# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ecs_task_definition_volume_not_encrypted.md

---
title: ECS task definition volume not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECS task definition volume not encrypted
---

# ECS task definition volume not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4d46ff3b-7160-41d1-a310-71d6d370b08f`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition#transit_encryption)

### Description{% #description %}

Amazon ECS task definition with EFS volumes should have transit encryption enabled to protect sensitive data transmitted between the ECS host and the EFS server. When transit encryption is disabled, data can be intercepted and read by unauthorized entities during transmission, posing a significant security risk to your containerized applications. To secure your EFS volumes, ensure the `transit_encryption` parameter is set to `ENABLED` in the `efs_volume_configuration` block, as shown below:

```
efs_volume_configuration {
  file_system_id = aws_efs_file_system.fs.id
  transit_encryption = "ENABLED"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ecs_task_definition" "service" {
  family                = "service"
  container_definitions = file("task-definitions/service.json")

  volume {
    name = "service-storage"

    efs_volume_configuration {
      file_system_id          = aws_efs_file_system.fs.id
      root_directory          = "/opt/data"
      transit_encryption      = "ENABLED"
      transit_encryption_port = 2999
      authorization_config {
        access_point_id = aws_efs_access_point.test.id
        iam             = "ENABLED"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ecs_task_definition" "service_2" {
  family                = "service"
  container_definitions = file("task-definitions/service.json")

  volume {
    name = "service-storage"

    efs_volume_configuration {
      file_system_id          = aws_efs_file_system.fs.id
      root_directory          = "/opt/data"
      transit_encryption_port = 2999
      authorization_config {
        access_point_id = aws_efs_access_point.test.id
        iam             = "ENABLED"
      }
    }
  }
}
```

```terraform
resource "aws_ecs_task_definition" "service_2" {
  family                = "service"
  container_definitions = file("task-definitions/service.json")

  volume {
    name = "service-storage"
  }
}
```

```terraform
resource "aws_ecs_task_definition" "service" {
  family                = "service"
  container_definitions = file("task-definitions/service.json")

  volume {
    name = "service-storage"

    efs_volume_configuration {
      file_system_id          = aws_efs_file_system.fs.id
      root_directory          = "/opt/data"
      transit_encryption      = "DISABLED"
      transit_encryption_port = 2999
      authorization_config {
        access_point_id = aws_efs_access_point.test.id
        iam             = "ENABLED"
      }
    }
  }
}
```
