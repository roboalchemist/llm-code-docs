# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/entra-id.md

# User Provisioning (SCIM) with Entra ID (Azure AD)

Copy page

## Introduction[​](#introduction "Direct link to Introduction")

Each Identity Provider requires specific information to configure a SCIM integration. The following guide will walk you through how you can connect ConfigCat with Entra ID via SCIM.

## 1. Create an Entra ID Enterprise Application[​](#1-create-an-entra-id-enterprise-application "Direct link to 1. Create an Entra ID Enterprise Application")

info

If you already configured your organization to use Entra ID as a SAML provider, you can use the existing Entra ID Enterprise application and skip to the [next step](#2-configure-provisioning-scim-for-the-azure-enterprise-application).

* Log in to the [Azure Portal](https://portal.azure.com/), go to the `Entra ID` resource, select `Enterprise applications`, and click on `New application`.

  ![Entra ID enterprise applications](/docs/assets/scim/entra_id/new_application.png)

* Click on `Create your own application`.

  ![Entra ID create own application](/docs/assets/scim/entra_id/create_application.png)

* Enter a descriptive `App name`, select the `Integrate any other application you don't find in the gallery (Non-gallery)` option, then click `Create`.

  ![Entra ID app name](/docs/assets/scim/entra_id/app_name.png)

The next step will guide you on how to setup Entra ID to synchronize your Identity Provider users and Identity Provider groups to ConfigCat.

## 2. Configure Provisioning (SCIM) for the Azure Enterprise Application[​](#2-configure-provisioning-scim-for-the-azure-enterprise-application "Direct link to 2. Configure Provisioning (SCIM) for the Azure Enterprise Application")

* On the `Manage` section of the application, select `Provisioning`, then click on `New Configuration`.

  ![Entra ID new SCIM configuration](/docs/assets/scim/entra_id/new_config.png)

* Gather the `SCIM URL` and the `Token` from the [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page in ConfigCat.

  ![SCIM URL and token](/docs/assets/scim/dashboard/token_generate_url.png) ![SCIM token](/docs/assets/scim/dashboard/token.png)

* Add the `SCIM URL` as the `Tenant URL` and the `Token` as the `Secret token` on the New provisioning configuration page in Azure. Click on the `Create` button.

  ![Entra ID SCIM URL and token](/docs/assets/scim/entra_id/scim_meta.png)

* Select the `Provisioning` menu and in the Mappings, configure the mapping for Users and Groups.

  ![Entra ID SCIM mappings](/docs/assets/scim/entra_id/mappings.png)

  * Mapping for Users: Configure only the following mappings and remove all other mappings if there are any.

    | Provisioning Attribute | Microsoft Entra ID Attribute                                 |
    | ---------------------- | ------------------------------------------------------------ |
    | externalId             | objectId                                                     |
    | userName               | userPrincipalName                                            |
    | displayName            | displayName                                                  |
    | active                 | Switch(\[IsSoftDeleted], , "False", "True", "True", "False") |

    ![Entra ID SCIM User mappings](/docs/assets/scim/entra_id/user_mappings2.png)

  * Mapping for Groups: Configure only the following mappings and remove all other mappings if there are any.

    | Provisioning Attribute | Microsoft Entra ID Attribute |
    | ---------------------- | ---------------------------- |
    | externalId             | objectId                     |
    | displayName            | displayName                  |
    | members                | members                      |

    ![Entra ID SCIM Group mappings](/docs/assets/scim/entra_id/group_mappings.png)

## 3. Assign Users/Groups to the Enterprise Application[​](#3-assign-usersgroups-to-the-enterprise-application "Direct link to 3. Assign Users/Groups to the Enterprise Application")

To start user provisioning with Entra ID, you need to assign groups to the Enterprise application.

* Select `Users and groups` on the `Manage` section of the menu, and click `Add user/group`. Then, you can select the groups you want to assign.

  ![Entra ID users and groups](/docs/assets/scim/entra_id/add_user.png)

caution

In ConfigCat, you can assign permissions only to groups that are synchronized from your Identity Provider, therefore it's important to select groups for synchronization rather than individual users.

## 4. Start provisioning[​](#4-start-provisioning "Direct link to 4. Start provisioning")

* Go to the `Overview` page of the provisioning configuration and click on `Start provisioning`.

  ![Entra ID start provisioning](/docs/assets/scim/entra_id/start_provisioning.png)

* Wait until the first provisioning is finished, and you should see each synced group and user on ConfigCat's [Authentication & Provisioning](https://app.configcat.com/organization/authentication/) page.

## 5. Next Steps[​](#5-next-steps "Direct link to 5. Next Steps")

* Continue with [assigning ConfigCat permissions to the synced groups](https://configcat.com/docs/advanced/team-management/scim/scim-overview.md#groups).
