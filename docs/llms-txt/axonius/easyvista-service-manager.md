# Source: https://docs.axonius.com/docs/easyvista-service-manager.md

# EasyVista Service Manager

EasyVista is an ITSM (IT Service Management) solution including change, release, incident, problem, and knowledge management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the EasyVista Service Manager server.

2. **Service Manager Account** - The Service Manager account as defined in [Different Platform Accounts](https://wiki.easyvista.com/xwiki/bin/view/Documentation/Service%20Manager%20-%20All%20Menus/Customize%20differents%20accounts/).

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="EasyVistaServiceManager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EasyVistaServiceManager.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch extra information for devices** *(required, default false*) - Select this option to fetch extra data to add more fields to the device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Service Manager REST API](https://wiki.easyvista.com/xwiki/bin/view/Documentation/Integration/WebService%20REST/).

## Supported From Version

Supported from Axonius version 4.8

## Related Enforcement Actions

* [EasyVista Service Manager - Create Ticket](https://docs.axonius.com/axonius-help-docs/docs/easyvista-create-ticket)