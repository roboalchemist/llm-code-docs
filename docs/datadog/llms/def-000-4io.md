# Source: https://docs.datadoghq.com/security/default_rules/def-000-4io.md

---
title: EC2 instances managed by SSM should have a compliant association status
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 instances managed by SSM should
  have a compliant association status
---

# EC2 instances managed by SSM should have a compliant association status

## Description{% #description %}

This control verifies if the AWS Systems Manager `association_status` status is `Success` following the execution of the association on an EC2 instance. Instances that have an empty `association_status`, or an `association_status` of `PENDING` are skipped as they may have been recently onboarded to Systems Manager.

## Remediation{% #remediation %}

For guidance on configuring and troubleshooting association statuses, refer to the [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations-history.html) and [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations-edit.html) sections of the AWS Systems Manager User Guide.
