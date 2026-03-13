# Source: https://docs.gitguardian.com/self-hosting/installation/databases/redis-memorystore.md

# MemoryStore: Redis on GCP

> Configure Google Cloud Memorystore as the Redis backend for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a Redis instance is required. This page is
dedicated to helping you set up a Redis on GCP using MemoryStore.

## High-Availability

GCP handles failover and redirects the traffic by itself. As long as your
MemoryStore is set up to be highly available, upgrades and single-node issues
will not cause an outage.

## Installation

### From the Google Cloud Console

To create a MemoryStore from the Google Cloud Console, we recommend following
the [official documentation](https://cloud.google.com/memorystore/docs/redis/creating-managing-instances).

You need to set the following fields:

- Enable `Redis AUTH`
- Enable `in-transit encryption`
- Set `Redis Tier` to `Standard`

### Using Terraform

To create a Redis instance using TF, you need the following resources:

- [google_redis_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/redis_instance)

In addition to the fields required by Terraform, we require the following fields
to be set:

- `auth_enabled=true`: indicates whether OSS Redis AUTH is enabled for the
  instance. If set to "true" AUTH is enabled on the instance. The default value
  is "false" meaning AUTH is disabled.
- `auth_string=<SECRET_AUTH_TOKEN>`: AUTH String set on the instance. This
  field will only be populated if auth_enabled is true.
- `tier="STANDARD_HA"`: the service tier of the instance. Must be one of these values:
- `transit_encryption_mode="SERVER_AUTHENTICATION"`: the TLS mode of the Redis instance, If not provided, TLS is disabled for the instance.
