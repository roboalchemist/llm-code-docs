# Source: https://docs.axonius.com/docs/ivanti-neurons.md

# Ivanti Neurons

Ivanti Neurons is a unified endpoint management tool that discovers and remediates security threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Ivanti Neurons server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID and Client Secret** *(required)* -  The credentials for a user account that has [Required Permissions](#required-permissions) to fetch assets. For information on authentication, see the [Ivanti People and Device Inventory API](https://help.ivanti.com/ht/help/en_US/CLOUD/api/PeopleDevices/peopledevices-authenication.htm).

3. **Tenant ID** *(required)* - The registered tenant ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IvantiNeurons](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IvantiNeurons.png)

## APIs

Axonius uses the [Ivanti People and Device Inventory API](https://developer.ivanti.com/ivanti-ivanti-default/api/people-and-device-inventory/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have read permissions for the People and Device Inventory API in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                            | Supported | Notes |
| ---------------------------------- | --------- | ----- |
| People and Device Inventory API V1 | Yes       |       |

## Supported From Version

Supported from Axonius version 6.0