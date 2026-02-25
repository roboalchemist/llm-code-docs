# Source: https://docs.datadoghq.com/security/default_rules/def-000-cm5.md

---
title: AWS principal assigned administrative privileges in an EKS cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS principal assigned administrative
  privileges in an EKS cluster
---

# AWS principal assigned administrative privileges in an EKS cluster
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an AWS principal is assigned administrative permissions on an Amazon EKS cluster.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if someone grants administrative permissions to an EKS cluster, through the following events:

- `CreateAccessEntry`
- `UpdateAccessEntry`
- `AssociateAccessPolicy`

It triggers when an AWS principal is assigned the managed access policy, `AmazonEKSAdminPolicy` or `AmazonEKSClusterAdminPolicy`, or if the access entry corresponding to the principal is assigned the built-in `cluster-admin` Kubernetes group.

To learn more about EKS Cluster Access Management, see this guide on Datadog Security Labs: [Deep dive into the new Amazon EKS Cluster Access Management features](https://securitylabs.datadoghq.com/articles/eks-cluster-access-management-deep-dive/).

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have granted permissions on the EKS cluster.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Revert the permissions change by removing the access entry.
If the API calls were made by the user:
- Determine if the user should be granting access to the cluster.
- If not, see if other API calls were made by the user and determine if they warrant further investigation.
