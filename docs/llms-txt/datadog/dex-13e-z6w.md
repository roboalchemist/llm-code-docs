# Source: https://docs.datadoghq.com/security/default_rules/dex-13e-z6w.md

---
title: Impossible Travel Auth0 login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Impossible Travel Auth0 login
---

# Impossible Travel Auth0 login
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event when two successful authentication events occur in a short time frame.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the user `{{@usr.name}}` traveled more than 500km at over 1,000km/hr.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` should have authenticated from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`.
1. If `{{@user.name}}` should not authenticated from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and reset credentials.
1. Audit any instance actions that may have occurred after the illegitimate login.

**NOTE** VPNs and other anonymous IPs are filtered out of this signal

## Changelog{% #changelog %}

- 10 October 2022 - Updated query.
- 20 November 2023 - Updated group by values to include `@usr.id`.
- 30 September 2024 - Updated query to replace attribute `@threat_intel.results.subcategory:anonymizer`.
