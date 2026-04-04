# Source: https://docs.datadoghq.com/security/default_rules/def-000-m2r.md

---
title: Publicly accessible Google Compute instance uses a privileged service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Google Compute
  instance uses a privileged service account
---

# Publicly accessible Google Compute instance uses a privileged service account

## Description{% #description %}

A publicly accessible VM instance has a Service Account with a privileged or administrative IAM policy. If an attacker retrieves the VM instance credentials through a vulnerability or other misconfiguration, they can compromise the victim's Google Cloud project resources.

## Remediation{% #remediation %}

1. Identify the service account assigned to the VM instance.
1. Identify effective permissions using [Policy Analyzer](https://console.cloud.google.com/iam-admin/analyzer).
1. Scope the policy to grant only the permissions that are required based on [Google Cloud Role recommendations](https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
