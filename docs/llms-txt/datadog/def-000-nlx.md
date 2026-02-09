# Source: https://docs.datadoghq.com/security/default_rules/def-000-nlx.md

---
title: SageMaker notebook instances should not grant users root access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SageMaker notebook instances should not
  grant users root access
---

# SageMaker notebook instances should not grant users root access
 
## Description{% #description %}

This control evaluates if root access is enabled for an Amazon SageMaker notebook instance.

Following the principle of least privilege, it's a best practice to limit root access to instance resources, ensuring that permissions are not inadvertently over-provisioned.

## Remediation{% #remediation %}

In order to restrict root access to SageMaker notebook instances, refer to the article [Control root access to a SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html).
