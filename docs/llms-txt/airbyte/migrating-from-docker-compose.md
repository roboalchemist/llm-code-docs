# Source: https://docs.airbyte.com/platform/deploying-airbyte/migrating-from-docker-compose.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/migrating-from-docker-compose.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/migrating-from-docker-compose.md

# Source: https://docs.airbyte.com/platform/1.7/deploying-airbyte/migrating-from-docker-compose.md

# Source: https://docs.airbyte.com/platform/1.6/deploying-airbyte/migrating-from-docker-compose.md

# Migrating from Docker Compose

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

warning

Migration from Docker Compose is no longer supported. The `--migrate` flag has been deprecated and removed from `abctl`.

If you were previously running Airbyte using Docker Compose, we recommend performing a fresh deployment of Airbyte. Docker Compose deployments are no longer supported.

To get started with a fresh installation, see the [Quickstart guide](/platform/1.6/using-airbyte/getting-started/oss-quickstart.md) or the [Deploy Airbyte](/platform/1.6/deploying-airbyte/.md) section for more deployment options.

If you need to preserve your existing connection configurations, you can manually recreate them in your new Airbyte instance. Historical sync data from your Docker Compose deployment cannot be migrated to the new installation.

For users with an external database, you can configure your new installation to use the same database. See the [database integration documentation](/platform/1.6/deploying-airbyte/integrations/database.md) for setup instructions.
