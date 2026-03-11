# Source: https://docs.axonius.com/docs/motus.md

# Motus

Motus is a platform that provides vehicle management and reimbursement solutions for mobile-enabled workforces.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets. For more information, see [Authentication and Security](https://developer.motus.com/authentication-and-security/).

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Motus.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Motus.png)

## APIs

Axonius uses the [Motus API](https://developer.motus.com/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1