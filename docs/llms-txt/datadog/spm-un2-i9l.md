# Source: https://docs.datadoghq.com/security/default_rules/spm-un2-i9l.md

---
title: AWS ConsoleLogin without MFA triggered Impossible Travel scenario
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS ConsoleLogin without MFA triggered
  Impossible Travel scenario
---

# AWS ConsoleLogin without MFA triggered Impossible Travel scenario
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event when a `@userIdentity.type:` `{{@userIdentity.type}}` performs a `consoleLogin` without a multi-factor authentication (MFA) device.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the user with `@userIdentity.session_name:` `{{@userIdentity.session_name}}` traveled more than 500km at over 1,000km/h and the account does not have MFA enabled.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}` in a short period of time.
1. If the user should not be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and reset credentials.
1. Use the Cloud SIEM - User Investigation dashboard to audit any user actions that may have occurred after the illegitimate login.

## Changelog{% #changelog %}

- 30 September 2024 - Updated query to replace attribute `@threat_intel.results.subcategory:anonymizer`.
