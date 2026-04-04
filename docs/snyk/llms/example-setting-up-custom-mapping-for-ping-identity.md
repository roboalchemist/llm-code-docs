# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping/examples-setting-up-custom-mapping-for-idps/example-setting-up-custom-mapping-for-ping-identity.md

# Example: setting up custom mapping for Ping Identity

This page explains how to configure the custom mapping of roles for Ping Identity using [Legacy custom mapping](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping/legacy-custom-mapping).

{% hint style="info" %}
This guide assumes your Ping Identity application is configured and functional.
{% endhint %}

{% hint style="info" %}
Any step on the Snyk side in setting up the Enterprise application must be performed by your Snyk contact, as self-serve SSO does not accommodate custom mapping.
{% endhint %}

1. In your application configuration, select **Attribute mappings** and click the pencil to edit the attributes.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-be84ee0fb4db350b687ddfc7d56c77e527fb08cc%2F6%20(4).png?alt=media" alt="Edit mapping attributes"><figcaption><p>Edit mapping attributes</p></figcaption></figure>
2. Select **+Add** and enter the following attribute, then save the change,\
   **roles**: `Group Names`\\

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-86fb4d7c1ae68c0ecd61b01e11cc82934279286f%2FScreenshot%202023-09-05%20at%2012.02.30%20PM.png?alt=media" alt="Add roles array"><figcaption><p>Add roles array</p></figcaption></figure>
3. In the left menu, select **Identities/Groups** and add the Snyk Groups needed following the syntax explained on the [Cusom Mapping Option](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping) page.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f77c9915cd118185d054dff06c95e9af522fd890%2F12.png?alt=media" alt="Adding an example Group"><figcaption><p>Adding an example Group</p></figcaption></figure>
4. If you so not select a **Population** at the bottom of the previous screen, ensure that you assign the Group to the user(s) who should be part of the role assignment in Snyk. If you select a **Population**, all users in that population will inherit the permissions of the assigned Snyk role.
5. To finalize the process, reach out to your Snyk contact to validate that the SAML payload contains the role array and to enable the custom mapping feature.
