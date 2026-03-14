# Source: https://docs.airbyte.com/integrations/sources/sendgrid-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-sendgrid/latest/icon.svg)

# Sendgrid Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.3.26](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-sendgrid)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-sendgrid)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `fbb5fbe2-16ad-4cf4-af7d-ff9d9c316c87`

<!-- -->

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

We're continuously striving to enhance the quality and reliability of our connectors at Airbyte.

As part of our commitment to delivering exceptional service, we are transitioning Source Sendgrid from the Python Connector Development Kit (CDK) to our new low-code framework improving maintainability and reliability of the connector. Due to differences between the Python and low-code CDKs, this migration constitutes a breaking change.

* The configuration options have been renamed to `api_key` and `start_date`.
* The `unsubscribe_groups` stream has been removed as it was a duplicate of `suppression_groups`. You can use `suppression_groups` and get the same data you were previously receiving in `unsubscribe_groups`.
* The `single_sends` stream has been renamed to `singlesend_stats`. This was done to more closely match the data from the Sendgrid API.
* The `segments` stream has been upgraded to use the Sendgrid 2.0 API as the previous version of the API has been deprecated. As a result, fields within the stream have changed to reflect the new API.

To ensure a smooth upgrade, please clear your streams and trigger a sync to bring in historical data.

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
