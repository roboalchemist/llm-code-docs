# Source: https://docs.axonius.com/docs/mulesoft-anypoint.md

# MuleSoft Anypoint Platform

The MuleSoft Anypoint Platform is a single solution for developing, deploying, securing, and managing APIs and integrations.

## Asset Types Fetched

* Users, Application Settings

## Before You Begin

### APIs

Axonius uses the MuleSoft Platform API.

1. Authorization: `/accounts/api/v2/oauth2/token`
2. Users: `/accounts/api/organizations/organization_id/users`
3. `GET /cloudhub/api/v2/applications/{domain}` — Fetch application settings

### Required Ports

Axonius must be able to communicate with the value supplied in Host Name or IP Address via the following ports:

* **TCP port 80/443**

### Required Permissions

Read permissions are required in order to fetch assets.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** *(default: `https://anypoint.mulesoft.com`)* - The hostname or IP address of the MuleSoft Anypoint Platform server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Organization ID** - The organization ID of the specific organization the customer wishes to fetch devices from.

![](https://files.readme.io/f3bb8857baa9aca2c9cb508f9e5d7e313bd264ad03e18b272dc91c0959115fa3-image.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Fetch All Vendor Settings** *(default: disabled)* - Select whether to fetch all vendor settings.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Supported From Version

Supported from Axonius version 6.0