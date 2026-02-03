# Source: https://docs.datadoghq.com/security/default_rules/def-000-prk.md

---
title: Possible enumeration activity from anomalous number of access denied errors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Possible enumeration activity from
  anomalous number of access denied errors
---

# Possible enumeration activity from anomalous number of access denied errors

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580) 
## Goal{% #goal %}

Detect when a user is generating an anomalous number of failed Read API calls in OCI.

## Strategy{% #strategy %}

Monitor OCI logs to identify when a user (`{{@usr.name}}`) generates an anomalous number of failed API calls. This could be indicative of an attacker attempting to enumerate their permissions and available resources.

## Triage and response{% #triage-and-response %}

1. Investigate the API calls associated with `{{@usr.name}}` in the time frame of the signal.
   - Use the Cloud SIEM - User Investigation dashboard to assess user activity.
1. Contact the user to see if they intended to make these API calls.
1. If the user did not make the API calls:
   - Rotate the credentials.
   - Investigate to see what API calls might have been made that were successful throughout the rest of the environment.
1. If the root cause is not a misconfiguration, investigate any other signals around the same time of the signal by looking at the Host Investigation dashboard.
