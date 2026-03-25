# Source: https://docs.axonius.com/docs/openvpn-cloud.md

# OpenVPN Cloud

OpenVPN Cloud is a VPN-as-a-Service solution that eliminates the need for VPN server installation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Unique API URL** *(required)* - The API endpoint address unique to your OpenVPN Cloud account, in the following format: *yourOpenVPNID*.api.openvpn.com

2. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret for an account that has Read access to the API.
   To obtain the Client ID and Client Secret, see [Creating OAuth Credentials](https://openvpn.net/cloud-docs/api-guide/).

3. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="OpenVPN_Cloud" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OpenVPN_Cloud.png" />

## APIs

Axonius uses the [OpenVPN Cloud API (beta)](https://openvpn.net/cloud-docs/api-guide/).

## Supported From Version

Supported from Axonius version 4.5