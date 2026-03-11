# Source: https://docs.axonius.com/docs/aruba.md

# HPE Aruba Networking

HPE Aruba Networking connects to Aruba switches and routers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Aruba Host** *(required)* - The hostname or IP address of the HPE Aruba Networking server.
2. **Port** *(optional)* - The port used for the connection.
3. **Is OS CX device** - Select whether the switch is managed by the AOS-CX operating system.
4. **Is EdgeConnect device** - Select whether the switch is managed by the EdgeConnect SD-WAN.
5. **User Name** and **Password** *(optional)* - The user name and password to access routers.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **Use SSL** - Select whether to connect to the server with SSL.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Aruba](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Aruba.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch CDP, LLDP and VRF information (only for OS CX devices)** - Select this option to fetch CDP, LLDP, and VRF information. This setting is only relevant when [**Is OS CX device**](/docs/aruba#parameters) is enabled.