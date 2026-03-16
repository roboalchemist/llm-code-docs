# Source: https://docs.rootly.com/integrations/sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SSO

> Enable single sign-on with SAML 2.0 compatible identity providers including Okta, Google, OneLogin, Auth0, Azure, and more.

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:﻿

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-1.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=2dca78f400e0963cb6a316cfeb60a19b" alt="Document Image" width="879" height="633" data-path="images/integrations/sso/images-1.webp" />
</Frame>

## Identity Providers

Rootly is compatible with **any identity provider** supporting **SAML 2.0.**

Depending on the identity provider, you might be asked for the following information during your setup process:

**ACS URL**: `https://rootly.com/users/saml/auth`

**Entity ID**: `https://rootly.com/users/saml/metadata`

### Okta

Let's go to the **Applications** panel.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-2.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=bdd13b68f2381904cbc5b1f5bdf34c6a" alt="Document Image" width="863" height="319" data-path="images/integrations/sso/images-2.webp" />
</Frame>

Search for **Rootly**.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-3.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=0ec134aaafe249dce6b3aa4d4708ca60" alt="Document Image" width="865" height="273" data-path="images/integrations/sso/images-3.webp" />
</Frame>

Click on **Add**.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-4.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=577475bfb749b1b4d63493d330e84321" alt="Document Image" width="878" height="795" data-path="images/integrations/sso/images-4.webp" />
</Frame>

Select **SAML 2.0**.

Now our app is created let's go back in **Applications > Rootly** and click **View Setup Instructions:**

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-5.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=4b978b190f3fc0b91856321d8f220a31" alt="Document Image" width="877" height="812" data-path="images/integrations/sso/images-5.webp" />
</Frame>

Finally copy the fields as shown below into **Rootly**, this information from Okta is unique to your organization.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-6.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=eedeb7d846c8a360c6aa659841752be0" alt="Document Image" width="871" height="466" data-path="images/integrations/sso/images-6.webp" />
</Frame>

You are all set!

### Google

