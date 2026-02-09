# Source: https://docs.datadoghq.com/security/default_rules/def-000-r8g.md

---
title: PingOne impossible travel authentication attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PingOne impossible travel
  authentication attempt
---

# PingOne impossible travel authentication attempt

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when unusual authentication attempts from different geo locations are made from a single user.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the user `{{@resources.name}}` traveled more than 500km at over 1,000km/h. This detection rule aims to identify potential threats early, allowing for timely investigation and mitigation to protect server resources and maintain service availability.

## Triage and response{% #triage-and-response %}

1. Investigate the source user `{{@resources.name}}` with a request from different geo location from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`.
1. Implement immediate measures to block or limit the impact of the suspicious activity if confirmed as a threat.

## Changelog{% #changelog %}

- 15 September 2025 - Excluded logins from corporate VPNs to reduce false positives.
