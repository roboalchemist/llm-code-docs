# Source: https://docs.axonius.com/docs/medimizer-cloud.md

# MediMizer Cloud

MediMizer Cloud is a healthcare asset management tool that offers equipment tracking and maintenance scheduling.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Access Token

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 8.0.3

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the MediMizer Cloud server.

2. **Access Token**  - An Access Token associated with a user account that has permissions to fetch assets.

<Image alt="MediMizer Cloud connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MediMizerCloud_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).