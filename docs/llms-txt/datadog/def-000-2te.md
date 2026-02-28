# Source: https://docs.datadoghq.com/security/default_rules/def-000-2te.md

---
title: Impossible travel GitLab event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Impossible travel GitLab event
---

# Impossible travel GitLab event

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect an Impossible Travel event when two successful events occur in a short time frame from geographically far locations.

## Strategy{% #strategy %}

The Impossible Travel detection type's algorithm compares the GeoIP data of the last log and the current log to determine if the user `{{@usr.name}}` traveled more than 500km at over 1,000km/hr.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` should have authenticated from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`.
1. If `{{@user.name}}` should not authenticated from `{{@impossible_travel.triggering_locations.first_location.city}}, {{@impossible_travel.triggering_locations.first_location.country}}` and `{{@impossible_travel.triggering_locations.second_location.city}}, {{@impossible_travel.triggering_locations.second_location.country}}`, then consider isolating the account and reset credentials.
1. Audit any instance actions that may have occurred after the illegitimate login.
