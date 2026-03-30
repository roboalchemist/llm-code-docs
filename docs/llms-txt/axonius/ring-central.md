# Source: https://docs.axonius.com/docs/ring-central.md

# RingCentral

RingCentral provides cloud-based communication and collaboration products and services including phone, messaging, video meetings, and contact center.

## Asset Types Fetched

* Devices, Users, Application Settings

## Before You Begin

### APIs

Axonius uses the [RingCentral API](https://developers.ringcentral.com/api-reference/using-the-api).

### Required Ports

* **TCP port 80/443**

### Required Permissions

The value supplied in [Client ID](/docs/ring-central#required-parameters-all-asset-types) must be associated with the following permissions:

* ReadAccounts (to fetch Users)
* ReadUserDevices (to fetch Devices)

## Configuring RingCentral to Work in Axonius

### Basic Configuration

1. Log in to [developers.ringcentral.com](https://developers.ringcentral.com/).
2. Select **Console** at the top-right corner of the screen.
3. Click on any of your applications. A dashboard opens.
4. In the left column, go to **Settings**. The **Settings** page opens, displaying app configuration information.
5. Scroll down to **Security** `>` **Application Scopes**.
6. Enter the required permission in **Application Scopes**.

### Configuring the App and Token

1. Before providing the [**Client ID** and **Client Secret** connection parameters](/docs/ring-central#required-parameters-all-asset-types), you need to create an app to access the API and associate client details. See [Configuring apps to use JWT](https://developers.ringcentral.com/guide/authentication/jwt/config-app) for more information.
2. Before providing the [**JWT Token** connection parameter](/docs/ring-central#required-parameters-all-asset-types), you need to [create a personal JWT credential](https://developers.ringcentral.com/guide/getting-started/create-credential) and assign ReadAccounts permission to the app when creating the token.

## Connecting the Adapter in Axonius

### Required Parameters - All Asset Types

1. **Host Name or IP Address** *(default: `https://platform.ringcentral.com`)* - The hostname or IP address of the RingCentral server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Client ID**, **Client Secret**, and **JWT Token**  - Credentials with permissions to fetch assets. See [Configuring the App and Token](/docs/ring-central#configuring-the-app-and-token) to learn more.

### Required Parameters - Application Settings

1. **User Name** and **Password**  - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image alt="RingCentralConnection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-9F4DKTH1.png" />

### Optional Parameters - All Asset Types

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

### Optional Parameters - Application Settings

1. **User managed by SSO** -  Enable this if the user is managed by an SSO. When enabled, the following parameters are displayed:
   1. **SSO Provider** - From the dropdown, select which SSO provider to use to manage your users, either **Google SSO** or **Other SSO**. For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

   2. **2FA Secret** - The secret generated in RingCentral for setting up 2-factor authentication for the adapter user created to fetch Application Settings. This parameter is required if the user is protected by 2FA authentication.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices** - Select this option to fetch Devices.
2. **Fetch Application Settings** - By default Axonius fetches Application Settings. Clear this option to not fetch this asset type.
3. **Enrich users with directory entries** - Select this option to enrich Users with phone numbers data fetched from directory entries
   * The API endpoint for this setting is `POST f'{ACCOUNTS_SUFFIX}/~/directory/entries/search'`. To learn more, see [Search Company Directory Entries](https://developers.ringcentral.com/api-reference/Internal-Contacts/searchDirectoryEntries).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Supported From Version

Supported from Axonius version 6.0