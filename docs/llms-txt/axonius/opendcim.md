# Source: https://docs.axonius.com/docs/opendcim.md

# openDCIM

openDCIM is a free open-source Data Center Infrastructure Management solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the openDCIM server.

2. **User ID / Username** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **API key / Password** - The API credentials associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. to fetch assets.

5. **Verify SSL**  - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).

6. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **URL Base Prefix** *(optional)* - Enter a suffix to append to the domain (not always requested).

10. **Authentication Method** *(optional, default: LDAP Authentication)* - Select the authentication method from the dropdown.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![openDCIM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/openDCIM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Override Hostname with Label field value** - When selected, the device Hostname is populated with the value specified in the **Label** field in **Advanced View**.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [openDCIM RESTful API](https://wiki.opendcim.org/wiki/index.php/API).

## Required Permissions

The value supplied in [User ID and API Key](#parameters) must have Read access to devices and users:

1. Create a separate account in the openDCIM User Manager for the API access. The account created for the API must have Global Read Access.
2. Generate a key for the account.
3. Supply the User ID and API key values in the [User ID and API Key](#parameters) fields.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| openDCIM 4.1 and lower | No        |       |
| openDCIM 4.2           | Yes       |       |