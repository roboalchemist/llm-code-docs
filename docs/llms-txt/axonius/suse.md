# Source: https://docs.axonius.com/docs/suse.md

# SUSE Manager

SUSE Manager is an open-source infrastructure management tool for Linux systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SUSE Manager server that Axonius can communicate with via the [Required Ports](#required-ports). Example URL: `https://manager.example.com/rhn/manager/api`
   Update the above URL and replace `manager.example.com` with your SUSE Manager Server URL. Then use the updated URL as the hostname for the adapter.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SUSE%20Manager(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SUSE%20Manager(1).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

Under **Endpoints Config**, you can enable any of the following options (disabled by default) to enrich the fetched devices with additional data by adding a field to the Devices table. Based on your selection, a System Groups / System Extra Packages / System Currency Stores field will be added to the table.

1. **Enrich System with System Groups**
2. **Enrich System with System Extra Packages**
3. **Enrich System with System Currency Stores**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SUSE Manager API](https://documentation.suse.com/suma/4.3/api/suse-manager/index.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have all of their system groups assigned to them, ideally "all groups".

<Callout icon="📘" theme="info">
  Important

  Due to a bug in SUSE Manager’s API, you should not check the ‘Read-Only API User’.
</Callout>

## Supported From Version

Supported from Axonius version 6.0