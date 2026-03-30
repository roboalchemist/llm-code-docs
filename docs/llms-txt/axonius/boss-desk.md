# Source: https://docs.axonius.com/docs/boss-desk.md

# BOSSDesk

BOSSDesk is an IT Service Management and Help Desk Software for both On-Premise and in the Cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BossDesk server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![BOSSDesk](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BOSSDesk.png)

## APIs

Axonius uses the [API Documentation - BOSSDesk Documentation](https://docs.bossdesk.io/api/).

## Required Permissions

The BossDesk enforcement actions require permissions.

## Supported From Version

Supported from Axonius version 4.8