# Source: https://docs.axonius.com/docs/aviatrix.md

# Aviatrix

The Aviatrix cloud network platform delivers a single platform for multi-cloud networking, security, and operational visibility.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Aviatrix server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that have the [Required Permissions](/docs/aviatrix#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="Aviatrix" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Aviatrix.png" />

## APIs

Axonius uses the Aviatrix API.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read-only permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| R6.6.5230 Aviatrix API | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.5