# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping/examples-setting-up-custom-mapping-for-idps/example-setting-up-custom-mapping-for-an-okta-oidc-app.md

# Example: setting up custom mapping for an Okta OIDC app

Follow these steps configure an integration for OIDC Okta.

## Create an Okta OIDC app

1. In Okta, select **Applications** > **Applications** > **Create App Integration** then choose **OICD OpenID Connect** and **Web Application.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-107ba139a459856075d6e6b578b3aba0153fa992%2F1.png?alt=media" alt="Create a new app integration in Okta"><figcaption><p>Create a new app integration in Okta</p></figcaption></figure>
2. In the next step add an **App integration name** for your OIDC application, check the **Implicit** **Grant Type** and add the **Sign-in redirect URI** relevant to your [Snyk platform deployment](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/set-up-snyk-single-sign-on-sso). Remove the placeholder **Sign-out redirect URI** and choose your assignment access control before clicking **Save.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ec3d770ddff530908096001f2410a9dae6f93b16%2F2%20(1).png?alt=media&#x26;token=5a8dc6cc-7d03-4cd8-8bfa-05035ed40759" alt="Provide details for new web app integration"><figcaption><p>Provide details for new web app integration</p></figcaption></figure>
3. On the application page that opens after saving, copy the details identified in [OIDC information to provide to Snyk](https://docs.snyk.io/implementation-and-setup/enterprise-setup/set-up-snyk-single-sign-on-sso#oidc-information-to-provide-to-snyk) and provide to your Snyk contact:
   * Client ID
   * If you are not using the Implicit Grant type, the client secret
4. Also, share with Snyk the Issuer URL/domain. This is typically the URL you find in your browser address bar without "-admin", for example, <https://customer.example.okta.com>. It can also be found under the **Sign-On** tab of your application by editing the **OpenID Connect ID Token** from **Dynamic** Issuer to **Okta URL**.

If you wish to set up custom mapping, move on to the next section of this guide.

## Add custom mapping

[Custom mapping](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping) for an OIDC application in Okta is easily managed through custom attributes on the Group level.

### Create a custom app user attribute to contain both the Snyk Organization name and role

1. In Okta, select your newly created OIDC application user profile under **Directory** > **Profile editor.**
2. Select **+Add Attribute.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1afe1ec02f568024263dd26e8677924fbe204921%2F3.png?alt=media&#x26;token=359113f0-cf22-4ec0-ad5c-44214b533367" alt="Okta profile editor"><figcaption><p>Okta profile editor</p></figcaption></figure>
3. In the corresponding fields, add the following details for this Attribute and click **Save**:\
   **Data type**: string array\
   **Display name**: Snyk roles\
   **Variable name:** roles\
   **Group Priority**: Combine values across groups

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-77ebb69ead31aa192f7f1b6ccf9b4f67b4355063%2F4.png?alt=media" alt="Attribute details"><figcaption><p>Attribute details</p></figcaption></figure>

### Assign the attribute to the relevant Okta groups

1. On the main page of Okta select **Directory** > **Groups**.
2. Select a **Group**, navigate to the **Applications** tab, click **Assign** **application** if not already assigned, and choose your Snyk OIDC app,. Then click on the pencil next to the displayed Snyk OIDC app.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5f70a0fb03862c01c183859e855e026e405112c3%2F5%20(1).png?alt=media&#x26;token=1c7c9c83-6cbe-45f6-8919-f49ed01e969c" alt="Group selected for modicification"><figcaption><p>Group selected for modicification</p></figcaption></figure>
3. In the **Edit App Assignment** dialog, add the Snyk org name + role associated with your Okta group (no spaces or capital letter(s)), following the syntax explained in [custom mapping](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping) (or [legacy custom mapping](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping/legacy-custom-mapping) if using the legacy mapping option). Example, `snyk:org:*:org_admin`.\\

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ec30eca1881fae6c14cc89fa022d1eec4e05cd94%2Fimage%20(160).png?alt=media" alt="Adding Snyk roles"><figcaption><p>Adding Snyk roles</p></figcaption></figure>
4. Repeat the preceding steps for all your applicable Okta groups to assign the org name and role combination to each user within each configured group.
