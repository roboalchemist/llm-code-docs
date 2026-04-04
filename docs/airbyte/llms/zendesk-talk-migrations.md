# Source: https://docs.airbyte.com/integrations/sources/zendesk-talk-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-zendesk-talk/latest/icon.svg)

# Zendesk Talk Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [2.0.6](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zendesk-talk)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zendesk-talk)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `c8630570-086d-4a40-99ae-ea5b18673071`

<!-- -->

## Upgrading to 2.0.0[​](#upgrading-to-200 "Direct link to Upgrading to 2.0.0")

This version adds OAuth2.0 with refresh token support. Users who authenticate via OAuth must re-authenticate to use the new flow with rotating refresh tokens.

### What changed[​](#what-changed "Direct link to What changed")

The OAuth authentication flow has been updated to support Zendesk's new grant-type tokens with rotating refresh tokens. The legacy OAuth2.0 option has been renamed to "OAuth2.0 (Legacy)" and a new "OAuth2.0" option with refresh token support has been added.

### Migration steps[​](#migration-steps "Direct link to Migration steps")

1. Go to your Zendesk Talk connection settings in Airbyte
2. If you are using OAuth authentication, you will need to re-authenticate
3. Select "OAuth2.0" as the authentication method
4. Complete the OAuth flow to authorize the connector

### Connector upgrade guide[​](#connector-upgrade-guide "Direct link to Connector upgrade guide")

Review the following information to prepare for and execute your upgrade.

### Review the changelog[​](#review-the-changelog "Direct link to Review the changelog")

Before updating a connector, review the changelog to understand the changes and their potential impact on your existing connections. Find the changelog for any connector by navigating to the bottom of the documentation for that connector. Major version releases also include a migration guide.

### Plan for major updates[​](#plan-for-major-updates "Direct link to Plan for major updates")

Major updates may require you to adjust connection settings or even make changes to your data pipelines. Allocate enough time and resources for this. Use the migration guide to ensure your transition process goes smoothly.

Airbyte provides tooling that guarantees safe connector version bumps and enforces automated version bumps for minor and patch updates. You always need to manually update for major version bumps.

### Self-managed plans: pin a specific version if you can't update[​](#self-managed-plans-pin-a-specific-version-if-you-cant-update "Direct link to Self-managed plans: pin a specific version if you can't update")

If you're unable to upgrade to the new version of a connector, you can pin that connector to a specific version.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Edit the entry for the connector you want to pin.

3. Set the **Default Version** to the version you want to use.

### Self-managed plans: update the local connector image[​](#self-managed-plans-update-the-local-connector-image "Direct link to Self-managed plans: update the local connector image")

If you self-manage Airbyte, you must manually update the connector image in your local registry before proceeding with the migration. Follow the steps below.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Find the connector you want to update in the list of connectors.

   note

   Airbyte lists two versions, the current in-use version and the latest version available.

3. Click **Change** to update your OSS version to the latest available version.

### Update the connector version[​](#update-the-connector-version "Direct link to Update the connector version")

Update each instance of the connector separately. If you have multiple instances of a connector, updating one doesn't affect the others.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Select the instance of the connector you wish to upgrade.

3. Select **Upgrade**.

4. Follow the prompt to confirm you are ready to upgrade to the new version.

### Clear data from affected streams[​](#clear-data-from-affected-streams "Direct link to Clear data from affected streams")

After upgrading a connector with a breaking change, you must refresh affected schemas and clear your data.

1. In the nav bar, click **Connections**.

2. Find the connection affected by the upgrade.

3. Click the **Schema** tab.

4. Click **Refresh source schema** (looks like ). When Airbyte finishes, it shows you any detected schema changes.

5. Click **OK**.

6. Click **Save changes**

7. [Clear the data](/platform/operator-guides/clear.md) for the streams affected by this upgrade.

Once the clear is complete, you can begin syncing your data again as usual.

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

We're continuously striving to enhance the quality and reliability of our connectors at Airbyte. As part of our commitment to delivering exceptional service, we are transitioning source zendesk-talk from the Python Connector Development Kit (CDK) to our innovative low-code framework. This is part of a strategic move to streamline many processes across connectors, bolstering maintainability and freeing us to focus more of our efforts on improving the performance and features of our evolving platform and growing catalog. However, due to differences between the Python and low-code CDKs, this migration constitutes a breaking change.

We’ve evolved and standardized how state is managed for incremental streams that are nested within a parent stream. This change impacts how individual states are tracked and stored for each partition, using a more structured approach to ensure the most granular and flexible state management. This change will affect the `calls` and `call_legs` streams.

To gracefully handle these changes for your existing connections, we highly recommend resetting your data before resuming your data syncs with the new version.

## Connector upgrade guide[​](#connector-upgrade-guide-1 "Direct link to Connector upgrade guide")

Review the following information to prepare for and execute your upgrade.

### Review the changelog[​](#review-the-changelog "Direct link to Review the changelog")

Before updating a connector, review the changelog to understand the changes and their potential impact on your existing connections. Find the changelog for any connector by navigating to the bottom of the documentation for that connector. Major version releases also include a migration guide.

### Plan for major updates[​](#plan-for-major-updates "Direct link to Plan for major updates")

Major updates may require you to adjust connection settings or even make changes to your data pipelines. Allocate enough time and resources for this. Use the migration guide to ensure your transition process goes smoothly.

Airbyte provides tooling that guarantees safe connector version bumps and enforces automated version bumps for minor and patch updates. You always need to manually update for major version bumps.

### Self-managed plans: pin a specific version if you can't update[​](#self-managed-plans-pin-a-specific-version-if-you-cant-update "Direct link to Self-managed plans: pin a specific version if you can't update")

If you're unable to upgrade to the new version of a connector, you can pin that connector to a specific version.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Edit the entry for the connector you want to pin.

3. Set the **Default Version** to the version you want to use.

### Self-managed plans: update the local connector image[​](#self-managed-plans-update-the-local-connector-image "Direct link to Self-managed plans: update the local connector image")

If you self-manage Airbyte, you must manually update the connector image in your local registry before proceeding with the migration. Follow the steps below.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Find the connector you want to update in the list of connectors.

   note

   Airbyte lists two versions, the current in-use version and the latest version available.

3. Click **Change** to update your OSS version to the latest available version.

### Update the connector version[​](#update-the-connector-version "Direct link to Update the connector version")

Update each instance of the connector separately. If you have multiple instances of a connector, updating one doesn't affect the others.

1. In the navigation bar:

   * If you're on the Self-Managed Enterprise plan, click **Organization settings** > **Sources**/**Destinations**.

   * If you're on any other plan, click **Workspace settings** > **Sources**/**Destinations**.

2. Select the instance of the connector you wish to upgrade.

3. Select **Upgrade**.

4. Follow the prompt to confirm you are ready to upgrade to the new version.

### Clear data from affected streams[​](#clear-data-from-affected-streams "Direct link to Clear data from affected streams")

After upgrading a connector with a breaking change, you must refresh affected schemas and clear your data.

1. In the nav bar, click **Connections**.

2. Find the connection affected by the upgrade.

3. Click the **Schema** tab.

4. Click **Refresh source schema** (looks like ). When Airbyte finishes, it shows you any detected schema changes.

5. Click **OK**.

6. Click **Save changes**

7. [Clear the data](/platform/operator-guides/clear.md) for the streams affected by this upgrade.

Once the clear is complete, you can begin syncing your data again as usual.
