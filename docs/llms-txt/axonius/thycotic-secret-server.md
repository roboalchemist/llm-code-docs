# Source: https://docs.axonius.com/docs/thycotic-secret-server.md

# Delinea Secret Server (Thycotic)

Delinea Secret Server (formerly Thycotic) is a Privileged Access Management (PAM) solution for protecting your privileged accounts, available both on premise or in the cloud.

The Delinea Secret Server adapter enables Axonius to fetch and catalog privileged account assets, including devices, users, groups, and secrets, ensuring comprehensive visibility into privileged access management and security compliance.

## Asset Types Fetched

* Devices

* Users

* Roles

* Groups

* Secrets

* Application Resources

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* User Name and Password

### Required Permissions

The value supplied in **[User Name](#connection-parameters)** must be a local Delinea user with the following role permissions:

* View Folders
* View Groups
* View Roles
* View Secret
* View Users
* View Devices

For more information, see the <Anchor label="Secret Server Role Permissions List" target="_blank" href="https://docs.delinea.com/online-help/secret-server-11-5-x/roles/role-permission-list/index.htm#ViewFolders">Secret Server Role Permissions List</Anchor>.

### APIs

* Axonius uses the <Anchor label="**Secret Server REST API**" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/OAuth/">**Secret Server REST API**</Anchor> to retrieve asset data.
* Vaults use <Anchor label="Secret Server REST API permissions" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/SecretPermissions/operation/SecretPermissionsService_SearchSecretPermissions">Secret Server REST API permissions</Anchor>.
* Rules use <Anchor label="Get SDK Client Rule" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/SdkClientRules/operation/SdkClientRulesService_Get">Get SDK Client Rule</Anchor>.
* Permissions use <Anchor label="Secret Server REST API Get Roles for user" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/Users/operation/UsersService_GetRoles">Secret Server REST API Get Roles for user</Anchor> and <Anchor label="Secret Server REST API Get Role Permissions" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/Roles/operation/RolesService_GetRolePermissions">Secret Server REST API Get Role Permissions</Anchor>.
* Users use <Anchor label="Folder Permissions API" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/FolderPermissions/operation/FolderPermissionsService_Get">Folder Permissions API</Anchor>.
* Devices use <Anchor label="Secret Server REST API Get Server Nodes" target="_blank" href="https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#tag/ServerNodes/operation/ServerNodesService_GetList">Secret Server REST API Get Server Nodes</Anchor>.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Delinea Secret Server URL** - Enter the full URL of the Delinea Secret Server:
   * For on-premises Delinea Secret Server, needs to be in the following format: `https://<hostname>/SecretServer` (for example: `https://demo-server/SecretServer`)
   * For cloud-based Delinea Secret Server, needs to be in the following format: `https://<tenant>.secretservercloud.com` (for example: `https://mycompany.secretservercloud.com`)
2. **User Name** and **Password** - Enter the credentials of a local Delinea user that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Port** - Enter the port number that is used for the connection.

<Image alt="DelineaSecretServerAdapter.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DelineaSecretServerAdapter.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Ignore disabled users** - Select to not fetch disabled users.
* **Fetch Vaults** - Select this option to fetch the secrets the user has access to.
* **Fetch Rules** - Select this option to fetch the SDK rules affecting the user.
* **Fetch Users Roles and Permissions** - Select this option to fetch the users roles and permissions the user has.
* **Fetch Groups** - Select this option to fetch groups.
* **Fetch Devices** - Select this option to fetch devices.
* **Fetch Folder Permissions** - Select this option to fetch permissions associated with folders.
* **Enable Fetch Lists Items** - Select this option to fetch list items from Delinea Secret Server. If selected, the following sub-options are relevant:
  * **Filter lists by listID** - Enter a comma-separated list of List IDs to fetch only specific lists.
  * **Filter by Category** - Enter a category name to filter the fetched lists.
  * **Filter by Active Lists** - Select this option to fetch only active lists.

### Related Enforcement Actions

* [Thycotic - Enable User](/docs/thycotic-enable-user)
* [Thycotic - Suspend User](/docs/thycotic-suspend-user)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version         | Supported | Notes |
| --------------- | --------- | ----- |
| Version 10.7.59 | Yes       |       |