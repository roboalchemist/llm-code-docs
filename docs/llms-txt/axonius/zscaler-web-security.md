# Source: https://docs.axonius.com/docs/zscaler-web-security.md

# Zscaler Web Security

Zscaler Web Security is a secure Internet and web gateway service that stops malware, advanced threats, phishing, browser exploits, malicious URLs, botnets, and more.

This adapter is compatible with Zscaler Internet Access (ZIA).

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Users, SaaS Applications, Network/Firewall Rules

## Before You Begin

### Authentication Methods

You can authenticate this adapter using either of the following methods:

* API Key
* OAuth 2.0 authentication (ZIdentity)

<Callout icon="❗️" theme="error">
  Note

  This adapter won't be able to fetch Devices when using OAuth 2.0 authentication.
</Callout>

See [Connecting the Adapter in Axonius](/docs/zscaler-web-security#connecting-the-adapter-in-axonius) for the connection parameters required for each authentication.

### Required Permissions

**General**

* Dashboard Access: View Only
* User Names: Visible
* Reporting Access: Full
* Device Information: Visible
* Auditor Logs: Read-only
* Users: Read-only
* Client Connector Portal: Read-only

**Reporting Data**

* Security: View Only
* Web Data: View Only
* Firewall: View Only
* URL Categories: View Only

#### Specific Permissions for fetching SaaS Applications data

For detailed instructions, see the [Zscaler documentation about Adding Admin Roles for Internet & SaaS Access](https://help.zscaler.com/zia/adding-admin-roles). Click **See image** under each permission section to see how they look in the Zscaler portal.

#### Specific Permissions for fetching Devices

1. In Zscaler, navigate to **Administration** > **Role Management** > **Roles**.
2. Select the **Traffic Forwarding** tab and add the permissions listed in the following image:

<Image align="center" alt="TrafficForwardingPermissions" width="700px" src="https://files.readme.io/a9b32887aba27f28d6fe6862022e463a4fb2182af68389fb37012ce6bd18b516-image.png" />

## Setting Up ZScaler Web Security to Work with Axonius

To authorize using the API Key, follow these steps:

### Create a Local Admin Account

1. Log into the ZScaler Admin Portal.
2. Navigate to **Administration** > **Role Management** > **Administrator Management**.
3. Create a new local administrator (must be local, not SAML/SSO-linked).
4. Set a strong password.

### Assign the Role With the Required Permissions

1. Navigate to **Administration** > **Role Management** > **Roles**.
2. Select the **Administration Controls** tab.
3. Configure the permissions listed in this image:

   <Image align="center" alt="AdministrationControlsPermissions" width="700px" src="https://files.readme.io/111aa5fd0c50782fefc5e5ae958630734620339fd9f797f5d9fcc5511dcb0df0-image.png" />
4. Continue to assign the relevant permissions based on the asset types you want to fetch, as detailed in [Required Permissions](https://docs.axonius.com/docs/zscaler-web-security#required-permissions)  and the [Zscaler documentation](https://help.zscaler.com/zia/adding-admin-roles) (for SaaS permissions).

### Retrieve the API Key

1. Navigate to **Administration** > **API Key Management**.
2. Copy the existing API key, or generate a new one.
3. Store the key in a secure place - it is required to connect the adapter.

## Connecting the Adapter in Axonius

### Required Parameters - General

1. **Zscaler Domain** *(default: admin.zscalerthree.net)* - Specify the Zscaler cloud name that was provisioned for your organization. For example:

   * admin.zscalerbeta.net
   * admin.zscalerone.net
   * admin.zscalertwo.net
   * admin.zscaler.net
   * admin.zscloud.net
   * admin.zscalerdomain.net
   * mobileadmin.zscalerdomain.net
   * mobile.zscalerdomain.net

   For more details, see 'Retrieve your base URI and API key' section under [Zscaler API - Getting Started](https://help.zscaler.com/zia/api-getting-started).

<Callout icon="📘" theme="info">
  Note

  Your organization may use a Zscaler domain for Single Sign On (SSO) that is different from the Base URL. This domain may need to be accounted for in firewall rule configurations to allow for a successful connection.
</Callout>

2. **Auth Method** - Select either API Key (default) or ZIdentity.

<Tabs>
  <Tab title="API Key Authentication">
    1) **User Name** and **Password** - The user name and password used to connect to Zscaler Web Security.
    2) **API Key** - Your organization's API key. The API key is mandatory to fetch user data from Zscaler.
       For more details about adding a new API key, see [Zscaler documentation - About API Key Management](https://help.zscaler.com/zia/about-api-key-management).

    ![ZscalerWebSecurityAddConnection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/zscaler%20web%20security%20connection.png)
  </Tab>

  <Tab title="OAuth 2.0 (ZIdentity) Authentication">
    1. **Client ID** and **Client Secret** - The client credentials sent in the request that were verified by ZIdentity, using the client registration details configured in the ZIdentity Admin Portal. See [OAuth 2.0 Client Registration](https://www.rfc-editor.org/rfc/rfc6749#section-2) for more details on the creation and syntax of these parameters.
    2. **Vanity Domain** - The domain name used by your organization. Only enter the subdomain. For more information, see the 'Accessing OneAPI' section in the [ Zscaler Getting Started with OneAPI docs](https://help.zscaler.com/oneapi/getting-started).

    For general information on OAuth 2.0 (ZIdentity) Authentication, see [Zscaler OneAPI Help](https://help.zscaler.com/oneapi/getting-started-oneapi).

    ![ZscalerWebSecurityOAuthAddConnection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/zscaler_auth.png)
  </Tab>
</Tabs>

### Optional Parameters

1. **Company ID** - Enter the Company ID. This parameter is required if the **Fetch Zscaler Client Connector enrolled devices**[advanced setting](/docs/zscaler-web-security#advanced-settings) is selected.
2. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Zscaler Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Zscaler Domain**.

#### Optional File Upload

When fetching SaaS Application, you have the option to fetch these applications based on logs listed in a remote location. To do so, select the **File Source** from the **Upload File** dropdown and provide the relevant parameters. For more information, see [connection parameters for the Custom Files adapter](https://docs.axonius.com/docs/custom-files#parameters) and the list of available [file sources](https://docs.axonius.com/docs/custom-files#file-sources).

<Callout icon="📘" theme="info">
  **Note**

  To fetch logs from a remote location, you must enable the **Enable real-time asset updates (Zscaler Nanolog Streaming Service)** advanced setting.
</Callout>

<Image align="center" alt="UploadFileDropdown" width="300px" src="https://files.readme.io/82b6264afdab41c9fd47c4bcf1508ee3c048d1f9ca254f1e1d83b420215baad3-image.png" />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

#### Selecting Asset Types

In Advanced Settings, at the top of the Advanced Configuration, you can choose asset types that are relevant to specific advanced configurations.

1. From the dropdown, select one or more asset types.<br />
   ![AssetTypeDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Zscaler%20Web%20Security%20Advanced%20Setting%20asset%20type%20dropdown.png)
2. The relevant advanced configurations are displayed.
3. Next to certain configurations, you can find a small ![TooltipIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tooltip%20icon\(1\).png)  icon. Hover over the icon to see more information.
4. The Advanced Configuration page is divided into sections, which can be collapsed to make it easier to navigate.

#### Data Enrichment

1. **Fetch users** *(default: true)* - Select this option to fetch users data. Each user is added as a user asset in Axonius.
2. **Enrich devices service status** - Select this option to enrich device information with Service Status data.
3. **Add last used users information for duplicated devices (if "Avoid hostnames duplications" is enabled)** - Select this option to add the last used users information for duplicated devices. This is applicable only when “Avoid hostnames duplications” is used.
4. **Add Device Manufacturer Serial for Zscaler devices** - Select this option to extract the device manufacturer serial number from the UDID and add it to the device.
5. **Discover Application Users** *(default: true)* - By default this adapter fetches SaaS application users. Clear this option to not fetch SaaS application users.

#### Fetch and Parse

6. **Ignore duplicated MAC addresses** - Select this option to ignore MAC addresses that are associated with more than one device fetched from Zscaler.
7. **Avoid hostnames duplications** - Select this option to avoid returning duplicate hostname fetches.
8. **Fetch Zscaler Client Connector enrolled devices** - Select this option to fetch enrolled devices from the Zscaler Client Connector.

<Callout icon="📘" theme="info">
  Note

  When **Fetch Zscaler Client Connector enrolled devices** is selected, you must enter a value in the **Company ID** parameter.
</Callout>

9. **Fetch Firewalls** - Select this option to fetch firewall policies data.
10. **Filter SaaS Applications data by timeframe** - Filter the SaaS Apps report by the selected time period.
11. **Ignore SaaS Applications without users** - Select this option to not fetch SaaS applications not assigned to any user.
12. **Ignore SaaS Applications Repository and parse all applications** - Select this option to fetch all applications even if they are not in the Axonius SaaS Applications Repository.
13. **Filter out applications by name** - Enter a name to filter out applications.
14. **Filter out applications by category** - Enter a category to filter out applications.
15. **SaaS Applications Source** - Select the source from with to fetch SaaS Applications: Shadow IT Report, Inferred by Insight Logs, or Both.
16. **Include Linux devices** - Select this option to include devices that have the Linux operating system on the device fetch.
17. **Device Types to be Fetched** - Filter the devices you want to fetch by registration status. Select between All states except Removed, Registered (default), Removal Pending (default), Unregistered, Removed, and Quarantined.
18. **Enable real-time asset updates (Zscaler Nanolog Streaming Service)** - Enable this if you want to fetch Zscaler Logs from a remote location.

#### Advanced Configuration

16. **RateLimit (requests/hour)** *(optional, default: 700)* - Enter the maximum rate of requests per hour by Axonius to the Zscaler server.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[Zscaler - Block URLs](/docs/zscaler-block-url)

[Zscaler - Delete Users](/docs/zscaler-delete-user)

[Zscaler - Add or Remove URL to/from Category](https://docs.axonius.com/axonius-help-docs/docs/zscaler-add-remove-url-category)

[Zscaler - Add or Remove Custom URLs to/from Category](https://docs.axonius.com/axonius-help-docs/docs/zscaler-add-remove-custom-url-category)