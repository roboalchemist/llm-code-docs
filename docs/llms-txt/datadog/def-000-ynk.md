# Source: https://docs.datadoghq.com/security/default_rules/def-000-ynk.md

---
title: Amazon Bedrock activity InvokeModel multiple regions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Bedrock activity InvokeModel
  multiple regions
---

# Amazon Bedrock activity InvokeModel multiple regions
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detect when there is an attempt to use InvokeModel in multiple regions.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when there is an attempt to use the API call [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) in multiple regions from a long-term access key. Attackers target the AWS Bedrock service generally for the purpose of hosting their own LLM service using the victim's resources.

## Triage and response{% #triage-and-response %}

1. Determine if the API call (`{{@evt.name}}`) should have been made by the user (`{{@userIdentity.arn}}`) from this IP address (`{{@network.client.ip}}`).
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.

## Changelog{% #changelog %}

- 11 Dec 2024 - Add case for temporary credentials.
- 6 October 2025 - Search for Bedrock-specific long term access keys
