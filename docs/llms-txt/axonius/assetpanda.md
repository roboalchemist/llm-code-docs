# Source: https://docs.axonius.com/docs/assetpanda.md

# AssetPanda

AssetPanda is a cloud-based asset tracking and management platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users

## Enforcements

Axonius has a built-in enforcement for creating and updating assets in AssetPanda.

**Related Enforcement Action:**

[Asset Panda - Create And Update Assets](/docs/asset-panda-create-and-update-assets)

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the AssetPanda server.
2. **Email** and **Password** *(required)* - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Bearer Token** *(optional)* - A Bearer token received from AssetPanda.
4. **Verify SSL** - Choose whether to verify the SSL certificate of the AssetPanda server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in HTTPS Proxy.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the HTTPS Proxy.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AssetPanda(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetPanda(1).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch asset type** - Select the type of asset to fetch from the drop-down. You can either choose Assets or Hardware Assets.
2. **Get users** - Select this option to fetch users.
3. **Parse invoice number** *(required, default: true)* - Select this option to parse the invoice number.
4. **Parse PO number** *(required, default: true)* - Select this option to parse the PO number.
5. **Parse employee status** *(required, default: true)* - Select this option to parse the employee status field.
6. **Fetch Employees** - Select this option to fetch employee group assets as users.
7. **Enable Custom Parsing** - Toggle on to enable custom parsing. When this setting is enabled, you can define which parts of the raw data you want to extract and how to interpret them, separately for devices and users. You can choose to parse the data into an already existing field, or create a new one. See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.
   * **Device Custom Parsing**
   * **User Custom Parsing**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [AssetPanda API - v3.1](https://team-asset-panda.readme.io/reference/post_v3-groups-group-id-search-objects).

## Required Permissions

The value supplied in [Email](#parameters) must have permissions to fetch assets.

## Supported From Version

Supported from version 4.5