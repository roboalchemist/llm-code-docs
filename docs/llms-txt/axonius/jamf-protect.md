# Source: https://docs.axonius.com/docs/jamf-protect.md

# Jamf Protect

Jamf Protect is an endpoint protection solution that prevents macOS malware, detects and remediates Mac-specific threats, and monitors endpoints for compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Jamf Protect server.

2. **Client ID** and **Password** *(required)* - An API Client associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1715\).png)

## APIs

Axonius uses the [Jamf Protect API](https://docs.jamf.com/jamf-protect/administrator-guide/Jamf_Protect_API.html).

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have permissions to fetch assets.

### Creating an API Client in Jamf Protect

1. In Jamf Protect, click **Administrative** `>` **API Clients** from the sidebar.
2. Click **Create API Client**.
3. Enter a name for your API client.
4. Copy the API client password for later use.

<Callout icon="📘" theme="info">
  NOTE

  Important: This value will not be displayed again by Jamf Protect.
</Callout>