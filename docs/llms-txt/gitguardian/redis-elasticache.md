# Source: https://docs.gitguardian.com/self-hosting/installation/databases/redis-elasticache.md

# ElasticCache: Redis on AWS

> Configure Amazon ElastiCache as the Redis backend for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a Redis instance is required. This page is
dedicated to helping you set up a Redis on AWS using ElasticCache.

## High-Availability

AWS handles failover by updating a DNS record. This creates a small window where
the GitGuardian application will use the ReadOnly replica in case of
maintenance.

## Installation

### From the AWS Console

To create an ElasticCache from the AWS Console, we recommend reading the
[official documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/GettingStarted.CreateCluster.html).

You need to set the following fields:

- Ensure `Multi-AZ` is enabled.
- Enable `Encryption at-rest`.
- Enable `Encryption in-transit`.
- Set `Access Control Option` to `Redis AUTH Default User`.
- Set `Redis AUTH Token` to `<SECRET_AUTH_TOKEN>`. You must save this value as
  it is required to configure the GitGuardian application.

Do not enable `Cluster Mode`, this option is not supported by the GitGuardian
application.

:::info
Our Helm installation supports Redis RBAC from AWS ElastiCache as long as the RBAC user authentication is managed through a password mechanism and not via IAM.
:::

### Using Terraform

To create a Redis instance using TF, you need the following resources:

- [elasticache_replication_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/elasticache_replication_group)

In addition to the fields required by Terraform, we require the following fields
to be set:

- `transit_encryption_enabled=true`: whether to enable encryption in transit.
- `auth_token=<SECRET_AUTH_TOKEN>`: the password used to access a password-protected server.
- `at_rest_encryption_enabled=true`: whether to enable encryption at rest.
- `automatic_failover_enabled=true`: specifies whether a read-only replica will
  be automatically promoted to read/write primarily if the existing primary
  fails.
- `multi_az_enabled=true`: specifies whether to enable Multi-AZ Support for the
  replication group.
