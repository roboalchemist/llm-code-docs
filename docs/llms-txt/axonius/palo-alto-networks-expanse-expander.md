# Source: https://docs.axonius.com/docs/palo-alto-networks-expanse-expander.md

# Palo Alto Networks Cortex Xpanse

Palo Alto Networks Cortex Xpanse (Palo Alto Networks Expanse Expander) discovers, monitors, and tracks Internet Assets automatically, anywhere in the world, and reduces risks and exposures.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, SaaS Applications, Domains & URLs, Compute Services, Certificates

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key or Client ID/Client Secret for API Version 1
* Standard API Key/Advanced API Key for API Version 2

### APIs

Axonius uses the <Anchor label="Cortex Xpanse API" target="_blank" href="https://docs-cortex.paloaltonetworks.com/r/Cortex-Xpanse-REST-API/Cortex-Xpanse-API-Overview">Cortex Xpanse API</Anchor>.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

Select the **API Version** you want to use to connect, either **API Version 1** or **API Version 2**. Each version requires different connection parameters.

#### API Version 1

![Palo Alto Networks Cortex Xpanse API Version 1 connection screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/PaloAltoNetworksCortexXpanseAPIVersion1__AddConnection.png)

1. **Host Name or IP Address** *(default: `https://expander.expanse.co`)* - The hostname or IP address of the Palo Alto Networks Cortex Xpanse server.

2. **Authentication Method** - Select the authentication method, either **API Key** or **Client ID and Client Secret**.
   1. **API Key** - An API Key associated with a user account that has permissions to fetch assets.
   2. **Client ID** and **Client Secret** - The credentials for a user account that has permissions to fetch assets. To obtain these credentials, see [Acquiring a Client ID and Client Secret](https://docs.axonius.com/docs/palo-alto-networks-cortex-xpanse#/acquiring-a-client-id-and-client-secret).

<br />

#### API Version 2

![Palo Alto Networks Cortex Xpanse API Version 2 connection screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/PaloAltoNetworksCortexXpanseAPIVersion2__AddConnection.png)

1. **Host Name or IP Address** *(default: `https://expander.expanse.co`)* - The hostname or IP address of the Palo Alto Networks Cortex Xpanse server.
2. **Authentication Method** - Select the authentication method, either **Standard API Key** or **Advanced API Key**.
   1. **Standard API Key** - An API Key, with a standard security level, that is associated with a user account that has permissions to fetch assets.
   2. **Advanced API Key** - An API Key, with an advanced security level, that is associated with a user account that has permissions to fetch assets.
3. **API Key ID** - If you select API v2 you need to add both an API Key and the API ID. In addition, make sure you enter the correct domain for your API version.

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Acquiring a Client ID and Client Secret

1. Open **Palo Alto Networks Cortex Xpanse**.

2. From the **Setting** tab, select **Client Credentials** in the left navigation pane.

3. Click **Generate Credentials**. The Client Credentials/Add New page is displayed.
   **Note:** Each user is limited to 10 client credentials at any one time.

4. Specify the Client Name. Your client name is automatically prefixed with “xpanse*expander*”.
   **Note:** Client names must be in lowercase.

5. Enter a description of the purpose of this credential.

6. Click **Generate Credentials**. The Client Identifier and Client Secret are displayed. Write the values for future reference.

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Categorize devices** - Select this option to categorize devices into different asset categories using their asset type.
2. **Fetch vulnerabilities** - Select this option to fetch vulnerabilities.
3. **Fetch confirmed vulnerabilities from external services** - Select this option to fetch confirmed vulnerabilities from the Service endpoint (`get_external_services`), which contains vulnerability data that is unavailable through the regularly-used Assets endpoint.
4. **Fetch Users** - Select this option to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Palo Alto Networks Cortex Xpanse - Tag Assets](/docs/expanse-expander-tag-assets)