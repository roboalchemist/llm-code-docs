# Source: https://docs.datadoghq.com/security/default_rules/def-000-hts.md

---
title: Redshift cluster snapshots should not be shared with external accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift cluster snapshots should not
  be shared with external accounts
---

# Redshift cluster snapshots should not be shared with external accounts

## Description{% #description %}

This rule evaluates whether Amazon Redshift cluster snapshots are shared with external AWS accounts that are not onboarded to Datadog. Redshift cluster snapshots contain complete copies of data warehouse clusters, including all data, configurations, and potentially sensitive information. Sharing cluster snapshots with unauthorized external accounts can lead to data exposure and security risks.

The data contained in the `accounts_with_restore_access` field is enumerated to identify which AWS accounts have access to restore from the snapshot.

The control fails if any account present is not onboarded to Datadog.

**Note**: If the Redshift cluster snapshot is shared with a trusted third-party AWS account that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

To remove external account sharing permissions from Amazon Redshift cluster snapshots, follow the steps outlined in the [Sharing a snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-share-snapshot.html) section of the Amazon Redshift Management Guide. For guidance regarding onboarding AWS accounts to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
