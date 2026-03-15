# Source: https://help.aikido.dev/getting-started/automated-user-management/saml-login/okta-login-with-saml.md

# Okta: Login with SAML

{% hint style="info" %}
This feature is only available on a **paying** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page showing option to enable SAML authentication for a GitHub account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fokta-login-with-saml_cd9146ff-36d4-4839-a879-0092907a7019.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen with required URLs and Name ID format for configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6a282e9f1b96450fcddfcafe2bb9f1476210c99c%2Fokta-login-with-saml_01f94720-00dc-4d8f-95a3-887c7546433b.png?alt=media)

### Continue in Okta <a href="#continue-in-okta" id="continue-in-okta"></a>

**Step 1.** Go to **Applications** > **Applications** in the Admin Console.

**Step 2.** Click **Create App Integration**, select **SAML 2.0** and click **Next**.

**Step 3.** Choose an **App name** and click **Next**.

**Step 4.** Fill the fields **Single sign-on URL**, **Audience URI** and **Name ID format** with the fields visible in Aikido (see above) and click **Next**.

**Step 5.** Now you should be on the tab **Sign On** and you should see **Metadata details**. Click **More details**.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Okta.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Form for entering SAML authentication details for secure single sign-on setup.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fokta-login-with-saml_bf648fe2-3f42-4490-9067-3840392e84f9.png?alt=media)

> Success! People having access to your Okta SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fokta-login-with-saml_b6d1fe83-fa12-410c-b6de-77ac12f0f41b.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click free login and sign-up with Google, Microsoft, or SSO—no card required.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fokta-login-with-saml_c233b6e3-7de6-40fe-b58c-8e6414a89556.png?alt=media)

![Login screen with Google, Microsoft, and email authentication options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fokta-login-with-saml_4e595972-8a51-4473-956b-7da0b4fd41fa.png?alt=media)
