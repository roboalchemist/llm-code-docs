# Source: https://docs.axonius.com/docs/bmc-truesight-automation-for-servers.md

# BMC TrueSight Automation for Servers

BMC TrueSight Automation for Servers automates vulnerability management, patching, compliance, configuration changes, software deployments, and service provisioning in the data center and cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BMC TrueSight Automation for Servers server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Port** - *(required, default: 9843)*   The port of the BMC TrueSight Automation for Servers server.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the Permissions to fetch assets.
4. **Role** *(required)* - A  Role associated with a user account that has the permissions to fetch assets. If there is no role specified in the request, the role assigned during the session creation is used.
5. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
6. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
9. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![BMCTRueSightAutmaton.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BMCTRueSightAutmaton.png)

## APIs

Axonius uses the [TrueSight Server Automation Rest API](https://docs.bmc.com/docs/tssa89/using-truesight-server-automation-restful-web-services-808908583.html#UsingTrueSightServerAutomation-RESTfulWebServices-UsingHTTPwithRESTfulwebservices).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 9843**

## Version Matrix

| Version                         | Supported | Notes |
| ------------------------------- | --------- | ----- |
| TrueSight Server Automation 8.9 | Yes       |       |

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, and it is not functioning as expected.