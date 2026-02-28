# Source: https://docs.datadoghq.com/security/default_rules/b2e-a9g-30x.md

---
title: Google Workspace accessed by Google
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Workspace accessed by Google
---

# Google Workspace accessed by Google
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199)
## Goal{% #goal %}

Create a signal when Google accesses your Google Workspace tenant using administrative tools.

## Strategy{% #strategy %}

Monitor Google Workspace logs to detect `ACCESS` events, which are part of Google's [Access Transparency](https://support.google.com/a/answer/9230474?hl=en) logs.

## Triage and response{% #triage-and-response %}

1. Determine the scope of Google's access activity, which can be found in the `ACCESS` event in the Google Workspace event log.
1. Review which Google Workspace user (`@event.parameters.OWNER_EMAIL`) and resources (`@event.parameters.RESOURCE_NAME`) were accessed by Google.
1. Investigate the resource(s) being accessed to determine if there is a legitimate reason it should be reviewed by Google.
