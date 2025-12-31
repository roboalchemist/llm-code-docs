# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/auth0.md

# Auth0 Identity Provider

Connect ConfigCat with Auth0 via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with Auth0 as a SAML Identity Provider.

## 1. Create an Application in Auth0[​](#1-create-an-application-in-auth0 "Direct link to 1. Create an Application in Auth0")

* Log in to [Auth0](https://auth0.com/auth/login), select `Applications` from the menu, then click `Create Application`.

  ![Auth0 applications](/docs/assets/saml/auth0/applications.png)

* Enter a descriptive `Name`, select `Regular Web Applications`, then click `Create`.

  ![Auth0 app name](/docs/assets/saml/auth0/app_name.png)

* Select the `Addons` tab, and click `SAML2`.

  ![Auth0 enable SAML](/docs/assets/saml/auth0/enable_saml.png)

The next step will guide you on how to collect the information required for the appearing configuration dialog.

## 2. Configure SAML for the Auth0 Application[​](#2-configure-saml-for-the-auth0-application "Direct link to 2. Configure SAML for the Auth0 Application")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/auth0_name.png)

* From the next section of the dialog, copy the following values and paste them into the Auth0 configuration dialog.

  * `Entity ID` -> `"audience": "<entity-id>"` in the configuration JSON below.
  * `Assertion Consumer Service` -> `Application Callback URL`
  * For `Settings`, use the following JSON value:

  ```
  {
    "audience": "<paste-your-entity-id-here>",
    "signatureAlgorithm": "rsa-sha256",
    "nameIdentifierProbes": [
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"
    ]
  }
  ```

  ![ConfigCat ACS configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png) ![Auth0 ACS configuration](/docs/assets/saml/auth0/auth0_acs_eid.png)

  * Click on `Save`.

## 3. Configure ConfigCat with SAML Details from Auth0[​](#3-configure-configcat-with-saml-details-from-auth0 "Direct link to 3. Configure ConfigCat with SAML Details from Auth0")

You can choose one of the following options to configure ConfigCat with SAML Identity Provider metadata.

* Metadata URL
* Manual Configuration

- Copy the URL of `Identity Provide metadata`.

  ![Auth0 metadata URL](/docs/assets/saml/auth0/metadata_url.png)

- Paste the copied value into the `Metadata URL` field at ConfigCat.

  ![ConfigCat metadata URL](/docs/assets/saml/auth0/cc_metadata_url_new.png)

- Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

- Click on `Save`.

* Copy the value of `Identity Provider Login URL` and download the `Identity Provider Certificate`, then paste them into the Configuration dialog at ConfigCat.

  ![Auth0 manual configuration](/docs/assets/saml/auth0/manual.png)![ConfigCat manual configuration](/docs/assets/saml/auth0/cc_manual_new.png)

* Select the **trusted domains**. Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click on `Save`.

## 4. Sign In[​](#4-sign-in "Direct link to 4. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com/auth/login) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address assigned to the Auth0 application.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to Auth0's sign in page. Type your credentials, and click `Continue`.

  ![Auth0 login](/docs/assets/saml/auth0/login.png)

* You should be redirected to ConfigCat signed in with your company account.

## 5. Next Steps[​](#5-next-steps "Direct link to 5. Next Steps")

* Configure the [auto-assignment of users](https://configcat.com/docs/docs/advanced/team-management/auto-assign-users/.md).
