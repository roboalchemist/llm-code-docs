# Source: https://docs.axonius.com/docs/backbox.md

# BackBox

BackBox is a network automation and security platform that provides automated configuration backup, compliance validation, and vulnerability remediation for network and security devices.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [BackBox API](https://support.backbox.com/customers/s/article/BackBox-API).

### Permissions

Read access for devices is required to fetch the device list.

#### Supported From Version

Supported from Axonius version 7.0.13

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the BackBox server.

2. **API Token**  - An API Token associated with a user account that has the  Required Permissions to fetch assets.

<Image alt="BackBox connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BackBox.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).