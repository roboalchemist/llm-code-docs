# Source: https://docs.axonius.com/docs/illusive-networks.md

# Illusive Networks

Illusive Networks deceives cyber attackers by planting false information about a given network's resources.

<Callout icon="📘" theme="info">
  NOTE

  Axonius uses the Illusive REST API. For details, see the Illusive REST API Guide.
</Callout>

The Illusive Networks adapter connection requires the following parameters:

1. **Illusive Domain** – The hostname of the Illusive Networks server.
2. **API Key** – The API key obtained from the Illusive Management Server. For more details, see the section below.
3. **Verify SSL** – Choose whether to verify the SSL certificate of the server.
4. **HTTPS Proxy** (optional) – Connect the adapter to a proxy instead of directly connecting it to the domain.

![illusive.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/illusive.png)

## Generating API Key for Illusive REST API Request

To obtain an API key for the Illusive REST API Request:

1. Navigate to **Settings `>` General** , **API keys** pane.
2. Enter values in the following fields:
   * **Description** - Specify description of key.
   * **Permissions** - Select the following permissions:
     * All Permissions
     * Create Event Read
     * Monitoring Data
   * **Restrict Source IP** (optional) - Limit the API key to be used only from the specified source IP address.
3. Click **+Add**. The API Key is created and added to the list of keys shown.
4. Copy the header containing the key to a text file and save it securely.

<Callout icon="📘" theme="info">
  NOTE

  The key is valid for one year to access the REST API on the specific Management Server only.
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Machine execution status include list** *(required, default: SUCCESS\_RESPONSE, FAILURE\_CONNECTION, FAILURE\_EXECUTION, SUCCESS\_EXECUTION, FAILURE\_RESPONSE)* - Specify which types of machine execution status to include in the fetch.

2. **Use only SUCCESS\_RESPONSE responses for last seen** *(optional, default: false)* - Select whether to include only successful pushes to populate the **Last Seen** field in Axonius.

<Image alt="Illusive_advanced" width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Illusive_advanced.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>