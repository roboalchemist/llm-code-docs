# Source: https://docs.datadoghq.com/security/default_rules/def-000-8hf.md

---
title: SageMaker notebook instances should be launched in a custom VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SageMaker notebook instances should be
  launched in a custom VPC
---

# SageMaker notebook instances should be launched in a custom VPC
 
## Description{% #description %}

This control evaluates whether an Amazon SageMaker notebook instance is launched within a custom virtual private cloud (VPC).

This configuration can be set only during the creation of a notebook instance and cannot be changed afterward. Using an Amazon VPC, you can manage the network access and internet connectivity for your SageMaker Studio and notebook instances.

## Remediation{% #remediation %}

Follow the [Connect a Notebook Instance in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html) documentation to learn how to create an Amazon SageMaker notebook instance with a custom virtual private cloud (VPC).
