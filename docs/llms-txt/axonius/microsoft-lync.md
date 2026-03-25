# Source: https://docs.axonius.com/docs/microsoft-lync.md

# Microsoft Lync

Microsoft Lync provides instant messaging (IM), audio and video calls, Lync Meetings, availability (presence) information, and sharing capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Root Domain** *(required)* - Your company root domain.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets. The supplied user must have be [enabled for Skype for Business Server](https://docs.microsoft.com/en-us/powershell/module/skype/enable-csuser?view=skype-ps).
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Root Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Root Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Root Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Root Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Root Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Root Domain**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Root Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Root Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1604\).png)

## APIs

Axonius uses the [Unified Communications Web API (UCWA)](https://docs.microsoft.com/en-us/skype-sdk/ucwa/ucwaresources.)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Microsoft Lync 2013 | Yes       |       |