# Source: https://docs.axonius.com/docs/changegear.md

# ChangeGear

ChangeGear is an AI-powered IT service management platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ChangeGear server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to access CMDB objects.

3. **Verify SSL** *(required, default: False)* - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ChangeGear](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeGear.png)

## APIs

Axonius uses the following [ChangeGear REST API](https://support.sunviewsoftware.com/cgrestapi/help)

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions  to access CMDB objects.

## Supported From Version

Supported from Axonius version 4.5