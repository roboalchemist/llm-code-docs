# Source: https://docs.datadoghq.com/security/default_rules/def-000-an8.md

---
title: Amazon Bedrock discovery attempt by long term access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Bedrock discovery attempt by
  long term access key
---

# Amazon Bedrock discovery attempt by long term access key
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detect unauthorized attempts to discover Amazon Bedrock models and training jobs using long-term AWS access keys.

## Strategy{% #strategy %}

Monitor CloudTrail and unauthorized attempts to discover Amazon Bedrock models or training jobs.

- ListModels
- DescribeModel
- ListTrainingJobs
- DescribeTrainingJob

These attempts were explicitly denied due to lack of permissions, indicating potential unauthorized enumeration of machine learning resources. If successful, an attacker can locate data sources for self-hosted models such as an S3 bucket, then exfiltrate potentially sensitive data from these sources.

## Triage and response{% #triage-and-response %}

1. Determine if the API call (`{{@evt.name}}`) should have been made by the user (`{{@userIdentity.arn}}`) from this IP address (`{{@network.client.ip}}`).
1. If the action is legitimate, consider including the user in a suppression list. For more information, see [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise).
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.
