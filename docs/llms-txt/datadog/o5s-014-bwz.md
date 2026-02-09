# Source: https://docs.datadoghq.com/security/default_rules/o5s-014-bwz.md

---
title: Abnormal successful Microsoft 365 Exchange login event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Abnormal successful Microsoft 365
  Exchange login event
---

# Abnormal successful Microsoft 365 Exchange login event
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event by a user logging in to Microsoft Exchange.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last and the current Microsoft-365 mailbox login event (`@evt.name:MailboxLogin`) to determine if the user `{{@usr.name}}` traveled more than 500km at over 1,000km/hr.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.name}}` should be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}` in a short period of time.
1. If the user should not be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and reset credentials.
1. Use the Cloud SIEM - User Investigation dashboard to audit any user actions that may have occurred after the illegitimate login.

## Changelog{% #changelog %}

- 15 September 2025 - Excluded logins from corporate VPNs and service accounts to reduce false positives.
- 18 December 2025 - Removed corporate VPNs as a threat intel source.
