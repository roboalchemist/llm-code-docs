# Source: https://docs.axonius.com/docs/oomnitza.md

# Oomnitza Enterprise Technology Management

Oomnitza Enterprise Technology Management  helps IT teams manage technology assets with an agentless solution for endpoints (laptops, mobile devices, monitors, peripherals, and accessories), software (desktop, cloud, virtual machines), and users.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Oomnitza Enterprise Technology Management server.

2. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets. To get the API token navigate to the Settings page and select [API](https://oomnitza.zendesk.com/hc/en-us/articles/360049276794-How-To-Create-an-API-Token?mobile_site=false).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="oomnitza.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/oomnitza.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Assets Status Ignore List** *(required, default: False)* - A comma separated list of asset status that should not be fetched.
   1. Default values: Decommissioned, Donated, and Retained by Departing User.
   2. To fetch all assets, clear the default and choose Save.
2. **Assets Type Ignore List** *(required, default: False)* - A comma separated list of asset types that should not be fetched.
3. **Populate Asset Name field with Host Name value** - Select this option to display the Host Name value in the Asset Name field

## APIs

Axonius uses the [Oomnitza API](https://oomnitza.zendesk.com/hc/en-us/article_attachments/17200483129623)(refer specifically to pages 6, *List Existing Asset Records* and  page 15, *Searching for User Records*).

## Supported From Version

Supported from Axonius version 4.5