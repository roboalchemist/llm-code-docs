# Source: https://docs.axonius.com/docs/trustwave-adapter.md

# Trustwave

Trustwave is a managed security services provider focused on managed detection and response.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Trustwave server.

2. **User Name** and **Hash Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Trustwave" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trustwave.png" />

## APIs

Axonius uses the [Trustwave API](https://support.trustwave.com/kb/KnowledgebaseArticle20867.aspx).
API endpoints are:

* **Get list of groups** - [https://localhost:19006/seg/api/groups](https://localhost:19006/seg/api/groups)
* **Get list of members in a group** - [https://localhost:19006/seg/api/groups/3/members](https://localhost:19006/seg/api/groups/3/members)
  * Returns details of each user in the group.

## Supported From Version

Supported from Axonius version 5.0