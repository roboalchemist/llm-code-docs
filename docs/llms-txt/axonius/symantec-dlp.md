# Source: https://docs.axonius.com/docs/symantec-dlp.md

# Symantec DLP

Symantec DLP is a data loss protection and prevention solution. Its management console, the DLP Enforce Platform, and its reporting tool, IT Analytics for DLP, allows writing and enforce policies to reduce information risks.

## Assets Types Fetched

* Devices, Networks

## Parameters

1. **Oracle Server** *(required)* - The DNS / IP Address of the Oracle server that your Symantec DLP instance is using.
2. **Port** *(optional, default: 1521)* - Enter the port of the Symantec DLP server.
3. **Database** *(required)* - The name of the database inside the Oracle DB.
4. **Alternative Schema Prefix** - Enter a customized prefix for the `agent` table from which data is fetched. The default prefix is "protect".
5. **User Name** and **Password** *(required)* - A user name and a password for a user with the [Required Permissions](/docs/symantec-dlp#required-permissions).
6. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-P12OG3WX.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Specify the number of results per page received for a given SQL query to gain better control on the performance of all connections for this adapter.
2. **Skip deleted devices** *(required, default: false)* - Select to exclude deleted devices from the fetch.
3. **Fetch subnets as network assets** - Select to fetch subnets as Networks.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [User Name](#parameters) must have Read-only permissions for Agent and Agent\_group tables to fetch assets.