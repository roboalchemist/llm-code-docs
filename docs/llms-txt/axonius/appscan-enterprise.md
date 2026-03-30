# Source: https://docs.axonius.com/docs/appscan-enterprise.md

# HCL AppScan

HCL AppScan is an application security tool that provides vulnerability assessment and management.

### Use Cases the Adapter Solves

* **Detecting Application Vulnerabilities**: Identify and manage security risks within your business applications by aggregating scan results.
* **Verifying Security Coverage**:  Ensure that all critical business applications are being actively monitored and scanned by HCL AppScan.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/business_applications.svg) Business Applications

## Data Retrieved through the Adapter

## Before You Begin

**Ports**

* **TCP port 443**

**Authentication Method**

* **Basic**
  * Use a user name and password to authenticate. This method requires a local AppScan Enterprise account.
* **API Key**
  * Use an API Key ID and Key Secret to authenticate. This method is recommended when users authenticate to AppScan Enterprise via Single Sign-On (SSO), as SSO accounts cannot use Basic authentication with the API.

### APIs

Axonius uses the HCL AppScan Enterprise REST API. The following endpoints are called:

* `POST /ase/api/login` - Retrieves a session token (Basic authentication)
* `POST /ase/api/keylogin/apikeylogin` - Retrieves a session token (API Key authentication)

#### Supported From Version

Supported from Axonius version 6.1.62

### Setting Up HCL AppScan Enterprise to Work with Axonius

#### Generating an API Key ID and Key Secret

If you are using the **API Key** authentication method, generate a Key ID and Key Secret in HCL AppScan Enterprise for the user account that Axonius will use to connect.

1. Log in to HCL AppScan Enterprise as the user that will be used for the Axonius connection.
2. Select the 3-line menu in the top left corner.
3. Select **AppScan Enterprise REST APIs**.
4. On the REST APIs page, generate a new API key.
5. Copy the **Key ID** and **Key Secret** values. Store them securely — the Key Secret is only displayed once.

For more information, see [How to generate an API key and secret for AppScan Enterprise](https://support.hcl-software.com/csm?id=kb_article\&sysparm_article=KB0089286) in the HCL Software Knowledge Base.

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **HCL AppScan**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the HCL AppScan server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Authentication Method** - Select the authentication method.

<Tabs>
  <Tab title="Basic">
    1) **User Name** - The user name of the AppScan Enterprise account.
    2) **Password** - The password of the AppScan Enterprise account.
  </Tab>

  <Tab title="API Key">
    1. **Key ID** - The API Key ID generated in HCL AppScan Enterprise. See [Generating an API Key ID and Key Secret](#generating-an-api-key-id-and-key-secret) above.
    2. **Key Secret** - The Key Secret associated with the Key ID. See [Generating an API Key ID and Key Secret](#generating-an-api-key-id-and-key-secret) above.
  </Tab>
</Tabs>

1. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="HCL AppScan connection screen" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/HCLAppScan.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

1. **Fetch BusinessApplications from Applications Endpoint** (default: true) - By default this adapter fetches business applications from the Applications Endpoint. Toggle off to not fetch business applications from the Applications Endpoint. When this setting is enabled, the setting below may be configured.
   * **Enrich Applications Endpoint with Application Components Endpoint** - Toggle on to enrich the Applications Endpoint with the Application Components Endpoint. When this setting is enabled, the setting below may be configured.
     * **Enrich Application Components Endpoint with Recommendations Endpoint** - Toggle on to enrich the Application Components Endpoint with the Recommendations Endpoint.
2. **Fetch RepositoryVulnerabilities from Issues Endpoint** - Toggle on to fetch repository vulnerabilities from the Issues Endpoint. When this setting is enabled, the setting below may be configured.
   * **Enrich Issues Endpoint with Recommendations Endpoint** - Toggle on to enrich the Issues Endpoint with the Recommendations Endpoint.

<br />