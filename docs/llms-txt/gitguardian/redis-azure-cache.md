# Source: https://docs.gitguardian.com/self-hosting/installation/databases/redis-azure-cache.md

# Azure Cache: Redis on Azure

> Configure Azure Cache for Redis as the Redis backend for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a Redis instance is required. This page is
dedicated to helping you set up Redis on Azure using Azure Cache for Redis.

:::warning Redis Compatibility
**Azure Managed Redis** is not supported by GitGuardian. Please use **Azure Cache for Redis** instead.
:::

## High-Availability

Azure Cache for Redis provides high availability through its Premium and Standard tiers, which offer replication and automatic failover. During failover or maintenance, there may be a brief window where the GitGuardian application may experience read-only access or a short downtime.

## Installation

### From the Azure Portal

To create an Azure Cache for Redis instance from the Azure Portal, we recommend reading the
[official documentation](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-create-redis-resource).

You need to set the following fields:

- Choose the **Premium** or **Standard** tier for high availability.
- Enable **Geo-replication** if cross-region redundancy is required.
- Enable **SSL** to ensure encryption in transit.
- Enable **Data persistence** if you require data recovery after failures (Premium tier only).
- Set the **Access keys** (primary/secondary) as the Redis AUTH password. You must save this value as
  it is required to configure the GitGuardian application.

:::info
Our Helm installation supports Redis authentication from Azure Cache for Redis as long as the authentication is managed through a password mechanism and not via Azure Active Directory (AAD).
:::

### Using Terraform

To create a Redis instance using Terraform, you need the following resources:

- [azurerm_redis_cache](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/redis_cache)

In addition to the fields required by Terraform, we require the following fields
to be set:

- `enable_non_ssl_port = false`: ensures only encrypted connections are allowed.
- `minimum_tls_version = "1.2"`: enforces a secure TLS version.
- `sku_name = "Premium"` or `"Standard"`: for high availability and replication.
- `redis_configuration = { "maxmemory-policy" = "allkeys-lru" }`: recommended memory policy.
- `redis_version = "6"` : Redis 6 is currently the latest available Redis version on Azure Cache.
- Use the **primary_access_key** as the password for the GitGuardian application.
- Enable **replicas_per_master** for additional redundancy (Premium tier).
