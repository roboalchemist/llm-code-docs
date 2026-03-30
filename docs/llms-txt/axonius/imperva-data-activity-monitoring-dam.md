# Source: https://docs.axonius.com/docs/imperva-data-activity-monitoring-dam.md

# Imperva Data Activity Monitoring (DAM)

Imperva Data Activity Monitoring (DAM) defines and enforces data security and compliance policies across the cloud and on-premises including relational databases, mainframes, big data platforms, data warehouses, and enterprise file stores.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Databases

## Parameters

1. **Imperva DAM Domain** *(required)* - The hostname or IP Address of the Imperva DAM server. When using a hostname, it must be the FQDN (Fully Qualified Domain Name) of your Imperva DAM server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Imperva%20Data%20Activity%20Monitoring%20(DAM)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Imperva%20Data%20Activity%20Monitoring%20\(DAM\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch DB connections as assets** - Select this option to fetch DB connections as assets.
2. **Fetch DAS assessment results** - Select this option to fetch DAS assessment results.
3. **Use DB name for asset name** - Select this option to use the database name for the asset name.
4. **Fetch DAS Assessment Run DBS** - Select this option to fetch additional details for the following fields: Database ID, Hostname, and Vendor ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Imperva DAM API](https://docs.imperva.com/bundle/v14.15-dam-api-reference-guide/page/61914.htm).

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
Such permission are required to access the data necessary to a given API resource. For more details, see [Creating a SecureSphere User](https://docs.imperva.com/bundle/v12.5-administration-guide/page/6754.htm) on Imperva documentation website.