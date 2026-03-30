# Source: https://docs.axonius.com/docs/apple-gsx.md

# Apple GSX

Apple GSX is an IT management tool that provides access to Apple’s device management and support services for authorized partners.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Apple GSX server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **SoldTo ID** and **ShipTo ID** *(required)* - The SoldTo and ShipTo location IDs. Example: 0000012345

3. **Service API Version** *(required)* - The version called for in service requests. Example: v2, v3

4. **Authentication Token** *(required)* - Use the API key you have generated.

5. **Apple ID** *(required)* - Enter the Apple ID.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Apple GSX](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Apple%20GSX.png)

## APIs

Axonius uses the Apple GSX API.

## Supported From Version

Supported from Axonius version 6.1.32.1