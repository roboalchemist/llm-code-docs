# Source: https://docs.datadoghq.com/security/default_rules/def-000-8nn.md

---
title: RDS cluster snapshots should not be publicly shared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS cluster snapshots should not be
  publicly shared
---

# RDS cluster snapshots should not be publicly shared

## Description{% #description %}

Ensures that your Amazon RDS cluster snapshots are **not publicly accessible** to protect sensitive data from unauthorized access.

## Rationale{% #rationale %}

Public RDS snapshots can be [accessed](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Public) and restored by **any AWS account** worldwide. This could expose confidential database contents, leading to data breaches or regulatory violations. Snapshots should never be publicly shared unless explicitly required and controlled.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the instructions in the [Stop sharing a manual DB snapshot with an AWS account](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Sharing) AWS Console docs.

### From the command line{% #from-the-command-line %}

Run `modify-db-cluster-snapshot-attribute` with the [cluster snapshot identifier, attribute name, and values to remove](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-snapshot-attribute.html#synopsis) to revoke a specific AWS account's permission to restore the DB snapshot.

```
aws rds modify-db-cluster-snapshot-attribute \
    --db-cluster-snapshot-identifier yourdbsnapshot \
    --attribute-name restore \
    --values-to-remove "all"
```
