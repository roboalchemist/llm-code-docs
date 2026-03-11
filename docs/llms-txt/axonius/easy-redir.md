# Source: https://docs.axonius.com/docs/easy-redir.md

# EasyRedir

EasyRedir is a URL redirection management platform that creates, analyzes, and manages redirects while automatically provisioning and renewing SSL certificates.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the EasyRedir server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** *(optional)* - Enter the Client ID.

3. **Client Secret** *(optional)* - Enter the Client Secret.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![easyredier connection parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NDEGPWZP.png)

## APIs

Axonius uses the [EasyRedir](https://dashboard.easyredir.com/docs/api#section/Introduction) API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1