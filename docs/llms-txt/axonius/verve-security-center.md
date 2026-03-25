# Source: https://docs.axonius.com/docs/verve-security-center.md

# Verve Security Center

Verve Security Center is a cybersecurity platform that offers comprehensive protection for industrial control systems.

## Use Cases the Adapter Solves

The Verve Security Center adapter could be used in various use cases, including:

* **Build a Unified IT/OT Inventory** - Aggregate the Verve Security Center OT asset data with IT asset data from other configured adapters.
* **Prioritize OT Vulnerabilities** - Correlate Verve's vulnerability data with business context from other data sources (for example: CMDB, network) for risk-based prioritization.
* **Audit OT Security Policy Compliance** - Query Verve asset data to identify devices that are non-compliant with defined security policies or configuration baselines.
* **Configure Automated Workflows** - Use Verve data as a condition to trigger defined actions in the Enforcement Center, such as creating a help desk ticket, adding an asset tag, or sending a notification.

## Asset Types Fetched

* Devices
* Vulnerabilities
* SaaS Applications

## Data Retrieved through the Adapter

The following data is retrieved through the Verve Security Center adapter:

* **OT/ICS Asset Details** - Device type (for example: PLC, HMI, controller), manufacturer, model number, and serial number.
* **Network Details** - IP address, MAC address, and network segment.
* **Configuration Data** - Firmware version and operating system.
* **Vulnerability Data** - Associated vulnerabilities (CVEs) and risk scores.
* **SaaS Applications** -  Information regarding SaaS applications.

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

* **User Credentials** - A Username and Password for the Verve user account.
* **API Key Credentials** - An API Key that is associated with the Verve user account.

### Required Permissions

The Verve Security Center adapter requires a user account within the Verve Security Center platform that has **Read-Only** permissions.

### APIs

The Verve Security Center adapter uses the Verve Security Center REST APIs.

<Callout icon="📘" theme="info">
  Note

  The adapter does not use a single, simple API but rather a collection of HTTP-based endpoints, which are configurable in the adapter settings.
</Callout>

### Supported from Version

Supported from Axonius version 6.1.55.0.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Verve Security Center server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Authentication Method** - Select an authentication method, either **User Credentials** (default) or **API Key Credentials**.
   * **User Credentials** -
     * **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.
   * **API Key Credentials** -
     * **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Verve_Required.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - Enter the user name for connecting to the value supplied in **Host Name or IP Address** through the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

Specific advanced settings that relate to the Verve Security Center adapter are shown in the following figure. These advanced settings enable you to configure the specific API methods used for data retrieval based on network access and environment size.

<Image align="center" alt="Verve Security Center advanced configuration" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Verve_Advanced_Configuration.jpg" className="border" />

<Callout icon="💡" theme="warn">
  Important

  Enable only the set of toggles that matches your specific configuration to prevent redundant data fetching.
</Callout>

### Direct Connection Options

Use these options when the Verve Elastic Search instance is directly accessible.

1. **Fetch Devices of sub type Device (ES direct paginated) from Assets Search (Paginated)** - Fetches device assets directly from Elastic Search using pagination. This is the default setting and is recommended for environments with fewer than 10,000 assets.
2. **Enrich Assets Search (Paginated) with Vulnerabilities Search (Paginated)** - Enriches the paginated asset list with vulnerability data using a paginated search method.
3. **Enrich Assets Search (Paginated) with Vulnerabilities Search** - Enriches the paginated asset list with vulnerability data using the standard Point-in-Time (PIT) search method.
4. **Fetch Devices of sub type Device (ES direct) from Assets Search** - Fetches device assets directly from Elastic Search using a PIT snapshot. This method is recommended for environments with more than 10,000 assets.
5. **Enrich Assets Search with Vulnerabilities Search** - Enriches assets fetched via the PIT method with vulnerability data.

### Kibana Console Proxy Options

Use these options only if the Verve Elastic Search instance is not directly accessible and connections must be routed through the Kibana Console Proxy.

1. **Fetch Devices of sub type Device (ES via Kibana Console Proxy Paginated) from Assets Search (Paginated via Kibana Console Proxy)** - Fetches device assets via the Kibana Proxy using pagination. Recommended for proxy connections with fewer than 10,000 assets.
2. **Enrich Assets Search (Paginated via Kibana Console Proxy) with Vulnerabilities Search (via Kibana Console Proxy)** - Enriches the paginated proxy asset list with vulnerability data via the proxy.
3. **Fetch Devices of sub type Device (ES via Kibana Console Proxy) from Assets Search (via Kibana Console Proxy)** - Fetches device assets via the Kibana Proxy using a PIT snapshot. Recommended for proxy connections with more than 10,000 assets.
4. **Enrich Assets Search (via Kibana Console Proxy) with Vulnerabilities Search (via Kibana Console Proxy)** - Enriches the PIT proxy asset list with vulnerability data via the proxy.