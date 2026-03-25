# Source: https://nodemailer.com/extras

Title: Extra modules | Nodemailer

URL Source: https://nodemailer.com/extras

Markdown Content:

* [](https://nodemailer.com/)
* Extra modules

Extra modules
-------------

In addition to Nodemailer itself, several companion libraries extend what you can do with email in Node.js. These tools help you receive incoming mail, compose messages programmatically, parse raw email content, and preview emails during development.

Official companion libraries[​](https://nodemailer.com/extras#official-companion-libraries "Direct link to Official companion libraries")
-----------------------------------------------------------------------------------------------------------------------------------------

These packages are maintained by the Nodemailer team and designed to work seamlessly with Nodemailer.

1. [smtp-server](https://nodemailer.com/extras/smtp-server) - Build your own SMTP server to accept incoming email connections. Useful for creating custom mail servers, testing email workflows, or building email-receiving applications.
2. [smtp-connection](https://nodemailer.com/extras/smtp-connection) - A low-level SMTP client for establishing connections to mail servers. This is the underlying component that powers Nodemailer's [SMTP transport](https://nodemailer.com/smtp), exposed separately for advanced use cases where you need direct control over the SMTP protocol.
3. [mailparser](https://nodemailer.com/extras/mailparser) - Parse raw email messages (RFC 822 format) into structured JavaScript objects. The streaming parser efficiently handles large emails and extracts headers, body content, and attachments into an easy-to-use format.
4. [mailcomposer](https://nodemailer.com/extras/mailcomposer) - Generate RFC 822-compliant email messages from JavaScript objects. This is useful when you need to create a properly formatted [MIME message](https://nodemailer.com/message) without sending it immediately, such as for storing drafts or passing to another system.

These are independent open-source projects that complement Nodemailer and may be helpful depending on your use case.

1. [EmailEngine](https://emailengine.app/?utm_source=nodemailer&utm_campaign=nodemailer&utm_medium=module-link) - A self-hosted application that provides a REST API for any IMAP mailbox. It handles email sending via SMTP and delivers real-time updates through webhooks, making it easier to integrate email functionality into your applications.
2. [ImapFlow](https://imapflow.com/) - A modern, Promise-based IMAP client for Node.js. Originally built for EmailEngine, it works as a standalone library for reading and managing emails from any IMAP server.
3. [mailauth](https://github.com/andris9/mailauth) - A comprehensive library for email authentication. It validates and generates SPF, DKIM, DMARC, ARC, and BIMI records, helping you verify email authenticity and improve deliverability.
4. [email-templates](https://github.com/forwardemail/email-templates) - A complete framework for managing email templates. It supports template rendering, preview in browsers and iOS Simulator, and integrates directly with Nodemailer for sending.
5. [preview-email](https://github.com/forwardemail/preview-email) - A development tool that automatically opens emails in your browser for preview. It works with Nodemailer to help you inspect and debug email content before sending to real recipients.

* * *

The first four packages (smtp-server, smtp-connection, mailparser, and mailcomposer) are maintained within the Nodemailer GitHub organization and follow the same release cycle as Nodemailer. The remaining projects are maintained by the broader open-source community.

[](https://nodemailer.com/dkim)[](https://nodemailer.com/extras/smtp-server)

* [Official companion libraries](https://nodemailer.com/extras#official-companion-libraries)
* [Related projects](https://nodemailer.com/extras#related-projects)
