# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/single-sign-on-sso.md

# Single Sign-On (SSO)

## Configuring Single Sign-On (SSO)

Tabnine provides full SAML 2.0 support so you can integrate with your chosen IdP and manage your Tabnine users’ SSO login in a centralized way. Here you can find the walkthrough process for integrating with the common IdPs in the market.

#### Setting SSO

* Sign in to the Tabnine console as an admin.
* Go to the **General** page under **Settings.**
* In the **Single Sign-on** section, enable the toggle button.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4d1c609cb3f41091777fa212232ccc2fcf813f4b%2FSSO%20activate%20gif.gif?alt=media" alt=""><figcaption></figcaption></figure>

* Copy the **SAML Callback** URL. Fill in the certificate, entry point, identifier format, and AuthnContext from [Azure](#use-azure-as-a-saml-idp) or [Okta](#use-okta-as-a-saml-idp). Click **Save.**

{% hint style="info" %}
"Identifier format" (optional) refers to a name identifier format of the request of your IdP.

"AuthnContext" (optional) specifies the authentication mechanism that the IdP should use and the level of assurance for the user's identity.
{% endhint %}

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cec82dc14f31f13174afd6ae95dbf2b298bf7e93%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9288c7921771207cbb2c42cb9b757df708a0e4fa%2Fazure%20logo.svg?alt=media" alt="" data-size="line"> Use Azure as a SAML IdP

1. Enter <https://portal.azure.com/>.
2. After logging into Azure, go to the **Azure Active Directory** tab.
3. Select **Enterprise applications** service.
4. Choose **New application.**
5. Choose **Create your own application.**
6. Choose **Non-gallery application.** (Integrate any other application you don't find in the gallery.)
7. Name it (for example, "TabnineSSO") and click **Add.**
8. Choose **Setup single sign-on**.
9. Select **SAML-based Sign-on** as the SSO mode.
10. Next, add the Tabnine service provider details to the configuration in Azure. Set the following values in **Identifier (Entity ID)** and **Reply URL (Assertion Consumer Service URL),** replacing **tabnine.customer.com** with your Tabnine cluster domain:\\

    <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-023abca927410cab7f2935d1cfa5a699b05b34b2%2Fsso1%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>
11. Choose **user.mail** as the value for **Unique User Identifier:**\\

    <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-518ad5719a487cbd67522eae7cbafbdea474ff3a%2Fsso2%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>
12. In Section 3 - SAML Certificates, choose **Download certificate (Base64).**
13. In Section 4, copy **Login URL** **value** to use in the next step.
14. Finally, make sure the following are checked at the bottom:\
    \&#xNAN;**☑ wantsAssertionSigned** and **☑ disableRequestedAuthnContext**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a32889cb168311f728ba8c6fa2a2229ea8b8fe33%2Fimage.png?alt=media" alt=""><figcaption><p>Be sure to have checked off <strong>☑ wantsAssertionSigned</strong> and <strong>☑ disableRequestedAuthnContext</strong> for Azure configurations</p></figcaption></figure>

### <picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5e007ad462944a955a0a5cdeb108fec4f05fbdd4%2FOkta_Aura_White_L.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-498d994363f704ce6b160eee04153dd8ca5128bb%2Fokta-logo.png?alt=media" alt="" data-size="line"></picture> Use Okta as a SAML IdP

1. Enter your Okta admin panel in **Applications > Create App Integration > SAML2 integration.**
2. Set an App name (e.g., "Tabnine"):\\

   <figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-875c72d602f166151fb88395e72c15a8517e148c%2Fsso3%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>
3. Next, set the following values:\
   \
   **Single sign-on URL:** *https\://**tabnine.customer.com**/auth/sign-in/sso/saml/callback*\
   \
   **Audience URI (SP Entity ID):** *https\://**tabnine.customer.com**/auth/sign-in/sso/saml*\
   \
   **Name ID format:** `EmailAddress`\
   \
   \&#xNAN;*NOTE: Replace **tabnine.customer.com** with your Tabnine cluster domain.*\\

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-06593635ac1a6a5bbc4b10463ee3e72b575a9e9f%2Fsso4%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

4. Choose 🔵 **I'm an Okta customer adding an internal app.**\\

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ec3a968a31cdbf657e17c5e46dd1876a6e5cbd9b%2Fsso5%20(1).webp?alt=media" alt=""><figcaption></figcaption></figure>

5. In the created App in Okta ("Tabnine"), Sign on tab, copy **Sign on URL** value and **Signing Certificate** values.
