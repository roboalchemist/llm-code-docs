# Source: https://docs.datadoghq.com/security/default_rules/def-000-cry.md

---
title: RDS instance snapshots should not be shared with external accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instance snapshots should not be
  shared with external accounts
---

# RDS instance snapshots should not be shared with external accounts

## Description{% #description %}

This rule evaluates whether Amazon RDS instance snapshots are shared with external AWS accounts that are not onboarded to Datadog. RDS instance snapshots contain complete copies of database instances, including all data, configurations, and potentially sensitive information. Sharing instance snapshots with unauthorized external accounts can lead to data exposure and security risks.

The data contained in the `db_snapshot_attributes` field is enumerated to identify which AWS accounts have access to restore from the snapshot.

The control fails if any account present is not onboarded to Datadog.

**Note**: If the RDS instance snapshot is shared with a trusted third-party AWS account that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

To remove external account sharing permissions from Amazon RDS instance snapshots, follow the steps outlined in the [Sharing a DB snapshot for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html) section of the Amazon RDS User Guide. For guidance regarding onboarding AWS accounts to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
