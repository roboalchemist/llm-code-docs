# Source: https://docs.axonius.com/docs/paloalto-prisma-access.md

# Palo Alto Networks Prisma Access

Prisma Access SASE from Palo Alto Networks converges network security, SD-WAN, and autonomous digital experience management in the cloud to provide a secure access service edge.

<Callout icon="📘" theme="info">
  Note

  This adapter is not supported if your Palo Alto Networks Prisma Access product is being hosted/managed by the Palo Alto Panorama service.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.sase.paloaltonetworks.com`)* - The hostname or IP address of the Palo Alto Networks Prisma Access server.

2. **Client ID and Client Secret** *(required)* - Refer to [Service Accounts](https://pan.dev/sase/docs/service-accounts/) for information of how to create a Service Account.

3. **Tenant Service Group ID** *(required)* - Refer to [Tenant Service Groups](https://pan.dev/sase/docs/tenant-service-groups/) for information of how to obtain the Service Group ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PaloAltoPrimsAccess](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PaloAltoPrimsAccess.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Folder List** *(required, default: true)* - The folder from which you want to fetch Users and Devices. Can be one or more of the following:  Shared, Mobile Users, Remote Networks, Service Connections, Mobile Users Container, Mobile Users Explicit Proxy.
2. **Fetch Global Protect Users** - Select this option to fetch Global Protect connected users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Prisma SASE Create an access token](https://pan.dev/sase/api/auth/post-auth-v-1-oauth-2-access-token/)
* [Prisma Access List all local users](https://pan.dev/access/api/prisma-access-config/get-sse-config-v-1-local-users/)
* [Prisma Access List Addresses](https://pan.dev/access/api/prisma-access-config/get-sse-config-v-1-addresses/)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

Service Account should be assigned at least the  “auditor” role in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8