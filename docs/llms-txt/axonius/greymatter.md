# Source: https://docs.axonius.com/docs/greymatter.md

# ReliaQuest GreyMatter

ReliaQuest GreyMatter is a security operations platform that provides unified threat detection, investigation, and automated response across cloud, endpoint, and network telemetry.

### Asset Types Fetched

* Devices, Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the <Anchor label="GreyMatter API" target="_blank" href="https://apidocs.myreliaquest.com/#intro">GreyMatter API</Anchor>.

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 8.0.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ReliaQuest GreyMatter server.
2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

<Image alt="ReliaQuest GreyMatter connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ReliaQuest_GreyMatter_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).