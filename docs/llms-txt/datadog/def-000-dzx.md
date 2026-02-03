# Source: https://docs.datadoghq.com/security/default_rules/def-000-dzx.md

---
title: AWS principal added to multiple EKS clusters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS principal added to multiple EKS
  clusters
---

# AWS principal added to multiple EKS clusters
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when an AWS principal is assigned permissions on multiple Amazon EKS clusters in a short amount of time. This can be indicative of an attacker compromising your AWS environment and laterally moving to your EKS clusters.

## Strategy{% #strategy %}

This rule leverages CloudTrail and triggers if `CreateAccessEntry` or `AssociateAccessPolicy` events are triggered for the same AWS principal on more than 5 unique EKS clusters.

To learn more about EKS Cluster Access Management, see this guide on Datadog Security Labs: [Deep dive into the new Amazon EKS Cluster Access Management features](https://securitylabs.datadoghq.com/articles/eks-cluster-access-management-deep-dive/).

## Triage and response{% #triage-and-response %}

1. Determine if `@requestParameters.principalArn` (the grantee) should be granted permissions on the target EKS clusters.
1. Determine if `{{@userIdentity.session_name}}` (the grantor) should have granted permissions on the target EKS clusters.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Revert the permissions change by removing the access entry.
If the API calls were made by the user:
- Determine if the user should be granting access to the cluster.
- If not, see if other API calls were made by the user and determine if they warrant further investigation.
