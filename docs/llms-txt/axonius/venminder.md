# Source: https://docs.axonius.com/docs/venminder.md

# Venminder

Venminder is a third-party risk management tool that helps manage and monitor the entire vendor lifecycle, including on/off-boarding, contract tracking, and risk assessment.

### Asset Types Fetched

* SaaS Applications, Tickets, Organizational Units

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID / Client Secret

### APIs

Axonius uses the [Venminder API](https://developers.venminder.com/318218fb2/p/9845ac-the-venminder-api).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 6.1.33.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Venminder server.

2. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets. For more information on obtaining these credentials, see [Getting Started](https://developers.venminder.com/318218fb2/p/036ae9-getting-started).

![Venminder](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Venminder.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).