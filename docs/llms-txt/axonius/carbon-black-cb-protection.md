# Source: https://docs.axonius.com/docs/carbon-black-cb-protection.md

# VMware Carbon Black App Control (Carbon Black CB Protection)

VMware Carbon Black App Control (formerly Carbon Black CB Protection) protects critical systems and servers to prevent unwanted changes and ensure continuous compliance with regulatory mandates.

<br />

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Software, SaaS Applications

<br />

<br />

## APIs

Axonius uses the Carbon Black App Control REST API v1. The following endpoints are called:

* GET /api/bit9platform/v1/computer - Fetch devices
* GET /api/bit9platform/v1/policy - Fetch policies
* GET /api/bit9platform/v1/appInstance - Fetch installed software per device (when Fetch installed software is enabled)
* PUT /api/bit9platform/v1/computer/ id  - Change device policy (enforcement action)
* GET /api/bit9platform/v1/user - Fetch console users (when Fetch users is enabled)
* GET /api/bit9platform/v1/userGroup - Fetch user groups for user enrichment (when Fetch users is enabled)

## Required Permissions

The  following permissions are required:

* View computers — Required to fetch devices (/v1/computer)
* View policies — Required to fetch policies (/v1/policy)
* View login accounts and user roles — Required to fetch users (/v1/user) and user groups (/v1/userGroup)
* Manage computers — Required for the Change Policy enforcement action (PUT /v1/computer/ id )
* Note: If you do not use the Change Policy enforcement action, Manage computers is not required. If the Fetch users advanced setting is disabled (default), View login accounts and user roles is not required.

## Parameters

1. **VMware Carbon Black App Control Domain** – The hostname or IP address of the VMware Carbon Black App Control server.
2. **API Key** - Specify an API Key for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
5. For details about the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![](https://files.readme.io/f7d9876f96a0bb355894c3c0a49118628ff0491346817e51b4e4c5f60a05f40c-image.png)

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch uninstalled devices** *(required, default: True)* - Select this option to fetch uninstalled devices.
2. **Fetch devices per page** *(required, default: 10)* - Set the number of results per page received for a given request, to gain better control of the performance of all connections of this adapter.
3. **Do not fetch instances that have been marked as deleted** *(required, default: False)* - Select this option to exclude instances marked 'deleted' by Carbon Black App Control, otherwise all instances will be fetched.
4. **Fetch installed software** *(default: false)* \_- Select to fetch Installed Software data for each device from AppCatalog.
5. **Fetch users** - Select this option to fetch users and enrich  them with their associated user group data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

### &#x20; API Key

To create an API key, do as follows:

1. As an admin, connect to the VMware Carbon Black App Control admin panel. Navigate to **Login Accounts**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(120\).png)

2. Click **Add User** and fill in the details. In **User Roles**, select the default group **ReadOnly**.
   Make sure you select **Show API token** and generate one. This is the API token we need for the adapter.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(121\).png)

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(122\).png)

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(123\).png)

3. Click **Create & Exit**.

<br />

### Related Enforcement Actions

* [Change Policy - VMware Carbon Black App Control](/docs/change-policy-vmware-carbon-black-protection)