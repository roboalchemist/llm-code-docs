# Source: https://nodemailer.com

Title: Nodemailer

URL Source: https://nodemailer.com/

Markdown Content:
Nodemailer
===============

[Skip to main content](https://nodemailer.com/#__docusaurus_skipToContent_fallback)

[![Image 1: Nodemailer](https://nodemailer.com/img/nm_logo_200x136.png) **Nodemailer**](https://nodemailer.com/)[Documentation](https://nodemailer.com/)[EmailEngine](https://emailengine.app/?utm_source=nodemailer&utm_campaign=nodemailer&utm_medium=navbar)

[NPM](https://www.npmjs.com/package/nodemailer)[GitHub](https://github.com/nodemailer/nodemailer)

Search

* [Nodemailer](https://nodemailer.com/)
* [Usage](https://nodemailer.com/usage)
* [Message configuration](https://nodemailer.com/message)
* [SMTP transport](https://nodemailer.com/smtp)
* [Other transports](https://nodemailer.com/transports)
* [Plugins](https://nodemailer.com/plugins)
* [DKIM](https://nodemailer.com/dkim)
* [Extra modules](https://nodemailer.com/extras)
* [Error reference](https://nodemailer.com/errors)
* [License](https://nodemailer.com/license)
* [![Image 2](https://nodemailer.com/img/EmailEngine_logo_vert.png) Send and receive emails easily with Outlook and Gmail using OAuth2.](https://emailengine.app/?utm_source=nodemailer&utm_campaign=nodemailer&utm_medium=sidebar)

* [](https://nodemailer.com/)
* Nodemailer

On this page

Nodemailer
==========

**Send emails from Node.js - easy as cake! ✉️**

Nodemailer is the most popular email sending library for Node.js. It makes sending emails straightforward and secure, with zero runtime dependencies to manage.

Install with npm

`npm install nodemailer`

Looking for a complete email gateway solution?

[**EmailEngine**](https://emailengine.app/?utm_source=nodemailer&utm_campaign=nodemailer&utm_medium=tip-link) is a self-hosted email gateway that provides REST API access to IMAP and SMTP accounts, webhooks for mailbox changes, and advanced features like OAuth2, delayed delivery, open and click tracking, bounce detection, and more.

Why Nodemailer?[​](https://nodemailer.com/#why-nodemailer "Direct link to Why Nodemailer?")
-------------------------------------------------------------------------------------------

* **Zero runtime dependencies** - everything you need is included in a single, well-maintained package.
* **Security focused** - designed to avoid remote code execution vulnerabilities that have affected other Node.js email libraries.
* **Full Unicode support** - send messages with any characters, including emoji 💪.
* **Cross-platform** - works identically on Linux, macOS, and Windows with no native addons required (ideal for cloud environments like Azure).
* **HTML and plain-text emails** - send rich HTML emails with automatic plain-text fallbacks.
* **[Attachments](https://nodemailer.com/message/attachments)** and **[embedded images](https://nodemailer.com/message/embedded-images)** - easily include files and inline images in your messages.
* **Built-in TLS/STARTTLS encryption** - secure connections are handled automatically.
* **Multiple [transports](https://nodemailer.com/transports)** - send via [SMTP](https://nodemailer.com/smtp), [Sendmail](https://nodemailer.com/transports/sendmail), [Amazon SES](https://nodemailer.com/transports/ses), [streams](https://nodemailer.com/transports/stream), and more.
* **[DKIM signing](https://nodemailer.com/dkim)** and **[OAuth2 authentication](https://nodemailer.com/smtp/oauth2)** - enterprise-ready email authentication.
* **[Proxy support](https://nodemailer.com/smtp/proxies)** - route email through proxies for restricted network environments.
* **[Plugin API](https://nodemailer.com/plugins)** - extend functionality with [custom plugins](https://nodemailer.com/plugins/create) for advanced message processing.
* **[Ethereal.email](https://ethereal.email/) integration** - generate test accounts instantly for [local development and testing](https://nodemailer.com/smtp/testing).

Requirements[​](https://nodemailer.com/#requirements "Direct link to Requirements")
-----------------------------------------------------------------------------------

* **Node.js v6.0.0 or later** (examples using async/await require Node.js v8.0.0 or later).

No additional system libraries, services, or build tools are needed.

Quick Start[​](https://nodemailer.com/#quick-start "Direct link to Quick Start")
--------------------------------------------------------------------------------

Sending an email with Nodemailer involves three simple steps:

1. **Create a transporter** - Configure your [SMTP server](https://nodemailer.com/smtp) or another supported [transport method](https://nodemailer.com/transports).
2. **Compose your message** - Define the sender, recipient(s), subject, and [content](https://nodemailer.com/message).
3. **Send the email** - Call `transporter.sendMail()` with your message options.

### Example: Sending an Email with Ethereal[​](https://nodemailer.com/#example-sending-an-email-with-ethereal "Direct link to Example: Sending an Email with Ethereal")

[Ethereal](https://ethereal.email/) is a free service that captures outgoing emails for [testing](https://nodemailer.com/smtp/testing). No emails are actually delivered, making it perfect for development.

`const nodemailer = require("nodemailer");// Create a transporter using Ethereal test credentials.// For production, replace with your actual SMTP server details.const transporter = nodemailer.createTransport({  host: "smtp.ethereal.email",  port: 587,  secure: false, // Use true for port 465, false for port 587  auth: {    user: "maddison53@ethereal.email",    pass: "jn7jnAPss4f63QBp6D",  },});// Send an email using async/await(async () => {  const info = await transporter.sendMail({    from: '"Maddison Foo Koch" <maddison53@ethereal.email>',    to: "bar@example.com, baz@example.com",    subject: "Hello ✔",    text: "Hello world?", // Plain-text version of the message    html: "<b>Hello world?</b>", // HTML version of the message  });  console.log("Message sent:", info.messageId);})();`

tip

Ethereal provides a preview URL for every message sent, allowing you to view the rendered email in your browser. This is invaluable for testing email layouts and content during development.

Source and License[​](https://nodemailer.com/#source-and-license "Direct link to Source and License")
-----------------------------------------------------------------------------------------------------

Nodemailer is open source software, licensed under the [MIT No Attribution (MIT-0)](https://nodemailer.com/license) license. This means you can use it freely in any project without attribution requirements. Browse the source code on [GitHub](https://github.com/nodemailer/nodemailer).

* * *

Made with ❤️ by [Andris Reinman](https://github.com/andris9). Logo by [Sven Kristjansen](https://www.behance.net/kristjansen).

[Next Usage](https://nodemailer.com/usage)

* [Why Nodemailer?](https://nodemailer.com/#why-nodemailer)
* [Requirements](https://nodemailer.com/#requirements)
* [Quick Start](https://nodemailer.com/#quick-start)
  * [Example: Sending an Email with Ethereal](https://nodemailer.com/#example-sending-an-email-with-ethereal)

* [Source and License](https://nodemailer.com/#source-and-license)

Copyright © 2010 - 2026 Andris Reinman. Powered by [EmailEngine](https://emailengine.app/?utm_source=nodemailer&utm_campaign=nodemailer&utm_medium=footer).
