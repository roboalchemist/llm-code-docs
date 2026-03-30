# Source: https://docs.axonius.com/docs/paycor.md

# Paycor

Paycor is an automated human capital management (HCM) platform for managing HR and payroll needs in one place.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: apis.paycor.com)* - The hostname or IP address of the Paycor server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID (Legal Entity ID)** and **Access Token** *(required)* - The Application OAuth Client ID and OAuth Client Secret for a user account that has the permissions to fetch assets.

To generate the Client ID, Access Token, and APIm Subscription Key, see [Paycor Developer Portal | Getting Started](https://developers.paycor.com/guides#getting-started).

4. **APIm Subscription Key** *(required)* - A subscription key associated with a user account that has permissions to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Paycor" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Paycor.png" />

## APIs

Axonius uses the [Paycor Public API](https://developers.paycor.com/explore).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be created by a user with App Creator Admin permissions.

## Supported From Version

Supported from Axonius version 4.7