# Source: https://docs.snowflake.com/en/user-guide/sfsql-install-config.md

# Configuring sfsql — *Obsoleted*

This topic describes how to configure `sfsql`. Note that the `sfsql` installer is no longer available for download.

## Prerequisites

`sfsql` uses the Snowflake JDBC driver to connect to Snowflake. The driver
does not need to be downloaded and installed before installing `sfsql`
because the driver is automatically installed along with `sfsql`; however,
the JDBC driver requires the 64-bit version of Java 1.7 (or higher).

If the required version of Java is not installed on the client machine where
`sfsql` will be installed, it must be installed. For more information, see
[Java requirements for the JDBC Driver](../developer-guide/jdbc/java-install.md).

## Configure Client Login

`sfsql` provides various parameters for configuring client connection and login.
The `client/login.defaults` file can be used to define default connection
parameters which can be overridden on the command line when starting the client.

When you download the client from Snowflake, the following parameters are preset
in `login.defaults`:

> ```bash
> ACCOUNT=<account_name>
> GSIP=<account_name>.snowflakecomputing.com
> PORT=443
> ```
>
> where `<account_name>` is the name assigned to your account by Snowflake.

To set additional defaults, add the corresponding parameters to the file, using the
same structure/format described above. For a complete list of the defaults you can set
in the file, see [Starting and Stopping sfsql — Obsoleted](sfsql-start-stop.md).
