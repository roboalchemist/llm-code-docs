# Source: https://docs.datadoghq.com/security/default_rules/d8d-awv-jsf.md

---
title: Google Workspace Alert Center
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Workspace Alert Center
---

# Google Workspace Alert Center
Classification:attack
## Goal{% #goal %}

Detect when [Google Workspace Alert Center](https://support.google.com/a/answer/9105393?hl=en) raises an alert.

## Strategy{% #strategy %}

Google Workspace Alert Center provides a comprehensive view of security related notifications, alerts, and actions across Google Workspace.

See [View alert details](https://support.google.com/a/answer/9104586#zippy=) for information about each type of alert.

## Triage and response{% #triage-and-response %}

1. Investigate the Google Workspace alert to determine if it is malicious or benign.
1. If the finding is deemed malicious, follow the [remediation guidance](https://support.google.com/a/answer/11123535?hl=en&ref_topic=9105077) provided by Google and also any internal incident response processes.
1. If the finding is a false positive, you can reduce false positives by:
   - [Providing feedback on alerts](https://support.google.com/a/answer/9104881?hl=en&ref_topic=9105077)
   - [Using rules to turn alerts on or off](https://support.google.com/a/answer/9288156?hl=en&ref_topic=9105077)
