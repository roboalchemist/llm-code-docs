# Source: https://docs.axonius.com/docs/invicti.md

# Invicti

Invicti (formerly Netsparker) is DAST and IAST vulnerability scanning for web applications.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications, Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required, default: `https://www.netsparkercloud.com`)* - The hostname or IP address of the Invicti server.

2. **User ID** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   **To obtain the Client ID and API Token**

   1. Log in to Invicti Enterprise.
   2. Select **\[Your Name]** (top right of the window) `>` **API Settings**.
   3. In the **Current Password** field, enter your current password.
   4. Select **Submit** to view your User ID and API Token.

   Further details are available in [Invicti API Overview](https://www.invicti.com/support/api-overview/).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Invicti" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Invicti.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** - Select whether to fetch vulnerabilities information from Invicti.
2. **Fetch vulnerabilities with CVE ID**  - Toggle on to fetch vulnerabilities with associated CVEs. This setting is only relevant when Fetch vulnerabilities is selected.
3. **Parse URLs also as Devices** - By default Axonius fetches device assets as both URLs and devices. Clear this option to parse assets only as URLs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Invicti Enterprise Web API](https://www.netsparkercloud.com/docs/index#!/Websites/Websites_List).

## Supported From Version

Supported from Axonius version 4.6

## Troubleshooting

Invicti doesn't support partial API calls. To update any object, for example, a scan profile object, do the following:

1. Make a GET request for the scan profile you want to update.
2. Update parameters.
3. Make a POST request to update the scan profile with new parameters.