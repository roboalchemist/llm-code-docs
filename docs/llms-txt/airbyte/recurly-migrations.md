# Source: https://docs.airbyte.com/integrations/sources/recurly-migrations.md

<!-- -->

![](https://connectors.airbyte.com/files/metadata/airbyte/source-recurly/latest/icon.svg)

# Recurly Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [1.3.43](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-recurly)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-recurly)(last updated 23 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `cd42861b-01fc-4658-a8ab-5d11d0510f01`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

We recently rolled out an update to the Recurly connector using a newer version of our CDK, as well as introducing several additions to the existing stream schemas. Our aim with these updates is always to enhance the connector's functionality and provide you with a richer set of data to support your integration needs.

While our intention was to make these updates as seamless as possible, we've observed that some users are experiencing issues during the "Discover" step of the sync process. This has led us to re-categorize the recent changes as breaking updates, despite not removing fields or altering property names within the schema.

Once you have migrated to the new version, we highly recommend all users refresh their schemas and reset their data before resuming syncs

## Connector upgrade guide[​](#connector-upgrade-guide "Direct link to Connector upgrade guide")

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
