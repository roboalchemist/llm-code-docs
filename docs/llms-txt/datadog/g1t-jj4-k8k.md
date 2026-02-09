# Source: https://docs.datadoghq.com/security/default_rules/g1t-jj4-k8k.md

---
title: EBS volume snapshot should not be publicly shared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EBS volume snapshot should not be
  publicly shared
---

# EBS volume snapshot should not be publicly shared
 
## Description{% #description %}

Secure Amazon Elastic Block Store (EBS) snapshots.

## Rationale{% #rationale %}

Publicly shared Amazon EBS volume snapshots contain sensitive application data that can be seen, copied, and exploited.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [AWS Share a snapshot documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-unencrypted-snapshot) to learn how to modify snapshot sharing for both the console and the command line.

### From the command line{% #from-the-command-line %}

1. Enter the following command with your snapshot ID to remove global sharing.

   ```
    aws ec2 modify-snapshot-attribute \
       --snapshot-id 1234567890abcdef0 \
       --attribute createVolumePermission \
       --operation-type remove \
       --group-names all
   ```

1. Run the follow command with your snapshot ID to share a snapshot with a specific user ID.

   ```
    aws ec2 modify-snapshot-attribute \
        --snapshot-id 1234567890abcdef0 \ 
        --attribute createVolumePermission \
        --operation-type add \
        --user-ids 123456789012
   ```
