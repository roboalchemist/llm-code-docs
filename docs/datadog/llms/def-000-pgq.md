# Source: https://docs.datadoghq.com/security/default_rules/def-000-pgq.md

---
title: Twilio bulk export from unusual location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Twilio bulk export from unusual
  location
---

# Twilio bulk export from unusual location
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1537-transfer-data-to-cloud-account](https://attack.mitre.org/techniques/T1537)
## Goal{% #goal %}

Detect when a BulkExport operation was detected from unsual location.

## Strategy{% #strategy %}

This rule monitors for [BulkExport](https://www.twilio.com/docs/usage/bulkexport) API calls from unusual location. This may indicate an attacker gaining access to sensitive inforamtion and exfiltrating data.

## Triage and response{% #triage-and-response %}

1. Investigate the other actions performed by the account SID `{{@account_sid}}`.
1. Follow the [guidelines](https://help.twilio.com/articles/360021347073) provided by Twilio.
