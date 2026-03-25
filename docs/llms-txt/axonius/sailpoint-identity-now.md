# Source: https://docs.axonius.com/docs/sailpoint-identity-now.md

# SailPoint IdentityNow

SailPoint IdentityNow is a SaaS identity and access management (IAM) solution.

## Use Cases the Adapter Solves

The SailPoint IdentityNow adapter could be used in various use cases, including:

* **Fetch User Accounts and Identity Data** - Aggregate user identities, roles, and entitlements managed by SailPoint into the Axonius inventory.
* **Correlate Users to Devices** - Link SailPoint user identities to their associated devices from other adapters.
* **Query for Access and Entitlements** - Identify devices associated with users based on their specific roles or access privileges.
* **Configure Automated Actions on Identity Status** - Use a user identity status as a trigger for Enforcement Center actions, such as tagging a device or creating a service desk ticket.

## Asset Types Fetched

The SailPoint IdentityNow adapter fetches the following assets:

* Users
* Application Extensions
* Admin Managed Extensions
* User-Initiated Extensions
* Application Add-Ons
* Roles
* Groups
* Application Extension Instances
* Admin Managed Extension Instances
* User-Initiated Extension Instances
* Application Add-On Instances
* Application Keys
* SaaS Applications
* Accounts/Tenants

## Data Retrieved through the Adapter

The following data is retrieved through the SailPoint IdentityNow adapter:

* **User Details** - Core identity attributes such as username, full name, email address, and employee ID.
* **Account Status** - The user lifecycle state (for example: active, inactive, terminated).
* **Organizational Data** - Information such as manager, department, and job title.
* **Entitlements** - Specific permissions, roles, and access profiles that are assigned to the user.
* **Accounts** - Associated application accounts that the identity has (for example: their specific account within Salesforce and Active Directory).
* **Group Memberships** - The security or access groups to which the user belongs.

## Before You Begin

### APIs

Axonius uses the following APIs:

* <Anchor label="SailPoint List of Public Identities API" target="_blank" href="https://developer.sailpoint.com/idn/api/v3/get-public-identities/">SailPoint List of Public Identities API</Anchor>
* <Anchor label="SailPoint Accounts list API" target="_blank" href="https://developer.sailpoint.com/idn/api/v3/list-accounts/">SailPoint Accounts list API</Anchor>

### Required Permissions

* The value supplied in [Client ID](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.
* The SailPoint personal access token must be assigned to the following grant types:
  * [CLIENT\_CREDENTIALS](https://developer.sailpoint.com/idn/api/authentication/#client-credentials-grant-flow)
  * [REFRESH\_TOKEN](https://developer.sailpoint.com/idn/api/authentication/#refresh-token-grant-flow)

### Additional Resources Required per Asset/Entity Type

| Asset/Entity Type           | API Endpoint(s)                              | Required Axonius Product                      | Type                                                                                                                | Permission(s)                                                                                                       | Scope(s)                                                                                           |
| --------------------------- | -------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Users                       | v3/public-identities                         | -                                             | Personal Access Token                                                                                               | User levels: USER                                                                                                   | sp:scopes:default                                                                                  |
| Users (Identities)          | v3/accounts                                  | Identities                                    | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, SOURCE\_ADMIN, SOURCE\_SUBADMIN, HELPDESK                                                  | idn:accounts:read                                                                                  |
| Accounts                    | v3/sources                                   | Axonius SaaS Applications                     | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, SOURCE\_ADMIN, SOURCE\_SUBADMIN, ROLE\_SUBADMIN                                            | idn:sources:read, idn:sources:manage                                                               |
| Roles / Rules               | v3/roles                                     | Axonius SaaS Applications, Axonius Identities | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, ROLE\_ADMIN, ROLE\_SUBADMIN                                                                | idn:role-unchecked:read, idn:role-unchecked:manage, idn:role-checked:manage, idn:role-checked:read |
| Groups                      | beta/workgroups                              | -                                             | Personal Access Token                                                                                               | -                                                                                                                   | idn:workgroup:read                                                                                 |
| Security Roles (1)          | beta/entitlements, v3/search                 | Identities                                    | Personal Access Token                                                                                               | User levels: Any                                                                                                    | idn:entitlement:read, idn:entitlement:manage                                                       |
| Security Roles (2)          | v3/access-profiles, v3/search                | Identities                                    | Personal Access Token **or** Client Credentials                                                                     | (Only for Client Credentials) User levels: ORG\_ADMIN, ROLE\_ADMIN, ROLE\_SUBADMIN, SOURCE\_ADMIN, SOURCE\_SUBADMIN | idn:access-profile:read                                                                            |
| Certification Campaigns     | v3/campaigns                                 | Identities                                    | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, CERT\_ADMIN, REPORT\_ADMIN                                                                 | idn:campaign:read, idn:campaign:manage, idn:campaign-report:read, idn:campaign-report:manage       |
| Certifications of campaigns | v3/certifications                            | Identities                                    | [Personal Access Token](https://developer.sailpoint.com/docs/api/v3/identity-security-cloud-v-3-api#authentication) | -                                                                                                                   | sp:scopes:all                                                                                      |
| Review Items                | v3/certifications/`{id}`/access-review-items | Identities                                    | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, CERT\_ADMIN                                                                                | -                                                                                                  |
| Approvers                   | v3/certifications/`{id}`/reviewers           | Identities                                    | Personal Access Token                                                                                               | User levels: ORG\_ADMIN, CERT\_ADMIN                                                                                | idn:certification:read                                                                             |

### Adapter Integration Setup

<Callout icon="💡" theme="warn">
  Important

  While to access SaaS data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
</Callout>

1. Log in to IdentityNow as an organizational administrator (ORG\_ADMIN).
2. Navigate to the **Admin UI** `>` **Dashboard** and select the **Overview** page.
3. Select **Preferences** from the drop-down menu under your username
4. Select **Personal Access Tokens**.
5. Click **New Token** and enter a meaningful description to help differentiate the token from others.
6. Click **Create Token** to generate and view the two components that comprise the token: **Client ID** and **Client Secret**. Copy them to use when [connecting the adapter in Axonius](/docs/sailpoint-identity-now#required-parameters).

### Supported from Version

Supported from Axonius version 4.7.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the SailPoint IdentityNow server. The field format is `https://sailpoint.api.identitynow.com/v3`.
2. **Client ID** and **Client Secret** - Enter the Client ID and Client Secret for an account that has the [Required Permissions](#required-permissions) to the API. To obtain the Client ID and Client Secret via your personal access token, see [Personal Access Tokens](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens) .

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/SailPoint_IdentityNow_Required.png" className="border" />

### Optional Parameters

1. **SSO Provider** - Required only for accounts with **Axonius SaaS Applications**.
   If your organization uses SailPoint Identify Now for SSO, this adapter can be set as an SSO provider. See [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider)  for more information.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

* [SailPoint IdentityNow Advanced Settings](https://docs.axonius.com/axonius-help-docs/docs/sailpoint-identitynow-advanced-settings)

### Related Enforcement Actions

* [SailPoint IdentityNow - Create Certification Campaign](/docs/identity-now-create-campaign)