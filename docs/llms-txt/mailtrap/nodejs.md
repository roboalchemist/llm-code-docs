# Source: https://docs.mailtrap.io/guides/sdk/nodejs.md

# Node.js

<a href="https://github.com/mailtrap/mailtrap-nodejs" class="button primary">Mailtrap Node.js SDK on GitHub</a>

### Overview

Mailtrap can be integrated with Node.js apps for email sending purposes with SDK, SMTP, and RESTful API.

### Email API/SMTP for Node.js

#### SDK integration

The [Mailtrap Node.js SDK](https://github.com/mailtrap/mailtrap-nodejs) provides a simple and intuitive way to send transactional and bulk emails from your Node.js applications. The SDK supports:

* Transactional email sending
* [Nodemailer](https://github.com/mailtrap/mailtrap-nodejs?tab=readme-ov-file#nodemailer-transport)
* Batch email sending
* Template management
* Contact management
* Sandbox testing
* Account management

### Installation

Install the SDK using npm or yarn:

{% code title="npm" %}

```bash
npm install mailtrap
```

{% endcode %}

{% code title="yarn" %}

```bash
yarn add mailtrap
```

{% endcode %}

### Minimal Example

Here's a minimal example to send your first email:

{% code title="index.js" %}

```javascript
import { MailtrapClient } from "mailtrap";

const mailtrap = new MailtrapClient({
  token: process.env.MAILTRAP_API_KEY, // You can create your API key here https://mailtrap.io/api-tokens
});

mailtrap
  .send({
    from: { name: "Mailtrap Test", email: "sender@example.com" },
    to: [{ email: "recipient@example.com" }],
    subject: "Hello from Mailtrap Node.js",
    text: "Plain text body",
  })
  .then(console.log)
  .catch(console.error);
```

{% endcode %}

{% hint style="info" %}
Get your API token from your Mailtrap account under **Settings → API Tokens**.
{% endhint %}

#### SMTP integration

To integrate SMTP with your Node.js app, navigate to the **Integration** tab under Sending Domains and copy/paste the ready-made code snippet or credentials.

{% hint style="info" %}
You'll have to use Nodemailer, as Node.js doesn't have built-in support for SMTP sending.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-fb34da83b6547eb2e57eb59dd46b010ccf0a0a81%2Fmailtrap-nodejs-smtp-integration.png?alt=media" alt=""></div>

Read more about SMTP integration in the [Email API/SMTP - SMTP Integration](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/smtp-integration) article.

#### RESTful API integration

To integrate Mailtrap using RESTful API, use the sample configuration among **Code samples** under the API section.

API integration can be used with any Node.js framework or library that supports HTTP requests. For more details, refer to the [API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api).

<div data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-d64f0c3b2448e81616270c5e1d1d63f9f69f77ce%2Fmailtrap-nodejs-api-integration.png?alt=media" alt=""></div>

Read more about API integration in the [Email API/SMTP - API Integration](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/api-integration) article.
