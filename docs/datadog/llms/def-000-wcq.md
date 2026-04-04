# Source: https://docs.datadoghq.com/security/default_rules/def-000-wcq.md

---
title: Oracle Cloud user requested to create or reset password from malicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Oracle Cloud user requested to create
  or reset password from malicious IP
---

# Oracle Cloud user requested to create or reset password from malicious IP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when an API request to reset the password was made by a user.

## Strategy{% #strategy %}

Monitor Oracle cloud logs to detect the API call [CreateOrResetMyPasswordRequest](https://docs.oracle.com/cd/E80480_01/help/en/user/178588.htm). An attacker can compromise the user's email address to reset the user's password.

## Triage and response{% #triage-and-response %}

1. Determine if the request to reset the user password should have been made.
1. If not, investigate the action performed by `{{@usr.name}}` for indicators of account compromise, and rotate credentials if necessary.
