# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/okta.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/okta.md

# Okta Identity Provider

Copy page

Connect ConfigCat with Okta via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with Okta as a SAML Identity Provider.

## 1. Create an Application in Okta[​](#1-create-an-application-in-okta "Direct link to 1. Create an Application in Okta")

* Log in to [Okta](https://login.okta.com/), go to the admin Dashboard, and select `Applications`.

  ![Okta applications](/docs/assets/saml/okta/applications.png)

* Click on `Create App Integration`.

  ![Okta create app](/docs/assets/saml/okta/create_app.png)

* Select `SAML 2.0` as the Sign-in method.

  ![Okta select SAML](/docs/assets/saml/okta/select_saml.png)

* Enter a descriptive `App name`, then click `Next`.

  ![Okta app name](/docs/assets/saml/okta/app_name.png)

The next step will guide you on how to collect the information required for the appearing `Configure SAML` section.

## 2. Configure SAML for the Okta Application[​](#2-configure-saml-for-the-okta-application "Direct link to 2. Configure SAML for the Okta Application")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/okta_name.png)

* From the next section of the dialog, copy the following values and paste them into the Okta application.

  * `Entity ID` -> `Audience URI (SP Entity ID)`

  * `Assertion Consumer Service` -> `Single sign on URL`

    ![ConfigCat SAML configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png) ![Okta SAML url EID](/docs/assets/saml/okta/okta_acs_eid.png)

* Set the `Name ID format` to `EmailAddress`, then click `Next`.

  ![Okta SAML nameid](/docs/assets/saml/okta/okta_name_id.png)

* Select `I'm an Okta customer adding an internal app`. Complete the form with any comments and click `Finish`.

  ![Okta SAML feedback](/docs/assets/saml/okta/feedback.png)

## 3. Configure ConfigCat with SAML Details from Okta[​](#3-configure-configcat-with-saml-details-from-okta "Direct link to 3. Configure ConfigCat with SAML Details from Okta")

You can choose one of the following options to configure ConfigCat with SAML Identity Provider metadata.

* Metadata URL
* Manual Configuration

- Select the `Sign On` tab.

  ![Okta sign on tab](/docs/assets/saml/okta/metadata_url1.png)

- Copy the URL of `View IdP metadata`.

  ![Okta metadata url](/docs/assets/saml/okta/metadata_url2.png)

- Paste the copied value into the `Metadata URL` field at ConfigCat.

  ![ConfigCat metadata url](/docs/assets/saml/okta/cc_metadata_new.png)

- Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

- Click on `Save`.

* Select the `Sign On` tab, and click on `View SAML setup instructions`.

  ![Okta SAML setup](/docs/assets/saml/okta/manual_setup.png)

* Copy the value of the `Identity Provider Single Sign-On URL` and `X.509 Certificate` fields and paste them into the Configuration dialog at ConfigCat.

  ![Okta manual configuration](/docs/assets/saml/okta/manual.png)![ConfigCat manual configuration](/docs/assets/saml/okta/manual_cc_new.png)

* Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click on `Save`.

## 4. Assign Users to Okta Application[​](#4-assign-users-to-okta-application "Direct link to 4. Assign Users to Okta Application")

To let users authenticate via SAML, you need to assign individual users or groups to the Okta application.

* Select the `Assignments` tab, and select either the `Assign to People` or the `Assign to Groups` option.

  ![Okta assign to groups](/docs/assets/saml/okta/assign.png)

## 5. Sign In[​](#5-sign-in "Direct link to 5. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address assigned to the Okta application.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to Okta's sign in page. Type your credentials, and click `Sign In`.

  ![Okta sign in](/docs/assets/saml/okta/okta_sign_in.png)

* You should be redirected to ConfigCat signed in with your company account.

## 6. Next Steps[​](#6-next-steps "Direct link to 6. Next Steps")

* Configure [User provisioning (SCIM)](https://configcat.com/docs/advanced/team-management/scim/scim-overview.md)
* or configure the [auto-assignment of users](https://configcat.com/docs/advanced/team-management/auto-assign-users.md) if you don't want to provision your users with your Identity Provider.
