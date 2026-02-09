# Source: https://docs.datadoghq.com/security/default_rules/def-000-dqn.md

---
title: Forcepoint Security Service Edge high number of download events from a user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Security Service Edge high
  number of download events from a user
---

# Forcepoint Security Service Edge high number of download events from a user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detects high number of download activity performed by a user.

## Strategy{% #strategy %}

Monitor user's download activities to identify potential risks or abnormal behavior.

## Triage and Response{% #triage-and-response %}

1. Confirm the user - `{{@usr.name}}` associated with the activity and their access rights.
1. Determine if the volume or frequency of the transfer is justified by ongoing tasks and check the device or system used for the download activity.
1. Notify the user about the spike and request justification for the activity. Escalate the matter to the security team if the activity cannot be explained.
