# Source: https://docs.datadoghq.com/security/default_rules/def-000-gsr.md

---
title: Google Compute Engine firewall egress rule opened to the world
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Compute Engine firewall egress
  rule opened to the world
---

# Google Compute Engine firewall egress rule opened to the world
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a Google Compute Engine firewall egress rule is opened to the world.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when a `v*.compute.firewalls.insert` API call is made with the traffic direction as egress (`@data.protoPayload.request.direction:EGRESS`) and the destination range as all IP addresses (`@data.protoPayload.request.destinationRanges:0.0.0.0/0`).

An excessively open firewall rule like this could be a sign of an ongoing cryptomining attack.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.id}}` from IP address `{{@network.client.ip}}` should have made the `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate the user credentials.
- Determine what other API calls were made by the user.
- Investigate VPC flow logs and OS system logs to determine if unauthorized access occurred.
If the API call was made legitimately by the user:
- Advise the user to modify the IP range to the company private network or bastion host.

## Changelog{% #changelog %}

- 17 August 2023 - Updated query to replace attribute `@threat_intel.results.subcategory:tor` with `@threat_intel.results.category:tor`.
- 25 September 2024 - Updated query to replace attribute `@threat_intel.results.category:anonymizer`.
