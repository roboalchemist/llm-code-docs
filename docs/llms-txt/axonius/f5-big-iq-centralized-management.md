# Source: https://docs.axonius.com/docs/f5-big-iq-centralized-management.md

# F5 BIG-IQ Centralized Management

F5 BIG-IQ Centralized Management provides centralized management, licensing, monitoring, and analytics for BIG-IP infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Load Balancers

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BIG-IQ server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Login Provider Name**  - The name of the login provider. In some scenarios, this field may be required.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ZLSCUDJY.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Pool Members**  *(optional, default: unchecked)* - Select this option to fetch the pool members of virtual IPs as devices.
2. **Fetch Big IP devices** - Select this option to fetch all the all the BIG IPs devices currently connected to BIG IQ Virtual Servers, enriching the BIG IQ Device itself.
3. **API version to use** - Enter the F5 API version to use. The adapter will then add the version to the requests to inform the F5 server which API version to use to retrieve results.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BIG-IQ 6.0.1 API](https://clouddocs.f5.com/products/big-iq/mgmt-api/v6.0.1/).

## Required Permissions

The value supplied in [User Name](#parameters) must have the following roles:

* Local Traffic
* Network Editor or Network Manager