You will need to access the **Google Admin Console:** [https://admin.google.com/ac/home](https://admin.google.com/ac/home).

Follow screenshot steps as below:

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-7.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=7d489688100ed9614391091e7cd43f06" alt="Document Image" width="878" height="472" data-path="images/integrations/sso/images-7.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-8.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=c6f670a48ba8657f035acff4805872b0" alt="Document Image" width="876" height="421" data-path="images/integrations/sso/images-8.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-9.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=caed170cb14bfe882b5f97c643a5033e" alt="Document Image" width="875" height="442" data-path="images/integrations/sso/images-9.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-10.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=2332f709f40bb4ad0fbe02994ca400b0" alt="Document Image" width="893" height="757" data-path="images/integrations/sso/images-10.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-11.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=60879b7f9fe6491c5e454bed58035b76" alt="Document Image" width="873" height="863" data-path="images/integrations/sso/images-11.webp" />
</Frame>

Make sure `Signed Response` is checked and the app `ON for everyone` is checked in your org unit.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-12.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=802c16dc4c311dfd7b801ff2dd882284" alt="Document Image" width="876" height="469" data-path="images/integrations/sso/images-12.webp" />
</Frame>

And finally let's edit the attributes mapping.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-13.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=3f8f1b232f88fa4226f917b289efb6bb" alt="Document Image" width="871" height="532" data-path="images/integrations/sso/images-13.webp" />
</Frame>

Let's switch to Rootly. You can get the identity login url by clicking on the `TEST SAML LOGIN` button.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-14.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=abc659439d4b43b384ded6d4304e7d14" alt="Document Image" width="881" height="792" data-path="images/integrations/sso/images-14.webp" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-15.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=d3bf24231e1b5d062782604271f42cc2" alt="Document Image" width="1059" height="774" data-path="images/integrations/sso/images-15.webp" />
</Frame>

### OneLogin

Browse the Applications Store page and install Rootly.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-16.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=2093a855009be8384f01e0196b78d8f3" alt="Document Image" width="876" height="470" data-path="images/integrations/sso/images-16.webp" />
</Frame>

Copy fields over Rootly like shown below

* Issuer URL **->** Identity Provider ID
* SAML 2.0 endpoint **->** Identity Login Url
* In the certificate section > View Details > X.509 Certificate **->** Idp Cert

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-17.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=8d040af01fc9573bbc754b44e19fe3e4" alt="Document Image" width="879" height="478" data-path="images/integrations/sso/images-17.webp" />
</Frame>

You are all set!

### Auth0

Docs: [https://marketplace.auth0.com/integrations/rootly-sso-integration](https://marketplace.auth0.com/integrations/rootly-sso-integration)﻿

### Azure

Install SSO integration through the Azure marketplace

* Marketplace: [https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.rootly](https://azuremarketplace.microsoft.com/en-US/marketplace/apps/aad.rootly)
* Tutorial: [https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/rootly-tutorial](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/rootly-tutorial)

### Rippling

Integrate Rippling SSO + SCIM in one click [https://www.rippling.com/app-shop/app/rootly](https://www.rippling.com/app-shop/app/rootly)

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-18.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=6a12b8d1955fabe6966bd8a83709440f" alt="Document Image" width="895" height="1078" data-path="images/integrations/sso/images-18.webp" />
</Frame>

### Keycloak

Keycloak is an open-source identity and access management solution. Follow these steps to configure SAML SSO with Rootly.

#### Prerequisites

* Access to Keycloak admin console
* Keycloak realm set up (can use default `master` realm for testing)
* User account in Keycloak with email attribute configured

#### Step 1: Create SAML Client in Keycloak

1. Navigate to **Clients** in the Keycloak admin console
2. Click **Create Client**
3. Select **SAML** as the client type
4. Set **Client ID** to: `https://rootly.com/users/saml/metadata`
5. Click **Next** and **Save**

#### Step 2: Configure Client Settings

Navigate to your client's **Settings** tab and configure:

**Access Settings:**

* **Root URL**: `https://rootly.com/users/saml`
* **Home URL**: `https://rootly.com/users/saml`
* **Valid redirect URIs**:
  * `https://rootly.com/*`
  * `https://rootly.com/users/saml/auth`
* **Master SAML Processing URL**: `https://rootly.com/users/saml/auth`

**SAML Capabilities:**

* **Name ID format**: `email`
* **Force POST binding**: `On`
* **Include AuthnStatement**: `On`

**Signature and Encryption:**

* **Sign documents**: `On`
* **Sign assertions**: `On`
* **Signature algorithm**: `RSA_SHA256`
* **SAML signature key name**: `KEY_ID`
* **Canonicalization method**: `EXCLUSIVE`

#### Step 3: Configure Keys

Navigate to the **Keys** tab:

* **Client signature required**: `Off`
* **Encrypt assertions**: `Off`

#### Step 4: Configure Name ID Mapper

1. Go to **Client scopes** → **Dedicated scopes** → **Mappers**
2. Create or edit the **Email** mapper:
   * **Mapper type**: `User Attribute Mapper For NameID`
   * **Name**: `Email`
   * **Name ID Format**: `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
   * **User Attribute**: `email`

#### Step 5: Configure User Email

Ensure your test user has an email address set:

1. Navigate to **Users** → Select your user
2. Go to **Details** tab
3. Set **Email** field (e.g., `user@company.com`)
4. Set **Email verified**: `Yes`

#### Step 6: Get Keycloak Configuration

Collect the following information from Keycloak:

1. **Identity Provider ID**: `https://your-keycloak-host/realms/your-realm`
2. **Identity Login URL**: `https://your-keycloak-host/realms/your-realm/protocol/saml`
3. **Certificate**:

   * Go to **Realm Settings** → **Keys** → **RS256** → **Certificate**
   * Copy the certificate and format with proper PEM headers:

   ```
   -----BEGIN CERTIFICATE-----
   [certificate content]
   -----END CERTIFICATE-----
   ```

#### Step 7: Configure Rootly

In your Rootly SSO integration modal, set:

| Rootly Field           | Keycloak Value                                               |
| ---------------------- | ------------------------------------------------------------ |
| `Identity Provider Id` | `https://your-keycloak-host/realms/your-realm`               |
| `Identity Login Url`   | `https://your-keycloak-host/realms/your-realm/protocol/saml` |
| `Identity Logout Url`  | Leave blank or set logout URL                                |
| `Idp Cert`             | PEM-formatted certificate from Keycloak                      |
| `Domain Name`          | Your domain (e.g. company.com)                               |

### Jumpcloud

Let's begin by navigating to the **SSO Applications** page from the left navigation.

<Frame>
    <img src="https://mintcdn.com/rootly/mf386ksmmuX18Cga/images/integrations/sso/images-19.webp?fit=max&auto=format&n=mf386ksmmuX18Cga&q=85&s=1490c674534fde056eb7caa7be1cb2dc" alt="Document Image" width="3010" height="880" data-path="images/integrations/sso/images-19.webp" />
</Frame>

Click **Add New Application**

<img src="https://mintcdn.com/rootly/mf386ksmmuX18Cga/images/integrations/sso/images-29.webp?fit=max&auto=format&n=mf386ksmmuX18Cga&q=85&s=e88527d047f3872ec00b9db3ea327e29" alt="Images 29 Web" width="3010" height="870" data-path="images/integrations/sso/images-29.webp" />

Search for and install the **Rootly** application.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-20.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=4979772c9b3958b2aa885c393e30edf8" alt="Document Image" width="1884" height="824" data-path="images/integrations/sso/images-20.webp" />
</Frame>

Once installed, select the Rootly application to enter edit mode and navigate to the **SSO** tab.

Update the `IdP Entity ID` from `JumpCloud` to `JumpCloud-<BusinessName>`.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-21.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=f0003e5fb48aa2e2629c14d237ff9c59" alt="Document Image" width="1424" height="758" data-path="images/integrations/sso/images-21.webp" />
</Frame>

Download your **IDP Certificate**. It should download as a `.pem` file.

<Frame>
    <img src="https://mintcdn.com/rootly/mf386ksmmuX18Cga/images/integrations/sso/images-22.webp?fit=max&auto=format&n=mf386ksmmuX18Cga&q=85&s=92eb604a37851812cf2d76a254448815" alt="Document Image" width="3010" height="870" data-path="images/integrations/sso/images-22.webp" />
</Frame>

Navigate to your **Rootly SSO Integration** modal and fill in the following fields with the corresponding values from JumpCloud.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-23.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=cc80394f15353e456c34125cfee2e8f1" alt="Document Image" width="923" height="795" data-path="images/integrations/sso/images-23.webp" />
</Frame>

| Rootly Field           | JumpCloud Field                                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `Identity Provider Id` | `IdP Entity ID `                                                                                                             |
| `Identity Login Url`   | `IDP URL`                                                                                                                    |
| `Identity Logout Url`  | Leave blank or choose any page you'd want to navigate your user to when they log out.                                        |
| `Idp Cert`             | Open the certificate you downloaded in the previous step with a text editor of your choice. Copy and paste the text content. |
| `Domain Name`          | Your domain (e.g. mycompany.com)                                                                                             |

Go ahead `Enable` and `Save` your SSO setup in Rootly.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-24.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=b4c18b45b963cc89503104a40b021fd3" alt="Document Image" width="926" height="557" data-path="images/integrations/sso/images-24.webp" />
</Frame>

You're now SSO enabled!

If you want to set up **Just-In-Time (JIT) provisioning**, navigate to the **Identity Management** tab in edit mode and set the following fields according to the mappings below.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-25.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=89ade8e8c87a6251c217adf207579627" alt="Document Image" width="1459" height="757" data-path="images/integrations/sso/images-25.webp" />
</Frame>

* `API Type`: `SCIM API`
* `SCIM Version`: `SCIM 2.0`
* `Base URL`: `https://rootly.com/scim`
* `Token Key`: Pick this value up from your SSO Configuration screen in in Rootly

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-26.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=05e17b63c8905a56992a035e4eb64508" alt="Document Image" width="920" height="805" data-path="images/integrations/sso/images-26.webp" />
</Frame>

* `Test User Email`: You can use your own email as long as the email domain matches the one set in your Rootly SSO configuration page.

Go ahead and select `Test Connection`. You should see a successful message once a connection is confirmed.

If you'd like to **provision users by JumpCloud Groups**, go ahead and select the following option.This will allow you to provision the users in each JumpCloud Group with a specific Rootly Role.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-27.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=b38994c668dae7690827cef719cfec8c" alt="Document Image" width="1451" height="743" data-path="images/integrations/sso/images-27.webp" />
</Frame>

Navigate to your **Rootly SSO Integrations** modal and map the desired JumpCloud Group to the desired Rootly Role.

<Frame>
    <img src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/sso/images-28.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=6c15b15012da71d10cb947e1b33c6f99" alt="Document Image" width="875" height="630" data-path="images/integrations/sso/images-28.webp" />
</Frame>

Go ahead and `Save` your configuration. You're all set for JIT user provisioning!

## Login Behaviour

If you have SSO enabled, all other login methods such as Google, Slack, Email/Password will automatically redirect users to the SSO method instead.

## Misconfiguration

If you set up SSO incorrectly, you may not be able to sign in anymore. In that case please contact [support@rootly.com](mailto://support@rootly.com) or use the lower right chat widget for live assistance.


Built with [Mintlify](https://mintlify.com).