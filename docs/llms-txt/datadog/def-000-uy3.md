# Source: https://docs.datadoghq.com/security/default_rules/def-000-uy3.md

---
title: AWS consoler detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS consoler detected
---

# AWS consoler detected
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when usage of the AWS Consoler tool is seen in AWS CloudTrail logs, which could indicate that the associated AWS credentials were compromised and used to pivot to the AWS console.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail logs for the `GetFederationToken` API call with the parameter [`aws_consoler`](https://github.com/NetSPI/aws_consoler). AWS Consoler is a tool that converts long-lived AWS access keys into AWS console access, by generating a [sign-in URL](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html). While this tool can be used legitimately by your teams, it may also be used by attackers to gain access to your console.

## Triage and response{% #triage-and-response %}

1. Determine if your organization is using the AWS consoler tool.
1. If the results of the triage indicate that this tool is not used by your organization, begin your company's incident response process and an investigation.
   - If appropriate, disable or rotate the affected credential.
   - Investigate any actions taken by the identity `{{@userIdentity.arn}}`.
   - Work with the relevant teams to remove the key from any source code repositories.
