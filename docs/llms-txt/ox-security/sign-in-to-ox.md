# Source: https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox.md

# Sign in to OX

Use this article to choose the sign-in method for your organization. OX Security supports the following sign-in methods:

* **Social/third-party sign-in using** [Google or GitHub](#allow-sign-in-with-google-or-github): Provides a strong layer of security by delegating password management via the OAuth/OpenID Connect protocol. Your application never stores the password. However, admins need to assign roles and scopes to users manually.
* [Username and password](#allow-sign-in-with-username-and-password): Gives your organization complete control but imposes the highest administrative and security burden. The organization must secure and manage all user credentials and strictly enforce complex password standards. As with Google / GitHub, admins need to assign roles and scopes to users manually.
* [Single Sign-On (SSO)](#allow-sign-in-using-single-sign-on-sso): Provides the highest level of security by centralizing credential management and policy enforcement (like Multi-Factor Authentication) through a dedicated Identity Provider (IdP). The initial setup is complex and requires time and specialized knowledge of IdP applications and protocols (SAML/OIDC). SSO provides the option for auto-provisioning, which the other methods do not.

### Prerequisites

You need OX admin permissions.

### Allow sign-in with Google or GitHub

Use this option when you want users to sign in to OX using existing Google or GitHub accounts.

OX uses OAuth to authenticate with Google and GitHub. These providers do not return role or scope data. You assign each user’s role and scope in OX after the user signs in for the first time.

**To allow sign-in with Google or GitHub:**

1. Go to **Settings > Login**.
2. Select **Google** or **GitHub**.
3. Confirm that the sign-in toggle is enabled.
4. After a user signs in, assign their role and scope. For instructions, see the article **Users**.

### Allow sign-in with username and password

Use this option when you want users to authenticate directly with OX.

Users set a password when they activate their account from the invitation email.\
You assign each user’s role and scope in OX after the user signs in for the first time.

**To allow sign-in with username and password:**

1. Invite the user from the Users page. OX sends the invitation email.
2. The user activates the account and sets a password.
3. After a user signs in, assign their role and scope. For instructions, see the article **Users**.

### Allow sign-in using Single Sign-On (SSO)

Use this option when your organization uses an identity provider (IdP) to manage authentication.

SSO uses your IdP to verify users with corporate credentials.\
You can map IdP groups to OX roles and scopes to reduce manual work, or you can configure manually.

**To set up SSO, follow the instructions in the relevant article:**

* [SSO with Entra ID](https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/logging-into-microsoft-entra-id)
* [SSO with Okta](https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/logging-into-okta)
* [SSO with OpenID Connect](https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/sso-with-openid-connect)
* [SSO with PingIdentity](https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/sso-with-saml-1)
* [SSO with SAML](https://docs.ox.security/get-started/onboarding-to-ox/connect-to-ox/sign-in-to-ox/sso-with-saml)
