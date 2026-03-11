# Source: https://docs.axonius.com/docs/druva-cloud-platform.md

# Druva Cloud Platform

Druva Cloud Platform is a data protection as-a-service that provides management across all customer data sources that are scalable, predictable and on-demand.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Druva Domain** *(required, default: `https://apis.druva.com`)* - Use your Druva Cloud Platform domain.
2. **Client ID** and **Client Secret** *(required)* - To fetch data from Druva Cloud Platform, you need to generate API Credentials for Axonius, which is a combination of Client ID and Secret Key. API Credentials can be created from the Druva Cloud Platform console.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **Organization ID** *(optional)* - Specify your Druva Cloud Platform Organization ID.
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Druva Cloud Platform](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Druva%20Cloud%20Platform.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Do not fetch disabled devices** *(required, default: False)* - Select to not fetch disabled devices.
2. **Fetch last successful backup for devices** *(optional, default: False)* - Select to fetch the last successful backup for each device.
3. **Fetch Microsoft 365 apps status** - Select this option to fetch the Microsoft 365 apps status configured to backup as an Application asset type.
4. **Fetch servers** - Select this option to fetch servers. Make sure that **Organization ID** is included in the connection when using this setting.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Permissions

In order to fetch InSync devices, the user associated with **API key** needs have the Druva Cloud Administrator role.