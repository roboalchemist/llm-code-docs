# Source: https://docs.axonius.com/docs/floqast.md

# FloQast

FloQast is a SaaS accounting application, incorporating AI to automate close management and accounting workflows.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FlowQast server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. Refer to the [FloQast API Guide](https://help.floqast.com/hc/en-us/articles/14270183516827-Generate-a-FloQast-API-Key) for instructions on how to generate the API Key.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FloQast(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FloQast\(1\).png)

## APIs

Axonius uses the [FloQast API](https://developer.floqast.app/#section/Authentication).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The user account used as a connection must have a Manager or Admin role to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.30.0