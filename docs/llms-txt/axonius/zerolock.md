# Source: https://docs.axonius.com/docs/zerolock.md

# ZeroLock

ZeroLock is a runtime security platform that provides hypervisor protection and virtual patching for Linux-based environments.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Email/Password

### APIs

Axonius uses the [ZeroLock Server API](https://api.zerolock.com/#/).

### Permissions

The value supplied in [User Email](/docs/zerolock#required-parameters) must have 'endpoint view' permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 7.0.10

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ZeroLock server.
2. **User Email** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

![ZeroLock.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZeroLock.png)

### Optional Parameters

1. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**   - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in HTTPS Proxy.
4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the HTTPS Proxy.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).