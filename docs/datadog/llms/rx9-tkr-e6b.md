# Source: https://docs.datadoghq.com/security/default_rules/rx9-tkr-e6b.md

---
title: Default VPC security group should restrict all traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Default VPC security group should
  restrict all traffic
---

# Default VPC security group should restrict all traffic

## Description{% #description %}

A VPC comes with a default security group that by default denies all inbound traffic, allows all outbound traffic, and permits all traffic among instances within the group. By setting up your default security group to restrict all traffic, you encourage the development of least privilege security groups and ensure mindful placement of AWS resources. This practice reduces the exposure of your resources. As each new VPC is created, including the default VPC in every region, updating the default security group is necessary to comply with security best practices.

Configuring VPC flow logging is a valuable tool during this process as it logs packet acceptances and rejections, helping identify the minimum port access requirements for proper system operation. Even if not adopted permanently, it proves critical for engineering least privileged security groups.

## Remediation{% #remediation %}

For detailed guidance on modifying default security groups to restrict all traffic, refer to the [AWS EC2 Security Groups documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#default-security-group).
