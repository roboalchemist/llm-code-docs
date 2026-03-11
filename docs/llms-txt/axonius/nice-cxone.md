# Source: https://docs.axonius.com/docs/nice-cxone.md

# NICE CXone

<br />

NICE CXone is a cloud-based customer experience platform that offers omnichannel routing, workforce optimization, and AI-driven analytics to enhance agent productivity and customer interactions.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the <Anchor label="NICE CXone UserHub API" target="_blank" href="https://developer.niceincontact.com/API/UserHubAPI#/">NICE CXone UserHub API</Anchor>.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 8.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the NICE CXone server.
2. **User Name** and **Password**  - The credentials for a user account that has permissions to fetch assets.
3. **Token Issuer URL** *(default: `http://localhost:22222`)* - Depending on your environment, select the Token issuer URL.

<Image alt="NICE CXone connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/NICECXone_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).