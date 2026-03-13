# Source: https://docs.gitguardian.com/self-hosting/installation/databases/postgres-rds.md

# RDS: PostgreSQL on AWS

> Configure Amazon RDS as the PostgreSQL database for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a PostgreSQL instance is required. This page is
dedicated to helping you set up a PostgreSQL on AWS using RDS.

## High-availability

AWS handles failover by updating a DNS record. This allows zero downtime for
planned maintenance, upgrades and reboots.

## Installation

### From the AWS console

To create a PostgreSQL from the AWS Console, we recommend following the
[official documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html).

We recommend you use the `Production` template as it contains sensible defaults
for a production-ready cluster.

You need to set the following fields:

- Ensure `Multi-AZ deployment` is set to `Create a standby instance`.
- Ensure `Database authentication options` are set to `Password authentication`.
- Set the `Master Username` to your liking or keep the default `postgres`.
- Set the `Master password` or Auto generate it. You must save this value as it
  is required to configure the GitGuardian application.

### Using Terraform

To create a PostgreSQL instance using TF, you need the following resources:

- [aws_db_instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance)

In addition to the fields required by Terraform, we require the following fields
to be set:

- `engine=postgres`: the name of the database engine to be used for this DB
  cluster.
- `username=<POSTGRES_USERNAME>`: username for the master DB user.
- `password=<POSTGRES_PASSWORD>`: password for the master DB user.

## Plugins installation (like pgvector)

To install a plugin on RDS, your user need the `rds_superuser` role. This role is granted on your [RDS default master user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.rds_superuser.html).

This role is only needed for plugin installation, the user configured in GitGuardian application does not require the role.
