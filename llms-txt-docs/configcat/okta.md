# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/okta.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/okta.md

# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/okta.md

# (Beta) User Provisioning (SCIM) with Okta

info

**Beta Feature**: SCIM provisioning is in public beta. It has been thoroughly tested with various Identity Providers. We're now collecting feedback from real-world usage to fine-tune the experience. Share your feedback [here](https://configcat.com/support).

## Introduction[​](#introduction "Direct link to Introduction")

Each Identity Provider requires specific information to configure a SCIM integration. The following guide will walk you through how you can connect ConfigCat with Okta via SCIM.

## 1. Create an Application in Okta[​](#1-create-an-application-in-okta "Direct link to 1. Create an Application in Okta")

* Log in to [Okta](https://login.okta.com/), go to the admin Dashboard, select `Applications`, and click on `Create App Integration`.

  ![Okta applications](/docs/assets/scim/okta/create_app.png)

* Select `SAML 2.0` as the Sign-in method.

  ![Okta select SAML](/docs/assets/scim/okta/app_type.png)

* Enter a descriptive `App name`, then click `Next`.

  ![Okta app name](/docs/assets/scim/okta/app_name.png)

The next step will guide you on how to collect the information required for the appearing `Configure SAML` section.

## 2. Configure SAML authentication for the Okta Application[​](#2-configure-saml-authentication-for-the-okta-application "Direct link to 2. Configure SAML authentication for the Okta Application")

* Follow our [SAML configuration guide for Okta](https://configcat.com/docs/docs/advanced/team-management/saml/identity-providers/okta/.md#2-configure-saml-for-the-okta-application).

## 3. Configure Provisioning (SCIM) for the Okta Application[​](#3-configure-provisioning-scim-for-the-okta-application "Direct link to 3. Configure Provisioning (SCIM) for the Okta Application")

* Click on `Edit` at the `App Settings`.

  ![Okta edit app settings](/docs/assets/scim/okta/edit_settings.png)

* Check the `Enable SCIM provisioning` checkbox, and hit `Save`.

  ![Okta enable provisioning](/docs/assets/scim/okta/enable_provisioning.png)

* Gather the `SCIM URL` and the `Token` from the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page in ConfigCat.

  ![SCIM URL and token](/docs/assets/scim/dashboard/token_generate_url.png) ![SCIM token](/docs/assets/scim/dashboard/token.png)

* Select the `Provisioning` tab and click on the `Edit` button.

  ![Okta edit provisioning](/docs/assets/scim/okta/edit_provisioning.png)

* On the `SCIM Connection` section configure the following:

  * Add the `SCIM URL` from the ConfigCat Dashboard as the `SCIM connector base URL`.

  * Set the `Unique identifier field for users` field to `email`.

  * Check the following `Supported provisioning actions`:

    <!-- -->

    * `Push New Users`
    * `Push Profile Updates`
    * `Push Groups`

  * Select the `HTTP Header` as the `Authentication Mode`.

  * Set the `Token` from the ConfigCat Dashboard as the `HTTP Header Authorization`.

  * Click on `Save`.
    <br />
    <br />

  ![Okta SCIM connection](/docs/assets/scim/okta/scim_connection.png)

* Select the `To App` menu item and click on `Edit`.

  ![Okta To App edit](/docs/assets/scim/okta/to_app_edit.png)

* Check the `Create Users`, `Update User Attributes`, and `Deactivate Users` checkboxes, and hit `Save`.

  ![Okta To App save](/docs/assets/scim/okta/to_app_save.png)

## 4. Assign Users/Groups to Okta Application[​](#4-assign-usersgroups-to-okta-application "Direct link to 4. Assign Users/Groups to Okta Application")

To select users for synchronization into ConfigCat, you have to assign their Okta group to the Application.

* Select the `Assignments` tab, click on the `Assign` dropdown, and select `Assign to Groups`.

  ![Okta assign groups](/docs/assets/scim/okta/assign_groups.png)

* Click the `Assign` button on those groups whose members you want to sync to ConfigCat.

  ![Okta assign group](/docs/assets/scim/okta/assign_group.png)

The above action starts the synchronization of the selected users but not their groups.

caution

Okta does not support using the same Okta group for assignments and for syncing group-member relations. You need to create a separate group that is used exclusively for syncing group-member relations. These groups are called `Push Groups` in Okta.

To learn more, see [Okta's documentation about Push Groups](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-about-group-push.htm).

To enable group syncing, create separate groups for the users that you want to sync and add these new groups to the application as `Push Groups`.

* Go to the `Push Groups` tab, click on the `Push Groups` dropdown, and select `Find groups by name`.

  ![Okta push groups](/docs/assets/scim/okta/push_groups.png)

* Select the group that you want to push, and click on the `Save` button.

  ![Okta add push group](/docs/assets/scim/okta/add_push_group.png)

* Make sure that the created push group's status is active.

  ![Okta push group active](/docs/assets/scim/okta/push_group_active.png)

* You should see each synced group and user on ConfigCat's [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page.

## 5. Next Steps[​](#5-next-steps "Direct link to 5. Next Steps")

* Continue with [assigning ConfigCat permissions to the synced groups](https://configcat.com/docs/docs/advanced/team-management/scim/scim-overview/.md#groups).
