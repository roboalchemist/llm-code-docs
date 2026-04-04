# Source: https://docs.acceldata.io/documentation/authenticating-using-external-oauth--microsoft-entra-id-.md

# Authenticating Using External OAuth (Microsoft Entra ID)

ADOC supports connecting to Snowflake using **External OAuth with Microsoft Entra ID**. This authentication method uses the **OAuth 2.0 Authorization Code Grant flow**, where Microsoft Entra ID issues OAuth tokens that Snowflake validates to establish a session.

This authentication method is useful for organizations that want to integrate Snowflake access with their **Microsoft Entra ID identity management and authentication policies**.

In this configuration:

- **Microsoft Entra ID** acts as the **Authorization Server**
- **Snowflake** acts as the **Resource Server**
- **ADOC** acts as the **OAuth Client**
- The **end user** authenticates through Microsoft Entra ID and grants access for ADOC to interact with Snowflake on their behalf

For more information about External OAuth with Snowflake, refer to:

- [https://docs.snowflake.com/en/user-guide/oauth-ext-overview](https://docs.snowflake.com/en/user-guide/oauth-ext-overview)
- [https://docs.snowflake.com/en/user-guide/oauth-azure](https://docs.snowflake.com/en/user-guide/oauth-azure?utm_source=chatgpt.com)
- [https://community.snowflake.com/s/article/oauth-authorization-code-grant-entra-id](https://community.snowflake.com/s/article/oauth-authorization-code-grant-entra-id)

---

## OAuth Authorization Code Flow Overview

The OAuth 2.0 Authorization Code flow typically involves four actors:

| Actor | Description | 
| ---- | ---- | 
| OAuth Client | The client application requesting access to the resource (ADOC). | 
| Authorization Server | The identity provider that authenticates the user and issues tokens (Microsoft Entra ID). | 
| Resource Server | The service that hosts the protected resources (Snowflake). | 
| End User | The user who authenticates and grants the application permission to access the resource. | 


In this setup:

1. ADOC redirects the user to Microsoft Entra ID for authentication.
2. The user signs in and grants consent.
3. Microsoft Entra ID returns an **authorization code**.
4. ADOC exchanges the authorization code for **access and refresh tokens**.
5. The access token is used to authenticate requests to Snowflake.

---

## Configuration Overview

Before configuring authentication in ADOC, you must complete the following setup:

1. Configure **Microsoft Entra ID as the OAuth provider**
2. Register applications in **Microsoft Entra ID**
3. Configure **Snowflake External OAuth security integration**
4. Configure **Snowflake user and role mapping**

## Step 1: Register Snowflake as the OAuth Resource in Microsoft Entra ID

Create an **App Registration** in Microsoft Entra ID that represents **Snowflake as the OAuth resource server**.

This application:

- defines the **Application ID URI** that Snowflake trusts
- exposes the scopes that OAuth clients can request

When configuring scopes, use:

```bash
session:role-any
```



This scope is required for the current ADOC implementation.

Record the following value from this registration: `Application ID URI`

This value will later be used as the **audience** in the Snowflake External OAuth integration.

## Step 2: Register ADOC as the OAuth Client

Create another **App Registration** in Microsoft Entra ID that represents **ADOC as the OAuth client**.

This client application will:

- redirect users to Microsoft Entra ID for authentication
- receive the authorization code
- exchange the authorization code for access and refresh tokens

Configure the following **Redirect URI**: `https://<TENANT_BASE_URL>/ui/oauth-success?oauth_type=integration`

After creating the app registration, record the following values:

| **Required Value** | **Description** | 
| ---- | ---- | 
| Client ID | Application (client) ID from Microsoft Entra ID | 
| Client Secret | Client secret generated in the Azure portal | 
| Authorization Endpoint | OAuth authorization endpoint | 
| Token Endpoint | OAuth token endpoint | 
| Entra Application ID | Application ID of the Snowflake resource app | 


These values will be required when configuring the Snowflake connection in ADOC.

## Step 3: Create or Update the Snowflake External OAuth Security Integration

Snowflake must be configured to trust tokens issued by Microsoft Entra ID.

Create an External OAuth security integration using the following configuration.

Example:

```sql
create security integration <INTEGRATION_NAME>
    type = external_oauth
    enabled = true
    external_oauth_type = azure
    external_oauth_any_role_mode = 'ENABLE'
    external_oauth_issuer = 'https://sts.windows.net/<DIRECTORYID>/'
    external_oauth_jws_keys_url = '<AZURE_AD_JWS_KEY_ENDPOINT>'
    external_oauth_audience_list = ('<SNOWFLAKE_APPLICATION_ID_URI>')
    external_oauth_token_user_mapping_claim = 'upn'
    external_oauth_snowflake_user_mapping_attribute = 'login_name';
```



### Important Parameters

| Parameter | Description | 
| ---- | ---- | 
| `external_oauth_type` | Specifies Azure as the identity provider | 
| `external_oauth_any_role_mode` | Allows users to assume any permitted role | 
| `external_oauth_issuer` | Microsoft Entra ID token issuer | 
| `external_oauth`_`_`_`jws_keys_url` | Endpoint used to validate token signatures | 
| `external_oauth_audience_list` | Application ID URI of the Snowflake resource application | 
| `external_oauth`` _token_user`_`_`_`mapping_claim` | Token claim used to map users | 
| `external_oauth_snowflake_user`` _mapping_attribute` | Snowflake user attribute used for mapping | 


## Updating an Existing Security Integration

If an External OAuth integration already exists, update the audience list instead of creating a new integration.

Example:

```sql
ALTER SECURITY INTEGRATION EXTERNAL_OAUTH_AZURE
SET EXTERNAL_OAUTH_AUDIENCE_LIST = (
    '<OLD_SNOWFLAKE_APPLICATION_ID_URI>',
    '<NEW_SNOWFLAKE_APPLICATION_ID_URI>'
);
```



## Important Snowflake Limitations

Snowflake allows **only one External OAuth security integration per Snowflake account per Azure tenant for a given issuer**.

Snowflake identifies the issuer using: `external_oauth_issuer`

If another integration already uses the same issuer, Snowflake returns an error.

In this case, update the existing integration instead of creating a new one.

## Step 4: Create or Verify the Snowflake User

Ensure that the Snowflake user exists and is correctly mapped to the Microsoft Entra ID user.

Example:

```sql
CREATE USER <USER_NAME>
LOGIN_NAME = '<LOGIN_NAME>'
PASSWORD = '<PASSWORD>';
```



Important The value of **LOGIN_NAME must match the Entra ID login name (UPN)**.

## Step 5: Configure Roles and Permissions

Ensure the required role and permissions are assigned to the Snowflake user.

This typically involves:

1. Creating a role
2. Granting permissions on databases, schemas, tables, and warehouses
3. Granting the role to the Snowflake user
4. Setting the role as the user's **default role**

Example operations may include:

- granting warehouse usage
- granting database and schema usage
- granting table privileges

These permissions allow ADOC to run reliability operations against Snowflake.

## Next Step

After completing the Microsoft Entra ID and Snowflake configuration steps, return to the **Snowflake Reliability** setup guide and configure the Snowflake connection in ADOC. For more information, see [External OAuth Authentication (Microsoft Entra ID)](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snowflake-reliability#step-2-add-connection-details) in the Snowflake Reliability documentation.