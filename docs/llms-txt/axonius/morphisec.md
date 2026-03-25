# Source: https://docs.axonius.com/docs/morphisec.md

# Morphisec Unified Threat Prevention Platform

Morphisec Unified Threat Prevention Platform provides centralized control, monitoring, and configuration of Morphisec’s endpoint security solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://eu-1.morphisec.cloud`)* - The hostname or IP address of the Morphisec server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Tenant ID** *(required)* - Specify the Tenant ID value.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Morphisec Unified Threat Prevention Platform](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Morphisec%20Unified%20Threat%20Prevention%20Platform.png)

## APIs

Axonius uses the [Morphisec API](https://eu-1.morphisec.cloud/api/management/swagger-ui/index.html#/Protectors/getProtectorsList).

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must have AMTD or AEM license permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.40.0