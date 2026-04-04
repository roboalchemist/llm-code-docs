# Source: https://docs.snowflake.com/en/developer-guide/native-apps/update-app.md

# Update an app (Legacy)

The Snowflake Native App Framework enables providers to update a Snowflake Native App to add new functionality,
fix bugs, and make other changes. Providers can create new versions or patches of
and app and upgrade the app in the consumer account.

## Workflow for updating an app

1. Understand the version and upgrade process for an app.

   Before developing a new version or patch of an app, providers should understand the version
   lifecycle for an app and how the upgrade process works. See [Overview of app versions and upgrades (Legacy)](update-app-overview.md) for
   information.
2. Develop and test the updated app local.

   Providers develop and test new versions or patches locally before publishing them to consumers. See
   [Develop a new version of an app (Legacy)](update-app-develop.md) for guidelines on how to develop a new version or patch. See [Use versioned schema to manage app objects across versions](versioned-schema.md)
   for information on how to handle objects during the upgrade.
3. Add the version or patch to the application package.

   After developing and testing a new version or patch locally, providers create a new version or patch
   for the app. Version and patch information are stored in the application package. See [Create versions and patches for an app (Legacy)](update-app-versions.md) for
   information on creating versions and patches.

   > **Note:**
   >
   > If an application package already has two versions for an app defined in the
   > application package, providers must drop one of the versions before adding a new version.
4. Wait for the results of the automated security scan.

   If the DISTRIBUTION property of the application package is set to EXTERNAL, creating a new version
   or patch initiates the automated security scan. The app must pass the security scan before it can be
   published to the Snowflake Marketplace.

   For information on setting the DISTRIBUTION property and the automated security scan, see
   [Run the automated security scan](security-run-scan.md).
5. Upgrade the app.

   Upgrades are initiated when the provider updates the
   [release directive](update-app-release-directive.md) of the application package.

   This initiates the upgrade process for all installed apps that are on the previous
   version. However, a provider can ask a consumer to perform a manual upgrade
   if the consumer needs to upgrade their app before the automated upgrade is complete.
6. Monitor the upgrade.

   After the upgrade begins, providers can monitor the upgrade in their account by querying the
   [APPLICATION_STATE view](../../sql-reference/data-sharing-usage/application-state-view.md).

   See [Monitor the state of an upgrade](update-app-upgrade.md) for information on monitoring an app upgrade and the
   possible upgrade statuses.
7. Update the listing for the app.

   After an app passes the security scan and the provider sets the release directive,
   Snowflake automatically updates the version and patch for the listing. However, providers
   may still need to update the listing to describe new functionality to the consumer.

   For more information, see [Modify published listings](../../collaboration/provider-listings-modifying.md).
