# Source: https://docs.axonius.com/docs/edirectory.md

# NetIQ eDirectory

NetIQ eDirectory is a directory service software from NetIQ, previously owned by Novell. It is a hierarchical, object-oriented database used to represent organizational assets in a logical tree, including organizations, units, people, positions, servers, volumes, workstations, applications, printers, services, and groups.

**Related Enforcement Actions:**

* [NetIQ eDirectory - Create or Update User](/docs/create-update-edirectory-user)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetIQ eDirectory server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Base DN** - Enter the Base DN of the memberQueryURL which specifies the search base from which you want to search.

4. **Tree Name** - The name of the NetIQ eDirectory Tree from which you want to fetch the data.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetIQ eDirectory](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetIQ%20eDirectory.png)

## APIs

Axonius uses the [NetIQ edirectory 9.2 API](https://www.netiq.com/documentation/edirectory-92/resources/SimpleLoginOpenapi/#/Session/validateSession).

## Required Permissions

* The value supplied in [User Name](#parameters) must have read and search rights to all objects and attributes in each subtree where access is needed in order to fetch assets. Configure permissions as detailed in [https://www.netiq.com/documentation/edir88/edir88/data/h0000007.html](https://www.netiq.com/documentation/edir88/edir88/data/h0000007.html)

## Supported From Version

Supported from Axonius version 6.1