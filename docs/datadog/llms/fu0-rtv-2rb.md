# Source: https://docs.datadoghq.com/security/default_rules/fu0-rtv-2rb.md

---
title: RDS databases should not be publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS databases should not be publicly
  accessible
---

# RDS databases should not be publicly accessible

## Description{% #description %}

It is important to ensure that RDS database instances provisioned in your AWS account restrict unauthorized access to minimize security risks. Publicly accessible RDS instances can expose your database to anyone on the internet, increasing the risk of malicious activities such as brute force attacks, SQL injections, or DoS/DDoS attacks. Disabling the Publicly Accessible flag and updating VPC security group settings prevents public access to these instances and protects sensitive data.

## Remediation{% #remediation %}

For instructions on securing RDS instances by disabling public access, refer to [Working with RDS Instances in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html).
