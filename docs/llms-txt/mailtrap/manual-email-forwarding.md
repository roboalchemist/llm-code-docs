# Source: https://docs.mailtrap.io/email-sandbox/management/manual-email-forwarding.md

# Manual Forwarding

You can forward emails from sandbox to any inbox.

* View emails in different email clients, or even other apps.
* Notify your colleagues or clients about the testing progress.
* Use it as a proxy between your application and your email client and never miss a thing from your QA environment.

Email forwarding is available starting from the [Basic plan](https://mailtrap.io/pricing/).

### Manual forwarding setup

To forward emails manually, go to the **Manual Forward** tab in your sandbox and add the email address for forwarding.

The email confirmation will be sent to this email address for verification. Once the address is confirmed by its owner, you can forward emails to it.

Return to the sandbox, open the message you want to forward and click the forwarding icon in the top-right of the screen.

In the **Manual Forward** tab, you will also find the list of email addresses for forwarding and their statuses:

* *active* means that its owner has confirmed that they agree to receive emails.
* *pending* means that the owner hasn't confirmed that they agree to receive emails.

Click the three-dot menu icon next to the email address to resend confirmation, or to remove this email address.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dca8a6a2d86c013e3a266e6f270ba91a889e08ef%2Fsandbox-manual-forward-addresses.png?alt=media" alt="" width="563"></div>

### `From:` header in forwarded emails

All forwarded email messages use forward.mailtrap.info in the `From:` header, e.g., when you forward an email, you'll see something like this in your sandbox:

> From: Mailtrap Forward <<b751965-a5480376@forward.mailtrap.info>

It helps to use forwarding for users with a strict DMARC policy on their domains. Since DMARC doesn't allow sending emails from your domain without permissions, sandbox rewrites the `From:` header.

But because the original sender is valuable information, especially in automated testing, we still preserve it in *x-mailtrap-original-from* header of the forwarded emails.
