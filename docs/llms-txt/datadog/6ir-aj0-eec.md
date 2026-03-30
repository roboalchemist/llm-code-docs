# Source: https://docs.datadoghq.com/security/default_rules/6ir-aj0-eec.md

---
title: Azure Firewall Threat Intelligence Alert
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Firewall Threat Intelligence
  Alert
---

# Azure Firewall Threat Intelligence Alert
Classification:threat-intel
## Goal{% #goal %}

Detect when an Azure firewall threat intelligence alert is received.

## Strategy{% #strategy %}

Monitor Azure Network Diagnostic logs and detect when `@evt.name` is equal to `AzureFirewallThreatIntelLog`.

## Triage and response{% #triage-and-response %}

1. Inspect the threat intelligence log.
1. Investigate the activity from this IP address.
