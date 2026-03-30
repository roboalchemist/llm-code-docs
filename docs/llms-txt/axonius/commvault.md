# Source: https://docs.axonius.com/docs/commvault.md

# Commvault

Commvault enables data protection, backup and recovery, and information management solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Commvault server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   The supplied value can be a CommCell Console user name or an Active Directory (AD) user name / email address.

3. **User Domain** *(optional)* - If an Active Directory (AD) user name is supplied in the **User Name** field, specify the user domain. Backslash (\\) prefix is not required.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Commvault.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Commvault.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks in parallel** *(required, default: 30)* - Specify the number of parallel requests all connections for this adapter will send to the Commvault server in parallel at any given point.
2. **Ignore devices without active node** *(default: true)* - Select whether to fetch 'virtual' devices. Commvault also backups SaaS applications like Google Drive, that are not actual devices.
3. **Do not populate LastSeen field for VMs** - Select this option to not populate the LastSeen field.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Commvault REST API](https://documentation.commvault.com/v11/essential/rest_api_overview.html).

## Required Ports

* TCP port 443

## Required Permissions

The value supplied in [User Name](#parameters) should be able to view all the users, laptops and clients in the organization. The role attached to the user should include “browse” and “view” permissions.

## Version Matrix

| Version       | Supported | Notes |
| ------------- | --------- | ----- |
| Commvault v11 | Yes       |       |