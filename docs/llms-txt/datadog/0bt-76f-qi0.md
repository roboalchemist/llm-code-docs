# Source: https://docs.datadoghq.com/security/default_rules/0bt-76f-qi0.md

---
title: Azure user ran command on container instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure user ran command on container
  instance
---

# Azure user ran command on container instance
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609) 
## Goal{% #goal %}

Detect when a command is executed on a container instance with the Azure API.

## Strategy{% #strategy %}

Monitor Azure container instance logs where `@evt.name` is `"MICROSOFT.CONTAINERINSTANCE/CONTAINERGROUPS/CONTAINERS/EXEC/ACTION"` and `@evt.outcome` is `Success`.

## Triage and response{% #triage-and-response %}

1. Verify that the user (`{{@usr.id}}`) should be executing commands on the container (`@resourceId`).
1. If the activity is not expected, investigate the activity around the container (`@resourceId`).
