# Source: https://docs.datadoghq.com/security/default_rules/moi-gio-c9a.md

---
title: Unfamiliar process accessed AWS EKS service account token
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unfamiliar process accessed AWS EKS
  service account token
---

# Unfamiliar process accessed AWS EKS service account token
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` accessed the EKS service account token which could be an attempt to steal credentials.

## Goal{% #goal %}

Detects when the AWS EKS service account token has been viewed by a user.

## Strategy{% #strategy %}

AWS provides an authentication mechanism called [IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to allow Kubernetes workloads such as pods to securely authenticate to AWS without hardcoding credentials.

The authentication token made available by AWS is located at `/var/run/secrets/eks.amazonaws.com/serviceaccount/token` and can be exchanged for AWS credentials using `sts:AssumeRoleWithWebIdentity`. It is consequently an attractive target for attackers.

This rule uses the New Value detection method. Datadog will learn the historical behavior of a specified field in Agent logs and then create a signal when unfamiliar values appear.

## Triage and response{% #triage-and-response %}

1. Determine which user executed the command to read the token and determine if that access is authorized.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack), and look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and network tools involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path and signals from other tools. For example, if a DNS exfiltration attack is suspected, examine DNS traffic and servers if available.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
