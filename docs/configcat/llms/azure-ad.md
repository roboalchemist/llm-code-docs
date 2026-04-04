# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/azure-ad.md

# Entra ID (Azure AD) Identity Provider

Copy page

Connect ConfigCat with Entra ID via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with Entra ID as a SAML Identity Provider.

## 1. Create an Entra ID Enterprise Application[​](#1-create-an-entra-id-enterprise-application "Direct link to 1. Create an Entra ID Enterprise Application")

* Log in to the [Azure Portal](https://portal.azure.com/), go to the `Entra ID` resource, and select `Enterprise applications`.

  ![Entra ID enterprise applications](/docs/assets/saml/azure-ad/eapplications.png)

* Click on `New application`.

  ![Entra ID new application](/docs/assets/saml/azure-ad/new_app.png)

* Click on `Create your own application`.

  ![Entra ID create own application](/docs/assets/saml/azure-ad/create_app.png)

* Enter a descriptive `App name`, select the `Integrate any other application you don't find in the gallery (Non-gallery)` option, then click `Create`.

  ![Entra ID app name](/docs/assets/saml/azure-ad/app_name.png)

* On the `Manage` section of the application, select `Single sign-on`, then select `SAML`.

  ![Entra ID enable SAML](/docs/assets/saml/azure-ad/enable_saml.png)

The next step will guide you on how to collect the information required for Configuring SAML in the application.

## 2. Configure SAML for the Azure Enterprise Application[​](#2-configure-saml-for-the-azure-enterprise-application "Direct link to 2. Configure SAML for the Azure Enterprise Application")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/aad_name.png)

* From the next section of the dialog, copy the following values and paste them into the Enterprise application.

  * `Entity ID` -> `Identifier (Entity ID)`

  * `Assertion Consumer Service` -> `Reply URL (Assertion Consumer Service URL)`

    ![ConfigCat SAML configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png) ![Entra ID URL configuration](/docs/assets/saml/azure-ad/saml_urls.png) ![Entra ID URLs](/docs/assets/saml/azure-ad/aad_acs_eid.png)

## 3. Configure ConfigCat with SAML Details from Azure[​](#3-configure-configcat-with-saml-details-from-azure "Direct link to 3. Configure ConfigCat with SAML Details from Azure")

You can choose one of the following options to configure ConfigCat with SAML Identity Provider metadata.

* Metadata URL
* Manual Configuration

- Copy the value of `App Federation Metadata Url`.

  ![Entra ID metadata URL](/docs/assets/saml/azure-ad/metadata_url.png)

- Paste the copied value into the `Metadata URL` field at ConfigCat.

  ![ConfigCat Entra ID metadata URL](/docs/assets/saml/azure-ad/cc_metadata_new.png)

- Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

- Click on `Save`.

* Copy the value of `Login URL` and download the `Certificate (Base64)`, then paste them into the Configuration dialog at ConfigCat.

  ![Entra ID metadata login URL](/docs/assets/saml/azure-ad/metadata_logon.png)![Entra ID metadata certificate](/docs/assets/saml/azure-ad/metadata_cert.png)![ConfigCat Entra ID manual configuration](/docs/assets/saml/azure-ad/cc_manual_new.png)

* Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click on `Save`.

## 4. Assign Users to the Enterprise Application[​](#4-assign-users-to-the-enterprise-application "Direct link to 4. Assign Users to the Enterprise Application")

To let users authenticate via SAML, you need to assign individual users or groups to the Enterprise application.

* Select `Users and groups` on the `Manage` section of the menu.

  ![Entra ID users and groups](/docs/assets/saml/azure-ad/users_groups.png)

* Click `Add user/group`, then select the users or groups you want to assign.

  ![Entra ID add user/group](/docs/assets/saml/azure-ad/add_users.png)

## 5. Sign In[​](#5-sign-in "Direct link to 5. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address assigned to the Enterprise application.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to Microsoft's sign in page. Type your credentials for sign-in.

  ![Entra ID sign in page](/docs/assets/saml/azure-ad/login.png)

* You should be redirected to ConfigCat signed in with your company account.

## 6. Next Steps[​](#6-next-steps "Direct link to 6. Next Steps")

* Configure [User provisioning (SCIM)](https://configcat.com/docs/advanced/team-management/scim/scim-overview.md)
* or configure the [auto-assignment of users](https://configcat.com/docs/advanced/team-management/auto-assign-users.md) if you don't want to provision your users with your Identity Provider.
