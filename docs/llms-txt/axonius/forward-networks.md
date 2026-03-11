# Source: https://docs.axonius.com/docs/forward-networks.md

# Forward Networks

Forward Networks delivers a digital twin of the network, enabling operators to ensure the network is secure, reliable, and agile. The platform supports devices from all major networking vendors and cloud providers.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Forward API](https://fwd.app/api-doc). Contact your admistrator for further information about connecting.

### Permissions

The value supplied in [User Name](#required-parameters) must have Read permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Forward Networks server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets. The API access key can be used as a user and the API Secret Key can be used as the password. For more information, see [APIs](#apis).

<Image alt="Forward Networks.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Forward%20Networks.png" />

### Optional Parameters

1. **Fetch Hosts Using NQE Query** - Select to use the Network Query Engine endpoint to fetch additional devices.

2. **Verify SSL** - Select to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Do not display Asset name for devices** - Select to not display the asset name for devices.
2. **Network Name Include list** *(optional)* - Enter a list of comma-separated network names to include in the fetch. If left empty, all network names are included in the fetch.
3. **Use Networks API to fetch devices** - Select this option to use the networks API to fetch devices.
4. **Fetch Vulnerabilities** - Select this option to fetch vulnerabilities.
5. **Devices custom NQE query** *(optional)* - Enter a custom NQE query for devices.
6. **Location custom NQE query** *(optional)* - Enter a custom NQE query for location.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and is not functioning as expected.

| Version                 | Supported | Notes |
| ----------------------- | --------- | ----- |
| Forward Networks 21.9.3 | Yes       |       |