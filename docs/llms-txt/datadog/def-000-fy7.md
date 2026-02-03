# Source: https://docs.datadoghq.com/security/default_rules/def-000-fy7.md

---
title: AWS ECS CreateCluster API calls in multiple regions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS ECS CreateCluster API calls in
  multiple regions
---

# AWS ECS CreateCluster API calls in multiple regions
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when there is an attempt to create AWS ECS clusters in multiple regions.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an attempt to create AWS ECS clusters in multiple regions occurs. An attacker may use ECS clusters as a means of creating easily scalable resources to mine cryptocurrency. See the following Datadog Security Labs [blog post](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-ecs-crypto-mining/) for further detail.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have carried out this operation.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Remove the newly created cluster `{{@requestParameters.clusterName}}` and any associated tasks or services.
- Determine what other API calls were made by the user.
- Begin your organization's incident response process and investigate.
