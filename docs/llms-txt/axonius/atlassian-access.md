# Source: https://docs.axonius.com/docs/atlassian-access.md

# Atlassian Guard

Atlassian Guard (formerly Access) is an identity and access management solution for controlling user access to applications and resources.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.atlassian.com`)* - The hostname or IP address of the Atlassian Guard server.

2. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets. For information about how to obtain the API Token, see [Authentication and authorization](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/intro/#auth).

3. **SCIM Directory ID** *(optional)* - The SCIM directory ID associated with a user account that has permissions to fetch assets. For information about how to obtain the Directory ID, see [Authentication and authorization](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/intro/#auth). The SCIM directory ID is required to fetch SCIM users.

4. **ORG ID** *(optional)* - The ORG ID is required to fetch ORG users.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Atlassian Access](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Atlassian%20Access.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users of sub type SCIM user from Endpoint: scim/directory/`{SCIM Directory ID}`/Users** *(default: true)* - Select whether to fetch users of the sub-type SCIM user from Endpoint: scim/directory/`{SCIM Directory ID}`/Users.
2. **Fetch Users of sub type ORG user from Endpoint: admin/v1/orgs/`{ORG ID}`/users** *(default: false)* - Select whether to fetch users of the sub-type ORG user from Endpoint: admin/v1/orgs/`{ORG ID}`/users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [User Provisioning REST API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/intro/#pagination).

## Required Permissions

The value supplied in [User Name](#parameters) must have read users permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| SCIM version 1 | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1