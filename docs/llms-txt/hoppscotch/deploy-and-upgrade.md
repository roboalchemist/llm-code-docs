# Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/deploy-and-upgrade.md

# Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/deploy-and-upgrade.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.hoppscotch.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy and upgrade

> Deploy and upgrade Hoppscotch Community Edition on your infrastructure.

This section contains instructions for deploying and upgrading Hoppscotch Community Edition.

## Deploy

Deploy Hoppscotch Community Edition on your infrastructure.

<Info>Instructions for deploying Hoppscotch on your infrastructure are coming soon.</Info>

## Upgrade

Upgrading Hoppscotch Community Edition is a simple process. Follow the instructions below to upgrade your Hoppscotch Community Edition instance.

### Using individual containers for the services

1. Check if there is a new version available by running the following command:

   ```bash  theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash  theme={null}
   docker pull hoppscotch/hoppscotch-frontend:latest
   docker pull hoppscotch/hoppscotch-backend:latest
   docker pull hoppscotch/hoppscotch-admin:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash  theme={null}
   docker pull hoppscotch/hoppscotch-frontend:<version>
   docker pull hoppscotch/hoppscotch-backend:<version>
   docker pull hoppscotch/hoppscotch-admin:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/community-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/community-edition/install-and-build#migrations) section for more information.</Info>

### Using the AIO container

1. Check if there is a new version available by running the following command:

   ```bash  theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash  theme={null}
   docker pull hoppscotch/hoppscotch:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash  theme={null}
   docker pull hoppscotch/hoppscotch:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/community-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/community-edition/install-and-build#migrations) section for more information.</Info>


Built with [Mintlify](https://mintlify.com).