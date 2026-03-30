# Source: https://docs.axonius.com/docs/coalfireone.md

# CoalfireOne

CoalfireOne provides year-round visibility and proactive management of your compliance program.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CoalfireOne server.
2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

   <Image alt="coalfireONe.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/coalfireONe.png" />

## APIs

Axonius uses the Version 2 of the [CoalfireOne API](https://app.swaggerhub.com/apis/CFO.Eng/CoalfireOne.API/2021.02.08).

### Generating the Client ID and Client Secret

You need to generate a key in order to access the API.

1. From the *User Profile* in CoalfireOne select *Programmatic Access*.

   <Image alt="Coalfire1Conf.jpg" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Coalfire1Conf.jpg" />

2. Click the icon to copy the ID Key and Secret or click *Download File* to save them to your computer.

   <Image alt="Coalfire1Conf2.jpg" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Coalfire1Conf2(1).jpg" />

Refer to CoalfireOne documentation for further details.

## Supported From Version

Supported from Axonius version 4.4