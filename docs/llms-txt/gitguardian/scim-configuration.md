# Source: https://docs.gitguardian.com/platform/enterprise-administration/scim-configuration.md

# Configure SCIM

> Configure SCIM provisioning to automatically synchronize users and groups between your identity provider and GitGuardian workspace.

System for Cross-domain Identity Management (SCIM) lets you manage GitGuardian users and teams directly from your Identity Provider (IdP). Based on changes in your IdP, SCIM automatically creates, updates, deactivates, and deletes users, and creates/manages teams from IdP groups.

:::info
SCIM supports user and team provisioning/deprovisioning for Okta and Microsoft Entra ID.
:::

## Prerequisites

- SCIM requires [Single Sign-On (SSO)](./saml-sso-configuration) to be configured first.
- SCIM is supported for Okta and Microsoft Entra ID.

## SCIM Features

GitGuardian supports:

- Manage the full user lifecycle: provision, activate, deactivate, and delete based on your IdP.
- Provision and manage teams from IdP groups.

## Enable SCIM in GitGuardian

1. Navigate to **Settings > [Authentication](https://dashboard.gitguardian.com/settings/workspace/auth)** in your GitGuardian workspace.
2. Under **SCIM**, toggle the option to enable SCIM integration.
   ![gitguardian scim enable](/img/platform/enterprise-administration/scim_enable.png)
3. Follow the instructions in the **Set up SCIM in your IdP** section.

Once SCIM is enabled, your users can be synchronized with your IdP, and user deprovisioning can occur automatically.

:::info Unlinked Members
You may see a message indicating that some users are **not linked to your IdP**. These users won't be managed by SCIM.

- **Review the Members List**: Check the unlinked users.
- **Deactivate if Necessary**: Manually deactivate any users who shouldn't have access.

This typically happens for users added before SCIM was enabled or not assigned in your IdP. SCIM only manages linked users.
:::

## Set up SCIM in your IdP

To configure SCIM, you will need to provide the SCIM endpoint and configure the corresponding SCIM settings in your IdP. Here's a high-level overview for common IdPs:

Follow the specific steps for your IdP to enable SCIM integration. Most IdPs provide an option to configure SCIM via their API or dashboard settings. You will need to provide:

- **GitGuardian SCIM Endpoint**: `https://api.gitguardian.com/v1/scim/v2` (or `https://gitguardian.mycorp.local/exposed/v1/scim/v2` for self-hosted)
- **API Token**: Use a GitGuardian [service account](https://dashboard.gitguardian.com/api/service-accounts) token with `members:write` and `teams:write` permissions.

Each IdP's SCIM configuration page will have specific instructions. Refer to the documentation for your IdP for details on how to enter the SCIM endpoint and configure API credentials.

:::info Google & Keycloak Users
Google only supports automatic provisioning for specific apps, so SCIM cannot be used for provisioning with Google at this time. However, we are planning to support SCIM for Google and publish our app in the future.

The [scim-for-keycloak plugin](https://scim-for-keycloak.de/) has a bug that causes confusion with the `externalId` value, which is used for making SCIM requests to GitGuardian, so it won't work with our SCIM integration. For more details, see the issue [here](https://github.com/Captain-P-Goldfish/scim-for-keycloak/issues/126).
:::

## Set up procedures

### Okta

You can configure SCIM using either the [GitGuardian app from the Okta Integration Network](#okta-oin-app) (recommended) or a [custom SAML app](#okta-custom-scim).

:::info Important Note
If users are assigned to the Okta app before SCIM is enabled, they won't be deactivated in GitGuardian when later unassigned. To ensure proper deactivation:

1. Duplicate the original Okta group (same members).
2. Assign the duplicate group to the app.
3. Unassign the original group from the app.

:::

#### Okta OIN app

If you've installed the GitGuardian app from the [Okta Integration Network](https://www.okta.com/integrations/gitguardian/), SCIM provisioning is built-in and Okta Verified.

##### Supported features

- **Create users**: Provision new users from Okta to GitGuardian
- **Update user attributes**: Sync user profile changes from Okta
- **Deactivate users**: Deactivate users when unassigned or disabled in Okta
- **Import users**: Import existing GitGuardian users into Okta
- **Push groups**: Sync Okta groups as GitGuardian teams

##### Generate API Token in GitGuardian

Before configuring SCIM in Okta, you need to create a service account token in GitGuardian:

1. In your GitGuardian dashboard, navigate to **API > [Service accounts](https://dashboard.gitguardian.com/api/service-accounts)**.
2. Click **Create service account**.
3. Enter a name (e.g., "Okta SCIM") and select the following permissions:
   - `members:write`
   - `teams:write`
4. Click **Create** and copy the generated token.

   ![GitGuardian service account token](/img/platform/enterprise-administration/scim-providers/api_token_scim.png)

##### Configuration steps

1. In Okta, navigate to your GitGuardian application and go to the **Provisioning** tab.
2. Under **Settings > Integration**, you will see that the provisioning integration is partner-built by GitGuardian.

   ![okta app provisioning tab](/img/platform/enterprise-administration/scim-providers/okta_app_provisioning_tab.png)

3. Click **Configure API Integration**.
4. Check the box for **Enable API integration**.
5. Enter your GitGuardian SCIM credentials:
   - **API Token**: Paste the service account token generated above.
   - **Import Groups**: Check this option if you want to sync groups as teams.
6. Click **Test API Credentials** to verify the connection. You should see "GitGuardian SCIM was verified successfully!".

   ![okta app api integration](/img/platform/enterprise-administration/scim-providers/okta_app_api_integration.png)

7. Click **Save**.
8. Go to **Settings > To App** and enable **Create Users**, **Update User Attributes**, and **Deactivate Users**.

   :::caution
   Make sure to disable **Set password when creating new users** (enabled by default).
   :::

   ![okta app provisioning to app](/img/platform/enterprise-administration/scim-providers/okta_app_provisioning_to_app.png)

9. Click **Save**.
10. Go to the **Assignments** tab to assign users.
11. Go to the **Push Groups** tab to sync Okta groups as GitGuardian teams.

#### Okta custom SCIM

If you're using a custom SAML application, follow these steps to enable SCIM:

1. In **Okta**, navigate to the **General** settings of your GitGuardian app and check the box for **Enable SCIM provisioning**.
   ![okta scim enable](/img/platform/enterprise-administration/scim-providers/okta_enable_scim.png)

2. In the **Provisioning** settings of your Okta app, configure the following:

   - Set the **SCIM Connector Base URL** to:
     `https://api.gitguardian.com/v1/scim/v2` (or `https://gitguardian.mycorp.local/exposed/v1/scim/v2` for self-hosted).
   - Use **email** as the unique identifier field for users. Username field must be an email.
   - Enable the **Push New Users**, **Push Profile Updates** and **Push Groups** settings.
   - Select **HTTP Header** for authentication mode and add the **service account token** in the **Authorization HTTP header**.
     ![okta scim connection](/img/platform/enterprise-administration/scim-providers/okta_scim_connection.png)

3. Check the **Create Users**, **Update User Attributes** and **Deactivate Users** options under the **Provisioning to app** settings.
   ![okta scim provisioning](/img/platform/enterprise-administration/scim-providers/okta_scim_provisioning.png)

4. Finally, in **Assignments**, assign the users. In **Push Groups**, assign the groups you want to sync with GitGuardian.

### Microsoft Entra ID

:::info important note
When a user is unassigned from the GitGuardian app in Entra ID, no deactivation request is sent. To deactivate, the user must be disabled in Entra ID.
:::

#### Generate API Token in GitGuardian

Before configuring SCIM in Entra ID, you need to create a service account token in GitGuardian:

1. In your GitGuardian dashboard, navigate to **API > [Service accounts](https://dashboard.gitguardian.com/api/service-accounts)**.
2. Click **Create service account**.
3. Enter a name (e.g., "Entra ID SCIM") and select the following permissions:
   - `members:write`
   - `teams:write`
4. Click **Create** and copy the generated token.

   ![GitGuardian service account token](/img/platform/enterprise-administration/scim-providers/api_token_scim.png)

#### Configuration steps

1. In **Microsoft Entra ID** (formerly Azure Active Directory), navigate to the **Enterprise Applications** section.
2. Select your GitGuardian app, then go to **Provisioning** and set the **Provisioning Mode** to **Automatic**.
3. Enter the following credentials:
   - **Secret Token**: Paste the service account token generated above.
   - **Tenant URL**: `https://api.gitguardian.com/v1/scim/v2` (or `https://gitguardian.mycorp.local/exposed/v1/scim/v2` for self-hosted).
4. In the **Attribute Mappings** section under **Provision Microsoft Entra ID Users**, configure the following mappings to match GitGuardian's SCIM requirements:
   - Target Object Actions: Set actions to `Create`, `Update` and `Delete` for the target object.
   - Attribute Mappings:
     - `userName`: Map this to `userPrincipalName`
     - `active`: Map this to `Switch([IsSoftDeleted], , "False", "True", "True", "False")`
     - `name.givenName`: Map this to `givenName`
     - `name.familyName`: Map this to `surname`
     - `externalId`: Map this to `userPrincipalName`
       ![ms intra scim attribute](/img/platform/enterprise-administration/scim-providers/ms_entra_id_attribute_mappings_users.png)
5. In the **Attribute Mappings** section under **Provision Microsoft Entra ID Groups**, configure the following mappings to match GitGuardian's SCIM requirements:
   - Target Object Actions: Set actions to `Create`, `Update` and `Delete` for the target object.
   - Attribute Mappings:
     - `displayName`: Map this to `displayName`
     - `externalId`: Map this to `objectId`
     - `members`: Map this to `members`
       ![ms intra scim attribute](/img/platform/enterprise-administration/scim-providers/ms_entra_id_attribute_mappings_teams.png)
6. Save the mapping and sync the users and teams.

## SCIM settings

Once SCIM is enabled, additional settings are available in your [Authentication settings page](https://dashboard.gitguardian.com/settings/workspace/auth/saml) to control the behavior of SCIM-provisioned members.

### Default team membership permission

This setting controls the **incident permission level** assigned to members synchronized via SCIM when they are added to a team. The available options are:

- **Can view**: Members can view incidents assigned to their team.
- **Can edit**: Members can view and edit incidents assigned to their team.

By default, this is set to **Can edit**. You can change this at any time from the Authentication settings page.

### Enable notifications for SCIM operations

When enabled, GitGuardian sends **notifications whenever SCIM updates affect users or teams** in your workspace. This includes events such as:

- User provisioning or deactivation
- Team creation, update, or deletion
- Membership changes

This setting is **disabled by default**. Toggle it on if you want members to stay informed about SCIM-driven changes.

## FAQ

**Can I use SCIM for provisioning teams?**

Yes, SCIM supports team provisioning for Okta and Microsoft Entra ID. Teams are automatically created and managed in your workspace when groups are added or updated in your IdP. Ensure your service account token has `teams:write` permissions.

**How do I link GitGuardian to my IdP for SCIM?**

You will need to configure SCIM in your IdP by entering the provided SCIM endpoint and API token. Each IdP has its own process for linking SCIM integrations. Follow the relevant setup instructions for your IdP.

**Does GitGuardian support Just-In-Time (JIT) provisioning with SCIM?**

SCIM now supports user provisioning, activation, deactivation, and deletion. JIT provisioning via SSO is also available, while SCIM gives you more control over the user lifecycle for provisioning, activation, deactivation, and deletion.
