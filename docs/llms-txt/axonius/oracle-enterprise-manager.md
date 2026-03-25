# Source: https://docs.axonius.com/docs/oracle-enterprise-manager.md

# Oracle Enterprise Manager

Oracle Enterprise Manager is an on-premises management platform that provides a single dashboard to manage all Oracle deployments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Oracle Enterprise Manager server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Oracle Enterprise Manager" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Oracle%20Enterprise%20Manager.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Include devices with the following type names** - Enter a comma-separated list of devices with specified type names to be fetched.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The user executing the REST call must have the VIEW\_ANY\_TARGET privilege or specific target-level privileges to see information about 'devices.'

## APIs

Axonius uses the [REST API for Oracle Enterprise Manager](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/APIOverview.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* TCP port 80, 443, or any other specific port set by the customer

## Supported From Version

Supported from Axonius version 4.7