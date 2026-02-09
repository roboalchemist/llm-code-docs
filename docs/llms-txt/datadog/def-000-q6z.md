# Source: https://docs.datadoghq.com/security/default_rules/def-000-q6z.md

---
title: ECR private repositories should have tag immutability enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECR private repositories should have
  tag immutability enabled
---

# ECR private repositories should have tag immutability enabled
 
## Description{% #description %}

This control verifies whether tag immutability is enabled on a private ECR repository. It passes when tag immutability is enabled and set to `IMMUTABLE`.

Amazon ECR Tag Immutability enables users to rely on descriptive tags as a consistent method for tracking and uniquely identifying images. An immutable tag is fixed, meaning each tag points to a unique image. This enhances reliability and scalability because a static tag will always reference the same image upon deployment. When enabled, tag immutability prevents tags from being overwritten, thereby reducing potential security risks.

## Remediation{% #remediation %}

For guidance on how to set up a repository with immutable tags or modify the image tag mutability settings for an existing repository, refer to the [Image Tag Mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html) section in the Amazon Elastic Container Registry User Guide.
