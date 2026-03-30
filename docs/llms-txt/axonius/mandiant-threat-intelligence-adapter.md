# Source: https://docs.axonius.com/docs/mandiant-threat-intelligence-adapter.md

# Mandiant Threat Intelligence

Mandiant is a cybersecurity platform offering threat intelligence, incident response, and security consulting services to detect and mitigate advanced cyber threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

2. **Monitor IDs** *(required)* - A list of IDs for monitors to retrieve alerts from.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Mandiant Threat Intelligence](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mandiant%20Threat%20Intelligence.png)

## APIs

Axonius uses the [Mandiant API](https://api.intelligence.mandiant.com/v4/dtm/alerts).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1