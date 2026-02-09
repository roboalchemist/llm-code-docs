# Source: https://docs.datadoghq.com/security/default_rules/zb7-axd-ee5.md

---
title: Google Workspace user forwarding email out of non Google Workspace domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Workspace user forwarding email
  out of non Google Workspace domain
---

# Google Workspace user forwarding email out of non Google Workspace domain
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1114-email-collection](https://attack.mitre.org/techniques/T1114) 
## Goal{% #goal %}

Create a signal when Google Workspace detects a user setting up mail forwarding to a non-Google Workspace domain.

## Strategy{% #strategy %}

Monitor Google Workspace logs to detect when `email_forwarding_out_of_domain` events.

## Triage and response{% #triage-and-response %}

1. Determine if the email address defined in `@event.parameters.email_forwarding_destination_address` is legitimate.
1. If the forwarding destination address is not legitimate, review all activity for `{{@usr.email}}` and all activity around the following IP: `{{@network.client.ip}}`.
