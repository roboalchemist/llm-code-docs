# Source: https://docs.axonius.com/docs/red-hat-idm.md

# Red Hat IDM

Red Hat Identity Management (IdM) provides a centralized and unified way to manage identity stores, authentication, policies, and authorization policies in a Linux-based domain.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **IDM Server Name** *(required)* - Specify the domain name of the Identity Management server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Certification File**  *(required)* - Click **Upload File** to upload an IdM Server certificate file.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![RedHat\_IDM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedHat_IDM.png)

## APIs

Axonius uses the [Identity Management API](https://access.redhat.com/articles/2728021).

## Supported From Version

Supported from Axonius version 4.5