# Source: https://docs.axonius.com/docs/threatlocker.md

# ThreatLocker

ThreatLocker is a zero-trust platform.

This adapter fetches the All Computers report.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Choose API Version** *(default: Old (Deprecated))* - Select the API Version you want to use to connect, either **Old (Deprecated)** or **New**.

<Callout icon="📘" theme="info">
  Note

  When **New** API Version is selected, **Managed Org ID** is required.
</Callout>

2. **Host Name or IP Address** *(required, default: `https://api.g.threatlocker.com/`)* - The hostname or IP address of the ThreatLocker server.

<Callout icon="📘" theme="info">
  Note

  ThreatLocker has different API URLs depending on your region. Your specific regional API URL should be provided when you receive your API keys from ThreatLocker.
</Callout>

2. **Auth Key** *(required)* - Specify the user authentication key associated with a user account that has permissions to fetch assets. Contact ThreatLocker to obtain the API key. Axonius needs the "Report" API key for this parameter.

3. **Managed Org ID** *(only required for New API Version)* - The managed organization ID provided by ThreatLocker support.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ThreatLocker(2)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ThreatLocker(2).png" />

## Supported From Version

Supported from Axonius version 6.0