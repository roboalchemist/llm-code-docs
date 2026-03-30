# Source: https://docs.axonius.com/docs/sevone.md

# SevOne Data Platform

SevOne Data Platform (acquired by IBM) is a network and infrastructure management platform

## Parameters

1. **SevOne Data Platform Domain** *(required)* - The SevOne Data Platform domain that  Axonius can communicate with via the [Required Ports](#required-ports).
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **SevOne Data Platform Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **SevOne Data Platform Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **SevOne Data Platform Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **SevOne Data Platform Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **SevOne Data Platform Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **SevOne Data Platform Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="image.png" border={false} width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(596).png" />

## APIs

Axonius uses the <Anchor label="SevOne RESTful API" target="_blank" href="https://www.ibm.com/docs/en/sevone-npm/8.0.0?topic=guides-restful-api-quick-start-guide">SevOne RESTful API</Anchor>.

## Required Ports

Axonius must be able to communicate with the value supplied in [Domain](#parameters) via the following ports:

* **Port 443 (HTTPS)**

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
Fore more details see SevOne documentation:

* <Anchor label="SevOne - User Manager" target="_blank" href="https://www.ibm.com/docs/en/sevone-npm/8.0.0?topic=guides-self-monitoring-quick-start-guide">SevOne - User Manager</Anchor>
* <Anchor label="SevOne - User Role Manager" target="_blank" href="https://www.ibm.com/docs/en/sevone-npm/8.0.0?topic=guides-sevone-nms-admin-notifications-quick-start-guide">SevOne - User Role Manager</Anchor> - In the **User Role Manager** page, under the **Devices and Device Groups Access** tab, provide the user with access to all devices groups.