# Source: https://docs.axonius.com/docs/veracode.md

# Veracode

Veracode provides static, dynamic, and software composition scanning to identify vulnerabilities in the software development lifecycle.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.veracode.com`)* - The hostname or IP address of the Veracode server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate the Client ID and Client Secret, see [Generate Veracode API Credentials](https://docs.veracode.com/r/t_create_api_creds).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Veracode" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Veracode.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch findings** - *(default: false)* - Enable this to fetch Findings for devices, which includes scans and vulnerability information from Veracode. When this is enabled, the following field become available:
  * **Scan types** - Select specific scan types to fetch for Findings. You can select multiple types.
* **Use findings hostname as hostname** - Select this option to use the first hostname found in the findings as the hostname for the device

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Veracode APIs](https://docs.veracode.com/r/c_gettingstarted).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have Read permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7