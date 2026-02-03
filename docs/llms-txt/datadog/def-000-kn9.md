# Source: https://docs.datadoghq.com/security/default_rules/def-000-kn9.md

---
title: Impossible travel observed from business logic event
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Impossible travel observed from
  business logic event
---

# Impossible travel observed from business logic event
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect an Impossible Travel event when two business logic events attributed to the same user occur within a short time frame from IPs that are geographically distant from one another.

## Strategy{% #strategy %}

The Impossible Travel detection algorithm compares the most recent business logic events to determine if the user {{@usr.id}} traveled a large distance at a high speed, based on the IP address.

If it does so, an `Info` signal is triggered.

**NOTE** VPNs and other known IP anonymizers are filtered out of this signal.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.id}}` plausibly could have traveled from `{{@impossible_travel.triggering_locations.first_location.city}}` (`{{@impossible_travel.triggering_locations.first_location.country}}`) to `{{@impossible_travel.triggering_locations.second_location.city}}`, (`{{@impossible_travel.triggering_locations.second_location.country}}`) in this timespan. 1.1 Review whether this activity may have gone through a proxy. This would make the signal a false positive.
1. If one of those locations appears unusual, the user may have been compromised. You should reset the credentials of the user and reset their session. Optionally, you may also block them while you're performing those actions.
1. Audit any recent action from this user.
