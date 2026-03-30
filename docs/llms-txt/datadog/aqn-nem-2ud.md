# Source: https://docs.datadoghq.com/security/default_rules/aqn-nem-2ud.md

---
title: AWS Route 53 DNS query logging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS Route 53 DNS query logging disabled
---

# AWS Route 53 DNS query logging disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user deletes a Route 53 query logging configuration.

## Strategy{% #strategy %}

Monitor cloudtrail logs where `@evt.name` is `DeleteResolverQueryLogConfig` which would stop Route53 Query logging for all of the Amazon VPCs that are associated with the configuration.

## Triage and response{% #triage-and-response %}

1. Determine if {{@userIdentity.arn}} is expected to perform the {{@evt.name}} API call.
1. Contact the principal owner and see if this was an API call that was made by the user.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.

## Changelog{% #changelog %}

- 7 April 2022 - Updated rule query and signal message.
- 5 January 2023 - Updated severity.
