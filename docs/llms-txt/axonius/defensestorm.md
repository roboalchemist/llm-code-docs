# Source: https://docs.axonius.com/docs/defensestorm.md

# DefenseStorm

DefenseStorm provides CyberSecurity, CyberCompliance and CyberFraud solutions specifically built for banking.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the DefenseStorm server.

2. **API Key** and **Secret Key** *(required)* - An API Key  and Secret Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To get an API Key and Secret Key, see [Get an API Key and Secret Key](/docs/defensestorm#get-an-api-key-and-secret-key).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **Fetch Tracked** *(optional, default: true)* - Select whether to fetch tracked devices.

8. **Fetch Untracked** *(optional)* - Select whether to fetch untracked devices.

9. **Fetch Deleted** *(optional)* - Select whether to fetch devices that were deleted.

10. **Filter By X Days** *(required, default: 30)* - Specify the number of days to fetch device information.

11. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="DefenseStorm" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DefenseStorm.png" />

## APIs

Axonius uses the [DefenseStorm Assets API](https://api.defensestorm.com/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **Port 443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with one of the following permission sets:

* "Power User" or "Admin" default roles
* RBAC custom role with Read/Write permission selected in **Settings** `>` **Auth Tokens**.

## Get an API Key and Secret Key

**To get an API Key and Secret Key**

1. In GRID, navigate to **Settings**.

2. Select **Input Tokens** on the top of the displayed Settings page.

3. At the top right of the Input Tokens page, click **Get API Token**.  Write down the key, secret, and organization ID (orgId) displayed.

4. The new key should be visible at the top of the Input Tokens view.  Click on the **Unnamed** label and give a descriptive label (such as "API Key - Assets API"), then click **Save** to complete the token rename.

<Callout icon="📘" theme="info">
  Note

  It is highly recommended to use different API keys for each API service. This limits the impact to your integrations should an API key need to be reissued in the future.
</Callout>

## Supported From Version

Supported from Axonius version 4.6