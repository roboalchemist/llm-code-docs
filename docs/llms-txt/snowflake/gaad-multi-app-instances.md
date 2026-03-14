# Source: https://docs.snowflake.com/en/connectors/google/gaad/gaad-multi-app-instances.md

# Install multi application instances for connectors (GAAD)

You can install multiple instances of the same connector application on your Snowflake account.

To install an additional application instance, do the following:

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Marketplace » Snowflake Marketplace.
3. Select the application for which you want to install another instance. The application details page appears.
4. Click Add instance. The installation dialog appears.
5. Provide the instance name and select the warehouse to be used during the installation.
6. Select Get to begin the installation process.

Adding connector instances can take several minutes. When the installation process completes, you get an email notification.

> **Attention:**
>
> To avoid ingested data corruption, during connector configuration, always use a database schema that is
> different from all other native applications.

To access your installed connector application instances, do the following:

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select your application instance to access it.
