# Source: https://docs.datadoghq.com/security/default_rules/ee2-dc1-3c1.md

---
title: AWS EBS default encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS EBS default encryption disabled
---

# AWS EBS default encryption disabled
Classification:complianceTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)Framework:cis-awsControl:2.2.1 
## Goal{% #goal %}

Detect when an EBS encryption is disabled by default.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when EBS encryption is disabled by default via the following API call:

- [DisableEbsEncryptionByDefault](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableEbsEncryptionByDefault.html)

## Triage and response{% #triage-and-response %}

1. Determine which user in your organization owns the API key that made this API call.
1. Contact the user and let them know that it is best practice to enable EBS encryption by default.
1. Re-enable EBS encryption by default.

For more information about Amazon EBS Encryption, check out the [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) documentation.

## Changelog{% #changelog %}

- 18 March 2022 - Rule query and severity updated.
- 16 November 2022 - Rule query updated.
