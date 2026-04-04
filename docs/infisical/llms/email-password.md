# Source: https://infisical.com/docs/documentation/platform/auth-methods/email-password.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email and Password

> Learn how to authenticate into Infisical with email and password.

**Email and Password** is the most common authentication method that can be used by user identities for authentication into Web Dashboard and Infisical CLI. It is recommended to utilize [Multi-factor Authentication](/documentation/platform/mfa) in addition to it.

It is currently possible to use the **Email and Password** auth method to authenticate into the Web Dashboard and Infisical CLI.

### Emergency Kit

Every **Email and Password** is accompanied by an emergency kit given to users during signup. If the password is lost or forgotten, emergency kit is only way to retrieve the access to your account. It is possible to generate a new emergency kit with the following steps:

1. Open the `Personal Settings` menu.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/access-personal-settings.png" alt="open personal settings" />
2. Scroll down to the `Emergency Kit` section.
3. Enter your current password and click `Save`.

### Change Password

You can update your account password at any time:

1. Open the `Personal Settings` menu.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/access-personal-settings.png" alt="open personal settings" />
2. Navigate to the `Authentication` tab.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/personal-settings-authentication-tab.png" alt="open authentication tab" />
3. In the `Change Password` section, enter your current password and new password.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/personal-settings-authentication-change-email-password.png" alt="change password section" />
4. Click `Save` to save your new password.

### Change Email

You can update your account email address:

1. Open the `Personal Settings` menu.
2. Navigate to the `Authentication` tab.
3. In the `Change Email` section, enter your new email address.

<Info>
  If you don't currently have Email authentication enabled, it will be automatically activated when you change your email. You may disable it in the authentication settings after logging in with your new email if needed.
</Info>

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/personal-settings-authentication-change-email-password.png" alt="change email section" />
4\. Click `Send Verification Code` to receive an 6-digit verification code at your new email address.
5\. Check your new email inbox and enter the verification code.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/auth-methods/personal-settings-authentication-change-email-confirmation.png" alt="change email section" />
6\. Click `Confirm Email Change` to complete the process.
7\. You will be logged out and need to sign in again with your new email address.

<Tip>
  Changing your email will remove all connected external authentication methods and terminate all active sessions for security.
</Tip>

<Warning>
  Email changes are disabled if SCIM is enabled for any of your organizations. Contact your organization administrator if you need to change your email address in a SCIM-enabled environment.
</Warning>
