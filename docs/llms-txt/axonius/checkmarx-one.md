# Source: https://docs.axonius.com/docs/checkmarx-one.md

# Checkmarx One

Checkmarx One is an application security platform that provides static and dynamic application security testing.

## Assets Types Fetched

* Aggregated Security Findings, Business Applications, SaaS Applications, Application Services

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret
* API Key

### APIs

Axonius uses the [Checkmarx One API](https://docs.checkmarx.com/en/34965-68772-checkmarx-one-api-documentation.html).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: US)* - From the dropdown select the hostname or IP address of the Checkmarx One server, depending on your region.

<Callout icon="📘" theme="info">
  Note

  The Checkmarx One regional mapping is as follows:

  * US - `https://iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * US2 - `https://us.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * EU - `https://eu.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * EU2 - `https://eu-2.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * DEU - `https://deu.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * Australia & New Zealand - `https://anz.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * India - `https://ind.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * Singapore - `https://sng.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`

  * UAE - `https://mea.iam.checkmarx.net/auth/realms/{tenant_account_name}/protocol/openid-connect/token`
</Callout>

2. **Authentication Method** - Select whether to authenticate via client credentials or API key.
3. **Client ID** and **Client Secret** - If the authentication method is via client credentials, specify the credentials for a user account that has the Required Permissions to fetch assets. For information about how to create these credentials, see [Creating an OAuth Client for Checkmarx One Integrations](https://docs.checkmarx.com/en/34965-188033-creating-an-oauth-client-for-checkmarx-one-integrations.html).

<Callout icon="📘" theme="info">
  Note

  These parameters are only displayed when the **Client Credentials Method** option is selected from the **Authentication Method** dropdown.
</Callout>

4. **API Key** - If the authentication method is via API key, specify the API key associated with a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  These parameters are only displayed when the **API Key Method** option is selected from the **Authentication Method** dropdown.
</Callout>

5. **Tenant Name** - Enter the name of the Tenant.

<Image alt="Checkmarx One" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Checkmarx%20One.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Global Endpoints Config

1. **Filter Scans using From Date: X Days in the past** *(default: 15)* - Enter a number to fetch scans only from the past specified number of days.
2. **Multi-Processing Workers** - Set your desired number of multi-processing workers. The default minimum is 1. The maximum is 3.

### Endpoints Config

1. Enrichment settings - You can choose to enrich Scans with the following data:
   * Results Summary *(default: true)*
   * Results *(default: true)*
2. **Scan Status List - applies context on the following endpoints: Scans** *(default: Completed)* - Select specific statuses from the menu so that only scans with these statuses will be fetched.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>