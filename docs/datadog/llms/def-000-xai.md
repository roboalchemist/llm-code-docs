# Source: https://docs.datadoghq.com/security/default_rules/def-000-xai.md

---
title: >-
  GCP Compute Engine Default Service Account has overly permissive access to
  resources in the project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GCP Compute Engine Default Service
  Account has overly permissive access to resources in the project
---

# GCP Compute Engine Default Service Account has overly permissive access to resources in the project

## Description{% #description %}

The Compute Engine default service account is associated with your Google Cloud project and attached by default to Compute Engine virtual machines, unless you explicitly assign another service account on virtual machine creation, to provide credentials to applications running on the instance.

## Rationale{% #rationale %}

Depending on your organization policy configuration, the default service account automatically grants the Editor role on your project. The permissions in the Editor role let you create and delete resources for most Google Cloud services within your Google Cloud project.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to the Compute Engine default service account to the minimum required for it to fulfill its function. To remediate the issue, remove the Editor role binding from the Compute Engine default service account on the project resource, and create a new role binding with the required permissions for your Compute Engine virtual machines.
