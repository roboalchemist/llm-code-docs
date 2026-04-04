# Source: https://www.apollographql.com/docs/graphos/platform/access-management/scim/okta.md

# Set up SCIM with Okta

This feature is in invite-only [preview](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages#preview). Contact [Apollo Support](https://support.apollographql.com/) to request access and the SCIM URL required for setup.

This guide walks through configuring Okta as your GraphOS organization's identity provider (IdP) for [SCIM-based user provisioning](https://www.apollographql.com/docs/graphos/platform/access-management/scim).
Once you've set up your integration, Okta will automatically manage user and group provisioning and deprovisioning in GraphOS.

## Prerequisites

* Only GraphOS [Org admins](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles) can set up SCIM.
* You must have administrative access to your Okta account.
* You must [configure SSO](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview) before configuring SCIM.

## Setup

### Step 1: Obtain SCIM credentials

1. If you haven't already, request a SCIM URL from [Apollo Support](https://support.apollographql.com/).
2. Go to your [API keys](https://studio.apollographql.com/user-settings/api-keys?referrer=docs-content) in GraphOS Studio.
3. Generate a new API key and give it a descriptive name like `Okta SCIM key`.
4. Save the API key securely. You'll need these in the next steps.

   The API key is only displayed once. If you lose it, you'll need to revoke the key and generate a new one.

### Step 2: Configure SCIM in Okta

1. Log in to your Okta Administrator Dashboard.

2. Navigate to **Applications** > **Applications** and select the GraphOS application you created when setting up SSO.

3. In the **General** tab, locate the **App Settings** section and click **Edit**.

4. Next to **Provisioning** select **SCIM**, then click **Save**.

5. Open the **Provisioning** tab, then the **Integration** section from the left menu, and click **Edit** in the **SCIM Connection** section.

6. Enter the following values:
   * **SCIM connector base URL**: the SCIM URL provided by your Apollo contact
   * **Unique identifier field for users**: `userName`
   * **Supported provisioning actions**:
     * Push New Users
     * Push Profile Updates
     * Push Groups

7. Set the **Authentication Mode** to **HTTP Header**.

8. Paste the API token you generated in GraphOS Studio into the **Authorization** field.

9. Click **Test Connector Configuration** to verify the connection. You should see a **Connector configured successfully** modal appear.

10. Click **Save** to complete setup.

### Step 3: Confirm provisioning and attribute mappings

In the **Provisioning** tab of your GraphOS application in Okta:

1. Click **Edit** in the **To App** section.

2. Enable the following features:

   * **Create Users**
   * **Update User Attributes**
   * **Deactivate Users**

3. Click **Save**.

4. On the same page, in the **Attribute Mapping** section, ensure the following required attributes are mapped correctly:

   * `userName`: Configured in Sign On settings
   * `givenName`: `user.firstName`
   * `familyName`: `user.lastName`
   * `email`: `user.email`

   If you need to make any changes, click **Go to Profile Editor**.

This ensures that whenever one of these attributes is updated in your IdP those changes are automatically forwarded to GraphOS.

### Step 4: Assign users to the GraphOS application

You've likely already completed this step when configuring SSO. You can follow these steps to double check your assignments and update them as necessary.

1. Navigate to the **Assignments** tab in your GraphOS application.
2. Click **Assign** and select either **Assign to People** or **Assign to Groups**.
3. Choose the users or groups you want to provision to GraphOS and click **Assign**.
4. Click **Done**.

Users assigned to the application will be automatically provisioned to GraphOS according to your provisioning configuration.

## Assign GraphOS roles

Apollo recommends using *either* SSO or SCIM for role assignment.
If you use both, role assignments will overwrite one another.

### Setup for SCIM-based role assignment

1. In your Okta Administrator Dashboard left navigation, go to **Directory** > **Profile Editor**.

2. Select the GraphOS Studio User for the application created during SSO configuration.

3. Click **+ Add Attribute** and create this attribute

   * **Data type**: `string array`
   * **Display name**: `GraphOS Roles`
   * **Variable name**: `roles`
   * **Description**: `GraphOS Studio roles`
   * **Enum**: Check `Define enumerated list of values` and add the following values for [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles):
     * `Org Admin`: `graphos_org_role:org_admin`
     * `Graph Admin`: `graphos_org_role:graph_admin`
     * `Contributor`: `graphos_org_role:contributor`
     * `Documenter`: `graphos_org_role:documenter`
     * `Observer`: `graphos_org_role:observer`
     * `Consumer`: `graphos_org_role:consumer`
     * `Billing Manager`: `graphos_org_role:billing_manager`
     * Additionally, for any graph-specific roles you want to assign, add roles in this format:

       * `Graph name and role`:`graphos_graph_role:<graph-id>:<graph-role>`

       For example, `Docs sandbox admin`:`graphos_graph_role:docs_sandbox:graph_admin`

       * A graph's ID is the portion of the graph ref before the `@`.
       * Valid values for graph-specific roles are `graph_admin`, `contributor`, `documenter`, `observer`, and `consumer`.
   * **Attribute type**: `Group`
   * **Group priority**: `Combine values across groups`

4. Click **Save Attribute**.

5. Back in the Okta GraphOS Studio application, open the **Assignments** > **Groups** tab.

6. If the desired groups are already assigned to the application, click the pencil icon next to a group to edit it. Otherwise, assign the group by clicking **Assign** > **Assign to Groups**.

7. When editing or assigning a group, select the appropriate **GraphOS Roles** for each group at the bottom of the modal.

8. Click **Save**.

You can apply the same work flow to individuals rather than groups.

Once you've completed the above steps, role assignments will be automatically pushed to GraphOS whenever groups or users are provisioned or updated in Okta.

## Additional resources

* [GraphOS SSO Configuration](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview)
* [Okta SCIM Documentation](https://developer.okta.com/docs/concepts/scim/)
