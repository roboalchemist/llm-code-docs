# Source: https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-email-verification-and-magic-links.md

# Handling Email Verification & Magic Links

Aikido provides a hosted email inbox to allow the AI Pentest agent to navigate authentication flows that require email interaction.

**Use this feature if your application requires:**

* **Magic Links:** Passwordless login via email links.
* **Email MFA:** Two-factor authentication where a code is sent to the inbox.
* **Account Verification:** New users must verify their email before logging in.

{% hint style="info" %}
If your app uses authenticator apps, use [TOTP setup](https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-two-factor-authentication-totp).

If your app uses SMS codes, use [SMS Verification](https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-sms-verification).
{% endhint %}

### How it works

You generate a unique `@auto-pentest.com` email address within Aikido. This address acts as a bridge:

1. **You** use it to create and verify a valid user account in your application.
2. **The Agent** monitors this inbox during scans to retrieve login codes or click magic links in real-time.

### Setup Guide

{% stepper %}
{% step %}

#### Let Aikido create the Email Address

In the **Authentication Set** modal:

1. Scroll to the **Email Inbox** section.
2. Click `+ Generate Email Address`.
3. Copy the address (e.g., `random-name@auto-pentest.com`).

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F60upjjBdkltJrNefKbjc%2FScreenshot%202025-12-10%20at%2018.26.57.png?alt=media&#x26;token=f46942f5-8d8f-4704-8409-75df64dc034d" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

#### Create the Test User in your application

Go to your application and sign up a new user using the address you just created.
{% endstep %}

{% step %}

#### Verify the Account (if required)

If your app sends a "Confirm your email" link upon signup:

1. Return to the Aikido modal.
2. Click the **Open Inbox** icon (or click the email address itself).
3. You will see the confirmation email from your app.
4. Open it and click the confirmation link/button to activate the user.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIViyHx1Bzi8Nvf0xmeLn%2FScreenshot%202025-12-10%20at%2018.10.23.png?alt=media&#x26;token=70645182-ec4c-472a-b8d2-768956210b35" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

#### Update Login Logic in Aikido

You must explicitly tell the agent to check this inbox in the **Login Logic** text area.

**Example Instruction for Magic Links:**

```
1. Navigate to https://app.example.com/login
2. Enter email: [insert the created email here]
3. Click "Send Magic Link"
4. Check the inbox for the login email and click the link inside.
```

**Example Instruction for Email MFA:**

```
1. Navigate to https://app.example.com/login
2. Enter username and password.
3. When prompted for the code, check the inbox.
4. Extract the 6-digit code from the latest email.
5. Enter the code into the verification field and submit.
```

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1HuywSOFaWkoSxVDf9Qr%2FScreenshot%202025-12-10%20at%2018.31.49.png?alt=media&#x26;token=32d194c9-25d9-4d5d-844a-c2e8553702b0" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Test the Configuration

Finally, verify that the agent can interpret your instructions:

1. Click **Save & Test**.
2. The agent will launch a browser session and attempt to log in using the credentials and inbox instructions.
3. If successful, you will see a confirmation that the agent authenticated and reached the post-login state.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGKojiQXYxcXclTd6Sykx%2FScreenshot%202025-12-10%20at%2018.36.04.png?alt=media&#x26;token=4eea247a-4084-474d-9e25-5e5bd1858de3" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}
