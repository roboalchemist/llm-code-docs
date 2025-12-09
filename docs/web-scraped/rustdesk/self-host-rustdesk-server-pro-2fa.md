# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-pro/2fa/

# 2FA

When logging in to your account, turning on Two-Factor Authentication (2FA) verification can improve account security.

Our web console currently supports two kinds of 2FA:

- Email verification
- TOTP. A third-party authentication app is required to generate the verification code, such as Authy, Microsoft Authenticator and [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) authentication app.

You first need to go to the account settings page.

## Email verification

To enable email verification for login, you need:

- Set email.
- Enable the `Enable email login verification` option.
- Click on `Submit`.

When we log in next time, RustDesk will send us a verification code email, and the web page will also jump to the verification page.

## TOTP

TOTP is a widely used 2FA method, so in the web console of RustDesk Server Pro, 2FA refers to TOTP verification.

### Prepare authentication app

First, you need to prepare an authentication app.
You can choose from these types Authy, Microsoft Authenticator and [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) authentication app.

### Enable 2FA

When the `Enable 2FA` button is displayed on the settings page, it means that 2FA is not currently enabled.

Click the button and a form will pop up to enable 2FA.

Open the authenticator app, add an account by scanning the QR code.

If you are inconvenient to scan the QR code, you can also enter the code here directly.

After adding the account in the authenticator app, enter the verification code in the authenticator app to turn on 2FA.

After 2FA is successfully turned on, RustDesk Server Pro will also be bound to 6 **backup codes**. So that you can use these **backup codes** to pass the verification even if you are unable to use the authenticator app.

Note

- 
These backup codes can only be used once.

- 
Please keep the backup codes in a safe place.

### Login verification

When 2FA is enabled, email login verification is no longer used. We will be using 2FA login verification instead.

When logging in, you will be redirected to the verification page.

### Modify settings

When 2FA is enabled, modifying account settings requires additional 2FA verification.

### 2FA state

2FA has a total of 3 states: not enabled, enabled and expired.

Note

2FA can still be used normally after it expires. It just means that the 2FA settings haven&rsquo;t been changed for a long time (default 180 days). For security reasons, we recommend re-enabling 2FA, so the secret data can been updated.