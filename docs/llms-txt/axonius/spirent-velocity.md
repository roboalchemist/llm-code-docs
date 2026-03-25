# Source: https://docs.axonius.com/docs/spirent-velocity.md

# Spirent Velocity

Spirent Velocity is a software deployment and release management tool used for automating application deployments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Spirent Velocity server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Spirent Velocity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Spirent%20Velocity.png)

## APIs

Axonius uses the [Velocity 9.4.0 API](https://kms.spirentcom.com/CSC/Velocity_API/9.4.0/index.html).

## Supported From Version

Supported from Axonius version 6.1