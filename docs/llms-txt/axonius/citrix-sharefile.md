# Source: https://docs.axonius.com/docs/citrix-sharefile.md

# Citrix ShareFile

ShareFile is a secure content collaboration, file sharing, and sync software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Company Name (subdomain)** *(required)* - The subdomain of your account. For instance if the URL of your account is 'mycompany.sharefile.com', then enter 'mycompany'.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If you access a ShareFile environment that requires Two-Step Verification, you must generate an application-specific password in the adapter configuration in order to allow API access.
  For more information, see [Security](https://docs.sharefile.com/en-us/sharefile/configure/admin-settings/security.html).
</Callout>

3. **Client ID** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
4. **Client Secret** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  You need to use both **User Name** and **Password** and **Client ID** and **Client Secret**.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
9. **Fetch Folder Data**  *(required, default: true)* - Select to fetch folder data.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CitrixShareFileNew](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CitrixShareFileNew.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch User Permissions and Access Controls** *(default: true)* - By default this adapter fetches user permissions and access controls. Clear this option to not fetch user permissions and access controls.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Citrix ShareFile API](https://api.sharefile.com/docs).

## Required Permissions

The value supplied in [User Name](#parameters) and [API Key](#parameters) must be associated with the following roles:

* AdminManageEmployees role
* CanManageUsers role

## Supported From Version

Supported from Axonius version 4.5