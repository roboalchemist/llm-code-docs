# Source: https://docs.axonius.com/docs/quadrant.md

# Quadrant

Quadrant is a Managed Detection and Response solution operating at the intersection of People and Product.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Quadrant server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **API Key** *(required)* - Credentials required to use the Quadrant API to retrieve alert data. To retrieve these credentials, sign into your Quadrant Sec Console and navigate to the Quadrant API page.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Quadrant](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Quadrant.png)

## APIs

Axonius uses the [Quadrant API (2.0.0)](https://api.qis.io/redoc).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read permissions to GET Quadrant V2/alerts.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V2      | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0