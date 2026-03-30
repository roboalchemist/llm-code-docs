# Source: https://docs.axonius.com/docs/ifs-assyst.md

# IFS Assyst

IFS Assyst is IT service management (ITSM) software that helps automate business processes.

**Related Enforcement Actions:**

* [IFS Assyst - Create Event per Entity](/docs/assyst-cmdb-create-event-per-entity)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IFS Assyst server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Product Class ID List** *(optional)* - Enter the Product Class ID to map to the product to import.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IFS%20Assyst](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IFS%20Assyst.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **UserField mapped to IP address** *(optional)* - Enter a field name from Assyst to map to the Axonius IP address field. This field is case sensitive and must match what is seen in the Advanced View.
2. **UserField mapped to MAC address** *(optional)* - Enter a field name from Assyst to map to the Axonius MAC address field. This field is case sensitive and must match what is seen in the Advanced View.
3. **UserField mapped to OS** *(optional)* - Enter a field name from Assyst to map to the Axonius OS field. This field is case sensitive and must match what is seen in the Advanced View.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 4.8