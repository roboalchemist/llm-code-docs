# Source: https://docs.datadoghq.com/security/default_rules/def-000-4re.md

---
title: Amazon Bedrock model invocations disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Bedrock model invocations
  disabled
---

# Amazon Bedrock model invocations disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detects when AWS Bedrock model invocation logging is disabled because the logging configuration was deleted.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail logs for the `DeleteModelInvocationLoggingConfiguration` event. This action removes audit logging for AWS Bedrock model invocations, eliminating visibility into which models are being used, what prompts are sent, and what responses are generated. Disabling logging is a defense evasion technique that attackers use to hide malicious activity or unauthorized use of AI models after gaining access to an AWS environment.

## Triage & Response{% #triage--response %}

- Verify if `{{@userIdentity.arn}}` has a legitimate business reason to disable Bedrock model invocation logging in the AWS account.
- Review recent Bedrock API activity from the same identity to identify any suspicious model usage patterns before logging was disabled.
- Examine CloudTrail logs for other defense evasion activities from the same identity, such as deleting CloudTrail trails or disabling GuardDuty.
- Check if there are any recent credential compromise indicators for the identity that performed this action.
- Re-enable model invocation logging configuration to restore audit visibility for AWS Bedrock operations.
