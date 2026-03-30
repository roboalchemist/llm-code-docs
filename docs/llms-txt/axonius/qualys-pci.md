# Source: https://docs.axonius.com/docs/qualys-pci.md

# Qualys PCI Compliance

Qualys PCI Compliance evaluates compliance with the Payment Card Industry Data Security Standard (PCI DSS).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Qualys PCI Compliance server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Qualys%20PCI%20Compliance](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Qualys%20PCI%20Compliance.png)

## APIs

Axonius uses the [PCI Merchant API](https://cdn2.qualys.com/docs/qualys-pci-merchant-api-user-guide.pdf).

## Required Permissions

An active PCI merchant account  is required in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0