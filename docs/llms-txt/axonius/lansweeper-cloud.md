# Source: https://docs.axonius.com/docs/lansweeper-cloud.md

# Lansweeper Cloud

Lansweeper Cloud federates data from all local Lansweeper discovery instances into a single source of truth.

The Lansweeper Cloud adapter provides Axonius with visibility into your publicly accessible assets, including device, vulnerability, software, and SaaS application data.

## Asset Types Fetched

* Devices
* Vulnerabilities
* Software
* SaaS Applications

## Before You Begin

### Required Ports

* TCP port 8080

### Authentication Methods

* API Token

### Required Permissions

The value supplied in [Token](#parameters) must be associated with credentials that have Oauth Client App permissions to fetch assets.

### APIs

Axonius uses the [Lansweeper V2 API](https://api.lansweeper.com/api/v2) to retrieve asset data.

### Supported From Version

This adapter is supported from Axonius version 4.7.

### Generating the API Token

1. In Lansweeper, from the bottom-left corner, select **Settings**.
2. Select **Developer tools** `>` **Add new API client**.
3. Select **Personal Access Token**.
4. Enter an API client name.
5. Optionally, enter a description and identifying image.
6. To use one of Lansweeper marketplace integrations, select it from the **Integrations** menu. Otherwise, select **Other** and enter a custom integration name.
7. Select an expiration date for the token.
8. Select which sites you want to grant API access to.
9. Copy the generated token and paste it into the Axonius **Token** parameter.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Lansweeper Cloud server that Axonius can communicate with via the [Required Ports](#required-ports). For example: `https://api.lansweeper.com`

2. **Token** - Enter the API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For instructions, see [Generating the API Token](/docs/copy-of-lansweeper-cloud#generating-the-api-token).

<Image align="center" alt="Lansweeper Cloud adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Lansweeper_Cloud_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Ignore Device Types** *(optional)* - Enter one or more comma-separated device types to ignore.
2. **Ignore devices with no last seen** *(default: false)* - Select this option to not fetch devices if they do not have a last seen timestamp.
3. **Fetch Vulnerabilities** *(default: false)* - Select this option to fetch vulnerabilities. This setting requires your Lansweeper account to have the **View Vulnerabilities** permission applied.
4. **Number Of Vulnerabilities Per Page** *(default: 100)* - Set how many vulnerabilities you want to include in each page to control the limit in the vulnerability fetch request.
5. **Parse OS data** *(default: true)* - Clear this option to disable OS data parsing, or keep it selected to enable the parsing.
6. **Export Status Timeout (Minutes)** *(default: 90)* - Enter the maximum duration (in minutes) for export status checks before a timeout occurs.