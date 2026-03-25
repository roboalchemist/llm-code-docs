# Source: https://docs.axonius.com/docs/manageengine-mdm.md

# ManageEngine Mobile Device Management

ManageEngine MDM is a mobile device management solution.

## Asset Types Fetched

* Devices, Users

## Before You Begin

### APIs

Axonius uses the [ManageEngine Mobile Device Manager Plus API](https://www.manageengine.com/mobile-device-management/api/).

### Required Ports

You can set your own customer port. If you do not, then Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

### Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

The following permissions are required:

* MDMOnDemand.MDMInventory.READ
* MDMOnDemand.MDMUser.READ

### Supported From Version

Supported from Axonius version 4.7

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ManageEngine MDM server.
2. **MDM Type** - Select the MDM type you are using, either **MDM On-Premises** (the default) or **MDM Cloud Zoho REST API**.

   When selecting **MDM On-Premises**, the following parameter is required:

   1. **API Key** - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
      To generate an API Key, see [Authentication](https://www.manageengine.com/mobile-device-management/api/#authentication).

   When selecting **MDM Cloud Zoho REST API**, the following parameters are required:

   1. **One Time OAuth Access Code** - The one-time authentication code to get the access token.
   2. **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has read access to the API. For more information, see [OAuth](https://www.manageengine.com/mobile-device-management/api/#authentication).

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ManageEngineMobile_connect.png" />

### Optional Parameters

1. **Port** - Enter a port that Axonius can use to communicate with the server. If you don’t enter a port, Axonius will use the [Required Ports](#required-ports).
2. When selecting **MDM Cloud Zoho REST API** as the **MDM Type**, the following parameters are optional:
   1. **Redirect URI** - The same redirect URL used when registering the Client ID and Client Secret.
   2. **MDM Instance ID** - Provide your `mdm_instance` Cookie.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1.0.0   | Yes       | --    |

<br />