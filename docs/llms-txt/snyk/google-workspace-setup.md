# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/configure-self-serve-single-sign-on-sso/google-workspace-setup.md

# Google Workspace setup

This example shows setting up an Google Workspace SAML application and connecting it to Snyk to facilitate SSO.

For details in addition to the information provided on this page, see [Set up your own custom SAML app](https://support.google.com/a/answer/6087519).

Start by logging into the Google Workspace [admin area](https://admin.google.com).

1. Go to **Apps** and then click **Web and mobile apps**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c3a24caea3c8d1f6c8008a1ac7c71704834641bc%2F1%20(2)%20(1).png?alt=media&#x26;token=8bdff586-ace1-4523-a2a0-f6f43cb22f91" alt="Open Web and Mobile apps"><figcaption><p>Open Web and Mobile apps</p></figcaption></figure>
2. Click on **Add app** and choose **Add custom SAML app**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-eed0883e8d68f554c6170e1dbf08c245445de7e9%2F2.png?alt=media" alt="Add new custom SAML app"><figcaption><p>Add new custom SAML app</p></figcaption></figure>
3. Name your application appropriately and click **Continue**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3558e6dfd4cc9927b6a70ce8257d8e24806b30f0%2F3.png?alt=media" alt="Name the SAML app"><figcaption><p>Name the SAML app</p></figcaption></figure>
4. Download the certificate and open it in your preferred text editor.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6d1e9b9a5b17b0b2f4944fb997b2aab921e9973e%2F4.png?alt=media" alt="Download signing certificate"><figcaption><p>Download signing certificate</p></figcaption></figure>
5. Navigate to the Snyk portal, login and from the drop down at the top left select **GROUP OVERVIEW** and then the cog wheel (top right corner) to get to your group settings.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8ad0c5c609f27fd4ec9f1faf55c6a70583e3e8ce%2F1.png?alt=media" alt="Open group view in Snyk"><figcaption><p>Open group view in Snyk</p></figcaption></figure>
6. Click on **SSO**, scroll down to step 2, and paste the Google SSO URL from step 4 into **Sign in URL** and the certificate in your text editor into **X509 signing certificate**.\
   Add the domain name(s) you are configuring this connection for in **Email domains and subdomains that need SSO access**.\
   Verify if an **IdP-initiated workflow** should be enabled and then save your modifications

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-efff3c3326e1e7a1b771dd2f910262fa2f638afc%2F6.png?alt=media" alt="Enter details from Google Workspace"><figcaption><p>Enter details from Google Workspace</p></figcaption></figure>
7. Scroll up to step 1 and copy the **Entity ID** and **ACS URL**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7406cbedddffa95632746b1b911f15bf9e87083a%2F7.png?alt=media" alt="Copy details from Snyk"><figcaption><p>Copy details from Snyk</p></figcaption></figure>
8. Go back to the Google admin portal , click **Continue,** and paste those two values into their respective fields. Then tick **Signed response**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3b2200afa46ae4a18f28a71cd58d50e94417312c%2F8.png?alt=media" alt="Enter details from Snyk in Google"><figcaption><p>Enter details from Snyk in Google</p></figcaption></figure>
9. Click **Continue**, add an app attribute named email tied to the **Primary Email**, and save the configuration.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1a58835286eb3429cb6c91d6fe1fcd887189f5bd%2F9.png?alt=media" alt="Add email attribute"><figcaption><p>Add email attribute</p></figcaption></figure>
10. Enable access to your app for your users by clicking **User Access**, tick **On for everyone**, and **Save**. Modify organizational access as needed.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4f96e9261ddf2954cb0ccf80bc331a78cfbae109%2F10.png?alt=media" alt="Enable SSO app for the organization"><figcaption><p>Enable SSO app for the organization</p></figcaption></figure>
11. Finalize the setup by going back to the Snyk portal and decide how new users should be processed when signing in. Choose the option you would like to use: **Group member**, **Org collaborator**, or **Org admin**.
12. Then add the previously created **email** app attribute to both **Email** and **Username** and save the configuration. If you wish to populate the full name you may configure a custom attribute in Google Workspace.

    <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a2444467251813441b2aa412fe867224cb183753%2F11.png?alt=media" alt="Tie together attributes from Google to Snyk"><figcaption><p>Tie together attributes from Google to Snyk</p></figcaption></figure>
