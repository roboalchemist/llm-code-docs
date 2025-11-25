# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md

# (Beta) User Provisioning (SCIM) with Onelogin

info

**Beta Feature**: SCIM provisioning is in public beta. It has been thoroughly tested with various Identity Providers. We're now collecting feedback from real-world usage to fine-tune the experience. Share your feedback [here](https://configcat.com/support).

## Introduction[​](#introduction "Direct link to Introduction")

Each Identity Provider requires specific information to configure a SCIM integration. The following guide will walk you through how you can connect ConfigCat with OneLogin via SCIM.

## 1. Create an Application in OneLogin[​](#1-create-an-application-in-onelogin "Direct link to 1. Create an Application in OneLogin")

* Log in to [OneLogin](https://app.onelogin.com/login), select `Applications` and click on `Add App`.

  ![OneLogin add application](/docs/assets/scim/onelogin/add_app.png)

* Type `SCIM V2` into the search bar, and select `SCIM Provisioner with SAML (SCIM v2 Core)`.

  ![OneLogin select APP](/docs/assets/scim/onelogin/select_app.png)

* Enter a descriptive `Display Name`, then click `Save`.

  ![OneLogin app name](/docs/assets/scim/onelogin/app_name.png)

## 2. Configure Provisioning (SCIM) for the OneLogin Application[​](#2-configure-provisioning-scim-for-the-onelogin-application "Direct link to 2. Configure Provisioning (SCIM) for the OneLogin Application")

* Gather the `SCIM URL` and the `Token` from the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page in ConfigCat.

  ![SCIM URL and token](/docs/assets/scim/dashboard/token_generate_url.png) ![SCIM token](/docs/assets/scim/dashboard/token.png)

* On the OneLogin application's Configuration tab's API Connection section configure the following:

  * Add the `SCIM URL` from the ConfigCat Dashboard as the `SCIM Base URL`.
  * Add the `Token` from the ConfigCat Dashboard as the `SCIM Bearer Token`.
  * Add the following as the `SCIM JSON Template`:
    <!-- -->
    ```
    {
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "userName": "{$parameters.scimusername}",
      "displayName": "{$user.display_name}"
    }
    ```

  ![OneLogin API Connection configuration](/docs/assets/scim/onelogin/configuration.png)

* On the OneLogin application's Provisioning tab configure the following:

  * Check the `Enable provisioning` checkbox.
  * Configure the other checkboxes and dropdowns based on your preference.

  ![OneLogin enable provisioning](/docs/assets/scim/onelogin/enable_provisioning.png)

* On the OneLogin application's Parameters tab configure the following:

  * Set Email as the `scimusername` parameter.
    <!-- -->
    ![OneLogin SCIM username parameter](/docs/assets/scim/onelogin/scimusername.png)
  * Check the `Include in User Provisioning` checkbox at the Groups parameter.
    <!-- -->
    ![OneLogin Groups parameter](/docs/assets/scim/onelogin/include_in_provisioning.png)

* On the OneLogin application's Rules tab configure which property should OneLogin send as the user's groups to ConfigCat.<br /><!-- -->In the following example we are mapping the user's role in OneLogin as the synced group to ConfigCat, but you can create other mappings as well based on your preference. Read more about mappings [here](https://developers.onelogin.com/scim/create-app#scimruleexamples).

  * Click on te `Add rule` button.
  * Specify a `Name` for your rule.
  * Select `Set Groups in ##YOUR APPLICATION NAME##` at the `Actions`.
  * Select `role` at the `For each` dropdown.
  * Set `.*` for the `with value that matches` input.

  ![OneLogin group mapping rule](/docs/assets/scim/onelogin/rule.png)

## 3. Assign users manually to the application or set access based on policies/roles on the OneLogin application's Access tab.[​](#3-assign-users-manually-to-the-application-or-set-access-based-on-policiesroles-on-the-onelogin-applications-access-tab "Direct link to 3. Assign users manually to the application or set access based on policies/roles on the OneLogin application's Access tab.")

![OneLogin assign groups/roles/users](/docs/assets/scim/onelogin/assign.png)

## 4. Start provisioning[​](#4-start-provisioning "Direct link to 4. Start provisioning")

* On the OneLogin application's Configuration tab click on the `Enable` button to start the provisioning.

  ![OneLogin enable provisioning](/docs/assets/scim/onelogin/enable.png)

* Wait until the first provisioning is finished, and you should see each synced group and user on ConfigCat's [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page.

## 5. Next Steps[​](#5-next-steps "Direct link to 5. Next Steps")

* Continue with [assigning ConfigCat permissions to the synced groups](https://configcat.com/docs/docs/advanced/team-management/scim/scim-overview/.md#groups).
