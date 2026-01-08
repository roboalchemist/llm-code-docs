# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/configure-self-serve-single-sign-on-sso/azure-ad-enterprise-application-setup.md

# Entra ID Enterprise application setup

This example shows setting up an Entra ID (formerly Azure AD) Enterprise Application and connecting this to Snyk to facilitate SSO. To configure your Azure Enterprise Application to use SSO with Snyk, first obtain an entity ID and a reply URL (Assertion Consumer Service URL) from Snyk.

1. From the dropdown at the top left select **GROUP OVERVIEW** and then the cog icon (top right corner) to get to your group settings.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8ad0c5c609f27fd4ec9f1faf55c6a70583e3e8ce%2F1.png?alt=media" alt="Select group overview"><figcaption><p>Select group overview</p></figcaption></figure>
2. Click on **SSO** and copy the values under **Entity ID** and **ACS URL** or leave the browser tab open for easy access.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8b7939bb9485e4396f209b637449862baaa4ff04%2F2.png?alt=media" alt="Group Settings: SSO"><figcaption><p>Group Settings: SSO</p></figcaption></figure>
3. Navigate to Azure and open Entra ID.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b4f0203de5cbcc7e328f67638ff2ee49f8b5fbed%2F3.png?alt=media" alt="Entra ID Default Directory"><figcaption><p>Entra ID Default Directory</p></figcaption></figure>
4. Click **Add** then **Enterprise application**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1a6f36e70b20681642d517c0deaf509de63c87ec%2F4.png?alt=media" alt="Add Enterprise application"><figcaption><p>Add Enterprise application</p></figcaption></figure>
5. Choose **Create your own application**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a99ca96be597636d96cd66cd5d90bab7ca1b5c56%2F5%20(4).png?alt=media" alt="Create your own application"><figcaption><p>Create your own application</p></figcaption></figure>
6. Name the application appropriately, for example, **Snyk-SSO**, making sure that **Integrate any other application you don't find in the gallery (Non-gallery)** is selected and then click **Create**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e59bfd22ee7e216cd9472743bce1d07758e4740f%2F6%20(1).png?alt=media&#x26;token=b95f76c8-529e-488c-b3cc-4e7c226e4d88" alt="Application name and integration"><figcaption><p>Application name and integration</p></figcaption></figure>
7. For the new app, select **Set up single sign on** and **Get started**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b733bd40d5b24abc6c7a2a102340bf301e7329b5%2F7%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(2).png?alt=media&#x26;token=c676d4d8-84df-4815-93a3-f85c36fe3cb8" alt="Set up single sign-on, Get started"><figcaption><p>Set up single sign-on, Get started</p></figcaption></figure>
8. Select **SAML** as the SSO method.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bfd18fbf3d40fbfc65cb39ab0f52795dbb1e21be%2F8%20(1).png?alt=media&#x26;token=27fd17ac-1b15-4b39-a8df-bf57ab64f851" alt="Select SAML"><figcaption><p>Select SAML</p></figcaption></figure>
9. Click **Edit** under **Basic SAML configuration**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-82c61f8bf083b7a820648f03bc20a3f897261924%2F9%20(1).png?alt=media" alt="Edit basic SAML configuration"><figcaption><p>Edit basic SAML configuration</p></figcaption></figure>
10. Add the Identity (Entity ID) and reply URL (Assertion Consumer Service URL) you obtained from Snyk and click **Save**; then close the edit window.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3bc1f3887dd71cd01cd20ee317cfc5ec97077183%2F10.png?alt=media" alt="Entity ID and Assertion Consumer Service URL"><figcaption><p>Entity ID and Assertion Consumer Service URL</p></figcaption></figure>
11. Scroll to find the login URL needed to finish the configuration in Snyk. Copy it and paste it into the SSO settings in the Snyk portal.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-43a1c4bf1bcddd764d4615ddd306af027d36e572%2F11.png?alt=media" alt="Login URL"><figcaption><p>Login URL</p></figcaption></figure>

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e9924c7247ffd98763e03e94e52355871dd71c12%2F1%20(3).png?alt=media&#x26;token=661a32cb-914c-4127-8833-5f3640cb8a03" alt="Sign in URL in Snyk portal"><figcaption><p>Sign in URL in Snyk portal</p></figcaption></figure>
12. Return to Entra ID and click **Download** next to **Certificate (Base64)**.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-dda738cb076e3a0d2c8152f5fe57a493dbc8ce00%2F13.png?alt=media" alt="Download SAML Certificate (Base 64)"><figcaption><p>Download SAML Certificate (Base 64)</p></figcaption></figure>
13. Open the downloaded certificate in your preferred text editor, copy the text and paste it into the Snyk **X509 signing certificate** field, and add the relevant domains that are supported by this SSO connection.\
    Finally, verify if an **IdP-initiated workflow** should be enabled and then click **Create Auth0 connection** if you are creating a completely new connection or **Save changes** if you are editing an existing connection.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3ad28c9f75b5c469f17903a091940e303315962f%2F14.png?alt=media" alt="Enter certificate and domains supported, set connection"><figcaption><p>Enter certificate and domains supported, set connection</p></figcaption></figure>
14. Decide how new users should be treated when signing in and choose the option you would like to use: **Group member**, **Org collaborator**, or **Org admin**. Finally, modify the **profile attributes** if your settings in Azure deviate from the default; then click **Save changes** and verify you can log in, either with the direct URL at the top of step 3 or by going to the [generic SSO login](https://app.snyk.io/login/sso).\
    \
    If you are not receiving profile values as expected, you may need to add email, name, and username as additional claims within Azure SSO settings and then map those accordingly in the Snyk SSO **Profile attributes** section.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bacfa4eeba3830012f8c6788552d6fa6348c7c64%2Fclaim1.png?alt=media" alt="Azure claim settings"><figcaption><p>Azure claim settings</p></figcaption></figure>

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-940ae8afa89d22fc2d5cc3885386ae3858663ed8%2Fimage2.png?alt=media" alt="Profile attributes section"><figcaption><p>Profile attributes section</p></figcaption></figure>

If you wish to add signature verification of the incoming Snyk request:

1. Download the **Signing certificate** at step 1 of the Snyk SSO settings.
2. Use the following openssl command to convert it to .cer-format `openssl x509 -outform DER -in snyk.pem -out snyk.cer`
3. At the bottom of the **SAML Certificates** settings of your SSO app in Active Directory, click **Edit** next to **Verification certificates.**
4. Check **Require verification certificates** and upload the certificate from the output of the above openssl command and click **Save**.
