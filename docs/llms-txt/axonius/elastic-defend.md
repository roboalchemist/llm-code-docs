# Source: https://docs.axonius.com/docs/elastic-defend.md

# Elastic Defend

Elastic Defend (formerly Endgame) is a tool for malware prevention, detection, and response.

### Asset Types Fetched

* Devices

## Before You Begin

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the <Anchor label="Elastic Security APIs" target="_blank" href="https://www.elastic.co/guide/en/security/current/list-endpoints-api.html">Elastic Security APIs</Anchor>.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Kibana server.

2. **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.

3. **Port** - The port number of your Kibana instance.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Elastic%20Defend.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**  - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoint Config

* **Fetch Devices of sub type Host from Hosts***(default: true)* - Enable this option to fetch devices whose sub-type is Host from the Hosts endpoint.

### Spaces - applies context on the following endpoints: Hosts by Space

* **Spaces** - Specify which SpaceID to use for the connection.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                  | Supported | Notes |
| ------------------------ | --------- | ----- |
| Elastic Security APIs V1 | Yes       |       |

## Supported From Version

Supported from Axonius version 6.0