# Source: https://docs.axonius.com/docs/akamai-eaa.md

# Akamai EAA

Akamai Enterprise Application Access (EAA) is part of the edge platform that helps companies secure applications that run behind a firewall or in a public cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Akamai EAA server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Contract ID** *(required)* - The Akamai contract identifier for your Enterprise Application Access product.

3. **Client Token**, **Client Secret**, and **Access Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. To create **Client Token**, **Client Secret**, and **Access Token**, refer to [Create an API client with custom permissions](https://techdocs.akamai.com/developer/docs/create-a-client-with-custom-permissions).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AkamaiEAA](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AkamaiEAA.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch user apps** *(default: disabled)* - Select this option to fetch the apps associated with the user's groups and directories, and add them to the user.
* **Apps names to ignore** (default: Empty, Optional) - List of applications names to ignore when adding the apps to the user.
* **Fetch only apps with directories** (default: disabled, Optional) - Select this option to fetch only apps that are associated with directories.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Enterprise Application Access API](https://techdocs.akamai.com/eaa-api/reference/api) for the following:

* Devices -[List device inventory](https://techdocs.akamai.com/eaa-api/reference/get-device-posture-inventory)
* Users -[List directory group users](https://techdocs.akamai.com/eaa-api/reference/get-directory-group-users)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The values supplied in [Access Token, Client Token, and Client Secret](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0