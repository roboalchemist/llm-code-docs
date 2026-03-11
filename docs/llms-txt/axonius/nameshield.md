# Source: https://docs.axonius.com/docs/nameshield.md

# Nameshield

Nameshield is a registrar and domain protection service that provides DNS management, domain monitoring, recovery, SSL certificates and DMARC security.

### Asset Types Fetched

* Domains & URLs

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Nameshield OpenAPI](https://docs.nameshield.net/docs/openapi/dns/8-deb-4-b-8-f-56-ce-8-a-8-c-774-c-4-aa-22-ec-1-cef-4/).

### Permissions

Consult with your vendor for the exact permission to fetch the objects.

#### Supported From Version

Supported from Axonius version 7.0.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Nameshield server.
2. **API Key**  - An API Key associated with a user account that has permissions to fetch assets.

![Nameshield.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nameshield.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).