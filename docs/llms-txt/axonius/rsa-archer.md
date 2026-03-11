# Source: https://docs.axonius.com/docs/rsa-archer.md

# Archer IRM

Archer IRM delivers innovative solutions that help businesses protect their assets, meet compliance requirements, and proactively manage risks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Archer server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Instance Name** *(required)* - The Archer instance name.

4. **User Domain** *(optional)* - The domain of the user.

5. **API Prefix** *(optional)* - Specify the directory path used to access the API. Unless otherwise specified, the API prefix defaults to:  /Archer

6. **Verify SSL** Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![RSA\_Archer\_6-4-22](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RSA_Archer_6-4-22.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **URL endpoint for devices** *(required, default: Devices)* - Enter a name of the URL endpoint for devices, as it appears in the Archer Configuration page.
2. **Fetch Applications** - Select this option to fetch applications.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Archer REST API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **Port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have permissions to fetch assets.