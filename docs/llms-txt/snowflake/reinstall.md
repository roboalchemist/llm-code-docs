# Source: https://docs.snowflake.com/en/connectors/postgres6/reinstall.md

# Source: https://docs.snowflake.com/en/connectors/mysql6/reinstall.md

# Reinstall the Snowflake Connector for MySQL

> **Important:**
>
> Thank you for your interest in the Snowflake Connector for MySQL.
> We’re now focused on a next-generation solution that will offer a significantly
> improved experience; therefore, moving this connector to the general availability
> status is currently not on our product roadmap.
> You may continue to use this connector as preview feature, but please note that support for future bug
> fixes and improvements are not guaranteed. The new solution is available as [Openflow Connector for MySQL](../../user-guide/data-integration/openflow/connectors/mysql/about.md) and
> includes better performance, customizability, and enhanced deployment options.

To upgrade or reinstall the Snowflake Connector for MySQL, do the following:

1. Drop the connector database using Snowsight. You will find instructions [here.](https://other-docs.snowflake.com/en/native-apps/consumer-managing-applications#uninstall-an-app-using-snowsight)
2. Install and run the new version as described in [Snowflake Connector for MySQL installation and configuration tasks](tasks.md).

   > > **Note:**
   > >
   > > The reinstalled connector will need to be set up again and will pull all the data from the source system like a fresh installation.
   > > Destination database can be reused, but data in existing tables will be reloaded instead of updated.
