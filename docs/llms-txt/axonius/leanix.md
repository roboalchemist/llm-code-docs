# Source: https://docs.axonius.com/docs/leanix.md

# LeanIX

LeanIX is a cloud-based software platform that helps companies manage and optimize their IT infrastructure and applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Application Services

**Related Enfocrement Actions**

[Make LeanIX Factsheets](/docs/make-leanix-factsheets)

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the LeanIX server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on authentication, see [Authentication to LeanIX Services](https://docs-eam.leanix.net/reference/authentication-for-managing-api-tokens).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="LeanIX" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LeanIX.png" />

## APIs

Axonius uses the [LeanIX GraphQL API](https://docs-eam.leanix.net/reference/get-fact-sheets).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read fact sheets permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1