# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/google.md

# Google Identity Provider

Copy page

Connect ConfigCat with Google via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with Google as a SAML Identity Provider.

## 1. Create a SAML Application in Google[​](#1-create-a-saml-application-in-google "Direct link to 1. Create a SAML Application in Google")

* Log in to [Google Admin console](https://admin.google.com/), select `Apps` from the side menu, then select `Web and mobile apps`.

  ![Google applications](/docs/assets/saml/google/applications.png)

* Click `Add App`, then select `Add custom SAML app`.

  ![Google add SAML app](/docs/assets/saml/google/add_saml_app.png)

* Enter a descriptive `App name`, then click `CONTINUE`.

  ![Google SAML app name](/docs/assets/saml/google/app_name.png)

The next step will guide you on how to configure ConfigCat with appearing information.

## 2. Configure ConfigCat with SAML Details from Google[​](#2-configure-configcat-with-saml-details-from-google "Direct link to 2. Configure ConfigCat with SAML Details from Google")

* Copy the value of `SSO URL` and `Certificate` fields and save them for further use.

  ![Google SSO url](/docs/assets/saml/google/meta_url_cert.png)

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/google_name.png)

* Select the `3. Set up ConfigCat` step, click `Manual Configuration`, then paste the copied values into the appearing fields.

  ![ConfigCat manual configuration](/docs/assets/saml/google/cc_manual_new.png)

* Click `CONTINUE` on the Google App configuration.

  ![Google SSO app configuration](/docs/assets/saml/google/meta_continue.png)

The next step will guide you on how to configure the Google App with details provided by ConfigCat.

## 3. Configure the Google Application with Service Provider Details from ConfigCat[​](#3-configure-the-google-application-with-service-provider-details-from-configcat "Direct link to 3. Configure the Google Application with Service Provider Details from ConfigCat")

* Select `2. Set up your Identity Provider` step on the ConfigCat configuration dialog, and copy the following values to the Google App.

  * `Entity ID` -> `Entity ID`

  * `Assertion Consumer Service` -> `ACS URL`

    ![Google acs url](/docs/assets/saml/dashboard/acs_entity_id_2.png)

  * Make sure the `Signed response` option is checked.

  * Select `EMAIL` as `Name ID format`.

  * Select `Basic Information > Primary email` as `Name ID`.

  * Click `CONTINUE`.

    ![Google meta data](/docs/assets/saml/google/google_acs_eid.png)

* Click `FINISH`.

  ![Google attribute mapping](/docs/assets/saml/google/attribute_mapping.png)

## 4. Select Trusted Domains on the SAML Configuration Dialog[​](#4-select-trusted-domains-on-the-saml-configuration-dialog "Direct link to 4. Select Trusted Domains on the SAML Configuration Dialog")

* Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click `Save`.

## 5. Give Users Access to the Application[​](#5-give-users-access-to-the-application "Direct link to 5. Give Users Access to the Application")

* Click on `View details` under the `User access` section.

  ![Google user access](/docs/assets/saml/google/user_access.png)

* Select `ON for everyone`, then click `SAVE`.

  ![Google ON for everyone](/docs/assets/saml/google/on_for_everyone.png)

## 6. Sign In[​](#6-sign-in "Direct link to 6. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address used in Google.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to Google's sign in page. Type your credentials, and sign in.

  ![Google SSO login](/docs/assets/saml/google/login.png)

* You should be redirected to ConfigCat signed in with your company account.

## 7. Next Steps[​](#7-next-steps "Direct link to 7. Next Steps")

* Configure the [auto-assignment of users](https://configcat.com/docs/advanced/team-management/auto-assign-users.md).
