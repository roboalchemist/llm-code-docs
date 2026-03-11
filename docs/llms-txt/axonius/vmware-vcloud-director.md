# Source: https://docs.axonius.com/docs/vmware-vcloud-director.md

# VMware vCloud Director

VMware vCloud Director is a cloud service-delivery platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

Select the **API Version** you want to use to connect, either **v31.0** or **v36.0 and above**. Each version requires different connection parameters.

### API v31.0

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/vcloud_v31.png" />

1. **vCloud Director Domain** *(required)* - The hostname of the VMware vCloud Director server.
2. **User Name** and **Password** *(required)* - The user name and password for an account that has the [Required Permissions](#required-permissions) to fetch assets.
   The user name has to be in a specific format as described in the [VMWare Cloud Director API](https://techdocs.broadcom.com/us/en/vmware-cis/cloud-director/vmware-cloud-director/10-6/create-a-session-integrated.html#GUID-536ED934-ECE3-4B17-B7E5-F8D0765C9ECB-en_GUID-CC6910F0-057F-457C-911F-EB2C15856BC8).
   You must append either "@system" to the user name or "@orgname". This depends on the role you have set for the user. System administrator users must use "@system" because admin user is not bound to a special organization. org admin or org user must append the organization name.
   For example:
   * superadmin\@system
   * orgadmin\@acme
   * `superadmin@domain.tld@system` (email format)
3. **Is Admin**
   * Select this option if user has admin/system permissions.
   * Clear this option if user does not have admin/system permissions. In this case, the adapter brings VMs into your organization that the user can view or modify.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

### API v36.0 and above

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/vloud_v36.png" />

1. **vCloud Director Domain** *(required)* - The hostname of the VMware vCloud Director server.
2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.
3. **Tenant Name** - Tenant name as supplied by VMware.
4. **Client ID** - Enter the Client ID.
5. **Device Code** - used by the Axonius application to poll VMware Cloud Director for the API token.
   For instructions on how to generate the **Client ID** and **Device Code**, see [here](https://blogs.vmware.com/cloudprovider/2022/07/cloud-director-service-accounts.html).
6. **User Name** and **Password** - The user name and password for an account that has the [Required Permissions](#required-permissions) to fetch assets.
   The user name has to be in a specific format as described in the [VMWare Cloud Director API](https://techdocs.broadcom.com/us/en/vmware-cis/cloud-director/vmware-cloud-director/10-6/create-a-session-integrated.html#GUID-536ED934-ECE3-4B17-B7E5-F8D0765C9ECB-en_GUID-CC6910F0-057F-457C-911F-EB2C15856BC8).

   You must append "@Tenant" to the username.
   For example: User\@Tenant (be sure to replace the 'User' with the actual username and 'Tenant' with your actual Tenant).
7. **Use Provider Authentication** - Check this to use the `sessions/provider` endpoint for authentication. You can only check this parameter if **User Name** and **Password** are configured as well.
8. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
9. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

<Callout icon="📘" theme="info">
  Note

  * When authenticating to API v36.0 and above, you must provide one of the following parameter pairs:

  * **User Name** and **Password**

  * **Tenant Name** and **API Key**

  * **Client ID** and **Device Code**
    Using only one parameter of each pair will result in a connection error.
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Max parallel requests** *(required, default: 50)* - Specify the number of parallel requests Axonius will send to gain better control on the performance of all connections for this adapter.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

**General:** To successfully fetch assets, you must have the "Administrator view" permission.

**For API v31.0:** The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

**For API v36.0 and above:** The value supplied in [API Key/User Name](#parameters) must be associated with credentials that have Read permissions in order to fetch assets and they must have permissions to fetch virtual centers.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                               | Supported | Notes         |
| ------------------------------------- | --------- | ------------- |
| VMWare vCloud Director 9.0 to 9.5     | Yes       | For API v31.0 |
| VMWare vCloud Director later than 9.5 | Yes       | For API v36.0 |