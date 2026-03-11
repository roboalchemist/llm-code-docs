# Source: https://docs.axonius.com/docs/radiant-logic-vds.md

# Radiant Logic Virtual Directory Server (VDS)

Radiant Logic Virtual Directory Server (VDS) is a software layer that consolidates disparate identity sources into a central virtual namespace.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Radiant Logic Virtual Directory Server (VDS) server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Port** *(required, default: 8089)* - The port number of the RadiantOne RESTFul Web Service that is used for the connection.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Radiant%20Logic%20Virtual%20Directory%20Server](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Radiant%20Logic%20Virtual%20Directory%20Server.png)

## APIs

Axonius uses the [RadiantOne REST API (ADAP)](https://developer.radiantlogic.com/idm/v8.0/web-services-api-guide/rest/#rest-query-examples).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **8089**

## Supported From Version

Supported from Axonius version 6.0