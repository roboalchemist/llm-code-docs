# Source: https://docs.axonius.com/docs/sentra.md

# Sentra

Sentra offers cloud data security posture management (DSPM), allowing customers to automatically discover, classify, monitor, and protect  cloud data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://app.sentra.io`)* - The hostname or IP address of the Sentra server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sentra](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sentra.png)

## APIs

Axonius uses the [sentra API](https://app.sentra.io/auth/callback)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 4.8