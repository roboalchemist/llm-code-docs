# Source: https://docs.axonius.com/docs/pulseway.md

# Pulseway

Pulseway is a remote monitoring and management (RMM) system solution that enables an admin to remotely monitor, manage and troubleshoot workstations, servers and network devices across an environment.

### Asset Types Fetched

* Devices
* Software
* SaaS Applications

## Before You Begin

**Ports**
Axonius must be able to communicate with the value supplied in Host Name or IP Address via the following ports:

* TCP port 443

### APIs

Axonius uses the [Pulseway REST API](https://api.pulseway.com/#introduction).

### Permissions

The user account must have READ permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Pulseway server.
2. **Token ID** and **Token Secret** - The credentials for a user account that has Read permissions to fetch assets.
3. **Verify SSL** - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

<Image alt="params" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-5WGQO5CY.png" />

### Optional Parameters

1. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
2. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
3. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version              | Supported | Notes |
| -------------------- | --------- | ----- |
| Pulseway REST API v3 | Yes       |       |