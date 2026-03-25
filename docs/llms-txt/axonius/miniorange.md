# Source: https://docs.axonius.com/docs/miniorange.md

# Mini Orange Identity Provider

Mini Orange Identity Provider is a cloud-based Identity and Access Management (IAM) solution that helps organizations manage and secure their digital identities,

### Asset Types Fetched

Users,  Groups

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

Customer Key and API Key

### APIs

Axonius uses the [MiniOrange User API](https://developers.miniorange.com/docs/idp/api/user-api-guide).

### Permissions

View Users and View Groups permissions are required.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Mini Orange Identity Provider server.

2. **Customer Key** and **API Key**  - The credentials associated with a user account that has Permissions to fetch assets.

<Image align="center" alt="MiniOrange connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MiniOrange.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />