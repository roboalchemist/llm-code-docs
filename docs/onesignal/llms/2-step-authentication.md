# Source: https://documentation.onesignal.com/docs/en/2-step-authentication.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2-step authentication

> Set up, manage, and recover Two-Factor Authentication (2FA) for your OneSignal account, including recovery codes, transferring to a new device, and regaining access if locked out.

## Overview

Two-step authentication (2FA) adds a layer of security to your OneSignal account by requiring a time-sensitive 6-digit code from an authenticator app each time you log in. If you lose access to your authenticator app, you can use one-time recovery codes to log in and reconfigure 2FA on a new device.

<Warning>
  Set up your authenticator on a **personal device you control long-term** — not a shared or temporary test device. If you lose access to that device and your recovery codes, you will be locked out of your account.
</Warning>

***

## Setup

### Download an authenticator app

Install one of the following authenticator apps on your **personal** mobile device:

* **Google Authenticator** (recommended — supports [cloud backup](https://support.google.com/accounts/answer/1066447)): [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) | [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
* **Microsoft Authenticator**: [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) | [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
* **Authy** (supports multi-device sync): [authy.com](https://authy.com/download/)

<Tip>
  Choose an app that supports **cloud backup or multi-device sync** (like Google Authenticator with cloud backup enabled). This protects you if you lose or replace your phone.
</Tip>

### Enable 2-step authentication

<Steps>
  <Step title="Sign in to your OneSignal account">
    If you are locked out, see [Lost your device or authenticator app?](#lost-your-device-or-authenticator-app).
  </Step>

  <Step title="Go to Account Management">
    Navigate to [Account Management](https://dashboard.onesignal.com/profile) or click **your email drop-down > Manage Account**.

    <Frame caption="Account Management">
      <img src="https://mintcdn.com/onesignal/EfnTRtPfvhvkYbyS/images/dashboard/manage-account.png?fit=max&auto=format&n=EfnTRtPfvhvkYbyS&q=85&s=4d1e2f2ac05585e83126fe4e9715566c" width="3094" height="1834" data-path="images/dashboard/manage-account.png" />
    </Frame>
  </Step>

  <Step title="Enable or reconfigure 2-step authentication">
    Scroll to the **2-Step Authentication** section and click **Enable** (or **Reconfigure** if already set up).

    <Frame caption="Enable 2-Step Authentication">
      <img src="https://mintcdn.com/onesignal/EfnTRtPfvhvkYbyS/images/dashboard/profile-2stepauth.png?fit=max&auto=format&n=EfnTRtPfvhvkYbyS&q=85&s=60530d96ba59614d1c6d44aeb35995bc" width="3000" height="1698" data-path="images/dashboard/profile-2stepauth.png" />
    </Frame>
  </Step>
</Steps>

### Set up your Authenticator App

<Steps>
  <Step title="Scan QR code or enter key manually">
    On the "Enable 2-Step Authentication" setup screen, scan the QR code using your authenticator app or manually enter the **Secret Key**.

    <Frame caption="Reconfigure 2-Step Authentication">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/95e9933-Screenshot_2023-02-28_at_11.07.19.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=49bcc4af161b71f7fad4a4d3bd73cc32" width="1100" height="1236" data-path="images/docs/95e9933-Screenshot_2023-02-28_at_11.07.19.png" />
    </Frame>

    If entering manually, tap **Add Account**, choose "Enter a setup key", and name it something memorable like `OneSignal_[your_email]`.

    <Frame caption="Reconfigure 2-Step Authentication">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/fb03ac0-sample-add-auth-1.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=44cfc6176d9f5029ad2041022eb52961" width="340" height="198" data-path="images/docs/fb03ac0-sample-add-auth-1.png" />
    </Frame>

    <br />

    <Frame caption="Reconfigure 2-Step Authentication">
      <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4ef7cbd-sample-add-auth-2.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=265994ad6c47c6d03a2185ba877c22b4" width="464" height="450" data-path="images/docs/4ef7cbd-sample-add-auth-2.png" />
    </Frame>
  </Step>

  <Step title="Get the 6-digit code">
    The app will now generate a 6-digit code every 30 seconds.
  </Step>

  <Step title="Login with auth code">
    * In OneSignal, enter the current 6-digit code from your auth app.
    * If the code fails, wait 30 seconds and try the next one.
    * If the code still fails, check that you entered the key correctly and try again.
  </Step>
</Steps>

***

## Recovery codes

After successful setup, OneSignal displays **10 one-time recovery codes**. Each code can only be used **once** to log in if you lose access to your authenticator app.

<Warning>
  Recovery codes are shown **only once** during setup. Download or copy them immediately and store them in a secure location like a password manager. If you lose both your authenticator device and your recovery codes, you will need to [contact support](#i-lost-my-recovery-codes-and-my-device) to regain access.
</Warning>

<Frame caption="Download your recovery codes immediately after setup.">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/ef0595c-Screenshot_2023-01-18_at_3.23.31_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=a8bb3e088721eae0277f01c44683fb51" width="579" height="557" data-path="images/docs/ef0595c-Screenshot_2023-01-18_at_3.23.31_PM.png" />
</Frame>

### Log in with a recovery code

If you cannot access your authenticator app, use a recovery code instead:

1. Enter your email and password on the OneSignal login page.
2. On the 2FA verification screen, select the option to use a recovery code.
3. Enter one of your saved recovery codes. Each code works only once. Cross it off your list after use.

<Warning>
  After logging in with a recovery code, **immediately reconfigure 2FA** on a device you currently have. If you keep using recovery codes without reconfiguring, you will run out and be locked out of your account. See [Transfer 2FA to a new device](#transfer-2fa-to-a-new-device).
</Warning>

***

### Lost your device or authenticator app?

If you no longer have the device with your authenticator app, follow the path that matches your situation:

**If you have recovery codes:**

<Steps>
  <Step title="Log in with a recovery code">
    Follow the steps in [Log in with a recovery code](#log-in-with-a-recovery-code).
  </Step>

  <Step title="Transfer 2FA to your current device">
    Immediately reconfigure 2FA on a device you control. See [Transfer 2FA to a new device](#transfer-2fa-to-a-new-device).
  </Step>
</Steps>

**If you lost your recovery codes and your device:**

Email `support@onesignal.com` and **CC a team member who can verify your identity**. If you don't have other team members with access to the OneSignal app, the Support Team will assist with alternative verification.

***

## Transfer 2FA to a new device

If you set up 2FA on a device you no longer have access to (for example, a test device or an old phone), reconfigure it on your current device:

<Steps>
  <Step title="Log in to your OneSignal account">
    Use your authenticator app or a [recovery code](#log-in-with-a-recovery-code) to sign in.
  </Step>

  <Step title="Go to Account Management">
    Navigate to [Account Management](https://dashboard.onesignal.com/profile) or click **your email drop-down > Manage Account**.
  </Step>

  <Step title="Reconfigure 2-step authentication">
    Scroll to the **2-Step Authentication** section and click **Reconfigure**.
  </Step>

  <Step title="Set up your authenticator on your new device">
    Scan the new QR code with the authenticator app on your current device. See [Set up your authenticator app](#set-up-your-authenticator-app) for details.
  </Step>

  <Step title="Save your new recovery codes">
    OneSignal generates a fresh set of 10 recovery codes. The previous codes are invalidated. Save these immediately.
  </Step>
</Steps>

***

## Enforce 2FA for all team members

To enforce 2-step authentication across your organization:

<Steps>
  <Step title="You must be an Organization Admin.">
    See [Team members](./manage-team-members) for details.
  </Step>

  <Step title="Navigate to your Organization.">
    Navigate to [Organizations](https://dashboard.onesignal.com/organization) on the left sidebar and select your organization.
  </Step>

  <Step title="Under Team Members > Security, click Enable.">
    <Frame caption="Organization-wide enforcement of 2FA">
      <img src="https://mintcdn.com/onesignal/nO2bC5lVWj6NEfK6/images/dashboard/enable-2fa-org.png?fit=max&auto=format&n=nO2bC5lVWj6NEfK6&q=85&s=ad5949e79376bc8ae48d7322b38b6a12" width="3000" height="1228" data-path="images/dashboard/enable-2fa-org.png" />
    </Frame>
  </Step>

  <Step title="Select Require 2-Step Authentication for all users, then click Continue.">
    <Frame caption="Require 2-Step Authentication for all users of your apps.">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1b138b3-Screenshot_2023-01-18_at_3.58.37_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=aaed5a436f7f8a3270c1b7f31e7476e9" width="577" height="530" data-path="images/docs/1b138b3-Screenshot_2023-01-18_at_3.58.37_PM.png" />
    </Frame>
  </Step>
</Steps>

<Check>
  Future invitations to the organization or apps will require users to set up 2FA before accessing.

  Anyone that is not using 2FA will be required to set it up upon next login.
</Check>

***

## Disable or reconfigure 2FA

<Warning>
  You may not disable 2FA if your organization requires it. Contact your [Organization Admin](./manage-team-members) or `support@onesignal.com` if needed.
</Warning>

Follow the steps to [Enable 2-step authentication](#enable-2-step-authentication) and if enabled, you will have the option to disable or reconfigure.

***

## FAQ

### I'm locked out of my account — how do I get back in?

If you have recovery codes, use one to [log in](#log-in-with-a-recovery-code), then immediately [transfer 2FA to your current device](#transfer-2fa-to-a-new-device). If you've used all your recovery codes or lost them, email `support@onesignal.com` and **CC a team member who can verify your identity**.

### I lost my recovery codes and my device

Email `support@onesignal.com` and **CC a team member who can verify your identity**. If you don't have other team members with access, the Support Team will assist with alternative verification.

### Why do I keep getting asked for a recovery code every time I log in?

This means your authenticator app is no longer generating valid codes for your OneSignal account — usually because the app was on a device you no longer have. Each recovery code is single-use, so you will eventually run out. To fix this permanently, [transfer 2FA to a device you currently use](#transfer-2fa-to-a-new-device) after logging in.

### Why can't I log in or see "Failed to configure OTP"?

Try:

* Waiting for the next 30-second code cycle
* Disabling browser extensions (AdBlock, CORS)
* Whitelisting `*.onesignal.com`
* Disabling Opera's "Block Trackers"
* Hard refresh
* Trying another browser

Still having issues? Email `support@onesignal.com` and **CC a team member who can verify your identity**.

### I forgot my password

[Reset your password](https://dashboard.onesignal.com/password-reset). Password reset is separate from 2FA — you still need your authenticator app or a recovery code after resetting your password.

### Can I use OAuth with 2FA?

Yes. Follow the same setup flow after logging in via OAuth.

### Which authenticator apps are supported?

Any TOTP-compatible app works, including Google Authenticator, Microsoft Authenticator, Authy, 1Password, and Bitwarden. Choose one that supports cloud backup or multi-device sync to avoid losing access if you switch phones.

### Does OneSignal support Okta?

Yes, there are 2 options:

1. Your Okta admin can add OneSignal as an app using [Secure Web Authentication (SWA)](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_Overview_of_Managing_Apps_and_SSO.htm). See the [OneSignal integration on Okta](https://www.okta.com/integrations/onesignal/) for setup. OneSignal's 2FA is separate from Okta.
2. Talk to our [Sales team](https://www.onesignal.com/contact) to get discuss setting this up based on your plan.

### What do the login method icons mean?

<Frame caption="Login method icon definitions.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/ca2fc2f-icons.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=85d3ebb31ee86122a2acfdc654798ae8" alt="Login method icons" width="1114" height="680" data-path="images/docs/ca2fc2f-icons.png" />
</Frame>

***

Built with [Mintlify](https://mintlify.com).
