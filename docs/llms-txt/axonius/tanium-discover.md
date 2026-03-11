# Source: https://docs.axonius.com/docs/tanium-discover.md

# Tanium Discover

The Tanium Discover adapter scans for unmanaged assets with almost no impact on the network.

## Parameters

1. **Hostname or IP Address** *(required)* - The Hostname or IP address of the Tanium server that Axonius can communicate with via the [Required Ports](#required-ports). This adapter supports both on-premise and Tanium Cloud instances. When connecting to a Tanium Cloud instance, "**-api**" must be added to the end of the subdomain of your Tanium Cloud instance. For example: "*domain.cloud.tanium.com*" should be entered as "*domain-api.cloud.tanium.com*".
2. **User Name or API Token ID** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the ID of the API token.  The Token ID column in Tanium may be hidden.
3. **Password or API Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the API token string.

<Callout icon="📘" theme="info">
  More information on API Tokens

  * When connecting to a Tanium Cloud instance, an API token **must** be used.
  * When creating an API token in Tanium, the default value for "Expire in Days" is 7. It is recommended to set this value to the maximum allowed value of 365.
    -Refer to the Tanium Documention on [Managing API tokens](https://docs.tanium.com/platform_user/platform_user/console_api_tokens.html) for more information.
</Callout>

4. **Fetch Unmanaged** *(required, default: True)* - Fetch assets from **Discover** `>` **Interfaces** `>` **Unmanaged**.

5. **Fetch Unmanageable** *(required, default: True)* - Fetch assets from **Discover** `>` **Interfaces** `>` **Unmanageable**.

6. **Fetch Managed** *(required, default: False)* - Fetch assets from **Discover** `>` **Interfaces** `>` **Managed**.

7. **Fetch Ignored** *(required, default: True)* - Fetch assets from **Discover** `>` **Interfaces** `>` **Ignored**.

8. . **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

9. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="tanium_discover_add_connection_dialog.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_discover_add_connection_dialog.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Trust Tanium Discover hostname** *(required, default: False)* - Select whether to consider the Tanium Discover hostname value as the device hostname.
   * If enabled, all connections for this adapter will set the **Aggregated:Host Name** with the fetched **Tanium Discover:Discover Hostname** field value.
   * If disabled, all connections for this adapter will not set the **Aggregated:Host Name** with the fetched **Tanium Discover:Discover Hostname** field value.
2. **Number of assets to fetch per page** *(required, default: 100)*  - Control the number of assets that are fetched per page.
3. **Number of seconds to wait in between each page fetch** *(required, default: 1)* - Control the number of seconds to wait in between each page.
4. **CIDR exclude list** *(optional)* - Specify a comma-separated list of CIDR blocks (for example: 192.168.20.0/24,192.168.30.0/24). The adapter will not fetch devices with an IP address that is in the range of any of the comma-separated list of CIDR blocks defined in this field .
5. **CIDR  include list** *(optional)* -  Specify a comma-separated list of CIDR blocks (for example: 192.168.20.0/24,192.168.30.0/24), where the adapter only fetches devices with an IP address that is in the range of any of the comma-separated list of CIDR blocks defined.
6. **Constrain configured fetch types** - Select this option to verify that only devices selected in the basic configuration will be ingested in Axonius.
7. **Deduplicate devices** - Select this option to deduplicate devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following ports:

* **TCP port 443**: REST API

## Required Permissions

* [Required Module Permissions](#required-module-permissions)

## Required Module Permissions

A Module Role named **Discover Read Only User** exists that provides these Module Permissions:

1. Show Discover
2. Discover Asset Read

## Assigning Required Permissions

These are the steps to assign the [Required Permissions](#required-permissions) to the value supplied in [User Name](#parameters):

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with an account that has the permissions necessary to edit users.
2. In the navigation menu:
   1. Go to the **Administration** `>` **Users** page.
3. In the **Users** Page:
   1. Select the value supplied in [User Name](#parameters) from the list of users.
   2. Click **View User**.
4. In the **User Administration** page in the **Roles and Effective Permissions** section:
   1. Click **Edit Roles**.
5. In the **Assign Roles** page in the **Role Management** `>` **Grant Roles** section:
   1. Click **Edit**.
6. In the **Edit Grant Roles** dialog window:
   1. Select the role named **Discover Read Only User**.
   2. Click **Save**.
7. In the **Assign Roles** page:
   1. Click **Show Preview to Continue**.
   2. Click **Save**.
8. In the **Notice** dialog window:
   1. Click **Continue**.
9. The **User Administration** page should look like this:

<Image alt="tanium_useradmin_discover" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_useradmin_discover.png" />

10. Perform the steps in [Verifying Permissions](#verifying-permissions)

## Verifying Permissions

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with the values supplied in [User Name and Password](#parameters).
2. In the navigation menu:
   1. Go to the **Discover** page.
3. In the **Discover** menu of the **Discover** page:
   1. Go to the **Interfaces** `>` **All** page.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                               | Supported | Notes                                                                      |
| ------------------------------------- | --------- | -------------------------------------------------------------------------- |
| Tanium versions prior to 7.3.314.3424 | No        | This adapter utilizes the REST API, which was added in Tanium 7.3.314.3424 |
| Tanium 7.3.314.3424                   | Yes       |                                                                            |
| Tanium 7.3.314.3668                   | Yes       |                                                                            |
| Tanium 7.3.314.4147                   | Yes       |                                                                            |
| Tanium 7.3.314.4250                   | Yes       |                                                                            |
| Tanium Cloud                          | Yes       |                                                                            |

### Discover Module Versions

Modules within Tanium have their own version which is separate from the platform version.

| Version                    | Supported | Notes |
| -------------------------- | --------- | ----- |
| Discover Module 2.11.1.18  | Yes       |       |
| Discover Module 3.1.0.0185 | Yes       |       |
| Discover Module 3.1.2.0007 | Yes       |       |