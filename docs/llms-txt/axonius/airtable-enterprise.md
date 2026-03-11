# Source: https://docs.axonius.com/docs/airtable-enterprise.md

# Airtable Enterprise

Airtable Enterprise is a spreadsheet-database hybrid serving as a low-code platform for building collaborative apps.

**Related Enforcement Actions:**

* [Airtable - Create User](/docs/create-airtable-user)
* [Airtable - Suspend User](/docs/suspend-airtable-user)
* [Airtable - Add or Remove User from Group](/docs/assign-airtable-group)
* [Airtable Enterprise - Records Operation](/docs/airtable-enterprise-records-operation)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Airtable Enterprise server, e.g. `api.airtable.com`

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. The API token is provided by Airtable Enterprise.

3. **Enterprise Account ID** - Specify your Airtable Enterprise Account ID.

4. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AirtableEnterprise" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AirtableEnterprise.png" />

## APIs

Axonius uses the [Airtable REST API](https://airtable.com/api).

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have READ permissions in order to fetch assets, as described in the following table.

| Action & Description                                                                    | Link                                                                                       | Scope                   | User Role         |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------- | ----------------- |
| GET enterprise - Returns basic information relevant to the enterprise account.          | `https://api.airtable.com/v0/meta/enterpriseAccounts/{enterpriseAccountId}`                | enterprise.account:read | Enterprise admin  |
| GET user group - Returns basic information relevant to the user group.                  | `https://api.airtable.com/v0/meta/groups/{groupId}`                                        | enterprise.groups:read  | Enterprise member |
| GET user by id - Returns basic information relevant to both internal and external user. | `https://api.airtable.com/v0/meta/enterpriseAccounts/{enterpriseAccountId}/users/{userId}` | enterprise.user:read    | Enterprise admin  |

## Supported From Version

Supported from Axonius version 4.8