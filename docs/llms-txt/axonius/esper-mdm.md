# Source: https://docs.axonius.com/docs/esper-mdm.md

# Esper

Esper is a platform that provides comprehensive device management and application deployment solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Esper server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Getting Started with APIs](https://help.esper.io/hc/en-us/articles/14199291792145-Getting-Started-with-APIs).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Esper.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Esper.png)

## APIs

Axonius uses the [Esper Get All Devices API](https://help.esper.io/hc/en-us/articles/16036992814609-Commonly-Used-APIs#h_01H2GX045Y2HBK303C3QHSX3XF).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.54.0