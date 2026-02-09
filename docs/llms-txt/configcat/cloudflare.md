# Source: https://configcat.com/docs/advanced/team-management/saml/identity-providers/cloudflare.md

# Cloudflare Zero Trust

Copy page

Connect ConfigCat with Cloudflare Zero Trust via SAML.

## Introduction[​](#introduction "Direct link to Introduction")

Each SSO Identity Provider requires specific information to configure a SAML integration. The following guide will walk you through how you can connect ConfigCat with Cloudflare Zero Trust as a SAML Identity Provider.

## 1. Create an Application in Cloudflare[​](#1-create-an-application-in-cloudflare "Direct link to 1. Create an Application in Cloudflare")

* Log in to [CloudFlare](https://dash.cloudflare.com/), go to the Zero Trust Dashboard, and select `Applications` under the `Access` menu.<br /><!-- -->Then click on `Add an application`.

  ![Create Cloudflare application](/docs/assets/saml/cloudflare/add_app.png)

* Select `SaaS`.

  ![Select SaaS](/docs/assets/saml/cloudflare/add_saas.png)

* Enter a descriptive name in the `Application` field.

  ![Cloudflare app name](/docs/assets/saml/cloudflare/app_name.png)

The next step will guide you on how to collect the information required for the appearing configuration section.

## 2. Configure SAML for the Cloudflare Application[​](#2-configure-saml-for-the-cloudflare-application "Direct link to 2. Configure SAML for the Cloudflare Application")

* Open your organization's authentication settings on the [ConfigCat Dashboard](https://app.configcat.com/organization/authentication).

  ![ConfigCat authentication settings](/docs/assets/saml/dashboard/authentication.png)

* Click `ADD SAML IDENTITY PROVIDER`.

  ![ConfigCat Add Identity Provider](/docs/assets/saml/dashboard/add_idp.png)

* Give a name for your Identity Provider, and click `Create`.

  ![ConfigCat Name Identity Provider](/docs/assets/saml/dashboard/cf_name.png)

* From the next section of the dialog, copy the following values and paste them into the Cloudflare application.

  * `Entity ID` -> `Entity ID`

  * `Assertion Consumer Service` -> `Assertion Consumer Service URL`

    ![ConfigCat SAML configuration](/docs/assets/saml/dashboard/acs_entity_id_1.png) ![Cloudflare SAML url EID](/docs/assets/saml/cloudflare/meta.png)

* Set the `Name ID Format` to `Email`.

  ![Cloudflare SAML name id](/docs/assets/saml/cloudflare/name_id.png)

* Click `Next` at the bottom of the page.

## 3. Configure policies for the Cloudflare Application[​](#3-configure-policies-for-the-cloudflare-application "Direct link to 3. Configure policies for the Cloudflare Application")

To let users authenticate via SAML, you need to assign groups to the Cloudflare application.

* Give a name for the Cloudflare Application's policy and check those groups that you want to assign.

  ![Cloudflare SAML name id](/docs/assets/saml/cloudflare/policy.png)

* Click `Next` at the bottom of the page.

## 4. Configure ConfigCat with SAML Details from Cloudflare[​](#4-configure-configcat-with-saml-details-from-cloudflare "Direct link to 4. Configure ConfigCat with SAML Details from Cloudflare")

* Copy the value of `SSO endpoint` and `Public key` fields.

  ![Cloudflare SSO url cert](/docs/assets/saml/cloudflare/cert_sign_on_url.png)

* On the ConfigCat Dashboard, select the `3. Set up ConfigCat` step, click `Manual Configuration`, then paste the copied values into the appearing fields.

  * `SSO endpoint` -> `Sign-on URL`

  * `Public key` -> `X.509 Certificate`

    ![ConfigCat manual configuration](/docs/assets/saml/dashboard/cf_manual.png)

## 5. Select Trusted Domains on the SAML Configuration Dialog[​](#5-select-trusted-domains-on-the-saml-configuration-dialog "Direct link to 5. Select Trusted Domains on the SAML Configuration Dialog")

* Only user accounts from trusted domains can login with SAML SSO. You can bind multiple verified domains to a SAML Identity Provider.

  ![Select trusted domains](/docs/assets/saml/dashboard/select_trusted_domains.png)

* Click `Save`.

## 5. Sign In[​](#5-sign-in "Direct link to 5. Sign In")

* Go to the [ConfigCat Log In](https://app.configcat.com) page, and click `COMPANY ACCOUNT - SAML`.

  ![ConfigCat SAML login](/docs/assets/saml/dashboard/saml_login.png)

* Sign in with your company email address assigned to the Cloudflare application.

  ![ConfigCat SAML company login](/docs/assets/saml/dashboard/company_email.png)

* ConfigCat will redirect you to Cloudflare's sign in page.

  ![Cloudflare sign in](/docs/assets/saml/cloudflare/login_page.png)

## 6. Next Steps[​](#6-next-steps "Direct link to 6. Next Steps")

* Configure the [auto-assignment of users](https://configcat.com/docs/advanced/team-management/auto-assign-users.md).
