# Source: https://docs.datadoghq.com/security/default_rules/fo0-6re-l0f.md

---
title: RDS instance snapshots should not be publicly shared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instance snapshots should not be
  publicly shared
---

# RDS instance snapshots should not be publicly shared

## Description{% #description %}

Secure your Amazon Relational Database Service (RDS) database snapshots by ensuring they are not publicly accessible.

## Rationale{% #rationale %}

RDS Snapshots can be marked as [public](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Public), allowing anyone the ability to copy the snapshot to their AWS account and create database instances from it. Unless a snapshot is being shared intentionally, it should be deleted.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Stop sharing a manual DB snapshot with an AWS account](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Sharing) AWS Console docs.

### From the command line{% #from-the-command-line %}

Run `modify-db-snapshot-attribute` with the [snapshot identifier, attribute name, and values to remove](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot-attribute.html#synopsis). This removes permission from a particular AWS account to restore the DB snapshot.

```
aws rds modify-db-snapshot-attribute \
    --db-snapshot-identifier yourdbsnapshot \
    --attribute-name restore \
    --values-to-remove "all"
```
