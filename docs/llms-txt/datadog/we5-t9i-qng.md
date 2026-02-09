# Source: https://docs.datadoghq.com/security/default_rules/we5-t9i-qng.md

---
title: AWS GuardDuty finding
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS GuardDuty finding
---

# AWS GuardDuty finding
 
## Goal{% #goal %}

Detect when an [AWS GuardDuty finding](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html) has been raised.

## Strategy{% #strategy %}

AWS GuardDuty is a native threat detection service that monitors:

- CloudTrail management events
- AWS CloudTrail data events for Amazon S3
- DNS logs
- Kubernetes audit logs
- Amazon VPC flow logs
- RDS login activity monitoring

It also analyzes Amazon EBS volume data for Malware Protection in Amazon GuardDuty. With these data sources, GuardDuty generates security findings for your account.

## Triage and response{% #triage-and-response %}

1. Investigate the GuardDuty finding to determine if it is malicious or benign.
1. If the finding is deemed malicious, follow the [remediation guidance](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_remediate.html) provided by Amazon along with any internal incident response processes.
1. Otherwise findings can be managed to reduce false positives through:
   - [Suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rule.html)
   - [Trusted IP lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html)

## Changelog{% #changelog %}

- 7 September 2023 - Updated group by value for EC2 query.
- 28 November 2023 - Added query for Runtime findings.
- 19 December 2023 - Added query for Runtime findings from ECS clusters.
- 9 December 2024 - Added query for Attack sequence findings and critical severity.
