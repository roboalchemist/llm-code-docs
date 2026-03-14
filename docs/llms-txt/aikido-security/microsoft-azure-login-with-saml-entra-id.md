# Source: https://help.aikido.dev/getting-started/automated-user-management/saml-login/microsoft-azure-login-with-saml-entra-id.md

# Microsoft Azure: Login with SAML/ Entra ID

{% hint style="info" %}
This feature is only available on a **Pro** or **Advanced** plan and is not enabled by default. If you’d like to enable this feature, please reach out via the chat in the bottom right corner within Aikido.
{% endhint %}

> If you switch to SAML Login instead of auto-onboarding via your Git provider, team import from GitHub, Bitbucket, or Azure DevOps will no longer work. You will need to manage your teams manually moving forward, either through the Aikido UI or [Access Profiles.](https://help.aikido.dev/getting-started/automated-user-management/saml-login/saml-user-rights-access-profiles-recommended)

## Setting up SAML in your account <a href="#setting-up-saml-in-your-account" id="setting-up-saml-in-your-account"></a>

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Workspace info screen with option to enable SAML authentication for GitHub account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-52bef8060e16dc93c85e5a6c3a75db646ff32e9a%2Fmicrosoft-azure-login-with-saml-entra-id_226233e4-b7ed-4614-a3c7-2316aa00830e.png?alt=media)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![SAML Authentication setup screen showing required URLs and Name ID format for configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d0f87c55a3ce6f0dca79d576308678a1d33cf8d3%2Fmicrosoft-azure-login-with-saml-entra-id_af05c8a1-f44f-499c-85a3-40090e79ede6.png?alt=media)

### Continue in Azure <a href="#continue-in-azure" id="continue-in-azure"></a>

**Step 1.** Go to **Microsoft Entra ID**.

**Step 2.** Click the **Add** dropdown and select **Enterprise application**.

![Adding a new enterprise application in Microsoft Azure Active Directory.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-be0bbc97894a04cf73d8b8813002f0a18089e255%2Fmicrosoft-azure-login-with-saml-entra-id_e2b0c97b-cd57-473d-a88b-ae86bae5f17e.jpg?alt=media)

**Step 3.** Click **Create your own application**, choose a name for your app and select 'Non-gallery'.

![Creating a custom non-gallery application named "Aikido-SSO" for integration purposes.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a593f1ffb0e6d737d0e15ce4ee98ab5cf9ef961%2Fmicrosoft-azure-login-with-saml-entra-id_34300cbc-6836-46d3-bcda-326d3726eaac.jpg?alt=media)

**Step 4.** Select **Set up single sign on**.

![Aikido-SSO application setup: Assign users and configure single sign-on in Microsoft Entra.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-071fa54e26d712a8a8ec61ff1ff343618ac94105%2Fmicrosoft-azure-login-with-saml-entra-id_041ab86f-83f5-4f7d-b318-3a5e4b8a4fdb.jpg?alt=media)

**Step 5.** Click the **SAML** option.

![Enable SAML single sign-on for secure application authentication in Aikido-SSO.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-adb03664c9535a4fbc72aff1305439f6e3de55d4%2Fmicrosoft-azure-login-with-saml-entra-id_1659ec2c-7283-426d-894c-48ef502505ec.jpg?alt=media)

**Step 6.** On **step 1**, click **Edit.**

![Basic SAML Configuration: Edit required Identifier and Reply URL fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e19ceee608639777d51f0504d6bd8cd3489dfadf%2Fmicrosoft-azure-login-with-saml-entra-id_62185eb3-6a97-427b-b914-3a1ec840b54c.jpg?alt=media)

**Step 7.** Fill in the **Entity ID** and **ACS URL** as shown in Aikido.

![Configuration screen for SAML SSO with Entity ID and Reply URL fields specified.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61508f5f6273b02030c7226c9cd8e74525d7a8f6%2Fmicrosoft-azure-login-with-saml-entra-id_b29695e0-9d2a-4f64-9a88-e30172e85348.jpg?alt=media)

**Step 8.** At **step 2**, click **Edit.**

![User attributes and claims mapping with editable options highlighted.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5dcf9aa3540b381c1af5bf5383478aa4ac7d0836%2Fmicrosoft-azure-login-with-saml-entra-id_0cc0859a-2fbd-4ca9-9442-c8114c034d3b.jpg?alt=media)

**Step 9.** Click the **Unique User Identifier (Name ID)**.\
Optional: clicking 'Add new claim' at the top of this page allows you to add [custom attributes](https://help.aikido.dev/getting-started/automated-user-management/saml-login/saml-user-rights-using-custom-attributes-advanced) to SAML. More info [here](https://help.aikido.dev/doc/microsoft-azure-custom-attributes-with-saml--entra-id/docFaysVwVZy).

![Highlighted SAML claim: Unique User Identifier (Name ID) for user identification.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9bb311d72ded942631541250588a40360249a636%2Fmicrosoft-azure-login-with-saml-entra-id_c58d21d6-7556-43db-96eb-3f2b81663b8d.jpg?alt=media)

**Step 10.** Make sure to set **Source attribute** to `user.mail` here.

![Configuring a SAML claim for user email as the name identifier in Azure AD.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a86243ee8598d6afe63a05a23b910836aed9038%2Fmicrosoft-azure-login-with-saml-entra-id_7359629d-6b9b-4c7a-822a-46ddb14ae30e.jpg?alt=media)

**Step 11.** At step 3 you can download the **Certificate (Base64)** & at step 4 you'll see the **Login URL** and **Mircosoft Entra Identifier**. These should be copy and pasted to Aikido.

### Go back to Aikido <a href="#go-back-to-aikido" id="go-back-to-aikido"></a>

* Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Azure.
* Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![SAML Authentication setup form for configuring Single Sign-On (SSO) credentials.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-851c3a7f92d35b9f083ce8fc28190e0b53544b85%2Fmicrosoft-azure-login-with-saml-entra-id_ecd63576-b9c5-464a-ae53-3bbb1494f534.png?alt=media)

> Success! People having access to your Azure SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client <a href="#id-2-options-for-users-to-login-using-your-saml-client" id="id-2-options-for-users-to-login-using-your-saml-client"></a>

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![SAML Authentication settings with options to manage or copy the login link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c359002b6002f1c6d80bd9683f7eaf4f8808d1c3%2Fmicrosoft-azure-login-with-saml-entra-id_bf7e0490-bc80-42f3-8517-805537105a8d.png?alt=media)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![One-click login and sign-up with Google, Microsoft, or SSO; no credit card needed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2bfbc01b8c5f3ac8d7bc3a12a695819f8f89a2c7%2Fmicrosoft-azure-login-with-saml-entra-id_a72d4e17-3465-4a72-bd1b-5b15115eb4da.png?alt=media)

![Login screen offering Google, Microsoft, or email sign-in options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-911aa517b4f1102384e77de360b476ca88642232%2Fmicrosoft-azure-login-with-saml-entra-id_9ad5fafb-e1f7-4ac8-b3b7-37d4639c046d.png?alt=media)
