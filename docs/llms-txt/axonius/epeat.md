# Source: https://docs.axonius.com/docs/epeat.md

# EPEAT

EPEAT (Electronic Product Environmental Assessment Tool) evaluates the effect of a product on the environment.

**Related Enforcement Actions**

* [Enrich Asset Data - EPEAT](/docs/enrich-device-data-with-epeat)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the EPEAT server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **ApiKey** *(required)* - The API key used to access your EPEAT account.

3. **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![EPEATAdapterConnnectionConfig.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EPEATAdapterConnnectionConfig.png)

## APIs

Axonius uses the [Computers & Displays Searching | EPEAT Registry](https://www.epeat.net/search-computers-and-displays) API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

Read permissions are required in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0