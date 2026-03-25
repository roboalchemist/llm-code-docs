# Source: https://docs.axonius.com/docs/lookout-mobile-endpoint-security.md

# Lookout Mobile Endpoint Security

Lookout Mobile Endpoint Security is a mobile security solution that provides comprehensive risk management across iOS and Android devices to secure against app, device, and network-based threats while providing visibility and control over data leakage.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.lookout.com/`)* - The hostname or IP address of the Lookout Mobile Endpoint Security server.
2. **User Name or E-mail Address** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets. This can be a read-only access account.

<Callout icon="📘" theme="info">
  Note

  When **Application Token** is not supplied, **User Name or E-mail Address** and **Password** are required.
</Callout>

3. **Enterprise GUID** *(required)* -  The globally unique identifier associated with a user account that has permissions to fetch assets. Obtain the GUID from [Lookout](https://api.lookout.com/system/account).
4. **Application Token** *(optional)* - Specify the application token to fetch the threat data.

<Callout icon="📘" theme="info">
  Note

  When **User Name or E-mail Address** and **Password** are not supplied, **Application Token** is required.
</Callout>

To generate the application token:

1. Log in to the Lookout MES Console as an administrator.
2. In the left navigation bar, navigate to **System `>` Application Keys**.
3. Click **Generate Key** in the upper-right.
4. Specify a label name, then click **Next**.
5. Copy the generated key clicking **Click to Copy Application Key to Clipboard**.
6. Copy the key from the clipboard into the adapter **Application Token** parameter.

<Callout icon="📘" theme="info">
  Note

  Copy the generated key immediately to the Axonius adapter, as you cannot access the key again.
</Callout>

12. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

13. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

14. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

15. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Lookout Mobile Endpoint Security" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lookout%20Mobile%20Endpoint%20Security.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Threat data time limit in hours**  *(optional, default: 720)* - Specify the threat data time limit in hours. The maximum value is 8760 hours (a year). The default is 720 (a month).
2. **Use API V2** - Select this option to use the version 2 of the API, which uses only the API key (without a username or password).
3. **Fetch Vulnerabilities from API V2** - Select this option to fetch vulnerabilities from `/mra/api/v2/os-vulns/android` and `/mra/api/v2/os-vulns/ios` and add them to devices with the same OS version.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Lookout API](https://api.lookout.com/).

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to fetch assets. You can use a local account with Read-Only access as long as it is identity-managed by Lookout and not by an external services provider.

<Image alt="LookoutConfig.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LookoutConfig.png" />