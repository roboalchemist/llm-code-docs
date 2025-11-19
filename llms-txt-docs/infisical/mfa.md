# Source: https://infisical.com/docs/documentation/platform/mfa.md

# Multi-factor Authentication

> Learn how to secure your Infisical account with MFA.

MFA requires users to provide multiple forms of identification to access their account.

## Email 2FA

If 2-factor authentication is enabled in the Personal settings page, email will be used for MFA by default.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/mfa-email.png" alt="Email-based MFA" />

## Mobile Authenticator 2FA

You can use any mobile authenticator app (Authy, Google Authenticator, Duo, etc.) to secure your account. After registration with an authenticator, select **Mobile Authenticator** as your 2FA method.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/mfa-authenticator.png" alt="Authenticator-based MFA" />

## Entra ID / Azure AD MFA

<Note>
  Before proceeding make sure you've enabled [SAML SSO for Entra ID / Azure AD](./sso/azure).

  We also encourage you to have your team download and setup the
  [Microsoft Authenticator App](https://www.microsoft.com/en-us/security/mobile-authenticator-app) prior to enabling MFA.
</Note>

<Steps>
  <Step title="Open your Infisical Application in the Microsoft Entra Admin Center">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_infisical_app.png"
          alt="Entra Infisical
    app"
        />
  </Step>

  <Step title="Tap on Conditional Access under the Security Tab">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_conditional_access.png"
          alt="conditional
    access"
        />
  </Step>

  <Step title="Tap on Create New Policy from Templates">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_create_policy.png" alt="create policy" />
  </Step>

  <Step title="Select Require MFA for All Users and Tap on Review + Create">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_review_policy.png"
          alt="require MFA and review
    policy"
        />

    <Note>
      By default all users except the configuring admin will be setup to require
      MFA. Microsoft encourages keeping at least one admin excluded from MFA to
      prevent accidental lockout.
    </Note>
  </Step>

  <Step title="Set Policy State to Enabled and Tap on Create">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_confirm_policy.png"
          alt="enable policy and
    confirm"
        />
  </Step>

  <Step title="MFA is now Required When Accessing Infisical">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/mfa/entra/mfa_entra_login.png" alt="mfa login" />

    <Note>
      If users have not setup MFA for Entra / Azure they will be prompted to do
      so at this time.
    </Note>
  </Step>
</Steps>
