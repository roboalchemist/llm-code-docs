# Source: https://docs.datadoghq.com/security/default_rules/def-000-gi8.md

---
title: Keycloak impossible user travel detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keycloak impossible user travel
  detected
---

# Keycloak impossible user travel detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Identify instances where users are trying to login from two distant geographical locations within an improbable time frame, potentially indicating credential theft or account compromise.

## Strategy{% #strategy %}

This rule analyzes login events to identify cases where a user appears to perform activities from two different countries or cities within a time frame that would make physical travel between those locations impossible.

## Triage and response{% #triage-and-response %}

1. Determine if userId `{{@usr.id}}` connected from `{{@impossible_travel.triggering_locations.first_location.city}}`, `{{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}`, `{{@impossible_travel.triggering_locations.second_location.country}}` in a short period of time.
1. Check for any failed login attempts or other unusual activities related to the user.
1. Contact the affected user to verify whether they initiated the login events.
1. If the user did not perform the logins, restrict their access until their credentials are reset.
