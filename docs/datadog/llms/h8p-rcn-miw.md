# Source: https://docs.datadoghq.com/security/default_rules/h8p-rcn-miw.md

---
title: AWS WAF traffic blocked by specific rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS WAF traffic blocked by specific
  rule
---

# AWS WAF traffic blocked by specific rule

## Goal{% #goal %}

Detects when a specific AWS Web Application Firewall (WAF) rule blocks an anomalous amount of traffic.

## Strategy{% #strategy %}

The rule monitors AWS WAF logs and detects when the `@system.action` has a value of `BLOCK`.

## Triage and response{% #triage-and-response %}

1. Inspect the `@webaclId`: `{{@webaclId}}` logs to confirm if the observed traffic should have been blocked or not.
1. If the request should have been blocked, then navigate to the IP Investigation dashboard. Inspect other requests from the IP address:{{@network.client.ip}} to find any other potentially malicious behaviors from the IP.
