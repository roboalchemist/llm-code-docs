# Source: https://docs.axonius.com/docs/netmotion-mobility.md

# NetMotion Mobility

NetMotion Mobility is mobile VPN software that maximizes mobile field worker productivity by maintaining and securing their data connections as they move in and out of wireless coverage areas and roam between networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetMotion Mobility server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required, default: 8080)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="NetMotionMobility" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetMotionMobility.png" />

## APIs

Axonius uses the following APIs:

* [Mobility Server API for User Queries](https://help.netmotionsoftware.com/support/docs/MobilityXG/1100/help/mobilityhelp.htm#page/Mobility%2520Server%2FWebServices.13.11.html%23)
* [Mobility Server API for Device Queries](https://help.netmotionsoftware.com/support/docs/MobilityXG/1100/help/mobilityhelp.htm#page/Mobility%2520Server%2FWebServices.13.05.html%23)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **HTTP/HTTPS port 80**
* **HTTP/HTTPS port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to read **/Device** and **/User** queries.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| 12 and greater | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7