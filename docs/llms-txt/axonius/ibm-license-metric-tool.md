# Source: https://docs.axonius.com/docs/ibm-license-metric-tool.md

# IBM License Metric Tool

IBM License Metric Tool (ILMT) helps manage license allocation services on supported systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IBM License Metric Tool server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Token** *(required)* - An API token associated with a user account that has permissions to fetch assets. See [APIs](#APIs) below on how to retrieve the authentication token.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IBMLicenseMetricTool](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBMLicenseMetricTool.png)

## APIs

Axonius uses [License Metric Tool 9.2 REST API resources and HTTP methods](https://www.ibm.com/docs/en/license-metric-tool?topic=api-rest-resources-http-methods), which includes the following sections:

* Authentication token: To retrieve the token from the user interface, log in to License Metric Tool, hover over the User icon, click **Profile**., and then click **Show token**.

* Endpoint:[Retrieval of hardware inventory (v2)](https://www.ibm.com/docs/en/license-metric-tool?topic=v2-retrieval-hardware-inventory)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.0