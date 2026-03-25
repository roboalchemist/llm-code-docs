# Source: https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md

# Set up SAML SSO with Microsoft Entra ID (formerly Azure AD)

This guide walks through configuring Microsoft Entra ID (formerly known as Azure Active Directory) as your GraphOS organization's identity provider (IdP) for SAML-based SSO.
Once you've set up your integration, you need to assign users to it in Entra ID so they can access GraphOS Studio via SSO.

Before assigning users, Apollo recommends setting a [default GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#set-default-graphos-role) for users logging in via SSO.
You can also configure Entra ID to [assign GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#assign-graphos-roles-in-entra-id) to your users based on their Entra ID groups.

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

### Step 2. Create an Entra ID enterprise application

1. Once you reach **Step 2: Configure Your IdP** in the wizard, go to your [Microsoft Entra admin center](https://entra.microsoft.com/). Alternatively, you can sign in to the [Azure Portal](http://portal.azure.com/) and then go to **Microsoft Entra ID**.

2. Go to **Identity > Applications > Enterprise applications** and select **+New application** in the top menu.

3. In the top menu, select **+Create your own application**.

4. Enter `Apollo GraphOS` as the name of your app. Below, keep the **Integrate any other application you don't find in the gallery (Non-gallery)** option selected. Click **Create**.

5. On the app's **Overview** page, select **2. Set up single sign-on**. You'll assign users and groups later.

6. On the app's **Single sign-on** page, select **SAML** as the single sign-on method.

7. At the top of the **SAML-based Sign-on** page, click **Upload metadata file** and upload the file provided by the GraphOS setup wizard. Alternatively, you can enter these values manually in the **Basic SAML Configuration** section:

   * **Identifier (Entity ID)**: Entity ID value provided by the setup wizard
   * **Reply URL (Assertion Consumer Service URL)**: Single Sign-on URL provided by the setup wizard

   Click **Save**.

8. In **Attributes & Claims**, ensure the following claim **names** have the corresponding **source attributes**:

   * `email`: `user.mail`
   * `given_name`: `user.givenname`
   * `family_name`: `user.surname`
   * `sub`: `user.userprinicipalname`
   * `Unique User Identifier`: `user.userprinicipalname`

   Otherwise, manually enter them.

   Leave **Namespace** blank for each claim.

9. Under **SAML Certificates**, copy the **App Federation Metadata URL** into a text file for the next step.

10. In the setup wizard in GraphOS Studio, select whether your Entra implementation requires signing an AuthnRequest.

11. Click **Continue**.

### Step 3. Share SAML metadata with Apollo

In the setup wizard, enter the **App Federation Metadata URL** you previously copied into the **Upload metadata from URL** field.
Click **Next**.

### Step 4. Verify details

The GraphOS Studio setup wizard populates your SSO metadata based on the URL you entered in the last step. Verify the values are correct.

You can find them in Entra ID, **Identity > Applications > Enterprise applications**, in the application you created for GraphOS.

* Your application's **Entity ID** is in the **Single sign-on** tab. Scroll down to the **Basic SAML Configuration** section and look for a field labeled **Identifier (Entity ID)**. This field contains the Entity ID. It has the following format: `urn:<unique>.<region>.auth0.com`.
* The **SSO URL** is also in thee **Basic SAML Configuration** section in the **Sign on URL** field.

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

You can set a [default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#set-default-graphos-role) for any users signing in with SSO. Apollo recommends setting the default role before [assigning users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#assign-users-in-entra-id).

## Set default GraphOS role

Once you've enabled SSO, you can optionally set the default [GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) for new users logging in via SSO.
If you don't set a default, the default role is **Consumer**.
To update the default role for new SSO users, go to **Settings** > **Security** > **Single sign-on** and click **Update new user role**.

## Assign users in Entra ID

Once you've set up your Apollo GraphOS application in Entra ID, you need to assign users to it so they can access GraphOS.
You can assign individual users or groups from the **User and groups** page of your Apollo GraphOS application in Entra ID.

You may want to begin by adding yourself individually and then testing SSO by clicking **Test** at the bottom of the **Single sign-on** page.

Once you've successfully tested your own user's ability to use SSO, add any applicable users or groups.
Once you've confirmed the new configuration works for your users, remove any legacy Apollo GraphOS applications in Entra ID or app registrations in Azure AD if you have them.

## Assign GraphOS roles in Entra ID

Apollo recommends using *either* SSO or SCIM for role assignment.
If you use both, role assignments will overwrite one another.

### Setup

Follow steps 1 and 2 to set organization-wide roles and step 3 for graph-specific roles.

#### Step 1: Add `graphos_org_role` claim

1. In your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Identity** > **Applications** > **Enterprise applications** and select the GraphOS application you previously created.

2. Go to the **Single sign-on** section and click **Edit** next to **Attributes & Claims**.

3. Click **+Add new claim** and give your new claim the name `graphos_org_role`. Leave the **Namespace** blank.

4. Expand the **Claim conditions** section. This is where you'll map groups to GraphOS roles.

   One claim condition row represents one GraphOS role and all the groups you want to assign to it. For each GraphOS role you want to map groups to, select the following:

   * **User type**: `Members`
   * **Scoped Groups**: Select all Entra ID groups that should have the same GraphOS role.
   * **Source**: `Attribute`
   * **Value**: Enter the GraphOS role name in all caps without quotes. [EntraID inserts quotes for constant values](https://learn.microsoft.com/en-us/entra/identity-platform/jwt-claims-customization#view-or-edit-claims).

     The following `string` values are valid GraphOS [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles):
     * `ORG_ADMIN`
     * `GRAPH_ADMIN`
     * `CONTRIBUTOR`
     * `DOCUMENTER`
     * `OBSERVER`
     * `CONSUMER`
     * `BILLING_MANAGER`

   The order of the rows matters. Since Entra ID assigns values [based on the last condition met](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization?WT.mc_id=Portal-Microsoft_AAD_IAM), you should assign groups to GraphOS roles in increasing order of permissions. This ensures that users who belongs to multiple groups get the highest level of permissions.

   * In the example above, imagine the general **Engineering** group is the **Scoped Group** for the `CONTRIBUTOR` role in the first claim condition.
   * Next, suppose a **Feature Team 1** group has the `GRAPH_ADMIN` role.
   * Finally, an **Apollo Admins** group has the most privileges as `ORG_ADMIN`s.
   * This order ensures a member of the Apollo Admin group has `ORG_ADMIN` privileges, even if they also belong to Feature Team 1 and the Engineering groups. If a user only belongs to the Engineering group, they receive the `CONTRIBUTOR` role.

5. Save your changes.

#### Step 2: Include claim in manifest

1. Still in your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Applications** > **App registrations** > **All applications** and select the GraphOS application you added claims to.

2. In the App registration left nav, open **Manage > Manifest**. Set both `isFallbackPublicClient` and `api.acceptMappedClaims` to `true`

3. Click **Save**.

#### (Optional) Step 3: Set graph-specific roles

1. In your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Identity** > **Applications** > **App registrations** and select the GraphOS application you previously created.

2. Go to the **App roles** section and click **+ Create app role**. Enter the following information:

   * **Display name**: Enter a descriptive name for your role.

   * **Allowed member types**: Leave as `Users/Groups`

   * **Value**: Use the `<graph-id>:<graph-role>` format for each graph-specific role.
     * A graph's ID is the portion of the graph ref before the `@`.
     * Valid values for graph-specific roles are `GRAPH_ADMIN`, `CONTRIBUTOR`, `DOCUMENTER`, `OBSERVER`, and `CONSUMER`.
     * Ensure the delimiter between the graph ID and role is a colon (`:`).

   * **Description**: Enter a detailed description of this app role and its rationale.

   * **Do you want to enable this app role?**: Leave as checked.

   - Click **Apply**.

3. Repeat these steps for any additional graph-specific roles you want to provision to Entra users or groups. Groups and individuals can have as many graph-specific roles as necessary.

4. Go to **Identity** > **Applications** > **Enterprise Applications** and select the GraphOS application you previously created.

5. From the inner left sidebar, open **Users and groups** and check all the users and/or groups you want to assign your newly created app role to. Once checked, click **Edit assignment**.

6. Under **Select Role**, click the selected roles or the text **None Selected** and add the relevant app roles. Click **Select**.

7. Click **Assign** to finish the assignment process.

8. Still in **Identity** > **Applications** > **Enterprise Applications** > your GraphOS application, open **Single sign-on** from the inner left sidebar. Click **Edit** next to **Attributes & Claims**.

9. Click **+Add new claim** and give your new claim the name `graphos_graph_roles`. Leave the **Namespace** blank.

10. Leave **Attribute** as the **Source** and select `user.assignedroles` as the **Source attribute**.

11. Click **Save**. The **Additional claims** section should now included a `graphos_graph_roles` claim.

### Role assignment behavior

Once you've completed the previous steps, whenever a user signs into GraphOS, they receive the role based on their IdP groups and/or individual graph-specific roles. If they don't belong to an IdP group that was assigned a role, they receive the [SSO default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#set-default-graphos-role).

If a user's assigned role changes in IdP while logged into GraphOS Studio, they must log out of Studio and back in to receive their new role and permissions.

#### Sending multiple roles

Each GraphOS team member can only have one organization-wide role. If your IdP sends multiple roles for a single user, GraphOS treats it as [invalid](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#invalid-role). This should only be a concern if you incorrectly configured the [`graphos_org_role` user attribute](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-microsoft-entra-id.md#step-1-add-user-attributes). If a user is part of multiple groups, IdPs generally only send the role corresponding to the highest priority group or last claim.

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
