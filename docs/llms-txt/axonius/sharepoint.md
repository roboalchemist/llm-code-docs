# Source: https://docs.axonius.com/docs/sharepoint.md

# SharePoint

SharePoint creates internal website where organizations store, organize, share, and access information from any device.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Groups, Business Applications, Application Resources

## Parameters

To set up the Client ID, Client Secret, and Tenant parameters, see the [Create an Application Key section](/docs/microsoft-azure-active-directory-ad#create-an-application-key) in the Microsoft Entra ID adapter page.

1. **Host Name or IP Address** *(required, default: graph.microsoft.com)* - The hostname or IP address of the SharePoint server.

2. **Tenant ID** *(required)* - The ID for Microsoft Entra ID.

3. **Client ID** *(required)* - The Application ID of the Axonius application.

4. **Client Secret** *(required)* - Specify a non-expired key, generated from the new client secret. This parameter is optional if **Enable Certificate-Based Certificate** is selected.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. **Microsoft Login Environment** *(optional)* - Select the API environment to login to. The default option is *Microsoft Public Login* and you can change that to *Microsoft Gov Login*.

10. **Enable Certificate-Based Authentication** - Enable this so that Axonius can use certificate-based authentication on Microsoft required APIs. When this is enabled, the **Client Secret** parameter is not required.
    * **Private Key File (.pem)** - Click **Upload File** to upload a client private key file in PEM format..
    * **Certificate File (.pem)** - Click **Upload File** to upload a public key file in PEM format.

<Callout icon="📘" theme="info">
  Note

  Certificate-Based Authentication by Microsoft uses a digital certificate to verify the identity of a user or application accessing APIs. Instead of passwords, the certificate’s public and private keys sign and validate requests. This method enhances security as certificates are harder to compromise than traditional passwords.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SPparams](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3SKCU9DM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch lists from sites** - Select this option to fetch list data from the endpoint `sites/{site_id}/lists`.

2. **Fetch sites groups** - Select this option to fetch Sharepoint site groups that only exists within a site. To be able to select and use this configuration, you must do the following:
   * Enable the **Fetch site permissions** advanced configuration.
   * Under [Connection Parameters](/docs/sharepoint#parameters), select **Enable Certificate-Based Authentication**, and provide a Client Private Key File and a Client Certificate File.
     Note that fetching site user roles may increase fetch time significantly.

3. **Fetch site permissions** - Select this option to fetch site permissions. This requires the permission `Sites.Read.All`.

4. **Fetch site users roles** - Select this option to fetch site user roles. To be able to select and use this configuration, you must do the following:
   * Enable the **Fetch site permissions** advanced configuration.
   * Under [Connection Parameters](/docs/sharepoint#parameters), select **Enable Certificate-Based Authentication**, and provide a Client Private Key File and a Client Certificate File.
     Note that fetching site user roles may increase fetch time significantly.

5. **Fetch Sites as** - Select which asset type you want to fetch Sites as. The options available are in accordance with your existing assets.

6. **Only fetch sites from specific lists by name** *(optional)* - Enter names of lists. Axonius will only fetch sites from these lists. If no list names are provided, all lists are fetched.

7. **Fetch lists items** *(optional)* - When fetching lists, also fetch all list items for each list. If no list names are provided, items of all lists are fetched.

8. **Fetch item permissions** *(optional)* - This setting can only be enabled when **Fetch lists items** is also enabled, as it adds the permissions of each list item fetched. Permissions information includes role type, and which applications, devices, groups or users have the role required for this item. The results are displayed on the **Devices** page, for devices of "Item" type, in the field **Item Permissions**.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SharePoint REST operations via the Microsoft Graph REST API](https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph)
Refer to [Get access without a user](https://learn.microsoft.com/en-us/graph/auth-v2-service?view=graph-rest-1.0) for details on obtaining credentials.

To fetch users Axonius uses the [SharePoint List Users endpoint](https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0\&tabs=http#optional-query-parameters).

To fetch site permissions Axonius uses the [List permissions endpoint](https://learn.microsoft.com/en-us/graph/api/site-list-permissions?view=graph-rest-1.0\&tabs=http).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Tenant](#parameters) must be associated with credentials that have ReadOnly Application permissions in order to fetch assets.

The value supplied in [Tenant](#parameters) must be associated with credentials that have User.ReadBasic.All Application permissions in order to fetch users.

The value supplied in [Tenant](#parameters) must be associated with credentials that have Sites.Read.All Application permissions in order to fetch site permissions.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| SharePoint v1.0.0 | Yes       |       |

<br />

**Related Enforcement Actions:**

* [SharePoint - Send CSV](/docs/send-csv-to-sharepoint)
* [SharePoint - Create Item In List](/docs/sharepoint-create-list-item)
* [SharePoint - Delete Item In List](/docs/sharepoint-delete-list-item)
* [SharePoint - Update Item In List](/docs/sharepoint-update-list-item)
* [SharePoint - Delete Users Sites Permissions](/docs/sharepoint-delete-users-sites-permissions)