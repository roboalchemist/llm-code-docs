# Source: https://docs.axonius.com/docs/cisco-cx-cloud.md

# Cisco CX Cloud

CX Cloud combines Cisco technology with AI/ML-driven insights, use cases, and contextual learning.

## Asset Types Fetched

Devices

<br />

## Before You Begin

**Authentication Method**

Client ID/Client Secret

### APIs

Axonius uses the [Cisco Developer API Version 2.0](https://apix.cisco.com/cs/api/v2)

### Permissions

The following API Scopes are required: CX Cloud Inventory v2

### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Cisco CX Cloud server.

2. **Authentication Domain** - (default `https://id.cisco.com/`) A verified DNS domain used to route users to a specific Identity Provider (IdP) for Single Sign-On (SSO) authentication within the Cisco CX Cloud platform.

3. **Client ID** and **Client Secret**  -  Client ID  and  Client Secret associated with a user account that has  permission to fetch assets. Read [Cisco Developer Authentication](https://developer.cisco.com/docs/service-apis/#authentication/application-registration) for information about the Client ID  and  Client Secret.

4. **CX Cloud Customer ID** - Your company's unique identifier within the CX Cloud platform, essential for API access and account managementץ

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CiscoCXCloud" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoCXCloud.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

<br />

<br />