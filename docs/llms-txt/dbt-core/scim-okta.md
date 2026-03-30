# Source: https://docs.getdbt.com/docs/cloud/manage-access/scim-okta.md

# Set up SCIM with Okta [Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise +](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")

SCIM available for Okta

System for Cross-Domain Identity Management (SCIM) [license mapping](https://docs.getdbt.com/docs/cloud/manage-access/scim-manage-user-licenses.md) is currently only supported for Okta. For other providers, license types must be [managed](https://docs.getdbt.com/docs/cloud/manage-access/seats-and-users.md#mapped-configuration) within the dbt platform user interface.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Available on [Enterprise or Enterprise+ plans](https://www.getdbt.com/pricing).
* You must use Okta as your single sign-on (SSO) provider and have it connected in the dbt platform.
* You must have [permissions](https://docs.getdbt.com/docs/cloud/manage-access/enterprise-permissions.md) to configure the account settings in dbt platform.
* Complete [setup SSO with Okta](https://docs.getdbt.com/docs/cloud/manage-access/set-up-sso-okta.md) before configuring SCIM settings.
* Complete the [Set up SCIM](https://docs.getdbt.com/docs/cloud/manage-access/scim.md#set-up-dbt) to get your SCIM base URL and token.

## Set up Okta[​](#set-up-okta "Direct link to Set up Okta")

1. Log in to your Okta account and locate the app configured for the dbt SSO integration.

2. Navigate to the **General** tab and ensure **Enable SCIM provisioning** is selected or the **Provisioning** tab will not be displayed.

   [![Enable SCIM provisioning in Okta.](/img/docs/dbt-cloud/access-control/scim-provisioned.png?v=2 "Enable SCIM provisioning in Okta.")](#)Enable SCIM provisioning in Okta.

3. Open the **Provisioning** tab and select **Integration**.

4. Enter the **SCIM base URL** from [Set up SCIM](https://docs.getdbt.com/docs/cloud/manage-access/scim.md#set-up-dbt) in the first field, then enter your preferred **Unique identifier field for users** — we recommend `userName`.

5. Select the boxes for the following **Supported provisioning actions**:

   * **Push New Users**
   * **Push Profile Updates**
   * **Push Groups**
   * **Import New Users and Profile Updates** (Optional for users created before SSO/SCIM setup)

6. From the **Authentication mode** dropdown, select **HTTP Header**.

7. In the **Authorization** section, enter the token from dbt into the **Bearer** field.

   [![The completed SCIM configuration in the Okta app.](/img/docs/dbt-cloud/access-control/scim-okta-config.png?v=2 "The completed SCIM configuration in the Okta app.")](#)The completed SCIM configuration in the Okta app.

8. Ensure the following provisioning actions are selected:

   * **Create Users**
   * **Update User Attributes**
   * **Deactivate Users**

   [![Ensure the users are properly provisioned with these settings.](/img/docs/dbt-cloud/access-control/provisioning-actions.png?v=2 "Ensure the users are properly provisioned with these settings.")](#)Ensure the users are properly provisioned with these settings.

9. Test the connection and click **Save** once completed.

You've now configured SCIM for the Okta SSO integration in dbt platform. You can [manage user licenses with SCIM](https://docs.getdbt.com/docs/cloud/manage-access/scim-manage-user-licenses.md) to set license type for users as they are provisioned.

## SCIM username format[​](#scim-username-format "Direct link to SCIM username format")

For dbt platform SCIM with Okta, `userName` **must be the email address format**. dbt platform uses `userName` to look up existing users during SCIM sync. If Okta sends another format (such as an Okta internal ID like `00u...` or an employee ID), dbt platform cannot match the existing user, and provisioning will fail.

If your Okta configurations map the `Username` field to a different attribute, set your Okta app config to `Email`:

1. Open the SAML app created for the dbt integration.
2. In the **Sign on** tab, click **Edit** in the **Settings** pane.
3. Set the **Application username format** field to **Email**.
4. Click **Save**.

## SCIM license mapping[​](#scim-license-mapping "Direct link to SCIM license mapping")

To automate seat assignments in Okta for users as they are provisioned, see [Manage user licenses with SCIM](https://docs.getdbt.com/docs/cloud/manage-access/scim-manage-user-licenses.md).

## Existing Okta integrations[​](#existing-okta-integrations "Direct link to Existing Okta integrations")

If you are adding SCIM to an existing Okta integration in dbt (as opposed to setting up SCIM and SSO concurrently for the first time), be aware of the following behavior:

* Users and groups already synced to dbt will become SCIM-managed once you complete the SCIM configuration.

* (Recommended) Import and manage existing dbt groups and users with Okta's **Import Groups** and **Import Users** features. Update the groups in your IdP with the same naming convention used for dbt groups. New users, groups, and changes to existing profiles will be automatically imported into dbt.

  <!-- -->

  * Ensure the **Import users and profile updates** and **Import Groups** boxes are selected under the **Provisioning settings** tab in the Okta SCIM configuration.
  * Use **Import Users** to sync all users from dbt, including previously deleted users, if you need to re-provision those users.
  * Read more about this feature in the [Okta documentation](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-import-groups-app-provisioning.htm).

To set license type for users as they are provisioned, see [Manage user licenses with SCIM](https://docs.getdbt.com/docs/cloud/manage-access/scim-manage-user-licenses.md).

## Was this page helpful?

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
