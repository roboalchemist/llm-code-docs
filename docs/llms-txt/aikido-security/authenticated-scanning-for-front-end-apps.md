# Source: https://help.aikido.dev/dast-surface-monitoring/front-end-scanning/authenticated-scanning-for-front-end-apps.md

# Authenticated Scanning for Front-End Apps

This guide will walk you through the steps to set up authenticated domain scanning in Aikido, ensuring thorough and secure assessments.

> This feature is not available on **Free** Plans.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* Ensure comprehensive security assessments for protected areas of your website.
* Identify vulnerabilities in authenticated sections of your domain.

### Setting up authentication on a domain <a href="#setting-up-authentication-on-a-domain" id="setting-up-authentication-on-a-domain"></a>

**Step 1:** Go to the [Domains Overview](https://app.aikido.dev/settings/domains) and open the action menu for a domain of your choice by clicking the triple dots. Select **Authenticate Domain.**

![Domain action menu with options to scan, configure, authenticate, or delete a domain.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9ff2baa9d095aebbc8b00e3d581e5320c1bcd0e6%2Fauthenticated-scanning-for-front-end-apps_73e3a4bd-4171-4010-a569-83aadd2f0994.png?alt=media)

**Step 2:** Fill in the URL and email/password for the domain authentication. Click **Test** to let Aikido check whether it can access the domain with those credentials.

![Form-based authentication setup for domain with login credentials and confirmation options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-782f1f590fa33a5bb7b56b55b0f2bea870ba2191%2Fauthenticated-scanning-for-front-end-apps_cef8d27b-529c-4fab-829d-a2df670c99ba.png?alt=media)

**Step 3.** Once the test has been succeeded, you can **Confirm Authentication.** Aikido will do a thorough scan and all results will appear in Aikido.

> Scan credentials are securely stored using PKCS1 encryption

## Authentication Options <a href="#authentication-options" id="authentication-options"></a>

### **Login via Form**

Fill in the URL and email/password for the domain authentication. Click **Test** to let Aikido check whether it can access the domain with those credentials.

You can also enter the one time password information if two factor authentication is enabled. For [more information about the OTP URL and how it works, see the documentation](https://help.aikido.dev/dast-surface-monitoring/using-2fa-in-front-end-and-api-scans).

{% hint style="success" %}

* Microsoft / Google SSO is currently **not** supported. As a workaround, you can manually authenticate and pass a valid session using the Cookie header via custom headers.
* Is your case not supported? Let us know via the chat and we will look into it!
  {% endhint %}

![Domain authentication setup screen for form-based login credentials configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FXdd1QcwDQOlanD6JOlJo%2FScreenshot%202026-01-09%20at%2014.16.32.png?alt=media\&token=161c5608-0dfa-485c-8306-1ba24e1ba6cd)

Aikido will attempt to submit the form using the following rules:

1. Find a visible button or input field with `type=submit` while ignoring popular OAuth options like Google and Facebook
2. Find button based on the label or text. Looks for text equal or similar to: login, log in, submit, sign in, .. It does so in multiple languages.
3. Find button based on set of HTML ID's, for example `id=form-submit`
4. Find first visible button on page

### Custom Headers&#x20;

If your endpoints accepts a fixed key, cookie or token which should not change after creation, you can add it as a custom header via this option.&#x20;

Use-cases:

* Cookies: Set the `Cookie` header.&#x20;

  ```
  Cookie: sessionId=38afes7a8
  ```

* JWT Bearer token: Set the `Authorization` header

  ```
  Authorization: Bearer <token>
  ```

### Login via AI Agent (beta)

The AI Agent uses an LLM to control a real browser session. It follows the instructions you provide to complete the authentication process, just like a human would. This works well for:

* Form based logins
* Static OTP or one time codes
* Multi step authentication flows
* Custom or non standard login screens

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1XL5KNWl2eqzZ0KTV57c%2FScreenshot%202026-02-12%20at%2011.38.08.png?alt=media&#x26;token=dcebe43d-7583-45b3-8972-fa9591d001c0" alt="" width="563"><figcaption></figcaption></figure>

Provide clear step by step instructions, including credentials and any required actions. The agent can handle redirects, dynamic pages, and intermediate steps without needing detailed configuration. In most cases, short and simple instructions are enough.

### Troubleshooting Authentication Issues <a href="#identifiers" id="identifiers"></a>

#### Login via form

Aikido scanner will use a fixed set identifiers to determine the username and password fields. Check that your input fields `id` or `name` parameters have one of the following values for the email or username field.

```javascript
"email", "username", "Username", "login-email", "EmailOrUsername", 
"UserNameOrEmail", "username_login", "txtUsername", "user_email", "email-input'
```

Password field are found by looking for input fields with password type.

```
input[type="password"]
```

Submit buttons are found by looking for buttons or input fields with type submit.

```
button[type="submit"]
input[type="submit"]
```

If you still encounter problems, please don't hesitate to reach out to support.&#x20;
