# Source: https://docs.axonius.com/docs/sunflower.md

# Sunflower

Sunflower Lab is a mobile app, web app, and custom software development company.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Sunflower server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Access Key** *(required)* - An Access Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Profile Description** *(default: CUST\_AREA)*

4. **Operation** *(default: INSERT)*

5. **Interface Type** *(default: QUERY)*

6. **Asset Identifier Key** *(default: Identifier)* - The key to be used as the device ID.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sunflower](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sunflower.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Custom Attributes for request** - Expand this section to add fields. For each field, specify the following:
  * **Attribute Name** - Enter the attribute name to add.
  * **Value** - Enter a value for the attribute.
    Click **+ Add Field** to add as many fields as you like, or **x** to delete the row.

![Sunflower custom attributes.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sunflower%20custom%20attributes.png)

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the snflwr\_wsc\_sunprds1/LoadcWSPort wsdl endpoint to call the function wsLoadcElement with the param ASSET\_DETAIL to get devices.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Access Key](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0