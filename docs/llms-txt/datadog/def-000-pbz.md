# Source: https://docs.datadoghq.com/security/default_rules/def-000-pbz.md

---
title: Redshift Serverless snapshots should not be shared with external accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift Serverless snapshots should
  not be shared with external accounts
---

# Redshift Serverless snapshots should not be shared with external accounts
 
## Description{% #description %}

This rule evaluates whether Amazon Redshift Serverless snapshots are shared with external AWS accounts that are not onboarded to Datadog. Redshift Serverless snapshots contain complete copies of data warehouse clusters, including all data, configurations, and potentially sensitive information. Sharing snapshots with unauthorized external accounts can lead to data exposure and security risks.

The data contained in the `accounts_with_restore_access` and `accounts_with_provisioned_restore_access` fields are enumerated to identify which AWS accounts have access to restore from the snapshot.

The control fails if any account present is not onboarded to Datadog.

**Note**: If the Redshift Serverless snapshot is shared with a trusted third-party AWS account that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

To remove external account sharing permissions from Amazon Redshift Serverless snapshots, follow the steps outlined in the [Sharing a snapshot or removing snapshot permissions](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-share.html) section of the Amazon Redshift Management Guide. For guidance regarding onboarding AWS accounts to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
