# Source: https://docs.axonius.com/docs/snipe-it.md

# Snipe-IT

Snipe-IT is a free, open source IT asset management system written in PHP.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **SnipeIT Domain** *(required)* – The hostname of the Snipe-IT server.
2. **API Key** *(required)* – The API Key generated through the Snipe-IT web interface.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SNIPE\_ITRegular.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SNIPE_ITRegular.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **SnipeIT category include list** *(optional, default: empty)* - Specify a comma-separated list of Snipe-IT categories.
   * If supplied, all connections for this adapter will only fetch devices whose category is any of the comma-separated list of Snipe-IT categories defined in this field.
   * If not supplied, all connections for this adapter will fetch devices with any Snipe-IT category.
2. **SnipeIT status label include list** *(optional, default: empty)* - Specify a comma-separated list of Snipe-IT lables. When this field is populated,  all connections for this adapter will only fetch devices whose label is any of the comma-separated list of Snipe-IT labels defined in this field.
3. **Use asset tag as hostname** - Select this option to set the Hostname with the Asset Tag value.
4. **Use asset name as hostname** - Select this option to set the Hostname with the Asset Name value.
5. **Parse updated at as Last Seen** - Select this option to parse the "Updated\_at" field as the "Last seen" field.