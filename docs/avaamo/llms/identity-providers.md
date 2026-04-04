# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/identity-providers.md

# Active Directory (AD) integrations - Identity provider

The Avaamo platform supports the Single Sign On (SSO) feature integration with SAML. It allows the users to log in with only one set of login credentials and makes it easier for users to use several different programs without having to type in several different usernames and passwords.

Security Assertion Markup Language (SAML) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider.

The users can integrate the SSO with SAML support on the Avaamo UI (SP) with Microsoft Azure, G Suite, and Okta (IdP).

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmES0IyGSuUSyFXtikoyM%2FScreenshot%202022-06-15%20at%201.44.38%20PM.png?alt=media\&token=c73c70f8-5ece-4af8-9953-0490e2b6d1af)

### Add Identity Service Provider

The user can add a new Identity Service Provider by clicking on Add New. Avaamo platform supports Microsoft Azure, Okta, and G Suite.

**Microsoft Azure** - With SAML single sign-on, Azure AD authenticates to the application by using the user's Azure AD account. Azure AD communicates the sign-on information to the application through a connection protocol.

**Okta** - To support SAML-based Single Sign-On from Okta set up an application in Okta with the details of your application (the new SAML Service Provider or “SAML SP”).

**G Suite** - The SAML-based Federated SSO article describes the SAML instance where Google is the identity provider (IdP). This group of articles describes the SAML instance where Google is the service provider (SP) and uses 3rd party identity providers.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4xfDryALvN1GALbvzK%2F-M4xj6xDhPoJquxZJnXI%2Fhowto-identity-provider.png?alt=media\&token=e7e0fd63-f700-4ad0-8649-e910ee2cb9da)

On the **Add New** popup window:

1. Enter the **Identity Provider Name** (IdP). A unique identity provider name for your identification. This name will be displayed in the drop-down list when you are selecting an identity provider for your dashboard users while either creating a new user or editing an existing one. For example, Microsoft Azure, G-Suite, Okta, etc.
2. Enter the **App ID/ Entity ID**, this is the application configured on the Identity Service Provider.
3. Enter the **Single Sign-On URL**.
4. Enter the **Certificate Signature**, this is downloaded once the application is created. So, browse your local disk and upload the certificate.
5. Click **Sign request**, if you wish to send the Avaamo certificate and key in the SAML request.&#x20;
6. Click on **Submit.**

You can edit the Identity Provider settings and also, delete an Identity Provider.
