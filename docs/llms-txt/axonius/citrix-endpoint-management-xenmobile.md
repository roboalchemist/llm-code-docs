# Source: https://docs.axonius.com/docs/citrix-endpoint-management-xenmobile.md

# Citrix Endpoint Management (XenMobile)

Citrix Endpoint Management (formerly XenMobile) is a solution for managing endpoints, offering mobile device management (MDM) and mobile application management (MAM) capabilities.

## Parameters

1. **Citrix Endpoint Management Domain** *(required)* - The hostname or IP address of the Citrix Endpoint Management server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Port** *(required, default: 4443)* - The port used for the connection.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(855\).png)

## Required Permissions

Access to the REST API requires one of the following permissions:

* Citrix Cloud administrator
* Super user permission
* Public API access permission set as part of role-based access configuration. For information, see [Configuring roles with RBAC](https://docs.citrix.com/en-us/xenmobile/server/users/rbac-roles-and-permissions.html).

  * If using RBAC, the following permissions must be granted:
    * Console `>` Devices `>` View software inventory