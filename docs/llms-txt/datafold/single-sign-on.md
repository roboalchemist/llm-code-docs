# Source: https://docs.datafold.com/security/single-sign-on.md

# Single Sign-On

> Set up Single Sign-On with one of the following options.

<CardGroup>
  <Card title="Okta (OIDC)" href="/security/single-sign-on/okta" icon="file" horizontal />

  <Card title="Google OAuth" href="/security/single-sign-on/google-oauth" icon="file" horizontal />

  <Card title="SAML" href="/security/single-sign-on/saml/" icon="folder-open" horizontal />
</CardGroup>

<Tip>
  **Tip**

  You can force all users to use the configured SSO provider by unchecking the *Allow non-admin users to login with email and password* checkbox under the organization settings.

  Admin users will still be able to login using email and password.

  <Frame>
    <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=29f90cc886243d77cd3ceac6fa825ad7" data-og-width="843" width="843" data-og-height="399" height="399" data-path="images/disable_non_admin_email_password_login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=795d023925dfc27b455e5478c8488b92 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bd259b872d305adce12884d34822ef76 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9fbff485e2d7b6c18b909f7e8f4a0bcc 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2e8feed2012315c85c5b6fa6503c1107 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2d479a6c5825d4695a12fa25cc6ac1ef 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/disable_non_admin_email_password_login.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9976e83d3bb4e81221150dc1e6c24618 2500w" />
  </Frame>
</Tip>

<Warning>
  **Caution**

  Ensure only authorized users keep using Datafold by setting up Okta webhooks or setting up credentials for the Microsoft Entra app if you're using Microsoft Entra ID (formerly known Azure Active Directory)

  This will disable non-admin users that don't have access to the configured SSO app.

  [Configure this for Okta](/security/single-sign-on/okta#synchronize-state-with-datafold-optional)

  [Configure this for Microsoft Entra ID](/security/single-sign-on/saml/examples/microsoft-entra-id-configuration#synchronize-user-with-datafold-optional)
</Warning>
