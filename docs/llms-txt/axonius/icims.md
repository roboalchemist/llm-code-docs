# Source: https://docs.axonius.com/docs/icims.md

# iCIMS

iCIMS is an enterprise recruiting platform allowing employers to attract, engage, hire, and advance employees.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **URL** *(required, default: `https://api.icims.com`)* - The hostname or IP address of the iCIMS server.

2. **Customer ID** - The customer ID for a user account provided by iCIMS that has the permissions to fetch assets.

3. **Client ID** and **Secret** *(required)* - The credentials provided by the iCIMS Integration Specialist.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="iCIMS" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/iCIMS.png" />

## APIs

Axonius uses the:

* [iCIMS API Field Types](https://developer.icims.com/REST-API/Object-Types-Commands/Field-Types)
* [iCIMS API Endpoints](https://developer.icims.com/REST-API/Object-Types-Commands)

Accessing an iCIMS API requires obtaining a Client ID and Client Secret for the service. To obtain a Client ID and Client Secret, request credentials from your organization’s iCIMS Integration Specialist.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Latest online version | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.5