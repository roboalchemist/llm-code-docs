# Source: https://docs.datadoghq.com/security/default_rules/def-004-oxv.md

---
title: Slack CLI login from suspicious IP address
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack CLI login from suspicious IP
  address
---

# Slack CLI login from suspicious IP address
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a Slack CLI login occurs from a suspicious IP address.

## Strategy{% #strategy %}

This rule monitors Slack events for CLI logins that originate from suspicious or unusual IP addresses. A CLI login from a risky IP could indicate unauthorized access, especially if it originates from a Tor exit node or an IP previously associated with malicious activity.

Potential risks associated with suspicious CLI logins include:

- Unauthorized access to Slack data, configurations, or admin-level actions.
- Compromised user credentials allowing attackers to interact with the workspace through API calls.
- Further infiltration into the organization' systems or data exfiltration.

## Triage and response{% #triage-and-response %}

1. Determine if the login is expected by:

   - Contacting the user `{{@usr.email}}` to confirm if they performed the CLI login from the identified IP address.
   - Checking Slack logs for unusual activities after the login, such as privilege escalations, data downloads, or unauthorized API interactions.

1. If the login is deemed suspicious or unauthorized:

   - Begin your organization's incident response process and investigate further.
   - Terminate the session immediately to prevent continued access to the Slack environment.
   - Reset the affected user's credentials and enforce multi-factor authentication (MFA) to secure the account.
   - Review recent activity associated with the account to identify any other compromised sessions or suspicious behavior.
