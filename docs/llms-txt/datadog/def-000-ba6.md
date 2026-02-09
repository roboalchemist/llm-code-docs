# Source: https://docs.datadoghq.com/security/default_rules/def-000-ba6.md

---
title: Instance roles should be used for AWS resource access from instances
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Instance roles should be used for AWS
  resource access from instances
---

# Instance roles should be used for AWS resource access from instances
 
## Description{% #description %}

This check ensures the EC2 instance uses IAM instance roles for granting resource access. By assigning an IAM role to your instances, you can access AWS resources securely and eliminate the need to manage credentials directly on the instances. IAM instance roles provide temporary credentials that are automatically rotated, reducing the risk of credential leakage and simplifying credential management.

## Remediation{% #remediation %}

For detailed instructions on how to assign an IAM role to an EC2 instance, refer to the [IAM Roles for Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

It is recommended to create IAM roles that have the minimum permissions required for accessing AWS resources, adhering to the principle of least privilege.
