# Source: https://docs.datadoghq.com/security/default_rules/def-000-tie.md

---
title: Asana content export initiated by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Asana content export initiated by user
---

# Asana content export initiated by user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect mass downloading of Asana attachments, which may represent data exfiltration of sensitive files.

## Strategy{% #strategy %}

This rule monitors Asana audit logs for `attachment_downloaded` events performed by a user and triggers an alert, with varying severity based on the quantity of attachments download.

An [attachment object](https://developers.asana.com/reference/attachments) represents any file attached to a task in Asana, whether it's an uploaded file or one associated through a third-party service such as Dropbox or Google Drive.

## Triage & Response{% #triage--response %}

- Verify the identity of the actor (`{{@usr.email}}`) and determine if they have legitimate business reasons to download multiple attachments.
- Review which attachments were downloaded and determine their sensitivity level.
- Analyze the actor's normal access patterns to identify deviations from typical behavior.
- Evaluate if the downloads occurred from unusual geographic locations or IP addresses.
- If malicious activity is suspected, begin your security incident response process.

## References{% #references %}
