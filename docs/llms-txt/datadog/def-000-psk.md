# Source: https://docs.datadoghq.com/security/default_rules/def-000-psk.md

---
title: ECS task definitions should have secure networking modes and user definitions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS task definitions should have secure
  networking modes and user definitions
---

# ECS task definitions should have secure networking modes and user definitions
 
## Description{% #description %}

This configuration check verifies Amazon Elastic Container Service (Amazon ECS) task definitions do not have unauthorized permissions. If task definitions have `NetworkMode` set to `host`, the rule fails if the container definitions have **user** set to `root` or `empty` and **privileged** set to `false` or `empty`.

This control ensures that access is intentionally defined when running tasks using the host network mode. If a task definition includes elevated privileges, it reflects a deliberate configuration choice. The control checks for unexpected privilege escalation in task definitions with host networking enabled when elevated privileges are not explicitly chosen.

Avoid running tasks in host network mode when running containers with the root user (UID 0). As a security best practice, you should always use a non-root user. By default, unless otherwise specified, Docker containers typically run as root. Therefore, explicitly setting a non-root user in the container definition is a security best practice.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Sign in to the **AWS Management Console**.
1. Navigate to the **Amazon ECS service**.
1. Select the cluster where the task definition with non-compliant configurations is located.
1. In the navigation pane, choose **Task Definitions**.
1. Select the task definition that has **NetworkMode** set to `host` and contains **privileged** set to `false` or `empty`, and **user** set to `root` or `empty`.
1. Click **Edit** to modify the task definition.
1. If required, update the privileged setting to `true` based on your application requirements.
1. Ensure that the user is set to a `non-root` user with a non-zero UID.
1. Otherwise, update the network mode to a non-host mode.
1. Save the changes to the task definition.
