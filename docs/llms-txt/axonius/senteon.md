# Source: https://docs.axonius.com/docs/senteon.md

# Senteon

Senteon is a cybersecurity platform that offers vulnerability assessment and risk management solutions.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the following APIs:

* <Anchor label="Senteon Public API" target="_blank" href="https://app.senteon.co/api/public/swagger/index.html">Senteon Public API</Anchor>
* <Anchor label="Senteon Public Stats API" target="_blank" href="https://senteon.readthedocs.io/en/latest/changelog_public_api/">Senteon Public Stats API</Anchor>

### Permissions

The value supplied in [API Key](#required-parameters) must have “read-access” scope in order to fetch assets.

#### Supported From Version

Supported from Axonius version 8.0.2

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Bright Security server.

2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Senteon connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Senteon_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).