# Source: https://docs.datadoghq.com/security/default_rules/def-000-ywp.md

---
title: RDS cluster snapshots should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS cluster snapshots should be
  encrypted at rest
---

# RDS cluster snapshots should be encrypted at rest

## Description{% #description %}

This control ensures snapshots are encrypted. It checks RDS, Neptune, DocDB, and Aurora snapshots. Snapshot encryption is crucial for maintaining data confidentiality and complying with security best practices.

## Remediation{% #remediation %}

To encrypt an RDS snapshot, refer to the [Encrypting Amazon RDS resources section in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html). Encryption covers the instance's underlying storage, automated backups, read replicas, and snapshots.

Although you can only enable encryption during the creation of an RDS DB instance, you can encrypt an existing instance by following these steps:

1. **Create a Snapshot:** Generate a snapshot of your current unencrypted DB instance.
1. **Create an Encrypted Copy:** Make an encrypted copy of the snapshot.
1. **Restore from Encrypted Snapshot:** Restore a DB instance from the encrypted snapshot.

By doing this, you effectively create an encrypted version of your original, unencrypted DB instance, ensuring data security and compliance.
