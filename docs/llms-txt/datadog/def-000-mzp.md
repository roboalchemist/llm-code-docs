# Source: https://docs.datadoghq.com/security/default_rules/def-000-mzp.md

---
title: EventBridge custom event buses should have a resource-based policy attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EventBridge custom event buses should
  have a resource-based policy attached
---

# EventBridge custom event buses should have a resource-based policy attached

## Description{% #description %}

This control verifies whether a resource-based policy is attached to an Amazon EventBridge custom event bus. The control fails if the event bus lacks a resource-based policy.

Without a resource-based policy by default, an EventBridge custom event bus permits access by principals within the account. By adding a resource-based policy, you can restrict access to the event bus to specific accounts and intentionally grant access to external entities as needed.

## Remediation{% #remediation %}

For steps to attach a resource-based policy to an EventBridge custom event bus, refer to [Using Resource-Based Policies for Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html) in the Amazon EventBridge User Guide.
