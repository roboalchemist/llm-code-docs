# Source: https://docs.axonius.com/docs/detectify.md

# Detectify

Detectify is an external attack surface management platform that provides continuous asset discovery and dynamic automated security testing to identify vulnerabilities across web applications and domains.

The Detectify adapter enables Axonius to fetch and catalog comprehensive information about your organization's internet-facing assets and security assessments to provide visibility into your external digital footprint.

## Asset Types Fetched

* Devices
* Vulnerabilities
* SaaS Applications
* Domains & URLs

## Data Retrieved through the Adapter

The adapter retrieves information to provide visibility into your publicly accessible assets. The retrieved data for each asset type may include:

* **Devices** - Data such as IP address details and geolocation information (country, continent).
* **Vulnerabilities** - Data such as finding titles, severity levels, and industry-standard risk scores (CVSS, CWE).
* **SaaS Applications** - Data such as breach information related to compromised assets and associated policy names.
* **Domains & URLs** - Data such as asset names, discovery status, and various lifecycle timestamps.

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* API Key

### Required Permissions

The adapter connection requires an API key associated with an account that has permissions to enumerate assets and IPs, and to retrieve vulnerability and breach data. See [Generating the API Key](/docs/detectify#generating-the-api-key).

### APIs

Axonius uses the <Anchor label="Detectify v2" target="_blank" href="https://developer.detectify.com/v2">Detectify v2</Anchor> and <Anchor label="Detectify v3" target="_blank" href="https://developer.detectify.com/">Detectify v3</Anchor> APIs to retrieve asset data.

<Callout icon="💡" theme="warn">
  Important

  The Detectify v3 API requires a specific API key separate from the Detectify v2 API. To fetch all supported data types across both endpoint versions, you must configure two separate connections using their respective keys.
</Callout>

### Generating the API Key

1. Log in to your <Anchor label="Detectify account" target="_blank" href="https://detectify.com/login">Detectify account</Anchor> and navigate to the **Team** menu.
2. Select **Account Settings** and go to the **API-Keys** tab.
3. Click **Generate API Key**.
4. Enter a name and optional description for the key, then click **Generate API-Key** again.
5. Copy and securely store the API key, as it will only be displayed once.
6. In **API Setting Permissions**, ensure that permissions for listing assets and reading vulnerabilities are enabled.

### Supported from Version

This adapter is supported from Axonius version 8.0.11.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the host name or IP address of the Detectify server.
2. **API Key** - Enter the API key generated for the specific API version (v2 or v3) you are connecting with.

<Image align="center" alt="Detectify adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Detectify_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />