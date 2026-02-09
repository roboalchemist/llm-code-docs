# Source: https://docs.datadoghq.com/security/default_rules/def-000-ihg.md

---
title: Forcepoint Secure Web Gateway unusual spike found in web category urls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Secure Web Gateway unusual
  spike found in web category urls
---

# Forcepoint Secure Web Gateway unusual spike found in web category urls

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071) 
## Goal{% #goal %}

Identify an unusual spike in request for URLs within a {{@webcategories}}.

## Strategy{% #strategy %}

This rule analyzes Forcepoint SWG logs to detect an abnormal increase in requests for URLs within a specific web category.

## Triage and Response{% #triage-and-response %}

1. Analyze the Forcepoint SWG logs and identify the users and user groups associated with spike in request for web category `{{@webcategories}}` URLs.
1. Check the web reputation of the URLs being accessed within the flagged category. Ensure that no high-risk URLs or known malicious destinations are being requested.
1. Examine any correlated activities that could be linked to the spike, such as file uploads, downloads, or data requests that may raise security concerns (such as matching DLP patterns or confidential data uploads).
1. Review actions taken by Forcepoint SWG, and block the web category or specific URLs associated with suspicious activity if they have not already been blocked.
1. Notify the users about the suspicious activity and educate them on safe browsing practices.
