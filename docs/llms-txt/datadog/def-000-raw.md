# Source: https://docs.datadoghq.com/security/default_rules/def-000-raw.md

---
title: >-
  GCP User managed Service Account has overly permissive access to resources in
  the project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GCP User managed Service Account has
  overly permissive access to resources in the project
---

# GCP User managed Service Account has overly permissive access to resources in the project
 
## Description{% #description %}

Editor or Owner roles are highly permissive roles that existed prior to the introduction of IAM.

## Rationale{% #rationale %}

Assigning the Editor or Owner role to a user managed service account grants them full control over all resources in the project. This includes the ability to create, modify, and delete resources across all services in the project.

## Remediation{% #remediation %}

Datadog recommends using predefined roles or creating custom roles with the minimum required permissions for users to fulfill their function. To remediate the issue, remove the Editor or Owner role binding from the user managed service account on the project resource, and create a new role binding with the required permissions for the user account.
