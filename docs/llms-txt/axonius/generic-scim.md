# Source: https://docs.axonius.com/docs/generic-scim.md

# Generic SCIM

Generic SCIM, or the System for Cross-domain Identity Management, is a protocol for automating the exchange of user identity information between identity domains and IT systems.

**Related Enforcement Actions:**

* [Suspend Generic SCIM User](/docs/suspend-generic-scim-user)
* [Delete Generic SCIM Group](/docs/delete-generic-scim-group)
* [Add Generic SCIM Entity to Group](/docs/add-generic-scim-entity-to-group)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Generic SCIM server. You need to write the whole URL without the users/groups part. For example, if the full URL to get the users is `https://www.example.com/scim/v2/users`, then you need to input only `https://www.example.com/scim/v2`.

2. **Login Method** *(optional)* - Select a login method, either **Bearer Token** or **Basic Authentication**. If you select **Bearer Token**, then **Token** is displayed. If you select **Basic Authentication**, then **User Name and Password** are displayed.

3. **Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="General SCIM with Bearer Token" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/General%20SCIM%20with%20Bearer%20Token.png" />

*Generic SCIM Settings with Bearer Token Login Method*

<Image alt="General SCIM with Basic Authentication" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/General%20SCIM%20with%20Basic%20Authentication.png" />

*Generic SCIM Settings with Basic Authentication Login Method*

## Supported From Version

Supported from Axonius version 6.1