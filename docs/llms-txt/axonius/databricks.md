# Source: https://docs.axonius.com/docs/databricks.md

# Databricks

Databricks combines data warehouses & data lakes into a lakehouse architecture that handles  data, analytics, and AI use cases.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Databricks server.

2. **Personal Access Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Databricks Level** - Select Account or Workspace. When you select Account the system scans all workspaces to  retrieve devices and users while also fetching account-level users and groups.
   1. When you select Account you need to enter the **Databricks Account ID**

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Databricks" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Databricks.png" />

## APIs

Axonius uses the [Cluster API 2.0](https://docs.databricks.com/dev-tools/api/latest/clusters.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 80, 433 or any other ports configured to access the environment

## Required Permissions

The value supplied in [Personal Access Token](#parameters) must be associated with credentials that have Permission to read Clusters API 2.0 in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version          | Supported | Notes |
| ---------------- | --------- | ----- |
| Clusters API 2.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7