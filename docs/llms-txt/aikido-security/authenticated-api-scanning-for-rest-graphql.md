# Source: https://help.aikido.dev/dast-surface-monitoring/api-scanning/authenticated-api-scanning-for-rest-graphql.md

# Authenticated API Scanning for REST/GraphQL

This guide will walk you through the steps to set up authenticated domain scanning in Aikido, ensuring thorough and secure assessments.

> API Scanning is only available on Pro and Advanced Plans

## Use Cases <a href="#use-cases" id="use-cases"></a>

* Ensure comprehensive security assessments for protected areas of your website.
* Identify vulnerabilities in authenticated sections of your APIs.

## Setting up authentication on a domain <a href="#setting-up-authentication-on-a-domain" id="setting-up-authentication-on-a-domain"></a>

**Step 1:** Go to the [**Domains Overview**](https://app.aikido.dev/settings/domains) and open the action menu for a REST/ GraphQL API domain of your choice by clicking the triple dots. Select **Authenticate Domain.**

![Domain action menu with options to scan, configure, authenticate, or delete a domain.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9ff2baa9d095aebbc8b00e3d581e5320c1bcd0e6%2Fauthenticated-api-scanning-for-rest-graphql_77efc1b9-0cd9-4015-a510-adde377cb2b0.png?alt=media)

**Step 2:** Select your preferred option to authenticate.

![Authentication setup screen with multiple login method options and credential input fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3a84ab63100868c47bba1a4da76b4b5d08301377%2Fauthenticated-api-scanning-for-rest-graphql_65ff7557-66be-45fb-b14a-2f4cf2001ec7.png?alt=media)

> All types of scan credentials are securely stored using PKCS1 encryption

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

### **OAuth Client Credentials**

This option can be used when you want to bypass MFA. Aikido makes a request to the provided login URL which follows the OAuth spec for a Client Credentials flow. This means that we'll make a POST request to the configured login url, with `grant_type` set to `client_credentials` and a basic authorization header containing the client\_id and client\_secret as the username and password respectively.

### **OAuth Password Grant**

Choose this option if your API requires direct user credentials (username and password) using the OAuth Password Grant flow. Aikido sends a POST request to your login URL with `grant_type` set to `password`, including the username and password you provide. Depending on the API, a Client ID and Secret might also be required.

### **Basic Auth**

Select this option if your API uses standard Basic Authentication. Provide your username and password, and Aikido will automatically include the necessary `Authorization: Basic ...` header with every request made to your API.

### Login via AI Agent (beta)

The AI Agent uses an LLM to control a real browser session. It follows the instructions you provide to complete the authentication process, just like a human would. This works well for:

* Form based logins
* Static OTP or one time codes
* Multi step authentication flows
* Custom or non standard login screens

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F1XL5KNWl2eqzZ0KTV57c%2FScreenshot%202026-02-12%20at%2011.38.08.png?alt=media&#x26;token=dcebe43d-7583-45b3-8972-fa9591d001c0" alt="" width="563"><figcaption></figcaption></figure>

Provide clear step by step instructions, including credentials and any required actions. The agent can handle redirects, dynamic pages, and intermediate steps without needing detailed configuration. In most cases, short and simple instructions are enough.
