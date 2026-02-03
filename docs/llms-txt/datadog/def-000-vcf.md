# Source: https://docs.datadoghq.com/security/default_rules/def-000-vcf.md

---
title: Publicly Accessible RDS instance uses a common master database username
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly Accessible RDS instance uses a
  common master database username
---

# Publicly Accessible RDS instance uses a common master database username

## Description{% #description %}

A publicly accessible database that uses a common master database username increases the likelihood of brute force attack successfully granting access, as these usernames are well-known and frequently targeted by attackers. The master database username is the default username created when the database is provisioned and typically grants full access to the database, which can be used by an attacker for unauthorized data access or destruction of sensitive information.

## Remediation{% #remediation %}

1. Modify the database instance to disable public accessibility. Review [Hiding a DB instance in a VPC from the internet](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.HidingInstance) for more information on how to disable public accessibility.

Note: You cannot change the master username without creating a new RDS instance. If you need to change the master username, create a new RDS instance and migrate the data to the new instance.
