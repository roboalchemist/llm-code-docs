# Source: https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/custom-mapping/examples-setting-up-custom-mapping-for-idps/example-setting-up-custom-mapping-for-entra-id.md

# Example: setting up custom mapping for Entra ID

The following information shows how to configure the custom mapping of roles for Entra ID (formerly Azure AD).

{% hint style="info" %}
See the [Entra ID Enterprise Application example](https://docs.snyk.io/implementation-and-setup/enterprise-setup/single-sign-on-sso-for-authentication-to-snyk/configure-self-serve-single-sign-on-sso/azure-ad-enterprise-application-setup) for guidance setting up the initial Enterprise application.

Any step on the Snyk side in setting up the Enterprise application must be performed by your Snyk contact, as self-serve SSO does not accommodate custom mapping.
{% endhint %}

The following are the prerequisites for configuring app roles:

* Snyk support must configure your Snyk SSO as Microsoft Entra ID (WAAD or SAML).
* If you select SAML, there is a requirement to add a custom claim; the step to do that is in these instructions.
* You must have an existing Azure Enterprise application and app registration connected to that SSO configuration.

The **steps** in **configuring App role**s follow.

1. In your App registration menu, select the name of your Enterprise Application.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-58d29e9cf6505cb1792fea1712d4416235935180%2Fimage%20(113).png?alt=media&#x26;token=6f9c572d-7fff-4d1c-ae47-3a987af3bc46" alt="App registration, select name of Enterprise Application"><figcaption><p>App registration, select name of Enterprise Application</p></figcaption></figure>
2. Select **App roles**, then **Create app role**.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ba6014b19f4a4c5065134672b52a797e426f70f5%2Fimage%20(1)%20(1)%20(2)%20(1).png?alt=media&#x26;token=e760628f-f775-44a5-a691-4e6a9cab8cfa" alt="Select App roles, Create app role"><figcaption><p>Select App roles, Create app role</p></figcaption></figure>
3. Create an app role with details as needed.\
   Select the **Allowed member types**: **Users/Groups**, **Applications**, or **Both**.\
   Enter the **Value** and **Description** for the selected type.\
   Enable the app role.\
   When you are finished, select **Apply**.\\

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8701f4ad9130eb9e6524431d0f8406f191de69e3%2Fimage%20(157).png?alt=media" alt="Create app role" width="285"><figcaption><p>Create app role</p></figcaption></figure>
4. In Entra ID, select your Enterprise Application.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f95267ced8f58c529797d0c72d6989b2be78af37%2Fimage%20(3)%20(3).png?alt=media&#x26;token=cfd2e6a2-e7b3-46be-a8f9-8cb6879a6b42" alt="Select Enterprise Application in Entra ID"><figcaption><p>Select Enterprise Application in Entra ID</p></figcaption></figure>
5. Select **Users and groups**; then **Add user/group**.\
   Search and select the users and groups to add.

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-71f838bfbb742334b9590c1084d317f63e1ac4a5%2Fimage%20(4).png?alt=media" alt="Select Users and groups, Add user/group"><figcaption><p>Select Users and groups, Add user/group</p></figcaption></figure>
6. Select **Users and groups**; from the dropdown, select a role and select **Assign**.\\

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5d78d13098c556c001f0f438561e81b6a3e4d639%2Fimage%20(158).png?alt=media" alt="Add assignment"><figcaption><p>Add assignment</p></figcaption></figure>
7. Repeat for all required groups and roles that should be assigned. Then verify that the list looks similar to this.\\

   Note that it is also possible to add multiple Snyk roles to one App role, as the payload can be interpreted as a comma-separated string. However, this can not be used in conjunction with multiple App roles, as only one syntax will be respected (string or array).

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fb557288eae538178f991661a6eaa581a9bbc2f0%2Fimage%20(159).png?alt=media" alt="Users and group list"><figcaption><p>Users and group list</p></figcaption></figure>
8. If you have configured a SAML connection, add a custom claim to pass the roles array in the SAML payload to Snyk. Select **Single sign-on** in the left-hand menu.
9. Select **Edit** next to **Attributes and Claims.**

   <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6faa2fc144d09685fa4570213516f630ad09ad14%2FScreenshot%202023-03-10%20at%203.19.31%20PM.png?alt=media" alt="Edit attributes and claims"><figcaption><p>Edit attributes and claims</p></figcaption></figure>
10. Select **Add new claim** add the following details, and **Save.**\
    **Name**: roles\
    **Source**: Attribute\
    **Source attribute**: user.assignedroles

{% hint style="warning" %}
Ensure you add the claim correctly. If you do not add it or you do it incorrectly, for example, by adding a typo, it can lead to a full mapping failure, which can lock users out of their accounts.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6b137e9ada079d1d40386fa66514c214480a59cb%2FScreenshot%202023-03-10%20at%202.55.05%20PM.png?alt=media" alt="Custom claim"><figcaption><p>Custom claim</p></figcaption></figure>

When you have completed these steps, reach out to your Snyk point of contact to have the configuration completed.
