# Source: https://docs.axonius.com/docs/sonicwall-nsm.md

# SonicWall Network Security Manager

SonicWall Network Security Manager enables organizations to deploy and manage all firewalls, connected switches and access points in one interface.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SonicWall Network Security Manager server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Tenant ID** *(optional)* -  The unique ID of the tenant that you want the adapter to connect. To obtain the Tenant ID, log in to the SonicWall NSM dashboard and inspect the Debug Console.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SonicWall_NSM" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SonicWall_NSM.png" />

## APIs

Axonius uses the [NSM API Gateway](https://nsm-uswest.sonicwall.com/api/docs/nsm).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **80**
* **443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read-only permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1.0.0   | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.5