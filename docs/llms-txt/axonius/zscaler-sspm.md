# Source: https://docs.axonius.com/docs/zscaler-sspm.md

# Zscaler SSPM

Zscaler SSPM is a solution that provides continuous monitoring and remediation of SaaS application security configurations to enhance data protection and compliance.

### Asset Types Fetched

* Vulnerabilities, Users, Business Applications, SaaS Applications, Network Services, Network/Firewall Rules

## Before You Begin

### Permissions

The following permissions are required:

* The service administrator of Zscaler SSPM must assign you either the **3rd‑Party App Governance** permission group, or a custom role who has this permission. To assign this permission, in the ZIA Admin Portal, go to **Administration** ➔ **Service Management**.
  * Without the above permission, calls to `GET/apps/app` will succeed, but `apiActivities`, `risks`, and other governance‑specific sub‑objects will be omitted or returned empty.
* To fetch all fields properly, a read‑only access to the App Governance service is required.
  * Write‑level permissions aren’t required for GET operations, but might be required later to modify app classifications or consent.
* If you authenticate with an API Key + session login (`POST /authenticatedSession`), ensure the underlying user account is in the App Governance permission group.
* If you authenticate with OAuth, ensure to request scopes that include the `appGovernance.read` permission (or an equivalent permission) for your token.

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters - General

<Callout icon="📘" theme="info">
  Note

  The following parameters are required to fetch all assets **except for** Business Applications.
</Callout>

1. **Cloud Service domain** - The base domain for the API. It should contain an `http://` or `https://` prefix, and should not contain any specific endpoints.
2. **User Name** and **Password**  - The credentials for a user account that has the [Required Permissions](/docs/zscaler-sspm#permissions) to fetch assets.
3. **Cloud Service API Key** - An API Key associated with a user account that has the [Required Permissions](/docs/zscaler-sspm#permissions) to fetch assets.

### Required Parameters - Business Applications

1. **3rd Party App Governance API domain** and **3rd Party App Governance API Key** - See [Required Permissions](/docs/zscaler-sspm#permissions) for more details.

<Image alt="ZscalerSSPM_parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-05ENTDWR.png" />

<Callout icon="📘" theme="info">
  Note

  To fetch all asset types, provide all the required parameters mentioned above.
</Callout>

### Optional Parameters

The following parameters are optional for all asset types:

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Global Endpoints Config

**Daily Rate Limit** *(default 4999)* - the maximum number of requests that the adapter is allowed to make to the Zscaler API every day.

### Endpoints Config

1. **Fetch Users from Zscaler Users** -  Enable to fetch Users from the Zscaler Users endpoint.
2. **Fetch BusinessApplications of sub type All App Views from Apps from App View Endpoint** - Enable to fetch Business Applications from **all** App Views in Zscaler.
3. **Fetch BusinessApplications of sub type Specific App Views from Apps Using IDs from App View Endpoint** - Enable to fetch Business Applications from **specific** App Views in Zscaler. Expand the **App View IDs** row to provide the IDs of the App Views you want to fetch assets from.
4. **Fetch NetworkServices from Zscaler DNS Gateways** - Enable this to fetch Network Services.
5. **Fetch Firewall from Zscaler NAT Rules** - Enable this to fetch Network/Firewall Rules.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>