# Source: https://docs.datadoghq.com/security/default_rules/def-000-yj3.md

---
title: Impossible travel scenario observed in Wiz authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Impossible travel scenario observed in
  Wiz authentication
---

# Impossible travel scenario observed in Wiz authentication

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event within Wiz authentication.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the user (`@usr.email`) traveled more than 500km at over 1,000km/h.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.email}}` should be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}`, `{{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}`, `{{@impossible_travel.triggering_locations.second_location.country}}` in a short period of time.
1. If the user should not be connecting from `{{@impossible_travel.triggering_locations.first_location.city}}`, `{{@impossible_travel.triggering_locations.first_location.country}}` or `{{@impossible_travel.triggering_locations.second_location.city}}`, `{{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and resetting their credentials.
1. Use the Cloud SIEM - User Investigation dashboard to audit any user actions that may have occurred after the illegitimate login.
