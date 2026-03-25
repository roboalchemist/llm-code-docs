# Source: https://docs.axonius.com/docs/trend-micro-deep-security.md

# Trend Micro Deep Security

Trend Micro Deep Security automatically shields servers, cloud environments, VDI systems, and applications from vulnerabilities through virtual patching.

The Trend Micro Deep Security adapter enables Axonius to fetch and catalog managed assets, providing visibility into their inventory details and protection status.

## Asset Types Fetched

* Devices
* Vulnerabilities
* Users
* SaaS Applications
* Networks

## Before You Begin

### Required Ports

* **For On-Premise deployments** - TCP port 4119 (default). Use this for traditional Trend Micro Deep Security Manager installed in your data center.
* **For SaaS / Cloud One deployments** - TCP port 443. Use this for **Trend Micro Cloud One – Workload Security** (formerly Deep Security as a Service) and AWS/Azure Marketplace deployments. You must manually change the Axonius default (4119) to 443 for these connections.

### Required Permissions

To connect the Axonius adapter to Trend Micro Deep Security, you need **Read-Only** (Auditor) access.

The recommended method is to create a dedicated API Key assigned to the built-in Auditor role. This ensures the adapter can fetch device and user data without having the ability to modify your security policies.

### APIs

Axonius uses the <Anchor label="Trend Micro Deep Security API" target="_blank" href="https://automation.trendmicro.com/deep-security/api-v20/">Trend Micro Deep Security API</Anchor>.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **On-Premise DeepSecurity Domain** - If you are using an on-premises deployment, enter the DeepSecurity domain. This value is also required when using a REST API Key. Alternatively, when working with Micro Trend Deep Security SaaS / Cloud One, enter the URL of the cloud platform: `https://cloudone.trendmicro.com`.

2. **Port** - If the port number is other than 4119 (default), specify the port number.

<Callout icon="💡" theme="warn">
  Important

  An authentication method selection is also required, even though these parameters are marked as optional. You must choose one of the following authentication methods:

  * **REST API** - Including domain + **REST API Key**.
  * **Legacy API** - Including **Username** + **Password** + **Tenant ID** or domain.

  For more information, see [Optional Parameters](/docs/trend-micro-deep-security#/optional-parameters).
</Callout>

<Image alt="Trend Micro Deep Security" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trend%20Micro%20Deep%20Security.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **Tenant ID** - If using a REST API Key, specify either the tenant (for cloud deployments) or domain (for on-premises).

3. **User Name** and **Password** *(**Legacy API - Not Recommended**)* - The user name and password for an account that has read access to the API. Fetch will not include all the data as the **Rest API Key** and should be used only if API Key is not applicable.

4. **REST API Key** *(**New API - Recommended**)* - API key for the REST API assigned for Axonius to consume Trend Micro Control Manager Automation APIs.

5. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

Specific advanced settings that relate to the Trend Micro Deep Security adapter are shown in the following figure.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Trend_Micro_DS_Advanced_Configuration.png" className="border" />

1. **Avoid Hostname duplications** - Select this option to avoid returning duplicate hostname fetches.
2. **Do not fetch devices with an inactive status** - Select this option to not fetch devices when the **Status** field is set to "inactive".
3. **Fetch Users** - Select this option to fetch users.
4. **Fetch policy details** - Enable this option to fetch policy details.
5. **Agent Version Control Profile ID** *(optional)* - Enter the agent version control profile ID.
6. **Fetch Network Assets** - Select this option to fetch network assets.
7. **Fetch Prevention Intrusion Rules** - Select this option to fetch Prevention Intrusion Rules. This will enrich the fetched devices with vulnerability information.
8. **Modify Device Serial Field** *(optional)* - Enter the specific attribute name from the Trend Micro source data that you want to map to the Axonius Serial Number field. By default, the adapter uses the `biosUUID` attribute name. You optionally enter `vmwareUUID`, `azureVMID`, or other names.