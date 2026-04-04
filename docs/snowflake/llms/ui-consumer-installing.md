# Source: https://docs.snowflake.com/en/developer-guide/native-apps/ui-consumer-installing.md

# Install an app from a listing

This topic describes how to use [Snowsight](../../user-guide/ui-snowsight-gs.md) to install apps created using the Snowflake Native App Framework.

## Workflow for installing an app from a listing

To find and install a listing for an app:

1. Set up the privileges required to install a listing.
2. Install the app from the listing.

   * If you are installing a privately shared listing, see Install an app from a privately shared listing
   * If you are installing a listing shared on the Snowflake Marketplace, see
     [Working with Snowflake Marketplace listings for an app](ui-consumer-installing-container.md).
   * If a provider has published multiple version of an app, see Install an app using release channels.
3. [View the installed listing](ui-consumer-managing-applications.md).

   See [Allow access to a consumer account](ui-consumer-granting-privs.md) for information on tasks related to managing an app.
   See [Set up event tracing for an app](ui-consumer-enable-logging.md) for information on setting up event sharing.

## Set up required privileges

To access a listing, you must use the ACCOUNTADMIN role or another role with the IMPORT SHARE and
CREATE DATABASE privileges.

After an app is installed, the app owner can grant access to the app
using application roles. See [Grant application roles to account roles](ui-consumer-managing-applications.md) for details.

> **Note:**
>
> To pay for an app, your role must also have the PURCHASE DATA EXCHANGE LISTING privilege and you must meet additional
> criteria. Refer to [Pay for listings](../../collaboration/consumer-listings-paying.md).

## Install an app from a privately shared listing

> **Note:**
>
> As a provider, you can test your app by creating a private listing, sharing it with another account in your organization
> that you have access to, signing in to that account, and following these steps to install the app.

To install an app from a private listing:

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. In Recently shared with you, select the tile for the listing.
4. Select Security to view the privileges and logging requests for the app, including:

   * [Account level privileges](ui-consumer-granting-privs.md)
   * [Privileges on objects](ui-consumer-granting-privs.md)
   * Connections
   * [App events](ui-consumer-enable-logging.md)
5. Select Get, or for a monetized app, select Buy.

   > **Note:**
   >
   > If the provider includes required
   > [event definitions](ui-consumer-enable-logging.md)
   > in the app, the consumer must set up an event table before installing the app. Even sharing
   > and the required event definitions are enabled during installation and cannot be disabled later.
6. Enter a name for the app.
7. Select the warehouse that you want to use to install the app.
8. Select Get.
9. Select Open to view the app or Done to finish.

## Install an app from a Snowflake Marketplace listing

To install an app from a Snowflake Marketplace listing:

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Marketplace » Snowflake Marketplace.
3. Search or browse to the listing you want to access.
4. Select the listing, then view the privileges and logging requests for the app,
   including:

   * [Account level privileges](ui-consumer-granting-privs.md)
   * [Privileges on objects](ui-consumer-granting-privs.md)
   * [Events and logs](ui-consumer-enable-logging.md)
5. Select Get to access the listing.

   > **Note:**
   >
   > If the provider includes required
   > [event definitions](ui-consumer-enable-logging.md)
   > in the app, the consumer must set up an event table before installing the app. Even sharing
   > and the required event definitions are enabled during installation and cannot be disabled later.
6. Select the warehouse that you want to use to install the app.
7. (Optional) Enter a name for Application name.
8. Select Get.
9. Select Open to view the app, or select Done to finish.

## Install an app using release channels

Release channels allow providers to publish multiple versions of an app. Possible
versions are:

QA:
:   Allows providers to publish a test version of an app. Apps installed from the QA release channel
    have not been reviewed or tested.

Alpha:
:   Allows providers to share apps with consumers to obtain feedback. Apps installed from the Alpha
    release channel may contain versions that have not passed the security review.

Default:
:   This is the production version of an app. Default versions have passed the Snowflake and functional review.

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. In Recently shared with you, select the tile for the listing.
4. Select Security to view the privileges and logging requests for the app, including:

   * [Account level privileges](ui-consumer-granting-privs.md)
   * [Privileges on objects](ui-consumer-granting-privs.md)
   * Connections
   * [App events](ui-consumer-enable-logging.md)
5. Select Get to access the listing.
6. Select the version of the app you want to install.

   Installing different versions of the app allows you to test each version independently.
7. Select the warehouse that you want to use to install the app.
8. Optional: For Application name, enter a name.
9. Select Get.
10. Select Open to view the app or Done to finish.

## Install multiple instances of an app

Providers can configure an app so that multiple instances of an app can be installed at the same time.

> **Note:**
>
> Apps installed from a trial listing or a monetized listings cannot have multiple instances.

If an app is configured to allow multiple installs, consumers can install additional instances after
installing the app from a private listing or from
the Snowflake Marketplace.

If multiple instances are enabled for an app, you can install a maximum of 10 instances in your account.

To install a new instance of an app, perform the following tasks:

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select the app of which you want to install another instance.

   If multiple instances of the app are already installed, Snowsight displays
   a panel showing all of the instances of the app.
4. Select Add instance

   > **Caution:**
   >
   > Add instance only appears if the provider has configured the app to allow multiple instances.
5. Enter a name for the instance, then select the warehouse to use for this instance.
6. Select Get.

   > The app installs and Snowflake sends a notification email to the app admin.
7. Select Done to complete the installation.

After installing the app instance, you can
[set up event tracing for an app](ui-consumer-enable-logging.md),
[configure privileges](ui-consumer-granting-privs.md) for the app, and perform other
[management tasks](ui-consumer-managing-applications.md).
