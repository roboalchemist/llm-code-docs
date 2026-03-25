# Source: https://docs.axonius.com/docs/digitalocean.md

# DigitalOcean

DigitalOcean is a cloud hosting provider that offers cloud computing services and Infrastructure-as-a-Service (IaaS).

<br />

### Asset Types Fetched

* Devices, Compute Services, Load Balancers, Network Services

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the <Anchor label="DigitalOcean REST API Version 2.0" target="_blank" href="https://docs.digitalocean.com/reference/api/api-reference/">DigitalOcean REST API Version 2.0</Anchor>.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 5.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the DigitalOcean server.

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For more information see [Authentication](https://docs.digitalocean.com/reference/api/api-reference/#section/Authentication).

<Image alt="DigitalOcean_Adapters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DigitalOcean_Adapters.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).