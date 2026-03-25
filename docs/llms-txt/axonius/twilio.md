# Source: https://docs.axonius.com/docs/twilio.md

# Twilio

Twilio is a customer engagement platform that offers programmable communication solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Accounts/Tenants

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Twilio server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Account SID** and **Authentication Token** *(required)* - The credentials for a user account that has permission to fetch assets. For more details, see [REST API: Credentials](https://www.twilio.com/docs/iam/credentials/api#authentication).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Twilio](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Twilio.png)

## APIs

Axonius uses the [Twilio REST API](https://www.twilio.com/docs/iam/api/account).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **443**

## Supported From Version

Supported from Axonius version 6.1.30.0