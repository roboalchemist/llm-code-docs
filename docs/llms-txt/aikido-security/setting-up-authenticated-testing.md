# Source: https://help.aikido.dev/pentests/setting-up-authenticated-testing.md

# Setting Up Test Users

Most critical vulnerabilities—IDORs, privilege escalations, logic bugs—live behind your login screen. To find them, Aikido’s Pentest agents needs access.

Unlike legacy tools that require complex Selenium scripts or proxy recordings, Aikido uses an LLM-driven approach. You simply tell the agent how to log in using natural language, just like you would explain it to a human QA tester.

Here is how to configure your authentication sets.

{% stepper %}
{% step %}

### Create a Test User

1. Click **Add Test User**.
2. **Name:** Give this set a descriptive name (e.g., `Admin User`, `Read-Only User`, `Tenant A - Manager`).

{% hint style="info" %}
We recommend setting up multiple personas to test for Broken Access Control (BAC) between different privilege levels.
{% endhint %}

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FCvgGWNKcqHoCEAm4Gznd%2FScreenshot%202025-12-11%20at%2011.33.44.png?alt=media&#x26;token=010f7c6d-7081-40b8-ab48-15118ba29448" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Provide Login Instructions

This is the most important step. In the **Authentication instructions** field, provide a step-by-step text description of your login flow.

The AI agent parses this to navigate your specific UI quirks. Be explicit.

**Example format:**

> Navigate to `staging.app.com/login`
>
> Click on "Log in with Username"
>
> Enter username: `pentest_admin`
>
> Enter password: `super_secure_password_123`
>
> Click the "Sign In" button

{% hint style="info" %}
The AI agent is equipped to solve standard Captchas automatically. You do not need to disable these for the scan or provide specific instructions for them.
{% endhint %}

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FQYR8KRbSfUZx3MCnnmyL%2FScreenshot%202025-12-11%20at%2011.35.23.png?alt=media&#x26;token=0c7727ee-df1d-4dd0-9038-5d807d408ed9" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}

### Test the Configuration

Finally, verify that the agent can interpret your instructions:

1. Click **Save & Test**.
2. The agent will launch a browser session and attempt to log in using the credentials and inbox instructions.
3. If successful, you will see a confirmation that the agent authenticated and reached the post-login state.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FfFaS7MOW8jQV8kuQzfXF%2Fimage.png?alt=media&#x26;token=f4b7ca13-a024-4f47-8148-d6965902f685" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Advanced Login Flows

If your application requires more than a simple username and password, use our specialized tools:

* [**Email Verification & Magic Links:**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-email-verification-and-magic-links) If you need to click a link in an email or receive a code.
* [**Two-Factor Authentication (TOTP):**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-two-factor-authentication-totp) If you need to generate 6-digit codes from an authenticator app.
* [**SMS Verification:**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/handling-sms-verification) If you need to handle SMS-based verification codes.

Vendor-Specific Authentication Flows:

* [**Google Auth:**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/google-auth) Native support for Google Workspace login flows is available in beta.
* [**Microsoft Auth:**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/oauth0-configuration) Support for Microsoft accounts with two-step verification.
* [**Auth0 Configuration:**](https://help.aikido.dev/pentests/setting-up-authenticated-testing/oauth0-configuration) Oauth provider settings required to support session sharing between multiple agents.

### Best Practices

* **Don’t use Production Credentials:** Always run pentests on a Staging or QA environment. The scanner performs intrusive tests that can corrupt data.
* **Create Dedicated Test Accounts:** Do not use personal developer accounts. Create specific accounts for the scanner (e.g., `aikido-scanner@yourdomain.com`).
* **Cover All Tenants:** If your app is multi-tenant, add credentials for users in different tenants (e.g., `User - Tenant A`, `User - Tenant B`). This allows the AI to test for cross-tenant data leakage.

### Troubleshooting

Authentication is verified during the **preflight check** immediately after launch. You can watch the agent's screen in real-time to see if it succeeds.

If the agent fails to log in:

* **Inspect the failure:** Check the agent's screenshots in the error log to see exactly where it got stuck.
* **Sanity check steps:** Walk through your provided instructions manually in an incognito window. If you skipped a step or a button is unclear, the agent might struggle.
* **Check accessibility:** Is the URL reachable from the public internet? (Check your IP whitelisting).
* **Account status:** Ensure the test user hasn't been locked out.
