# Source: https://docs.axonius.com/docs/grouper.md

# Grouper

Grouper is an access management tool that provides attribute/role-based access control and group memberships.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Grouper server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. For more information, see [Grouper Web Services Authentication](https://spaces.at.internet2.edu/display/Grouper/Grouper+web+services+-+authentication+-+built-in+Grouper).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Grouper](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Grouper.png)

## APIs

Axonius uses the [Grouper Web Services API](https://spaces.at.internet2.edu/display/Grouper/Grouper+Web+Services).

## Supported From Version

Supported from Axonius version 6.1.31.0