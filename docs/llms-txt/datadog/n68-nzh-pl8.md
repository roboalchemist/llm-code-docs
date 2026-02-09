# Source: https://docs.datadoghq.com/security/default_rules/n68-nzh-pl8.md

---
title: EBS snapshot should be encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > EBS snapshot should be encrypted
---

# EBS snapshot should be encrypted
 
## Description{% #description %}

Encrypt Amazon Elastic Block Store (EBS) snapshots with volume snapshot encryption keys.

## Rationale{% #rationale %}

Amazon EBS snapshots contain sensitive data, and publicly accessible snapshots can be copied. Keep your data secure from exploits or unauthorized users by using AWS key management.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Default key for EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_key_mgmt) docs to learn how to encrypt a snapshot in the AWS Console.

### From the command line{% #from-the-command-line %}

1. Run `get-ebs-default-kms-key-id` to describe [the default CMK](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ebs-default-kms-key-id.html).

1. If you need to create a new key, follow the [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) AWS Console docs or the [create-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html) AWS CLI docs.

1. Run `modify-ebs-default-kms-key-id` with your `--kms-key-id` to [modify the default CMK used to encrypt EBS volumes](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html).

See the [Set encryption defaults using the API and CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default-api) docs for additional information.
