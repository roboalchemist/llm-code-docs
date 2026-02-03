# Source: https://docs.datadoghq.com/security/default_rules/gay-o0u-6in.md

---
title: Compromised AWS EC2 Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Compromised AWS EC2 Instance
---

# Compromised AWS EC2 Instance
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event when a `@userIdentity.type:` `{{@userIdentity.type}}` uses an AWS EC2 access key and filter out VPNs and AWS Internal IPs.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the EC2 instance with `@userIdentity.session_name:` `{{@userIdentity.session_name}}` traveled more than 500km at over 1,000km/hr and used an AWS EC2 access key.

## Triage and response{% #triage-and-response %}

1. Determine if the `@userIdentity.accessKeyId:` `{{@userIdentity.accessKeyId}}` for `@userIdentity.session_name:` `{{@userIdentity.session_name}}` instance should be used from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`.
1. If the EC2 access key should not be used from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`., then consider isolating the account and reset credentials.
1. Audit any instance actions that may have occurred after the illegitimate login.

**NOTE** VPNs and other anonymous IPs are filtered out of this signal

## Changelog{% #changelog %}

- 7 April 2022 - Updated rule name and signal message.
- 30 September 2024 - Updated query to replace attribute `@threat_intel.results.category:anonymizer`.
