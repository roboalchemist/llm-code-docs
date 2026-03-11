# Source: https://docs.axonius.com/docs/msp-manager.md

# MSP Manager

N-able MSP Manager is cloud-based help desk and billing software for IT service

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.mspmanager.com`)* - The hostname or IP address of the MSP Manager server that Axonius can communicate with via the [Required Ports](#required-ports) Use the default value.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MSPManager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MSPManager.png)

## APIs

Axonius uses the [MSP Manager oData API](https://api.mspmanager.com/odata/swagger/index.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.
Follow the [MSP Manager instructions](https://documentation.n-able.com/MSPM/userguide/en/Content/MSP-Configure-API-permissions.htm) to configure permissions to access MSP Manager's API.

## Supported From Version

Supported from Axonius version 5.0