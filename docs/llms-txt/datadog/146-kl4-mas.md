# Source: https://docs.datadoghq.com/security/default_rules/146-kl4-mas.md

---
title: EBS volumes should be encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > EBS volumes should be encrypted
---

# EBS volumes should be encrypted
 
## Description{% #description %}

Enable encryption for Elastic Block Store (EBS) by default in the region. EBS uses AES-256 encryption to protect data stored on volumes, disk I/O, and snapshots, safeguarding your sensitive data from exploits and unauthorized users.

## Remediation{% #remediation %}

For detailed instructions on enabling EBS encryption by default in your region, refer to the [AWS EBS Encryption Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#ebs-encryption-requirements).
