# Source: https://docs.axonius.com/docs/jetpatch.md

# JetPatch

JetPatch is a centralized patch management platform focusing on end-to-end enterprise patch management and vulnerability remediation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the JetPatch server.

2. **User Name** *(required)* - The credentials for a user account that has the [required permissions](/docs/jetpatch#required-permissions) to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To generate an API Key, see [Granting API Permission](https://kc.jetpatch.com/hc/en-us/articles/360024119211-Granting-API-Permission).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="JetPatch" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JetPatch.png" />

## APIs

Axonius uses the [JetPatch API](https://kc.jetpatch.com/hc/en-us/categories/360001504172-API-Developer-Guide).

## Required Permissions

The value supplied in [User Name](#parameters) must have read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.6