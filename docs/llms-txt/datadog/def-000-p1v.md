# Source: https://docs.datadoghq.com/security/default_rules/def-000-p1v.md

---
title: SageMaker notebook instances should not have direct internet access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SageMaker notebook instances should not
  have direct internet access
---

# SageMaker notebook instances should not have direct internet access
 
## Description{% #description %}

This control evaluates if direct internet access is disabled for a SageMaker notebook instance.

If you create a SageMaker notebook instance without setting it up in a custom VPC, it will automatically have direct internet access enabled. To prevent this, during the instance creation process, you must choose a VPC. Once a VPC is selected, you can then disable direct internet access by selecting the **Disable** option for the Direct Internet Access setting.

To allow internet access, your VPC must be configured with either an interface endpoint (AWS PrivateLink) or a NAT gateway with a security group that permits outbound traffic.

## Remediation{% #remediation %}

Follow the [Connect a Notebook Instance in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) documentation to learn how to create an Amazon SageMaker notebook instance with a custom virtual private cloud (VPC) and the Direct Internet Access setting disabled.
