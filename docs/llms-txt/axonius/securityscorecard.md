# Source: https://docs.axonius.com/docs/securityscorecard.md

# SecurityScorecard

SecurityScorecard rates cybersecurity postures of corporate entities through completing scored analysis of cyber threat intelligence signals for the purposes of third party management and IT risk management.

## Asset Types Fetched

This adapter fetches the following types of assets:

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Domains_URLs.svg) Domains & URLs | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications (via [Advanced Settings](/docs/securityscorecard#advanced-settings))

*

<Callout icon="📘" theme="info">
  **Note**

  Any Device Findings that contain vulnerability data are fetched and parsed by the adapter as Vulnerable Software.
</Callout>

## Before You Begin

### APIs

Axonius uses the [SecurityScorecard API](https://securityscorecard.readme.io/reference).

### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **SecurityScorecard Domain** *(default: api.securityscorecard.io)* - The hostname or IP address of the SecurityScorecard server.
2. **Token**  An API Key associated with a user account that has permissions to fetch assets.

<Image alt="SecurityScorecard" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecurityScorecard.png" />

### Optional Parameters

1. **Portfolios**   Specify the portfolio ID or portfolio name for each portfolio that you want to fetch. If more than one value is specified, separate each value by a comma. If no portfolios are specified, all portfolios are fetched.
2. **Companies**  - Specify the scorecard identifier or company name for each company that you want to fetch. If more than one value is specified, separate each value by a comma. If no companies are specified, all companies belonging to the specified portfolios are fetched. If **Portfolios** and **Companies** parameters are both empty, all companies are fetched, regardless of their associated portfolio.
3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy**  - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
5. **HTTPS Proxy User Name**   - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password**  - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch IP's from portfolio** - Select whether to fetch IP addresses from a portfolio.
2. **Detect IP from URL** - Select this option to detect the IP address from the URL.
3. **Parse as URL asset or device asset** - From the dropdown, select either **Create only devices assets**, **Create only URL assets**, or **Create both assets**.
4. **Fetch domains from parent domain** - Select this option to fetch domains from parent domains.
   * **Filter domain names that contains these values** - Enter values to filter the fetched domains by.
5. **Parse last seen from Findings: Last Seen Time** - Select this option to parse the “Last Seen” value of the device from the latest “Findings: Last Seen Time”.
6. **Fetch SaaS applications** - Select this option to fetch all followed companies and their risk scores, which is available on the [SaaS Applications repository](/docs/saas-applications-repository) if found in the Axonius catalog.
   * To use this setting, you must have permission to access the risk score of the company, which means that the company must be added to a portfolio first.
7. **Fetch Domains & URLs Vulnerabilities** - Select this option to fetch vulnerabilities for Domains and URLs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />