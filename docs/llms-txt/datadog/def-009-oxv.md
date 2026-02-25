# Source: https://docs.datadoghq.com/security/default_rules/def-009-oxv.md

---
title: Slack private channel converted to public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack private channel converted to
  public
---

# Slack private channel converted to public
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a Slack channel is changed from private to public.

## Strategy{% #strategy %}

This rule monitors Slack events for when a channel's privacy setting is modified from private to public. Changing a private channel to public can expose sensitive conversations, files, and information that were previously restricted. This action may be deliberate, accidental, or malicious, making it essential to track and verify the intent behind the change.

Potential risks associated with this change include:

- Exposure of sensitive or confidential information to a wider audience.
- Unintended sharing of critical discussions with external collaborators or users.
- Increased risk of data leaks or breaches if the channel contains sensitive information.

## Triage and response{% #triage-and-response %}

1. Determine if the channel change is expected by:

   - Contacting the channel owner or administrators to confirm if they authorized the change.
   - Reviewing Slack logs related to the user `{{@usr.email}}` who performed the change, focusing on:
     - The time of the change and surrounding activities.
     - Unusual behavior or other changes, such as role modifications or new members added to the channel.
   - Checking the content of the channel to assess whether it contains sensitive information that should not be public.

1. If the activity is deemed unauthorized or malicious:

   - Begin your organization's incident response process to investigate further.
   - Immediately revert the channel back to private if it contains sensitive data.
   - Review access permissions and ensure only trusted users can modify channel privacy settings.
   - Investigate if any unauthorized users accessed the channel while it was public and evaluate potential exposure.
