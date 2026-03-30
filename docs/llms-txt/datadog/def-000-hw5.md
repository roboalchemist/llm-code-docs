# Source: https://docs.datadoghq.com/security/default_rules/def-000-hw5.md

---
title: Google Workspace administrator initiated a data transfer request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Workspace administrator
  initiated a data transfer request
---

# Google Workspace administrator initiated a data transfer request
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1537-transfer-data-to-cloud-account](https://attack.mitre.org/techniques/T1537)
## Goal{% #goal %}

Detect when a Google Workspace administrator initiates a data transfer request.

## Strategy{% #strategy %}

Monitor Google Workspace logs to detect when a Google Workspace administrator initiates a request to transfer the ownership of a user's data to a destination user within the same organization. This request is typically made when a user has left an organization and their data is transferred to another user. However, the service could be leveraged by an attacker to transfer data to an attacker-controlled account for exfiltration.

## Triage and response{% #triage-and-response %}

1. Determine if there is a legitimate reason for the data transfer request.
1. If there is not a legitimate reason, investigate activity from around the Google Workspace administrator (`{{@usr.email}}`) and IP address that initiated the request (`{{@network.client.ip}}`).
