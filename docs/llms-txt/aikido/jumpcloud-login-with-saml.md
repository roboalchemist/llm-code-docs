# Source: https://help.aikido.dev/getting-started/automated-user-management/saml-login/jumpcloud-login-with-saml.md

# JumpCloud: Login with SAML

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page with option to enable SAML authentication.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fjumpcloud-login-with-saml_e1fd0c18-f548-4071-919d-67e1fac297ec.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML authentication setup screen with required URLs and Name ID format.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fjumpcloud-login-with-saml_09a7d874-2d07-4f24-b41c-83eb4ae62a50.png?alt=media)

### Continue in JumpCloud <a href="#continue-in-jumpcloud" id="continue-in-jumpcloud"></a>

**Step 1.** Go to **User Authentication** > **SSO Applications** in the JumpCloud Admin Portal navigation.

**Step 2.** Click the **Add New Application** and search for **SAML 2.0**. Click **Next**.

**Step 3.** Choose a **Display Label** and click **Save Application**.

**Step 4.** Click **Configure Application**.

**Step 5.** Click on the **SSO** tab and fill following fields:

* **Idp Entity ID:** `https://console.jumpcloud.com/<appname>`
* **SP Entity ID:** `https://app.aikido.dev/saml`
* **ACS URLs** - **Default URL:** `https://app.aikido.dev/api/saml/saml_auth?samlClientId=...` (As shown in Aikido)
* **SAMLSubject NameID:** `email`
* **SAMLSubject NameID Format:** `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
* **Signature Algorithm:** `RSA-SHA256`
* **Default RelayState:** You can leave this empty

![SAML 2.0 single sign-on configuration settings for secure identity management integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-eff061b095b5f561245505a012f6875e2e63d38a%2Fjumpcloud-login-with-saml_05b8da4a-cc77-4099-856c-70e00b369a45.png?alt=media)

**Step 6.** We'll continue in Aikido, but you might as well click **Save** and come back to this screen.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the:
  * **Entity ID / Issuer:** `https://console.jumpcloud.com/<appname>` (Make sure this matches what you've entered as **Idp Entity ID** in JumpCloud. If you're having issues with this, see the Troubleshooting section at the bottom)
  * **Single Sign-On URL:** as shown in JumpCloud under **IDP URL**. (looks like `https://sso.jumpcloud.com/saml2/<appname>`)
  * **X.509 Certificate**: This can be fetched in different ways. One way is to click **Export Metadata** in JumpCloud the config and open the downloaded xml. You'll find your certificate between the `ds:X509Certificate` tags.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML Authentication setup form for configuring identity provider details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fjumpcloud-login-with-saml_282cde57-79ed-4aab-bddb-bd4073327ee6.png?alt=media)

> Success! People having access to your JumpCloud SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fjumpcloud-login-with-saml_13d717d7-9d5e-4dd1-ab34-4d5b6455f475.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO—no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fjumpcloud-login-with-saml_ca4791cb-4534-471c-8757-b2dc3ca7e569.png?alt=media)

![Login screen with Google, Microsoft, and email login options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fjumpcloud-login-with-saml_ff9dd4af-ca57-484d-aacb-ed9cbe5aad7d.png?alt=media)

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

**Error**

![SAML client already exists error; prompts user to contact support for linking organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fde2154e1f44785ccbde15520e03afb67162f2c8%2Fjumpcloud-login-with-saml_5f7761f9-08db-4072-8559-0567d1bfc719.png?alt=media)

**Solution**

Make sure the **Idp Entity ID** is unique. Perhaps you could change it to `https://console.jumpcloud.com/<samlClientId>`. Note that you'll also need to change it in Aikido in **Entity ID / Issuer** as these should match.
