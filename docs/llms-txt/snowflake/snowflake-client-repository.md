# Source: https://docs.snowflake.com/en/user-guide/snowflake-client-repository.md

# Downloading Snowflake Clients, Connectors, Drivers, and Libraries

To download the installation package for a Snowflake client, connector, driver, or library, use the
download pages in the Snowflake Developer Center.

If you want to write a script to download clients over HTTP (e.g. using [curl](https://curl.se/)), you can download SnowSQL, the ODBC Driver,
the Snowpark Library, and SnowCD directly from the Snowflake Client Repository.

See [Drivers](../developer-guide/drivers.md) and [Using Snowflake with Kafka and Spark](connectors.md) for documentation for the drivers and
connectors, respectively. For other developer documentation,
see [Develop Apps and Extensions](https://docs.snowflake.com/developer).

## Snowflake Developer Center Download Pages

To download a Snowflake client, use the following download pages in the [Snowflake Developer Center](https://developers.snowflake.com/):

| Client / Connector / Driver / Library | Download Page |
| --- | --- |
| [Snowflake CLI](../developer-guide/snowflake-cli/index.md) | [Snowflake CLI Download](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html) |
| [ODBC Driver](../developer-guide/odbc/odbc.md) | [ODBC Download](https://developers.snowflake.com/odbc/) |
| [Snowpark API](../developer-guide/snowpark/index.md) | [Snowpark Client Download](https://developers.snowflake.com/snowpark/) |
| [Drivers](../developer-guide/drivers.md) | [Drivers and Libraries](https://developers.snowflake.com/drivers-and-libraries/) |
| [Scala and Java connectors](connectors.md) | [Drivers and Libraries](https://developers.snowflake.com/drivers-and-libraries/) |
| [SnowCD](snowcd.md) | [Drivers and Libraries](https://developers.snowflake.com/drivers-and-libraries/) |
| [Snowpark ML](../developer-guide/snowflake-ml/overview.md) | [Drivers and Libraries](https://developers.snowflake.com/drivers-and-libraries/) |

## Snowflake Client Repository

To download SnowSQL, the ODBC Driver, the Snowpark Library, or SnowCD over HTTP programmatically (e.g. using [curl](https://curl.se/)), use the
Snowflake Client Repository. The Snowflake Client Repository serves the packages for these clients through CDN (Content Delivery
Network) using the following endpoints:

> * <https://sfc-repo.azure.snowflakecomputing.com/index.html> (mirror on Azure Blob)

If the endpoint is not specified explicitly, the client upgrader (e.g., the SnowSQL auto-upgrader) uses the AWS endpoint. For instructions on specifying the endpoint, see the installation documentation for the client.

> **Note:**
>
> Users can download Snowflake clients from either endpoint regardless of which cloud provider hosts their Snowflake account.
