# Source: https://docs.axonius.com/docs/systrack.md

# Lakeside SysTrack

Lakeside SysTrack is a digital experience monitoring solution used for workplace analytics, IT asset optimization, and end-user experience.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

The Lakeside SysTrack adapter supports two authentication methods:

<Tabs>
  <Tab title="API Key (Recommended)">
    **API Key Authentication** - Uses a SysTrack API key for authentication. This is the recommended method for new integrations.

    To generate an API key:

    1. Log in to your SysTrack portal
    2. Navigate to **Settings > Manage API Keys**
    3. Create a new API key with one of the following types:
       * **SysTrack Read-Only** (recommended for Axonius)
       * **SysTrack Read/Write**

    **Note:** API keys expire after up to 180 days. You will need to regenerate and update the key in Axonius before expiration.
  </Tab>

  <Tab title="OAuth2 (Legacy)">
    **OAuth2 (Username/Password) Authentication** - Uses Azure AD B2C OAuth2 authentication with username and password. This is the legacy authentication method.

    This method requires:

    * Azure AD B2C domain for token requests
    * SysTrack Client ID
    * Service account username and password
  </Tab>
</Tabs>

### APIs

Axonius uses the SysTrack API. The following endpoints are called:

* `GET /api/systems` - Fetch device information
* `GET /api/systems/{system_id}?$expand=invn.localmembers` - Fetch system local members (optional)

### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Lakeside SysTrack, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

<Tabs>
  <Tab title="API Key (Recommended)">
    1. **Host Name or IP Address for API request** *(default:`https://cloud.lakesidesoftware.com`)* - The hostname or IP address of the Lakeside SysTrack server.

    2. **Authentication Method** - Select **API Key** from the dropdown.

    3. **API Key** *(required)* - The SysTrack API key generated from **Settings > Manage API Keys** in SysTrack. Use a "SysTrack Read-Only" or "SysTrack Read/Write" key type. API keys expire after up to 180 days.
  </Tab>

  <Tab title="OAuth2 (Legacy)">
    1. **Host Name or IP Address for API request** *(default:`https://cloud.lakesidesoftware.com`)* - The hostname or IP address of the Lakeside SysTrack server.

    2. **Authentication Method** - Select **OAuth2 (Username/Password)** from the dropdown.

    3. **Host Name or IP Address for token request** *(`lakaborgsystrack.b2clogin.com`)* - The Azure AD B2C domain for OAuth2 token requests.

    4. **Systrack Client ID** *(required)* - The Client ID for your SysTrack tenant. Can be found on the Tenant Information page in SysTrack.

    5. **User Name** and **Password** *(required)* - The service account username for API access and the service account password.
  </Tab>
</Tabs>

<br />

<Image alt="SysTrack" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SysTrack.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:
  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

* **Fetch system's local members** - Select this option to fetch the local member inventory for each system.