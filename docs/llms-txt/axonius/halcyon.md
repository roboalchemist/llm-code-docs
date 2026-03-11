# Source: https://docs.axonius.com/docs/halcyon.md

# Halcyon

The Halcyon Anti-Ransomware and Cyber Resilience Platform offers layered ransomware protection.

**Related Enforcement Actions:**

* [Tag Halcyon Device](/docs/tag-halcyon-device)
* [Untag Halcyon Device](/docs/untag-halcyon-device)
* [Halcyon - Delete Device](/docs/delete-halcyon-device)
* [Halcyon - Set Device Policy](/docs/set-halcyon-device-mode)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Base API url** *(required)* - Enter [https://api.halcyon.ai/](https://api.halcyon.ai/)  to access the Halcyon server.

2. **User Name** and **Password** *(required)* - The credentials for a user account to log into the Halcyon application.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Halcyon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Halcyon.png" />

## APIs

Axonius uses the [Halcyon API](https://api.halcyon.ai/docs#section/Authentication).

## Supported From Version

Supported from Axonius version 5.0.