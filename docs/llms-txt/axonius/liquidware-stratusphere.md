# Source: https://docs.axonius.com/docs/liquidware-stratusphere.md

# Liquidware Stratusphere UX

Liquidware Stratusphere UX is a user experience monitoring and diagnostics platform that analyzes the performance of virtual and physical environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Liquidware server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Liquidware Stratusphere UX](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Liquidware%20Stratusphere%20UX.png)

## APIs

Axonius uses the [Liquidware Stratusphere API](https://docs.liquidware.com/stratusphere/en-us/common/stratusphere-getting-started-api-guide/using-the-api.htm).

## Required Permissions

The value supplied in [User Name](#parameters) must have admin permissions in order to fetch assets. For more information, see [Granting Client Devices API Access](https://docs.liquidware.com/stratusphere/en-us/common/stratusphere-getting-started-api-guide/granting-client-devices-api-access.htm).

## Supported From Version

Supported from Axonius version 6.1.32.1