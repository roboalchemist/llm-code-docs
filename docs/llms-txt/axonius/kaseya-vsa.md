# Source: https://docs.axonius.com/docs/kaseya-vsa.md

# Kaseya VSA

Kaseya VSA is a remote monitoring and management solution for remote control, discovery, patch management, and monitoring.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Kaseya Domain** *(required)* - The hostname of the Kaseya server. The format of this field is '\[instance].kaseya.net'.
2. **Authentication Method** *(required, default: Auto-select)* - Select the relevant authentication method. If not selected, 'Auto-select' will attempt to authenticate by  **Password** and **API Key**. The following authentication methods are available:
   * Auto-select
   * User Name and Password
   * User Name and API Key
3. **User Name** and **Password/API Key** *(required)* - The credentials for a user account that has the permissions to fetch assets. Use either a Password or an API Key, as selected in the Authentication Method. The user and password/API Key must be for a Kaseya VSA admin.
4. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Kaseya Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).
5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Kaseya Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Kaseya\_VSA](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Kaseya_VSA.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Disable paginated requests** - Select this option to avoid using paginated API requests. If cleared, Axonius will attempt to use paginated API calls to fetch data.
2. **Include assets missing agent data** - Select this option to include assets that are missing agent data.
3. **Enrich devices with software** *(default: true)* - By default this adapter enriches devices with software. Toggle off to not enrich devices with software.
4. **Enrich devices with group members** *(default: true)* - By default this adapter enriches devices with group members. Toggle off to not enrich devices with group members.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>