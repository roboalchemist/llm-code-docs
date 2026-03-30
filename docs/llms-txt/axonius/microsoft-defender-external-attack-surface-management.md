# Source: https://docs.axonius.com/docs/microsoft-defender-external-attack-surface-management.md

# Microsoft Defender External Attack Surface Management (Defender EASM)

Microsoft Defender External Attack Surface Management discovers and maps the digital attack surface and provides an external view of a company’s online infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications
* Domains and URLs
* Certificates

## Parameters

1. **Azure Tenant ID** *(required)* - The Microsoft Entra ID (Azure AD) ID.

2. **Azure Client ID** *(required)* - The Application ID of the Axonius application.

3. **Azure Subscription ID** *(required)* - The Microsoft Entra ID (Azure AD) Subscription ID.

4. **Azure Client Secret** *(required)* - Specify a non-expired key generated from the new client secret.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![attack surface parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Microsoft%20Defender%20External%20Attack%20Surface%20Management%20\(Defender%20EASM\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Devices of sub type Pages from EASM Pages** *default: disabled* - Select this option to fetch Page devices from EASM pages.
* **Fetch Devices of sub type Hosts from EASM Hosts** *default: disabled* - Select this option to fetch Host devices from EASM hosts.
* **Fetch Devices of sub type IP Addresses from EASM IP Addresses** *default: disabled* - Select this option to fetch IP addresses from EASM pages.
* **Fetch URLs of sub type URLs from EASM Pages** *default: enabled* - Select this option to fetch URLs from EASM pages.
* **Fetch URLs of sub type Domains from EASM Domains** *default: disabled* - Select this option to fetch domains from EASM domains.
* **Fetch Certificate from EASM SSL Certificates** *default: disabled* - Select this option to fetch certificates from EASM SSL certificates.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the Adapter Configuration tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Microsoft Defender EASM REST API](https://learn.microsoft.com/en-us/rest/api/defenderforeasm/).

## Required Permissions

To connect to Microsoft Entra ID (Azure AD), you need to create a **Designated Axonius application** in the Microsoft Azure Portal and grant it **read-only permissions**. All required credentials will be given once an application is created. For more details, see [Creating an application in the Microsoft Azure Portal](/docs/microsoft-azure#creating-an-application-in-the-microsoft-azure-portal).

To assign a Reader role to the application you use to connect to Axonius, on your Azure portal:

1. Navigate to **Subscriptions**.
2. Select the subscription used in the adapter configuration.
3. Select **Access Control (IAM)**.
4. Select **Add** `>` **Add Role Assignment** to add a new permission.
5. Select the **Reader** permission and click **Next**.
6. On the **Members** screen, click **Select Members**.
7. Select the Axonius application and click **Review + assign**.

Apply the same permissions as are used on the [Microsoft Entra ID (Azure AD) adapter](/docs/microsoft-azure-active-directory-ad#set-permissions). The required permissions are as follows:

* AuditLog.Read.All
* Directory.Read.All
* Application.Read.All

## Supported From Version

Supported from Axonius version 6.0