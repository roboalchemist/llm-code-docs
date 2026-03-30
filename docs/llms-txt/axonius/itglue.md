# Source: https://docs.axonius.com/docs/itglue.md

# IT Glue

IT Glue is a SOC 2-compliant IT documentation management platform designed for managed service providers (MSPs).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IT Glue server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To create an API Key:

   1. Login to IT Glue with an Administrator role.

   2. Select **Account `>` Settings >**

   3. Enter a name for the key and click **Generate API Key**. Store your API Key in a secure location so it could be retrieved later.

3. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="IT Glue" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IT%20Glue.png" />

## APIs

Axonius uses the [IT Glue API](https://api.itglue.com/developer).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Administrator permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5