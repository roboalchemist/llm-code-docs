# Source: https://docs.axonius.com/docs/emass.md

# eMASS

eMASS is a federal system designed to help maintain information assurance situational awareness, manage risk, and comply with federal regulations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the eMASS server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets. Provided or from the authentication process.

3. **Org ID** *(required)* - Organization ID provided by eMASS Support.

4. **Certificate File** *(required)* - Choose and upload (click **Upload File**) the eMASS issued certificate file (.CRT).

5. **Key File** *(required)* - Choose and upload (click **Upload File**) the .KEY file created as part of the CSR process for authentication of the cetificate file.

6. **Passphrase** - A passphrase for the private key file.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![eMASS](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/eMASS.png)

## APIs

Axonius uses the eMASS REST API (V3.3).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following port:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.8