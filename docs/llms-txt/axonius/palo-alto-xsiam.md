# Source: https://docs.axonius.com/docs/palo-alto-xsiam.md

# Palo Alto Networks Cortex XSIAM

Palo Alto Networks Cortex XSIAM is an extended security intelligence and automation management platform that provides threat detection, investigation, and response capabilities across enterprise environments.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key/API Key ID

### APIs

Axonius uses the <Anchor label="Cortex XSIAM APIs" target="_blank" href="https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM-REST-API/Cortex-XSIAM-APIs">Cortex XSIAM APIs</Anchor>.

### Permissions

The user must have one of the following licenses:

* Cortex XSIAM Premium
* Cortex XSIAM Enterprise
* Cortex XSIAM Enterprise Plus

#### Supported From Version

Supported from Axonius version 8.0.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Palo Alto Networks Cortex XSIAM server.

2. **API Key** and **API Key ID**  - An API Key and API Key ID associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Palo Alto Cortex XSIAM connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/PaloAltoNetworksCortexXSIAM_AddConnection.png" />

### Optional Parameters

1. **Use Advanced Authentication Method** - Select this option to use advanced API keys to test authentication.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).