# Source: https://docs.axonius.com/docs/proofpoint-endpoint-dlp.md

# Proofpoint Endpoint DLP

Proofpoint Endpoint DLP helps identify risk user behavior and protect sensitive data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

* **Host Name or IP Address** *(required, default: explore.proofpoint.com)* - The hostname or IP address of the Proofpoint Endpoint DLP server.

* **Specify a direct endpoint** - Toggle on to specify which endpoint to fetch devices from if different from the main domain used for authentication. **Specify a direct endpoint** is an option for users who may have a Proofpoint account/services in international availability zones.

* **Tenant ID** *(required)* - Use for server authentication. The Tenant ID is the prefix in the URL used to access the portal. For example, TENANT\_ID in `https://TENANT_ID.explore.proofpoint.com`

* **Client ID** and **Client Secret** *(required)* - Register an App in the Dev portal to get a **Client ID** and **Client Secret** as shown below.

  ![ProofPointDRLConmfig](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProofPointDRLConmfig.png)

* **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Proofpoint_Endpoint_DLP" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Proofpoint_Endpoint_DLP.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Ignore updater instances agent information** *(required, default: true)* - Select whether to ignore agent information of updater instances.
* **Ignore Deleted Instances** *(optional)* - Select whether to ignore deleted instances.
* **Populate Last Seen Time for Last Seen (Updater) Field, Non-Agent Only** - Select this option to populate the Last Seen Updater field for devices of the type updater agent, and not populate the Last Seen field.
* **Populate Last Seen Time for Last Seen (Updater) and Last Seen Fields** - Select this option to parse "Last Seen (Updater)" and "Last Seen" fields with the same value.
* **Use latest version of the API** - Select this option to use the latest version of the API.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Permissions

The application need to have permissions for 'Endpoint Component Instance View'.

## Supported From Version

Supported from Axonius version 4.6