# Source: https://planetscale.com/docs/security/multi-factor-authentication.md

# Multi-factor authentication

> Multi-factor authentication (MFA) provides better safety for your databases and prevents unauthorized access to your user account. 

## Overview

MFA strengthens security by requiring two or more methods *(i.e. authentication factors)* to verify your identity.

PlanetScale allows users logging in with an email address and password to set MFA as a requirement for logging into the user account.

<Note>
  If you're authenticating via GitHub OAuth or [SSO](/docs/security/sso), MFA settings will not be displayed.
</Note>

### Authentication providers

PlanetScale supports login with a unique *time-based one-time password (TOTP)* that is generated for your user account by using TOTP apps such as [1Password](https://docs/support.1password.com/one-time-passwords/), [Authy](https://docs/support.authy.com/hc/en-us/articles/360006303934-Add-a-New-Two-Factor-Authentication-2FA-Account-Token-in-the-Authy-App), or [LastPass Authenticator](https://lastpass.com/auth/).

## Enable MFA

You can enable MFA for your user account under your PlanetScale account settings.

<Steps>
  <Step>
    Go to your [PlanetScale account settings](https://app.planetscale.com/account) page.
  </Step>

  <Step>
    Find the **Security** row and click the **"Setup multi-factor authentication"** button.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f4edfa84b8b413a6ad57cbbc2352e442" alt="Click the &#x22;Setup MFA&#x22; button priority" data-og-width="3074" width="3074" data-og-height="282" height="282" data-path="docs/images/assets/docs/concepts/mfa/setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f8dd0dce93d91a0ddc5d5211b23a6b14 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=10d6543b46f9d54594519bd44688caf2 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a4a3a4ae917c5d1ab911d1f860fb4d75 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=464f1d2b2eb4e6edc94ca6babcd57359 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=aaf4e6dc3f1ca854c2648fa430b47747 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/setup.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e03f2f6cc49fad6c807e0cabb8d90df5 2500w" />
    </Frame>

    This will bring up a pop-up modal with a *QR code* and some `recovery codes` that you will need to copy.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7dab6f372e3f6c38543cc73f9ede99ac" alt="Pop-up modal with QR code and recovery codes priority" data-og-width="976" width="976" data-og-height="1522" height="1522" data-path="docs/images/assets/docs/concepts/mfa/recovery-codes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0ba128fe36918b9681b71ea2fcf23717 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=38f8bcf831d613b7c6a081b8f3bf8d5e 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6f6d1a3555c3c60ebfd2ffed6e365d27 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1c93b3f6df89b0cfd4d34109a9ca16f3 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a1742746f6f220a8adb74fc8d1c84b77 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/recovery-codes.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=95e3236dd79a42f9ca74647d50d963fe 2500w" />
    </Frame>

    <Warning>
      Recovery codes are the only account recovery method accepted when MFA is enabled. If you lose both your TOTP app and the recovery codes, there is no way to regain access to your account.
    </Warning>
  </Step>

  <Step>
    Scan the QR Code with your preferred TOTP app and enter the generated code.
  </Step>

  <Step>
    Press **"Validate OTP"** to ensure that your application setup is correct.
  </Step>

  <Step>
    Once the generated code is validated, click the **Copy** button in the `recovery codes` section.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5a66009cff34f2e90b448b9e0e04204f" alt="Copy the recovery codes" data-og-width="1018" width="1018" data-og-height="196" height="196" data-path="docs/images/assets/docs/concepts/mfa/copy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=4ee38296e61784a81d25ad47b8f5b959 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f0d2b813d2a88bdaf19e5efbc3e39cbc 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e4e0b3a945dede504f3217446c90294f 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=4bdea3b0f242a09dbacba99904890ea0 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5678149ae5d243a0f81ec5bbbf84c362 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/copy.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=034d11f659a3aa6e177db1be6e2c1378 2500w" />
    </Frame>

    <Tip>
      Recovery codes are only visible during the MFA setup process. Make sure the recovery codes are copied and saved some place secure before continuing.
    </Tip>
  </Step>

  <Step>
    Click **Done** to close the pop-up modal.
  </Step>
</Steps>

## Login with two-factor authentication

Once you've enabled MFA in your PlanetScale user account, the next time you login, you'll be prompted to enter your two-factor authentication (2FA) code.

* Use the **OTP code** generated by your preferred TOTP app to login to your PlanetScale account.

## Recovery code login

The `recovery codes` shown during MFA setup are **the only way regain access to your account** in the event that you lose the device that generates your authentication codes. PlanetScale will not accept any other method of authentication or identification.

You can use one of the `recovery codes` in the place of a TOTP token on the second screen during login.

## Disable MFA

<Warning>
  We strongly recommend that you do not disable MFA to avoid unauthorized access to your user account.
</Warning>

<Note>
  * Any devices setup with the QR code for your account will no longer be able to produce valid OTP tokens.
  * Any recovery codes that were generated when MFA was enabled will no longer be valid.
</Note>

You can disable MFA for your user account under your PlanetScale account settings.

<Steps>
  <Step>
    Go to your [PlanetScale account settings](https://app.planetscale.com/account) page.
  </Step>

  <Step>
    Click the **Disable** button next to *"Multi-factor authentication enabled"* in the **Security** row.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=579199129da39c54b73b13fb9d24ce3c" alt="Click the &#x22;Disable&#x22; button" data-og-width="2418" width="2418" data-og-height="214" height="214" data-path="docs/images/assets/docs/concepts/mfa/disable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6a71282290304e3da7031f7a1e04d62f 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f91420f8cf1f1562a35a9e5686c399a2 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=10737e36df84611ca58c7fe12c726368 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d15e6b8127d7ec19b16fc546e4f662fa 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=fdd2ede71e1702c85f75658e252f929b 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/disable.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=44bfb00f7531df7e5a13e4b2b4219d9a 2500w" />
    </Frame>
  </Step>

  <Step>
    Enter an **OTP code** or one of the `recovery codes` generated by your preferred TOTP app to confirm.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9e8817684df875bf178afdac4c2b2ffa" alt="Disable MFA pop-up modal" data-og-width="980" width="980" data-og-height="814" height="814" data-path="docs/images/assets/docs/concepts/mfa/modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=047a79f38de3d486bf361d231b9e0a5d 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d51085b118ee67036de16e3bb24774c2 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d827299f586334ecfc7a66cbebc11b1d 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c8b6072cd204b741ddb695cf54aa3d1e 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a3c885718acc44a8854a1bd772f72b38 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/mfa/modal.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=b12f0f625a8a5167374bb2e45685f485 2500w" />
    </Frame>
  </Step>

  <Step>
    Click the **Disable** button to close the pop-up modal.
  </Step>
</Steps>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt