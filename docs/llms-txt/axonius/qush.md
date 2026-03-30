# Source: https://docs.axonius.com/docs/qush.md

# NextDLP

NextDLP, formerly Qush Security, enables customers to discover risks, educate employees, enforce policies and prevent data loss.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Qush Reveal server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To generate a token, see [Authentication](https://www.qush.com/support/using-the-reveal-platform-api#authentication).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NextDLP](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NextDLP.png)

## APIs

Axonius uses the [Qush Reveal Platform API](https://www.qush.com/support/using-the-reveal-platform-api#authentication).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **HTTP/S port 80**
* **HTTP/S port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                          | Supported | Notes |
| -------------------------------- | --------- | ----- |
| Qush Reveal Agent Version 7.10.1 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6