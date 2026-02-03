# Source: https://docs.datadoghq.com/security/default_rules/def-000-0xs.md

---
title: EBS volume snapshot should not be shared with external accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EBS volume snapshot should not be
  shared with external accounts
---

# EBS volume snapshot should not be shared with external accounts
 
## Description{% #description %}

This rule evaluates whether Amazon Elastic Block Store (Amazon EBS) volume snapshots are shared with external AWS accounts that are not onboarded to Datadog. EBS snapshots contain point-in-time copies of your volumes and may include sensitive data. Sharing snapshots with unauthorized external accounts can lead to data exposure and security risks.

The data contained in the `create_volume_permissions` field is enumerated and the following types of principals are assessed:

- `user_id` - designates an AWS account

The control fails if any AWS account present in `create_volume_permissions` is not onboarded to Datadog.

**Note**: If the snapshot is shared with a trusted third-party AWS account that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

To remove external account sharing permissions from Amazon EBS snapshots, follow the steps outlined in the [Sharing an Amazon EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html) section of the Amazon EC2 User Guide. For guidance regarding onboarding AWS accounts to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
