# Source: https://docs.datadoghq.com/security/default_rules/wem-cvg-42m.md

---
title: AWS Route 53 VPC disassociated from query logging configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Route 53 VPC disassociated from
  query logging configuration
---

# AWS Route 53 VPC disassociated from query logging configuration
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user disassociates a VPC from the query logging configuration.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if a user has disassociated.

- [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html)

## Triage and response{% #triage-and-response %}

1. Determine if {{@userIdentity.arn}} is expected to perform the {{@evt.name}} API call.
1. Contact the principal owner and see if this was an API call that was made by the user.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.

## Changelog{% #changelog %}

- 7 April 2022 - Update rule and signal message.
- 15 December 2022 - Update query to include Access Denied events and reduce severity.
