# Source: https://www.apollographql.com/docs/graphos/platform/access-management/scim/microsoft-entra-id.md

# Set up SCIM with Microsoft Entra ID

This feature is in invite-only [preview](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages#preview). Contact [Apollo Support](https://support.apollographql.com/) to request access and the SCIM URL required for setup.

This guide walks through configuring Microsoft Entra ID (formerly Azure Active Directory) as your GraphOS organization's identity provider (IdP) for [SCIM-based user provisioning](https://www.apollographql.com/docs/graphos/platform/access-management/scim).
Once you've set up your integration, Microsoft Entra ID will automatically manage user and group provisioning and deprovisioning in GraphOS.

## Prerequisites

* Only GraphOS [Org admins](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles) can set up SCIM.
* You must have administrative access to your Microsoft Entra ID account.
* You must [configure SSO](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview) before configuring SCIM.

## Setup

### Step 1: Obtain SCIM credentials

1. If you haven't already, request a SCIM URL from [Apollo Support](https://support.apollographql.com/).
2. Go to your [API keys](https://studio.apollographql.com/user-settings/api-keys?referrer=docs-content) in GraphOS Studio.
3. Generate a new API key and give it a descriptive name like `Microsoft Entra ID SCIM key`.
4. Save the API key securely. You'll need these in the next steps.

   The API key is only displayed once. If you lose it, you'll need to revoke the key and generate a new one.

### Step 2: Configure SCIM in Entra ID

1. Log in to the [Microsoft Azure portal](https://portal.azure.com/).
2. Navigate to **Microsoft Entra ID** (formerly Azure Active Directory).
3. Select **Enterprise applications** from the left sidebar.
4. Find and select the GraphOS application you created when setting up SSO.
5. In the left sidebar, select **Provisioning**.
6. Click **+ New Configuration**.
7. Under **Admin Credentials**, enter the following information:
   * **Tenant URL**: Enter the SCIM URL provided by your Apollo contact.
   * **Secret Token**: Enter the API key you generated in Step 1.
8. Click **Test Connection** to verify the connection.
9. If the connection test is successful, click **Create**.

### Step 3: Configure provisioning

1. Still in the **Provision** section, open the **Mappings** tab. Click **Provision Microsoft Entra ID Users**.
2. Verify the following settings are enabled:
   * **Create users**
   * **Update users**
   * **Delete users**
3. Review the attribute mappings.
4. Ensure the following required attributes are mapped correctly:
   * `userName`: `userPrincipalName` (this should be the default)
   * `emails[type eq "work"].value`: `mail`
   * `name.givenName`: `givenName`
   * `name.familyName`: `surname`
5. Click **Save** to apply your mapping settings.

### Step 4: Start provisioning

1. Back on the main **Provisioning** page, set the **Provisioning Status** to **On**.

2. Click **Save** to start the provisioning process.

3. Microsoft Entra ID will now begin synchronizing users to GraphOS based on your configured settings.

Initial synchronization can take anywhere from a few minutes to several hours depending on the number of users and groups in your directory.
Once initial synchronization is complete, Entra ID re-syncs regularly.

### Step 5: Assign users to the GraphOS application

You've likely already completed this step when configuring SSO. You can follow these steps to double check your assignments and update them as necessary.

1. In the left sidebar of your enterprise application, select **Users and groups**.
2. Click **+ Add user/group**.
3. Select the users or groups you want to provision to GraphOS.
4. Click **Assign**.

Users assigned to the application will be automatically provisioned to GraphOS according to your provisioning configuration.

## Monitoring and troubleshooting

In the **Provisioning** page, check the **Provisioning logs** section to see details about the provisioning process, including any errors or warnings.

## Additional Resources

* [GraphOS SSO Configuration](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview)
* [Microsoft Entra ID SCIM Documentation](https://learn.microsoft.com/en-us/entra/architecture/sync-scim)
