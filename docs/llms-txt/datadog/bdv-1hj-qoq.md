# Source: https://docs.datadoghq.com/security/default_rules/bdv-1hj-qoq.md

---
title: New Public Repository Container Image detected in AWS ECR
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > New Public Repository Container Image
  detected in AWS ECR
---

# New Public Repository Container Image detected in AWS ECR
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1525-implant-internal-image](https://attack.mitre.org/techniques/T1525) 
## Goal{% #goal %}

Detect when a new image is uploaded to the public ECR. This could be a potential exfil route of data from the cloud. Could be a supply chain effect as well if a company hosts their containers here for consumers.

NOTE: Amazon ECR requires that users have permission to make calls to the `ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they can authenticate to a registry and push any images to an Amazon ECR repository.

## Strategy{% #strategy %}

Detect when `@evt.name:PutImage` is used against the `ecr-public.amazonaws.com` API.

## Triage & Response{% #triage--response %}

1. Check that `{{@responseElements.image.imageId.imageDigest}}` is a valid sha256 hash for the container image with a tag of `{{@responseElements.image.imageId.imageTag}}` in the `{{@responseElements.image.repositoryName}}` repository on AWS Account `{{@userIdentity.accountId}}`.
1. If the hash is not valid for that container image, determine if the container image was placed there for a malicious purpose.
