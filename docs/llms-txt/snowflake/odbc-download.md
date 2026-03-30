# Source: https://docs.snowflake.com/en/developer-guide/odbc/odbc-download.md

# Downloading the ODBC Driver

Snowflake provides an installer for the ODBC driver.

> **Note:**
>
> If you plan to use `yum` to download and install the ODBC driver for Linux, skip ahead to
> [Using yum to download and install the driver](odbc-linux.md).

To download the installer:

1. Review the [license agreement](https://sfc-repo.snowflakecomputing.com/odbc/Snowflake_ODBC_Driver_License_Agreement.pdf).
2. If you are already using the ODBC driver and need to download an updated version, check the version that you are using, and
   review the changes between your version and the updated version in the [ODBC Driver release notes](../../release-notes/clients-drivers/odbc.md)

   To find the version of the driver that you are using, call the [CURRENT_CLIENT](../../sql-reference/functions/current_client.md) SQL function from
   an application using the driver. You can also [verify the driver version](../../user-guide/snowflake-client-version-check.md) by
   examining queries executed by the driver in the QUERY_HISTORY view.
3. Go to the [ODBC Download](https://developers.snowflake.com/odbc/) page, and download the installer.

   > **Note:**
   >
   > The Linux installation package is provided in three variations:
   >
   > * TGZ (TAR file compressed using .GZIP)
   > * RPM
   > * DEB
   >
   > The TGZ package requires some manual configuration tasks. The RPM and DEB packages include an automated installer and support
   > validation using the public GPG key provided by Snowflake.
4. See the following topics to install and configure the driver:

   * [Installing and configuring the ODBC Driver for Windows](odbc-windows.md)
   * [Installing and configuring the ODBC Driver for macOS](odbc-mac.md)
   * [Installing and configuring the ODBC Driver for Linux](odbc-linux.md)
   * [ODBC configuration and connection parameters](odbc-parameters.md)
