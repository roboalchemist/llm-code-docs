# Source: https://docs.axonius.com/docs/agni.md

# AGNI

AGNI is an Arista Networks solution that simplifies secure onboarding, posture analysis, and network access control. It is designed to work seamlessly with Zero Trust architectures through integrated segmentation, encryption, and advanced monitoring capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the AGNI server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Key ID** and **Key Value** *(required)* - The Authentication Key ID and Authentication Key Secret.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AGNI](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AGNI.png)

## APIs

Axonius uses the [AGNI API](https://www.arista.com/assets/data/pdf/user-manual/um-books/AGNI-API-Guide.pdf) as well as the following APIs:

* Key Login - /cvcue/keyLogin
* User List - /identity.user.list
* Config NAD List - /config.nad.list

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [**Key ID** and **Key Value**](/docs/agni#parameters) must be associated with credentials that have Super-Admin or Admin permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.31.0