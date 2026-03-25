# Source: https://docs.axonius.com/docs/avi-networks.md

# VMware NSX Advanced Load Balancer

VMware NSX Advanced Load Balancer (formerly AVI Networks) delivers multi-cloud application services used for load balancing, web application firewall and container ingress.

### Asset Types Fetched

* Devices, Load Balancers

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Avi Networks REST API Usage Version 22.1.1](https://avinetworks.com/docs/latest/api-guide/).

The API domain is local on client.

### Permissions

The value supplied in [User Name](#required-parameters) must have ”Security-Readonly” Role  permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 4.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the VMware NSX Advanced Load Balancer server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets. This needs to be for a local user account. Make sure you enable Basic Authentication  in NSX ALB.

![AviNetworks](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AviNetworks.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse devices as Load Balancers** - Select this option to parse devices as load balancers.
2. **Fetch from all tenants** - Select this option to fetch assets from all available tenants instead of the default tenant alone.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |