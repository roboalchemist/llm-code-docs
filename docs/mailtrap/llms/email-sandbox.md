# Source: https://docs.mailtrap.io/getting-started/email-sandbox.md

# Email Sandbox

Learn how to inspect and debug emails with sandbox functionality.

**What you can do:**

1. Catch testing emails from staging.
2. Preview and analyze content for spam.
3. Validate HTML/CSS before sending emails.

### Good to know

* Your emails won't reach your users as you use our Sandbox SMTP.
* You don't need to verify a domain to use sandbox.

### Overview

{% stepper %}
{% step %}
**Navigate to Email Sandbox**

Go to [your first Sandbox](https://mailtrap.io/inboxes) by clicking **Sandboxes**, then My **Sandbox**.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-33398144da3e02dddb55e33938a6af5c67b90851%2Fgetting-started-sandbox-navigation.png?alt=media" alt="Sandboxes page showing My Project with My Inbox sandbox highlighted"><figcaption></figcaption></figure></div>

{% hint style="info" %}
By default, we created an sandbox for you and called it "My Sandbox". The Edit button on the far right allows you to rename either a project or a sandbox.
{% endhint %}

Once inside My **Sandbox**, copy the credentials from the **Integration** tab to your clipboard.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-16813c2be4a9ab3460cdb264dd3bfd2647a2f7f3%2Fgetting-started-sandbox-smtp-credentials.png?alt=media" alt="Integration tab showing SMTP credentials including host, port, username, password and auth settings" width="375"><figcaption></figcaption></figure></div>

Or, use one of the pre-made code snippets for major programming languages and frameworks:

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-255b2e6d5f02aa8189979ea89403d3fa4d119ffc%2Fgetting-started-sandbox-code-samples.png?alt=media" alt="Code Samples section with PHP framework dropdown showing CakePHP, Laravel, Symfony and other options" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
**Send your first test email**

After sending the first test email, you can immediately find it in your Mailtrap sandbox.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d4d3d1234b92f3066bbf117bceff36df73c6335d%2Fgetting-started-test-email-received.png?alt=media" alt="Test email displayed in Mailtrap sandbox inbox" width="563"><figcaption></figcaption></figure></div>

Click on the email, and proceed to inspect and debug it by selecting the HTML Check tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d0e8dbdd58e18017feb19295c0f2d2b99b4fb1c0%2Fgetting-started-html-check-results.png?alt=media" alt="HTML Check tab showing email validation results" width="375"><figcaption></figcaption></figure></div>

Lastly, you can automate the QA flow with [API](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-email-testing-api) if you need it.
{% endstep %}

{% step %}
**Bonus: Invite your colleagues**

Mailtrap is a collaborative tool. Starting from the [Team Plan](https://mailtrap.io/billing/plans/testing), you can create different sandboxes and projects and share them with your colleagues.

This allows you to organize all testing-related workflows among different people, from user management with different permissions to SSO.
{% endstep %}
{% endstepper %}

### What else you can do with Email Sandbox

* [Enable email per sandbox feature](https://docs.mailtrap.io/email-sandbox/setup/email-address-per-sandbox)
* [HTML or RAW format preview](https://docs.mailtrap.io/email-sandbox/testing/email-template)
* [HTML Check](https://docs.mailtrap.io/email-sandbox/testing/email-html)
* [Automatic Forwarding](https://docs.mailtrap.io/email-sandbox/management/automatic-email-forwarding) and [Manual Forwarding](https://docs.mailtrap.io/email-sandbox/management/manual-email-forwarding) to view emails in real sandboxes
* [Test Bcc and email headers](https://docs.mailtrap.io/email-sandbox/testing/email-headers-and-bcc)
