# Source: https://docs.klarna.com/resources/developer-tools/testing-conversion-boosters/testing-and-integration-checklist-for-sign-in-with-klarna.md

# Testing and integration checklist for Sign in with Klarna

## Before you go live with Sign in with Klarna solution, follow this checklist to make sure your integration is tested and ready to be enabled in production.

## Testing Sign in with Klarna

In order to test against the playground environment, please use the following base url: [<https: login.playground.klarna.com="">](https://login.playground.klarna.com/).

### Testing consent flow

You can trigger the consent screen in various ways depending on the environment and integration type.

#### Production

- Open Klarna app and go to Profile -\&gt; Security and privacy -\&gt; Data sharing and revoke consent.

#### Playground

- If you're using the Klarna Web SDK, add the following query parameter to the URL where the "Sign in with Klarna" button is loaded: `klarna-auth-prompt=consent`.
- For those using the Identity platform or integrating directly with the API, the simplest approach is to create a new Klarna user account by using a different phone number or email address during login.

## Integration checklist

### General

- <span>Verify that SIWK button appears in the right places, for example login component or the myaccount page.</span>
- <span>Verify that the button is clickable and is not covered by any other elements or not blocked by cookie prompts or other toggles.</span>
- <span>Verify that the button is accessible, e.g. can be clicked with keyboard-only setup.</span>
- <span>Verify that the flow is accessible to users with disabilities, following WCAG standards.</span>
- <span>Verify that clicking on the button starts the flow without delay.</span>
- <span>Verify that the redirect uri is provided to the script.</span>
- <span>Verify that redirect flow starts if popups are blocked in the browser.</span>
- <span>Verify that popup flow starts if you do not support redirect flow.</span>
- <span>Verify that the SIWK flow appears in a correct language.</span>
- <span>Verify that in case of an error, error messages are displayed clearly and accurately throughout the flow, providing actionable information to the user.</span>

### Login

- <span>(In Sweden and Norway) Verify that the Bank ID step does not have any errors and on mobile you get redirected back the the app after using Bank ID app. Both scanning of the QR code and confirming in the Bank ID app on the same device should work.</span>
- <span>Verify that if you did not have an account with Klarna associated with provided phone number, or your account was incomplete, you see onboarding screens - email and billing address collection.</span>

### Consent

- <span>Verify that if you are a new user you see the consent screen at the end of the flow.</span>
- <span>Verify all data points on the consent screen. You should only request what you require to create an account.</span>
- <span>Verify that Privacy policy and Terms and conditions links are going to the correct pages.</span>

### After login and consent

- <span>Verify that if you already have an account in your app with the identifier from the Klarna account you used to login, accounts are either merged automatically or you saw a screen informing about the merge. Verify that after logging in either popup closes or you get redirected back to the app and you are in a logged in state in the app.</span>
- <span>Verify that when using SIWK to register a new account, after flow finishes you are also back in the app in a logged in state. You should not be required to use SIWK again to login.</span>
- <span>Verify that the new app’s account contain the same data as your Klarna account.</span>

### Returning users

- <span>Verify that if you logged in to Klarna on a device through any of the products (Klarna App, Klarna Payments) you do not see the login screen in the Sign in with Klarna flow.</span>
- <span>Verify that as a returning user you do not see the consent screen in the flow.</span>
- <span>Verify that after revoking consent through Klarna App and logging out from your app, next time you sign in with Klarna you see the consent screen.</span>

### Purchase

- <span>If you have Klarna integrated in your checkout, it is imperative to verify that if you logged in with Sign in with Klarna you are automatically logged in in the Klarna purchase flow.</span></https:>