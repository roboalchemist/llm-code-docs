# Source: https://docs.axonius.com/docs/teramind.md

# Teramind

Teramind is an employee monitoring, user behavior analytics, and insider threat detection solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Teramind server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Access Token** *(required)* - Create an Access Token from your Teramind dashboard: Administrator menu → Access Tokens.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Teramind](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Teramind.png)

## APIs

Axonius uses the [Teramind Dashboard API](https://apidoc.dev.teramind.co/#intro).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.0