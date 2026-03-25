# Source: https://docs.axonius.com/docs/sophos.md

# Sophos Endpoint Protection

Sophos Endpoint Protection helps secure workstations by adding prevention, detection, and response technology on top of the operating system.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Sophos API Domain** *(required, default: `https://api.central.sophos.com`)* - The API Access URL address provided in the Sophos Central Admin.
2. **Client ID** and **Client Secret** *(required)* - The credentials provided in the Sophos Central Admin. For information on how to create a Client ID and Client Secret, see [Getting Started as a Tenant](https://developer.sophos.com/getting-started-tenant).
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sophos Endpoint Protection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sophos%20Endpoint%20Protection.png)

## APIs

Axonius uses the following APIs:

* [Sophos Central APIs](https://developer.sophos.com/getting-started-tenant)
* [Sophos Endpoint API](https://developer.sophos.com/docs/endpoint-v1/1/routes/endpoints/get)

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must have Super Admin credentials in order to generate the API Key.