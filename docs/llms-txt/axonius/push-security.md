# Source: https://docs.axonius.com/docs/push-security.md

# Push Security

Push Security is a cybersecurity platform that helps organizations secure their SaaS environments by monitoring user behavior, detecting misconfigurations, and guiding employees to fix security issues directly through browser-based prompts.

### Asset Types Fetched

* Users
* SaaS Applications
* Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Use an API key in the `x-api-key` header. API keys are managed in the Push admin console under **Settings** → **Create API Key**.

### APIs

Axonius uses the [Push Security REST API](https://pushsecurity.redoc.ly/rest-v1/).

### Permissions

The value supplied in [API Key](/docs/push-security#required-parameters) must have read-only permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Push Security server.
2. **API Key**  - An API Key associated with a user account that has the  Required Permissions to fetch assets.
3. **API Version** *(default: v1)* - Select the API Version you want to use to connect.

<Image alt="Push Security.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Push%20Security.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

* [Push Security - Add/Remove Group to User](/docs/push-security-alter-group-for-user)