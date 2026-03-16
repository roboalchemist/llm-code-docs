# Source: https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md

# Set up SSO with a SAML-based IdP

This guide walks through configuring a generic SAML-based identity provider (IdP) for use with Apollo SSO.
If you use Okta or Microsoft Entra ID as your IdP, instead see the corresponding guide for your IdP:

* [Okta](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta)
* [Microsoft Entra ID](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id) (formerly known as Azure Active Directory)

Once you've set up your integration, you need to assign users to it in your IdP so they can access GraphOS Studio via SSO.
Before assigning users, Apollo recommends setting a [default GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#set-default-graphos-role) for users logging in via SSO.
You can also configure Okta to [assign GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#assign-graphos-roles-in-your-idp) to your users based on their Okta groups.

## SSO impact on user accounts and access

For organizations using SSO, access to GraphOS is exclusively managed through your IdP.
Any [invitation links](https://www.apollographql.com/docs/graphos/org/members/#inviting-members) created before SSO setup will be automatically revoked and you won't be able to create new invitation links once SSO is enabled.
To give team members access, you must assign them to the GraphOS application in your IdP.

Once your SSO connection is finalized, all non-SSO user accounts are removed from your GraphOS organization. This means:

* If team members could previously login before you implemented SSO, they must re-login to GraphOS Studio via SSO.
* Signing in via SSO creates new user profiles separate from previous non-SSO user profiles.
* Any [personal API keys](https://www.apollographql.com/docs/graphos/platform/access-management/account#personal-api-keys) associated with non-SSO user profiles will be lost.
  * [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are unaffected and remain functional.
* You must reassign any [GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) associated with previous user profiles.

## Prerequisites

Setup requires:

* A GraphOS user account with the [**Org Admin** role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles)
  * Check the **Members** tab in [GraphOS Studio](https://studio.apollographql.com/) to see your role and which team members are org admins
* Administrative access to your IdP

## Setup

### Step 1. Enter your SSO details

### Step 2. Create a custom application

1. Once you reach **Step 2: Configure Your IdP** in the wizard, open your IdP's admin dashboard in a separate browser tab.

2. Create a new application. While doing so, set the following values:

   * **App Name**: `Apollo GraphOS`
   * **Logo**: [Apollo logo](https://www.apollographql.com/docs/img/apollo-sk-logo.png) (optional)

3. If your IdP permits it, upload the SAML XML metadata file provided by the GraphOS setup wizard. Otherwise, manually enter the following metadata values in your IdP:

   * Set your **Single Sign-on URL** or **ACS URL** to the Single Sign-on URL provided by the wizard. You can also use this value for the following fields:

     * **Recipient**
     * **ACS (Consumer) URL Validator**
     * **ACS (Consumer) URL**

   * Set your **Entity ID** to the Entity ID value provided by the wizard.

4. Set the following user attributes:

   * `sub`: `user.email`
     * The `sub` attribute should uniquely identify any particular user to GraphOS. In most cases, `user.email` or `user.mail` provides this unique mapping.
   * `email`: Your IdP's email attribute, often something like `user.email`
   * `given_name`: Your IdP's first name attribute, often something like `user.firstName`
   * `family_name`: Your IdP's last name attribute,often something like `user.lastName`

5. Save the configuration in your IdP.

6. In the GraphOS setup wizard, select whether your IdP requires signing an AuthnRequest.

7. Click **Next**.

### Step 3. Share SAML metadata with Apollo

In the GraphOS setup wizard, enter your application's metadata URL or metadata file.
Consult your IdP's documentation if you need assistance finding it.
Click **Next**.

### Step 4. Verify details

The GraphOS Studio setup wizard populates your SSO metadata based on the URL you entered in the last step. Verify the values are correct. Consult your IdP's documentation if you need assistance finding them.

Once you've verified the values or corrected them, click **Next**.

### Step 5. Verify SSO Configuration

To verify that your SSO configuration works, click **Login with new SSO** in the GraphOS Studio wizard.
This button launches a new login session in a new browser tab. You may need to assign yourself to the application in your IdP first.

Once you successfully login using your new configuration, click **Continue**.

### Step 6. Enable SSO

Once you've verified your new SSO configuration works, you'll be prompted to finalize your configuration.

Once your SSO connection is finalized, all non-SSO user accounts are removed from your GraphOS organization. This means:

* If team members could previously login before you implemented SSO, they must re-login to GraphOS Studio via SSO.
* Signing in via SSO creates new user profiles separate from previous non-SSO user profiles.
* Any [personal API keys](https://www.apollographql.com/docs/graphos/platform/access-management/account#personal-api-keys) associated with non-SSO user profiles will be lost.
  * [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are unaffected and remain functional.
* You must reassign any [GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) associated with previous user profiles.

You can set a [default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#set-default-graphos-role) for any users signing in with SSO. Apollo recommends setting the default role before [assigning users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#assign-users-in-your-idp).

## Set default GraphOS role

Once you've enabled SSO, you can optionally set the default [GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) for new users logging in via SSO.
If you don't set a default, the default role is **Consumer**.
To update the default role for new SSO users, go to **Settings** > **Security** > **Single sign-on** and click **Update new user role**.

## Assign GraphOS roles in your IdP

Apollo recommends using *either* SSO or SCIM for role assignment.
If you use both, role assignments will overwrite one another.

### Setup

#### Step 1: Add user attributes

1. In your IdP administrator dashboard, add one or both of the following attributes:

   * For organization-wide roles, add an attribute named `graphos_org_role`.

     The following `string` values are valid GraphOS [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles):
     * `ORG_ADMIN`
     * `GRAPH_ADMIN`
     * `CONTRIBUTOR`
     * `DOCUMENTER`
     * `OBSERVER`
     * `CONSUMER`
     * `BILLING_MANAGER`

   * For [graph-specific roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-specific-member-roles), add an attribute named `graphos_graph_roles`. It takes an array of strings.

2. Still in your IdP, go to the GraphOS Studio application you created during SSO setup.

3. Add new attribute statements for the user attribute(s) you previously created. The names should be `graphos_org_role` or `graphos_graph_roles`.

4. Save your changes.

#### Step 2: Assign organization-wide GraphOS roles to groups

Follow these steps to assign [organization-wide](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) to groups.

1. Assign groups to your GraphOS Studio application if you haven't already done so.

2. Select the appropriate **GraphOS Organization Role** for each group.

3. If your IdP uses group prioritization, ensure the groups are ordered correctly. For example, in Okta, the groups with more privileged access should have a higher priority.

   * For example, imagine an **Apollo Admins** group has the highest priority. Suppose this group has the most privileges as **Org admin**s.
   * Next, suppose the **Feature Team 1** has the **Graph Admin** role.
   * The rest of the **Engineering** organization has the **Contributor** role.
   * This priority order ensures a user belonging to the Apollo Admin group has Org admin privileges, even if they also belong to Feature Team 1 and the Engineering groups. If a user only belongs to the Engineering group, they receive the Contributor role.

   Review your IdP's prioritization documentation to confirm the correct order.

#### Step 3: Assign graph-specific roles to individual users

Follow these steps to assign [graph-specific roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-specific-member-roles) to individuals or groups.
If a user has both organization-wide and graph-specific roles set, the graph-specific roles take precedence.

1. In your IdP, go to where you assign individuals and groups access to your GraphOS Studio application.
2. Edit any individually assigned user or group and add as many graph-specific roles as necessary, using the `<graph-id>:<graph-role>` format for each graph-specific role.

   * A graph's ID is the portion of the graph ref before the `@`.
   * Valid values for graph-specific roles are `GRAPH_ADMIN`, `CONTRIBUTOR`, `DOCUMENTER`, `OBSERVER`, and `CONSUMER`.
   * Ensure the delimiter between the graph ID and role is a colon (`:`).
   * For example, `docs-sandbox:DOCUMENTER` is a valid string for assigning the Documenter role to a graph with the ID `docs-sandbox`.

A user's graph-specific role must have higher permissions than their organization-wide role to be applied.

### Role assignment behavior

Once you've completed the previous steps, whenever a user signs into GraphOS, they receive the role based on their IdP groups and/or individual graph-specific roles. If they don't belong to an IdP group that was assigned a role, they receive the [SSO default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#set-default-graphos-role).

If a user's assigned role changes in IdP while logged into GraphOS Studio, they must log out of Studio and back in to receive their new role and permissions.

#### Sending multiple roles

Each GraphOS team member can only have one organization-wide role. If your IdP sends multiple roles for a single user, GraphOS treats it as [invalid](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#invalid-role). This should only be a concern if you incorrectly configured the [`graphos_org_role` user attribute](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-integration-guide.md#step-1-add-user-attributes). If a user is part of multiple groups, IdPs generally only send the role corresponding to the highest priority group or last claim.

Team members can have as many graph-specific roles as graphs. Their graph-specific role must have higher permissions than their organization-wide role to be applied.

#### Sending invalid roles

Only the `graphos_org_role` values specified in setup Step 1 are valid.
If your IdP sends an invalid `graphos_org_role`:

* Existing users keep their current roles.
* New users receive your organization's default role.
* Either way, the user will still be authenticated and allowed to log in.

#### Accidental removal of org admins

If your role assignment removes all org admins from your GraphOS organization, you can fix it by:

* Updating your assignments so that at least one group maps to the Org Admin role.
* Reaching out to [support@apollographql.com](mailto:support@apollographql.com) to update roles manually.
