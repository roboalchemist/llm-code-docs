# Source: https://docs.datadoghq.com/security/default_rules/kq2-xck-hec.md

---
title: New Private Repository Container Image detected in AWS ECR
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > New Private Repository Container Image
  detected in AWS ECR
---

# New Private Repository Container Image detected in AWS ECR
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1525-implant-internal-image](https://attack.mitre.org/techniques/T1525)
## Goal{% #goal %}

Detect potential persistence mechanisms being deployed in the AWS Elastic Container Registry (ECR).

NOTE: Amazon ECR requires that users have permission to make calls to the `ecr:GetAuthorizationToken` API through an IAM policy before they can authenticate to a registry and push or pull any images from any Amazon ECR repository.

## Strategy{% #strategy %}

Detect when `@evt.name:PutImage` is used against the `ecr.amazonaws.com` API.

## Triage & Response{% #triage--response %}

1. Check that `{{@responseElements.image.imageId.imageDigest}}` is a valid sha256 hash for the container image with a tag of `{{@responseElements.image.imageId.imageTag}}` in the `{{@responseElements.image.repositoryName}}` repository on AWS Account `{{@userIdentity.accountId}}`.
1. If the hash is not valid for that container image, determine if the container image was placed there for a malicious purpose.
