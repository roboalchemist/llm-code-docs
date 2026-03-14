# Source: https://help.aikido.dev/getting-started/automated-user-management/saml-login/google-workspaces-login-with-saml.md

# Google Workspaces: Login with SAML

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

### Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info page showing option to enable SAML authentication.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fgoogle-workspaces-login-with-saml_6bb8581e-5aab-49a3-8ce8-4b5f13a49749.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen with required URLs and Name ID format fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fgoogle-workspaces-login-with-saml_131b2923-631f-42e8-af65-87faa35c50e0.png?alt=media)

### Continue in Google <a href="#continue-in-google" id="continue-in-google"></a>

**Step 1.** Go to **Apps** > **Web and mobile apps** in the Google Admin Console.

**Step 2.** Click the **Add app** dropdown and select **Add custom SAML app**.

**Step 3.** Choose an **App name** and click **Continue**.

**Step 4.** Ignore the metadata page for now, we'll get this information later on. Click **Continue**.

**Step 5.** Fill the fields **ACS URL**, **Entity ID** and **Name ID format** with the fields visible in Aikido (see above) and click **Continue** and click **Finish**.

**Step 6.** Now you should be on the detail page of your newly created app. Click **Download Metadata**.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in the modal in Google.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML authentication setup form requiring identity provider and company domain details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fgoogle-workspaces-login-with-saml_33ba5a40-204e-4c76-8a85-971b8115c30b.png?alt=media)

> Success! People having access to your Google SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fgoogle-workspaces-login-with-saml_d44ce4f2-726b-4108-b8d5-bb83c49b1490.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO—no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fgoogle-workspaces-login-with-saml_fa842428-89f5-4aa8-91a4-56cc2a7533eb.png?alt=media)

![Login options: Google, Microsoft, or email for account access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fgoogle-workspaces-login-with-saml_2ec57086-151e-48f9-ab55-0c1ac60cafb1.png?alt=media)
