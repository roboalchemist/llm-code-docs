# Source: https://configcat.com/docs/advanced/team-management/scim/identity-providers/onelogin.md

# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/onelogin.md

# OneLogin Identity Provider

Copy page

Connect ConfigCat with OneLogin via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with OneLogin as a SAML Identity Provider.

## 1. Create an Application in OneLogin[​](#1-create-an-application-in-onelogin "Direct link to 1. Create an Application in OneLogin")

* Log in to [OneLogin](https://app.onelogin.com/login), and select `Applications`.

  ![OneLogin applications](/docs/assets/saml/onelogin/applications.png)

* Click on `Add App`.

  ![OneLogin add application](/docs/assets/saml/onelogin/add_app.png)

* Type `SAML` into the search bar, and select `SAML Custom Connector (Advanced)`.

  ![OneLogin select APP](/docs/assets/saml/onelogin/select_app.png)

* Enter a descriptive `Display Name`, then click `Save`.

  ![OneLogin app name](/docs/assets/saml/onelogin/app_name.png)

The next step will guide you on how to collect the information required for the appearing `Configuration` page.

## 2. Configure SAML for the OneLogin Application[​](#2-configure-saml-for-the-onelogin-application "Direct link to 2. Configure SAML for the OneLogin Application")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/onelogin_name.png)

* From the next section of the dialog, copy the following values and paste them into the OneLogin application's configuration page.

  * Copy `Entity ID` and paste it into the `Audience (EntityID)` field.

  * Copy `Assertion Consumer Service` and paste it into the `ACS (Consumer) URL` field.

  * Paste the same `Assertion Consumer Service` into the `ACS (Consumer) URL Validator` field in regex format e.g. `^https:\/\/dashboard\-api\.configcat\.com\/saml\/acs\/08db93fc\-c4e7\-441f\-834f\-17c804385c29$`

    ![ConfigCat SAML configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png) ![OneLogin SML configuration](/docs/assets/saml/onelogin/onelogin_acs_eid.png)

* Scroll down a bit on this page and configure the following:

  * Select `OneLogin` as `SAML Initiator`.

  * Select `Email` as `SAML nameID format`.

  * Select `Both` as `SAML signature element`.

    ![OneLogin SAML initiator](/docs/assets/saml/onelogin/saml_config2.png)

* Select `Parameters`, and make sure there is a `NameID value` entry under the `SAML Custom Connector (Advanced) Field` with the value `Email`.

  ![OneLogin nameID](/docs/assets/saml/onelogin/name_id.png)

* Select `SSO`, then select `SHA-256` as `SAML Signature Algorithm`.

  ![OneLogin SAML Signature Algorithm](/docs/assets/saml/onelogin/sso_signing_algo.png)

## 3. Configure ConfigCat with SAML Details from OneLogin[​](#3-configure-configcat-with-saml-details-from-onelogin "Direct link to 3. Configure ConfigCat with SAML Details from OneLogin")

You can choose one of the following options to configure ConfigCat with SAML Identity Provider metadata.

* Metadata URL
* Manual Configuration

- Select `SSO`, and copy the value of `Issuer URL`.

  ![OneLogin SAML SSO configuration](/docs/assets/saml/onelogin/sso_config.png)

- Paste the copied value into the `Metadata URL` field at ConfigCat.

  ![ConfigCat SAML configuration](/docs/assets/saml/onelogin/cc_meta_url_new.png)

- Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

- Click on `Save`.

* Select `SSO`, and copy the value of `SAML 2.0 Endpoint (HTTP)`, then click `View Details` under the `X.509 Certificate`.

  ![OneLogin manual SAML SSO configuration](/docs/assets/saml/onelogin/sso_config_manual.png)

* Copy the value of the `X.509 Certificate`.

  ![OneLogin certificate](/docs/assets/saml/onelogin/cert.png)

* Paste the value of the `SAML 2.0 Endpoint (HTTP)` and the `X.509 Certificate` into the Configuration dialog at ConfigCat

  ![ConfigCat manual configuration](/docs/assets/saml/onelogin/cc_manual_new.png)

* Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click on `Save`.

## 4. Assign the OneLogin Application to Users[​](#4-assign-the-onelogin-application-to-users "Direct link to 4. Assign the OneLogin Application to Users")

To let users authenticate via SAML, you need to assign the newly created application to them.

* Select `Users`.

  ![OneLogin users](/docs/assets/saml/onelogin/users.png)

* Select the user you want to get access to the application.

  ![OneLogin select user](/docs/assets/saml/onelogin/select_user.png)

* Select `Applications`, then click on the `+` sign.

  ![OneLogin add application](/docs/assets/saml/onelogin/add_application.png)

* Select your application, then click `Continue`.

  ![OneLogin application added](/docs/assets/saml/onelogin/app_added.png)

* Click `Save`.

  ![OneLogin application details](/docs/assets/saml/onelogin/app_details.png)

## 5. Sign In[​](#5-sign-in "Direct link to 5. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address assigned to the OneLogin application.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to OneLogin's sign in page. Type your credentials, and click `Continue`.

  ![OneLogin SAML login](/docs/assets/saml/onelogin/login.png)

* You should be redirected to ConfigCat signed in with your company account.

## 6. Next Steps[​](#6-next-steps "Direct link to 6. Next Steps")

* Configure [User provisioning (SCIM)](https://configcat.com/docs/advanced/team-management/scim/scim-overview.md)
* or configure the [auto-assignment of users](https://configcat.com/docs/advanced/team-management/auto-assign-users.md) if you don't want to provision your users with your Identity Provider.
