# Source: https://docs.axonius.com/docs/digital-guardian-dlp.md

# Digital Guardian DLP

Digital Guardian DLP is a SaaS-based platform that provides data-loss prevention across Windows, Mac, and Linux systems and applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Digital Guardian DLP server.

2. **API Access ID** and **API Access Secret** *(required)* - The API token for a user account that has permissions to fetch assets.
   **To obtain the API Access ID and API Access Secret**

   1. From the Digital Guardian Management Console, navigate to: **System** `>` **Configuration** `>` **Cloud Services**.
   2. Copy the values displayed in **API Access ID** and **API Access Secret**.

3. **Export Profile** *(required)* - Enter the Export Profile, obtainable from Digital Guardian.

4. **Export API Version** *(optional, default: 1.0)* - Select the Export API version.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="DigitalGuardian_DLP" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DigitalGuardian_DLP.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Remove device name prefix** *(optional)* - When selected, the device name won't include the prefix before the backslash (\\) delimiter.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Digital Guardian External API.

## Supported From Version

Supported from Axonius version 4.5