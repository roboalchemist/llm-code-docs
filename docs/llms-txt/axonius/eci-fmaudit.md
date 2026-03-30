# Source: https://docs.axonius.com/docs/eci-fmaudit.md

# ECI FMAudit

ECI FMAudit is print management software that allows users to remotely monitor print environments and maintain visibility into their operations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ECI FMAudit server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Account ID** *(required)* - Enter your ECI FMAudit account number.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="FMAudit" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FMAudit.png" />

## APIs

Axonius uses the [FMAudit API](http://imagenet.fmwebaudit.com/WebServices/PublicAPI.asmx?wsdl).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80 or 443**

## Supported From Version

Supported from Axonius version 4.7