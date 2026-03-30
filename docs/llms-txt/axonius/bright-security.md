# Source: https://docs.axonius.com/docs/bright-security.md

# Bright Security

Bright Security is a dynamic application and API security testing platform that automates vulnerability detection, remediation, and validation throughout the software development lifecycle.

### Asset Types Fetched

* Vulnerabilities, SaaS Applications, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the Bright REST API. For more information, see the following:

* <Anchor label="REST API Overview" target="_blank" href="https://docs.brightsec.com/docs/about-bright-api">REST API Overview</Anchor>
* <Anchor label="Integrating with the Bright API" target="_blank" href="https://docs.brightsec.com/docs/integrating-with-the-bright-api">Integrating with the Bright API</Anchor>

### Permissions

Read permissions are required across projects, groups, issues, and comments modules.

#### Supported From Version

Supported from Axonius version 8.0.2

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Bright Security server.

2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Bright Security connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BrightSecurity_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).