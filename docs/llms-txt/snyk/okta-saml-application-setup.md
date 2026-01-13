# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/configure-self-serve-single-sign-on-sso/okta-saml-application-setup.md

# Okta SAML application setup

This example shows setting up an Okta SAML application and connecting this to Snyk to facilitate SSO. To configure your Okta to use SSO with Snyk, you need an entity ID and a reply URL (Assertion Consumer Service URL) from Snyk.

1. From the drop-down at the top left select **GROUP OVERVIEW** and then the cog wheel (top right corner) to get to your group settings.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8ad0c5c609f27fd4ec9f1faf55c6a70583e3e8ce%2F1.png?alt=media" alt="Select group overview"><figcaption><p>Select group overview</p></figcaption></figure>
2. Click on **SSO** and copy the values under **Entity ID** and **ACS URL** or leave the browser tab open for easy access.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8b7939bb9485e4396f209b637449862baaa4ff04%2F2.png?alt=media" alt="Group Settings: SSO"><figcaption><p>Group Settings: SSO</p></figcaption></figure>
3. Navigate to [Okta](https://www.okta.com/se/login/), open the application menu, and click on **Create App Integration.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0a9b07ffb6f6719e59ed32143e4b35e47b102cb9%2F1%20(1).png?alt=media" alt="Okta Applications main page"><figcaption><p>Okta Applications main page</p></figcaption></figure>
4. Choose **SAML 2.0** and name your application appropriately; click **Next**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-df9b5dc50bc791fb4ed0357879d6cae12b90950b%2F2.png?alt=media" alt="Okta SAML application creation"><figcaption><p>Okta SAML application creation</p></figcaption></figure>
5. Add the Entity ID and the sign on URL you copied from Snyk to the appropriate fields.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e7c636b9005d427257a5b327a6eb0366fa689054%2F3.png?alt=media" alt="Add SSO details in Okta"><figcaption><p>Add SSO details in Okta</p></figcaption></figure>
6. Scroll down to **Attribute Statements** and add three attributes named with values as follows:

   * **Name**: email, **Value**: user.email
   * **Name**: name, **Value**: user.firstName + " " + user.lastName
   * **Name**: username, **Value**: user.login

   Click **Next** and enter feedback details if desired or go to the next step.
7. Open your Okta application list again and click on your newly created application and the **Sign on** tab. To the right of the page, click on **View SAML setup instructions** then from the page that opens, copy the **Identity Provider Single Sign-On URL** and the **X.509 certificate**.
8. Go back to the previous page and go to the **Assignments** tab. Click on **Assign** and choose users, groups, or both according to your needs.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bdb8b4d12c40986cdfa6f32a55d3dc1a73f72505%2F7%20(1).png?alt=media&#x26;token=e1f36ac0-8a3c-4931-a773-a357493ec890" alt="Assign the SSO application"><figcaption><p>Assign the SSO application</p></figcaption></figure>
9. Go back to the Snyk portal, scroll to step 2, and enter the details from step 7, including the domain(s) you wish to use over the SSO connection, verify if an IdP-initiated workflow should be enabled, and then click **Create Auth0 connection.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-caafe253ba4e6f3034ec6e414ee6cbb4fb0095b2%2F8.png?alt=media" alt="Snyk SSO step 2"><figcaption><p>Snyk SSO step 2</p></figcaption></figure>
10. Scroll to step 3 and determine how new users should be treated when signing in. Choose the option you would like to use: **Group member, Org collaborator** or **Org admin**. Finally, enter the profile attributes as you configured them in Okta, click **Save changes** and verify you can log in, either with the direct URL at the top of step 3 or by going to the [generic SSO login](https://app.snyk.io/login/sso).

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5627b099a4498b1f435de68e4ad6d1432e4b80cd%2F9.png?alt=media" alt="Profile attributes"><figcaption><p>Profile attributes</p></figcaption></figure>
