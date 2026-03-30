# Source: https://docs.axonius.com/docs/hitachi-operations-center.md

# Hitachi Operations Center

Hitachi Ops Center provides data  infrastructure management including automation, analytics, and protection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Hitachi Ops Center server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="hitachioperationscenter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/hitachioperationscenter.png" />

## APIs

Axonius uses the following APIs:

* [Ops Center Administrator REST API](https://knowledge.hitachivantara.com/Documents/Management_Software/Ops_Center/Administrator/10.0.x/API_resources/01_Using_the_Ops_Center_Administrator_REST_API)
* [Server management resources](https://knowledge.hitachivantara.com/Documents/Management_Software/Ops_Center/Administrator/10.0.x/API_resources/16_Server_management_resources)
* [Token management](https://knowledge.hitachivantara.com/Documents/Management_Software/Ops_Center/Administrator/10.0.x/API_resources/02_Token_management)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have read only permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8