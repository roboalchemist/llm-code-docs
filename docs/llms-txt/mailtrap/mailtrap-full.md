# Mailtrap Documentation

Source: https://docs.mailtrap.io/llms-full.txt

---

# Documentation

Complete email infrastructure for developers. Send production emails, test in sandbox, and run email campaigns - all in one platform.

Build, test, and send emails with confidence using Mailtrap's comprehensive email platform designed for developers and product teams.

## Official SDKs

Get started quickly with our official SDKs for your favorite programming language.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><i class="fa-node-js">:node-js:</i> <strong>Node.js</strong></td><td><em>Official Node.js SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/nodejs">Node.js</a></td><td></td></tr><tr><td><i class="fa-php">:php:</i> <strong>PHP</strong></td><td><em>Official PHP SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/php">PHP</a></td><td></td></tr><tr><td><i class="fa-gem">:gem:</i> <strong>Ruby</strong></td><td><em>Official Ruby SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/ruby">Ruby</a></td><td></td></tr><tr><td><i class="fa-microsoft">:microsoft:</i> <strong>.NET</strong></td><td><em>Official .NET SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/dotnet">.NET</a></td><td></td></tr><tr><td><i class="fa-java">:java:</i> <strong>Java</strong></td><td><em>Official Java SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/java">Java</a></td><td></td></tr><tr><td><i class="fa-python">:python:</i> <strong>Python</strong></td><td><em>Official Python SDK for Mailtrap</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/python">Python</a></td><td></td></tr><tr><td><i class="fa-laravel">:laravel:</i> <strong>Laravel</strong></td><td><em>Laravel integration with Mailtrap PHP SDK</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/php">PHP</a></td><td></td></tr><tr><td><i class="fa-symfony">:symfony:</i> <strong>Symfony</strong></td><td><em>Symfony integration with Mailtrap PHP SDK</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/sdk/php">PHP</a></td><td></td></tr></tbody></table>

{% columns %}
{% column %}
**Get started in 5 Minutes**

Setting up Mailtrap should be the easiest part of your email journey. With clear endpoints, copy-paste-ready examples, and instant authentication, you'll send your first email in minutes — not hours.

No guesswork, no complexity — just your first successful email, fast.

[Get started](https://docs.mailtrap.io/documentation/getting-started/email-api-smtp) [API reference](https://api-docs.mailtrap.io/)
{% endcolumn %}

{% column %}
{% code title="index.js" overflow="wrap" %}

```javascript
// Send your first email
const { MailtrapClient } = require("mailtrap");

const client = new MailtrapClient({
  token: "YOUR_API_TOKEN"
});

await client.send({
  from: { email: "hello@example.com" },
  to: [{ email: "user@example.com" }],
  subject: "Hello from Mailtrap!",
  text: "Welcome to Mailtrap Email API"
});
```

{% endcode %}
{% endcolumn %}
{% endcolumns %}

## Quick start guides

Choose your product and get up and running quickly with our step-by-step guides.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><i class="fa-paper-plane">:paper-plane:</i> <strong>Email API/SMTP</strong></td><td>Send Production Emails</td><td><em>Deliver transactional emails reliably with our API or SMTP service. Get detailed analytics and ensure high deliverability.</em></td><td><a href="getting-started/email-api-smtp">email-api-smtp</a></td><td></td></tr><tr><td><i class="fa-bug">:bug:</i> <strong>Email Sandbox</strong></td><td>Test Before Sending</td><td><em>Catch and inspect emails in a safe testing environment. Preview, analyze, and debug emails before they reach real inboxes.</em></td><td><a href="getting-started/email-sandbox">email-sandbox</a></td><td></td></tr><tr><td><i class="fa-cart-arrow-up">:cart-arrow-up:</i> <strong>Email Marketing</strong></td><td>Run Email Campaigns</td><td><em>Design, send, and track marketing campaigns. Manage subscribers and analyze campaign performance.</em></td><td><a href="getting-started/email-marketing">email-marketing</a></td><td></td></tr></tbody></table>

## Explore features

Discover the full range of features and capabilities across our email platform.

{% columns %}
{% column width="33%" %} <i class="fa-paper-plane">:paper-plane:</i> **Email API/SMTP**

* [API Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [Email Templates](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates)
* [Email Logs](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/logs)
* [Webhooks](https://docs.mailtrap.io/documentation/email-api-smtp/advanced/webhooks)
  {% endcolumn %}

{% column width="33%" %} <i class="fa--bug">:-bug:</i> **Email Sandbox**

* [Email Template Inspector](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-template)
* [HTML Check](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-html)
* [Deliverability Tests](https://docs.mailtrap.io/documentation/email-sandbox/testing/spam-blacklist-reports)
* [Sandbox API](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-api-integration)
* [Team Collaboration](https://docs.mailtrap.io/documentation/email-sandbox/collaboration/sharing-sandboxes)
  {% endcolumn %}

{% column width="33%" %} <i class="fa-cart-arrow-up">:cart-arrow-up:</i> **Email Marketing**

* [Campaign Management](https://docs.mailtrap.io/documentation/email-marketing/campaigns)
* [Contacts Management](https://docs.mailtrap.io/documentation/email-marketing/contacts)
* [Email Templates](https://docs.mailtrap.io/documentation/email-marketing/campaigns/email-templates)
* [Statistics](https://docs.mailtrap.io/documentation/email-marketing/campaigns/statistics)
* [Segments](https://docs.mailtrap.io/documentation/email-marketing/contacts/segments)
  {% endcolumn %}
  {% endcolumns %}

## Guides & integrations

Learn how to integrate Mailtrap with your favorite tools and migrate from other services.

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><i class="fa-link">:link:</i> <strong>Integrations</strong></td><td>Third-party Tools</td><td><em>Connect Mailtrap with Laravel, Rails, Node.js, Python and more popular frameworks.</em></td><td><a href="https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/integrations">Integrations</a></td></tr><tr><td><i class="fa-globe">:globe:</i> <strong>DNS Setup</strong></td><td>Domain Configuration</td><td><em>Configure SPF, DKIM, and DMARC records with guides for all major DNS providers.</em></td><td><a href="email-api-smtp/setup/sending-domain">sending-domain</a></td></tr></tbody></table>

## Ready to get started?

{% hint style="info" %}
**New to Mailtrap?** Start with our [Email Sandbox](https://docs.mailtrap.io/documentation/getting-started/email-sandbox) to test your emails in a safe environment, then move to [Email API/SMTP](https://docs.mailtrap.io/documentation/getting-started/email-api-smtp) for production sending.
{% endhint %}

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><i class="fa-rocket-launch">:rocket-launch:</i> <strong>Start with a Free plan</strong></td><td><em>Get started with Mailtrap's free plan. No credit card required. Test emails, send up to 4000 emails/m, and explore all features.</em></td><td><a href="https://mailtrap.io/register/signup?utm_source=gitbook&#x26;utm_campaign=article" class="button secondary">Sing up free</a></td><td></td></tr><tr><td><i class="fa-message">:message:</i> <strong>Talk to Sales</strong></td><td><em>Need a custom plan or have enterprise requirements? Our team is ready to help you find the perfect solution.</em></td><td><a href="https://mailtrap.io/talk-to-sales/?utm_source=gitbook&#x26;utm_campaign=article" class="button secondary">Contact Sales</a></td><td></td></tr></tbody></table>


# Email API/SMTP

Learn how to send your application emails with Mailtrap Email API/SMTP

Learn how to send your application emails with Mailtrap.

**Migration guides:**

* [SendGrid](https://mailtrap.io/sendgrid-migration/)
* [Mailchimp](https://mailtrap.io/mandrill-migration/)
* [Mailgun](https://mailtrap.io/mailgun-migration/)
* [Postmark](https://mailtrap.io/postmark-migration/)
* [Amazon SES](https://mailtrap.io/amazon-ses-migration/)

Big-volume sender? [Contact us for onboarding assistance](https://mailtrap.io/talk-to-sales/).

### Overview

{% hint style="info" %}
**Good to know**

* To send emails to your recipients, you must own a domain and add it to Mailtrap.
* Every new domain requires a Compliance Check after DNS verification. In most of cases it takes a few minutes.
* You can try out all features with the Demo domain we provided once you sign up.
  {% endhint %}

{% stepper %}
{% step %}
**Verify the sending domain you own**

To add a domain you own, go to the **Sending Domains** tab and click **Add Domain**. Type your domain name and confirm with the **Add** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-763b1fe1e16ad1d7bd180575732ab39acc4a3ae4%2Fsending-domains-add-domain-button.png?alt=media" alt="Add Domain form in Mailtrap with domain input field" width="375"><figcaption></figcaption></figure></div>

Then, add the DNS records Mailtrap provides to your domain provider.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7cd3f3d08e7583cdf7ae997eadd54df078b35734%2Fsending-domains-dns-records-to-add.png?alt=media" alt="DNS records table showing domain verification requirements" width="563"><figcaption></figcaption></figure></div>

Check our [Sending Domain Setup Guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain) for detailed instructions on adding and verifying your domain.
{% endstep %}

{% step %}
**Integrate your application via Email API or SMTP**

**SMTP Integration**

To send emails via Mailtrap SMTP, follow the instructions [in this article](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b3f6c0e6edcf50132a4514612bbf3dfabfb59518%2Fgetting-started-smtp-integration-credentials.png?alt=media" alt="SMTP integration credentials and code samples" width="563"><figcaption></figcaption></figure></div>

**Email API Integration**

To send emails via Mailtrap Email API, follow the steps [in this article](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-602b5f9aee3c5224140faf8c5f40b6ef0e609592%2Fgetting-started-api-integration-credentials.png?alt=media" alt="Email API integration credentials and code samples" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### What else you can do with Mailtrap Email API/SMTP

* [Set up Tracking Settings](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain#optional-tracking-settings-ffi49)
* [Set up Unsubscribe Settings](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain#unsubscribe-settings-ekyqh)
* [Set up Webhooks](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain#optional-webhooks-4hmes)
* [Set up Email Categories](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/categories)
* [Add or import Suppressions](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/suppressions-list)
* [Create templates](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-templates.md)


# Email Sandbox

Learn how to inspect and debug emails with Mailtrap Email Sandbox

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

* [Enable email per sandbox feature](https://docs.mailtrap.io/documentation/email-sandbox/setup/email-address-per-sandbox)
* [HTML or RAW format preview](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-template)
* [HTML Check](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-html)
* [Automatic Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding) and [Manual Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/manual-email-forwarding) to view emails in real sandboxes
* [Test Bcc and email headers](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-headers-and-bcc)


# Email Marketing

Learn how to set up and send email marketing campaigns with Mailtrap

Make sure you've added and [verified a domain](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain), or you won't be able to send a campaign.

### How to set up and send a campaign

{% stepper %}
{% step %}
Go to **Email Marketing** and click **Create New Campaign**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e78333259c0895cb79f8191c0ee30ff6a54e96d1%2Fmarketing-campaign-create-button.png?alt=media" alt="Email Marketing page with Create New Campaign button" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Fill out the form with your company details, such as name, address, city, zip code, and country. Optionally, enter your company's phone number and link to the website. Click **Continue**.

{% hint style="info" %}
This information will be added to email footers to ensure compliance with existing regulations. You'll only have to complete this step once when creating your first campaign.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fe2f916144c632bbca566ba05fd0e30e9b041ac6%2Fmarketing-campaign-company-details.png?alt=media" alt="Company details form for campaign compliance" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Choose a domain from the **Select domain** dropdown, then set the **Campaign name**, **Subject**, and **From** email address. Optionally, set the From name, Reply-To name, and Reply-To email. If you have only one domain, no need to choose anything, it's selected for you by default. Click **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7438e739ed4d440af44bdd34f4db7be4c157acc4%2Fmarketing-campaign-settings.png?alt=media" alt="Campaign details form with domain, name, subject, and email settings" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
You'll be taken to the Design step, where you can choose between Drag & Drop and HTML editors. If you have templates stored, you'll see them here. You can use them in your campaigns. Read more about creating templates [here](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-templates.md).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a39b2f1f77325f288af5dd1d98e02701be96b2ef%2Ftemplate-design-selection.png?alt=media" alt="Template selection page with Drag &#x26; Drop and HTML editors" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Create your campaign design, click **Save**, and then **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c8be19e87f8d68f7965da6b5b11e176692580cf6%2Fmarketing-campaign-design-editor.png?alt=media" alt="Drag and drop email editor interface" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Instead of continuing to the next step, you can click **Send Test** to send a test to one email address to check the design in your email client or click **Finish Later** to return to the campaign **Details**, where you can change any of the parameters you set in previous steps.
{% endhint %}
{% endstep %}

{% step %}
If you've already imported your contacts, select your audience by including or excluding specific lists. Then, click **Confirm Audience**.

{% hint style="success" %}
With **Including** and **Excluding** features, you can easily send campaigns to specific audience groups only.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5e05b425a2dbc0bc7fa105c60b3a02004dd3ecc0%2Fgetting-started-audience-selection.png?alt=media" alt="Audience selection with including and excluding lists" width="563"><figcaption></figcaption></figure></div>

{% hint style="warning" %}
If you didn't upload your contacts before creating a campaign, you'll be prompted to import contacts at this stage. Simply click **Import Contacts** and follow the steps ([refer to this section](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/contacts.md#how-to-upload-contacts-nag8y) in our Contacts guide for more details). **Important**: you should create Fields beforehand to be able to assign variables to the fields (map fields) when importing contacts.
{% endhint %}
{% endstep %}

{% step %}
At this point, you can click **Send Test** to send a test email to one email address, choose **Send now** to send the campaign immediately, or select **Schedule campaign** to send it at a specific date and time.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ad90c58a55bc9f563f5d29c31c02bbb1d6b4bf3e%2Fmarketing-campaign-send-options.png?alt=media" alt="Send and schedule campaign options" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
To schedule the campaign, click **Schedule Campaign**, select the date, and choose the time. Then, confirm the action by clicking **Schedule Sending**.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9c32b4843af03eee725633fa8eeeabc38f45fbb1%2Fmarketing-campaign-schedule-form.png?alt=media" alt="Schedule campaign form with date and time picker" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### What's next?

Once your campaign has been sent, you can check the campaign deliverability data and stats. Here's how to do it:

{% stepper %}
{% step %}
Click **Email Marketing** in the left navigation panel and you'll have a quick preview of all the campaign data. If we're still collecting the data, you'll be notified accordingly.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-96be0e0862d333dd58e722c7c64504714e9c596c%2Fmarketing-campaign-list-view.png?alt=media" alt="Campaign sent confirmation messages" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
If you want more details for a particular campaign, click the campaign name, then select the **Reports** tab where you'll see the full [Statistics report](https://docs.mailtrap.io/documentation/email-marketing/campaigns/statistics).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-56ae57c22ff2e41fd60d52b78f5af2a4e444a81b%2Fmarketing-campaign-statistics.png?alt=media" alt="Campaign statistics report showing delivery rates, opens, clicks, and mailbox provider breakdown" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}


# Overview

Overview of Mailtrap Email API and SMTP service: key features, use cases, and target audience.

Mailtrap Email API/SMTP is a reliable email delivery service designed for developers and businesses to send transactional and bulk emails at scale. Whether you're sending password resets, order confirmations, or marketing campaigns, we ensure your emails reach the inbox.

## What is Email API/SMTP?

Email API/SMTP provides two powerful methods for sending emails:

* **RESTful API**: Modern, flexible API for programmatic email sending
* **SMTP Service**: Traditional protocol compatible with any email client or library

Both methods offer the same features, deliverability, and analytics - choose based on your technical requirements.

## Key Features

#### Reliable Delivery

* Enterprise-grade infrastructure: Built for reliability and scale
* Automatic Failover: Redundant systems ensure delivery
* Smart Routing: Optimal rules selection for each email depending on recipient MX

#### Analytics & Monitoring

* Real-Time Analytics: Track opens, clicks, bounces instantly
* Detailed Email Logs: Full visibility into email journey
* Custom Categories: Organize and analyze by type/templates/etc
* Webhook Events: Real-time notifications for email events

#### Deliverability + Support

* Deliverability and Support teams: helps with migration, monitoring and all questions you might have
* [Complete Deliverability Guide](https://mailtrap.io/email-deliverability-guide/): Best practices for optimal inbox placement
* Domain Authentication: SPF, DKIM, DMARC setup
* Dedicated IP + Warmup: Gradual reputation building
* Suppressions Management: Automatic bounce handling
* Feedback Loops: ISP complaint processing

#### Developer-Friendly

* Official SDKs: Node.js, PHP, Python, Ruby, and more
* RESTful API: Simple JSON-based communication
* SMTP Integration: Works with existing email libraries
* Sandbox Testing: Test before production

## Use Cases

#### Transactional Emails

Perfect for critical user communications:

* Password resets and account verification
* Order confirmations and shipping notifications
* Appointment reminders and alerts
* System notifications and updates
* Two-factor authentication codes

#### Bulk Emails

Dedicated infrastructure for marketing:

* Newsletters and announcements
* Promotional campaigns
* Product updates and releases
* Event invitations
* Customer surveys

## Quick Start Guide

{% stepper %}
{% step %}
**Choose Your Integration Method**

{% tabs %}
{% tab title="API" %}

```bash
curl -X POST "https://send.api.mailtrap.io/api/send" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "from": {"email": "hello@example.com"},
    "to": [{"email": "user@example.com"}],
    "subject": "Hello from Mailtrap!",
    "text": "Welcome to Mailtrap Email API"
  }'
```

{% endtab %}

{% tab title="SMTP" %}

```
Host: live.smtp.mailtrap.io
Port: 587
Username: YOUR_USERNAME
Password: YOUR_PASSWORD
Encryption: STARTTLS
```

{% endtab %}

{% tab title="Node.js SDK" %}

```javascript
const { MailtrapClient } = require("mailtrap");

const client = new MailtrapClient({
  token: "YOUR_API_TOKEN"
});

await client.send({
  from: { email: "hello@example.com" },
  to: [{ email: "user@example.com" }],
  subject: "Hello from Mailtrap!",
  text: "Welcome to Mailtrap Email API"
});
```

{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
**Verify Your Domain**

Add DNS records to authenticate your sending domain and improve deliverability.
{% endstep %}

{% step %}
**Start Sending**

Begin with transactional emails, then expand to bulk campaigns as needed.
{% endstep %}
{% endstepper %}

## Two Streams Architecture

Mailtrap separates email traffic for optimal deliverability:

| Stream                                                                              | Purpose               | Features                                                              |
| ----------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------- |
| **Transactional**                                                                   | Triggered user emails | High priority, immediate delivery                                     |
| [**Bulk**](https://docs.mailtrap.io/documentation/email-api-smtp/setup/bulk-stream) | Marketing campaigns   | Built-in compliance, unsubscribe management, separate suppresion list |

## Getting Started

{% columns %}
{% column %}
**Setup & Configuration**

* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [API Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [IP Warmup](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/ip-warmup)
  {% endcolumn %}

{% column %}
**Essential Features**

* [Deliverability Guide](https://mailtrap.io/email-deliverability-guide/)
* [Email Templates](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates)
* [Analytics & Reports](https://docs.mailtrap.io/documentation/email-api-smtp/analytics)
* [Deliverability Features](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability)
  {% endcolumn %}
  {% endcolumns %}

## Why Choose Mailtrap?

**For Developers**

* Clean, well-documented APIs
* Multiple integration options
* Comprehensive SDKs
* Sandbox environment for testing

**For Businesses**

* High deliverability rates
* Detailed analytics and reporting
* Scalable infrastructure
* Enterprise-grade reliability

**For Teams**

* Multi-user access control
* Shared resources and templates
* Collaborative workflows
* Activity logging

## Support & Resources

Need help getting started or have questions?

<a href="https://api-docs.mailtrap.io/" class="button primary" data-icon="books">API Reference</a> <a href="help/faqs" class="button primary" data-icon="messages-question">FAQs</a> <a href="help/troubleshooting" class="button primary" data-icon="screwdriver-wrench">Troubleshooting</a> <a href="mailto:support@mailtrap.io" class="button primary" data-icon="envelope">Contact Support</a>

## Next Steps

{% stepper %}
{% step %}
[setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup "mention")

*Authenticate your sending domain*
{% endstep %}

{% step %}
[api-integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration "mention")

*Choose integration method - API or SMTP*
{% endstep %}

{% step %}
[email-templates](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates "mention")

*Design reusable emails*
{% endstep %}

{% step %}
[analytics](https://docs.mailtrap.io/documentation/email-api-smtp/analytics "mention")

*Track your email metrics*
{% endstep %}
{% endstepper %}


# Setup & Configuration

Set up and configure Mailtrap email API and SMTP service and start sending emails in minutes.

Complete guide to setting up and configuring Mailtrap Email API/SMTP for your application. Follow these steps to start sending emails in production.

### Quick start checklist

Get up and running with this essential setup checklist:

* [ ] Create your Mailtrap account
* [ ] Verify your sending domain
* [ ] Choose integration method (API or SMTP)
* [ ] Configure authentication
* [ ] Send your first email

### Configuration steps

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Sending Domain Setup</strong></td><td><em>the foundation of email delivery. Verify your domain ownership and configure authentication records (SPF, DKIM, DMARC) for optimal deliverability.</em></td><td><a href="setup/sending-domain">sending-domain</a></td></tr><tr><td><strong>API Integration</strong></td><td><em>modern RESTful API for programmatic email sending. Best for new applications and microservices architecture.</em></td><td><a href="setup/api-integration">api-integration</a></td></tr><tr><td><strong>SMTP Integration</strong></td><td><em>traditional SMTP protocol for universal compatibility. Works with any email library or legacy system.</em></td><td><a href="setup/smtp-integration">smtp-integration</a></td></tr><tr><td><strong>Dedicated IP</strong></td><td><em>gradually build your sending reputation. Essential for high-volume senders and dedicated IPs.</em></td><td><a href="deliverability/ip-warmup">ip-warmup</a></td></tr></tbody></table>

### Choose your integration method

#### When to use API

**Best for:**

* Modern web applications
* Microservices architecture
* Cloud-native applications
* Real-time sending needs
* Advanced analytics requirements

**Advantages:**

* Faster performance
* Better error handling
* Detailed response data
* Webhook support
* Easier debugging

**Example:**

```bash
curl -X POST "https://send.api.mailtrap.io/api/send" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "from": {"email": "hello@example.com"},
    "to": [{"email": "user@example.com"}],
    "subject": "Test Email",
    "text": "This is a test email"
  }'
```

#### When to use SMTP

**Best for:**

* Legacy applications
* Email clients
* CMS platforms
* Standard libraries
* Minimal code changes

**Advantages:**

* Universal compatibility
* No code changes required
* Works with any language
* Familiar protocol
* Easy migration


# Sending Domain Setup

Set up your sending domain in Mailtrap. Add DNS records, verify SPF/DKIM/DMARC, pass compliance, and start sending emails in minutes.

Need help adding DNS records for your specific provider? Check out our detailed step-by-step guides:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>AWS Route 53</td><td><a href="sending-domain/aws-route-53">aws-route-53</a></td></tr><tr><td>Cloudflare</td><td><a href="sending-domain/cloudflare">cloudflare</a></td></tr><tr><td>Digital Ocean</td><td><a href="sending-domain/digitalocean">digitalocean</a></td></tr><tr><td>GoDaddy</td><td><a href="sending-domain/godaddy">godaddy</a></td></tr><tr><td>Google Cloud DNS</td><td><a href="sending-domain/google-cloud-dns">google-cloud-dns</a></td></tr><tr><td>Google Domains</td><td><a href="sending-domain/google-domains">google-domains</a></td></tr><tr><td>Namecheap</td><td><a href="sending-domain/namecheap">namecheap</a></td></tr></tbody></table>

### Setting up your domain <a href="#setting-up-your-own-domain-ys86q" id="setting-up-your-own-domain-ys86q"></a>

{% hint style="info" %}
In the example below, we'll be using GoDaddy.
{% endhint %}

{% stepper %}
{% step %}
**Add domain**

Navigate to *Sending Domains* in the left navigation panel.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e765901ed723ae470ea4999bd6aca87031b7d4f0%2Fsending-domains-navigation-menu.png?alt=media" alt="Sending Domains navigation menu in Mailtrap" width="375"><figcaption></figcaption></figure></div>

Click *Add Domain.*

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-763b1fe1e16ad1d7bd180575732ab39acc4a3ae4%2Fsending-domains-add-domain-button.png?alt=media" alt="Add Domain button in Sending Domains page" width="375"><figcaption></figcaption></figure></div>

Type in the domain from which you want to send emails and click Add. Remember that you should be the domain owner with access to its DNS records/have someone with access to DNS records.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-09fac4e0475bb2277240b3e73db3d004056e3a1e%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

After this step, you’ll see the Domain Verification page.
{% endstep %}

{% step %}
**Domain verification**

At this stage, you need to verify the domain. You have two options:

* Send domain verification instructions to your admin or developer;
* Or verify the domain yourself if you have access to your domain’s DNS records (your domain provider account).

{% hint style="success" %}
To send instructions to your admin or developer, enter their email address and click Send Instructions.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-869cd3d0c5cc4d89f1e4892747ff10fc420c6792%2Fsending-domains-email-to-admin.png?alt=media" alt=""></div>
{% endstep %}

{% step %}
**Company / personal information**

After adding your DNS records, click on “Fill in Compliance Form” to complete a short form where you’ll be asked to provide either business or personal information.

Please keep in mind that it’s crucial to provide correct information corresponding to your company registration details. It is important in order to comply with international regulations. This information may also be automatically added to the email footer of promotional emails sent from your domain.

{% hint style="success" %}
Tip: If you've provided this information before, you won't be asked to fill it in again.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9abe8b736e49ddd031913668386f6ad03005f22a%2Fimage.png?alt=media" alt="" width="178"><figcaption></figcaption></figure></div>

You can switch between personal and business information only once, meaning that you cannot change it after the form is submitted.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1d6ac87b600ed374ceb5375fb248eeeaffd325d2%2Fimage%20(1).png?alt=media" alt="" width="307"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
**Compliance check**

Compliance check is a process of checking every new domain added to Mailtrap.

Once all the DNS records are successfully verified, your domain will undergo an automatic review. This usually takes a couple of minutes. If your domain is verified at this stage, you’ll see the Verified badge next to your domain and below Compliance Check, and you’ll be able to start sending the emails. You’ll also receive an email informing you that your domain is ready for sending emails.

Some domains may be selected for additional checks. If so, we’ll ask you to fill out a simple Compliance Form and answer a few questions about your business, sending goals, etc. You’ll see a notification under Compliance Check and a link to the form.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7779f11b318169af3b41c44b26a059baf14fef93%2Fsending-domains-compliance-pending.png?alt=media" alt="Compliance check pending status with Fill In Compliance Form button" width="375"><figcaption></figcaption></figure></div>

We’ll email you if we need additional information from you. If all the checks are successful at this stage, your domain will be verified.

In some cases, your domain may be selected for manual verification. This is the final check before your domain is verified. The length of the manual verification depends on how fast you reply to our emails. If successful, you'll see Verified status. If not, you'll see a Rejected badge next to your domain and a message under Compliance Check. In case of any questions about the reasons for rejection, please contact our support team at <support@mailtrap.io>.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-248f70c090b3a4a77e5890ac8d8fec86e1a1bd7c%2Fimage%20(2).png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### To verify the domain yourself

{% stepper %}
{% step %}
Go to your domain provider and locate the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-97687794bc213094201a864a828e89bea8e0ee4b%2Fgodaddy-domain-list.png?alt=media" alt="GoDaddy domain list showing mailtrap.club domain" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Open the DNS settings and click Add New Record.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-91993d13b41a1e9e878b4837e98def98f64a3909%2Fgodaddy-add-new-record.png?alt=media" alt="GoDaddy DNS Management with Add New Record button" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Return to Mailtrap. On the Domain Verification page, you'll see the DNS records you need to add to your domain provider. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**. The naming of these records in Mailtrap is the same as in most domain providers but may differ slightly depending on the provider.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgQYlfnIjyfuyMmoUrOi7%2FScreenshot%202026-03-07%20at%2012.53.29.png?alt=media&#x26;token=f38534c6-c9eb-4b68-994b-9ab5a9abb67b" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in your domain provider. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbTwnYzuhhZ0Z7azFxeEs%2F2.png?alt=media&#x26;token=14a4ca67-124c-4c33-b42a-9c2facb89adb" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-646eb806c7559d828f77292968e0a7b7c526f2d7%2Fgodaddy-dns-record-types.png?alt=media" alt="DNS record type dropdown in GoDaddy showing CNAME selected" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Copy the Name and Value for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-94d5f169e6204e5059cd20ab6270710a6da97e88%2Fsending-domains-copy-button.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste them into your domain provider.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2da2e0320002e1cba5f9eaa12d9d57f225a5e49b%2Fgodaddy-dns-new-record-form.png?alt=media" alt="GoDaddy DNS new record form with CNAME type, name, and value fields" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click Save after adding each record in your domain provider.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to your domain provider.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fc27bfe4a827818976df3203f0d583ad9e6c47eb%2Fgodaddy-dns-all-records-added.png?alt=media" alt="GoDaddy DNS records table showing all Mailtrap DNS records added" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Then, return to Mailtrap. Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7cd3f3d08e7583cdf7ae997eadd54df078b35734%2Fsending-domains-dns-records-to-add.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from Missing to Verified, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-924eae9e3b33c09d9093d228643e516438d4278d%2Fsending-domains-godaddy-domain-list.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Once the DNS records are verified, you’ll be taken to the next step, which is Compliance Check.

**Notes:**

* Some domain providers require a postfix format of the DKIM record. If that’s the case, replace `rwmt1._domainkey` with `rwmt1._domainkey.yourdomain.com` . Repeat the process for `rwmt2._domainkey` , changing the name to `rwmt2._domainkey.yourdomain.com` .
* If you’re asked to set TTL, use the default value as indicated under the TTL field on the Domain Verification page in Mailtrap.
  {% endstep %}
  {% endstepper %}

### DNS propagation time

After you add or update DNS records, it may take **15 minutes to a few hours** for Mailtrap to detect them.

DNS changes are not applied instantly because:

* DNS records are cached by DNS resolvers according to their TTL (Time To Live).
* There are multiple DNS servers worldwide, and updates need time to propagate across them.
* Even if you can see the updated record using one DNS checker or resolver, it doesn’t necessarily mean that Mailtrap (or other services) can already resolve it from their location.

In most cases, propagation completes within a few hours, but in rare cases it may take up to 24 hours.

#### How to check if your DNS records have propagated

To check if your DNS records have propagated, you have two options:

<details>

<summary>DNS Checker (automatic)</summary>

An easy way to verify whether your DNS records are publicly available is to use [DNS Checker](https://dnschecker.org/), which queries DNS servers worldwide and shows DNS propagation of 6 continents.

To use DNS Checker:

* Go to dnschecker.org and enter your domain name

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjYwez8Hi97R8ERodoUbA%2FScreenshot%202026-02-26%20at%2017.52.40.png?alt=media&#x26;token=34f1c3a1-ff72-4f22-a381-22e9396a638e" alt=""><figcaption></figcaption></figure>

* Select the record type (e.g., TXT, MX, CNAME, etc.)
* Click **Search**

And here's what your results should look like:

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FUk5K6M7crZW5x2mYetJj%2FScreenshot%202026-02-26%20at%2017.53.29.png?alt=media&#x26;token=64885c49-ab38-4192-917e-d39e2792d325" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary><code>dig</code> command (manual)</summary>

You can also verify your DNS records manually with the `dig` command. The `dig` command is a DNS lookup tool available on macOS and Linux (and on Windows via BIND tools) that queries DNS servers and returns the current records for a domain.

To use it, open a terminal and run dig followed by the record type and your domain name. You can also add `+short` for a concise output.

For instance, here's what you can run if you want to check:

* A TXT record (for SPF or domain verification):

```
dig TXT yourdomain.com +short
```

* A specific selector (e.g., DKIM):

```
dig TXT selector._domainkey.yourdomain.com +short
```

* MX records:

```
dig MX yourdomain.com +short
```

* CNAME records:

```
dig CNAME track.yourdomain.com +short
```

**If the correct value is returned in the response**, the record has likely propagated.

**If you see no result or an old value**, the record may still be propagating.

You can also check propagation using different public DNS resolvers:

```
dig TXT yourdomain.com @8.8.8.8 +short      # Google DNS
dig TXT yourdomain.com @1.1.1.1 +short      # Cloudflare DNS
```

</details>

**If the record appears across multiple public resolvers**, it should soon be visible to Mailtrap as well.

**If the records are correctly configured and still not verified after several hours**, double-check:

* Record type (TXT, CNAME, MX, etc.)
* Host/name field (e.g., using `selector._domainkey` instead of the full domain)
* That there are no duplicate or conflicting records

If everything looks correct, please allow additional time for propagation before contacting support.

### (Optional) Tracking settings <a href="#optional-tracking-settings-ffi49" id="optional-tracking-settings-ffi49"></a>

An optional step is to change the tracking settings. By default, Mailtrap tracks email opens for each email sent. You can also enable click tracking.

{% hint style="info" %}
*Click tracking* and *custom domain for clicks tracking* are available only for paid accounts.
{% endhint %}

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-11682d2b0b3e8ee2ae0b3572d55a78281df0e6ab%2Fsending-domains-godaddy-dns-settings.png?alt=media" alt=""></div>

With tracking enabled, you will find the open and click rates in the Analytics reports. [Read this article](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/statistics/README.md) for a detailed breakdown of Statistics.

1. Navigate to the Tracking Settings tab.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f2dd8ab60d23d151d14cdb89ad413b76d8022820%2Fsending-domains-godaddy-record-type-dropdown.png?alt=media" alt="" width="563"></div>

2. Toggle the switch next to Track Opened Emails to enable or disable tracking opens. Mailtrap tracks email opens via an invisible pixel. It’s added to each message sent from your account. When an email is opened, a pixel is loaded, and an ‘open’ event is recorded. Each of these events will be visible in [Email Logs](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/statistics/email-logs.md).

{% hint style="info" %}
Some mailbox providers, browsers, and extensions block invisible pixels. Users can also choose not to display images, or a solution they use to retrieve emails may not support images by default. In each of these cases, an 'open' event won't be recorded even if an email is opened.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b80d5a176fb44087160973643aaf26f0e36813f7%2Fsending-domains-godaddy-add-txt-record.png?alt=media" alt="" width="563"></div>

3. If you're a paid user, toggle the switch next to Track Clicks to enable or disable tracking clicks. If you enable click tracking, the toggle for Custom Domain for Clicks Tracking will be switched on automatically. That way, all links will be redirected through your domain (mt-link.yourdomain.com). And if you verified all the records correctly in Step 2, Domain Tracking will also be verified and ready to use.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ebea938a8d30b08f905db3fc9a0ea11d22c61e96%2Fsending-domains-godaddy-add-cname-record.png?alt=media" alt="" width="563"></div>

### Unsubscribe settings <a href="#unsubscribe-settings-ekyqh" id="unsubscribe-settings-ekyqh"></a>

You can also configure unsubscribe settings.

Unsubscribe links are mandatory for bulk emails as per privacy laws. If your emails don't include an unsubscribe link, Mailtrap will add an Unsubscribe Footer automatically. This is what it will look like:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-af55a590f24ed383f919ec678823504c5da079a0%2Fsending-domains-godaddy-all-records-added.png?alt=media" alt="" width="375"></div>

To add an unsubscribe link anywhere in your template, include this tag in your HTML template: `<a href="__unsubscribe_url__">unsubscribe</a>` . Mailtrap will render a clickable link in your email.

Unsubscribe Footer and Links are optional for transactional emails and are switched off by default.

However, if you want to, you can still add an Unsubscribe Footer to your transactional emails by toggling the switch On under Unsubscribe Footer for Transactional emails or adding an HTML tag mentioned above.

<div align="left" data-full-width="true" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4992ee5c7ad9aaa93f7ba76bc3ac07394a7d475b%2Fsending-domains-verification-complete.png?alt=media" alt=""></div>

If you’d like, you can mix both approaches: automatically add a footer to emails sent from one domain and do it manually (when applicable) for emails sent from another domain.

If an end-user uses an unsubscribe link, Mailtrap will reject any future emails sent to this address from this particular domain. You can quickly find all such emails in the Email Logs by filtering for the “reject” event.

You will still be able to email them using other domains or subdomains added to your Mailtrap account.

For that reason, it's worth having different domains or subdomains for different types of emails. This way, users can, for example, unsubscribe from your bulk or marketing messages while still receiving vital transactional messages.

### (Optional) Webhooks <a href="#optional-webhooks-4hmes" id="optional-webhooks-4hmes"></a>

Lastly, you can set up webhooks to receive event information almost real-time.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-988c8a11b6d92b6c3dda2afa7f212395a570236e%2Fsending-domains-compliance-in-progress.png?alt=media" alt="" width="563"></div>

Click the Add New Webhook button, choose the Sending Stream, paste the webhook URL (your endpoint) into the designated field, select the events you want to listen to, and then test the setup.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e2d625db2172c74e3034aef951960418e6e0f130%2Fsending-domains-webhook-setup.png?alt=media" alt="" width="563"></div>

Mailtrap also allows you to batch up to 500 events within a webhook. That is, group all events under one object, and thus save on computing power.

### Useful tips <a href="#sending-domains-j_1ht" id="sending-domains-j_1ht"></a>

After completing the setup process, you can always return to the Sending Domains tab to add any additional domains or subdomains. If you, for example, misspelled a domain, you’ll need to delete it and re-add it with the correct spelling.

{% hint style="info" %}
You can't create any additional demo domains, but you can delete an existing one if needed.
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-db9360468d9f8504c86b87ea24f07e71b02a4ade%2Fsending-domains-verified-list.png?alt=media" alt="Sending Domains list showing verified domains with status and emails sent" width="563"><figcaption></figcaption></figure></div>

Remember that the domain with the Demo badge can be used to send emails only to the email address you registered with.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f195f25522fd08164c2662a526e8098cd0d33bb1%2Fsending-domains-demo-restrictions.png?alt=media" alt="Demo domain showing restriction message that it can only send to yourself" width="375"><figcaption></figcaption></figure></div>

You can send emails to your recipients only from domains that have a Verified status. If the status is Pending or Rejected, you won't be able to send emails.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5ab4fb4261ca787c13445c10c912573aa792bed2%2Fsending-domains-pending-verified-statuses.png?alt=media" alt="Sending Domains showing pending and verified status badges" width="375"><figcaption></figcaption></figure></div>

From the Sending Domains menu, you can also delete the domains, subdomains, or the demo domain you no longer use. Just press the bin icon next to the domain. This will remove the domain from the list, and you won't be able to send any further emails until you add and verify it again.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-882512a0e6a62b63ad781d7be6015356d46215a5%2Fsending-domains-delete-button.png?alt=media" alt="Sending Domains with delete button highlighted" width="563"><figcaption></figcaption></figure></div>

Note that removing a domain won't remove it from your Mailtrap account completely. It will still appear, for example, in analytics, and will be displayed with the (deleted) suffix, just like in the example below:

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-de575e5dbc7fc7d39303b25d1ddd55637d0697ed%2Fsending-domains-deleted-in-stats.png?alt=media" alt="Stats overview showing deleted domains with (deleted) suffix" width="375"><figcaption></figcaption></figure></div>

We do this to preserve your historical stats that would otherwise be lost.


# AWS Route 53

Verify your Mailtrap sending domain in AWS Route 53. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from AWS Route 53.

This guide assumes your domain uses Route 53's nameservers (e.g., `ns-123.awsdns-12.com` or `ns-456.awsdns-34.net`). This applies whether you registered your domain directly with AWS or just pointed your DNS to Route 53 from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the AWS Management Console, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to the **AWS Management Console**, type **Route 53** in the search bar, and click on it.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fk9E6RAYQXU6kCjvQKo6l%2Faws-route53-search.png?alt=media&#x26;token=ce589f79-3d1a-4cc1-bdff-a6f6f81928b0" alt="" width="375"></div>
{% endstep %}

{% step %}
Navigate to **Hosted Zone** settings for the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FqF8mqbLrxo3wwY8lY1AF%2Faws-route53-hosted-zones.png?alt=media&#x26;token=bb48b450-01c8-46c2-9606-d0517b81a74c" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FK1R2UizdVI9Cbh7n5TM8%2Faws-route53-domain-records.png?alt=media&#x26;token=f5cdf109-0e07-4238-b47f-e200555bb78c" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Create record** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FNA8EYM9RYQGOUOxbjrDN%2Faws-route53-create-record-button.png?alt=media&#x26;token=2db45bca-6494-4ffb-966a-c66ca693b1cf" alt="" width="375"></div>
{% endstep %}

{% step %}
Return to Mailtrap. On the Domain Verification page, you'll see the DNS records you need to add to AWS Route 53. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FJquaSVRQBHMiM4aSbxjH%2F1.png?alt=media&#x26;token=b7f605ad-89c0-4123-94e7-c319d35148c4" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in AWS Route 53. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type records** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjmkdQ32IwgOcpQs5HM5A%2F2.png?alt=media&#x26;token=12a1a229-b725-426f-bdd0-102611afba36" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPdyyks2i6mSTQRDEAYU5%2Fmailtrap-dns-records-copy.png?alt=media&#x26;token=7eaa8210-7e6b-451c-a1a9-a4ea64cb6a32" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the **Name** and **Value** into AWS Route 53. The namings of the records are the same in AWS Route 53 as in Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fad42KavVGNP0bnEJeMtJ%2Faws-route53-add-record-form.png?alt=media&#x26;token=3f6c28d6-c281-49e9-a13c-3e6ae024e7d6" alt="" width="563"></div>

Use the default value for TTL as indicated in Mailtrap. Click Add another record after adding each record in AWS Route 53.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to AWS Route 53. Click **Create Records**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FSt3aa6mmzjjCpRdUUsMX%2Faws-route53-all-records-added.png?alt=media&#x26;token=0f4936e2-2608-4091-82ac-ac0122da33ca" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FchZAR8QZqW8HXV1qt27M%2Faws-route53-recheck-dns.png?alt=media&#x26;token=672ff691-3f18-4d33-ac8d-b905aaccf2f2" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the **Status** of DNS records will change from Missing to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FvoLvu6K12jnOfutIV0AM%2Fmailtrap-verified-dns-records.png?alt=media&#x26;token=7fdb4ea8-9a6d-4002-a301-4630f89c52d7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, [consult AWS documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) or contact us at <support@mailtrap.io>.
{% endhint %}


# Cloudflare

Verify your Mailtrap sending domain in Cloudflare. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Cloudflare.

This guide assumes your domain uses Cloudflare's nameservers (e.g., `anna.ns.cloudflare.com` or `bob.ns.cloudflare.com`). This applies whether you registered your domain directly with Cloudflare or just pointed your DNS to Cloudflare from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in Cloudflare's dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Open the **Cloudflare dashboard** and select the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FX34GISlEp6hCT3gdwXu5%2Fcloudflare-domain-dashboard.png?alt=media&#x26;token=be43139b-a9be-4307-aa26-73b91c8c0b76" alt="" width="563"></div>
{% endstep %}

{% step %}
Click on the **DNS button** in the left navigation panel. This will open DNS records.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbqITal5uybQkArd6cTsD%2Fcloudflare-dns-menu.png?alt=media&#x26;token=e99c9153-255f-45f7-bf88-9193e20e30df" alt="" width="131"></div>
{% endstep %}

{% step %}
Click on the **Add Record** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fswm55N6qPhld319vXmFW%2Fcloudflare-add-record-button.png?alt=media&#x26;token=c8dae520-e838-4d8b-a383-ccc7db5681e1" alt="" width="563"></div>
{% endstep %}

{% step %}
On the **Domain Verification page** in Mailtrap, you'll see the DNS records you need to add to Cloudflare. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FGwQOUF3UKuy9oM9IVSUP%2F1.png?alt=media&#x26;token=a86e347a-bf9f-4e1f-bfa1-785f5a631e8e" alt=""><figcaption></figcaption></figure>

Pay attention to the Type next to each record in Mailtrap and choose a relevant one in Cloudflare. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjILEdX6bX0GcoJKI0Gmu%2F2.png?alt=media&#x26;token=51fa1a45-c89d-449f-9b2f-4f41d1797dd3" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FEXds5DPNC7IJtndLIcZy%2Fcloudflare-record-type-dropdown.png?alt=media&#x26;token=e41a106b-f48d-4e8d-be5b-25aad380d2a9" alt="DNS record type dropdown in Cloudflare" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FZwLgo6duw7mE0nndLgz3%2Fcloudflare-copy-dns-values.png?alt=media&#x26;token=a88b4350-5f1c-46ee-8474-023954498165" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the the values into Cloudflare. Remember that Cloudflare refers to the Value field as **Target** for **CNAME records** and **Content** for **TXT records**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgA5QbsK62ivxw3AMPEmk%2Fcloudflare-paste-dns-values.png?alt=media&#x26;token=16b2cee0-8889-4c22-b311-1e3f9c9bdf3b" alt="" width="563"></div>
{% endstep %}

{% step %}
If you're not using a proxy, make sure you disable it. By default, it will be enabled.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FMSQr9P6sGH235Ko4qQmu%2Fcloudflare-disable-proxy.png?alt=media&#x26;token=46953687-bafd-43c6-a39b-cf0cdb4f64a3" alt=""></div>
{% endstep %}

{% step %}
Use the default value for **TTL**.

Click **Save** and repeat the process for all the remaining DNS records.
{% endstep %}

{% step %}
Then, **return to Mailtrap**. Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Furic1nPmhM4mz8fNHoKY%2Fcloudflare-recheck-dns-records.png?alt=media&#x26;token=7e62b12a-5021-42dc-bace-5e4d98c4da9c" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FLwRo224r3B8pXSH0KBkp%2Fcloudflare-verified-dns-records.png?alt=media&#x26;token=7e856771-bd6b-4b05-a101-71197002d559" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Cloudflare documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) or contact us at <support@mailtrap.io>
{% endhint %}


# DigitalOcean

Verify your Mailtrap sending domain in Digital Ocean. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from DigitalOcean.

This guide assumes your domain uses DigitalOcean's nameservers (e.g., `ns1.digitalocean.com`, `ns2.digitalocean.com`, or `ns3.digitalocean.com`). This applies whether you registered your domain directly with DigitalOcean or just pointed your DNS to DigitalOcean from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the DigitalOcean control panel, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Choose **Networking** in the main menu of the control panel and click the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ftj6ovmJqSTrZnQi2wucn%2Fdigitalocean-networking-menu.png?alt=media&#x26;token=0764f9e3-8e25-45b5-b6ce-9bf60d16f33b" alt="" width="563"></div>

You'll see the Create new record heading.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FCjXvWku54jbF9eR0zttt%2Fdigitalocean-create-new-record.png?alt=media&#x26;token=0665f3fe-452e-40b2-8117-4354cca3fa0c" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to DigitalOcean. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FfTY2GuH8Cqg8jp9jAMNx%2F1.png?alt=media&#x26;token=ecb83873-85ff-4933-87d6-571e0abbfbcd" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Check the type next to each record in Mailtrap and choose a relevant one in DigitalOcean (CNAME or TXT). Mailtrap has **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FM9Qb9xjRN51kRXe6SBsg%2F2.png?alt=media&#x26;token=a2fa60c8-020b-4137-88f0-5439168147cc" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FuMmYcXehJRSsqDT1DSwv%2Fdigitalocean-record-type-selector.png?alt=media&#x26;token=78281ed5-f83f-4ed6-a813-565efee3a007" alt="DigitalOcean DNS record type selector dropdown" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FltKclhYOCGvriEpopafy%2Fdigitalocean-copy-dns-values.png?alt=media&#x26;token=8754abcb-643e-486e-9f1b-9ae3392954d6" alt="" width="563"></div>
{% endstep %}

{% step %}
**Paste the values into DigitalOcean**. Remember that DigitalOcean refers to the Name field as Hostname for all record types. For CNAME type records, it refers to the Value field as Is an Alias of.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F9szhr97gl9HQeHH6y7GF%2Fdigitalocean-txt-record-fields.png?alt=media&#x26;token=544eb54c-84c4-449c-b9a6-1be36df21cdf" alt="DigitalOcean TXT record input form showing Hostname and Value fields" width="563"><figcaption></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FVYKtkvSXKoEhdnprvll4%2Fdigitalocean-cname-record-fields.png?alt=media&#x26;token=0ff82e6c-f134-48ed-9697-cea2318e771c" alt="DigitalOcean CNAME record input form showing Hostname and Is an Alias of fields" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Use the default value for TTL.

Click Create Record after adding each record in DigitalOcean.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all Mailtrap DNS records to DigitalOcean.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FJgIBvUvor8R1OyTU3cfT%2Fdigitalocean-all-records-added.png?alt=media&#x26;token=7af22ec5-97a7-4f27-b9fc-bee143e611b3" alt="" width="375"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FAJo4OwRGaiDH9Ug6Smf5%2Fnamecheap-recheck-dns-records.png?alt=media&#x26;token=9255ea93-967d-41ab-b05e-32d5edcdd3bb" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from Missing to Verified, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fn5rsgyAtuI3lw5nTa0Mq%2Fdigitalocean-dns-verified.png?alt=media&#x26;token=31ad7aae-f939-4ecc-9ff0-bc05bfb3cdb3" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [DigitalOcean documentation](https://docs.digitalocean.com/products/networking/dns/how-to/manage-records/) or contact us at <support@mailtrap.io>.
{% endhint %}


# GoDaddy

Verify your Mailtrap sending domain in GoDaddy. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from GoDaddy.

This guide assumes your domain uses GoDaddy's nameservers (e.g., `ns1.domaincontrol.com` or `ns2.domaincontrol.com`). This applies whether you registered your domain directly with GoDaddy or just pointed your DNS to GoDaddy from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the GoDaddy dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to GoDaddy and locate the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FA0We0czQf0sdyOo6gKiC%2Fgodaddy-domain-list.png?alt=media&#x26;token=67c6c7c6-e8da-4f3e-b6ce-8957ae821348" alt="" width="375"></div>
{% endstep %}

{% step %}
Open the DNS settings and click **Add New Record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5WCxWMiIYgu6HdkFDKFO%2Fgodaddy-dns-settings.png?alt=media&#x26;token=994af315-6860-455a-969c-ea0300864e90" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to GoDaddy. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**. The naming of these records in Mailtrap is the same as in GoDaddy.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fm0siaM1xMYdRbyinCWx9%2F1.png?alt=media&#x26;token=9c199389-6e2a-48cd-b5d7-f6741bf7140a" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in GoDaddy. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7RhtVtC6IiYXIdbZbkj6%2F2.png?alt=media&#x26;token=091e9e14-661e-420f-b98a-2dda217f4831" alt=""><figcaption></figcaption></figure>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FEWjqsg3rLrTV7zZ3HIIW%2Fgodaddy-dns-type-selector.png?alt=media&#x26;token=f20316cf-3859-45c2-95d5-515446d7d7a2" alt="GoDaddy DNS record type selector dropdown" width="375"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FYf5YGSWS0GzgFLZFuYyc%2Fgoogle-cloud-dns-6.png?alt=media&#x26;token=e0c487f6-cbac-453d-a924-79502ac975da" alt="" width="563"></div>
{% endstep %}

{% step %}
Paste the values into GoDaddy DNS management page.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fv1UJWwEjCESQB92EKm5M%2Fgodaddy-paste-dns-values.png?alt=media&#x26;token=79bc9a14-4ef4-49f7-a9b5-71fb1d47db72" alt="Pasting DNS values into GoDaddy record form" width="563"></div>
{% endstep %}

{% step %}
Use the default value for TTL.

Click Save after adding each record in GoDaddy.
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to GoDaddy.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5ET4NItKg574VPZXOJDe%2Fgodaddy-all-dns-records-added.png?alt=media&#x26;token=b1c7dca8-042f-46bf-8f25-0ac175335499" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBhy4zE92B4b5WXKNU3FL%2Fgoogle-cloud-dns-11.png?alt=media&#x26;token=7971338b-bf0b-4e9f-96f2-e9ee91a7f37a" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from Missing to Verified, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTHdyFGVpLLtjdgD99mOW%2Fgoogle-cloud-dns-12.png?alt=media&#x26;token=f1bc9168-5e47-460a-8e79-3fbc859f9df7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [GoDaddy documentation](https://uk.godaddy.com/help/manage-dns-records-680) or contact us at <support@mailtrap.io>.
{% endhint %}


# Google Cloud DNS

Verify your Mailtrap sending domain in Google Cloud DNS. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Google Cloud DNS.

This guide assumes your domain uses Google Cloud DNS nameservers (e.g., `ns-cloud-a1.googledomains.com` or `ns-cloud-b1.googledomains.com`). This applies whether you registered your domain directly with Google or just pointed your DNS to Google Cloud DNS from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the Google Cloud Console, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to Google Cloud Console, type **Cloud DNS** in the search bar, and choose it from the results.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FmYbK66KbGzgbkcPOwCTk%2Fgoogle-cloud-dns-1.png?alt=media&#x26;token=bda68415-50ab-407c-aab7-ad2805886e32" alt="" width="563"></div>
{% endstep %}

{% step %}
In the Cloud DNS Zones page, open the **Zone details** for the domain you've added to Mailtrap by clicking on the **Zone name**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FGGBCde4w4LMHrJsJ96Ch%2Fgoogle-cloud-dns-2.png?alt=media&#x26;token=03a8aa03-471a-419e-9505-e8b113b0efbf" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add Standard**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRGFkPwWvqNCftp6I2U86%2Fgoogle-cloud-dns-3.png?alt=media&#x26;token=afd9664f-d5d8-4332-aaaa-aa54fb0f7148" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Google Cloud DNS. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F0jgCAhBqu6m4BYgC2mqz%2F1.png?alt=media&#x26;token=8dbdf55f-1e8f-412e-98db-c35942f73831" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Google Cloud DNS. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC). Ignore Google's SPF type record; it's deprecated.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FW90JI06Gym4eKGihPq3l%2F2.png?alt=media&#x26;token=0383b6e3-e1f9-4a5a-9ced-95802ac3f76a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FYf5YGSWS0GzgFLZFuYyc%2Fgoogle-cloud-dns-6.png?alt=media&#x26;token=e0c487f6-cbac-453d-a924-79502ac975da" alt="" width="563"></div>
{% endstep %}

{% step %}
And paste the values into Google Cloud DNS. Remember that Google Cloud DNS refers to the Name field as DNS Name and the Value field as either Canonical name (for CNAME-type records) or TXT data (for TXT-type records).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FxwFtV5zCdArLaotzijqp%2Fgoogle-cloud-dns-7.png?alt=media&#x26;token=035cb915-4406-4464-9b76-0ca2c2262b95" alt="Google Cloud DNS CNAME record form with DNS Name and Canonical name fields" width="375"><figcaption></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FfmxLtDqQusMdXFqCb1Uy%2Fgoogle-cloud-dns-8.png?alt=media&#x26;token=42a14773-0ace-4d00-9b61-f09fbd09f002" alt="Google Cloud DNS TXT record form with DNS Name and TXT data fields" width="563"><figcaption></figcaption></figure></div>

When adding TXT-type records, add double quotes in the beginning and the end of the record string in the TXT data field.
{% endstep %}

{% step %}
Use the default value for TTL.

Click **Create** after adding each record in Google Cloud DNS.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FIGyGSCq1CSZ4wZjUuzPb%2Fgoogle-cloud-dns-9.png?alt=media&#x26;token=ddf1dfea-cc5a-465e-8f70-b8bb6a4c3c7d" alt="" width="375"></div>
{% endstep %}

{% step %}
Repeat the process of copying and pasting for each record until you've added all the Mailtrap DNS records to Google Cloud DNS.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FHsPTUXl5rDKhlSzW8vdN%2Fgoogle-cloud-dns-10.png?alt=media&#x26;token=a3f30b17-0048-4e9e-ab57-2b1649c627ce" alt=""></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBhy4zE92B4b5WXKNU3FL%2Fgoogle-cloud-dns-11.png?alt=media&#x26;token=7971338b-bf0b-4e9f-96f2-e9ee91a7f37a" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTHdyFGVpLLtjdgD99mOW%2Fgoogle-cloud-dns-12.png?alt=media&#x26;token=f1bc9168-5e47-460a-8e79-3fbc859f9df7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Google Cloud DNS documentation](https://cloud.google.com/dns/docs/records) or contact us at <support@mailtrap.io>.
{% endhint %}


# Google Domains

Verify your Mailtrap sending domain in Google Domains. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To add and verify a sending domain in Mailtrap, you need access to your domain's DNS records and your domain provider account.

<a class="button secondary">Sending Domain Setup</a> check it for more details on setting up your sending domain. Continue reading to learn how to add Mailtrap DNS records to Google Domain.

{% hint style="info" %}
Note: On September 7, 2023, Squarespace acquired all domain registrations and related customer accounts from Google Domains. This means that Google Domains is now in the process of migrating account and domain data to Squarespace. Until the migration is completed, you can still manage your domains in Google Domains. After the migration, you'll need to manage your domain in Squarespace.

This guide assumes that your domain is either registered with Google Domains and uses its nameservers or isn't registered with Google Domains but uses its nameservers.
{% endhint %}

{% stepper %}
{% step %}
Go to Google Domains and select the domain you've added to Mailtrap.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fn8m9pbQlbNuRxybArIO5%2Fgoogle-domains-select-domain.png?alt=media&#x26;token=60319616-6454-4a4c-8729-1e5257f1502e" alt="" width="563"></div>
{% endstep %}

{% step %}
In the left-side navigation panel, click **DNS**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FrvAw8dVDX8iXocnhu8gN%2Fgoogle-domains-click-dns.png?alt=media&#x26;token=756b6162-cb0e-4985-820c-525bf040ff1c" alt="" width="188"></div>
{% endstep %}

{% step %}
Under **Custom records** in the **Resource** **records** section, choose **Manage custom records**. In case you don't have any resource records, click **Custom records** directly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FiAj90YvBSY3uMoUVEEgt%2Fgoogle-domains-manage-custom-records.png?alt=media&#x26;token=36e9a606-88b6-433d-bf47-ac126dcceeb6" alt="" width="563"></div>
{% endstep %}

{% step %}
Scroll down at the bottom of the records and click **Create new record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FcOkl9pUBwsuZ83lwAuwO%2Fgoogle-domains-create-new-record.png?alt=media&#x26;token=1cdf55f6-5019-4435-b9a6-d99cedd9c63d" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Google Domains. These are **Domain Verification**, **DKIM**, **DMARC**, and **Domain Tracking**. You'll need the values under **Type**, **Name**, and **Value**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWuaJG1KKC95SKGOlNcA5%2F1.png?alt=media&#x26;token=bb2cdb5d-c035-48e0-9ec1-dab04ecf38ec" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Google Domains. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FCbYGL0u9AEGgLtzgqO6C%2F2.png?alt=media&#x26;token=20b7980f-4b19-42c5-b508-d3e0925b1604" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTY9xq92EMTDoX50aTrh6%2Fgoogle-domains-copy-name-value.png?alt=media&#x26;token=4fb04b68-b3c3-4cb3-ad6e-0bb1af7493e8" alt="" width="563"></div>
{% endstep %}

{% step %}
**Paste the values into Google Domains**. Remember that Google Domains refers to the Name field as the **Host name** and the **Value field** as either the **Domain name** (for CNAME-type records) or **Text** (for TXT-type records).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F04K0RFkHyCxWovek3Ugz%2Fgoogle-domains-paste-values.png?alt=media&#x26;token=9d623582-c72e-43bb-ac49-d27edbc8234b" alt="" width="563"></div>
{% endstep %}

{% step %}
Use the **default** value for TTL.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FJX5Qb7tJcISLSCvks1bR%2Fgoogle-domains-ttl-default.png?alt=media&#x26;token=b0bc0958-0e54-48bc-a068-84e547de49ca" alt="" width="563"></div>
{% endstep %}

{% step %}
Repeat the process of copying, pasting, and clicking **Create new record** for each record until you've added all the Mailtrap DNS records to Google Domains. **Click Save**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FMOf7S7m2nYxm776SmVL0%2Fgoogle-domains-save-records.png?alt=media&#x26;token=db251b8f-cd42-41ae-8c04-3278493489fd" alt="" width="563"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FSWwZlpBRD4M8BSBrOpxT%2Fgoogle-domains-recheck-dns.png?alt=media&#x26;token=4c22a985-42c5-40c5-999d-1ef66e6e02de" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FUBrtvYPBZS0hlfJWb21t%2Fgoogle-domains-verified-status.png?alt=media&#x26;token=4c7535b7-2484-4dc3-806c-5c8eafe6ca92" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the [official Google Domains documentation](https://support.google.com/domains/answer/3290350?hl=en) or contact us at <support@mailtrap.io>.
{% endhint %}


# Namecheap

Verify your Mailtrap sending domain in Namecheap. Add DNS records for DKIM/DMARC verification, pass compliance, and start sending emails.

To start sending emails with Mailtrap, you need to own a domain (e.g., `yourcompany.com`) and then verify your ownership over it. For this, you'll need access to your domain provider account, more specifically, the DNS records management page.

In this guide, you'll learn how to add and verify a domain from Namecheap.

This guide assumes your domain uses Namecheap's nameservers (e.g., `dns1.registrar-servers.com` or `dns2.registrar-servers.com`). This applies whether you registered your domain directly with Namecheap or just pointed your DNS to Namecheap from another registrar. Not sure? Check your domain registrar's settings or look for where you manage your DNS records. If it's in the Namecheap dashboard, you're in the right place.

### Step-by-step guide

{% stepper %}
{% step %}
Go to Namecheap, locate the domain you've added to Mailtrap on the dashboard, and click **Manage**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBqoAkP7QizsTG9tMiNJf%2Fnamecheap-domain-dashboard.png?alt=media&#x26;token=f935c9fa-07b9-49ca-a0cf-95ae433aeec9" alt="" width="563"></div>
{% endstep %}

{% step %}
Navigate to the **Advanced DNS** tab.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRnNUAdv0cxefuUKEz8cG%2Fnamecheap-advanced-dns-tab.png?alt=media&#x26;token=231fbd1c-4a96-49e2-86da-02f895860992" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add New Record**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWJvru1WCVEGyti4E7Du1%2Fnamecheap-add-new-record-button.png?alt=media&#x26;token=424d01bd-62c5-4781-90af-e94647430545" alt="" width="563"></div>
{% endstep %}

{% step %}
On the Domain Verification page in Mailtrap, you'll see the DNS records you need to add to Namecheap. These are Domain Verification, DKIM, DMARC, and Domain Tracking. You'll need the values under Type, Name, and Value.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fkhch8E7OiMUoshdmr6Gd%2F1.png?alt=media&#x26;token=50ff1280-1fb3-404f-bc81-18e5fb1348dc" alt=""><figcaption></figcaption></figure>

Make sure you check the type next to each record in Mailtrap and choose a relevant one in Namecheap. There are **four CNAME type records** (Domain Verification, DKIM (2), and Custom Tracking Domain) and **one TXT type record** (DMARC).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FS8XlNVrj8Y7upIOU7zMP%2F2.png?alt=media&#x26;token=7c4c0452-c6d6-4962-8484-3d35e6896967" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The SPF check for your mail is covered by the domain verification record. There is no need to add a separate SPF record on your sending domain.
{% endhint %}
{% endstep %}

{% step %}
Copy the **Name** and **Value** for each record one by one. You can do this by hovering and clicking each record.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPdyyks2i6mSTQRDEAYU5%2Fmailtrap-dns-records-copy.png?alt=media&#x26;token=7eaa8210-7e6b-451c-a1a9-a4ea64cb6a32" alt="" width="563"></div>
{% endstep %}

{% step %}
And paste the values into Namecheap. Remember that Namecheap refers to the **Name** **field** as **Host**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F9LeXD9EjyIOuU6vjJGT9%2Fnamecheap-paste-host-value.png?alt=media&#x26;token=1f38354b-3d32-4d12-9102-d372e9b42406" alt="" width="563"></div>
{% endstep %}

{% step %}
Use the **default** value for TTL.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fuw1wRhjTWFsIEoNBIOYH%2Fnamecheap-ttl-default.png?alt=media&#x26;token=d6dd6543-5a92-4e6e-9b62-065ebe33e7d5" alt="" width="375"></div>
{% endstep %}

{% step %}
Repeat the process of copying, pasting, and clicking **Add New Record** for each record until you've added all the Mailtrap DNS records to Namecheap. Click **Save All Changes**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTMPRobkoji0ZnebCs3p8%2Fnamecheap-save-all-changes.png?alt=media&#x26;token=d02f1c5b-4ce9-4a35-8493-6b869816f35f" alt="" width="375"></div>
{% endstep %}

{% step %}
Some records may be verified immediately, while some may take more time. Mailtrap will check the DNS records automatically every hour, but you can force a check by clicking the Re-check DNS Records button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FAJo4OwRGaiDH9Ug6Smf5%2Fnamecheap-recheck-dns-records.png?alt=media&#x26;token=9255ea93-967d-41ab-b05e-32d5edcdd3bb" alt="" width="563"></div>
{% endstep %}

{% step %}
If you add all the required DNS records correctly, the Status of DNS records will change from **Missing** to **Verified**, and the red dots will turn green.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FvoLvu6K12jnOfutIV0AM%2Fmailtrap-verified-dns-records.png?alt=media&#x26;token=7fdb4ea8-9a6d-4002-a301-4630f89c52d7" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you have additional questions, consult the official [Namecheap documentation](https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/) or contact us at <support@mailtrap.io>.
{% endhint %}


# API Integration

Integrate Mailtrap email API. Get API credentials, choose transactional or bulk sending, use SDKs or code samples, and start sending.

Use API credentials to integrate Mailtrap with your project.

{% stepper %}
{% step %}
Go to the **Sending Domains** tab and choose the domain you want to send emails from. Remember that you'll be able to start sending emails once the domain is verified.
{% endstep %}

{% step %}
Navigate to the **Integration** tab for your selected domain.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c770f21d61dc676fb576e19fabf81671cb5b5a8c%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the **Integrate** button under **Transactional Stream** or **Bulk Stream**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bb2ed533ad8282eddc4bfd9aa9d575249205e9ac%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

**Transactional Stream** is used to send automated, non-promotional application emails triggered by the specific user action.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-eef39a1323370d004e69c4c9686f291f06ca942f%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

**Bulk Stream** is used to send a single marketing campaign to a large group of recipients in bulk.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4deee87f494c19629c1f76a859bb83eb47a66c27%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Toggle the switch to **API**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e5bc6fe628c677dfb1012313d9f2232f6564d4a5%2Fapi-integration-credentials-streams.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Build the authenticated HTTP request in your programming language or framework and configure it with **Mailtrap Host** and **API Token**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-277ed4a03452a3091f2067afa8e3078df3030ed6%2Fapi-integration-credentials-transactional.png?alt=media" alt="Transactional Stream API credentials showing Host and API Token" width="563"><figcaption><p>Transactional Stream API credentials</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-60ba1ceace0286cee9131e3d55845680d4d5e20e%2Fapi-integration-credentials-bulk.png?alt=media" alt="Bulk Stream API credentials showing Host and API Token" width="563"><figcaption><p>Bulk Stream API credentials</p></figcaption></figure></div>

Alternatively, choose the programming language or framework from the menu under **Code Samples** and copy the sample configuration already containing your credentials. In this menu, you'll find official SDKs for [PHP](https://github.com/railsware/mailtrap-php), [Python](https://github.com/railsware/mailtrap-python), [Ruby](https://github.com/railsware/mailtrap-ruby), and [Node.js](https://github.com/railsware/mailtrap-nodejs).

{% hint style="info" %}
Note: For now, only Ruby, PHP (Laravel + Symfony), and Node.js SDKs support Bulk Stream, but others are in development. Request and response examples are also available [here](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/67f1d70aeb62c-send-email-including-templates).
{% endhint %}

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a39d965f764098a681859256d7e0f8967b9f60a6%2Fapi-integration-code-samples-transactional.png?alt=media" alt="Code Samples dropdown showing programming languages including cURL, C++, C#, Go, Java, Node.js, Ruby, Python, and PHP" width="563"><figcaption><p>Transactional Stream code samples</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b415435c884d7847b7cd3079864ce33fdf1d75e7%2Fapi-integration-code-samples-bulk.png?alt=media" alt="Code Samples dropdown for Bulk Stream showing available programming languages and frameworks" width="563"><figcaption><p>Bulk Stream code samples</p></figcaption></figure></div>
{% endstep %}

{% step %}
Complete your script and run it. If you did everything correctly, you should find the sent email in the inbox of the email address you indicated in the script. The email will also appear in **Email Logs** in Mailtrap.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d64cbccae97e40d1548f8f93468528e98d31d9f7%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

Remember that each domain has different API tokens that you can always access by clicking on the desired domain and going to the **Integration** tab.

You can also create additional API tokens by going to **Settings** → **API Tokens** and clicking **Add Token**.

<a href="api-tokens" class="button primary" data-icon="magnifying-glass">Learn more about API Tokens</a>

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>

Mailtrap Email Sending API supports:

* attachments
* [email templates](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-sandbox/email-marketing/email-templates.md)
* [custom variables](https://docs.mailtrap.io/documentation/email-api-smtp/advanced/custom-variables)
* [email categories](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/categories)

{% hint style="info" %}
If you need any help with API integration, please, contact our support team at <support@mailtrap.io>.
{% endhint %}


# API Tokens

Learn how to create, manage, and use API tokens for Email API/SMTP.

#### Add and manage tokens manually

{% stepper %}
{% step %}
Navigate to **Settings** in the menu on the left and select **API Tokens**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
To add a new token, click the **Add Token** button in the upper right corner.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
**Type the token name** into the designated field.&#x20;

It’s perfectly fine to have a custom name for the API token, as it’s only for your reference, regardless of the use case.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FlpA9pLUncYMLdgSmAeKK%2FScreenshot%202025-12-16%20at%2016.19.22.png?alt=media&#x26;token=db12e0a4-70a9-4c7e-ba86-03015e19afdd" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Assign permissions** by checking the boxes in the corresponding access level columns. Note that you must have admin permissions on a particular domain to send emails with this token.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aad9698d90812d10b8afa0226ddf5fcafd66d19f%2Fapi-tokens-permissions-editor.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the **Save** button and preview the new token under the **API Tokens** main menu.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbJoeiyZ94WGz0p0AdGh3%2FScreenshot%202025-12-16%20at%2016.20.39.png?alt=media&#x26;token=f400948a-2bd0-4232-bc85-5d9d61e23475" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

#### Auto-created token per domain

When you create a domain, a token is automatically created and named based on the following formula: \[domain name] + \[token] + \[token ID].

For example, if you add the example.com domain, the token for that domain will be named example.com token 1234. By default, the automatically generated token gets Domain Admin Mailtrap for the given domain.

{% hint style="info" %}
You need to edit permissions for the automatically generated token to allow for authorization on other domains.
{% endhint %}

### Where to find tokens?

Select **Settings** in the left menu, then API Tokens. You’ll see all active tokens, their creator, and their access level.&#x20;

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FIjRHg8ZYMhuIFtktQHkC%2Fimage.png?alt=media&#x26;token=7596f750-f75e-4e47-a126-99a9c5d30615" alt="" width="563"><figcaption></figcaption></figure></div>

The automatically assigned token per domain is under the Integration tab in Sending Domains. Choose the desired stream, click Integrate, and toggle the switch to API. You'll see the endpoint (Host) and your API Token.

### Reset token

Go to **Settings** > **API Tokens**, click the three-dot menu icon next to the token you want to reset, and click **Reset API Token**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3762cde4a3322e8764196f336b594df6f4ec68c5%2Fapi-tokens-reset-menu-option.png?alt=media" alt="" width="563"></div>

Confirm your choice by clicking on the corresponding button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-25e07ca7578551e8334f73700b5026fa96047780%2Fapi-tokens-reset-confirmation.png?alt=media" alt="" width="563"></div>

{% hint style="success" %}
**Tip:** The three-dot menu icon next to the token also allows you to copy a token to your clipboard.
{% endhint %}

{% hint style="warning" %}
**Important notes:**

* After clicking the Reset credentials or Reset API Token buttons, the existing token becomes invalid after 12 hours. So, you have a 12-hour window to update all apps that use the old API token. Once the old token expires, some parts of your application will not work properly unless you've updated the token. All expired tokens get deleted from your account within 24 hours after expiration.
* After the API token is reset and expired, a new token is created. The token ID is added to the token name the same way it's done for automatically generated tokens, e.g., mailtrap.example token 4231.
  {% endhint %}

### Edit permissions

As mentioned earlier, click the menu icon at the far right of a token and select **Edit permissions**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-532af5c8cd0d2effab0678823088ef476173c267%2Fapi-tokens-edit-permissions-option.png?alt=media" alt="" width="563"></div>

Click on the corresponding boxes to add or remove token permissions. Then, confirm your selection with the **Save** button.

### Delete token

To delete a token, click a three-dot menu icon and choose the **Delete** **token** option.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-51692fed552abdb850f55a54a7bca58cbe023465%2Fapi-tokens-delete-menu-option.png?alt=media" alt="" width="563"></div>

Confirm the action by clicking the **Confirm** button.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-738ea005c1db709ef926c8698ffc7e1a4bbe85b9%2Fapi-tokens-delete-confirmation.png?alt=media" alt=""></div>

{% hint style="warning" %}
**Important:** Keep in mind that a token is deleted immediately, and you can't delete the last token per domain.
{% endhint %}


# SMTP Integration

Integrate Mailtrap SMTP. Get SMTP credentials, choose transactional or bulk sending, use code samples, and start sending.

Learn how to integrate your application via SMTP.

### Locating your Mailtrap credentials

{% stepper %}
{% step %}
Go to the **Sending Domains** tab and choose the domain you want to send emails from.&#x20;

Keep in mind that the [domain must be verified](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) in order for you to start sending emails.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fj54II6e8ZbYkiZQQexIo%2FScreenshot%202026-02-20%20at%2010.26.54.png?alt=media&#x26;token=92eaa47a-8ac3-44a5-ac96-2ca160e48511" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
Navigate to the **Integrations** tab for your selected domain and select whether you want to use our **Transactional Stream** or [**Bulk Stream**](https://docs.mailtrap.io/email-api-smtp/setup/bulk-stream).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fjfo4z0cNdJMgQd6neTYF%2FScreenshot%202026-02-20%20at%2010.29.17.png?alt=media&#x26;token=eabfc395-ca87-4b93-af54-4695b49d79a0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Transactional Stream** is used to send automated, non-promotional application emails that are triggered by the user's specific action.

**Bulk Stream** is used to send a single marketing campaign to a large group of recipients in bulk.
{% endhint %}
{% endstep %}

{% step %}
Once you choose your preferred sending stream, click on **SMTP**. There, you will be able to see your Mailtrap credentials.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FTmpxU5fEpwEv6XlNzp8o%2FScreenshot%202026-02-20%20at%2010.32.53.png?alt=media&#x26;token=1dcac091-2fad-4786-b8f6-2ace52c0515e" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Method #1. Manual SMTP configuration

If you're using a tool like WordPress or Salesforce, you can simply copy/paste credentials such as **Host**, **Port**, **Username**, and **Password**. Here are some examples:

{% tabs %}
{% tab title="WordPress" %}
If you want to send emails from WordPress, you can use one of the many plugins (e.g., WP Mail SMTP or Post SMTP). For example, if you are using WP Mail SMTP, you can just navigate to the settings page and insert the Mailtrap credentials there.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FEgTg65C7yu0i0ZTgwQAJ%2Fwordpress%20smtp.png?alt=media&#x26;token=eb6fbdf7-6411-4c24-a7bd-d92b6af71c12" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Salesforce" %}
To send emails from Salesforce, simply add your Mailtrap credentials to your Email Relay configuration, just like so:

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FALTpCKUPIeFUNezTvq3O%2Fsmtp%20salesforce.png?alt=media&#x26;token=ef03d18c-bfc5-4167-99f1-2ff0ce5de324" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Method #2. Copy/pasting code samples

If you have a programming project, you can also copy/paste one of the pre-made code samples for various programming languages and frameworks. For instance:

{% tabs %}
{% tab title="Nodemailer" %}
For Nodemailer, all you need to do is copy/paste the pre-made transporter object from Mailtrap into your main configuration file (i.e., **index.js**).

```javascript
var transport = nodemailer.createTransport({
  host: "live.smtp.mailtrap.io",
  port: 587,
  auth: {
    user: "api",
    pass: "<YOUR_API_TOKEN>"
  }
});
```

{% endtab %}

{% tab title="Laravel" %}
Similarly, for Laravel, you can just copy the code snippet from Mailtrap into your **.env** file:

```php
MAIL_MAILER=smtp
MAIL_HOST=live.smtp.mailtrap.io
MAIL_PORT=587
MAIL_USERNAME=api
MAIL_PASSWORD=<YOUR_API_TOKEN>
```

{% endtab %}
{% endtabs %}

### Verifying your configuration

Once you add Mailtrap SMTP to your project, try sending an email from the tool of your choice or the project you're working on. If you did everything correctly, you should find the sent email in the inbox of the email address you indicated in the script. The email will also appear in the [Mailtrap Email Logs](https://docs.mailtrap.io/email-api-smtp/analytics/logs).

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FUySCf0dOpk7ltvUZC2aI%2FScreenshot%202026-02-20%20at%2011.06.56.png?alt=media&#x26;token=bef33e3a-f17a-481a-ac62-946fc74f44de" alt=""><figcaption></figcaption></figure>

Remember that each domain has different SMTP credentials that you can always access by clicking on the desired domain and going to the **Integrations** tab.

You can also create additional API tokens (or SMTP passwords) by going to **Settings** → **API Tokens** and clicking **Add Token**.

<a href="api-tokens" class="button primary" data-icon="magnifying-glass">Learn more about API Tokens</a>

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-0232d2eb19e582c06446c68faaba9605af021549%2Fsmtp-tokens-add-token.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
If you need any help with SMTP integration, please, contact our support team at <support@mailtrap.io>.
{% endhint %}


# Bulk Stream

Integrate Mailtrap Bulk Stream via API or SMTP. Get credentials, use SDKs or code samples, and send promotional emails with built-in compliance features.

## What is Bulk Stream?

Bulk Stream is Mailtrap's dedicated infrastructure for sending marketing, promotional, and non-transactional emails. It's designed to handle high-volume email campaigns while maintaining optimal deliverability and compliance with industry standards.

{% hint style="warning" %}
**Important**: Mailtrap requires you to use the Bulk Stream for all marketing and promotional emails. This separation protects your transactional email reputation and ensures compliance with email provider requirements.
{% endhint %}

## Why Use Bulk Stream?

### Suppression list separation

* **We separate suppression by a stream**. So e.g. you use one domain for both transactional and bulk emails and your recipients unsubscribed from bulk email - it won't affect your transactional email.

### Deliverability Protection

Using separate streams for transactional and bulk emails is critical for maintaining high deliverability:

* **Reputation Isolation**: Marketing emails don't affect your transactional email reputation. Ideally you should use a seperate subdomain/domain for your bulk emails.
* **Different IP Pools**: Dedicated IPs for bulk sending
* **Optimized Routing**: Infrastructure optimized for bulk sending patterns
* **Better Inbox Placement**: Proper categorization by email providers

### Automatic Compliance Features

Mailtrap automatically adds required elements to comply with Google, Yahoo, and other major providers' bulk sending requirements:

* **List-Unsubscribe Headers**: One-click unsubscribe functionality
* **List-Unsubscribe-Post Headers**: RFC 8058 compliance
* **Precedence Headers**: Proper bulk email identification
* **Unsubscribe Links**: Automatic footer unsubscribe links when not present

{% hint style="info" %}
**Google Requirements**: Starting February 2024, Gmail requires authentication, easy unsubscribe, and low spam rates for senders of 5,000+ daily emails. Mailtrap's Bulk Stream automatically handles these requirements.
{% endhint %}

## How to Use Bulk Stream

### Key Differences from Transactional Stream

The main difference from a user perspective is the endpoint/host you use:

| Stream        | SMTP Host               | API Base URL                       |
| ------------- | ----------------------- | ---------------------------------- |
| Transactional | `live.smtp.mailtrap.io` | `https://send.api.mailtrap.io/api` |
| Bulk          | `bulk.smtp.mailtrap.io` | `https://bulk.api.mailtrap.io/api` |

**Important**: The API structure and calls remain the same - only the domain changes.

### Using with SDKs

Our official SDKs make it easy to switch between streams:

```javascript
// Node.js SDK example
const { MailtrapClient } = require("mailtrap");

// For bulk emails
const bulkClient = new MailtrapClient({
  token: "your_api_token",
  bulk: true  // This flag switches to bulk stream
});

// Send bulk email
await bulkClient.send({
  from: { email: "marketing@yourdomain.com" },
  to: [{ email: "subscriber@example.com" }],
  subject: "Our Monthly Newsletter",
  html: "<p>Newsletter content...</p>",
  category: "newsletter"  // Categorize for analytics
});
```

## Setup Instructions

{% stepper %}
{% step %}
**Verify Your Sending Domain**

To use Bulk Stream, first verify a domain you own. Go to the Sending Domains tab and click Add Domain. Type your domain name and confirm with the Add button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5d6fa78618fdaf84ed02ab10620c5fe701d525fd%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

Then, add the DNS records Mailtrap provides to your domain provider.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b9aef85e3be109fe33074bfb3d562c9c4ba389db%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

Check our [Sending Domain Setup Guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain) for detailed instructions on adding and verifying your domain.
{% endstep %}

{% step %}
**Integrate Your Application**

**For SMTP Integration**

To send emails via Bulk Stream SMTP, use the bulk-specific credentials:

* **Host**: `bulk.smtp.mailtrap.io`
* **Port**: 587 (or 25, 2525, 465 with SSL)
* **Authentication**: Your stream-specific username and password

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-48c156a7570eeadf78503692946334068ed4b11e%2Fbulk-smtp-credentials.png?alt=media" alt="Bulk Stream SMTP credentials with host, port, username, and password" width="563"></div>

See our [SMTP Integration Guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration) for detailed setup instructions.

**For API Integration**

To send via Bulk Stream API, use the bulk endpoint:

* **Base URL**: `https://bulk.api.mailtrap.io/api`
* **Authentication**: Bearer token (same as transactional)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-953999910745763efe83dc0bdf90222846737bf6%2Fbulk-api-credentials.png?alt=media" alt="Bulk Stream API credentials with host and API token" width="563"></div>

See our [API Integration Guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration) for implementation details.
{% endstep %}
{% endstepper %}

## Bulk Email Best Practices

### Content Guidelines

* Include valuable, relevant content
* Use clear, honest subject lines
* Avoid spam trigger words
* Include your physical mailing address
* Make unsubscribe prominent and functional

### List Management

* Only send to opted-in subscribers
* Implement double opt-in for new subscribers
* Regularly clean your list of inactive users
* Honor unsubscribe requests immediately
* Never purchase email lists

### Sending Patterns

* Start with small volumes and gradually increase
* Maintain consistent sending patterns
* Avoid sudden volume spikes
* Send at optimal times for your audience
* Monitor engagement metrics

## Compliance Information

### Google & Yahoo Requirements (2024)

Starting February 2024, major email providers require:

1. **Authentication**: SPF, DKIM, and DMARC must be properly configured
2. **Easy Unsubscribe**: One-click unsubscribe must be supported
3. **Low Spam Rate**: Keep spam complaints below 0.3%
4. **Valid DNS Records**: Ensure proper forward and reverse DNS

{% hint style="success" %}
**Automatic Compliance**: Mailtrap's Bulk Stream automatically handles authentication headers, unsubscribe mechanisms, and proper email formatting to meet these requirements.
{% endhint %}

### Who is Considered a Bulk Sender?

According to Google's guidelines:

* Any sender reaching **5,000+ messages** to Gmail accounts within 24 hours
* Counted across all subdomains of your primary domain
* Once classified as bulk sender, the designation is permanent

### What Mailtrap Adds Automatically

When using Bulk Stream, Mailtrap automatically includes:

```
List-Unsubscribe: <mailto:unsubscribe@yourdomain.com>, <https://yourdomain.com/unsubscribe?id=xyz>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
Precedence: bulk
```

Plus, if no unsubscribe link is detected in your HTML, we add a compliant footer:

```html
<div style="text-align: center; margin-top: 20px;">
  <a href="__unsubscribe_url__">Unsubscribe</a> |
</div>
```

## Monitoring and Analytics

### Track Performance

* **Delivery Rate**: Monitor successful deliveries
* **Open Rate**: Track email engagement
* **Click Rate**: Measure content effectiveness
* **Bounce Rate**: Identify delivery issues
* **Spam Complaints**: Stay below 0.3% threshold
* **Unsubscribe Rate**: Monitor list health

### Use Email Categories

Categorize your bulk emails for better analytics:

```javascript
// API example with category
{
  "category": "newsletter",  // or "promotion", "announcement", etc.
  "custom_variables": {
    "campaign_id": "summer_2024",
    "segment": "active_users"
  }
}
```

## FAQ

<details>

<summary>Can I use the same API token for both streams?</summary>

Yes, your API token works for both Transactional and Bulk streams. Only the endpoint URL changes.

</details>

<details>

<summary>What happens if I send marketing emails through the Transactional stream?</summary>

This can harm your transactional email deliverability and may result in account warnings. Always use Bulk Stream for marketing emails.

</details>

<details>

<summary>Do I need separate domain verification for Bulk Stream?</summary>

No, once your domain is verified in Mailtrap, it works for both streams. However, you might want to use subdomains (e.g., marketing.yourdomain.com) for better reputation management.

</details>

<details>

<summary>How do I handle unsubscribes?</summary>

Mailtrap automatically adds unsubscribe headers and can manage suppressions. You can also implement your own unsubscribe handling via webhooks.

</details>

<details>

<summary>What's the sending limit for Bulk Stream?</summary>

Limits depend on your plan. Start with gradual volume increases to build reputation. Contact support for high-volume needs.

</details>

## Related Resources

* [**Email Deliverability Guide**](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/setup/broken-reference/README.md) - Essential reading for bulk senders
* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [Email Templates](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates)
* [Suppressions List](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/suppressions-list)
* [Email Categories](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/categories)
* [IP Warmup](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/ip-warmup)
* [Google's Email Sender Guidelines](https://support.google.com/mail/answer/81126)


# Sending Limits

Learn Mailtrap email sending limits: hourly, daily, connection, and email size. Understand what happens when limits are reached and how to upgrade.

When you first sign up for Mailtrap, we limit your throughput to 150 emails an hour. This is a security measure to prevent abusing our system for spam.

You can raise the hourly limit by upgrading to a one of our [paid plans](https://mailtrap.io/pricing/), which starts at 600 or even 800 emails per hour. Later on, our automation will proactively raise your limit if you're nearing it. For an even higher limit, you can submit a request to our support team.

{% hint style="warning" %}
Mailtrap Support team can set hourly limit depending on your needs.

It's a soft limit we are ready to adjust for your depending on your needs and usage.
{% endhint %}

If you try to send more emails than your hourly limit allows, the extra emails will be queued and sent in the next hours.

{% hint style="info" %}
Note: There are no hourly limits for Email Campaigns.
{% endhint %}

## Daily Limits

We have a daily limit of 150 emails/day only for our Free plan, which lets you send up to 4,000 emails per month. Emails sent over this limit will be rejected and won't be sent. There are no daily limits on paid plans.

Need to send more? Upgrade to a paid plan!

## Connection Limits

The maximum number of concurrent SMTP connections **per account** is 10.

If you exceed this limit, you'll get the following error:

```
535 5.7.8 Too many connections per account
```

The maximum number of concurrent SMTP connections **per IP** is 10.

The maximum number of messages per 1 SMTP connection is 100.

{% hint style="success" %}
If those limits are not enough, please let us know by contacting our Support Team. Limits can be adjusted only for paid plans.
{% endhint %}

## Email Size

The maximum allowed size of each email message, including attachments, is 10 MB in all plans by default. In Business and higher plans it's possible to increase size up to 30 MB by contacting our Support team.


# Email Templates

Create and send Mailtrap email templates with drag-and-drop builder or HTML editor, add Handlebars variables, and integrate via API or SMTP.

### Overview

Email Templates allow you to design, edit, and host HTML email templates, and reference them via API.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9ff933e3fb8c346003904bf50374326db5d665cf%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

By storing the template on Mailtrap and calling it via API, you can easily change the template code without committing to your codebase.

Email Templates support Variables, and Mailtrap uses Handlebars as a template engine.

You can put {{user\_name}} into your template and pass "John" as the "user\_name" value via API.

For a complete guide on using Handlebars with email templates, see [Handlebars Guide](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/handlebars).

### Creating a template

{% stepper %}
{% step %}
Navigate to the **Templates** menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-472bf2d946c91f5f5d547e55913798aaa2fda7f6%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the **Create New Template** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-08c42f957e72d0bf718a9b46f35119e185237472%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click the drop-down menu to select one of your domains, enter the **Template name**, **Subject**, and **Category**, and click **Continue**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e305265aa6521ed901e2095b7037b3d0b50ab2eb%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Choose the **Drag & Drop Editor** to build the template without coding, or select **HTML Editor** if you prefer to write/modify the code.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f56822fb58761484b716c51f934ff2c46dc90448%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Create/modify the design and click **Finish**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-04acabe528652a54e28c38bb6295c6ee24da3316%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

The main **Templates** menu features all your saved templates. To quickly access a saved template, just click on it within the main menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bb74cbc0483f284c95a1cceebe12226f7e22d94c%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Managing templates

#### List of templates and user permissions

Clicking on Templates in the side menu lists all the templates you can access. Access to templates is managed on a domain level. You need to have Admin access to a domain to manipulate the templates. In case you don't have Edit rights, you can't change the template. Each account can have up to 200 email templates.

{% hint style="warning" %}
You can delete a template. However, this action is irreversible, so be sure to change the sending/testing code after deletion. When the template is deleted, the UUID is also deleted, and Mailtrap won't be able to render it.
{% endhint %}

### Next steps

* [Editing and Customizing Templates](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/editing-and-customizing) - Learn how to customize templates with the Drag & Drop or Code Editor
* [Handlebars Guide](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/handlebars) - Complete guide to using Handlebars syntax in templates
* [Integration](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/integration) - Integrate templates with Email API/SMTP
* [Debugging](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/debugging) - Test templates with Email Sandbox


# Editing and Customizing

Learn how to edit and customize email templates using Details, Drag & Drop Editor, Code Editor, and test your templates.

### Details

Each template must have a name, subject, category, and assigned domain. The subject also supports variables.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-940dfd68b21c2a101059dfadfcb7857e371653bd%2Ftemplate-details-view.png?alt=media" alt="Template Details page showing domain, name, subject, and category fields in a bordered section" width="563"><figcaption><p>Template details section</p></figcaption></figure></div>

### Drag & Drop Editor

The drag-and-drop editor allows you to design templates without any coding.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d113e67ef60ce61aa373995bd7d775b5750784f0%2Ftemplate-drag-drop-interface.png?alt=media" alt="Drag and Drop Editor interface showing template preview in center with blocks and content options on right sidebar" width="563"><figcaption><p>Drag and Drop Editor</p></figcaption></figure></div>

### Code Editor

Code Editor allows you to edit the HTML or Text content, depending on the emails you want to send.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a13a7256fbeafc8cc946b9b71c1115bb07b93ba7%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

The editor supports Find and Replace options, and you can use Cmd+F or Win+F as a hotkey to reveal a quick search bar.

If your template has an error, Handlebars cannot render it. You'll see an error message in the Preview tab, and the RAW code with an error will be highlighted in the Editor.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-403e2b462026d23199f72e547fbb1576c88ac32b%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

You can't save a template with errors, either. Remember that we don't validate HTML.

### **Uploading an image**

{% stepper %}
{% step %}
Click Upload image in the upper right corner of the Code Editor.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1c636a6f212f1eb0016484ce6996e33e23f26483%2Ftemplate-upload-image-button.png?alt=media" alt="Code Editor with Upload image button highlighted in upper right corner" width="375"><figcaption><p>Upload image button in Code Editor</p></figcaption></figure></div>
{% endstep %}

{% step %}
Hit the Upload New button in the following menu and choose an image from your local drive (Supported formats are JPG, PNG, and GIF, and the maximum file size is 2 MB).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-af66650da784a3ba3a9591ad8626cd93605e92bd%2Ftemplate-images-library.png?alt=media" alt="Images library page showing Upload New button highlighted in top right" width="563"><figcaption><p>Images library with Upload New button</p></figcaption></figure></div>
{% endstep %}

{% step %}
Once the image is uploaded, you will receive a confirmation notification. If the file format is unsupported or the image is too big, you will receive the corresponding error message.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3c240eac8ce9ee4922028a23cf32b616a4143cdb%2Ftemplate-image-upload-success.png?alt=media" alt="Success notification showing Image successfully uploaded message in green banner" width="563"><figcaption><p>Image upload success notification</p></figcaption></figure></div>
{% endstep %}

{% step %}
Click the Copy URL button to copy the image URL to your clipboard, then click Template to return to the editing menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8c33d18b581f860bb20fc7f11d661cd63c758472%2Ftemplate-copy-url-button.png?alt=media" alt="Images library showing uploaded images with Copy URL button highlighted" width="563"><figcaption><p>Copy URL button for uploaded images</p></figcaption></figure></div>
{% endstep %}

{% step %}
Proceed to add the image to the template body under the `<img>` tag. You can preview it in the template as soon as the asset is added.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2226ade6f36bc2deb1d039dffcc6394e93093a54%2Ftemplate-image-in-code.png?alt=media" alt="HTML code showing image URL inserted in img src attribute with highlighted code" width="375"><figcaption><p>Image URL added to template HTML</p></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### **Test Data**

Code Editor automatically parses your template and shows all the variables found. The Test Data tab helps you preview the object variables.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58f9d403a4f9289176f7a2b14d0712c9b5a802f1%2Ftemplate-test-data-variables.png?alt=media" alt="Test Data tab showing template variables with test values and preview" width="563"><figcaption><p>Test Data tab with template variables</p></figcaption></figure></div>

By default, as a value, we put a variable name and add the "Test\_" prefix.

### Send test

If you're using email templates in production, you can send a test email to the account owner's email address to run basic tests. Simply press the Send Test button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e656b0110b9272cc878ad6e33ac0a35c9c24a4ea%2Ftemplate-send-test-button.png?alt=media" alt="Template editor showing Send Test button highlighted in top right" width="563"><figcaption><p>Send Test button</p></figcaption></figure></div>

Important Notes:

* Your domain should be verified to send a test.
* Each test email is billed over your quota.

### Next steps

* [Handlebars Guide](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/handlebars) - Learn how to use Handlebars syntax to add dynamic content
* [Integration](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/integration) - Integrate templates with Email API/SMTP
* [Debugging](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/debugging) - Test templates with Email Sandbox


# Handlebars Guide

Complete guide to using Handlebars templating language with Mailtrap Email Templates, including syntax examples, helpers, and practical use cases.

Mailtrap Email Templates support the Handlebars templating language. It combines an input object (JSON) and a template to create text formats, HTML, or an email subject.

You can use Handlebars syntax to personalize your email templates and insert specific information for each of your recipients.

For instance, you may have a client business name called "business name" under a JSON object property. Then, using `{{business name}}` Handlebars expression somewhere in the template, you can insert the property value to an email template.

The main benefit of using this syntax is that you don't have to update your code base. The dynamic templating happens fast and outside the code base.

### Supported Handlebars features

Handlebars supports a bunch of features, not just the variable replacement. Mailtrap templates support the standard set of helpers:

* **Basic replacement**
* **Conditional statements**: `{{#if}}`, `{{#unless}}`, `{{#each}}`, and `{{#with}}`

The following sections give you examples for each of the helpers including code blocks, mock JSON data, and HTML output.

### Basic replacement

The basic usage is just to render the values you pass. You can use objects and refer to variables like `{{object_name.variable}}`.

If the variable is present in the data you pass, it won't be rendered.

If you want to do a replacement with HTML, use triple brackets `{{{value_with_html}}}`.

**Template**

```html
<p>Hello {{firstName}} {{lastName}}!</p>
<p>Click this <a href="{{url}}">link</a></p>
<p>{{company.name}}, {{company.adress}}</p>
<p>{{{signature}}}</p>
```

**JSON Object**

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "url": "http://example.com",
  "company": {
    "name": "Best Company",
    "adress": "Its Address"
  },
  "signature": "<strong>thanks!<strong>"
}
```

**HTML output**

```html
<p>Hello John Smith!</p>
<p>Click this <a href="http://example.com">link</a></p>
<p>Best Company, Its Address</p>
<p><strong>thanks!<strong></p>
```

### Conditional Statements

#### if / else / if else

Use the `if` helper for conditional block rendering.

{% hint style="info" %}
Should the argument return `""`, `0`, `nil`, `false`, `empty_map`, `empty_slice`, or an `empty_array`, then the block won't be rendered.
{% endhint %}

**Template**

```html
{{#if user.isSubscribed}}
  <p>Hello {{user.name}},</p>
  <p>Thank you for subscribing to our newsletter!</p>
{{else}}
  <p>Hello {{user.name}},</p>
  <p>We noticed that you have not yet subscribed to our newsletter. Click <a href='#'>here</a> to subscribe.</p>
{{/if}}
```

**JSON test data**

```json
{
  "user": {
    "name": "Jane Doe",
    "isSubscribed": true
  }
}
```

**HTML email output**

```html
  <p>Hello Jane Doe,</p>
  <p>Thank you for subscribing to our newsletter!</p>
```

If you change the `isSubscribed` variable to `false` in JSON data, the HTML output is:

```html
  <p>Hello Jane Doe,</p>
  <p>We noticed that you have not yet subscribed to our newsletter. Click <a href='#'>here</a> to subscribe.</p>
```

{% hint style="info" %}
The examples above include both `if` and `else` expressions. Of course, you can use only `if`, but it's recommendable to include `else` as well to cover the scenario where a conditional statement is `false`.
{% endhint %}

#### unless

The `unless` block helper works like an inverse `if`. Simply put, it renders when the expression returns a `false` value.

**Template**

```html
{{#unless user.isSubscribed}}
  <p>Hello {{user.name}},</p>
  <p>We noticed that you have not yet subscribed to our newsletter. Click <a href='#'>here</a> to subscribe.</p>
{{else}}
  <p>Hello {{user.name}},</p>
  <p>Thank you for subscribing to our newsletter!</p>
{{/unless}}
```

**JSON test data**

```json
{
  "user": {
    "name": "Jane Doe",
    "isSubscribed": false
  }
}
```

**HTML email output**

```markup
<p>Hello Jane Doe,</p>
<p>We noticed that you have not yet subscribed to our newsletter. Click <a href='#'>here</a> to subscribe.</p>
```

The block helper example also contains `{{else}}` and should the `isSubscribed` variable be `true`, here's the HTML output:

```markup
  <p>Hello Jane Doe,</p>
  <p>Thank you for subscribing to our newsletter!</p>
```

#### each

The `{{#each}}` helper is used to iterate over an object or array, then execute a block of code for each item.

In the example below, `{{#each user.items}}` iterate over the `user.items` array, then execute the code inside the block.

{% hint style="info" %}
`{{this}}` helper is used as a reference to the current item in the iteration.
{% endhint %}

**Template**

```html
{{#each user.items}}
  <p>Item: {{this}}</p>
{{/each}}
```

**JSON test data**

```json
{
  "user": {
    "name": "Jane Doe",
    "items": ["Item 1", "Item 2", "Item 3"]
  }
}
```

**HTML email output**

```html
  <p>Item: Item 1</p>
  <p>Item: Item 2</p>
  <p>Item: Item 3</p>
```

**Template with else block**

```html
{{#each user.items}}
  <p>Item: {{this}}</p>
{{else}}
  <p>No items found</p>
{{/each}}
```

**JSON test data**

```json
{
  "user": {
    "name": "Jane Doe",
    "items": []
  }
}
```

**HTML email output**

```html
<p>No items found</p>
```

#### with

You can use the `with` helper to change the context in which the code block gets executed.

In the example below, the `{{with user}}` block sets the context for the user object. Consequently, the `{{name}}` and `{{email}}` can be accessed directly. This is useful when you want to avoid writing long chains of nested property accessors.

**Template**

```html
{{#with user}}
  <p>Name: {{name}}</p>
  <p>Email: {{email}}</p>
{{/with}}
```

**JSON test data**

```json
{
  "user": {
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
}
```

**HTML email output**

```markup
<p>Name: Jane Doe</p>
<p>Email: jane.doe@example.com</p>
```

**Template with else block**

In the example below, the `{{else}}` clause only gets executed if there's no value within the `{{with}}` block.

```markup
{{#with user}}
  <p>Name: {{name}}</p>
  <p>Email: {{email}}</p>
{{else}}
  <p>No user found</p>
{{/with}}
```

**JSON test data**

```json
{
  "user": null
}
```

**HTML email output**

```markup
<p>No user found</p>
```

### Example: Order confirmation template

The following example contains the majority of Handlebars helpers explained above as well as mock JSON data, and HTML output.

**Email template in HTML:**

```html
<html>
  <body>
    <h1>Order Confirmation</h1>
    <p>Hello {{customer.name}},</p>
    <p>Thank you for your order! Your order number is {{order.number}}.</p>
    <p>Your order details are:</p>
    <table>
      <thead>
        <tr>
          <th>Product</th>
          <th>Quantity</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {{#each order.items}}
        <tr>
          <td>{{name}}</td>
          <td>{{quantity}}</td>
          <td>${{price}}</td>
        </tr>
        {{/each}}
      </tbody>
    </table>
    <p>Shipping to:</p>
    <address>
      {{#with customer.address}}
        {{#if company}}
          {{company}}<br>
        {{/if}}
        {{firstName}} {{lastName}}<br>
        {{street}}<br>
        {{city}}, {{state}} {{zip}}<br>
        {{country}}
      {{/with}}
    </address>
    <p>Your order will be shipped {{#unless order.isRush}}within 3-5 business days{{else}}within 24 hours{{/unless}}.</p>
    <p>Total: ${{order.total}}</p>
    <p>Thank you for shopping with us!</p>
  </body>
</html>
```

**Mock JSON data:**

```json
{
  "customer": {
    "name": "John Smith",
    "address": {
      "company": "My company",
      "firstName": "John",
      "lastName": "Smith",
      "street": "123 Main St",
      "city": "Anytown",
      "state": "State",
      "zip": "ZIP",
      "country": "USA"
    }
  },
  "order": {
    "number": "123456",
    "items": [
      {
        "name": "Product 1",
        "quantity": "1",
        "price": "10"
      },
      {
        "name": "Product 2",
        "quantity": "2",
        "price": "20"
      }
    ],
    "isRush": true,
    "total": 50
  }
}
```

**HTML email output:**

```html
<html>
  <body>
    <h1>Order Confirmation</h1>
    <p>Hello John Smith,</p>
    <p>Thank you for your order! Your order number is 123456.</p>
    <p>Your order details are:</p>
    <table>
      <thead>
        <tr>
          <th>Product</th>
          <th>Quantity</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Product 1</td>
          <td>1</td>
          <td>$10</td>
        </tr>
        <tr>
          <td>Product 2</td>
          <td>2</td>
          <td>$20</td>
        </tr>
      </tbody>
    </table>
    <p>Shipping to:</p>
    <address>
      My company<br>
      John Smith<br>
      123 Main St<br>
      Anytown, State ZIP<br>
      USA
    </address>
    <p>Your order will be shipped within 24 hours.</p>
    <p>Total: $50</p>
    <p>Thank you for shopping with us!</p>
  </body>
</html>
```

### Testing templates with Handlebars

In the quick tutorial below, we assume you've activated both Email Sandbox and Email API/SMTP.

{% stepper %}
{% step %}
Navigate to **Email API/SMTP** > **Email Templates** in the menu on the left.
{% endstep %}

{% step %}
Select your email template and click the **Integration** tab.
{% endstep %}

{% step %}
Copy the code under the **Integration** tab (cURL, or any other based on your preference).

To test the template, you only need to change the Sending API endpoint ([send.api.mailtrap.io](http://send.api.mailtrap.io/)) to Sandbox API ([sandbox.api.mailtrap.io](http://sandbox.api.mailtrap.io/)) and add the `inbox_id` to the end of the endpoint URL.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-de8c7136039e15eb13f39177eac503126e90dee7%2Ftemplate-stream-options.png?alt=media" alt="Integration page showing Transactional Stream and Bulk Stream options with Integrate buttons highlighted by red arrows" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Run the template test and check the associated inbox to preview the template under sandbox.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-88505e24bb75c8852b93a6b20042f3fd6b186606%2Ftemplate-test-email-received.png?alt=media" alt="Email Testing sandbox showing received test email with template content" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

**Important notes:**

* Pay attention that the `Authorization: Bearer` (API token) token is related to the Inbox you're targeting. You can check (and copy-paste) the token under Settings > API Tokens.
* Your `inbox_id` is in the Inbox URL.

For more details on template debugging, see [Debugging](https://docs.mailtrap.io/documentation/email-api-smtp/email-templates/debugging).


# Integration

Learn how to integrate Mailtrap email templates with Email API/SMTP using Transactional or Bulk streams.

### Overview

Once you've created and customized your email template, you can integrate it with your application using the Email API or SMTP. This guide shows you how to get the necessary credentials and code samples to send emails using your templates.

### Integration steps

{% stepper %}
{% step %}
Navigate to Templates in the menu on the left.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d4b58986a09646ee33096aceec07e1af772c471a%2Ftemplate-menu-nav.png?alt=media" alt="Mailtrap sidebar menu with Templates menu item highlighted by red arrow" width="375"><figcaption><p>Templates in navigation menu</p></figcaption></figure></div>
{% endstep %}

{% step %}
Click the template you want to call using the API.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8e27873c5eca3dc3ff209d4d535f0f20a9f73e9a%2Ftemplate-list-view.png?alt=media" alt="Templates list showing Newsletter template highlighted by red arrow" width="563"><figcaption><p>Select template from list</p></figcaption></figure></div>
{% endstep %}

{% step %}
Open the Integration tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-297f15ee561555c6f584050e24c7d81749233721%2Ftemplate-integration-tab.png?alt=media" alt="Template page showing Details and Integration tabs with Integration tab highlighted by red arrow" width="563"><figcaption><p>Open Integration tab</p></figcaption></figure></div>
{% endstep %}

{% step %}
With Email API/SMTP toggled on, click Integrate under Transactional Stream or Bulk Stream.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-de8c7136039e15eb13f39177eac503126e90dee7%2Ftemplate-stream-options.png?alt=media" alt="Integration page showing Transactional Stream and Bulk Stream options with Integrate buttons highlighted by red arrows" width="375"><figcaption><p>Choose stream type and click Integrate</p></figcaption></figure></div>
{% endstep %}

{% step %}
Copy the necessary credentials such as Host, API Token, and Template UUID.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-277ed4a03452a3091f2067afa8e3078df3030ed6%2Fapi-integration-credentials-transactional.png?alt=media" alt="Transactional Stream API credentials box showing Host, API Token, and Template UUID" width="375"><figcaption><p>Transactional Stream API credentials</p></figcaption></figure></div>

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-60ba1ceace0286cee9131e3d55845680d4d5e20e%2Fapi-integration-credentials-bulk.png?alt=media" alt="Bulk Stream API credentials box showing Host, API Token, and Template UUID" width="375"><figcaption><p>Bulk Stream API credentials</p></figcaption></figure></div>
{% endstep %}

{% step %}
Alternatively, under Code Samples, choose the desired language and copy the sample configuration already containing the necessary credentials. Mailtrap's official SDKs ([Node.js](https://github.com/railsware/mailtrap-nodejs), [Python](https://github.com/railsware/mailtrap-python), [PHP](https://github.com/railsware/mailtrap-php), and [Ruby](https://github.com/railsware/mailtrap-ruby)) also support the templates feature.
{% endstep %}

{% step %}
Paste the code into your project and customize it if needed. Then, run the code to send an email to the email address you indicated in your script.

For more details, [open the API docs](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api) and go to Email Sending API → Emails → Send email (including template) for transactional stream and Bulk Sending API → Emails → Send email (including template) for bulk stream. Under Body, click the dropdown menu, and choose `EmailFromTemplate`.
{% endstep %}
{% endstepper %}


# Debugging with Sandbox

Learn how to test and debug your email templates using Mailtrap Email Sandbox.

### Overview

Before sending your email templates to production, it's important to test them in a safe environment. Mailtrap Email Sandbox allows you to test your templates, preview how they render, and verify that all variables are working correctly.

### Debugging steps

{% stepper %}
{% step %}
Navigate to Templates in the menu on the left.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d4b58986a09646ee33096aceec07e1af772c471a%2Ftemplate-menu-nav.png?alt=media" alt="Mailtrap sidebar with Templates menu item highlighted by red arrow" width="375"><figcaption><p>Navigate to Templates</p></figcaption></figure></div>
{% endstep %}

{% step %}
Click the template you want to call using the API.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8e27873c5eca3dc3ff209d4d535f0f20a9f73e9a%2Ftemplate-list-view.png?alt=media" alt="Templates list showing Newsletter template highlighted by red arrow" width="563"><figcaption><p>Select template to debug</p></figcaption></figure></div>
{% endstep %}

{% step %}
Open the Integration tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-297f15ee561555c6f584050e24c7d81749233721%2Ftemplate-integration-tab.png?alt=media" alt="Template page showing Details and Integration tabs with Integration tab highlighted by red arrow" width="563"><figcaption><p>Open Integration tab</p></figcaption></figure></div>
{% endstep %}

{% step %}
Toggle the switch to Email Testing.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a2ddf21275dd23fa7abb84d23afc7a20ab5a48da%2Ftemplate-email-testing-toggle.png?alt=media" alt="Integration page with Email Testing toggle highlighted by red arrow" width="375"><figcaption><p>Toggle to Email Testing</p></figcaption></figure></div>
{% endstep %}

{% step %}
And click Integrate.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-558189239e819805d79ca1b0341d8af6cf25030b%2Ftemplate-testing-inbox-integrate.png?alt=media" alt="Testing Inbox card with Integrate button highlighted by red arrow" width="375"><figcaption><p>Click Integrate for Testing Inbox</p></figcaption></figure></div>
{% endstep %}

{% step %}
Select the desired sandbox from the dropdown menu to reveal its credentials. Copy the Host, API Token, Template UUID, and Sandbox ID.

Alternatively, you can also use one of the pre-made Code Samples.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b38cabbabb625c845c08d07152235ac12c089ef4%2Ftemplate-sandbox-credentials.png?alt=media" alt="Sandbox integration showing API credentials and code samples with sandbox dropdown" width="563"><figcaption><p>Sandbox credentials and code samples</p></figcaption></figure></div>
{% endstep %}

{% step %}
Paste the code into your project and customize it if needed. Then, run the code to send an email to the selected Email Testing sandbox.
{% endstep %}

{% step %}
Finally, check the sandbox you specified in the script.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-88505e24bb75c8852b93a6b20042f3fd6b186606%2Ftemplate-test-email-received.png?alt=media" alt="Email Testing sandbox showing received test email with template content" width="563"><figcaption><p>Test email received in sandbox</p></figcaption></figure></div>

The Tech Info tab contains the link to the template you tested and lists all the variables used in the template.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-63682ff6247b69e0210eb3acd1d8b547c72ed85a%2Ftemplate-tech-info-variables.png?alt=media" alt="Tech Info tab showing template link and variables used in the email" width="563"><figcaption><p>Tech Info tab with template details</p></figcaption></figure></div>

For more details, [open the API docs](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/5tjdeg9545058-mailtrap-api) and go to [Sandbox API](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-email-testing-api) → Test Emails → Send email (including templates). Under Body, click the dropdown menu, and choose `EmailFromTemplate`.
{% endstep %}
{% endstepper %}


# Analytics & Reports

Learn what statistics Mailtrap provides: Stats dashboard, Email logs, Email categories, Mailbox providers.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td><strong>Stats Dashboard</strong></td><td><em>check the analytics for all the emails you send</em></td><td><a href="analytics/dashboard">dashboard</a></td><td></td></tr><tr><td><strong>Email Logs</strong></td><td><em>include the status of each message, its preview, events history, HTML source, and statistics</em></td><td><a href="analytics/logs">logs</a></td><td></td></tr><tr><td><strong>Email Categories</strong></td><td><em>performance of various types of emails, such as welcome emails, billing emails, confirmation emails, etc</em></td><td><a href="analytics/categories">categories</a></td><td></td></tr><tr><td><strong>Mailbox Providers</strong></td><td><em>check the deliverability stats using filters such as Domains, Mailbox Providers, and Categories</em></td><td><a href="analytics/mailbox-providers">mailbox-providers</a></td><td></td></tr><tr><td><strong>Statuses and Events</strong></td><td><em>the latest delivery status of an email, each status bears a distinct color, and an email can only have one status at a time</em></td><td><a href="analytics/statuses-and-events">statuses-and-events</a></td><td></td></tr></tbody></table>


# Stats Dashboard

Understand Mailtrap stats dashboard: delivery, open, click, bounce, and spam rates. Learn about domain filtering, warning thresholds, and metric calculations.

Mailtrap provides analytics for all the emails you send.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-947c0d824bc69ef1d85cf08381d99d272d0532b9%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

On the statistics dashboards, you can see the following metrics:

* Delivered emails
* Unique open rate
* Click rate
* Bounce rate
* Spam complaints

### **Navigating around the statistics dashboards**

In that **Stats** tab, you'll find a domain selector at the top of the page. Here, you can choose to show stats for a particular domain.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5755e8c9559bc9694cc71736265638bf64d2eb16%2Fstats-domain-selector.png?alt=media" alt="" width="226"></div>

By default, the stats are shown for the last week + today.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-6b4113678a9f6348d8851acd6eab0ce522aad968%2Fstats-mailbox-providers-overview.png?alt=media" alt="" width="563"></div>

### **Thresholds**

The thresholds are based on our extensive cross-industry research and, at this point, can’t be edited. The current values are:

* For bounce rate:
  * 2-5% is a warning level (yellow)
  * \>5% is a critical level (red)
* For spam rate:
  * 0.08%-0.1% is a warning level (yellow)
  * \>0.1% is a critical level (red)

### **Terminology**

#### **Delivered**

Delivered refers to the percentage of emails that were accepted by the recipient’s mailbox providers compared to all emails sent. Email is counted as delivered when a Delivery event is recorded in its Event History in [Email Logs.](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/logs)

{% hint style="info" %}
"**Delivered**" status doesn't mean that a message went straight into the recipient's Primary folder. It may have still gone into Promotions and Updates, or it might have been automatically put into a Spam folder.
{% endhint %}

Mailtrap will reject an email if a recipient is on a suppression list for a given domain. Read more about [Suppressions](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/suppressions-list).

On top of that, an email can be rejected on the recipient’s end for various reasons:

* A message is considered spam, phishing, or other foul play.
* A security policy on the recipient’s end dictates that a message should be declined.
* A server timeout occurs (in such case, Mailtrap will retry the delivery 10 times until it eventually gives up).
* Email authentication protocols (SPF, DKIM, DMARC) fail.

#### **Unique open rate**

Unique open rate refers to the percentage of emails that were opened at least once compared to all emails sent.

Open tracking needs to be enabled for a domain in question in the Sending Domains tab. Only then will email opens be recorded.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8e0c6d8e4226f3cc705c9488f9b4ebf7c101444e%2Fstats-tracking-settings.png?alt=media" alt="" width="563"></div>

#### **Click rate**

Click rate refers to the percentage of emails that received at least one link click compared to all delivered emails.

When any of the links in an email are clicked, a **click** event is recorded. The same happens for any further clicks, even if a recipient keeps clicking on the same or different links.

You can see the details of each click (timestamp, Recipient's IP, URL) in the **Events History** in the **Email Logs**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-91c441d361c53c662b6b10d8ede7254519350b79%2Fstats-click-events-history.png?alt=media" alt="" width="292"></div>

However, the metrics such as **clicked** and **click rate** used in the statistics are calculated differently.

**Clicked** metric indicates how many emails received at least one click on.

The **click rate** is basically clicked/delivered \* 100%.

#### **Bounce rate**

Bounce rate refers to the percentage of emails dispatched from Mailtrap that were rejected on the recipient’s end compared to all emails sent.

Emails may bounce for different reasons, most commonly:

* Invalid email address.
* Rejection by the recipient’s mailbox because email is deemed spam, phishing, etc.
* The security policy of a mailbox provider that rejects emails from all or some domains.
* Permanent connection issue.

The term bounce used in Mailtrap is also known as a hard bounce. This is different from a soft bounce - another event present in Mailtrap that refers to a temporary delivery problem.

If an email soft bounces, Mailtrap will try to deliver it 10 more times. If there’s no positive outcome, an email will (hard) bounce and get counted towards the bounce rate.

#### **Spam complaints**

Spam complaints refer to the percentage of emails that are reported as spam by recipients, as compared to all emails that were delivered.


# Email Logs

Understand Mailtrap email logs: search and filter sent emails by status, events, and provider. View event history, previews, HTML source, and spam analysis.

It’s a place to view all the emails sent from your account, along with their corresponding details. These include the status of each message, its preview, event history, HTML source, and statistics.

#### How to use filters in Email Logs

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-02734628302342b3067b49762d277a3a813602b5%2Femail-logs-filter-tabs.png?alt=media" alt="" width="375"></div>

These filters are a quick way to find:

* **Bounces** — All emails that were not accepted by the recipient’s mailbox provider (for any reason).
* **Spam** — All emails that were reported as spam by the recipients (this does not include emails that landed in the recipients’ spam folders).
* **Google** — All emails that were sent to free Gmail accounts.
* **Google Workspace** — All emails sent to mailboxes using Google Workspace, the paid version of Gmail used by businesses and organizations.
* **Outlook** — All emails that were sent to Outlook.com mailboxes.
* **Office 365** — All emails that were sent to Office 365 mailboxes.
* **Yahoo** — All emails that were sent to Yahoo mailboxes.

{% hint style="info" %}
When an email is sent, Mailtrap doesn't yet know which Mailbox Provider (e.g., Google, Outlook, Hotmail, etc.) it sent a message to. It's only able to determine this when it receives a response from the recipient's Mailbox Provider, which may sometimes take a few minutes.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5c8e19030c6246c26b174f4d5accec68cf905a29%2Femail-logs-date-picker.png?alt=media" alt="" width="375"></div>

The number of days Mailtrap stores email logs depends on your [billing plan](https://mailtrap.io/pricing/).

#### Understanding the filters

If you prefer to set up your filters manually, you have plenty of options at your disposal. Here’s what you can filter by:

<table data-header-hidden><thead><tr><th width="206.75"></th><th width="291.34375"></th><th></th></tr></thead><tbody><tr><td><strong>Criteria</strong></td><td><strong>What is it?</strong></td><td><strong>Example operator and value</strong></td></tr><tr><td>Email to</td><td>Email address of a recipient, the <code>To:</code> header of a message.</td><td>Is: john.doe@mailtrap.io</td></tr><tr><td>Email from</td><td>Email address a message is sent from, the <code>From:</code> header of a message. Can be used to find messages sent from a specific domain.</td><td>Is: marketing@mailtrap.io</td></tr><tr><td>Subject</td><td>Subject line of a message. The value is not case-sensitive.</td><td>Contains: Product Update</td></tr><tr><td>Status</td><td>The current state of an email.</td><td>Is: Delivered, Not delivered, Enqueued, Opted Out</td></tr><tr><td>Events</td><td>An action that occurred to an email before, during, or after delivery. An email can have multiple events associated with it.</td><td>Include: Sending, Delivery, Open</td></tr><tr><td>Number of clicks</td><td>The total count of clicks that links in an email received. Click tracking must be enabled for clicks to be counted.</td><td>Greater than: 3</td></tr><tr><td>Number of opens</td><td>The total number of times that an email was opened. <em>Note</em>: some mailbox providers, browsers, or extensions can block tracking, which will affect the results. Open tracking must be enabled for opens to be counted.</td><td>Is: 2</td></tr><tr><td>Client sending IP</td><td>IP of a device (e.g., your computer) that an email was sent from.</td><td>Is: 107.177.200.201</td></tr><tr><td>Mailtrap sending IP</td><td>IP that Mailtrap used to send an email.</td><td>Is not: 34.193.89.247</td></tr><tr><td>Full response from the Mailbox provider server</td><td>The response Mailtrap received when an email failed to be delivered or when a soft bounce was recorded.</td><td>Contains: The email account that you tried to reach does not exist.</td></tr><tr><td>Mailbox provider server type</td><td>The name of the recipient’s mailbox provider. Available once an email is delivered or a response about a failed delivery is received.</td><td>Is: Proton Mail</td></tr><tr><td>Mailbox provider server raw</td><td>The name of the recipient’s mailbox provider, as specified in their MX record.</td><td>Contains: gmail-smtp-in.l.google.com</td></tr><tr><td>Categories</td><td>The category specified in the “X-MT-Category” header of an email.</td><td>Contains: Newsletter</td></tr></tbody></table>

You can combine different filters by using the **Add Filter** button to the right. In some fields, you may add multiple values to find emails matching either of them.

For example, here, we search for emails that were delivered or clicked, and the recipient has either a Google Workspace or Yahoo! mailbox.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-035d11219fd13ba4c45bf4a56c6964da705abeda%2Femail-logs-filter-example.png?alt=media" alt="" width="563"></div>

Email Logs store emails sent from all your domains. If you wish to filter only for a particular domain or address, use **Email from**. For example:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1fcbfc5ac4a8dafe2bca2c0956c4e3f642ff404c%2Femail-logs-filter-by-domain.png?alt=media" alt="" width="563"></div>

#### Diving deeper into Email Logs

Email Logs provide much more information about each sent message. To access this, click on any of the messages.

The **Email info** tab provides the basic details of a message, including the timestamps, status, from/to addresses, or the IPs. If you’re confused about any of these terms, check our [Sending Glossary](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-sandbox/sandbox-glossary.md).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3d0f9c20d3a054f2766f73fa0329b7856259c8ad%2Femail-logs-email-info-tab.png?alt=media" alt="" width="563"></div>

Event History offers a list of all the events that have happened to this email since it was sent and until this moment.

You may know the HTML Source, Text, Preview, Raw, and Spam Analysis tabs well from Email Sandbox. Here, you can preview how your message looks on different devices, see its code, or see its spam score.


# Email Categories

Understand Mailtrap email categories: organize email types like welcome, onboarding, or billing. Track performance, analyze metrics, and compare categories.

Email Categories were built to show the performance of various types of emails, such as welcome emails, billing emails, confirmation emails, etc.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-6392fab22989e23d06402cbcb931b118c64e647a%2Femail-categories-overview-table.png?alt=media" alt="" width="563"></div>

#### Why should you use categories?

* See statistics for each type of email you send.
* Analyze key metrics of each category, such as open, click, or bounce rates. A single underperforming category can influence your overall sender reputation.
* Compare different types of emails and know straight away which perform better.
* Debug specific templates when, for example, an open rate suddenly drops.
* Simplify the search for any particular message. Filter out only emails matching a certain category to narrow down the results.

Email categories examples:

* “Feature XYZ intro”
* “Password reset 1st email”
* “Test A Order Confirmation”
* “Downgrade flow Tier 1”
* “Onboarding Msg 3”
* “Newsletter 04/20”

#### How to use

You specify categories when creating an email to be sent with Mailtrap, by inserting a category name into the `X-MT-Category` header if you are using SMTP.

If you are using the API, refer to our [Api Docs](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/67f1d70aeb62c-send-email-including-templates).

At this point, categories can only be specified when sending an email. Once you add one to an email and a message is sent, the category will appear in Mailtrap Email Logs’ filters as well as in statistics.

Categories cannot be removed or modified at this point. The number of categories in your account is unlimited.

#### How to analyze performance

Categories can be tracked via the Email Categories tab in the Stats menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-62fd09fc83581da5b9941f55d2fdeec928eebe44%2Femail-categories-metrics-detail.png?alt=media" alt="" width="563"></div>

You can filter out the data for specific domains or mailbox providers using the filters. You can also limit the number of domains displayed and compare statistics only for some of them.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-6388bb33e12f7702b89dc460b4e0b32e8a7e21dd%2Femail-categories-charts-view.png?alt=media" alt="" width="563"></div>

Mailtrap tracks statistics for each day separately, which can sometimes lead to, for example, open rates going into hundreds of percent.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bdc314b9d84f79617b16f2875246b97ee78ab253%2Femail-categories-daily-stats.png?alt=media" alt="" width="563"></div>


# Mailbox Providers

Analyze email performance by mailbox providers like Gmail, Outlook, and Yahoo. Filter by domain and category, track metrics, and identify deliverability issues.

<details>

<summary>Why is it important to monitor mailbox provider stats?</summary>

It’s important because the deliverability towards a specific provider can suddenly drop. This is a clear sign that a provider has started treating you negatively, so it’s critical to take action to improve the situation.

</details>

The following sections detail how to take advantage of **Mailbox Providers** feature within **Mailtrap API/SMTP**.

#### Mailbox Providers filters <a href="#mailbox" id="mailbox"></a>

Mailbox Providers Overview panel allows you to filter by **Domains**, **Mailbox Providers**, and **Categories**. Here’s how to use each filter.

**Domains**

1. Click on arrows in the All Domains box.
2. Choose one or more domains you’d like to use.
3. When you select the domain, the Table automatically shows corresponding statistics.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9f702c8da8a6fe1db2525933578771ed3d73a0e8%2Fmailbox-providers-domains-filter.png?alt=media" alt="Domains filter dropdown in Mailbox Providers panel" height="104" width="624"></div>

**Mailbox providers filter**

1. Click the arrows in the Mailbox Provider box.
2. Choose the provider you’d like to use.
3. Check the corresponding stats in the table below.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-74a47571082c3c0e5862a0521833a313f694bbf7%2Fmailbox-providers-provider-filter.png?alt=media" alt="Mailbox Provider filter dropdown showing available providers" height="199" width="624"></div>

You can select a few providers at the same time - just repeat the actions listed above.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-6a5c02b2623ca35b8ec0fa8986a8b76dbac3e0ed%2Fmailbox-providers-multiple-selection.png?alt=media" alt="Multiple mailbox providers selected in filter dropdown" height="152" width="624"></div>

**Categories**

1. Click the arrows in the **Categories** box.
2. Choose a category or categories.
3. Preview the stats for that category in the table below.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f3e0cf1258d053e02db657be7b5877a39ff57a42%2Fmailbox-providers-categories-filter.png?alt=media" alt="Categories filter dropdown in Mailbox Providers panel" height="139" width="624"></div>

#### Navigating mailbox providers <a href="#navigating" id="navigating"></a>

**Table**

The first column features **Mailbox Providers** of your recipients.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-32ab20e4ebcd7033a0d7cce08cf0f2a888da53ae%2Fmailbox-providers-table-column.png?alt=media" alt="Mailbox Providers statistics table showing provider names and metrics" height="168" width="624"></div>

The stats include the number of **Delivered** emails. You can also see **Unique Opens** and **Unique Open Rate**, as well as **Clicked** emails and **Click Rate**.

Also, the Tables tab shows **Bounce** emails and **Bounce Rate**, plus **Spam** and Spam **Complaints**. Finally, you can see the **Clicked to Open Rate**.

You can learn more about [Stats](https://docs.mailtrap.io/documentation/email-api-smtp/analytics) here.

**Color coding**

To immediately understand email deliverability, the table features colors that signal if the value is good, bad, or just average.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a292107f76f4b8f266d24e1629b6d4fa814a3141%2Fmailbox-providers-green-status.png?alt=media" alt="Mailbox Providers table row with green status indicator showing good performance" width="563"></div>

* Green - good results - exceed what we perceive as a satisfactory value for a particular data point.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a38e6eeeaaa0427d1560fdecd2e7b6bf72b6e1c6%2Fmailbox-providers-yellow-status.png?alt=media" alt="Mailbox Providers table row with yellow status indicator showing borderline performance" width="563"></div>

* <mark style="background-color:yellow;">Yellow</mark> - borderline results - neither good nor bad, and may require your attention or action.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d7267a4fb6b1473a1eea1b5356336a7fc3954557%2Fmailbox-providers-red-status.png?alt=media" alt="Mailbox Providers table row with red status indicator showing poor performance requiring attention" width="563"></div>

* <mark style="background-color:red;">Red</mark> - the result is under the threshold we consider satisfactory and it requires your action to improve the performance of a specific mailbox provider.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ba2f7c059f7309ac38a8e4749666506d382db0e1%2Fmailbox-providers-table-example.png?alt=media" alt="Mailbox Providers table showing email statistics with color-coded performance indicators" width="563"></div>


# Statuses and Events

Learn about Mailtrap statuses and events: delivery, bounces, opens, clicks, and opt-outs. Understand how statuses differ from events and track performance.

When sending emails with Mailtrap, you’ll often encounter the terms Status and Event.

**Status** is the latest delivery status of an email. Each status bears a distinct color, and an email can only have one status at a time. The available statuses are: **Delivered, Not Delivered, Enqueued,** and **Opted Out**.

As an email changes status, multiple **events** can occur. Events are one-time occurrences that are logged into the **Event History**. Multiple events can (and often are) recorded for an email.

For example, a certain email can have the status **Opted Out**. This indicates that the recipient marked your message as spam or unsubscribed from the list. The **Event History** tab for such an email may look like this:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e31948e0fe216ce79d807b04e255833b32e4637f%2Fstatuses-event-history-example.png?alt=media" alt="" width="375"></div>

The chart below showcases all the possible events and the relations between them.

![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f5c23592019133543de49639177c24a9450e4956%2Fstatuses-events-flow-diagram.png?alt=media)

Here’s a summary of all the possible events:

{% tabs %}
{% tab title="Enqueued" %}
Email has been queued for sending or has been dispatched, but something prevented its delivery.

<table><thead><tr><th width="188.58203125">Event</th><th>Event Description</th></tr></thead><tbody><tr><td>Sending</td><td>Email sending is in process, or it’s in the queue.</td></tr><tr><td>Soft bounce</td><td>Email couldn’t be delivered, most commonly due to a server timeout, full inbox, or too large size. The delivery will be attempted 10 more times. Possible outcomes: Delivery or Bounce.</td></tr><tr><td>Suspension</td><td>Email was sent from an unverified domain. We’ll re-check the domain status 10 more times. If it’s verified during this time, an email will be sent. Possible outcomes: Delivery, Reject.</td></tr></tbody></table>
{% endtab %}

{% tab title="Not delivered" %}
Email failed to be delivered, and no further attempts will be made.

<table><thead><tr><th width="189.0625">Event</th><th>Event Description</th></tr></thead><tbody><tr><td>Reject</td><td>The domain in question was not verified in time after an initial suspension of an email, and a message was rejected. Or, a recipient is on a suppression list for this domain.</td></tr><tr><td>Bounce</td><td>Email recorded a bounce (permanent delivery failure), and no further attempts will be made to deliver it. Most commonly, this happens because of an invalid email address or a rejection by the recipient’s mailbox provider.</td></tr></tbody></table>
{% endtab %}

{% tab title="Delivered" %}
Email was accepted by the recipient’s mailbox provider.

<table><thead><tr><th width="188.8046875">Event</th><th>Event Description</th></tr></thead><tbody><tr><td>Delivery</td><td>Email was accepted by the recipient’s mailbox provider. Note: this doesn’t exclude a delivery to a spam folder. In some cases, an email may be accepted, but an internal policy may prevent it from reaching a sandbox.</td></tr><tr><td>Open</td><td>Email was opened by a recipient or another person that a message was forwarded to. Multiple open events can be recorded.</td></tr><tr><td>Click</td><td>Any link in an email was clicked.</td></tr></tbody></table>
{% endtab %}

{% tab title="Opted Out" %}
A recipient opted out of receiving any further messages and has been added to Mailtrap’s suppression list for this domain.

{% hint style="info" %}
This doesn't prevent you from emailing them from other verified domains.
{% endhint %}

<table><thead><tr><th width="188.83984375">Event</th><th>Event Description</th></tr></thead><tbody><tr><td>Unsubscribe</td><td>The recipient unsubscribed from receiving emails. Mailtrap won’t send any further emails to them from this domain.</td></tr><tr><td>Spam</td><td>User reported a message as spam. Mailtrap won’t send them any more messages from this domain.</td></tr></tbody></table>
{% endtab %}
{% endtabs %}

And here's a summary of the possible statuses:

<table><thead><tr><th width="138.8515625">Status</th><th width="223.07421875">Status Description</th><th width="137.93359375">Event</th><th>Event Description</th></tr></thead><tbody><tr><td>Enqueued</td><td>Email has been queued for sending or has been dispatched, but something prevented its delivery.</td><td>Sending</td><td>Email sending is in process, or it’s in the queue.</td></tr><tr><td><br></td><td><br></td><td>Soft bounce</td><td>Email couldn’t be delivered, most commonly due to a server timeout, full inbox, or too large size. The delivery will be attempted 10 more times. Possible outcomes: Delivery or Bounce.</td></tr><tr><td><br></td><td><br></td><td>Suspension</td><td>Email was sent from an unverified domain. We’ll re-check the domain status 10 more times. If it’s verified during this time, an email will be sent. Possible outcomes: Delivery, Reject.</td></tr><tr><td>Not delivered</td><td>Email failed to be delivered, and no further attempts will be made.</td><td>Reject</td><td>The domain in question was not verified in time after an initial suspension of an email, and a message was rejected. Or, a recipient is on a suppression list for this domain.</td></tr><tr><td><br></td><td><br></td><td>Bounce</td><td>Email recorded a bounce (permanent delivery failure), and no further attempts will be made to deliver it. Most commonly, this happens because of an invalid email address or a rejection by the recipient’s mailbox provider.</td></tr><tr><td>Delivered</td><td>Email was accepted by the recipient’s mailbox provider.</td><td>Delivery</td><td>Email was accepted by the recipient’s mailbox provider. Note: this doesn’t exclude a delivery to a spam folder. In some cases, an email may be accepted, but an internal policy may prevent it from reaching an sandbox.</td></tr><tr><td><br></td><td><br></td><td>Open</td><td>Email was opened by a recipient or another person that a message was forwarded to. Multiple open events can be recorded.</td></tr><tr><td><br></td><td><br></td><td>Click</td><td>Any link in an email was clicked.</td></tr><tr><td>Opted Out</td><td>A recipient opted out of receiving any further messages and has been added to Mailtrap’s suppression list for this domain. Note: this doesn’t prevent you from emailing them from other verified domains.</td><td>Unsubscribe</td><td>The recipient unsubscribed from receiving emails. Mailtrap won’t send any further emails to them from this domain.</td></tr><tr><td><br></td><td><br></td><td>Spam</td><td>User reported a message as spam. Mailtrap won’t send them any more messages from this domain.</td></tr></tbody></table>

{% hint style="success" %}
If you want to track how many emails were delivered, it's better to use the **Delivery** event rather than the **Delivered** status.
{% endhint %}

When a recipient unsubscribes or reports your message as spam, an email's status changes to Opted Out. At the same time, the Delivery event remains in its Events History. By filtering for this event, you’ll easily find all emails that were delivered in a chosen timeframe, regardless of what happened to them next.

Some useful definitions:

* **Client sending IP** — IP address of a device that was used to send an email.
* **Mailtrap sending IP** — IP address of Mailtrap, used to send a message to the final recipient.
* **Recipient IP** — IP address of a device or an email server where an email was opened. If a message is opened on devices using different IP addresses, multiple Recipient IPs will be recorded. If a message is not opened at all, no Recipient IP will be displayed.

<a href="https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-sandbox/sandbox-glossary.md" class="button primary">Find more definitions in Sending Glossary</a>


# Deliverability Features

Learn about email deliverability features and tools Mailtrap provides to guarantee high inbox placement rates of your emails.

Maximize your email deliverability with Mailtrap's comprehensive suite of deliverability tools. These features help you maintain a good sender reputation, manage bounces effectively, and ensure your emails reach their intended recipients.

### Essential Guide

#### [Email Deliverability Guide](https://mailtrap.io/email-deliverability-guide/)

**Start here!** Our comprehensive guide covers everything you need to know about achieving optimal deliverability:

* Golden rules of email deliverability
* Technical setup and domain authentication
* List management best practices
* Content optimization
* Monitoring and compliance

{% hint style="info" %}
**Recommended**: Read the Email Deliverability Guide first to understand best practices before configuring individual features.
{% endhint %}

### Key Features

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Suppressions List</strong></td><td><em>Automatically manage unsubscribed users and prevent sending to invalid email addresses. Keep your lists clean and maintain good sender reputation.</em></td><td><a href="deliverability/suppressions-list">suppressions-list</a></td></tr><tr><td><strong>Bounce Categorization</strong></td><td><em>Understand why emails bounce with detailed categorization. Differentiate between soft and hard bounces to take appropriate action.</em></td><td><a href="deliverability/bounce-categorization">bounce-categorization</a></td></tr><tr><td><strong>Feedback Loops</strong></td><td><em>Receive notifications when recipients mark your emails as spam. Automatically suppress these contacts to maintain deliverability.</em></td><td><a href="deliverability/feedback-loops">feedback-loops</a></td></tr><tr><td><strong>Dedicated IP</strong></td><td><em>IP address that only you use for sending emails. As such, you have full control over your reputation and can influence it with each email sent.</em></td><td><a href="deliverability/ip-warmup">ip-warmup</a></td></tr><tr><td><strong>Deliverability Alerts</strong></td><td><em>Get weekly health status reports and critical alerts for your email deliverability metrics including opens, clicks, bounces, unsubscribes, and spam complaints.</em></td><td><a href="deliverability/deliverability-alerts">deliverability-alerts</a></td></tr><tr><td><strong>Protecting Your Domain</strong></td><td><em>Best practices to protect your sending domain from abuse, including securing web forms, implementing CAPTCHA, and hiding sensitive configuration files.</em></td><td><a href="deliverability/protecting-domain-security">protecting-domain-security</a></td></tr></tbody></table>


# Suppressions List

Manage Mailtrap suppression lists. View, add, remove, or import suppressed emails from hard bounces, unsubscribes, and spam complaints via CSV or manually.

When hard bounce, unsubscribe, and spam complaints events occur, Mailtrap adds the email address to a suppression list. The suppression list contains all the addresses you cannot send emails to.

You'll find all the addresses on suppression lists in the **Suppressions** menu to the left.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-54ff880c7eb4f2239d3d64571d8db844c01286d2%2Fsuppressions-list-table.png?alt=media" alt="" width="563"></div>

The menu contains the data for all your domains. If an email address was suppressed for more than one domain, it appears multiple times on the list.

You can export the whole Suppressions list.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-79c14346a568c54f29866b1c1b4cc618f98e5b49%2Fsuppressions-list-export.png?alt=media" alt="" width="563"></div>

### How to remove an email from a suppression list

If you believe an email landed on a suppression list by accident, you can remove it by clicking the **Reactivate** button to the right.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-778cb990d609d58d2b11031f26dda68a336f7975%2Fsuppressions-list-reactivate-button.png?alt=media" alt="" width="563"></div>

However, we advise you not to misuse the feature.

If someone decided to report your message as spam or leave your email list, you really don’t want to be emailing them again (unless they explicitly told you they had done it by mistake). Any further attempts will probably result in the same outcome, immediately hurting your email deliverability.

### Suppression list filters

You can filter the suppression list for:

* Specific email address
* Sending domain
* Type of suppression
* Reason for suppression

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fea06a2896ed471c4392f1b27beec65d103c7d0f%2Fsuppressions-list-filters.png?alt=media" alt="" height="129" width="624"></div>

### How to add recipients to the suppression list

Mailtrap allows you to add recipients manually or by uploading a CSV file.

#### Manual method

Select **Insert manually**. Then, under **Add to stream**, choose Bulk, Transactional, or Any. Under **Add to domain**, choose all or one of your domains.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-08174b267885270e2ad47ec0b037a05ccb1f41fd%2Fsuppressions-add-manual-modal.png?alt=media" alt="" width="375"></div>

After you select the domain and stream, type or copy-paste the email addresses you want to suppress into the designated box. Then, click the **Add To Suppressions** button to complete the action.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-cf3549453be1014e877b0159f83fef9ef43f4a65%2Fsuppressions-add-manual-form.png?alt=media" alt="" width="375"></div>

You can add only one email address per line and up to 1,000 emails per selected domain.

Note that there's also the **Add New/Import** button at the top right of the screen in the Suppressions main dashboard. It allows you to access the **Add recipients to suppression list** menu quickly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-06baa355f9a91da163aa531479c542f878020337%2Fsuppressions-add-new-import-button.png?alt=media" alt="" height="92" width="624"></div>

#### Upload CSV

Before you upload CSV to Mailtrap, you first need to export the document from your current sending provider. See how to do it with SendGrid, Postmark, and Mailgun.

### Exporting suppressions

#### Sendgrid

Navigate to Suppression Management - this is where you’ll find the list of all your Unsubscribe Groups. You’ll see the default groups and the ones you created.

To export the CSV file, you need to click the Settings button (the gear icon) next to each group, then choose **Export**.

#### Mailgun

Mailgun keeps three suppression lists (complaints, bounces, and unsubscribes) for each of your sending domains. There's no global, account-level suppression list, so you need to export separate lists for each domain you transfer to Mailtrap.

To get the list in CSV format, make sure you choose the correct domain and use the Mailgun dashboard to export the lists.

#### Postmark

There’s an Export button in the Postmark dashboard. This allows you to export up to 500 records in a JSON file. For more records, you need to use Postmark’s Messages API.

Many online services offer services for converting JSON to CSV. [Postmark’s help page](https://postmarkapp.com/support/article/881-can-i-export-a-list-of-all-bounces) provides more information.

### Importing to Mailtrap

Select **Upload CSV**, then choose the stream and the domain.

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FLVGZ3DkmdXORBHZ1UMpe%2FScreenshot%202026-01-02%20at%2011.25.25.png?alt=media&#x26;token=059c58bd-3e4d-4433-afec-61f8e6061153" alt=""><figcaption></figcaption></figure></div>

Click **Browse file** to select the CSV file from your computer or drag and drop it into the **Select file** box.

To complete the action, click **Add To Suppressions** and you’re done. If you wish, you can also download our CSV template by clicking on the corresponding option.

**Hint:** You can suppress sending of transactional and marketing emails separately or do both at once by selecting 'Any'. For example, if a user X unsubscribes from marketing emails and they're now on the suppression list, this doesn't stop you from sending them transactional emails. However, if they unsubscribe from those too, they won't receive any emails.


# Dedicated IP

Learn about Mailtrap IP warmup: shared vs dedicated IPs, automated IP warmup schedule, and gradual daily sending limits over 3 weeks.

Mailtrap offers both shared IP addresses as well as dedicated IPs.

### Shared IP vs Dedicated IP

A **shared IP** is a default option with nearly all sending providers (including Mailtrap). A provider maintains a pool of IPs that are shared among their users.

A **dedicated IP** is the IP address that only you use for sending emails. As such, you have full control over your reputation and can influence it with each email sent.

We recommend dedicated IPs only if your volume regularly exceeds 100,000+ emails per month.

{% hint style="info" %}
If you’re interested in using a dedicated IP, the Deliverability team will be happy to assist you.&#x20;

<a href="mailto:deliverability@mailtrap.io" class="button secondary">Contact us</a>
{% endhint %}

Each request is reviewed individually by our Deliverability team. In some cases we recommend and insist users to stay on a shared IP for their own benefit.

### Automated IP warmup at Mailtrap

Each newly purchased dedicated IP goes through a mandatory 3-weeks-long (in most cases) warm-up process, aimed at giving you the best possible preparation for sending mass emails.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7b580196ce1a113c19e7e64e497b108a5ee38e38%2Fip-warmup-dedicated-ips-status.png?alt=media" alt=""></div>

Mailtrap automatically increases your volume each day, with about 30% more emails sent every day. Simultaneously, our deliverability experts closely monitor your stats.

At the moment the IP warm-up schedule looks as follows:

<table data-header-hidden><thead><tr><th width="100">Day</th><th>Emails sent per day</th><th>Max emails per hour</th></tr></thead><tbody><tr><td><strong>Day</strong></td><td><strong>Emails sent per day</strong></td><td><strong>Max emails per hour</strong></td></tr><tr><td>1</td><td>300</td><td>60</td></tr><tr><td>2</td><td>390</td><td>80</td></tr><tr><td>3</td><td>510</td><td>100</td></tr><tr><td>4</td><td>660</td><td>130</td></tr><tr><td>5</td><td>860</td><td>170</td></tr><tr><td>6</td><td>1,100</td><td>220</td></tr><tr><td>7</td><td>1,400</td><td>290</td></tr><tr><td>8</td><td>1,900</td><td>380</td></tr><tr><td>9</td><td>2,400</td><td>490</td></tr><tr><td>10</td><td>3,200</td><td>640</td></tr><tr><td>11</td><td>4,100</td><td>830</td></tr><tr><td>12</td><td>5,400</td><td>1,100</td></tr><tr><td>13</td><td>7,000</td><td>1,400</td></tr><tr><td>14</td><td>9,100</td><td>1,800</td></tr><tr><td>15</td><td>11,800</td><td>2,400</td></tr><tr><td>16</td><td>15,400</td><td>3,100</td></tr><tr><td>17</td><td>20,000</td><td>4,000</td></tr><tr><td>18</td><td>26,000</td><td>5,200</td></tr><tr><td>19</td><td>33,700</td><td>6,700</td></tr><tr><td>20</td><td>43,900</td><td>8,800</td></tr><tr><td>21</td><td>57,000</td><td>11,400</td></tr></tbody></table>

This schedule shouldn’t, of course, limit your email sending capability. Any emails over a limit will automatically be sent via one of Mailtrap’s Shared IPs.


# Bounce Categorization

Understand how Mailtrap categorizes email bounces based on MX server responses, including bounce types, descriptions, and automatic suppression rules.

Mailtrap categorizes [bounces](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/dashboard) based on the responses from the recipients' MX servers.

The table below lists these responses and their descriptions. It also contains information on whether these bounces cause automatic suppression.

You can find bounce categories in the app, specifically in event history in Email Logs, Webhooks payload for bounce and soft\_bounce events, and Suppressions for hard bounces.

<table><thead><tr><th width="132.73046875">Category</th><th width="156.31640625">Event name</th><th width="361.05859375">Description</th><th>Adding to Suppressions</th></tr></thead><tbody><tr><td>transientfail</td><td>Transient failure</td><td>The email encountered a temporary issue.</td><td>No</td></tr><tr><td>greylisting</td><td>Greylisting</td><td>The email was temporarily rejected by the recipient's server to determine whether the sender was legitimate or not.</td><td>No</td></tr><tr><td>badsender</td><td>Bad sender</td><td>The email was rejected because the sender's address was invalid or unrecognized.</td><td>No</td></tr><tr><td>block</td><td>Blocked</td><td>The recipient's email server blocked the email, possibly due to security policies.</td><td>No</td></tr><tr><td>content</td><td>Content issue</td><td>The email content triggered content filters and was rejected by the recipient's server.</td><td>No</td></tr><tr><td>dnsFail</td><td>DNS failure</td><td>The email could not be delivered due to issues with the DNS configuration of the recipient's domain.</td><td>No</td></tr><tr><td>generalfail</td><td>General failure</td><td>The email could not be delivered due to a general failure on the recipient's server.</td><td>No</td></tr><tr><td>other</td><td>Other</td><td>The email was bounced for an unspecified or unknown reason.</td><td>No</td></tr><tr><td>relayfail</td><td>Relay failure</td><td>The email was rejected because the server is not allowed to relay messages.</td><td>No</td></tr><tr><td>serverfail</td><td>Server failure</td><td>The email could not be delivered due to a failure on the recipient's server.</td><td>No</td></tr><tr><td>spam</td><td>Spam detected</td><td>The email was identified as spam by the recipient's mail server.</td><td>No</td></tr><tr><td>verifyfail</td><td>Verification failed</td><td>The email was rejected because the sender's or recipient's addresses could not be verified.</td><td>No</td></tr><tr><td>timeout</td><td>Timeout</td><td>The email was bounced due to an unspecified issue, probably a timeout.</td><td>Yes</td></tr><tr><td>badrecipient</td><td>Bad recipient</td><td>The email was bounced because the recipient's email address is invalid or does not exist.</td><td>Yes</td></tr><tr><td>overquota</td><td>Over quota</td><td>The recipient's mailbox is full and cannot accept new messages.</td><td>Yes</td></tr><tr><td>serverpolicy</td><td>Server policy</td><td>The email was rejected due to the recipient's server policy settings.</td><td>No</td></tr><tr><td>spam_gmail</td><td>Gmail limitation</td><td>The email bounced due to limitations from Gmail recipient due to either incorrect authentication, sudden increase of email traffic, or reputation issue</td><td>No</td></tr></tbody></table>


# Feedback Loops

Learn how Mailtrap integrates with popular Feedback Loops (FBLs) to track spam complaints from major mailbox providers including Outlook, Yahoo, and more.

Mailtrap is integrated with the majority of popular Feedback Loops (FBLs) to gather information about spam complaints.

{% hint style="info" %}
Remember that Gmail doesn’t provide spam complaint information per message.
{% endhint %}

Still, Mailtrap adds `Feedback-ID` to all emails sent to Gmail. If you specify Email Categories, we add it to the header as a part of the category. Yet, it’s up to Gmail to show that info in your Google Postmaster. Read more about the feedback header [here](https://support.google.com/a/answer/6254652?hl=en).

Our Deliverability Team can review aggregated data for Spam Rates for Gmail recipients daily if you provide us with view rights for Google Postmaster. This service is available for our paid customers. Please contact our support team for the details.

<a href="mailto:support@mailtrap.io" class="button secondary">Contact Support</a>

<details>

<summary>The list of FBLs Mailtrap is integrated with:</summary>

* Microsoft Outlook
* Yahoo! Mail
* Bluetie
* Comcast
* Fastmail
* gandi.net
* Liberty Global (Chello, UPC, and UnityMedia)
* Locaweb
* Mail.ru
* OpenSRS/Hostedmail (Tucows)
* Rackspace
* Seznam
* SFR
* SilverSky
* Swisscom
* Synacor
* Telecom Italia
* Telenet
* Telenor
* Telstra
* Terra
* UOL
* Virgilio
* Virgin Media
* Yandex
* Ziggo

</details>

While using our services, Mailtrap may get alerts from these FBLs if your recipients submit spam complaints. You'll see them in your [Stats](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/dashboard) and may receive them via [Webhooks](https://docs.mailtrap.io/documentation/setup/sending-domain#optional-webhooks-4hmes).

We also support the `CFBL-Address` header as per [RFC 9477](https://www.rfc-editor.org/rfc/rfc9477.html). However, it’s still experimental, and not all mailbox providers support it.


# Deliverability Alerts

Get weekly health status reports and critical alerts for your email deliverability metrics including opens, clicks, bounces, unsubscribes, and spam complaints.

Deliverability Alerts help you monitor your email performance by providing automated notifications about your sending metrics.

{% hint style="info" %}
A minimum of 500 emails per week is required to receive alerts, as the system needs sufficient data to provide meaningful statistics.
{% endhint %}

If you want, you can toggle the alerts off. However, we recommend keeping them enabled because a missed issue may affect your domain authority and sender reputation.

## Health Status Weekly

Health Status Weekly alerts are sent out on Mondays and provide a detailed preview of the following stats:

* Opened
* Clicks
* Bounces
* Unsubscribes
* Spam

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a4267082e8c18bc0c134789ecc9779045b6ea308%2Fdeliverability-alerts-weekly-stats.png?alt=media" alt="Weekly stats table showing email metrics with color-coded status indicators for All good, Attention required, and Critical" width="563"><figcaption></figcaption></figure></div>

The report includes clearly color-coded comparisons to the previous week, making it immediately obvious if one or more stats need your attention or show a negative trend. Additionally, there are insights (digest explanations of the stats) to help you troubleshoot your email infrastructure faster.

## Integrate Mailtrap Alerts with Slack

Each Slack channel has a unique email address. You can leverage that to route Mailtrap Alerts directly to Slack. Here's how to do it on the desktop app:

{% stepper %}
{% step %}
Click the channel name in the header and select **Integrations**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3a0b8d3d8a76529aa5f617bfc8228837e707448d%2Fslack-channel-integrations.png?alt=media" alt="Slack channel settings showing Integrations tab highlighted with arrow" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Send emails to this channel**, then the **Get Email Address** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-16d5cfe0ff6b7ab90bf9c194fe10b437195d6270%2Fslack-get-email-address.png?alt=media" alt="Slack modal showing Get Email Address button for sending emails to channel" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Navigate to the Deliverability Alerts page in Mailtrap, and paste the Slack email address into the field under **Who receives notifications?**

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c9154ed305e8f0298a47a0ae3a358a78d9485fca%2Fdeliverability-alerts-settings.png?alt=media" alt="Mailtrap Deliverability Alerts settings page showing notification recipients field with Save button" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Save** and all alerts will be routed to the Slack channel instead of your email.
{% endstep %}
{% endstepper %}

## Critical Alerts

{% hint style="warning" %}
Critical Alerts feature is currently switched off. We'll notify you once it's back on.
{% endhint %}

Critical Alerts are sent hourly (the system checks your metrics every three hours for the past 24 hours) when one or more of your critical stats are below the predetermined threshold.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-614c1e107dc21ce8bb17ccf17cc0b3295c4b89d5%2Fcritical-alerts-demo.gif?alt=media" alt="Animated demonstration of Critical Alerts notification appearing on mobile device" width="563"><figcaption></figcaption></figure></div>

The predetermined thresholds are based on extensive cross-industry research and examples of best practices.

{% hint style="info" %}
If you're getting a lot of false positives or negatives, feel free to reach out to us at <support@mailtrap.io>.
{% endhint %}


# Protecting Your Domain

Best practices to protect your sending domain from abuse, including securing web forms, implementing CAPTCHA, and hiding sensitive configuration files.

Adding and verifying your domain with Mailtrap is a simple process. However, in some cases, an automated security tool may flag your domain as high-risk and reject it. To prevent this, follow the best practices outlined in this article to enhance your security and ensure a smooth verification process.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8bfc0b0b68e3d5e409c69aefb7f7a4d14d892f9c%2Fdomain-verified-status.png?alt=media" alt="Domain verified status message showing domain can be used to send emails" width="375"><figcaption><p>Verified domain status</p></figcaption></figure></div>

### Protect your web forms

You should protect all email-triggering online forms on your website. Otherwise, bots may use them to send a large volume of unsolicited emails to recipients who did not expect these emails and can start marking them as spam. Also, those kinds of emails may potentially contain malicious content, severely affecting your sender's reputation.

{% hint style="warning" %}
It's highly recommended that **all** web forms that can trigger email sending, such as newsletters, user registration pages, and password reset forms, be secured. This applies even if emails to be sent via Mailtrap are unrelated to those forms or are sent to different email addresses than the one gathered through online forms.
{% endhint %}

{% hint style="info" %}
If your domain is used to send emails to users who registered through an unprotected form that gets abused - even if those emails were sent using a tool other than Mailtrap - your domain reputation may suffer, and you can experience deliverability issues when sending legitimate emails through Mailtrap.
{% endhint %}

#### Protection methods

* **CAPTCHA/reCAPTCHA** — Requires human interaction to complete the form
* **Honeypots** — An invisible field that bots automatically fill, but humans don't see
* **Timing check** — Rejecting all submissions completed under 1 second
* **IP rate limiting** — Detect IPs that attempt to use the form multiple times and prevent further submissions
* **Double opt-in** — Ensure that the email address is valid and that the user genuinely wants to receive communications

### CAPTCHA

Adding CAPTCHA or reCAPTCHA is one of the most efficient ways to protect your forms on your website from bots and spam. Here's how to implement it:

1. Choose a trusted CAPTCHA solution:
   * [Google reCAPTCHA](https://www.google.com/recaptcha/about/)
   * [hCAPTCHA](https://www.hcaptcha.com/)
   * [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/)
2. Sign up for the API keys
3. Add the CAPTCHA widget to your form HTML
4. Validate the CAPTCHA on your server
5. Test your implementation

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-511d6ae8977e5013d164d16c8d495b9ab1a79f05%2Frecaptcha-widget.gif?alt=media" alt="Google reCAPTCHA widget showing I&#x27;m not a robot checkbox" width="300"><figcaption></figcaption></figure></div>

### Honeypot fields

Honeypot fields are hidden fields that should remain empty. If a bot catches them, it'll automatically complete them, thus blocking itself from the form.

To add honeypots:

1. Add a hidden input field to your frontend
2. Validate the honeypot field in your backend

{% hint style="info" %}
We recommend using a randomized name for honeypot fields to avoid detection by bots that specifically look for common field names.
{% endhint %}

### Timing check

By adding a timing check, you block all submissions completed under 1 second (or any time you think a bot might be able to complete a form).

You can also add a maximum time limit, like 1 hour. This way, if a form is left open too long, the user submission will be rejected. This can be useful for detecting expired or suspicious sessions.

### Rate limiting by IP address

Rate limiting controls the number of requests a single IP can make to a server within a timeframe you specify. With rate limiting, you can easily detect IPs that attempt to use the form multiple times and prevent further submissions.

### Double opt-in

After a user submits their email address, they must confirm their subscription by clicking a verification link sent to their inbox. This extra step:

* Ensures that the email address is valid
* Confirms the user genuinely wants to receive communications
* Helps prevent spam and fraudulent sign-ups
* Protects your sender reputation

### Hide your .env file

The .env file is where you store your sensitive configuration information, including API keys, database credentials, and other critical environment variables. Spammers could send emails to your recipients on your behalf if your .env is exposed, so we may not approve your domain if it's accessible.

{% hint style="danger" %}
How you store your .env file is your first line of defense against attackers.
{% endhint %}

**Best practices:**

* Keep your .env file from the public by hiding it outside your web root, restricting file permissions, or using your preferred method.
* Turn off debug mode, as it can expose sensitive information, including environment variables. This is typically done by setting your `DEBUG` to `False`, depending on your programming language.

### Additional security measures

The methods outlined in this article are not exhaustive. While securing your web forms and hiding your .env files are fundamental security measures, they should be considered just the first line of defense.

Additional recommended measures:

* Use strong passwords that are regularly updated.
* Manage access rights carefully to ensure only authorized users can access sensitive systems.
* Conduct regular security audits to identify and address potential vulnerabilities.
* Implement additional security layers to better protect your website or application.


# Advanced Features

Learn what features for advanced email sending scenarios Mailtrap Email API/SMTP provides.

Take your email sending to the next level with Mailtrap's advanced features. These tools are designed for power users who need more control over their email infrastructure and want to optimize their sending patterns.

## Features Overview

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Custom Variables</strong></td><td><em>Add custom metadata to your emails for advanced tracking and segmentation. Pass through data that helps you analyze email performance in your own systems.</em></td><td><a href="advanced/custom-variables">custom-variables</a></td></tr><tr><td><strong>Excluding Links from Tracking</strong></td><td><em>Have sensitive links that shouldn't be tracked? Learn how to exclude specific URLs from click tracking while maintaining analytics for other links.</em></td><td><a href="advanced/excluding-specific-links-from-tracking">excluding-specific-links-from-tracking</a></td></tr><tr><td><strong>Auto BCC</strong></td><td><em>Automatically send blind carbon copies of all emails to a specified address for compliance and monitoring purposes.</em></td><td><a href="advanced/auto-bcc">auto-bcc</a></td></tr><tr><td><strong>Webhooks</strong></td><td><em>Webhooks allow you to receive all information about your deliverability and activities within your account almost in real-time.</em></td><td><a href="advanced/webhooks">webhooks</a></td></tr></tbody></table>


# Custom Variables

Add unique data to your emails with custom variables. Track user IDs, inbox IDs, and other metadata via Email Logs using X-MT-Custom-Variables header.

Custom variables are pieces of information that you can include with emails to better manage them in the future. They allow you to add unique data to each message, for example, the data can be an internal `user_id`, `inbox_id`, etc.

For now, you can only access them via Email Logs.

#### How to access custom variables

1. Click on the given functionality
2. Choose an email
3. Check the variables (Variable name 1, 2, 3…) under the Email info tab

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e2392290d7b03df7e5fb1cb5f9036eb7fc72667b%2Fcustom-variables-email-info-tab.png?alt=media" alt="Email info tab showing custom variables in Mailtrap interface" width="563"></div>

#### **How to set up custom variables with SMTP**

Mailtrap has an option to pass unique arguments to each sent email via the `X-MT-Custom-Variables`. And we add the arguments to the RAW email body. Of course, the RAW data is visible to the sender but not the end-user.

To set custom variables, you only need to set the unique argument in the following format - `{"variable name": "variable value"}`.

Here’s a code snippet, to show you where to look for it, and how to set the variable. Note that this applies when you set Mailtrap as your SMTP server.

{% code title="cURL Example with Custom Variables" %}

```bash
curl --ssl-reqd \
  --url 'smtp://send.smtp.mailtrap.io:587' \
  --user 'api:49ad7a716f18d9c64xxxxx' \
  --mail-from 'example@mailtrap.io' \
  --mail-rcpt 'email@exampledomain.com' \
  --upload-file - <<EOF
To: Mailtrap Sandbox
Subject: custom header
X-MT-Custom-Variables: {"variable name":"variable value"}
Content-Type: multipart/alternative; boundary="boundary-string"

--boundary-string
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable
Content-Disposition: inline

You are awesome!
EOF
```

{% endcode %}

As you can see, you only need to add the variable name and value in the given format. The exemplary mail has one variable; and you can add more, of course.

The format for adding more custom variables is - `X-MT-Custom-Variables: {"variable1":"value1", "variable2":"value2"}`. Also, here’s another example of how custom variables appear in Mailtrap UI.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fe5e0b59bb6735ed12fa608dc58330043037fde7%2Fcustom-variables-ui-example.png?alt=media" alt="Custom variables displayed in Mailtrap UI showing variable names and values" width="375"></div>

Lastly, keep in mind that we don’t support arrays. If you want to add arrays - `[“index0”,”index1”,”index2”]`, for example, Mailtrap only takes the first value (`"index0"`) and ignores the rest.

{% hint style="warning" %} We limit the custom variables payload to 1000 bytes, and it’s a valid JSON string. If the payload is more than 1000 bytes, Mailtrap ignores the `X-MT-Custom-Variables`.

We use only - `X-MT-Custom-Variables`; and it can’t get appended with another one.


# Excluding Links from Tracking

Learn how to exclude specific links from tracking using the data-mt-no-track attribute to preserve app deeplinks and sensitive URLs.

By default, when link tracking is enabled for a domain, Mailtrap rewrites links in your emails to add tracking redirects. However, in some cases you may want to exclude certain links (such as app deeplinks or sensitive URLs) from being tracked.

### How to Disable Tracking for a Specific Link

To prevent a link from being tracked, add the special attribute `data-mt-no-track` to your `<a>` tag in the HTML body of the email.

```html
<a data-mt-no-track href="https://example.com/deeplink">Open in App</a>
```

When this attribute is present:

* The link in the HTML body will not be replaced with a tracking redirect.
* If the same link also exists in the Text body of your email, it will also remain untouched (not rewritten).

### Notes

* This works on a per-link basis - all other links without the attribute will still be tracked.
* The attribute must be included in the HTML body. If the identical URL also appears in the Text body, it will inherit the no-track behavior.
* Use this for app deeplinks or any URL where tracking redirects could break functionality.


# Auto BCC

Automatically add BCC recipients to all emails sent from your domain with custom headers support.

### How to set up Auto BCC

{% stepper %}
{% step %}
Go to **Sending Domains** and choose the domain you want to set up Auto BCC for.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-05532a096d2941cef62f874aa17ed1ec5bbedb9f%2Fauto-bcc-sending-domains-list.png?alt=media" alt="Sending Domains page showing list of verified domains with domains highlighted" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Navigate to the **Auto BCC** tab.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-85aed464b5ab611501e8a37b20e0b1f3263eac6d%2Fauto-bcc-tab.png?alt=media" alt="Domain page showing Auto BCC tab highlighted by red arrow" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter an email address that will be included as BCC in all the emails you send from this domain and click **Add Email**.

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-241fd324619c429bd0bf5813f7ef921f44ce186d%2Fauto-bcc-add-email.png?alt=media" alt="Auto BCC page with email input field and Add Email button highlighted by red arrow" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Optionally, specify a custom X-header that will be included in emails to BCC recipients. Enter the Name and Value, and click **Add Header**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4231db79febbaa273437142bd8578c3193f4d12c%2Fauto-bcc-add-header.png?alt=media" alt="Custom Headers section with Name and Value fields and Add Header button highlighted by red arrow" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
To delete the email address or a custom header, click the trash bin icon and confirm the action by clicking **Delete**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-060445e232eb255ee8bf63ecb2bcaa59e9b16486%2Fauto-bcc-delete-confirmation.png?alt=media" alt="Auto BCC page showing email with trash icon and delete confirmation dialog with Delete button highlighted" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Important notes

* You can add multiple BCC email addresses, and all of them will receive email copies;
* You can’t use Auto BCC with a demo domain;
* Using this feature will increase your usage. Each email copy sent will count against your quota or overage calculation.


# Webhooks

Set up webhooks to receive real-time notifications about email deliverability events and account activities within your Mailtrap account.

Webhooks allow you to receive all information about your deliverability and activities within your account (Audit Log) almost in real-time.

### Event types

**Sending events:**

* **Delivery** - Email successfully delivered
* **Bounce** - Permanent delivery failure
* **Soft bounce** - Temporary failure (will retry)
* **Spam complaint** - Recipient reported spam
* **Unsubscribe** - Recipient unsubscribed
* **Open** - Email was opened
* **Click** - Link was clicked
* **Suspension** - Message suspended
* **Reject** - Message rejected

**Audit Log events (available for enterprise only):**

* User login events
* Profile updates
* Permission changes
* And more

### How to set up webhooks

{% stepper %}
{% step %}
Navigate to **Settings** → **Webhooks** and click the **Create New Webhook** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b908e25662b6f21712959047a0da29d53dd2138f%2Fwebhooks-1.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Enter a valid **Webhook URL**. Use a password and username as an extra security layer with basic authorization to prevent others from sending information to that endpoint. You can also use a token as a query parameter or use [webhook signature](https://docs.mailtrap.io/email-api-smtp/advanced/webhooks#webhook-signature-verification).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-49ceef02cb620da85293246c9e1e2225729fd353%2Fwebhooks-2.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Choose the **Payload format** (JSON or JSON Lines).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a8df1bc312151c57c3bdb088e110e112fb0c08d2%2Fwebhooks-3.png?alt=media" alt="" width="375"></div>

Examples of payload:

{% tabs %}
{% tab title="JSON" %}
Events sent as a JSON object with an `events` array:

```json
{
  "events": [
    {"event": "delivery", "email": "user@example.com", ...}
  ]
}
```

{% endtab %}

{% tab title="JSON Lines" %}
Events sent as newline-delimited JSON:

```jsonl
{"event":"delivery","email":"user@example.com",...}
{"event":"open","email":"user@example.com",...}
```

{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
Select the webhooks area (**Audit Log** or **Email Sending**).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ba96b5306c950827e929861a54f5519975bb3f57%2Fwebhooks-4.png?alt=media" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

**If you choose Audit Log**, you will receive events related to all activities within your account that are supported by the Audit Log.

**If you choose Email Sending**, you'll also need to:

{% stepper %}
{% step %}
Choose the **Sending Stream** (Transactional or Bulk) for which you want to set up the webhooks.

{% hint style="info" %}
**Transactional Stream** is used to send user-triggered emails to one recipient at a time, while **Bulk Stream** is used to send promotional emails to multiple recipients at once.
{% endhint %}
{% endstep %}

{% step %}
Choose the **domain** you want to receive events' data for and select one or more [event types](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/statuses-and-events) by ticking the corresponding checkbox.

<div align="center" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-361ed32f9ee11e91e8ce03e8f471d1d2fb6145d2%2Fwebhooks-5.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the **Run Test** button to test the webhook setup. The code represents a dummy payload of the webhook structure and how to read it correctly. If your endpoint responds with a 200 code, you'll see a confirmation in the app. All other response codes show an error during a test.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4083f1d14ff78989b410bcb12a00fb22494c44a5%2Fwebhooks-6.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
One popular way to test webhooks outside your system is [Webhook.site](https://webhook.site/#!/view/d24cebd2-99cc-46f3-8685-c779017f39a0), but don't use it for production.
{% endhint %}
{% endstep %}

{% step %}
If the tests are successful, click the **Save** button. All information will be sent to your webhook endpoint.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aef902d761ff49e14764e74dbffb1d090f181171%2Fwebhooks-7.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
To edit, pause, or delete an active webhook, go back to the Webhooks tab and select the webhook you want to change.
{% endhint %}
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
Mailtrap webhooks are delivered only on ports 443 (for HTTPS) or 80 (for HTTP). Please be sure to use these ports only.
{% endhint %}

### Receive events (JSON format)

Receive webhook events as a JSON object containing an array of events.

Set **Payload format: JSON** in your webhook settings.

Mailtrap sends a `POST` request to your webhook URL with events as a JSON object.

**Your endpoint should:**

* Accept `Content-Type: application/json`
* Return HTTP 200 to acknowledge receipt
* Process events asynchronously

#### Payload

**events** <mark style="color:$info;">one of\[]</mark> <mark style="color:blue;">optional</mark>

<details>

<summary><mark style="color:$info;">object · SendingWebhookEvent</mark> <mark style="color:blue;">optional</mark><br><mark style="color:$info;">Email lifecycle webhook event</mark></summary>

**event** <mark style="color:$info;">string · enum</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Event type</mark>\ <mark style="color:$info;">Possible values</mark>: `delivery` `open` `click` `unsubscribe` `spam` `soft bounce` `bounce` `suspension` `reject`

**message\_id** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unique message ID</mark>&#x20;

**sending\_stream** <mark style="color:$info;">string · enum</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Sending stream used</mark>\ <mark style="color:$info;">Possible values:</mark> `transactional` `bulk`

**email** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Recipient email address</mark>

**sending\_domain\_name** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Sending domain name</mark>

**category** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Category assigned when sending</mark>

**custom\_variables** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Custom variables from the email</mark>

* **Other properties** <mark style="color:$info;">string | number | boolean</mark> <mark style="color:$primary;">optional</mark>

**timestamp** <mark style="color:$info;">integer</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unix epoch timestamp</mark>

**event\_id** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unique event ID (use for idempotency)</mark>

**reason** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Reason (for</mark> `suspension` <mark style="color:$info;">and</mark> `reject` <mark style="color:$info;">events)</mark>

**response** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Server response (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**response\_code** <mark style="color:$info;">integer</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">SMTP response code (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**bounce\_category** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Bounce category (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**ip** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">User IP address (for</mark> `open`<mark style="color:$info;">,</mark> `click`<mark style="color:$info;">,</mark> `unsubscribe` <mark style="color:$info;">events)</mark>

**user\_agent** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">User agent (for</mark> `open`<mark style="color:$info;">,</mark> `click`<mark style="color:$info;">,</mark> `unsubscribe` <mark style="color:$info;">events)</mark>

**url** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark> \ <mark style="color:$info;">Clicked URL</mark> <mark style="color:$info;">(for</mark> `click` <mark style="color:$info;">events)</mark>

</details>

<details>

<summary><mark style="color:$info;">object · ActivityLogWebhookEvent</mark> <mark style="color:$primary;">optional</mark><br><mark style="color:$info;">Account activity webhook event (Enterprise only)</mark></summary>

**event** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Activity log event type</mark>\ <mark style="color:$info;">Example:</mark> `activity_log.user.updated`

**description** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">User-friendly event description</mark>\ <mark style="color:$info;">Example:</mark> `updated the user profile`

**actor** <mark style="color:$info;">object</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">User or system that performed the action</mark>

* **id** <mark style="color:$info;">integer</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor ID</mark>\ <mark style="color:$info;">Example:</mark> `1`
* **type** <mark style="color:$info;">string · enum</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor type</mark>\ <mark style="color:$info;">Possible values:</mark> `user` `api_token`
* **name** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor name</mark>\ <mark style="color:$info;">Example:</mark> `John Doe`

**resource** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Affected resource (optional)</mark>

* **id** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource ID</mark>\ <mark style="color:$info;">Example:</mark> `1`
* **type** <mark style="color:$info;">string · enum</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource type</mark>\ <mark style="color:$info;">Possible values:</mark> `user` `api_token` `billing` `account` `sso_config` `sending_domain` `project` `inbox` `contact_list` <kbd>contact\_field</kbd> `contact_segment`
* **name** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource name</mark>\ <mark style="color:$info;">Example:</mark> `John Doe`

**changes** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Changes made (optional)</mark>\ <mark style="color:$info;">Example:</mark> `{"name":{"from":"John","to":"John Doe"}}`

* **Other properties** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>

**timestamp** <mark style="color:$info;">integer</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unix epoch timestamp</mark>\ <mark style="color:$info;">Example:</mark> `1735830138`

</details>

**Responses**

| <mark style="color:$success;">`200`</mark> | Return 200 to acknowledge successful receipt             |
| ------------------------------------------ | -------------------------------------------------------- |
| <mark style="color:$danger;">`500`</mark>  | Any other status triggers retry (40 retries every 5 min) |

**Payload**

{% tabs %}
{% tab title="Delivery" %}

```json
{
  "events": [
    {
      "event": "delivery",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "category": "Password reset",
      "custom_variables": {
        "user_id": "123"
      },
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Bounce" %}

```json
{
  "events": [
    {
      "event": "bounce",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "response": "[CS01] Message rejected due to local policy",
      "response_code": 555,
      "bounce_category": "spam",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Soft Bounce" %}

```json
{
  "events": [
    {
      "event": "soft bounce",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "response": "4.7.1 Temporary error, please retry",
      "response_code": 451,
      "bounce_category": "greylisting",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Spam" %}

```json
{
  "events": [
    {
      "event": "spam",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Suspension" %}

```json
{
  "events": [
    {
      "event": "suspension",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "reason": "Your account has reached its daily sending limit.",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Reject" %}

```json
{
  "events": [
    {
      "event": "reject",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "reason": "Recipient in suppression list. Reason: unsubscription",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Open" %}

```json
{
  "events": [
    {
      "event": "open",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "ip": "127.138.158.185",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Click" %}

```json
{
  "events": [
    {
      "event": "click",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "ip": "142.86.27.2",
      "user_agent": "Mozilla/5.0 (Windows NT x.y; Win64; x64)",
      "url": "https://mailtrap.io/email-api",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Unsubscribe" %}

```json
{
  "events": [
    {
      "event": "unsubscribe",
      "timestamp": 1728669700,
      "sending_stream": "transactional",
      "message_id": "1df37d17-0286-4d8b-8edf-bc4ec5be86e6",
      "email": "receiver@example.com",
      "event_id": "bede7236-2284-43d6-a953-1fdcafd0fdbc",
      "sending_domain_name": "examplesender.com"
    }
  ]
}
```

{% endtab %}

{% tab title="Audit Log User Login" %}

```json
{
  "events": [
    {
      "event": "activity_log.user.login",
      "description": "logged in with SSO",
      "actor": {
        "id": 1,
        "type": "user",
        "name": "John Doe"
      },
      "timestamp": 1735830138
    }
  ]
}
```

{% endtab %}

{% tab title="Audit Log: Profile Update" %}

```json
{
  "events": [
    {
      "event": "activity_log.user.updated",
      "description": "updated the user profile",
      "actor": {
        "id": 1,
        "type": "user",
        "name": "John Doe"
      },
      "resource": {
        "id": "1",
        "type": "user",
        "name": "John Doe"
      },
      "changes": {
        "name": {
          "from": "John",
          "to": "John Doe"
        }
      },
      "timestamp": 1735830138
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Receive events (JSON Lines format)

Mailtrap sends a `POST` request to your webhook URL with events in [JSON Lines](https://jsonlines.org/) format.

Each line is a separate JSON object. Parse line by line.

**Your endpoint should:**

* Accept `Content-Type: application/jsonl`
* Return HTTP 200 to acknowledge receipt
* Process events asynchronously

**Payload**

<details>

<summary><mark style="color:$info;">object · SendingWebhookEvent</mark> <mark style="color:blue;">optional</mark><br><mark style="color:$info;">Email lifecycle webhook event</mark></summary>

**event** <mark style="color:$info;">string · enum</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Event type</mark>\ <mark style="color:$info;">Possible values</mark>: `delivery` `open` `click` `unsubscribe` `spam` `soft bounce` `bounce` `suspension` `reject`

**message\_id** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unique message ID</mark>&#x20;

**sending\_stream** <mark style="color:$info;">string · enum</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Sending stream used</mark>\ <mark style="color:$info;">Possible values:</mark> `transactional` `bulk`

**email** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Recipient email address</mark>

**sending\_domain\_name** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Sending domain name</mark>

**category** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Category assigned when sending</mark>

**custom\_variables** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Custom variables from the email</mark>

* **Other properties** <mark style="color:$info;">string | number | boolean</mark> <mark style="color:$primary;">optional</mark>

**timestamp** <mark style="color:$info;">integer</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unix epoch timestamp</mark>

**event\_id** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unique event ID (use for idempotency)</mark>

**reason** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Reason (for</mark> `suspension` <mark style="color:$info;">and</mark> `reject` <mark style="color:$info;">events)</mark>

**response** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Server response (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**response\_code** <mark style="color:$info;">integer</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">SMTP response code (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**bounce\_category** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Bounce category (for</mark> `soft bounce` <mark style="color:$info;">and</mark> `bounce` <mark style="color:$info;">events)</mark>

**ip** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">User IP address (for</mark> `open`<mark style="color:$info;">,</mark> `click`<mark style="color:$info;">,</mark> `unsubscribe` <mark style="color:$info;">events)</mark>

**user\_agent** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">User agent (for</mark> `open`<mark style="color:$info;">,</mark> `click`<mark style="color:$info;">,</mark> `unsubscribe` <mark style="color:$info;">events)</mark>

**url** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark> \ <mark style="color:$info;">Clicked URL</mark> <mark style="color:$info;">(for</mark> `click` <mark style="color:$info;">events)</mark>

</details>

<details>

<summary><mark style="color:$info;">object · ActivityLogWebhookEvent</mark> <mark style="color:$primary;">optional</mark><br><mark style="color:$info;">Account activity webhook event (Enterprise only)</mark></summary>

**event** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Activity log event type</mark>\ <mark style="color:$info;">Example:</mark> `activity_log.user.updated`

**description** <mark style="color:$info;">string</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">User-friendly event description</mark>\ <mark style="color:$info;">Example:</mark> `updated the user profile`

**actor** <mark style="color:$info;">object</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">User or system that performed the action</mark>

* **id** <mark style="color:$info;">integer</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor ID</mark>\ <mark style="color:$info;">Example:</mark> `1`
* **type** <mark style="color:$info;">string · enum</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor type</mark>\ <mark style="color:$info;">Possible values:</mark> `user` `api_token`
* **name** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Actor name</mark>\ <mark style="color:$info;">Example:</mark> `John Doe`

**resource** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Affected resource (optional)</mark>

* **id** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource ID</mark>\ <mark style="color:$info;">Example:</mark> `1`
* **type** <mark style="color:$info;">string · enum</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource type</mark>\ <mark style="color:$info;">Possible values:</mark> `user` `api_token` `billing` `account` `sso_config` `sending_domain` `project` `inbox` `contact_list` <kbd>contact\_field</kbd> `contact_segment`
* **name** <mark style="color:$info;">string</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Resource name</mark>\ <mark style="color:$info;">Example:</mark> `John Doe`

**changes** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>\ <mark style="color:$info;">Changes made (optional)</mark>\ <mark style="color:$info;">Example:</mark> `{"name":{"from":"John","to":"John Doe"}}`

* **Other properties** <mark style="color:$info;">object</mark> <mark style="color:$primary;">optional</mark>

**timestamp** <mark style="color:$info;">integer</mark> <mark style="color:$warning;">required</mark>\ <mark style="color:$info;">Unix epoch timestamp</mark>\ <mark style="color:$info;">Example:</mark> `1735830138`

</details>

**Responses**

| <mark style="color:$success;">`200`</mark> | Return 200 to acknowledge successful receipt             |
| ------------------------------------------ | -------------------------------------------------------- |
| <mark style="color:$danger;">`500`</mark>  | Any other status triggers retry (40 retries every 5 min) |

**Payload**

{% tabs %}
{% tab title="Delivery events" %}

```jsonl
{"event":"delivery","timestamp":1728669927,"sending_stream":"transactional","category":"Password reset","message_id":"1df37d17-0286-4d8b-8edf-bc4ec5be86e6","email":"receiver@example.com","event_id":"bede7236-2284-43d6-a953-1fdcafd0fdbc","sending_domain_name":"examplesender.com"}
{"event":"delivery","timestamp":1728669927,"sending_stream":"transactional","category":"Email confirmation","message_id":"ca7974af-7212-42aa-99fb-cc4742d0658b","email":"another@example.com","event_id":"657b8544-6a95-4c47-997f-6e47922a5052","sending_domain_name":"examplesender.com"}
```

{% endtab %}

{% tab title="Bounce events" %}

```jsonl
{"event":"bounce","timestamp":1728669927,"sending_stream":"transactional","message_id":"1df37d17-0286-4d8b-8edf-bc4ec5be86e6","email":"receiver@example.com","event_id":"bede7236-2284-43d6-a953-1fdcafd0fdbc","response":"[CS01] Message rejected","response_code":555,"bounce_category":"spam","sending_domain_name":"examplesender.com"}
```

{% endtab %}

{% tab title="Mixed events" %}

```jsonl
{"event":"delivery","timestamp":1728669927,"message_id":"abc-123","email":"user1@example.com","event_id":"evt-1","sending_stream":"transactional","sending_domain_name":"example.com"}
{"event":"open","timestamp":1728669930,"message_id":"abc-123","email":"user1@example.com","event_id":"evt-2","sending_stream":"transactional","ip":"192.168.1.1","sending_domain_name":"example.com"}
{"event":"click","timestamp":1728669935,"message_id":"abc-123","email":"user1@example.com","event_id":"evt-3","sending_stream":"transactional","url":"https://example.com","sending_domain_name":"example.com"}
```

{% endtab %}
{% endtabs %}

### Audit Log event structure

Audit Log events include the following fields:

* **event** — The event type
  * Example: `activity_log.user.updated`
* **description** — The event description. Meant to be a user-friendly representation of the event type.
  * Example: `updated the user profile`
* **actor** — Object representing the actor who executed the action or if the action was performed by the system actor.
  * Example: `{"id":1,"type":"user","name":"Jack"}` or `{"name":"Mailtrap"}`
* **resource** — Optional object representing the resource affected by the action
  * Example: `{"id":17,"type":"sandbox","name":"Main"}`
* **changes** — Optional object representing the changes made to the resource
  * Example: `{"name":{"from":"John","to":"John Doe"}}`
* **timestamp** — The timestamp in Unix epoch format
  * Example: `1735830138`

All stats are built on the events, and you get most event information from the Mailtrap UI.

### Retry schedule and batches

#### Retry schedule

If your endpoint is down and doesn't respond with 200 OK, we'll retry multiple times. The scheduling logic is as follows:

* **Retry** - 40 retries every 5 minutes. The webhook will be considered failed if we don't receive 200 OK with all retries. If the webhook fails, we'll pause it and notify you by email. You'll need to check its settings and resume it manually.
* **Timeout** - 30 seconds. If your endpoint doesn't respond within that time, the webhook event batch will go to the retry schedule.

#### Batches

Webhooks are delivered in batches, so a single request can contain multiple events. This reduces the number of requests to your endpoint and lowers load on your infrastructure.

Mailtrap can include up to 500 events per delivery. Events are collected and sent every 30 seconds (if there are events to deliver).

The batch format depends on the webhook payload type you choose:

* **JSON**: events are sent as a JSON array in a single payload.
* **JSON Lines**: events are sent as one JSON object per line (not wrapped in an array).

### Webhook Signature Verification

Mailtrap signs all webhook requests to ensure they originate from Mailtrap and haven't been tampered with.

#### Overview

Mailtrap uses [HMAC-SHA256](https://tools.ietf.org/html/rfc2104) to sign webhook payloads. Each webhook has a unique signing secret that you can use to verify the authenticity of incoming requests.

### How it works

* Signature Header – Mailtrap includes a \`Mailtrap-Signature\` header in every webhook request.
* Signature Algorithm – The signature is computed using HMAC-SHA256.
* Signature Format – The signature is a hexadecimal-encoded string.
* Signing Secret – Each webhook has a unique signing secret (32 hex characters).

### Getting your signing secret

The signing secret is automatically generated when you create a webhook. You can view and manage your signing secret in the Mailtrap UI:

{% stepper %}
{% step %}

### Find the webhook you want to configure in to your webhooks settings

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FF5O0VlJrUxQGVP8wHl6A%2FScreenshot%202026-01-26%20at%2011.40.11.png?alt=media&#x26;token=f2595ddf-d8dc-4b49-abbf-2f658f575b09" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### The signing secret will be displayed in the webhook details

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FHYr8KtXghwGXwFnuXTsT%2FScreenshot%202026-01-26%20at%2011.18.14.png?alt=media&#x26;token=131d1bff-c56a-4d29-83cc-524bfbc3eeb4" alt=""><figcaption></figcaption></figure>

Then, you can:

* Copy the secret to use in your verification code.
* Reset it at any time from the UI if you wish to (i.e., for security reasons).

**Important**: When you reset the signing secret, the old secret becomes invalid immediately. Make sure to update your verification code with the new secret.
{% endstep %}
{% endstepper %}

#### Verifying the signature&#x20;

To verify a webhook signature, you need to:

1. Extract the \`Mailtrap-Signature\` header from the incoming request
2. Get the raw request body (as bytes/string, not parsed JSON)
3. Compute HMAC-SHA256 using your signing secret and the raw body
4. Compare the computed signature with the header value using a constant-time comparison

**Important notes:**

* **Use the raw request body** – Do not parse the JSON first. Use the raw bytes/string exactly as received.
* **Constant-time comparison** – Always use a constant-time comparison function to prevent timing attacks.
* `Content-Type` – The signature is computed on the raw body regardless of Content-Type (JSON or JSONL)

#### Code examples

{% tabs %}
{% tab title="Ruby" %}

```ruby
ruby
require 'openssl'

def verify_webhook_signature(request_body, signature_header, signing_secret)
  return false if signature_header.blank? || request_body.blank?
  
  computed_signature = OpenSSL::HMAC.hexdigest(
    OpenSSL::Digest.new('sha256'),
    signing_secret,
    request_body
  )
  
  # Use secure_compare for constant-time comparison
  Rack::Utils.secure_compare(computed_signature, signature_header)
end
```

{% endtab %}

{% tab title="Rails controller" %}

```ruby
def webhook_received
  signature = request.headers['Mailtrap-Signature']
  body = request.raw_post
  signing_secret = 'your_signing_secret_here'
  
  unless verify_webhook_signature(body, signature, signing_secret)
    head :bad_request
    return
  end
  
  # Process the webhook...
end
```

{% endtab %}

{% tab title="Python" %}

```python
import hmac
import hashlib

def verify_webhook_signature(request_body, signature_header, signing_secret):
    if not signature_header or not request_body:
        return False
    
    computed_signature = hmac.new(
        signing_secret.encode('utf-8'),
        request_body.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    # Use hmac.compare_digest for constant-time comparison
    return hmac.compare_digest(computed_signature, signature_header)
```

{% endtab %}

{% tab title="Flask" %}

```python
from flask import request

@app.route('/webhook', methods=['POST'])
def webhook_received():
    signature = request.headers.get('Mailtrap-Signature')
    body = request.get_data(as_text=True)
    signing_secret = 'your_signing_secret_here'
    
    if not verify_webhook_signature(body, signature, signing_secret):
        return '', 400
    
    # Process the webhook...
    return '', 200
```

{% endtab %}

{% tab title="Node.js / Express" %}

```javascript
const crypto = require('crypto');

function verifyWebhookSignature(requestBody, signatureHeader, signingSecret) {
  if (!signatureHeader || !requestBody) {
    return false;
  }
  
  const computedSignature = crypto
    .createHmac('sha256', signingSecret)
    .update(requestBody, 'utf8')
    .digest('hex');
  
  // Use crypto.timingSafeEqual for constant-time comparison
  const signatureBuffer = Buffer.from(signatureHeader, 'hex');
  const computedBuffer = Buffer.from(computedSignature, 'hex');
  
  if (signatureBuffer.length !== computedBuffer.length) {
    return false;
  }
  
  return crypto.timingSafeEqual(signatureBuffer, computedBuffer);
}

// Usage in Express
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['mailtrap-signature'];
  const body = req.body.toString('utf8');
  const signingSecret = 'your_signing_secret_here';
  
  if (!verifyWebhookSignature(body, signature, signingSecret)) {
    return res.status(400).send('Invalid signature');
  }
  
  // Process the webhook...
  res.status(200).send('OK');
});
```

{% endtab %}

{% tab title="Express" %}

```javascript
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['mailtrap-signature'];
  const body = req.body.toString('utf8');
  const signingSecret = 'your_signing_secret_here';
  
  if (!verifyWebhookSignature(body, signature, signingSecret)) {
    return res.status(400).send('Invalid signature');
  }
  
  // Process the webhook...
  res.status(200).send('OK');
});
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

function verifyWebhookSignature($requestBody, $signatureHeader, $signingSecret) {
    if (empty($signatureHeader) || empty($requestBody)) {
        return false;
    }
    
    $computedSignature = hash_hmac('sha256', $requestBody, $signingSecret);
    
    // Use hash_equals for constant-time comparison
    return hash_equals($computedSignature, $signatureHeader);
}

// Usage
$signature = $_SERVER['HTTP_MAILTRAP_SIGNATURE'] ?? '';
$body = file_get_contents('php://input');
$signingSecret = 'your_signing_secret_here';

if (!verifyWebhookSignature($body, $signature, $signingSecret)) {
    http_response_code(400);
    exit;
}

// Process the webhook...
```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
    "crypto/hmac"
    "crypto/sha256"
    "encoding/hex"
    "net/http"
    "strings"
)

func verifyWebhookSignature(requestBody []byte, signatureHeader, signingSecret string) bool {
    if signatureHeader == "" || len(requestBody) == 0 {
        return false
    }
    
    mac := hmac.New(sha256.New, []byte(signingSecret))
    mac.Write(requestBody)
    computedSignature := hex.EncodeToString(mac.Sum(nil))
    
    // Use hmac.Equal for constant-time comparison
    return hmac.Equal([]byte(computedSignature), []byte(signatureHeader))
}
```

{% endtab %}

{% tab title="HTTP Handler" %}

```http
func webhookHandler(w http.ResponseWriter, r *http.Request) {
    signature := r.Header.Get("Mailtrap-Signature")
    body, _ := io.ReadAll(r.Body)
    signingSecret := "your_signing_secret_here"
    
    if !verifyWebhookSignature(body, signature, signingSecret) {
        w.WriteHeader(http.StatusBadRequest)
        return
    }
    
    // Process the webhook...
    w.WriteHeader(http.StatusOK)
}
```

{% endtab %}
{% endtabs %}

#### Security best practices

* **Always verify signatures** – Never process webhooks without verifying the signature first.
* **Store secrets securely** – Keep your signing secrets in environment variables or secure secret management systems.
* **Use constant-time comparison** – Always use constant-time comparison functions to prevent timing attacks.
* **Handle missing headers gracefully** – If the signature header is missing, reject the request.
* **Rotate secrets when compromised** – If you suspect a secret has been compromised, reset it immediately in the Mailtrap UI.

#### Troubleshooting

**Signature verification fails:**

* **Check the raw body** – Make sure you're using the raw request body, not parsed JSON.
* **Verify encoding** – Ensure you're handling UTF-8 encoding correctly.
* **Check secret** – Confirm you're using the correct signing secret for the webhook.
* **Header name** – The header is case-insensitive, but ensure you're reading it correctly (\`Mailtrap-Signature\`).

**Signature header is missing:**

* This could indicate the request is not from Mailtrap
* Reject the request with a 400 Bad Request status

**Different payload formats:**

* The signature is computed on the raw body regardless of payload format (JSON or JSONL)
* Both formats use the same verification process


# Help & Support

Get help with Email API/SMTP issues and find answers to common questions.

Find answers to common questions and troubleshoot issues with Mailtrap's Email API/SMTP service. Our comprehensive help resources are designed to get you back on track quickly.

## Resources

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Frequently Asked Questions</strong></td><td><em>Browse our comprehensive FAQ section for quick answers to common questions about Email API/SMTP setup, integration, and best practices.</em></td><td><a href="help/faqs">faqs</a></td></tr><tr><td><strong>Troubleshooting Guide</strong></td><td><em>Step-by-step solutions for common issues including authentication errors, domain configuration problems, and delivery issues.</em></td><td><a href="help/troubleshooting">troubleshooting</a></td></tr></tbody></table>

## Common Issues

### Authentication & Access

* [401 Unauthorized Error](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/unauthorized-401-error) - Fix API token and authentication issues
* [Domain Not Allowed](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/sending-from-domain-not-allowed) - Resolve domain verification problems

### Email Delivery Issues

* [From Header Mismatch](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/from-header-domain-mismatch) - Fix sender address configuration
* [SSL Cipher Error](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/ssl-cipher-overlap-error) - Resolve SSL/TLS connection issues
* [Office 365 Quarantine](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/ms-office-365-quarantine) - Handle Microsoft email filtering

## Getting Help

### Self-Service Resources

1. Check the [FAQs](https://docs.mailtrap.io/documentation/email-api-smtp/help/faqs) for quick answers
2. Review the [Troubleshooting Guide](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting)
3. Search our documentation using the search bar
4. Check our [API Reference](https://api-docs.mailtrap.io/)

### <i class="fa-comments-question-check">:comments-question-check:</i>Contact Support

If you can’t find the answer you need in our documentation and would like to contact support and speak with an agent, we’re here to help.

You can get in touch with the Mailtrap Support team using one of the following ways:

* **From your Mailtrap account**&#x20;

1. Log in to your account [here](https://mailtrap.io/signin).
2. Go to the <i class="fa-circle-question">:circle-question:</i>[<mark style="color:$primary;">**Help Center**</mark>](https://mailtrap.io/help-center) > <i class="fa-message-dots">:message-dots:</i> Get Help
3. Click <mark style="color:$primary;">**Start conversation.**</mark>&#x20;

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7hftpJFYZKk1D4GQCYd8%2FScreenshot%202026-02-19%20at%2017.12.57.png?alt=media&#x26;token=90aebf2d-07b7-4c5b-aa6b-07623bc02077" alt=""><figcaption></figcaption></figure>

* **Email us at** 📧 <support@mailtrap.io>

Whether you need technical assistance, help troubleshooting an issue, or simply want to talk to customer support, our team will be happy to assist you.

### Before Contacting Support

Please have the following information ready:

* Your account email
* Error messages (exact wording)
* Request IDs from email logs
* Steps to reproduce the issue
* Screenshots if applicable

## Feedback & suggestions

*We welcome technical feedback and contributions that help us improve Mailtrap’s functionality and documentation. Please use the appropriate channel depending on the type of request.*

#### <i class="fa-bug">:bug:</i>Bug Reports

**If you encounter a product issue or unexpected behavior, please** [#contact-support](#contact-support "mention")**.**

To help us investigate efficiently, include:

* A detailed description of the issue
* Exact reproduction steps
* Relevant stream, domain, sandbox, or account details
* Timestamps (including timezone)
* Screenshots or logs if available

#### <i class="fa-file-circle-plus">:file-circle-plus:</i>Feature Requests

For product improvements or new feature proposals, use **our** [**Public Roadmap**](https://mailtrap.featurebase.app/en) **portal**.

There you can:

* **Submit a new feature request**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ff9yf6pEv5ZXR4EHh5ABg%2FScreenshot%202026-03-02%20at%2010.32.03.png?alt=media&#x26;token=2cea9a79-0387-4fb3-988d-272d13327b77" alt="" width="375"><figcaption></figcaption></figure></div>

* **Upvote existing requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fax54DgMBWcXzIQEiLeCg%2FScreenshot%202026-03-02%20at%2010.33.40.png?alt=media&#x26;token=0454c018-c008-4287-a329-407bcd3e1c35" alt="" width="375"><figcaption></figcaption></figure></div>

* **Subscribe to updates for specific requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FmB0AdDAkT5l43l0jmBps%2FScreenshot%202026-03-02%20at%2010.33.11.png?alt=media&#x26;token=790a0502-73e1-4bd2-803a-c4b4c7973d60" alt="" width="375"><figcaption></figcaption></figure></div>

#### <i class="fa-file-doc">:file-doc:</i>Documentation Improvements

If you identify unclear, incomplete, or outdated documentation:

1. Use the **feedback widget** located on the right-hand side of the page to rate the article:\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FOLpynTOT2XMAP3d7c7Ct%2FScreenshot%202026-03-02%20at%2010.30.47.png?alt=media\&token=c71836e0-95da-47ae-b9d7-917dbebc9149)
2. **Provide specific feedback** describing what should be corrected, clarified, or expanded\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FU94kVQcPPjT7e6bgJz4m%2FScreenshot%202026-03-02%20at%2010.31.22.png?alt=media\&token=7e0ec64d-058e-4b47-a25f-4bd01d40e549)

This helps us continuously refine our docs.

#### <i class="fa-square-code">:square-code:</i>GitHub & Technical Collaboration

For open-source projects, SDKs, or public repositories, join us on [GitHub](https://github.com/mailtrap).

## Quick Solutions

### Can't send emails?

1. Verify your [API token](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-tokens) is correct
2. Check your [sending domain](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain) is verified
3. Review your [sending limits](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-limits)
4. Confirm your [integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration) is properly configured

### Emails not reaching inbox?

1. Check [email logs](https://docs.mailtrap.io/documentation/email-api-smtp/analytics/logs) for delivery status
2. Review [bounce categorization](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/bounce-categorization) for issues
3. Verify SPF, DKIM, and DMARC records
4. Check if recipients are on [suppressions list](https://docs.mailtrap.io/documentation/email-api-smtp/deliverability/suppressions-list)

### Integration issues?

1. Review the [API integration guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration)
2. Check the [SMTP integration guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
3. Test with [Email Sandbox](https://docs.mailtrap.io/documentation/email-sandbox/overview) first
4. Use our [API reference](https://api-docs.mailtrap.io/) for detailed endpoints


# Sending Glossary

Definitions of key terms and phrases used in Mailtrap Email API/SMTP, including DNS records, email events, SMTP settings, and deliverability concepts.

This glossary explains key terms and phrases used in Mailtrap Email API/SMTP.

## A

**API sending** — Send emails using Mailtrap's API endpoints. Our API is compatible with SendGrid, Mandrill, and Mailgun APIs.

**AWS CLI** — An abbreviation for Amazon Web Services Command Line Interface. It's a tool to control and manage AWS resources. Mailtrap provides DNS records in JSON format for AWS Route53 to create records using AWS CLI.

**AWS Route53** — A DNS service from Amazon. If you use it, you can copy-paste the DNS records in JSON format and add them to AWS Route53.

## B

**Bounce** — One of the possible events, also known as "hard bounce". Most commonly, a bounce occurs when the recipient's email address is incorrect or the server declines a message. It indicates a permanent failure of delivery. You won't be able to send any further emails to this address from this domain.

**Bounce rate** — The percentage of bounced emails. A bounce event may happen due to an invalid address, your email not passing certain mailbox provider criteria, or a connection issue. Note that it's the recipients who bounce the emails, not Mailtrap. To secure great deliverability in the long run, you want to keep the bounce rate low.

## C

**Category** — A method used to categorize different types of emails sent from your Mailtrap account. You specify a category when creating an email as one of its parameters. For each unique category specified this way, you'll be able to see separate email analytics. Example categories can include password reset, invoice, welcome email, etc.

**Click** — An event that occurs when a link in your email is clicked. Click tracking must be enabled prior to sending an email for any clicks to be recorded.

{% hint style="info" %}
When an email with click tracking enabled is forwarded, all further clicks will also be included in the click count.
{% endhint %}

**Click rate** — The percentage of opened emails that got one or more clicks on their links. All clicks are recorded and can be seen under Events History in the Email Logs menu. But only the first click is calculated towards the Click Rate within a selected period.

**Client sending IP** — IP address of a device that was used to send an email.

**cURL** — A command-line tool to transfer data using various protocols and an option to quickly make API calls. With Mailtrap, you get a sample cURL code with an API to send an email to yourself.

## D

**DNS records** — A DNS record is an instruction stored at a DNS server. It describes how to handle requests from that domain. Certain records you add give Mailtrap a guarantee that you own the domain and have the right to send from it. Other records let mailbox providers know that you're an authenticated server and boost your email deliverability.

### DNS record types

| Record type                     | Description                                                                                                                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CNAME domain authentication** | DNS record used for verification purposes. Mailtrap uses it to verify that you're the owner of a domain and can send through it.                                                                                                                                       |
| **SPF**                         | A very common TXT-type authentication method. It specifies which IP addresses (mail servers) are authorized to send emails on your behalf.                                                                                                                             |
| **DKIM**                        | A CNAME type authentication method, an encrypted digital signature that comes with each email. Mailtrap uses private keys to sign the body and the header of your emails before sending them to the mailbox providers.                                                 |
| **DMARC**                       | A TXT type email authentication protocol used to ensure an authenticated email domain aligns with the domain found in the `from:` address. It's an additional security layer that tells mailbox providers what to do with your emails should they fail authentication. |

**Domain** (or **Sending Domain**) — The domain used in the `from:` field of an email. You must be the owner of a domain and have it verified to be able to send emails from Mailtrap. No public domains can be used with Mailtrap Sending (e.g. Gmail, Hotmail).

## E

**Email Logs** — The list of all the emails sent from your account. Contains all the vital details of each message, including the recipient's details, timestamps, HTML/CSS of a message, opens/clicks stats, as well as additional tools, such as email preview or spam check.

**Event** — A particular action that occurred to your email. The available events are: Sending, Delivery, Reject, Open, Click, Bounce, Spam, Unsubscribe, Soft Bounce, Suspension. In the Email Logs, you can view all the events associated with a particular message in chronological order.

## M

**Mailbox provider** — An email service used by the end recipient to receive emails. Examples include Gmail, Outlook, Cisco email protection, or Mimecast email protection.

**Mailtrap sending IP** — IP address of Mailtrap, used to send a message to the final recipient.

## O

**Open** — An event that occurs when an email is opened. Mailtrap inserts an invisible pixel into an email. When a message is opened and a pixel is "displayed", an 'open' event is recorded.

{% hint style="info" %}
Some mailbox providers, browsers, and plugins block the tracking of opens. Users or their providers can also block images from being displayed. In each of these cases, no "open" event will be recorded even if an email is opened.
{% endhint %}

## R

**Recipient IP** — IP address of a device or an email server where an email was opened. If a message is opened on devices using different IP addresses, multiple recipient IPs will be recorded. If a message is not opened at all, no recipient IP will be displayed.

## S

**SMTP** — Short for Simple Mail Transfer Protocol, SMTP is a protocol that facilitates email transmissions.

### SMTP Settings

| Setting      | Description                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Host**     | Name of Mailtrap's outgoing email sending server.                                                                                                                                                 |
| **Port**     | Communication endpoints responsible for moving email data between servers via SMTP. Mailtrap supports 587, 2525, and 25 ports. We recommend using 587 because it's the standard secure SMTP port. |
| **Username** | When configuring Mailtrap Sending with SMTP, the username is 'api'.                                                                                                                               |
| **Password** | Mailtrap uses API tokens as SMTP passwords. By default, a token is generated when you add a domain.                                                                                               |
| **Auth**     | Authentication mechanism that Mailtrap supports. We use two common mechanisms: LOGIN, PLAIN.                                                                                                      |
| **TLS**      | Short for Transport Layer Security, TLS is a protocol that encrypts and delivers mail securely.                                                                                                   |

**Spam** — One of the possible email events. This happens when a recipient chooses to report a message as spam. No further messages will be delivered to such recipients. Recurring spam complaints are known to very negatively influence email deliverability.

**Spam complaints** — The percentage of delivered emails that got labeled as spam by recipients. It also includes the emails that got automatically labeled as spam by mailbox providers.

**Status** — Indicates the most recent state of your message. The available statuses are: Delivered, Not Delivered, Enqueued, and Opted Out. An email can have only one status at a time.

**Suppression list** — A list of email addresses that Mailtrap won't send any further emails to. Email addresses land on a suppression list when a message bounces, a recipient unsubscribes, or they report an email as spam.

{% hint style="info" %}
Suppression lists are individual for each of your sending domains. If an address lands on such a list for domain X, it won't prevent you from sending emails to them from other verified domains.
{% endhint %}

## T

**Transactional email** — The type of email triggered by a user's action (e.g. registration, password reset, etc.) or a certain event in the system (monthly invoice, notification about a limit reached, etc.). Transactional emails are usually triggered separately for each recipient, as opposed to marketing or sales emails that are traditionally sent in batches.

## U

**Unique open rate** — The percentage of opened emails out of all delivered emails within a specified period. Recipients may block tracking on their end, so the actual open rate could be higher than what you see in Mailtrap.

**Unsubscribe** — One of the possible events. It occurs when a recipient of your email clicks on the "unsubscribe" link in your message. No further emails will be sent to this recipient from a given domain.


# FAQs

Frequently asked questions about Mailtrap Email API/SMTP.

This page covers frequently asked questions about Mailtrap Email API/SMTP. For technical issues and error troubleshooting, see the [Troubleshooting section](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting).

#### Getting Started

<details>

<summary>What is Mailtrap?</summary>

Mailtrap is an email delivery service to send transactional and promotional emails. Popular among developer and product teams for its Email API and SMTP solutions.

</details>

<details>

<summary>How do I integrate Mailtrap with my application?</summary>

1. [Sign up](https://mailtrap.io/register/signup/) for an account.
2. Go to Email Sending and select [Sending Domains](https://mailtrap.io/sending/domains).
3. After you've added and verified all the DNS records, wait for the Compliance Check to be completed.
4. Proceed to integrate Mailtrap with your application via SMTP or API.

Learn more:

* [API Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)

If you have any questions, contact us at <support@mailtrap.io>.

</details>

<details>

<summary>Can I send emails without my domain?</summary>

No, you can't.

To send emails, Mailtrap requires you to add a sending domain, authenticated and verified using the DNS records Mailtrap provides.

</details>

<details>

<summary>Can I send emails on behalf of other domains?</summary>

No, you can't.

If you verified mydomain.com, you can send emails only on behalf of your domain.

</details>

#### Domain Setup

<details>

<summary>Should I use my domain name with www. ?</summary>

No, you should use your domain without it.

Please check our [Sending Domain Setup Guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain) for detailed instructions on adding and verifying your domain.

</details>

<details>

<summary>When I add a domain to Mailtrap, does that include subdomains?</summary>

No, you need to add and verify each subdomain/domain separately.

</details>

#### Features & Capabilities

<details>

<summary>Can I receive emails with Mailtrap?</summary>

Right now, Mailtrap doesn't provide MX records to catch inbound emails, so they'll bounce.

Another option is to use a real email address in the "reply-to" field if a recipient replies to your email.

</details>

<details>

<summary>Can I send emails to end-users with Mailtrap?</summary>

Yes, you can. Mailtrap is an email delivery service to send transactional and promotional emails. Popular among developer and product teams for its Email API and SMTP solutions.

</details>

<details>

<summary>Can I force an encrypted connection?</summary>

Yes, you can enforce encrypted connections. Mailtrap SMTP server uses STARTTLS, which works for all SMTP ports. We support only TLS connections because of the POODLE vulnerability (SSLv2 and SSLv3 are disabled).

</details>

<details>

<summary>I would like to whitelist live.smtp.mailtrap.io on my firewall. What is Mailtrap's IP range?</summary>

We use AWS with auto-balancing, so our IP ranges are the following: <https://ip-ranges.amazonaws.com/ip-ranges.json>

</details>

#### Billing & Limits

<details>

<summary>How does Mailtrap billing work?</summary>

We bill each email. For example, if an email has 3 recipients - we bill 3 of them. If it has + 3 in CC, we bill 6 together. The same goes for recipients in BCC.

</details>

<details>

<summary>What is the email size limit?</summary>

The maximum size of an email with attachments for Mailtrap is 10 MB. Upon request, we can extend the limit in some cases to 30 MB.

</details>

<details>

<summary>What is the monthly message limit for email sending?</summary>

It's the maximum number of emails you can send with Mailtrap per month. The total number of emails per month depends on the subscription plan.

If you reach your monthly limit, you'll receive the SMTP protocol error: "535 5.7.0 Monthly messages limit reached". We also send out notifications for having used 80%, 90%, and 100% of the monthly limit.

To continue sending when you're over the limit, please upgrade your subscription plan. Alternatively, you can wait until the next billing period starts, when the limit is reset.

For more details, check the [Sending Limits](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-limits) and [Pricing page](https://mailtrap.io/pricing/?tab=api).

</details>

<details>

<summary>How much does Mailtrap cost?</summary>

Mailtrap offers flexible pricing plans that scale with your email volume, from starter plans for small projects to enterprise solutions for high-volume senders.

For current pricing and to choose a plan that best fits your needs, visit our [pricing page](https://mailtrap.io/pricing/?tab=api).

</details>

#### Data & Privacy

<details>

<summary>Is it possible to export Email logs?</summary>

Right now, it's not possible, but there's a workaround.

You can set up [Webhooks](https://docs.mailtrap.io/documentation/email-api-smtp/advanced/webhooks) to automatically collect logs. And you can use a tool like [Zapier](https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/integrations/zapier), for example, to create a spreadsheet from your webhooks.

</details>

<details>

<summary>Does Mailtrap comply with the GDPR?</summary>

The General Data Protection Regulation (GDPR) came into effect on May 25, 2018. We have implemented appropriate technical and security processes to ensure Mailtrap's full compliance with this regulation.

For more details, refer to our:

* [Privacy Policy](https://mailtrap.io/privacy/)
* [Navigational Information](https://mailtrap.io/navigational-info/)
* [Data Protection Agreement](https://mailtrap.io/dpa/)

</details>

<details>

<summary>Do you have a bug bounty program?</summary>

We do not. In case you have found a vulnerability on our website that you are eager to report to us, you are welcome to do so at <support@mailtrap.io>. All issue reporters will be mentioned on our [changelog page](https://mailtrap.io/changelog/).

</details>


# Troubleshooting

Common issues and solutions for Mailtrap Email API/SMTP.

This section covers common issues you might encounter when using Mailtrap Email API/SMTP and their solutions.

### Common Issues

#### Authentication & Authorization

* [Unauthorized Error (401 Code)](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/unauthorized-401-error) - Issues with API credentials, tokens, or domain verification
* [Sending from Domain Not Allowed](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/sending-from-domain-not-allowed) - Domain verification and FROM address problems

#### Email Delivery

* [From Header Domain Mismatch](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/from-header-domain-mismatch) - Fixing FROM header configuration issues

#### SSL & Security

* [SSL Cipher Overlap Error (Error 1001)](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/ssl-cipher-overlap-error) - Custom tracking domain SSL certificate issues

#### Third-Party Services

* [MS Office 365 Quarantine](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/ms-office-365-quarantine) - Mailtrap emails going to Office 365 quarantine

### Need More Help?

If you don't find the solution to your problem here:

1. Check our [FAQs](https://docs.mailtrap.io/documentation/email-api-smtp/help/faqs) for general questions
2. Contact support at <support@mailtrap.io>
3. Visit the API documentation for technical details


# 401 Unauthorized Error

How to fix "Unauthorised" (401) authentication errors in Mailtrap Email API/SMTP.

If you're getting an "Unauthorised" error (401 code) when trying to send emails, there are several possible causes and solutions.

### Common Causes

**1. Sending from Unverified Domain**

Make sure you're sending from the domain that you've set up and verified in Mailtrap. Using any other domain will result in this error.

{% hint style="danger" %}
If you verified `example.com`, you can only send from `*@example.com` addresses. Attempting to send from `otherdomain.com` will fail with a 401 error.
{% endhint %}

**2. API Token Permissions**

If you've configured a custom API token for your domain, make sure it has proper permissions to send emails.

Check your [API tokens](https://mailtrap.io/api-tokens) and verify the token has:

* Email sending permissions
* Access to the correct domain
* Valid expiration date (if applicable)

**3. Incorrect Credentials**

Make sure you're using the correct SMTP/API credentials provided in the Integration tab of your domain.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2caae3c1dba9c159c8b60f02ce10b2620f155f8d%2Ftroubleshoot-sending-credentials-both-streams.png?alt=media" alt="Integration tab showing SMTP and API credentials for both Transactional Stream and Bulk Stream in Mailtrap"><figcaption><p>SMTP and API credentials in Integration tab</p></figcaption></figure></div>

### How to Fix

{% stepper %}
{% step %}
**Verify Your Domain**

1. Go to [Sending Domains](https://mailtrap.io/sending/domains)
2. Ensure your domain shows the **Verified** badge
3. If not verified, complete the DNS record setup
   {% endstep %}

{% step %}
**Check API Token (if using custom tokens)**

1. Go to [API Tokens](https://mailtrap.io/api-tokens)
2. Verify the token has **Send Email** permissions
3. Ensure it's assigned to the correct domain
4. Check that the token hasn't expired
   {% endstep %}

{% step %}
**Verify Credentials**

Navigate to: **Sending Domains > Integration > Integrate** (under Transactional or Bulk Stream)

Copy the exact credentials shown there:

* For SMTP: Username and Password
* For API: API Token

Replace your current credentials with these values.
{% endstep %}

{% step %}
**Test with cURL**

Use the cURL code example to test if the error persists:

1. Go to **Sending Domains > Integration > Integrate**
2. Select your stream (Transactional or Bulk)
3. Go to **Code Samples > cURL**
4. Copy and run the cURL command

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b7c7048f01d78409e4c08a9306434233329e62ef%2Ftroubleshoot-sending-code-samples.png?alt=media" alt="Code Samples section in Mailtrap showing cURL integration example" width="563"><figcaption><p>Code Samples section with cURL example</p></figcaption></figure></div>

If the cURL test succeeds but your application fails, the issue is with your application's configuration.
{% endstep %}
{% endstepper %}

### Still Having Issues?

If you've verified all the above and still getting 401 errors:

* Double-check that your FROM address domain matches your verified domain
* Ensure there are no extra spaces or special characters in your credentials
* Contact support at <support@mailtrap.io> with:
  * Your domain name
  * The exact error message
  * A code sample showing how you're attempting to send

### Related Articles

* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [API Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-integration)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [Sending from Domain Not Allowed](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/sending-from-domain-not-allowed)


# Domain Not Allowed

How to fix "Sending from domain is not allowed" (550 5.7.1) error in Mailtrap Email API/SMTP.

### Error Message

```
Error: Mail command failed: 550 5.7.1 Sending from domain is not allowed
```

This error occurs when you try to send an email using SMTP with a domain that doesn't match your verified domain in Mailtrap.

### Common Causes

**1. Domain Mismatch**

You're sending an email with `FROM: {anything}@mydomain.com`, but in Mailtrap, you've verified `anotherdomain.com`.

**The verified domain and FROM domain in your emails must match.**

{% hint style="warning" %}
If you verified `example.com` in Mailtrap, you can only send emails from `*@example.com` addresses.
{% endhint %}

**2. Domain Not Verified or Compliance Check Failed**

Your domain might not be fully verified, or you haven't passed the Compliance Check.

### How to Fix

{% stepper %}
{% step %}
**Check Your Verified Domains**

Go to [Sending Domains](https://mailtrap.io/sending/domains) in your Mailtrap account.
{% endstep %}

{% step %}
**Verify Domain Status**

Look for the **Verified** badge next to your domain. If you don't see it:

1. Click on the domain
2. Check if all DNS records are found by Mailtrap (all should be green)
3. If any records are missing or incorrect, update them with your DNS provider
   {% endstep %}

{% step %}
**Check Compliance Status**

Scroll down to see the **Compliance Check** status.

If the compliance check hasn't passed:

* Review any additional steps required
* Complete any pending actions
* Wait for the check to complete
  {% endstep %}

{% step %}
**Update Your FROM Address**

Ensure your application sends emails from an address that matches your verified domain:

* **Correct:** `noreply@yourdomain.com` (if `yourdomain.com` is verified)
* **Incorrect:** `noreply@otherdomain.com` (if `otherdomain.com` is not verified)
  {% endstep %}
  {% endstepper %}

### Related Articles

* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [Unauthorized Error (401 Code)](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/unauthorized-401-error)


# From Header Mismatch

How to fix "From: Header does not match the sender's domain" error in Mailtrap Email API/SMTP.

### Error Message

```
From: Header does not match the sender's domain
```

This error occurs when the `From:` header in your email doesn't match your verified domain in Mailtrap.

### The Requirement

To send email with Mailtrap, your `From:` header **must match** your verified domain.

{% hint style="info" %}
**Example:** If your verified domain in Mailtrap is `acme.com`, your `From:` address must be `{anything}@acme.com`.

If you're sending from a subdomain like `mail.acme.com`, your `From:` address must match that subdomain exactly.
{% endhint %}

### Common Causes

**1. Unverified Domain**

Your domain hasn't been added or verified in Mailtrap yet.

**Solution:**

1. Go to [Sending Domains](https://mailtrap.io/sending/domains)
2. Add your domain
3. Complete the DNS verification process

**2. Envelope From vs Header From Mismatch**

In some frameworks (like Laravel), the `MAIL_FROM_ADDRESS` variable is used for the envelope from address, but it's not the same as the header `From:` address.

{% hint style="warning" %}
Make sure both the **envelope from** and the **header from** use the same domain.
{% endhint %}

**3. Subdomain Confusion**

If you verified `example.com` but are trying to send from `mail.example.com`, you need to verify the subdomain separately.

### How to Fix

{% stepper %}
{% step %}
**Verify Your Domain**

First, check if your domain has been added to your Mailtrap account.

1. Go to [Sending Domains](https://mailtrap.io/sending/domains)
2. Look for your domain in the list
3. Ensure it has the **Verified** badge

If not verified, complete the DNS setup process.
{% endstep %}

{% step %}
**Check Your Email Configuration**

Ensure your email message has a `From:` header that contains an address on your verified domain.

**Example for Laravel:**

{% code title=".env" %}

```bash
MAIL_FROM_ADDRESS=noreply@yourdomain.com
MAIL_FROM_NAME="Your App Name"
```

{% endcode %}

Make sure `MAIL_FROM_ADDRESS` uses your verified domain.
{% endstep %}

{% step %}
**Verify Envelope From Matches Header From**

Most likely, the envelope from address is set separately from the header. Make sure they match.

For Laravel specifically:

* Check that `MAIL_FROM_ADDRESS` in your `.env` file matches your verified domain
* Verify this address is used in both the envelope and header
  {% endstep %}

{% step %}
**Test Your Configuration**

Send a test email and verify:

* The `From:` header shows your verified domain
* The envelope from (visible in email headers) matches
* No errors appear in your logs
  {% endstep %}
  {% endstepper %}

### Framework-Specific Examples

**Laravel**

In your `.env` file:

{% code title=".env" %}

```bash
MAIL_MAILER=smtp
MAIL_HOST=live.smtp.mailtrap.io
MAIL_PORT=587
MAIL_USERNAME=your-smtp-username
MAIL_PASSWORD=your-smtp-password
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=noreply@yourdomain.com
MAIL_FROM_NAME="${APP_NAME}"
```

{% endcode %}

Ensure `MAIL_FROM_ADDRESS` uses your verified domain.

**Other Frameworks**

The principle is the same across all frameworks:

1. Set your `From:` address to use your verified domain
2. Ensure both envelope and header from addresses match
3. Verify the domain in Mailtrap before sending

### Still Having Issues?

If you've verified your domain and updated your configuration but still see this error:

* Check your email sending code for hardcoded `From:` addresses
* Look for middleware or plugins that might be modifying the `From:` header
* Review your framework's documentation for email configuration
* Contact support at <support@mailtrap.io>

### Related Articles

* [Sending Domain Setup](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [SMTP Integration](https://docs.mailtrap.io/documentation/email-api-smtp/setup/smtp-integration)
* [Sending from Domain Not Allowed](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/sending-from-domain-not-allowed)
* [Unauthorized Error (401 Code)](https://docs.mailtrap.io/documentation/email-api-smtp/help/troubleshooting/unauthorized-401-error)


# SSL Cipher Error

How to fix SSL errors when using custom domains for click tracking in Mailtrap Email API/SMTP.

When using a custom domain for click tracking, you may encounter `SSL_ERROR_NO_CYPHER_OVERLAP` or `Error 1001` error.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-eac083264592d53fee719c7df4cbf7a9087d03db%2Ftroubleshoot-sending-ssl-error.png?alt=media" alt="Browser showing SSL_ERROR_NO_CYPHER_OVERLAP or Error 1001 when accessing custom tracking domain" width="563"><figcaption><p>SSL error when accessing custom domain for click tracking</p></figcaption></figure>

### Understanding Custom Domain Click Tracking

Mailtrap allows you to use your own domain for click tracking. To achieve this:

1. You add an `mt-link` CNAME record during the domain setup process
2. Mailtrap issues a security certificate for the mt-link subdomain to ensure a secure connection
3. Certificates from **Let's Encrypt** and **Google Trust Services** are used

### The Cause of the Error

Some domains have a list of trusted Certificate Authorities (CAs) specified in **CAA records**.

{% hint style="warning" %}
If your CAA records don't include Google Trust Services and Let's Encrypt, Mailtrap won't be able to request certificates from them. This prevents click tracking from working because browsers can't establish a secure connection.
{% endhint %}

### Checking Your CAA Records

You can check the CAA records for your domain using this command:

{% code title="Terminal" %}

```bash
dig CAA example.com
```

{% endcode %}

The output might look similar to this:

{% code title="Sample Output" %}

```
;; ANSWER SECTION:
example.com.   13990    IN    CAA    0 issue "globalsign.com"
example.com.   13990    IN    CAA    0 issuewild "globalsign.com"
```

{% endcode %}

In this example, the domain only allows GlobalSign to issue certificates, which is why Mailtrap cannot obtain a certificate.

### Solution: Update CAA Records

You have two options:

**Option 1: Add Required CAs (Recommended)**

If you want to keep your existing CAA records, modify them to include Google Trust Services and Let's Encrypt:

{% code title="Required CAA Records" %}

```
# Google Trust Services
0 issue "pki.goog; cansignhttpexchanges=yes"

# Let's Encrypt
0 issue "letsencrypt.org"
```

{% endcode %}

**Option 2: Remove CAA Restrictions**

If you don't need to restrict which CAs can issue certificates for your domain, you can remove the CAA records entirely.

### How to Add CAA Records

**CAA Record Configuration**

<table><thead><tr><th width="148.625">Field</th><th width="318.66015625">Value</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>blank or <code>@</code>, depending on your provider</td><td></td></tr><tr><td>TTL</td><td>1 hour or any other appropriate TTL</td><td>Controls how long the record is valid.</td></tr><tr><td>Flag</td><td>0</td><td><code>0</code> means that no flags have been set. Please read your DNS provider's documentation for specific behavior.</td></tr><tr><td>Tag</td><td>issue</td><td>Allows the CA to issue certificates for this domain and its subdomains (e.g., mt-link subdomain).</td></tr><tr><td>Domain</td><td><code>pki.goog; cansignhttpexchanges=yes</code> <strong>OR</strong> <code>letsencrypt.org</code></td><td>Google Trust Services needs the additional parameter <code>cansignhttpexchanges=yes</code>.</td></tr></tbody></table>

{% hint style="info" %}
You'll need to create **two separate CAA records**: one for Google Trust Services and one for Let's Encrypt.
{% endhint %}

### Verification

After updating your CAA records:

{% stepper %}
{% step %}
**Wait for DNS Propagation**

It can take several hours for the changes to your CAA records to propagate. This varies by DNS provider and TTL settings.
{% endstep %}

{% step %}
**Verify CAA Records**

Run the `dig CAA example.com` command again to confirm the new records are in place.
{% endstep %}

{% step %}
**Test Your mt-link Subdomain**

Once propagated, you should be able to access your mt-link subdomain without SSL errors:

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-108f68d7bc93b30bb4b39735cce4a851b925dc8b%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### Additional Resources

For DNS setup guides specific to your provider, see:

* AWS Route 53 Setup Guide
* Cloudflare DNS Setup Guide
* GoDaddy DNS Setup Guide

### Need Help?

If you're still experiencing SSL errors after updating CAA records:

* Wait at least 24 hours for full DNS propagation
* Verify the records are correctly formatted (check for typos)
* Contact your DNS provider for CAA record support
* Reach out to Mailtrap support at <support@mailtrap.io>


# Office 365 Quarantine

How to resolve your emails sent from Mailtrap Email API/SMTP being sent to Office 365 quarantine.

Sometimes transactional messages from Mailtrap (such as email confirmations, invitations to join a sandbox, invoices, etc.) can be sent to Threat Management >> Quarantine by MS Office 365.

### Solution

If you have faced this issue, follow these steps to resolve it:

{% stepper %}
{% step %}
**Access Office 365 Quarantine**

Go to <https://protection.office.com/#/quarantine>.
{% endstep %}

{% step %}
**Select Mailtrap Emails**

Select the emails sent from Mailtrap that are in quarantine.
{% endstep %}

{% step %}
**Release Messages**

Click the **Release messages** button.
{% endstep %}

{% step %}
**Add to Allow List**

Check the **"Add sender to your organization's allow list"** checkbox.

This will prevent future emails from Mailtrap from being quarantined.
{% endstep %}
{% endstepper %}

### Alternative: OAuth Integration

When signing up for Mailtrap, you have the option to use Office 365 account authorization (OAuth) for smooth integration. In this case, email confirmation won't be required and you can avoid quarantine issues altogether.

### Related Articles

* [Getting Started with Email API/SMTP](https://docs.mailtrap.io/documentation/email-api-smtp/setup/sending-domain)
* [Email API/SMTP FAQs](https://docs.mailtrap.io/documentation/email-api-smtp/help/faqs)


# Overview

Test and preview emails safely in a sandbox environment before sending to production

Email Sandbox is a safe testing environment that captures all your test emails, preventing them from reaching real inboxes. Perfect for development, QA testing, and staging environments, it ensures your email functionality works flawlessly before going live.

## What is Email Sandbox?

Email Sandbox acts as a **fake SMTP** server that traps all emails sent from your application. Instead of delivering to actual recipients, emails are captured in a secure inbox where you can:

* Preview how emails look across different clients
* Test email workflows without risk
* Validate HTML rendering and responsiveness
* Debug email issues before production
* Share test results with your team

## Key Features

### Safe Testing Environment

* **Zero Risk**: Emails never reach real recipients
* **Multiple Sandboxes**: Separate environments for different projects
* **Email Address per Sandbox**: Unique inbound email addresses for each sandbox
* **Team Collaboration**: Share sandboxes with team members

### Email Analysis Tools

* **HTML/Text Preview**: See exactly how emails render
* **Spam Score Analysis**: Predict spam filter behavior
* **Email Headers**: Inspect all technical details
* **Attachment Support**: Test file attachments

### Advanced Testing

* **Bounce Emulation**: Test bounce handling
* **API & SDKs**: Full programmatic access with official SDKs

### Collaboration Features

* **Shared Sandboxes**: Team-wide access
* **Email Forwarding**: Share specific test cases
* **Access Control**: Manage permissions

## Use Cases

### Development Testing

Perfect for developers building email features:

* Test email templates during development
* Verify dynamic content and personalization
* Debug email sending logic
* Test different email scenarios
* Validate email formatting

### QA & Staging

Essential for quality assurance:

* End-to-end workflow testing
* Cross-client compatibility checks
* Regression testing
* Performance testing
* User acceptance testing

### Email Design

Ideal for designers and marketers:

* Preview email designs
* Test responsive layouts
* Check image rendering
* Validate link tracking
* Review content formatting

## How It Works

### 1. Simple Integration

Choose your integration method:

**SMTP Configuration:**

```
Host: sandbox.smtp.mailtrap.io
Port: 2525
Username: YOUR_SANDBOX_USERNAME
Password: YOUR_SANDBOX_PASSWORD
```

**Unique Email Addresses:** Each sandbox provides unique @mailtrap.io addresses for inbound testing.

### 2. Send & Receive Test Emails

* **Outbound**: Your application sends emails normally - Sandbox captures them
* **Inbound**: Send emails to your sandbox's unique addresses for testing replies and parsing

### 3. Review & Analyze

Access your sandbox to preview, test, and share all captured emails (both sent and received).

## Quick Start

{% stepper %}
{% step %}
**Create a Sandbox**

Log in and create your first sandbox. Name it based on your project or environment.
{% endstep %}

{% step %}
**Configure Your App**

Update your application's SMTP settings with sandbox credentials.
{% endstep %}

{% step %}
**Send Test Email**

Send a test email from your application to verify the connection.
{% endstep %}

{% step %}
**Analyze Results**

Review the captured email in your sandbox inbox.
{% endstep %}
{% endstepper %}

## Integration Methods

### SMTP Integration

Works with any application or framework:

```python
# Python example
import smtplib

server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525)
server.login('username', 'password')
server.sendmail(from_addr, to_addr, message)
```

### API Integration with Official SDKs

Full programmatic access with our official SDKs for all major languages:

**Node.js SDK:**

```javascript
const { MailtrapClient } = require("mailtrap");

const client = new MailtrapClient({
  token: "YOUR_API_TOKEN",
  testInboxId: INBOX_ID
});

// Send test email
await client.testing.send({
  from: { email: "test@example.com" },
  to: [{ email: "user@example.com" }],
  subject: "Test Email",
  text: "Testing in sandbox"
});
```

**PHP SDK:**

```php
use Mailtrap\MailtrapClient;
use Mailtrap\Helper\ResponseHelper;

$mailtrap = new MailtrapClient('YOUR_API_TOKEN');

// Get sandbox messages
$response = $mailtrap->sandbox()
    ->inbox(INBOX_ID)
    ->messages()
    ->get();
```

**Available SDKs:**

* Node.js/TypeScript
* PHP
* Python
* Ruby
* Java
* Go
* .NET

### Email Address per Sandbox

Each sandbox automatically gets unique email addresses:

```
# Example addresses for your sandbox:
sandbox-12345@inbox.mailtrap.net
test-project-67890@inbox.mailtrap.net

# Test inbound email processing:
1. Send email to your sandbox address
2. Process received email via API/SDK or review in your Sandbox
3. Test reply handling and parsing
```

### Framework Examples

Pre-configured for popular frameworks:

* Laravel
* Ruby on Rails
* Django
* Spring Boot
* others

## Testing Capabilities

### Email Validation

* **HTML Validation**: Check for rendering issues
* **Attachment Testing**: Validate file handling

### Deliverability Testing

* **Spam Score**: SpamAssassin scoring
* **Blacklist Check**: IP reputation verification
* **Header Analysis**: Technical validation

## Best Practices

### Environment Separation

* Use different sandboxes for dev, staging, QA
* Name sandboxes clearly (e.g., "iOS App - Dev")
* Document sandbox purposes

### Testing Strategy

* Test both happy path and edge cases
* Check mobile responsiveness
* Test with real data (safely)
* Automate repetitive tests

## Getting Started

{% columns %}
{% column %}
**Setup Guides**

* [Application Integration](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-smtp-integration)
* [Sandbox API](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-api-integration)
* [Email Address Setup](https://docs.mailtrap.io/documentation/email-sandbox/setup/email-address-per-sandbox)
  {% endcolumn %}

{% column %}
**Testing Tools**

* [Email Inspector](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-template)
* [HTML Check](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-html)
* [Deliverability Tests](https://docs.mailtrap.io/documentation/email-sandbox/testing/spam-blacklist-reports)
* [Bounce Emulator](https://docs.mailtrap.io/documentation/email-sandbox/testing/bounce-rate)
  {% endcolumn %}
  {% endcolumns %}

## Support & Resources

* [Features and Limits](https://docs.mailtrap.io/documentation/email-sandbox/help/features-and-limits)
* [Sandbox Glossary](https://docs.mailtrap.io/documentation/email-sandbox/help/glossary)
* [FAQs](https://docs.mailtrap.io/documentation/email-sandbox/help/faqs)
* [Troubleshooting](https://docs.mailtrap.io/documentation/email-sandbox/help/troubleshooting)

## Next Steps

1. [**Create your first sandbox**](https://docs.mailtrap.io/documentation/email-sandbox/setup) - Get started in minutes
2. [**Integrate with your app**](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-smtp-integration) - Configure SMTP settings
3. [**Test email templates**](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-template) - Validate your emails
4. [**Share with team**](https://docs.mailtrap.io/documentation/email-sandbox/collaboration/sharing-sandboxes) - Collaborate on testing


# Setup & Configuration

Get Email Sandbox configured and integrated with your application

Get started with Email Sandbox quickly and easily. This section covers everything you need to integrate Email Sandbox into your development workflow.

## Integration Options

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Application Integration</strong></td><td><em>Step-by-step guide to integrate Email Sandbox with your application. Learn how to configure SMTP settings, use API endpoints, and route test emails to your sandbox.</em></td><td><a href="setup/sandbox-smtp-integration">sandbox-smtp-integration</a></td></tr><tr><td><strong>Sandbox API</strong></td><td><em>Programmatically manage your sandboxes and emails using our comprehensive API. Automate testing workflows and integrate with your CI/CD pipeline.</em></td><td><a href="setup/sandbox-api-integration">sandbox-api-integration</a></td></tr><tr><td><strong>API Tokens</strong></td><td><em>Learn how to create, manage, and use API tokens for Email Sandbox.</em></td><td><a href="setup/api-tokens">api-tokens</a></td></tr><tr><td><strong>Email Address per Sandbox</strong></td><td><em>Each sandbox gets a unique email address. Learn how to use sandbox-specific addresses for organizing and isolating test scenarios.</em></td><td><a href="setup/email-address-per-sandbox">email-address-per-sandbox</a></td></tr></tbody></table>

## Quick Start

#### 1. Create Your First Sandbox

* Log in to your Mailtrap account
* Navigate to Email Sandbox
* Click "Create New Sandbox"
* Name your sandbox (e.g., "Development", "Staging", "QA")

#### 2. Get Your Credentials

* SMTP Host: `sandbox.smtp.mailtrap.io`
* SMTP Port: `2525` (or `25`, `465`, `587`)
* Username: Your sandbox username
* Password: Your sandbox password

#### 3. Configure Your Application

```javascript
// Example Node.js configuration
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: 'sandbox.smtp.mailtrap.io',
  port: 2525,
  auth: {
    user: 'your_username',
    pass: 'your_password'
  }
});
```

#### 4. Send Test Email

```javascript
await transporter.sendMail({
  from: 'test@example.com',
  to: 'user@example.com',
  subject: 'Test Email',
  text: 'This is a test email'
});
```

## Integration Methods

#### SMTP Integration

* Universal compatibility with any SMTP client
* No code changes required
* Perfect for legacy applications
* Supports all major frameworks and languages

#### API Integration

* Full programmatic control
* Retrieve and analyze emails via API
* Automate testing workflows
* Perfect for CI/CD pipelines


# Sandbox SMTP Integration

Learn how to integrate sandbox with your application using SMTP credentials or code samples

## Copy SMTP credentials

{% stepper %}
{% step %}
Go to **Email Testing** → **Sandboxes**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8f946da2c1074f0a2f0700dd00e0b4acc6a111cc%2Fsandbox-integration-navigate-to-sandboxes.png?alt=media" alt="Navigation menu showing Email Testing section with Sandboxes option" width="563"></div>
{% endstep %}

{% step %}
Open the sandbox (named **My Sandbox**) created by default.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-10b7e1b77daf3d2eead7469a7661bc0cbb978ce0%2Fsandbox-integration-open-my-sandbox.png?alt=media" alt="Sandboxes list displaying My Sandbox and other project sandboxes" width="563"></div>
{% endstep %}

{% step %}
Under the **Integration** tab, select **SMTP** and copy the credentials such as Host, Port, Username, and Password.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-72ef2089bec7b1a9ea41e9defb4c81d83a8464b2%2Fsandbox-integration-smtp-credentials.png?alt=media" alt="Integration tab showing SMTP credentials including Host, Port, Username, and Password" width="563"></div>
{% endstep %}

{% step %}
Paste them into your email-sending script, service, or MTA (any service that supports SMTP integration), and run it. The email will arrive in your sandbox in a few seconds.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d74cb92a9a7f2d35427ec74c02524115c91c018e%2Fsandbox-integration-email-received.png?alt=media" alt="Sandbox inbox displaying received test email message" width="563"></div>
{% endstep %}
{% endstepper %}

## Select your integration

Instead of copy-pasting the SMTP credentials, you can use the code samples already containing your credentials.

{% stepper %}
{% step %}
In the **Integration** tab of your sandbox, scroll down to **Code Samples** and select the programming language or framework you're working with.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58bb8ca2dd649b4b27dfcae7a8812a196b50d959%2Fsandbox-integration-code-samples.png?alt=media" alt="Code Samples section showing various programming language options for integration" width="563"></div>
{% endstep %}

{% step %}
Copy the configuration and paste it into your email-sending script. Then, run it. The email will arrive in the sandbox in a few seconds.
{% endstep %}
{% endstepper %}

{% hint style="success" %}
*Learn how exactly Mailtrap can help you streamline email testing processes from our* [*case study with The Software House*](https://mailtrap.io/case-studies/the-software-house/)*.*
{% endhint %}


# Sandbox API Integration

Learn how to use the Sandbox API to automate testing and manage email sandboxes programmatically.

### How the API works

The testing API uses REST protocol and can return calls as JSON objects. And it's compatible with the majority of programming languages.

Mailtrap supports the following HTTPs requests:

* **POST** to create a resource
* **PATCH** to update a resource
* **GET** to get a resource or list of resources
* **DELETE** to delete a resource

### What you can do with the Sandbox API

Via the API, you can run the following commands:

* **Sandbox** — Create a new sandbox, reset the sandbox credentials and its email address; receive messages, clean one or all messages in the sandbox, mark all messages as read; manage users.
* **Project** — Create a new project, update, and delete it; manage its users.
* **Email forwarding** — Manage forwarding messages to real email addresses (available starting from the Individual plan).
* **Email content** — Inspect the email body by getting raw HTML (you can also download it), text, and detailed info about the HTML part, including a list of possible errors; receive message attachments.
* **Bcc and message headers** — Receive message headers (Bcc is also included in this section, notwithstanding that it is not a regular message header). Bcc is available starting from the Team plan.
* **Deliverability** — Get a Spam report and domain blacklisting details.

This way, you can test and verify if:

* Email sending script works.
* Email recipients are correct + Bcc testing (on the advanced plans).
* HTML template doesn't cause errors.
* Mail merge/dynamic content is replaced properly.
* Appropriate files are attached.
* Important links, such as reset password and account confirmation, work.
* Your message doesn't trigger a spam filter and your domain is not blacklisted, etc.

### How to get started with Sandbox API

First, you need to get a token. You can find it under **Settings** > **`API Tokens`**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f58393406a4d158ba3a4e32ae3c9974deaf2c39d%2Fsandbox-api-tokens-settings.png?alt=media" alt="" width="123"></div>

To learn more about managing your tokens, please [check this guide](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-tokens). Then, there are a couple ways to send authenticated HTTP requests:

* Send a HTTP header `Api-Token: {api_token}` , where `{api_token}` is your API token.
* Send a HTTP header `Authorization: Bearer #{token}` , where `{api_token}` is your API token (more info: Token Access Authentication).

Go to the [API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-email-testing-api), check samples, and experiment in the console.


# API Tokens

Learn how to create, manage, and use API tokens for Email Sandbox.

The guidelines assume that you've set up Email Sandbox and use the corresponding [APIv2](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-sandbox-api).

#### Add and manage tokens manually

{% stepper %}
{% step %}
Navigate to **Settings** in the menu on the left and select **API Tokens**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
To add a new token, click the **Add Token** button in the upper right corner.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
**Type the token name** into the designated field.&#x20;

It’s perfectly fine to have a custom name for the API token, as it’s only for your reference, regardless of the use case.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FlpA9pLUncYMLdgSmAeKK%2FScreenshot%202025-12-16%20at%2016.19.22.png?alt=media&#x26;token=db12e0a4-70a9-4c7e-ba86-03015e19afdd" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Assign permissions** by checking the boxes in the corresponding access level columns. Note that you must have admin permissions on a particular domain to send emails with this token.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aad9698d90812d10b8afa0226ddf5fcafd66d19f%2Fapi-tokens-permissions-editor.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the **Save** button and preview the new token under the **API Tokens** main menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbJoeiyZ94WGz0p0AdGh3%2FScreenshot%202025-12-16%20at%2016.20.39.png?alt=media&#x26;token=f400948a-2bd0-4232-bc85-5d9d61e23475" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

#### Auto-created token per domain

When you create a domain, a token is automatically created and named based on the following formula: \[domain name] + \[token] + \[token ID].

For example, if you add the example.com domain, the token for that domain will be named example.com token 1234. By default, the automatically generated token gets Domain Admin Mailtrap for the given domain.

{% hint style="info" %}
You'll need to edit permissions for the automatically generated token to allow for authorization on other domains.
{% endhint %}

#### Where to find tokens?

**SMTP Integration**

The automatically assigned token per domain is under the **Integration** tab in **Sending Domains**. Choose the desired stream, click **Integrate**, and toggle the switch to **SMTP**. SMTP password is the same as the API Token.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-186162064de44083d6fac8d9df38546d716aae77%2Fsmtp-integration-credentials-streams.png?alt=media" alt=""></div>

#### Settings > API Tokens

Select **Settings** in the left menu, then **API Tokens**. You'll see all active tokens, their creator, and their access level.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>

Click the three-dot menu to the far right of the specific user token and select Edit permissions.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-553a50709bf5064d20e425d713a561600dba14eb%2Fapi-tokens-edit-permissions-menu.png?alt=media" alt="" width="188"></div>

{% hint style="info" %}
**Important notes:**

* You can also give Account Admin access to the token and get access to all Projects, Sandboxes, and domains on that account.
* If you want to test how it works, you need to get authenticated using your API token. Mailtrap uses Bearer Authentication, so you must pass the token under the Authorization header of your email.
  {% endhint %}

### Reset token

There are two ways to reset API tokens:

#### Resetting API tokens in the Sandboxes

To reset tokens, go to your Sandbox under the **Sandboxes** tab and click the **Reset Credentials** function next to your credentials.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-0ba079e671cd45f4523c20db7e284c1455861db0%2Fapi-tokens-reset-credentials-button.png?alt=media" alt=""></div>

Then, click **Reset Credentials** and confirm your choice with the **Yes,** **Reset** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4e4367d17c5e317a6b32a307174dd570f3954de3%2Fapi-tokens-reset-credentials-dialog.png?alt=media" alt="" width="375"></div>

#### Resetting API Tokens from the API Tokens menu

Go to API Tokens, click the three-dot menu icon next to the token you want to reset, and click Reset API Token.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3762cde4a3322e8764196f336b594df6f4ec68c5%2Fapi-tokens-reset-menu-option.png?alt=media" alt="" width="563"></div>

Confirm your choice by clicking on the corresponding button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-25e07ca7578551e8334f73700b5026fa96047780%2Fapi-tokens-reset-confirmation.png?alt=media" alt="" width="563"></div>

{% hint style="success" %}
**Tip:** The three-dot menu icon next to the token also allows you to copy a token to your clipboard.
{% endhint %}

{% hint style="warning" %}
**Important notes:**

* After clicking the Reset credentials or Reset API Token buttons, the existing token becomes invalid after 12 hours. So, you have a 12-hour window to update all apps that use the old API token. Once the old token expires, some parts of your application will not work properly unless you've updated the token. All expired tokens get deleted from your account within 24 hours after expiration.
* After the API token is reset and expired, a new token is created. The token ID is added to the token name the same way it's done for automatically generated tokens, e.g., mailtrap.example token 4231.
  {% endhint %}

### Edit permissions

As mentioned earlier, click the menu icon at the far right of a token and select Edit permissions.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-532af5c8cd0d2effab0678823088ef476173c267%2Fapi-tokens-edit-permissions-option.png?alt=media" alt="" width="563"></div>

Click on the corresponding boxes to add or remove token permissions. Then, confirm your selection with the Save button.

### Delete token

To delete a token, click the three-dot menu icon and choose the **Delete token** option.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-51692fed552abdb850f55a54a7bca58cbe023465%2Fapi-tokens-delete-menu-option.png?alt=media" alt="" width="563"></div>

Confirm the action by clicking the **Confirm** button.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-738ea005c1db709ef926c8698ffc7e1a4bbe85b9%2Fapi-tokens-delete-confirmation.png?alt=media" alt=""></div>

{% hint style="warning" %}
**Important:** Keep in mind that a token is deleted immediately, and you can't delete the last token per domain.
{% endhint %}


# Email Address per Sandbox

Use a dedicated customizable email address for each sandbox to send test messages without SMTP integration.

This feature offers an email address for testing, which you can customize. It supports dynamic aliases and provides you with an unlimited number of virtual email addresses. As soon as it is linked to your [sandbox](https://mailtrap.io/inboxes/), you can manage, view, and share your test results via the Mailtrap UI.

Starting from the [Basic](https://mailtrap.io/pricing/) billing plan, each of your sandboxes includes a dedicated email address you can use to send messages. You will find it in the **Email Address** tab. You can use your current email setup without needing to integrate Mailtrap as a fake server and run safe experiments.

The email address is enabled for you by default. To disable, edit, and reset the email address for this sandbox, click on the three-dots (more) menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ee12698dda0ff03dd86b066669fafc3394f1ac9c%2Fsandbox-email-address-tab.png?alt=media" alt="" width="563"></div>

As you can see from the screenshot, the sandbox address consists of two parts:

* A **customizable alias**, which you can edit manually. You can use any combination of numbers and Latin symbols. For example, you can use your company name or the name of the current sandbox with an identifying number.
* Mailtrap's **technical hash**, which can't be changed. It consists of 6 symbols and acts as our internal sandbox identifier.

This way, you get an infinite number of combinations and can imitate sending emails to a large number of users (with unique email addresses).

The sandbox name changes are applied instantly.

{% hint style="info" %}
Note that Mailtrap verifies sandbox aliases so that if you try to send a message to a custom sandbox address that doesn't exist, you will receive a `554 5.5.1 Error: no sandbox for this email.`message.
{% endhint %}

Additionally, Mailtrap sandboxes support dynamic aliased addresses. For example, [mailtrap-load-test-12ab34+1@inbox.mailtrap.io](mailto:mailtrap-load-test+1-12qb34@mailtrap.io) and [mailtrap-load-test-12ab34](mailto:mailtrap-load-test+2-12qb34@mailtrap.io)[+2](mailto:mailtrap-load-test+2-12qb34@mailtrap.io)[@inbox.mailtrap.io](mailto:mailtrap-load-test+2-12qb34@mailtrap.io) will be equally accepted and delivered to the same sandbox.

As a result of testing, all your experiments will be perfectly sorted and delivered to the corresponding Mailtrap virtual sandboxes. You will be able to review all of the messages and verify their content. This is crucial when you use personalization (especially in a subject line) and dynamic elements or localization.

Another important point is that sending to sandboxes from your production server doesn't affect your domain's reputation for the main email providers like Gmail, Hotmail, Yahoo, etc.


# Testing Features

Comprehensive email testing tools for quality assurance

Email Sandbox provides a complete suite of testing tools to ensure your emails look perfect and function correctly across all email clients and scenarios.

## Testing Capabilities

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Email Template Inspector</strong></td><td><em>Analyze your email templates in detail. Check rendering, validate structure, and ensure compatibility across different email clients.</em></td><td><a href="testing/email-template">email-template</a></td></tr><tr><td><strong>HTML Check</strong></td><td><em>Validate your HTML email code for errors and compatibility issues. Get recommendations for improving email client compatibility.</em></td><td><a href="testing/email-html">email-html</a></td></tr><tr><td><strong>Email Headers and Bcc</strong></td><td><em>Inspect all email headers including hidden Bcc recipients. Verify that your email configuration is correct and secure.</em></td><td><a href="testing/email-headers-and-bcc">email-headers-and-bcc</a></td></tr><tr><td><strong>Deliverability Tests</strong></td><td><em>Run comprehensive deliverability tests to predict how your emails will perform in production. Check spam scores, authentication, and more.</em></td><td><a href="testing/spam-blacklist-reports">spam-blacklist-reports</a></td></tr><tr><td><strong>Bounce Emulator</strong></td><td><em>Simulate various bounce scenarios to test your application's bounce handling. Ensure your system properly processes different bounce types.</em></td><td><a href="testing/bounce-rate">bounce-rate</a></td></tr><tr><td><strong>Load Testing</strong></td><td><em>Test your email system under high load. Verify performance and identify bottlenecks before they impact production.</em></td><td><a href="testing/load-testing">load-testing</a></td></tr></tbody></table>


# Email Template Inspector

Check email content, validate HTML code, and verify text versions of your message.

### 1. View the email in the sandbox and check its content

Go to the **HTML tab**, which opens by default when you open a message. It demonstrates how the email is rendered in a web browser and allows you to:

* Check whether the template looks as expected: Markup is correct, images are displayed, and fonts are supported.
* Review the message content, click the links and buttons.
* Test the message for responsiveness: click the device icons in the tab to see how it looks on mobile, tablet, and desktop.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8c9420ed0c858d32c840e5cbc505efb7a6cbbab2%2Fsandbox-inspect-template-html-view.png?alt=media" alt="" width="563"></div>

### 2. Check the HTML template code for validity

Email clients use different rendering standards. This is why your email can be displayed not as you designed it. You need to check that your message code won't cause rendering issues.

**HTML Check** scans through your email in search of problematic elements. For each it finds, it displays the list of email clients that lack support for it or support it only partially. It also estimates the support for your emails' code across popular email clients, making adjustments for their popularity.

Go to the **HTML Check** tab to see the report:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-706451ecddab821bb7f2c6ffffd0b03deb576cb7%2Fsandbox-inspect-template-html-check.png?alt=media" alt="" width="563"></div>

**HTML Check** collects the list of rules used in your email and compiles it with the supporting data we have for the most popular email clients. The final result is the Market Support, or the overall level of HTML/CSS support for your email.

Below you will see a list of rules that cause errors in the specified email clients. To the right of each element, you can see the numbers (\[1], \[2], etc.). Click on any of them, and the "show more" section will expand, explaining what the issue is and which client/version it applies to.

Clicking on the line number will take you to the **HTML Source** tab where you can view your email's entire HTML.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e5f241e5c06d09c3a9978cc0b22f2d92c9121779%2Fsandbox-inspect-template-html-source.png?alt=media" alt="" width="563"></div>

To learn more about the HTML Check feature, refer to the [HTML Check article](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-html).

### 3. Make sure that the HTML and TEXT versions of your message match

It is important to include both the HTML and text versions in your message. This not only affects the spam score but also helps your recipients to understand your message if the HTML part hasn't rendered for some reason. Go to the **Text** tab to inspect the text version.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a5513b5c31aa8f94f69bd6dc862ded7adc6c79d0%2Fsandbox-inspect-template-text-view.png?alt=media" alt="" width="563"></div>


# HTML Check

Learn how HTML Check scans your email for problematic elements and provides market support scores.

**HTML Check** scans through your email in search of problematic elements. For each it finds, it displays the list of email clients that lack support for it or support it only partially. It also estimates the support for your emails' code across popular email clients, and provides you with percentage of the market share accordingly.

The report is available in the **HTML Check** tab:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5d4e45024fe60b999fcb6d95ea3f07fc5cce17d0%2Fsandbox-html-check-report.png?alt=media" alt="" width="563"></div>

The higher your market support score, the better for your email!

### Understanding the Market Support score

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-73d2a78a041e58d01d6e2dbe3affd9f5995aa6f1%2Fsandbox-html-check-market-support-score.png?alt=media" alt="" width="375"></div>

Each HTML email template consists of dozens, if not hundreds, of HTML/CSS rules. The support for them varies across email clients and even across versions of particular clients. It's not uncommon that, for example, Apple Mail supports a rule for iOS 11.0+ (but doesn't for an older version) and only has partial support for the macOS app.

**HTML Check** collects the list of rules used in your email and compiles it with the support data we have for the most popular email clients. The final result is the **Market Support**, or the overall level of HTML/CSS support for your email.

The support for a rule in a particular client can fall into one of three categories:

* **Full support** — The rule is fully supported across all versions of a client.
* **Partial support** — The rule is not fully supported in a given client, OR at least one of the versions of this client doesn't support it.
* **No support** — The email client offers no support for this rule.

When calculating the score, we take into consideration the market share of each email client. Some clients (e.g., Gmail or iPhone's default Mail app) are far more popular than others (for example, Yahoo! Mail). For that reason, the less popular clients may lack support for specific elements thus having a far more significant impact on the Market Support score.

### Filtering options

By default, the market support is calculated for all email clients listed to the right and all their versions in common use. You can freely check and uncheck particular filters, and the market score will adjust immediately.

The vertical list shows five common families of email clients, 'Other' representing less popular clients (e.g., Thunderbird, AOL, etc.). The horizontal list lets you narrow down the results for the particular type of client: mobile, web, or desktop.

For example, if you were to select only Apple Mail and Yahoo! Mail but unchecked 'Mobile', both clients' iOS and Android apps would be ignored. If there's no client for a particular category (e.g., Apple Mail doesn't have a web client), unchecking a category won't alter the results.

As usual, the weight on the Market Support result is proportional to the popularity of each client.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c83252b6ef7ef7d3f8648ec2da82478333c93226%2Fsandbox-html-check-filtering-options.png?alt=media" alt="" width="375"></div>

Filtering is particularly beneficial if you know that the vast majority of your users are, for example, on mobile or use only Outlook to view your emails. You can get a more focused market support result this way.

Note that at least one category (Web/Mobile/Desktop) and at least one email client need to be checked to generate any result.

### The algorithm behind HTML Check

You may also view the support for the entire family of popular email clients, such as Gmail (iOS, Android apps, desktop, mobile webmail, etc.). Simply hover over the respective name, and the green (fully supported), orange (partially supported), and red (not supported) numbers will appear.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a33f83532cc922c7c27bca06eca9fb215f1d7df3%2Fsandbox-html-check-email-client-support.png?alt=media" alt="" width="375"></div>

To understand how these are calculated, let's look at an example. We want to view the results for Gmail only, which, across all three categories, has ten different versions of its email client (as an example). Our email has three HTML/CSS rules:

* **'height attribute'** — Not supported in clients \[2], \[4], and \[6], only partially supported in \[5]
* **'max-width'** — Not supported in clients \[2], \[3], and \[4], partially supported in \[5], and \[6]
* **'style tag**' — Not supported in \[2]

**HTML Check** algorithm calculates which clients:

* Don't support at least one of the styles used in a template -> \[2], \[3], \[4], \[6] -> 4/10 -> 40% -> these are marked as red (no support)
* Only partially support at least one of the styles (and have not been marked as 'no support') -> \[5] -> 1/10 -> 10% -> these are marked as orange (partial support)
* All other clients - \[1], \[7], \[8], \[9], \[10] - 5/10 -> 50% - are marked as green (full support)

Note that client \[5] partially supports one rule but doesn't support another. Because we look at the "worst" support level across all rules, this client was tagged as 'no support'.

The support for Gmail in our example is:

* **Full support** — 50%
* **Partial support** — 10%
* **No support** — 40%

We collect the data on support for particular rules from [Caniemail.com](https://www.caniemail.com/).

### Analyzing the HTML elements

Almost always, at least a few errors will appear. For instance:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e5af05d06da74943268f9b5d93e2e47ac4f213a8%2Fsandbox-html-check-element-errors.png?alt=media" alt="" width="563"></div>

Each will display:

* Element name (e.g. 'margin-left')
* Clients that don't support this element (red) or offer only partial support (orange)
* Hyperlinks to individual lines where the element was found (more on these below)
* "show more" label shedding more light on the problematic element.

To the right of each element, you can see the numbers (\[1], \[2], etc.). Click on any of them, and the "show more" section will expand, explaining what the issue is and which client/version it applies to.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8412aa8f3f67f764663c4f1c0c2786579ec4c2ef%2Fsandbox-html-check-element-details.png?alt=media" alt="" width="563"></div>

Clicking on the line number will take you to the **HTML Source** tab where you can view your email's entire HTML.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-12f252451ed645822e2028c66712c34685c6306e%2Fsandbox-html-check-source-view.png?alt=media" alt="" width="563"></div>

This also demonstrates the alternative way of using HTML Check. You can use the **HTML Source** tab from the start and inspect the code, line by line. Each problematic line will be highlighted with an orange or a red circle, with an exclamation mark inside of it.

For more details on the issue, head to the **Check HTML** tab and look for this item down the list.


# Email Headers and Bcc

Learn how to verify email headers including Subject, From, To, and Bcc fields.

* **Subject line.** View how it looks for the recipient and make sure that they are rendered as expected, especially if you used emojis.
* **FROM** (sender). Make sure the sender's name and email address are correct.
* **TO** (recipients) - To and Cc. When you send multiple emails and/or use "merge" functions, you should carefully check whether recipients are generated correctly.
* **Bcc** - Blind copy, which is not a header, making it especially difficult to test. With Sandbox, you can check whether proper addresses are added (available starting from the [Team plan](https://mailtrap.io/pricing/)).

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-56228d198162a09e6aebfec35f29fbc6460fd61a%2Fsandbox-email-headers-bcc.png?alt=media" alt="" width="563"></div>

You can perform all these checks in your Mailtrap sandbox. Open the message, and check the Subject, From, and To headers first. Then click **Show Headers** or go to the **Tech Info** tab directly. There, you will find the following information:

* Message-Id
* Message date and time
* Reply-To
* Bcc'ed email address(-es) (if there is no Bcc, then you will see the "There is no Bcc information in this email message" message)

**SMTP Info** section demonstrates the message details according to the SMTP protocol. Mailtrap analyzes SMTP commands of the message, compares message headers and recipients, and then prints out the difference to the Bcc field. To learn more about Bcc and how it works, read:

{% embed url="<https://mailtrap.io/blog/cc-bcc-in-smtp/>" %}

Please note that the sandbox shows Bcc 'as is'. It displays an email message for each DATA SMTP command. If an SMTP client fetches Bcc from the RCPT TO command, it will be displayed as one email message in the Mailtrap sandbox. However, some clients send email messages to Bcc'ed addresses as separate RCPT TO **and** DATA commands that result in a separate/second email message in the sandbox.

If you need detailed information about the message metadata, view the **Raw** tab.


# Spam & Blacklist reports

Learn how to check spam score and blacklisting to ensure email deliverability

### Spam Report

Go to the **Spam Analysis** tab to view the Spam Report. It contains the general score and a detailed table with spam test points and their descriptions.

[Apache SpamAssassin](https://mailtrap.io/blog/spamassassin-score/), the most popular email filter, runs numerous tests on email headers and body text and assigns a score to each of them.

A score below 5 points is considered good. If your email gets more than 5 points, it will most likely be treated as spam by various email clients. In this case, check the rules that gained the highest score and fix your email template accordingly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8f5379403481f939e52b03b660bac93739db5d00%2Fsandbox-spam-analysis-report.png?alt=media" alt="Spam Analysis report showing SpamAssassin score breakdown with detailed test results" width="563"></div>

### Blacklists Report

You will find the Blacklists Report in the **Spam** **Analysis** tab as well.

It checks whether your IP or domain has been listed on any of the commonly used blacklists. It shows resources that have been queried and your current status. If your domain or IP is blacklisted, click the resource name; it's hyperlinked to the blacklist website -- check their rules for delisting and follow their instructions.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9b686c549e6408c33c9464b827cddca2755b5c5c%2Fsandbox-blacklists-report.png?alt=media" alt="Blacklists Report displaying domain and IP blacklist checking results" width="563"></div>


# Bounce Emulator

Learn how to test your SMTP client's behavior when the server responds with an error

## Constructing the address

The recipient's username should start with bounce+ and contain the response in URL-encoded form: `bounce+550+no+such+user+here@inbox.mailtrap.io` .

To create it, use [https://www.urlencoder.org](https://www.urlencoder.org/) or any other URL encoding solution.

Tip: You cannot use capital letters because email addresses are converted to lowercase by any responsible SMTP client. But you can use URL encoding to express capital letters: `bounce+550+%4Eo+such+user+here@inbox.mailtrap.io` .

## Using Bounce Emulator with an email client

Just use the inbox.mailtrap.io host with any email client or application and send an email to `bounce+451+server+unavailable@inbox.mailtrap.io` .

## Using Bounce Emulator with Sandbox

If your application is connected to Email Sandbox SMTP, send an email from the application to `bounce+454+authentication+required@anydomain.com` , and your application will receive a bounce response from the Sandbox SMTP server.

*Note: This feature does not work with API, as bounce codes are specific to SMTP.*


# Load Testing

Test your email application at scale using the Sandbox Enterprise plan with up to 150 emails per 10 seconds across 300 sandboxes

Email app load testing is one of the most popular cases of using Sandbox Enterprise plan. This plan allows you to send up to 150 emails every 10 seconds to as many as 300 sandboxes.

Every sandbox has a unique email address that can be customized (the "email per sandbox" feature). It consists of two parts:

* A **customizable alias, which you can edit manually**. You can use any combination of numbers and Latin symbols. For example, your company name or the name of the current sandbox with an identifying number. Sandboxes support dynamic aliased addresses. For example, <mailtrap-load-test-12ab34+1@inbox.mailtrap.io> and <mailtrap-load-test-12ab34+2@inbox.mailtrap.io> will both be accepted and delivered to the same sandbox.
* **Technical hash, which cannot be changed**. It consists of 6 symbols and acts as our internal sandbox identifier. Using this feature, you can use an infinite number of address combinations, and can imitate sending emails to a large number of users (with unique email addresses). The sandbox name changes are applied instantly, meaning that you don't have to pause your email testing and wait until a new alias becomes valid.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8f4b7b907c57a7cf578157005d412a5602eba6ad%2Fsandbox-load-testing-email-address-customization.png?alt=media" alt="Email address customization interface showing alias and hash components for load testing" width="563"></div>

{% hint style="success" %}
*Also, note that if you try to send a message to a custom sandbox address that doesn't exist, you will get the "554 5.5.1 Error: no sandbox for this email" message.*
{% endhint %}

By default, the sandbox email address is disabled for security reasons. To activate it, go to the **Email Address** tab and open the three dots menu next to the **Copy** button. Click **Enable**. In this menu, you will also find the **Edit** and **Reset Address** buttons.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2e9b28b427b546039e81830d17396f08dab46cf9%2Fsandbox-enable-email-address.png?alt=media" alt="Three dots menu displaying Enable, Edit, and Reset Address options for sandbox email" width="563"></div>

### Load testing use case

Large-scale systems employ numerous servers to distribute loading. Specifying **a separate testing email address for each server** allows you to follow and inspect failures or unexpected behavior. This way you can test and load all your resources at once and then filter the results accordingly.

Here is how it looks in practice:

* email **server A** sends messages to the [servera-12ab32@inbox.mailtrap.io](mailto:servera-12ab32@mailtrap.io) sandbox
* email **server B** sends messages to the [serverb-12ab44@inbox.mailtrap.io](mailto:servera-12ab32@mailtrap.io) sandbox
* email **server C** sends messages to the [serverc-12ab55@inbox.mailtrap.io](mailto:servera-12ab32@mailtrap.io) sandbox
* …
* email **server L** sends messages to the [serverl-12ab99@inbox.mailtrap.io](mailto:servera-12ab32@mailtrap.io) sandbox, etc.

Afterward, you can enter a corresponding project in your account and see a list of these sandboxes with the number of messages in each sandbox.

This way, you can check and compare your sending capabilities and instantly identify which of your servers is experiencing problems.

*You can disable the email addresses any time you need it. We recommend disabling them as soon as you finish testing, for improved safety.*


# Sandbox Management

Manage and organize emails in your sandbox effectively

Efficiently manage, search, and organize emails within your Email Sandbox. These tools help you maintain a clean testing environment and quickly find the emails you need.

## Management Features

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Searching Messages</strong></td><td><em>Powerful search capabilities to find specific emails quickly. Filter by sender, subject, date, content, and custom criteria.</em></td><td><a href="management/searching-messages">searching-messages</a></td></tr><tr><td><strong>Automatic Forwarding</strong></td><td><em>Set up rules to automatically forward emails from your sandbox to real email addresses. Perfect for sharing test results with team members.</em></td><td><a href="management/automatic-email-forwarding">automatic-email-forwarding</a></td></tr><tr><td><strong>Manual Forwarding</strong></td><td><em>Manually forward individual emails when needed. Share specific test cases or examples with stakeholders.</em></td><td><a href="management/manual-email-forwarding">manual-email-forwarding</a></td></tr></tbody></table>


# Searching Messages

Search for emails in your sandbox by subject, recipient address, or recipient name

Email search works as a case-insensitive pattern matching. You can search for emails by:

* All words from email subject
* TO email address
* TO name

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-454984c300c2330a06e14aa6ccfea56bf68ea2ef%2Fsandbox-search-messages.png?alt=media" alt="Search interface showing filter options for finding emails by subject, address, or name"></div>


# Automatic Forwarding

Forward emails from the sandbox to any inbox automatically for testing in different clients and notifying colleagues.

You can forward emails from the sandbox to any inbox.

* View emails in different email clients, or even other apps.
* Notify your colleagues or clients about the testing progress.
* Use it as a proxy between your application and your email client; never miss a thing from your QA environment.

Email forwarding is available starting from the [Basic plan](https://mailtrap.io/pricing/). You can set automatic forwarding to confirmed email addresses or domains.

### How to set automatic forwarding to an email address

To set auto-forwarding to email addresses, go to the **Auto Forward** tab in your sandbox and enter the forwarding email address(es).

The email confirmation will be sent to this email address(es) for verification. Once the address is confirmed by its owner, you can **add this address to the "To" or "Cc" headers** of your email messages, and they will be automatically forwarded.

In the **Auto Forward** tab, you will also find the list of email addresses for forwarding and their statuses:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fd3127d31c6758b7868b0da4b9c1ebf1bb8d743f%2Fsandbox-auto-forward-email-addresses.png?alt=media" alt=""></div>

* *Active* means that its owner has confirmed that they agree to receive emails.
* *Pending* means that the owner hasn't confirmed that they agree to receive emails.

To resend the confirmation or remove a forwarding rule, use the action buttons in the three-dots menu next to the selected email address.

### How to set automatic forwarding to a domain

To set auto-forwarding to a domain, you need to add a TXT record to verify your site. Here are the steps:

1. Enter your domain in the Domain field and click the **Add domain** button.
2. In the displayed table you will find the record and its value.
3. Go to your domain settings page, select **Manage DNS**, and **choose TXT** from the list of options (for details, consult your domain provider documentation).
4. Copy the authentication key from the **Value** column and paste it to your TXT record.
5. Once completed, get back and click the **Verify** button for this domain. The status should change to **Active**. The system will forward messages to any email address which matches "\*@domain" in the "To" or "Cc" email headers. To remove a forward rule, use the action buttons in the three-dots menu next to the domain.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a5f20c7c74be6e01ac71f45cc7cbe0384bc03658%2Fsandbox-auto-forward-domain-verification.png?alt=media" alt="" width="563"></div>

### `From:` header in forwarded emails

All forwarded email messages use forward.mailtrap.info in the `From:` header, e.g., when you forward an email from sandbox you'll see something like this in your sandbox:

> From: Mailtrap Forward <<b751965-a5480376@forward.mailtrap.info>>

It helps to use forwarding for users with a strict DMARC policy on their domains. Since DMARC doesn't allow sending emails from your domain without permissions, sandbox rewrites the `From:` header. But because the original sender is valuable information, especially in automated testing, we still preserve it in *x-mailtrap-original-from* header of the forwarded emails.


# Manual Forwarding

Forward individual emails from sandbox to any inbox for testing in different clients or notifying colleagues.

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


# Collaboration

Team features for collaborative email testing

Work effectively with your team using Email Sandbox's collaboration features. Share sandboxes, projects, and test results to streamline your email testing workflow.

## Collaboration Features

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Sharing Sandboxes</strong></td><td><em>Share individual sandboxes with team members. Control access levels and permissions for different users.</em></td><td><a href="collaboration/sharing-sandboxes">sharing-sandboxes</a></td></tr><tr><td><strong>Sharing Projects</strong></td><td><em>Share entire projects containing multiple sandboxes. Perfect for organizing testing environments across teams.</em></td><td><a href="collaboration/sharing-projects">sharing-projects</a></td></tr></tbody></table>


# Sharing Sandboxes

Share individual sandboxes with team members for collaborative email testing.

### How to organize your sandbox data

The best practice is to create separate sandboxes for different environments: development, test, or staging. Each sandbox is defined by SMTP credentials (your username and password). If necessary, you can reset them at any time.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e1ef509d8af99d956316aa4a7a6a668d162c973f%2Fsandbox-sharing-sandboxes-credentials.png?alt=media" alt="" width="563"></div>

### How to share your sandboxes with others

For effortless collaboration with your colleagues or customers, you can share data of your choice with them: separate sandboxes or whole projects. To learn how to share projects, read our [dedicated article](https://docs.mailtrap.io/documentation/email-sandbox/collaboration/sharing-projects).

There are two ways to share your sandbox:

1. Invite users directly to sandbox
2. Share sandbox via User Management

To share a sandbox, you need to be one of the following:

1. Sandbox, project, or account admin
2. Account owner

Also, sharing options are available starting from the Team plan.

You can invite anyone, even if they don't have a Mailtrap account yet.

1. Click the gear icon on the far right of the sandbox you'd like to share.
2. Go to the Access Rights tab.
3. Enter the email address of your team member.
4. Choose the invitee's permission level (e.g. Sandbox Viewer or Admin)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-f79144483d3d3a9f705080ffffd1475ba85efc52%2Fsandbox-sharing-sandboxes-access-rights.png?alt=media" alt=""></div>

Once you click the **Add** button, the email invitation will be sent to the specified email address. The recipient should accept the email invitation.

But if a person is already in your account, the sandbox will immediately become visible to them.

Alternatively, you can use the **User Management** feature. Select it and click the **Add Member** button. Type the user's email address and tick the box under the permission level for a sandbox you'd like to share.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-72195a74443a865777fd5ad622be381b098021a4%2Fsandbox-sharing-sandboxes-user-management.png?alt=media" alt="" width="375"></div>

And yes, you can share multiple sandboxes at the same time. To finalize sharing, hit **Send Invite** and you're good to go.

### Sandboxes shared with you by others

Clicking on Sandboxes in the menu bar on the left reveals only the sandboxes associated with the account you're currently using.

If you want to access a different account and sandboxes that were shared with you, click on the account switcher in the upper right corner of the window, then select an account from the drop-down menu.

Note that you can be invited to any sandbox or project as a user, regardless of the subscription plan you currently use.


# Sharing Projects

Organize and share projects to collaborate with team members on email testing.

### How to organize projects

All incoming emails in Sandbox are organized into sandboxes, the folders that are grouped into projects. Usually, projects are used to separate companies, environments, or (surprisingly) projects.

### How to share your projects

Sharing options are available starting from the Team plan.

You can share any of the projects in your account. Users that receive access to your project also receive access to all of its sandboxes and can manage or view their content. To learn how to share a specific sandbox, check out the [Sharing sandboxes](https://docs.mailtrap.io/documentation/email-sandbox/collaboration/sharing-sandboxes) article.

To share a project including all of its sandboxes, you have three options:

* Use the three vertical dots next to My Project under Sandboxes

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aee1a3cdca602bf1ea1ff3ec1d74abe2ccd1101f%2Fsandbox-sharing-projects-menu.png?alt=media" alt="" width="563"></div>

* Share a link from Project Team Members

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-01fb2a514e9a9fe4cd1e09543434d338a7eb2a1d%2Fsandbox-sharing-projects-team-members.png?alt=media" alt="" width="563"></div>

* Utilize the User Management feature

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58e520fef03008de3387fad31161dbc33c048280%2Fsandbox-sharing-projects-user-management.png?alt=media" alt="" width="375"></div>

It doesn't matter which option you choose. New users will be visible in the Sandbox Team Members, Project Team Members tab and in the User Management list. But to share a project, you need to be one of the following:

* Project or account admin
* Account owner

### Important notes

The User Management section is visible to Account Admins and the Account owner.

In the "Project Team Members" window, you see all people who have access to this project, whether they were invited directly to the project or they have access to it. For example, the users could be account admins and thus have access to all projects.

If you select the "Team Members" tab of an sandbox, you see all people who have access to this sandbox. That goes for those invited directly to the sandbox and users who have access to the sandbox. Again, they could be project admins and thus have access to all project sandboxes.


# Help & Support

Get help with Email Sandbox issues and find answers to common questions

Find answers to common questions and troubleshoot issues with Email Sandbox. Our comprehensive help resources are designed to get you back on track quickly.

## Resources

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Frequently Asked Questions</strong></td><td><em>Browse our comprehensive FAQ section for quick answers to common questions about Email Sandbox setup, integration, testing features, and best practices.</em></td><td><a href="help/faqs">faqs</a></td></tr><tr><td><strong>Troubleshooting</strong></td><td><em>Step-by-step solutions for common issues including connection problems, email capture issues, and configuration errors.</em></td><td><a href="help/troubleshooting">troubleshooting</a></td></tr></tbody></table>

## Common issues & solutions

### Connection issues

#### Can't connect to Sandbox SMTP

1. **Verify credentials**: Check username and password
2. **Confirm port**: Use 2525, 25, 587, or 465
3. **Check firewall**: Ensure ports aren't blocked
4. **Test connection**: Use telnet or nc command

```bash
telnet sandbox.smtp.mailtrap.io 2525
```

#### Emails not appearing in Sandbox

1. **Check sandbox limits**: Free plan has 500 emails/month
2. **Verify credentials**: Ensure using correct sandbox
3. **Check spam folder**: Some emails may be filtered
4. **Review email size**: Maximum 5MB including attachments
5. **API rate limits**: Check if hitting rate limits

### Configuration problems

#### Framework integration not working

* **Laravel**: Clear config cache with `php artisan config:clear`
* **Rails**: Restart server after config changes
* **Django**: Check `EMAIL_BACKEND` setting
* **Node.js**: Verify environment variables loaded

#### Authentication failures

```
535 5.7.0 Invalid login or password
```

Solution:

* Copy credentials directly from Mailtrap dashboard
* Don't use email address as username
* Regenerate credentials if needed

### Testing issues

#### HTML not rendering correctly

* Use HTML Check tool to validate code
* Test with different email clients
* Check for missing closing tags
* Validate CSS compatibility

#### Attachments not working

* Verify file size < 5MB total
* Check MIME type configuration
* Ensure proper encoding (base64)
* Test with different file types

## Getting help

### Self-service resources

1. **Search documentation**: Use the search bar above
2. **Check FAQs**: [Frequently Asked Questions](https://docs.mailtrap.io/documentation/email-sandbox/help/faqs)
3. **Review troubleshooting**: [Common issues](https://docs.mailtrap.io/documentation/email-sandbox/help/troubleshooting)
4. **API reference**: [API Documentation](https://api-docs.mailtrap.io/)

### <i class="fa-comments-question-check">:comments-question-check:</i>Contact Support

If you can’t find the answer you need in our documentation and would like to contact support and speak with an agent, we’re here to help.

You can get in touch with the Mailtrap Support team using one of the following ways:

* **From your Mailtrap account**&#x20;

1. Log in to your account [here](https://mailtrap.io/signin).
2. Go to the <i class="fa-circle-question">:circle-question:</i>[<mark style="color:$primary;">**Help Center**</mark>](https://mailtrap.io/help-center) > <i class="fa-message-dots">:message-dots:</i> Get Help
3. Click <mark style="color:$primary;">**Start conversation.**</mark>&#x20;

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7hftpJFYZKk1D4GQCYd8%2FScreenshot%202026-02-19%20at%2017.12.57.png?alt=media&#x26;token=90aebf2d-07b7-4c5b-aa6b-07623bc02077" alt=""><figcaption></figcaption></figure>

* **Email us at** 📧 <support@mailtrap.io><br>

Whether you need technical assistance, help troubleshooting an issue, or simply want to talk to customer support, our team will be happy to assist you.

### Before contacting support

Please have the following information ready:

* Account email address
* Sandbox ID or name
* Error messages (exact wording)
* Steps to reproduce the issue
* Framework/language you're using
* Code snippets (if applicable)

## Quick solutions

### Email capture issues

| Problem            | Solution                             |
| ------------------ | ------------------------------------ |
| No emails received | Check credentials and connection     |
| Emails delayed     | Normal processing time is < 1 second |
| Missing emails     | Check inbox limits and filters       |
| Partial content    | Verify email size < 5MB              |

### API issues

| Error Code | Meaning      | Solution                 |
| ---------- | ------------ | ------------------------ |
| 401        | Unauthorized | Check API token          |
| 403        | Forbidden    | Verify permissions       |
| 404        | Not found    | Check inbox ID           |
| 429        | Rate limited | Implement backoff        |
| 500        | Server error | Retry or contact support |

### SMTP errors

| Error                 | Cause               | Fix                               |
| --------------------- | ------------------- | --------------------------------- |
| Connection refused    | Wrong port/host     | Use sandbox.smtp.mailtrap.io:2525 |
| Authentication failed | Invalid credentials | Copy from dashboard               |
| Message rejected      | Size limit exceeded | Keep under 5MB                    |
| Timeout               | Network issue       | Check firewall/proxy              |

## Debugging tools

### Connection testing

```bash
# Test SMTP connection
openssl s_client -connect sandbox.smtp.mailtrap.io:2525 -starttls smtp

# Test with curl
curl -v telnet://sandbox.smtp.mailtrap.io:2525
```

### Email testing

```python
# Python test script
import smtplib
from email.mime.text import MIMEText

def test_sandbox():
    msg = MIMEText('Test email body')
    msg['Subject'] = 'Test Subject'
    msg['From'] = 'test@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as server:
        server.login('YOUR_USERNAME', 'YOUR_PASSWORD')
        server.send_message(msg)
        print("Email sent successfully!")

test_sandbox()
```

## Best practices

### Optimal configuration

* Use port 2525 for best compatibility
* Enable STARTTLS for security
* Set reasonable timeout values
* Implement retry logic
* Use connection pooling

### Testing strategy

* Create separate sandboxes per environment
* Clear sandboxes regularly
* Use descriptive email subjects
* Tag emails with test IDs
* Automate common tests

### Team collaboration

* Share sandboxes appropriately
* Document sandbox purposes
* Use consistent naming
* Regular permission audits
* Communicate test schedules

## Community resources

### Tutorials & guides

* [Getting started video](https://www.youtube.com/watch?v=example)
* [Blog tutorials](https://mailtrap.io/blog/tag/sandbox/)
* [Integration examples](https://github.com/railsware/mailtrap-examples)

### Developer resources

* [API client libraries](https://github.com/railsware)
* [Postman collection](https://www.postman.com/mailtrap)
* [Code snippets](https://mailtrap.io/blog/test-emails-in-dev/)

## Feedback & suggestions

*We welcome technical feedback and contributions that help us improve Mailtrap’s functionality and documentation. Please use the appropriate channel depending on the type of request.*

#### <i class="fa-bug">:bug:</i>Bug Reports

**If you encounter a product issue or unexpected behavior, please** [#contact-support](#contact-support "mention")**.**

To help us investigate efficiently, include:

* A detailed description of the issue
* Exact reproduction steps
* Relevant stream, domain, sandbox, or account details
* Timestamps (including timezone)
* Screenshots or logs if available

#### <i class="fa-file-circle-plus">:file-circle-plus:</i>Feature Requests

For product improvements or new feature proposals, use our [Public Roadmap](https://mailtrap.featurebase.app/en) portal.

There you can:

* **Submit a new feature request**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ff9yf6pEv5ZXR4EHh5ABg%2FScreenshot%202026-03-02%20at%2010.32.03.png?alt=media&#x26;token=2cea9a79-0387-4fb3-988d-272d13327b77" alt="" width="375"><figcaption></figcaption></figure></div>

* **Upvote existing requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fax54DgMBWcXzIQEiLeCg%2FScreenshot%202026-03-02%20at%2010.33.40.png?alt=media&#x26;token=0454c018-c008-4287-a329-407bcd3e1c35" alt="" width="375"><figcaption></figcaption></figure></div>

* **Subscribe to updates for specific requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FmB0AdDAkT5l43l0jmBps%2FScreenshot%202026-03-02%20at%2010.33.11.png?alt=media&#x26;token=790a0502-73e1-4bd2-803a-c4b4c7973d60" alt="" width="375"><figcaption></figcaption></figure></div>

:soon:**The following enhancements are currently planned:**

* GraphQL API
* Advanced search filters
* Email templates library
* Browser extension
* Mobile app

#### <i class="fa-file-doc">:file-doc:</i>Documentation Improvements

If you identify unclear, incomplete, or outdated documentation:

1. Use the **feedback widget** located on the right-hand side of the page to rate the article:\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FOLpynTOT2XMAP3d7c7Ct%2FScreenshot%202026-03-02%20at%2010.30.47.png?alt=media\&token=c71836e0-95da-47ae-b9d7-917dbebc9149)
2. **Provide specific feedback** describing what should be corrected, clarified, or expanded\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FU94kVQcPPjT7e6bgJz4m%2FScreenshot%202026-03-02%20at%2010.31.22.png?alt=media\&token=7e0ec64d-058e-4b47-a25f-4bd01d40e549)

This helps us continuously refine our docs.

#### <i class="fa-square-code">:square-code:</i>GitHub & Technical Collaboration

For open-source projects, SDKs, or public repositories, join us on [GitHub](https://github.com/mailtrap).


# FAQs

Frequently asked questions about Email Sandbox

This page covers frequently asked questions about Email Sandbox. For technical issues and error troubleshooting, see the [Troubleshooting section](https://docs.mailtrap.io/documentation/email-sandbox/help/troubleshooting).

#### Integration & setup

<details>

<summary>How do I integrate Email Sandbox with my application?</summary>

The integration is very simple and you can complete it in just a couple of minutes using SMTP credentials or code samples for over 20 frameworks.

**See our step-by-step guide**: [How to integrate Email Sandbox with your application](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-smtp-integration).

</details>

<details>

<summary>Do you need to view Sandbox emails only through its interface?</summary>

No, you don't have to stick to Email Sandbox web interface. You can forward every single email to your or a teammate's mailbox.

You can even enable automatic forwarding, and Email Sandbox will act as a proxy between your application and your email client. In this case, you won't miss important messages from the QA environment, such as exception notifications.

**Learn more**:

* [Automatic Email Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding)
* [Manual Email Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/manual-email-forwarding)

</details>

#### Technical specifications

<details>

<summary>How does Email Sandbox render emails?</summary>

Sandbox renders emails in the same way browsers do, which means no additional stylesheet or CSS presets are applied by default.

</details>

<details>

<summary>Can Email Sandbox show what emails look like in various email clients?</summary>

Email Sandbox is compatible with web email clients and renders HTML as-is, without external CSS styles.

Sandbox provides [HTML checks](https://docs.mailtrap.io/documentation/email-sandbox/testing/email-html) and demonstrates potential errors that different email clients may experience when rendering an HTML email. You can also get a preview of test emails for different devices (e.g., mobile, tablet, desktop).

You can also forward emails to Outlook, Thunderbird, etc., and use these desktop clients to view them.

</details>

<details>

<summary>What does Sandbox do with the &#x3C;style> tag?</summary>

Sandbox doesn't remove the `<style>` tag from email templates.

</details>

<details>

<summary>What does Sandbox do with the &#x3C;script> tag?</summary>

For enhanced security, Sandbox removes all `<script>` tags from HTML.

</details>

<details>

<summary>Can I use Email Sandbox as a /dev/null SMTP server?</summary>

The main goal of Sandbox is to help you test emails, and `/dev/null` is not a part of it.

Should you need a `/dev/null` SMTP server, please use the following built-in Python SMTP server:

```bash
python -m smtpd -nc DebuggingServer localhost:2525 > /dev/null
```

</details>

<details>

<summary>What is the email size limit for Sandbox?</summary>

The maximum size of an email including attachments ranges from 5 MB to 25 MB, depending on your subscription plan.

If your message exceeds this limit, you will get the following error: `552 5.3.4 Error: message too big`.

For complete details, see [Features and Limits](https://docs.mailtrap.io/documentation/email-sandbox/features-and-limits#email-size-mb).

</details>

<details>

<summary>What is the testing rate limit for the sandbox?</summary>

It's the number of emails you can send to each of your sandboxes every 10 seconds. The rate limit depends on the subscription plan.

For more details, check out the [Features and Limits](https://docs.mailtrap.io/documentation/email-sandbox/features-and-limits#rate-limits-per-10-sec) article and our [pricing page](https://mailtrap.io/pricing/).

</details>

<details>

<summary>What is the monthly messages limit for Email Sandbox?</summary>

It's the maximum number of emails you can test and get in all your sandboxes per month. The total emails per month limit depends on the subscription plan.

If you reach your monthly limit, you'll receive the SMTP protocol error: `535 5.7.0 Monthly messages limit reached`. We also send out notifications for having used 80%, 90%, and 100% of the monthly limit.

To continue testing when you're over the limit, please upgrade your subscription plan. Alternatively, you can wait until the next billing period starts, when the limit is reset.

For more details, check out the [Features and Limits](https://docs.mailtrap.io/documentation/email-sandbox/features-and-limits#total-test-emails-per-month) article or our [pricing page](https://mailtrap.io/pricing/).

</details>

#### Pricing

<details>

<summary>How much does Email Sandbox cost?</summary>

Email Sandbox provides a free subscription plan for new users who want to evaluate it.

For larger teams, we offer sets of features within several paid subscription plans, starting from $17/month.

To choose one that best fits your needs, check our [pricing plans](https://mailtrap.io/pricing/?tab=sandbox).

</details>


# Troubleshooting

Common issues and solutions for Email Sandbox

This page covers common issues you might encounter when using Email Sandbox and their solutions.

### Connection errors

If you can't connect to the Sandbox SMTP server and receive errors like **Connection cannot be established** or **Connection timed out**, follow these troubleshooting steps:

{% stepper %}
{% step %}
**Test your connection using the Telnet utility**

{% code title="Terminal" %}

```bash
telnet sandbox.smtp.mailtrap.io 2525
```

{% endcode %}

If Telnet shows that a connection can't be established with our server, you should:
{% endstep %}

{% step %}
**Try alternative SMTP ports**

Use another SMTP port, such as **2525**, **465**, or **25**.

{% hint style="info" %}
In most cases, connection issues are related to the firewall blocking the SMTP port.
{% endhint %}
{% endstep %}

{% step %}
**If none of these ports work, try connecting with:**

* A different machine
* A different location
* A different ISP
* A VPN connection

This will help identify the route affected by the issue.
{% endstep %}

{% step %}
**Check idle timeout**

If you've opened an SMTP connection and haven't closed it afterward, the SMTP server will close the session after the idle timeout time.
{% endstep %}

{% step %}
**Verify server status**

To make sure our SMTP server is up and running, go to the [Status page](http://status.mailtrap.info/). Here, you can check the SMTP server availability from different locations.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If the issue persists after trying all these steps, please contact us at <support@mailtrap.io>.
{% endhint %}

### Authentication error (530)

**Error message:**

```
Expected response code 250 but got code "530", with the message "530 5.7.1 Authentication required"
```

When you receive the **5.7.1 Authentication required** error, it means that either:

* The SMTP authentication is disabled in your configuration, or
* The authentication failed

{% hint style="danger" %}
In either case, an email was not sent.
{% endhint %}

**Solution:**

1. Enable SMTP authentication in your settings
2. Configure your app to enable SMTP authentication
3. If it is already enabled, revise your credentials and authentication settings
4. Try sending an email again

### Messages not delivered to Sandbox

If your messages aren't appearing in your sandbox, follow these troubleshooting steps:

{% stepper %}
{% step %}
**Verify your** [**SMTP integration**](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-smtp-integration) **is correct**

1. Go to your sandbox **Integration** tab
2. Compare hostname, username, and password with those in your app

{% hint style="warning" %}
If you reset SMTP/POP3 credentials, all existing integrations are affected and must be updated.
{% endhint %}
{% endstep %}

{% step %}
**Verify limits**

Make sure that the number and frequency of the messages sent correspond to the terms of your [billing plan](https://mailtrap.io/pricing/). Check:

* Rate limits (emails per 10 seconds)
* Monthly message limits
* Email size limits
  {% endstep %}

{% step %}
**Check SMTP logs**

View your SMTP logs and check whether you received any errors. To view SMTP logs, enable debugging in your email code.

For example, see [how to enable debugging in PHPMailer](https://mailtrap.io/blog/phpmailer/).
{% endstep %}

{% step %}
**Contact support**

If you still can't figure out why your emails aren't getting delivered to your sandbox:

1. Save an undelivered message in **.eml** format
2. Remove any sensitive information
3. Send it to us at <support@mailtrap.io>
   {% endstep %}
   {% endstepper %}

### Sandbox email address disabled

Email per sandbox is a premium feature available in the Basic, Team, Enterprise, or Business plans.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-452d2a16b109af56aa4b1f3926d9585885f668cc%2Ftroubleshoot-sandbox-email-address-disabled.png?alt=media" alt="Sandbox Email Address tab showing disabled status with upgrade message"><figcaption></figcaption></figure></div>

**Enabling after upgrade**

Once you upgrade your plan, make sure you activate the address:

{% stepper %}
{% step %}
Go to the **Email Address** tab in your sandbox.
{% endstep %}

{% step %}
Click the three-dot menu to the right, and select **Enable**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9af740fda93790a80452bddcb1fa6de45652ffc1%2Ftroubleshoot-sandbox-enable-email-address.png?alt=media" alt="Email Address menu with Enable option highlighted" width="375"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

**Alternative: SMTP integration**

{% hint style="info" %}
You can freely test emails without this feature. With any plan (including the free tier), you can integrate SMTP credentials into your app and receive every email this way.
{% endhint %}

You'll find the integration samples for over 20 frameworks and libraries on the Integration page of your sandbox. You can also use the API without any restrictions.

### Tech info / headers unavailable

The **Tech Info** tab will show the following headers if they're present in an email:

* `Message_id`
* `X_mailer`
* `Sender`
* `From`
* `To`
* `Cc`
* `Reply_to`
* `Return_path`

{% hint style="info" %}
If any of these headers haven't been specified (for example, an email doesn't have a `reply_to` header specified), it won't be displayed.
{% endhint %}

**BCC Header**

If you are on the Business plan or higher ([view plans](https://mailtrap.io/pricing/)), you will also see the **BCC** header in this tab (if specified for the message).

On lower plans, no BCC field will appear even if it was included in a message.

### Team members limit reached

If you can't add more team members, you may have reached the user limit of your plan.

**Solution:** Upgrade your plan to increase the team member limit. Check [pricing plans](https://mailtrap.io/pricing/) for details.

### Automatic forwarding issues

If your test emails aren't being forwarded automatically, there's very probably an error in the auto-forwarding configuration.

**How auto-forwarding works**

When auto-forwarding to predefined addresses/domains, sandbox verifies the `TO` and `CC` headers of a message (BCC is ignored).

An email is forwarded if:

* `TO` or `CC` of your email matches the value in the **Emails** list, **OR**
* The domain in the `TO` or `CC` of your email matches the value in the **Domains** list

{% hint style="warning" %}
A forwarding rule needs to be verified (its status must be **Active**) before it can be considered. To do that, you'll need to confirm the email address or the domain's ownership.
{% endhint %}

**Troubleshooting steps**

If a particular email is not forwarded:

1. Check its headers via the **Tech Info** tab
2. Verify you have the correct `TO` or `CC` address set
3. Ensure your forwarding rule status is **Active**
4. Confirm the email address or domain has been verified

**Furher reading**: [Automatic Email Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding)

### Suspicious emails in sandbox

If you see emails in your sandbox that you didn't send from your app, someone may have accessed your SMTP credentials.

{% hint style="danger" %}
If you suspect unauthorized access to your sandbox, reset your credentials immediately.
{% endhint %}

**How to reset credentials**

Don't panic — it's very easy to reset your credentials:

{% stepper %}
{% step %}
Log in to your dashboard, open your sandbox, and go to the **Integration** tab.
{% endstep %}

{% step %}
Click the **Reset Credentials** button, and your details will be reset right away.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-82c61e67dbbb315c7368c6e6864a8590740c8b56%2Ftroubleshoot-sandbox-reset-credentials.png?alt=media" alt="Integration tab with Reset Credentials button highlighted"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Make sure you update the credentials in your app, as old credentials will no longer be valid.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
We don't store information about the server or IP address that sent messages. As such, we won't be able to help you track down the sender.
{% endhint %}

#### Related articles

* [How to integrate Email Sandbox with your application](https://docs.mailtrap.io/documentation/email-sandbox/setup/sandbox-smtp-integration)
* [Features and Limits](https://docs.mailtrap.io/documentation/email-sandbox/help/features-and-limits)
* [Automatic Email Forwarding](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding)
* [Email Sandbox FAQs](https://docs.mailtrap.io/documentation/email-sandbox/help/faqs)

#### Need More Help?

If you don't find the solution to your problem here, contact our support at <support@mailtrap.io>.


# Features and Limits

All Mailtrap features and possible limits explained

### Total test emails per month

The maximum number of emails you can test with Sandbox per month, depends on your [billing plan](https://mailtrap.io/pricing/?tab=email-sandbox).

### Rate limits per 10 sec

The number of emails you can send to each of your Sandboxes every 10 seconds. The exact number depends on your billing plan.

Once the rate limit per 10 seconds is reached, the messages are not getting sent and are rejected with the error "550 5.7.0 Requested action not taken: too many emails per second".

### Sandboxes

Sandboxes are separate folders where your test messages from different environments (Dev, QA, staging) are captured. Every Sandbox is created inside a Project - a folder which can be shared with other users, according to the Team Members options (available in the Team plan and more advanced billing plans)

### Projects

The groups that help you arrange your Sandboxes and distinguish different tasks you are working on simultaneously. You can share your projects with other team members (available in the Team and more advanced billing plans).

### Team members

Mailtrap users who you can interact with by inviting them to your account and sharing projects or the billing section. This feature is available from the Basic Testing plan and more advanced billing plans. [Click here](https://docs.mailtrap.io/documentation/account-and-organization/management/users) to learn more about the User Management feature.

### Max emails per sandbox

The total number of emails you can store in each of your sandboxes at once. The exact number depends on your billing plan. When the limit is reached, Mailtrap uses the FIFO model for automatic sandbox cleanup (oldest messages first).

### Sandbox API

Sandbox API allows developers to run integration or load tests, as well as receive messages or email lists via API. To learn how to use the Email Sandbox API, refer to the [Email Sandbox API documentation](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-sandbox-api).

### Email address per sandbox

The dedicated email address for each of your Sandboxes that you can use to send messages from other email accounts or right from your application during the testing process. It is available in the Basic Testing plan and more advanced billing plans.

### Email size, MB

The maximum allowed size of each email message, including attachments, in megabytes, is between 5MB and 25MB, depending on your plan.

### Total forwarded emails per month

The maximum number of emails you can forward from your account to real inboxes for testing and preview purposes. The maximum number of forwarding rules is 300. Email forwarding is available in the Basic Testing plan and more advanced billing plans.


# Sandbox Glossary

Common terms and definitions for Email Sandbox features and protocols

**Sandbox API** — Compatible with most programming languages, uses the REST protocol, and returns calls in JSON format. Here's the [link](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/a2041e813d169-email-testing-api) to the API documentation. With API, you can take actions related to an sandbox, a project, email forwarding, email content, message headers, and more.

**CORS Domains** — CORS is Cross-Origin Resource Sharing. It's a mechanism that allows restricted resources to be requested from another domain outside the domain from which the first resource was served. You can specify a list of domains that will have access to API.

**Sandbox** — A virtual sandbox with its own credentials to organize your emails. Typically, users have sandboxes for different environments, i.e. staging, development, and testing.

**POP3** — Stands for Post Office Protocol 3. It's among the most widely used protocols for receiving various emails.

**Project** — Sandboxes can be grouped into different projects to separate testing environments, companies, and projects you work on. Note that the number of projects is limited based on your plan.

**STARTTLS** — It's an email protocol command that relays security information between an email server and an email client. The command shows an email client that Gmail, for example, wants to upgrade to a secure connection with TLS or SSL. STARTTLS is also commonly used with IMAP.

### Miscellaneous Terms

**Email Headers** — All the original values of the email headers displayed as a table.

**HTML Source** — The HTML source code of an email that you send.

**MTA** — Message (or Mail) Transfer Agent. It's the software that relays emails between senders' and recipients' computers via SMTP. To find out more about MTA, check out our related [blog post](https://mailtrap.io/blog/mail-transfer-agent/).

**MTA Settings** — When setting up a sandbox, you get the SMTP settings to copy-paste into your MTA. That way, your MTA will use Mailtrap servers.

**RAW** — It's your processed email consisting of a series of required and optional text headers followed by a message body. These details may be important for diagnosing email delivery issues.

**Text** — The plain text version of an email. If your email has only an HTML version, the Text tab won't be available. This is true the other way around, too.


# Overview

Create, send, and analyze email marketing campaigns with Mailtrap's comprehensive marketing platform

Mailtrap Email Marketing is a complete solution for creating, sending, and analyzing email campaigns. Build beautiful emails with our drag-and-drop editor, manage your subscriber lists, automate campaigns, and track performance - all in one platform.

## What is Email Marketing?

Email Marketing by Mailtrap provides everything you need to run successful email campaigns:

* **Visual Email Builder**: Drag-and-drop editor for beautiful emails
* **Contact Management**: Organize and segment your audience
* **Campaign Automation**: Set up triggered and scheduled campaigns
* **Analytics & Reporting**: Track opens, clicks, and conversions

## Key Features

### Campaign Creation

* **Drag & Drop Editor**: No coding required
* **HTML Editor**: Full control for developers
* **Reusable Templates**: Save and reuse designs
* **Responsive Design**: Mobile-optimized emails
* **Personalization**: Dynamic content insertion

### Audience Management

* **Contact Import**: CSV, API
* **List Segmentation**: Target specific groups
* **Custom Fields**: Store any subscriber data
* **Suppression Management**: Automatic unsubscribe handling

### Campaign Automation

* **Welcome Series**: Onboard new subscribers
* **Drip Campaigns**: Nurture leads over time
* **Behavioral Triggers**: Action-based emails

### Analytics & Insights

* **Real-Time Stats**: Track campaign performance
* **Engagement Metrics**: Opens, clicks, conversions
* **Audience Insights**: Subscriber behavior analysis
* **Export Reports**: CSV

## Use Cases

### E-commerce

Perfect for online stores:

* Product announcements
* Customer win-back campaigns
* Loyalty program updates

### SaaS & Technology

Ideal for software companies:

* Product updates and releases
* Feature announcements
* User onboarding sequences
* Renewal reminders

### Content & Media

Great for publishers and creators:

* Newsletter distribution
* Content roundups
* Event announcements
* Subscriber exclusives
* Breaking news alerts

### B2B Marketing

Essential for business growth:

* Lead nurturing campaigns
* Webinar invitations
* Case study distribution
* Industry insights
* Partnership announcements

## How It Works

### 1. Build Your List

Import existing contacts or use signup forms to grow your audience.

### 2. Create Your Campaign

Design beautiful emails with our editor or use pre-built templates.

### 3. Send & Schedule

Send immediately or schedule for optimal timing.

### 4. Track Performance

Monitor real-time analytics and optimize future campaigns.

## Quick Start Guide

{% stepper %}
{% step %}
**Verify Your Domain**

Add and verify your sending domain for authentication.
{% endstep %}

{% step %}
**Import Contacts**

Upload your subscriber list via CSV or API.
{% endstep %}

{% step %}
**Create Campaign**

Design your email using templates or the editor.
{% endstep %}

{% step %}
**Send or Schedule**

Launch your campaign immediately or schedule it.
{% endstep %}
{% endstepper %}

## Email Builder Options

{% tabs %}
{% tab title="Drag & Drop" %}
Visual editor perfect for marketers:

* Pre-built content blocks
* Image galleries
* Button styles
* Social media icons
* No coding required
  {% endtab %}

{% tab title="HTML Editor" %}
Code editor for developers:

* Full HTML/CSS control
* Template variables
* Custom scripts
* Import existing designs
* Live preview
  {% endtab %}

{% tab title="Templates" %}
Ready-to-use designs:

* Industry-specific templates
* Seasonal campaigns
* Newsletter layouts
* Promotional designs
* Customizable themes
  {% endtab %}
  {% endtabs %}

## Compliance & Deliverability

### Built-in Compliance

* **GDPR Ready**: Data portability and privacy controls
* **CAN-SPAM Compliant**: Unsubscribe links, physical address
* **CASL Support**: Canadian anti-spam compliance
* **Footer Management**: Automatic compliance footers

### Deliverability Features

* **Domain Authentication**: SPF, DKIM, DMARC
* **List Cleaning**: Remove invalid emails
* **Engagement Tracking**: Identify inactive subscribers

## Best Practices

### List Building

* Use double opt-in
* Offer valuable incentives
* Clear value proposition
* Easy signup process
* Regular list cleaning

### Campaign Design

* Mobile-first approach
* Clear CTAs
* Concise content
* Personalization
* Accessible design

### Sending Strategy

* Consistent schedule
* Optimal timing
* Segment audiences
* Test subject lines
* Monitor engagement

## Getting Started

{% columns %}
{% column %}
**Setup & Configuration**

* [Campaign Creation](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/copy-of-email-marketing.md)
* [Campaign Scheduling](https://docs.mailtrap.io/documentation/email-marketing/campaigns/scheduling)
* [Email Templates](https://docs.mailtrap.io/documentation/email-marketing/campaigns/email-templates)
* [Automations](https://docs.mailtrap.io/documentation/email-marketing/automations)
  {% endcolumn %}

{% column %}
**Audience & Analytics**

* [Contact Management](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/contacts.md)
* [List Segmentation](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/broken-reference/README.md)
* [Campaign Statistics](https://docs.mailtrap.io/documentation/email-marketing/campaigns/statistics)
* [Reports & Analytics](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/broken-reference/README.md)
  {% endcolumn %}
  {% endcolumns %}

## Support & Resources

* [Campaign Guide](https://docs.mailtrap.io/documentation/email-marketing/campaigns)
* [Audience Management](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/broken-reference/README.md)
* [Analytics Guide](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/broken-reference/README.md)
* [FAQs](https://docs.mailtrap.io/documentation/email-marketing/help/faqs)
* [Troubleshooting](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/broken-reference/README.md)

## Next Steps

1. [**Verify your domain**](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/copy-of-email-marketing.md) - Set up authentication
2. [**Import contacts**](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/contacts.md) - Build your subscriber list
3. [**Create first campaign**](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/copy-of-email-marketing.md) - Design and send
4. [**Track performance**](https://docs.mailtrap.io/documentation/email-marketing/campaigns/statistics) - Monitor results


# Campaign Management

Create, schedule, and manage email marketing campaigns

Build and manage successful email marketing campaigns with Mailtrap's comprehensive campaign management tools. From creation to scheduling to analysis, we provide everything you need.

## Campaign Features

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Campaign Scheduling</strong></td><td><em>Schedule campaigns for optimal delivery times. Set up one-time sends or recurring campaigns with advanced scheduling options.</em></td><td><a href="campaigns/scheduling">scheduling</a></td></tr><tr><td><strong>Email Templates</strong></td><td><em>Design beautiful, responsive email templates. Use our drag-and-drop editor or code your own HTML templates.</em></td><td><a href="campaigns/email-templates">email-templates</a></td></tr></tbody></table>


# Email throttling

Spread campaign delivery over time rather than send all emails simultaneously and avoid sudden traffic spikes that can trigger ESP/IP reputation issues.

{% hint style="info" %}
The feature applies to both [shared and dedicated IP](https://docs.mailtrap.io/email-api-smtp/deliverability/ip-warmup) users for UI-launched campaigns only, not transactional or bulk stream.
{% endhint %}

### How to configure email throttling

We have introduced a new step in the Campaign creation flow called Delivery.

{% stepper %}
{% step %}

### Create your Campaign

Set up your Details, Design, and Audience as usual.
{% endstep %}

{% step %}

### Navigate to Step 4 (Delivery)

Here you will see two options:

* **Send all at once**: The standard method where Mailtrap attempts to deliver emails as fast as possible.
* **Send gradually (Throttling)**: The new option to control speed.
  {% endstep %}

{% step %}

### Set your limit

Select Send gradually. Enter the number of Emails to send per hour.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FV3JW4gIMHxFGd97EyCfj%2FScreenshot%202026-01-13%20at%2013.03.04.png?alt=media&#x26;token=e5a731fb-28ed-4099-8ddf-751afe7d7373" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Proceed to Schedule

Click **Continue**.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FVRlWwmKcDS4REPFBpCxi%2FScreenshot%202026-01-13%20at%2013.12.45.png?alt=media&#x26;token=ab6aaabd-2779-4121-9b4a-086d38d18233" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The Schedule options have moved to a dedicated Step 5. You can now choose to start the gradual process immediately ("No schedule") or pick a specific start date and time.
{% endhint %}
{% endstep %}
{% endstepper %}

### Benefits

Sending a massive blast of emails all at once can sometimes overwhelm recipient servers or trigger spam filters. By throttling your campaign, you can:

{% tabs %}
{% tab title="Improve deliverability" %}
Mimic more natural sending behavior, build trust with ISPs over time, avoid spam filters, and maximize engagement with your subscribers.
{% endtab %}

{% tab title="Protect sender reputation" %}
Avoid being flagged as "suspicious" by mailbox providers (Gmail, Outlook, etc.) due to sudden volume spikes.
{% endtab %}

{% tab title="Manage server load" %}
Lessen the immediate load on receiving servers so your emails are processed smoothly and delivered without any delays.
{% endtab %}
{% endtabs %}

### Use cases

{% tabs %}
{% tab title="Warming up sender reputation" %}
**Who is it for**: Teams sending medium to large campaigns.

We recommend enabling throttling from the very first campaigns, even for smaller batches of a few hundred recipients, to establish healthy sending patterns.
{% endtab %}

{% tab title="Managing large-scale campaigns (50K+)" %}
**Who is it for**: Anyone operating under hourly sending limits or following deliverability best practices.

Even for well-warmed senders, throttling helps control delivery pace and avoid volume spikes and possible limitations due to irregular sending patterns.
{% endtab %}
{% endtabs %}

### How email throttling works

By default, Mailtrap Email Campaigns send messages at the maximum possible speed. For high-volume senders, this can create challenges: many major email service providers may flag or block sudden bursts of traffic as suspicious, impacting deliverability. Managing this manually often requires workarounds that add extra time and effort.

Throttling allows you to set a maximum number of emails Mailtrap will send per hour for a campaign (e.g., 100 emails per hour). After setting the limit, Mailtrap automatically paces delivery to stay within your defined threshold - sending continuously but never exceeding it. This provides a predictable sending cadence, better control over sender reputation, and a safer rollout of large campaigns.

{% hint style="info" %}
The maximum throttling limit is 150,000 emails per hour.
{% endhint %}

When you set an hourly limit, Mailtrap does not send one email every minute. Instead, it splits your hourly limit into 5-minute batches.

**The formula**:

`[Emails per Hour] ÷ 12 = Emails sent every 5 minutes`

**Example**:

If you set your limit to 60 emails per hour:

* Mailtrap will send **5 emails** every **5 minutes**
* 60 emails / 12 five-minute slots = 5 emails per slot

### Monitor your campaign

Once a gradual campaign has started, you can monitor its progress in real-time.

Go to your Campaigns list and click on the campaign being sent.

* **Status bar**: You will see a progress bar showing "X out of Y emails have been sent."
* **Delivery mode**: The details section will confirm the mode is set to "Send gradually" and show your configured rate (e.g., 60/hr).
* **Terminate sending**: If you need to stop the campaign immediately, click the red Terminate Sending button in the top right corner.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F0OTKSDkJq0Qz0qDEYTXs%2FScreenshot%202026-01-13%20at%2013.28.43.png?alt=media&#x26;token=66e1a6f5-6181-446e-8226-2e6aa3725b84" alt=""><figcaption></figcaption></figure>

If you notice your inbox placement rates dropping, an increase in bounce rates or spam complaints, or if emails are taking longer than usual to deliver, terminate the campaign and review the recipients.<br>


# Campaign Scheduling

Schedule your email campaigns up to two weeks in advance

Once you have an email campaign ready for launch, you can schedule it by clicking on Schedule Campaign → Schedule Campaign.

On the next page, you'll be able to schedule a campaign two weeks in advance.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9c32b4843af03eee725633fa8eeeabc38f45fbb1%2Fmarketing-campaign-schedule-form.png?alt=media" alt="Schedule the campaign form with date selector and time picker showing 02.09.2025 at 15:40 UTC" width="375"><figcaption><p>Campaign scheduling form</p></figcaption></figure></div>

Note: If you want to change your timezone, go to your [Profile Settings](https://mailtrap.io/profile-settings) and choose your preferred timezone from the drop-down menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9960612b6bb7734a8a44849de6fa241afdebe8e7%2Fprofile-settings-timezone-selector.png?alt=media" alt="Profile Settings page with timezone dropdown highlighted showing UTC timezone selection" width="375"><figcaption><p>Timezone selector in Profile Settings</p></figcaption></figure></div>


# Email Templates

Design, edit, and host HTML email templates and reference them via API.

Email Templates allow you to design, edit, and host HTML email templates.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dd28f099cf5ad9e1bf7c74120a724a8082ae42b0%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

By storing the template on Mailtrap and calling it via API, you can easily change the template code without committing to your codebase.

Email Templates support Variables, and Mailtrap uses Handlebars as a template engine. You variable should match the `{{merge_tag}}` in your contact Fields.

You can put `{{name}}` into your template and, as your contact has a field named "name" with the value "John", the template will display "John". In our visual builder, you'll see a list of your contact fields.

## Creating a template

{% stepper %}
{% step %}
Navigate to the **Templates** menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d4b58986a09646ee33096aceec07e1af772c471a%2Ftemplate-menu-nav.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the **Create New Template** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-218b5d1f14443cfd13d0ffd947dfb55182aab419%2Ftemplate-list-create-button.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Click the drop-down menu to select one of your domains, enter the Template name, Subject, and Category, and click **Continue**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1a0a2b7b1e61d6306372fe417cddc3e2a2d67b18%2Ftemplate-details-form.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Choose the **Drag & Drop Editor** to build the template without coding, or select **HTML Editor** if you prefer to write/modify the code.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a39b2f1f77325f288af5dd1d98e02701be96b2ef%2Ftemplate-design-selection.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Create/modify the design and click **Finish**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c58b11b7213dc7518f0bdd04d7d0acc44c4a792f%2Ftemplate-drag-drop-editor.png?alt=media" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
The main Templates menu features all your saved templates. To quickly access a saved template, just click on it within the main menu.
{% endhint %}

## Editing and customizing templates

### Template details

Each template must have a name, subject, category, and an assigned domain. The subject also supports variables.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-940dfd68b21c2a101059dfadfcb7857e371653bd%2Ftemplate-details-view.png?alt=media" alt="" width="563"></div>

### Available editors

{% tabs %}
{% tab title="Drag & Drop Editor" %}
The drag-and-drop editor allows you to design templates without any coding.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d113e67ef60ce61aa373995bd7d775b5750784f0%2Ftemplate-drag-drop-interface.png?alt=media" alt="" width="563"></div>
{% endtab %}

{% tab title="Code Editor" %}
The Code Editor allows you to edit the HTML or text content, depending on the emails you want to send.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e55112852cce21ebf4ad250f753310b035725a42%2Ftemplate-html-code-editor.png?alt=media" alt="" width="563"></div>

The editor supports Find and Replace options, and you can use **Cmd+F** or **Win+F** as a hotkey to reveal a quick search bar.

{% hint style="warning" %}
**Template Validation**

If your template has an error, Handlebars cannot render it. You'll see an error message in the Preview tab, and the RAW code with an error will be highlighted in the Editor.

You can't save a template with errors. Note that we don't validate HTML — only Handlebars syntax is validated.
{% endhint %}

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-79253cbc9b882d2d076aecc377b8fef3628222a7%2Fmarketing-templates-error.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endtab %}
{% endtabs %}

### Uploading images

{% stepper %}
{% step %}
Click **Upload image** in the upper right corner of the Code Editor.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1c636a6f212f1eb0016484ce6996e33e23f26483%2Ftemplate-upload-image-button.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Hit the **Upload New** button in the following menu and choose an image from your local drive.

<div align="left"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-af66650da784a3ba3a9591ad8626cd93605e92bd%2Ftemplate-images-library.png?alt=media" alt="" width="375"></div>

{% hint style="info" %}
**Image Requirements**

* Supported formats: JPG, PNG, and GIF
* Maximum file size: 2 MB
  {% endhint %}
  {% endstep %}

{% step %}
Once the image is uploaded, you will receive a confirmation notification. If the file format is unsupported or the image is too big, you will receive the corresponding error message.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3c240eac8ce9ee4922028a23cf32b616a4143cdb%2Ftemplate-image-upload-success.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Click the **Copy URL** button to copy the image URL to your clipboard, then click **Template** to return to the editing menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8c33d18b581f860bb20fc7f11d661cd63c758472%2Ftemplate-copy-url-button.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
Proceed to add the image to the template body under the `<img>` tag. You can preview it in the template as soon as the asset is added.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2226ade6f36bc2deb1d039dffcc6394e93093a54%2Ftemplate-image-in-code.png?alt=media" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

### Test Data

Code Editor automatically parses your template and shows all the variables found. The Test Data tab helps you preview the object variables.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58f9d403a4f9289176f7a2b14d0712c9b5a802f1%2Ftemplate-test-data-variables.png?alt=media" alt="" width="563"></div>

{% hint style="info" %}
By default, as a value, we put a variable name and add the "Test\_" prefix.
{% endhint %}

### Sending test emails

If you're using email templates in production, you can send a test email to the account owner's email address to run basic tests. Simply press the **Send Test** button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e656b0110b9272cc878ad6e33ac0a35c9c24a4ea%2Ftemplate-send-test-button.png?alt=media" alt="" width="563"></div>

{% hint style="warning" %}
**Test email requirements**

* Your domain must be verified to send a test.
* Each test email is billed over your quota.
  {% endhint %}


# Stats

View and analyze email campaign performance metrics and analytics

Mailtrap provides statistics for you to track the most important email marketing metrics.

In your campaign dashboard, you can find:

* [Campaign stats](#campaign-stats)&#x20;
* [Recipients stats](#recipients-stats)&#x20;
* [Clicks stats](#clicks-stats)&#x20;
* [Mailbox provider stats](#mailbox-providers-stats)&#x20;

{% hint style="info" %}
Feature applies to UI-launched campaigns only, not emails sent using the transactional or [bulk stream](https://docs.mailtrap.io/email-api-smtp/setup/bulk-stream)
{% endhint %}

### Campaign Stats

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgFMAuPPCHPsGYDA9aKfR%2Fcampaign%20stats.png?alt=media&#x26;token=7ec15567-393c-497a-82b6-f6368127d944" alt=""><figcaption></figcaption></figure></div>

In the **Reports** tab, you can see the following campaign statistics:

* **Sent** – Emails attempted to be sent to recipients, including those that may have bounced or not yet been delivered.
* **Delivered** – Emails delivered to the recipient’s mailbox provider.
* **Opened** – Percentage of emails opened at least once.&#x20;
* **Clicked** – Percentage of emails where a recipient clicked any link.
* **Bounced** – Percentage of emails rejected by mailbox providers.
* **Spam complaints** – Percentage of emails recipients reported as spam.
* **Unsubscribed** – Percentage of recipients that unsubscribed from your campaign.

{% hint style="info" %}
By default, the Charts Overview shows data based on hourly sends, but you can also view it by daily totals.
{% endhint %}

### Recipients stats

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FwT72rFb2KANPyIMm9xoJ%2Frecipient%20stats.png?alt=media&#x26;token=44a29666-094a-4d24-975e-7e42236dc27d" alt=""><figcaption></figcaption></figure></div>

In the **Recipients** tab, you can see how your campaign is performing for each recipient.

The individual stats are shown in a list, as opposed to a chart, and you can filter the recipients by email, number of clicks or opens, and events (i.e., delivered, unsubscribed, etc.)

{% hint style="info" %}
You can also export the stats in a .csv file by clicking on the Download Recipients Report button.
{% endhint %}

### Clicks stats

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fixuuu2ZbsTSAQuuzyLCl%2Fclick%20stats.png?alt=media&#x26;token=69ccf1fb-65b4-432d-ae89-76a6122cdae2" alt=""><figcaption></figcaption></figure></div>

In the **Clicks** tab, you can keep track of the performance of your links, more specifically:

* **Clicks** – Number of emails where a recipient clicked any link.
* **% of total clicks** – The percentage of all campaign clicks that this link received.
* **Unique clicks** – Number of unique recipients who clicked this link at least once. Each recipient is counted only once.
* **% of unique clicks** – The percentage of all campaign clicks that came from unique users for this link.

### Mailbox providers stats

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FuD8iWxpBLZS5Ug1x35sQ%2Fmailbox%20providers.png?alt=media&#x26;token=306e59e7-cefa-4e0b-8712-50e24a45b4b0" alt=""><figcaption></figcaption></figure></div>

Finally, you can go to the **Mailbox Providers Stats** and see how your campaign is performing with different Mailbox Providers, such as Google, Yahoo, Outlook, Apple Mail, and others.


# Automations

Create automated email sequences to engage your contacts with triggers, actions, and rules.

The Automations feature allows you to create automated email sequences to engage your contacts.

Set up triggers, actions, and rules to automate your email sending.

## Use cases

Use integrations to add contacts into Mailtrap using API, SDKs, [Make.com](https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/integrations/make), [Zapier](https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/integrations/zapier), or [N8N](https://app.gitbook.com/s/gkNigAKiqQtQub1GOdjY/integrations/n8n).

{% tabs %}
{% tab title="Welcome Series" %}
**Use case**: Greet new contacts, set expectations, and share first-week tips. Perfect for onboarding new subscribers and making a great first impression.

**How to set it up**:

1. Trigger: Contact created
2. Add Send email steps with Time delays
3. Optionally: Conditional split by plan or locale

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FjZDyONhFaFePZRXCWA9o%2Fwelcome.png?alt=media&#x26;token=50f98a0b-d91c-4835-a83e-a9fb72ce261d" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Onboarding Prompts" %}
**Use case**: Nudge users when a field changes (e.g., trial started, role/plan updated). Ideal for guiding users through product adoption milestones.

**How to set it up**:

1. Trigger: Contact field updated
2. Send email with next steps
3. Add to list "Onboarding" for later messages

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FBBtdAVef1Pbs30iOn1Oi%2Fonboarding.png?alt=media&#x26;token=24a96713-af96-46eb-a3c7-349a1e1914c7" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Segment-Based Campaigns" %}
**Use case**: Deliver targeted content as people enter key lists. Great for webinar registrants, new customers, or list cleanup workflows.

**How to set it up**:

1. Trigger: Contact added to list (or removed from list)
2. Send email
3. Add/Remove from lists to manage follow-ups

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fne4iodIZ5Bg1EscKyrnl%2Fsegment%20basd.png?alt=media&#x26;token=d853c7a1-123b-4aa0-8417-ed35c10bfcb9" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Event-Driven Follow-ups" %}
**Use case**: React to product or billing events. Excellent for purchase confirmations, payment failures, or milestone celebrations.

**How to set it up**:

1. Trigger: API event received
2. Send email
3. Optionally: Update contact field and Conditional split based on event data

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FX2pLCZzvPjgUmqjEFxDd%2FScreenshot%202026-02-04%20at%2012.20.41.png?alt=media&#x26;token=0b455798-0356-4eff-82e1-4a3cceb3fafa" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Functionality

### Available components

{% tabs %}
{% tab title="Triggers" %}
Some of the Entry points available in the automation builder include:

* **Contact created** — Starts when a new contact is added.
* **Contact field updated** — Fires when specific field changes (e.g., email, last name, state, etc.).
* **Contact added to list** — Activates when a new user is added to your list.
* **Contact removed from list** — Triggers when a contact is removed from your list.
* **Contact custom event** — Starts when Mailtrap receives a custom API event.

{% hint style="info" %}
Each contact can only enter the same automation once every 24 hours.
{% endhint %}
{% endtab %}

{% tab title="Actions" %}
Here are the operations you can perform on your contacts in the automation builder:

* **Send email** — Deliver personalized messages to your contacts.
* **Update Contact Field** — Modify contact properties (e.g., email, last name, state, etc.).
* **Unsubscribe Contact** — Unsubscribe a contact from receiving your marketing emails.
* **Add to List(s)** — Assign a contact to one or more lists.
* **Remove from List(s)** — Remove a contact from one or more lists.
  {% endtab %}

{% tab title="Rules" %}
To control the flow and timing of your automations, you can use:

* **Time delay** — Wait a specified amount of time before moving on to the next step.
* **Conditional Split** — Branch the workflow automation based on criteria (fields and events).
  {% endtab %}
  {% endtabs %}

## Triggering via API Event

"Contact custom event" trigger requires you to send an API event.

{% hint style="warning" %}
Event in the trigger settings should be equal to the event you pass via API.
{% endhint %}

Here is [description of the endpoint](https://api-docs.mailtrap.io/docs/mailtrap-api-docs/6b1b5749b0eec-create-contact-event).

{% code title="API Event Example" %}

```bash
curl -X POST https://api.mailtrap.io/contacts/{contact_id}/events \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "event": "purchase_completed",
    "data": {
      "amount": 99.99,
      "product": "Premium Plan"
    }
  }'
```

{% endcode %}

## Limits

Each Mailtrap Email API/SMTP plan comes with different automation limits. To see the usage:

* Navigate to the [Billing Dashboard](https://mailtrap.io/billing/dashboard).
* Click on 'View all features' under Email API/SMTP.
* Look for 'Automations run count'.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-34d3907247e4ca0540a36831cee0252bf10836f4%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Each contact can go through the same automation once in 24 hours.
{% endhint %}

## Creating your first automation

To get started, navigate to the tab in your Mailtrap account or go to <https://mailtrap.io/automations>.

{% stepper %}
{% step %}
Define the name for your automation.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5d9ef78db5f51ea6763eea822146e5448bb890ae%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

Choose a descriptive name that indicates the automation's purpose.
{% endstep %}

{% step %}
Set up an entry trigger and select when the automation should start.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b99ad1442d73be6fc481620ec5b0d87251cbe07d%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

For this example, we'll use the "Contact created" trigger. This means the automation will start whenever a new contact is added. After selecting the trigger type, click "Save".
{% endstep %}
{% endstepper %}

## Building your automation sequence

Now that you've set up the trigger, you can start adding steps to your automation.

{% stepper %}
{% step %}
Click the "Add Step" button to add your first action.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-6eda7a0856020e2af24918273e63a86a65f915e2%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Select "Send Email" as your first action.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c71b7101ec673c3251d71e1c149763b34f86e295%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Customize your email content and settings.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfafa836b4c086a4f0cb09fb63cb5caf528e7ad3%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

Add your subject line, choose a template, and personalize with merge tags.
{% endstep %}
{% endstepper %}

### Adding delays and additional steps

To create a more complex sequence, you can add time delays and further actions.

{% stepper %}
{% step %}
Insert waiting periods between actions.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d416d62a2d46cd90c7567a7e5593eb77b9bf6323%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

Configure the delay duration (minutes, hours, days, or weeks).
{% endstep %}

{% step %}
Continue building your sequence with additional messages or actions.

Repeat the process to add more emails, list assignments, or field updates.
{% endstep %}
{% endstepper %}

## Automation activation

Once you've built your automation sequence, it's time to activate it.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-572273f1d58d99802b308d89a952733064fa6ab2%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

{% hint style="success" %}
**Before activating**

* Test with a small group first
* Review all email content
* Verify trigger conditions
* Check time delays
  {% endhint %}

### Pausing and disabling

You can pause or disable your automation at any time.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-78a5764850ade72213a3061ab2f006f08fb741ee%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

{% tabs %}
{% tab title="Pause Automation" %}
**Temporary suspension**

* No new contacts can enter automation
* Contacts currently in automation continue the flow
* Use when making minor adjustments
  {% endtab %}

{% tab title="Disable Automation" %}
**Complete shutdown**

* No new contacts can enter automation
* All contacts currently in automation will complete their current step
* Then removed from the flow
* Use for major changes or discontinuation
  {% endtab %}
  {% endtabs %}

## Stats — Monitoring automation performance

You can track the performance of your automation by clicking on the Reports tab within the automation builder.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c2c7642c6b16515e084fb63753b2048002798270%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

**Available metrics**:

* Open rate per email
* Click rate per email
* Number of step completions
* Delivery rate

## Best practices

* **Start simple**: Begin with basic welcome series before complex flows.
* **Test thoroughly**: Use test contacts before going live.
* **Monitor performance**: Check reports weekly for optimization opportunities.
* **Segment wisely**: Use conditional splits for personalization.
* **Time delays**: Consider time zones and optimal send times.
* **Exit strategies**: Plan how contacts leave the automation.


# Contacts Management

Upload, store, and organize your contacts in email lists to send targeted campaigns.

Mailtrap Contacts allows you to upload and store your contacts on the Mailtrap platform and organize them in different email lists to send targeted campaigns.

## Key Features

* Import contacts via CSV, API, or third-party integrations
* Organize contacts into targeted lists and segments
* Manage custom fields for personalization
* Track subscription status and engagement

## Getting Started

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Overview</strong></td><td><em>Filter, search, edit, and perform bulk actions on your contact database.</em></td><td><a href="contacts/overview">overview</a></td></tr><tr><td><strong>Custom Fields</strong></td><td><em>Define custom variables like name, date of birth, or location to personalize your campaigns.</em></td><td><a href="contacts/custom-fields">custom-fields</a></td></tr><tr><td><strong>Import Contacts</strong></td><td><em>Bulk contacts import from spreadsheets, sync via API, or use our integrations.</em></td><td><a href="contacts/import-contacts">import-contacts</a></td></tr><tr><td><strong>Lists</strong></td><td><em>Static groups of contacts that help you organize your audience for targeted email campaigns</em></td><td><a href="contacts/lists">lists</a></td></tr><tr><td><strong>Segments</strong></td><td><em>Dynamic groups of contacts that automatically update based on criteria you define</em></td><td><a href="contacts/segments">segments</a></td></tr></tbody></table>

## Contact management workflow

{% stepper %}
{% step %}
**Define custom fields**

Set up custom fields to store additional contact information for personalization.
{% endstep %}

{% step %}
**Import your contacts**

Upload contacts via CSV, API integration, or third-party tools like Zapier.
{% endstep %}

{% step %}
**Organize into lists**

Group contacts into relevant lists based on your marketing strategy.
{% endstep %}

{% step %}
**Create segments**

Build dynamic segments that automatically update based on contact properties.
{% endstep %}

{% step %}
**Launch campaigns**

Use your organized contacts to send targeted email marketing campaigns.
{% endstep %}
{% endstepper %}

## Import methods

{% tabs %}
{% tab title="CSV Import" %}
**Bulk upload from spreadsheets**

Perfect for migrating existing contact lists or periodic bulk updates.

* Download our CSV template
* Map fields to custom variables
* Import thousands of contacts at once
  {% endtab %}

{% tab title="API Integration" %}
**Real-time syncing from your application**

Keep contacts synchronized with your application database.

* RESTful API endpoints
* Webhook support
* Automatic updates
  {% endtab %}

{% tab title="Third-party Integrations" %}
**Connect your favorite tools**

Seamlessly integrate with your existing workflow.

* Zapier automation
* Make.com scenarios
* n8n workflows
  {% endtab %}
  {% endtabs %}

## Important considerations

{% hint style="warning" %}
**Consent requirements:**

You must have explicit consent from recipients before adding them to marketing campaigns. Mailtrap requires confirmation of consent during the import process.
{% endhint %}

{% hint style="info" %}
**Subscription management:**

Once a contact unsubscribes, they cannot be manually resubscribed. They must sign up for your list again to receive marketing emails.
{% endhint %}


# Overview

Search, filter, edit, and perform bulk operations on your contact database

Efficiently manage your contact database with powerful search, filtering, and bulk operation capabilities. Keep your lists clean and up-to-date with comprehensive management tools.

## Viewing Contacts

Navigate to **Contacts** → **All contacts** to access your complete contact database.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b4a6f6f3ba0ebb706b6cd2c79c01b0202eaa0435%2Fmarketing-contacts-details-view.png?alt=media" alt="Contact details page showing subscription status and associated fields" width="563"></div>

## Searching and Filtering

### Quick Search

Use the search bar to quickly find contacts by:

* Email address
* Name (if custom field exists)
* Any custom field value

### Advanced Filtering

Build complex filters using multiple criteria:

{% stepper %}
{% step %}
**Select Filter Type**

Choose from:

* Subscription Status
* Email
* Lists
* Custom Fields
  {% endstep %}

{% step %}
**Set Conditions**

Define your filter logic:

* **Is** / **Is not**
* **Contains** / **Does not contain**
* **Greater than** / **Less than** (for numbers)
* **Before** / **After** (for dates)
  {% endstep %}

{% step %}
**Apply Filter**

Click **Search** to view filtered results.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3e09c0b28df2fc6a3e3b794d4383e5d9d1136da3%2Fmarketing-contacts-filter-search.png?alt=media" alt="Contact filtering interface with subscription status filter" width="563"></div>
{% endstep %}
{% endstepper %}

### Common Filter Examples

{% tabs %}
{% tab title="Active Subscribers" %}

```
Subscription Status → Is → Subscribed
```

Find all contacts who can receive campaigns.
{% endtab %}

{% tab title="Recent Signups" %}

```
Signup Date → After → [Last 30 days]
AND Subscription Status → Is → Subscribed
```

Identify new subscribers for welcome campaigns.
{% endtab %}

{% tab title="VIP Customers" %}

```
Customer Tier → Is → VIP
OR Total Purchases → Greater than → 1000
```

Target high-value customers.
{% endtab %}

{% tab title="Inactive Users" %}

```
Last Activity → Before → [90 days ago]
AND Subscription Status → Is → Subscribed
```

Re-engage dormant subscribers.
{% endtab %}
{% endtabs %}

## Individual Contact Actions

Click on any contact to view their details and perform individual actions:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9051eb5935f7e3ca9c4e7aa7b6d82ef355a0c1ae%2Fmarketing-contacts-actions-menu.png?alt=media" alt="Contact actions menu with delete, unsubscribe, and edit options" width="563"></div>

### Available Actions

{% tabs %}
{% tab title="Edit Details" %}
**Update contact information**

* Modify custom field values
* Update email address
* Change list assignments
* Add notes or tags

{% hint style="info" %}
Changes are saved automatically and reflected immediately in campaigns.
{% endhint %}
{% endtab %}

{% tab title="Manage Lists" %}
**Add or remove from lists**

* Add to multiple lists
* Remove from specific lists
* View all assigned lists
* Check list membership history
  {% endtab %}

{% tab title="Unsubscribe" %}
**Remove from all marketing**

* Marks contact as unsubscribed
* Removes from all active campaigns
* Preserves contact data
* Cannot be reversed manually

{% hint style="warning" %}
Unsubscribed contacts must re-subscribe themselves to receive emails again.
{% endhint %}
{% endtab %}

{% tab title="Delete" %}
**Permanently remove contact**

* Deletes all contact data
* Removes from all lists
* Cannot be undone
* Frees up contact quota

{% hint style="danger" %}
Deletion is permanent. Export contact data before deleting if needed.
{% endhint %}
{% endtab %}
{% endtabs %}

## Bulk Operations

Perform actions on multiple contacts simultaneously for efficient management.

### Selecting Contacts

{% hint style="info" %}
**Selection Methods**

* Click checkboxes for individual contacts
* Use "Select All" for current page
* Apply filters first to target specific groups
  {% endhint %}

### Bulk Actions Available

#### Add to Lists

{% stepper %}
{% step %}
**Select Contacts**

Check the contacts you want to add to lists.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-06df90326b5b3d07ba8e91e3a9f30d3cf198bc04%2Fmarketing-contacts-bulk-add-to-lists.png?alt=media" alt="Bulk action to add selected contacts to lists" width="563"></div>
{% endstep %}

{% step %}
**Choose Lists**

Select one or more destination lists.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-7822ef30145c1d10e0325a825f511c84056b7d8b%2Fmarketing-contacts-select-lists.png?alt=media" alt="List selection dialog for adding contacts" width="563"></div>
{% endstep %}

{% step %}
**Confirm Action**

Click **Add To Lists** to complete the operation.
{% endstep %}
{% endstepper %}

#### Remove from Lists

{% stepper %}
{% step %}
**Select Contacts**

Mark contacts to remove from lists.

Click **More Actions** → **Remove from lists**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-eb6c66d4a635b7571d5285891109d4117ba10a67%2Fmarketing-contacts-bulk-remove.png?alt=media" alt="Bulk action menu showing Remove from lists option" width="563"></div>
{% endstep %}

{% step %}
**Choose Lists**

Select which lists to remove contacts from.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-71c0089e11705918f2f66c3ab15d74ff5e7a8a6d%2Fmarketing-contacts-remove-from-lists.png?alt=media" alt="List selection dialog for removing contacts" width="563"></div>
{% endstep %}

{% step %}
**Confirm Removal**

Click **Remove** to process the action.
{% endstep %}
{% endstepper %}

#### Bulk Unsubscribe

{% stepper %}
{% step %}
**Select Contacts**

Choose contacts to unsubscribe.

Click **More Actions** → **Unsubscribe**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-02c24d268ee0c69ebed6ec53c2c8f488845b17e6%2Fmarketing-contacts-bulk-unsubscribe.png?alt=media" alt="Bulk action menu showing Unsubscribe option" width="563"></div>
{% endstep %}

{% step %}
**Confirm Action**

Type 'unsubscribe' to confirm.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-0d5df6cf31dbd3dec4b0997006b3739296b5815a%2Fmarketing-contacts-unsubscribe-confirm.png?alt=media" alt="Confirmation dialog to unsubscribe contacts" width="563"></div>
{% endstep %}

{% step %}
**Process Unsubscribe**

Click **Unsubscribe** to complete.

{% hint style="warning" %}
This action cannot be undone. Contacts must re-subscribe themselves.
{% endhint %}
{% endstep %}
{% endstepper %}

#### Export Contacts

{% stepper %}
{% step %}
**Select for Export**

Choose contacts to export.

Click **More Actions** → **Export**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-5f93fae1d8b2a84155b2f5d2af3a3652fb73ae04%2Fmarketing-contacts-export.png?alt=media" alt="Bulk action menu showing Export option" width="563"></div>
{% endstep %}

{% step %}
**Confirm Export**

Click **Confirm Export**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8a8c486c335b74e28e19b504f2394750cbf544bf%2Fmarketing-contacts-export-confirm.png?alt=media" alt="Confirmation dialog to export contacts" width="563"></div>
{% endstep %}

{% step %}
**Download File**

Check your email for the download link.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dccb9340ab8bd7567adeae3b094516b6810881a7%2Fmarketing-contacts-export-email.png?alt=media" alt="Email notification with download link for exported contacts" width="563"></div>

{% hint style="info" %}
Export includes all contact fields and list memberships.
{% endhint %}
{% endstep %}
{% endstepper %}

#### Bulk Delete

{% stepper %}
{% step %}
**Select for Deletion**

Choose contacts to delete.

Click **More Actions** → **Delete**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-26615fa72de957a814c2ea91dbe0d849590ab194%2Fmarketing-contacts-bulk-delete.png?alt=media" alt="Bulk action menu showing Delete option" width="563"></div>
{% endstep %}

{% step %}
**Confirm Deletion**

Type 'delete' to confirm.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-bc17a8e5049faa418cec343f31ef270aac0dba3c%2Fmarketing-contacts-delete-confirm.png?alt=media" alt="Confirmation dialog to delete contacts with warning" width="563"></div>
{% endstep %}

{% step %}
**Process Deletion**

Click **Delete** to permanently remove contacts.

{% hint style="danger" %}
This action cannot be undone. All contact data will be permanently deleted.
{% endhint %}
{% endstep %}
{% endstepper %}

## Contact Status Management

### Understanding Subscription Status

{% tabs %}
{% tab title="Subscribed" %}
**Active and engaged**

* Can receive marketing emails
* Counted in campaign recipients
* Full access to all features
* Default status for new imports
  {% endtab %}

{% tab title="Unsubscribed" %}
**Opted out**

* Cannot receive marketing emails
* Excluded from all campaigns
* Status preserved for compliance
* Can only be changed by contact
  {% endtab %}

{% tab title="Pending" %}
**Awaiting confirmation**

* Double opt-in required
* Confirmation email sent
* Cannot receive campaigns yet
* Expires after set period
  {% endtab %}

{% tab title="Bounced" %}
**Invalid or unreachable**

* Email address is invalid
* Automatically marked by system
* Excluded from future sends
* Requires manual review
  {% endtab %}
  {% endtabs %}

## Best Practices

{% hint style="success" %}
**Contact Management Tips**

1. **Regular Cleaning**: Remove bounced and inactive contacts monthly
2. **List Hygiene**: Audit lists quarterly for relevance
3. **Segmentation**: Use filters to create targeted segments
4. **Export Backups**: Regular exports for data safety
5. **Consent Tracking**: Document how consent was obtained
   {% endhint %}


# Custom Fields

Create and manage custom fields to store additional contact information for personalization

Custom fields allow you to store additional information about your contacts beyond their email address. Use these fields to personalize campaigns and create targeted segments.

## Understanding Custom Fields

{% hint style="info" %}
**What are Custom Fields?** Custom fields are variables that store specific information about your contacts, such as:

* Personal details (first name, last name, birthday)
* Geographic information (city, country, timezone)
* Preferences (product interests, communication frequency)
* Custom data specific to your business
  {% endhint %}

## Default Fields

Every contact in Mailtrap has these default fields:

{% tabs %}
{% tab title="Email (Required)" %}
**Primary identifier for contacts**

* Automatically created
* Cannot be deleted or modified
* Must be unique across your account
* Used for sending campaigns
  {% endtab %}

{% tab title="Subscription Status" %}
**Tracks consent and engagement**

* Subscribed
* Unsubscribed
* Pending (awaiting confirmation)
  {% endtab %}
  {% endtabs %}

## Creating Custom Fields

{% stepper %}
{% step %}
**Navigate to Fields**

Go to **Contacts** → **Fields** in your Mailtrap dashboard.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-453691e947ea6bb6296723bf3e519b7838df0941%2Fmarketing-contacts-fields-menu.png?alt=media" alt="Contacts menu showing Fields tab" width="375"></div>
{% endstep %}

{% step %}
**Click Create Field**

Select the **Create Field** button to open the field creation form.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4e6db69f93bd0970bd9358d7f93bd511a347d2c8%2Fmarketing-contacts-create-field-button.png?alt=media" alt="Create Field button in the fields interface" width="563"></div>
{% endstep %}

{% step %}
**Configure Field Properties**

Fill in the field details:

* **Field Name**: Display name (e.g., "First Name")
* **Type**: Select the appropriate data type
* **Merge Tag**: Variable for personalization (e.g., `first_name`)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-43853f804cb84baf33b121988303b5b518bca8f1%2Fmarketing-contacts-field-form.png?alt=media" alt="Form to create a new contact field with name, type, and merge tag inputs" width="563"></div>

{% hint style="warning" %}
**Merge Tag Format** Use underscores for multi-word merge tags (e.g., `last_name`, `date_of_birth`)
{% endhint %}
{% endstep %}

{% step %}
**Save Your Field**

Click **Create** to add the field to your account.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-985f0e49610b95a7a13a91f36199959c53e803bd%2Fmarketing-contacts-fields-list.png?alt=media" alt="List of created contact fields including name and email" width="563"></div>
{% endstep %}
{% endstepper %}

## Field Types

Choose the appropriate field type based on your data:

{% tabs %}
{% tab title="Text" %}
**For short text values**

* Names, titles, company names
* Short descriptions
* Single-line inputs
* Maximum 255 characters

Example: `first_name`, `company`, `job_title`
{% endtab %}

{% tab title="Number" %}
**For numeric values**

* Age, scores, counts
* Integers and decimals
* Mathematical operations in segments

Example: `age`, `purchase_count`, `loyalty_points`
{% endtab %}

{% tab title="Date" %}
**For date and time values**

* Birthdays, anniversaries
* Registration dates
* Last activity timestamps
* Format: YYYY-MM-DD

Example: `birthday`, `registration_date`, `last_purchase`
{% endtab %}

{% tab title="Boolean" %}
**For yes/no values**

* Preferences and flags
* Subscription statuses
* Feature toggles
* Values: true/false

Example: `is_vip`, `newsletter_subscriber`, `has_purchased`
{% endtab %}

{% tab title="List" %}
**For predefined options**

* Categories, segments
* Multiple choice values
* Dropdown selections

Example: `product_interest`, `customer_tier`, `preferred_language`
{% endtab %}
{% endtabs %}

## Using Fields in Campaigns

### Personalization with Merge Tags

Use merge tags to personalize your email content:

{% code title="Example Email Template" %}

````

</div>

### Dynamic Content

Create conditional content based on field values:

<div data-gb-custom-block data-tag="code" data-title='Conditional Content Example'>
```liquid

<div data-gb-custom-block data-tag="if" data-expression='preferred_language == "Spanish"'>

  Hola {{first_name}},

<div data-gb-custom-block data-tag="elsif" data-0='French' data-1='French' data-2='French'></div>

  Bonjour {{first_name}},

<div data-gb-custom-block data-tag="else"></div>

  Hello {{first_name}},

</div>

````

{% endcode %}

## Best Practices

{% hint style="success" %}
**Field Management Tips**

1. **Plan before creating**: Map out all fields you need before importing contacts
2. **Use descriptive names**: Make field names clear and intuitive
3. **Consistent naming**: Use a naming convention for merge tags
4. **Data validation**: Choose appropriate field types to ensure data quality
5. **Document usage**: Keep notes on what each field represents
   {% endhint %}

## Common Use Cases

## Field Limits and Considerations

{% hint style="info" %}
**Technical Specifications**

* Maximum fields per account: Depends on your plan
* Field name length: Up to 50 characters
* Merge tag length: Up to 50 characters
* Text field value: Up to 255 characters
* Cannot delete fields with existing data
  {% endhint %}


# Import Contacts

Import contacts via CSV, API, or third-party integrations

Import your contacts into Mailtrap using CSV files, API integration, or third-party tools. This guide walks you through each method step by step.

## Before You Begin

{% hint style="warning" %}
**Preparation Checklist** Before uploading contacts, ensure you have:

1. Created all necessary custom fields
2. Cleaned your contact list (removed duplicates, invalid emails)
3. Obtained explicit consent from all recipients
4. Prepared your data in the correct format
   {% endhint %}

## Import Methods Overview

{% tabs %}
{% tab title="CSV Upload" %}
**Best for:**

* One-time migrations
* Periodic bulk updates
* Offline contact management

**Pros:**

* Simple and straightforward
* No technical knowledge required
* Visual field mapping

**File requirements:**

* UTF-8 encoding
* Comma-separated values
* Header row with field names
  {% endtab %}

{% tab title="API Integration" %}
**Best for:**

* Real-time synchronization
* Automated workflows
* Dynamic contact updates

**Pros:**

* Automatic updates
* No manual intervention
* Programmatic control

**Requirements:**

* API key
* Development resources
* Integration setup
  {% endtab %}

{% tab title="Third-party Tools" %}
**Best for:**

* Connecting existing tools
* No-code automation
* Multi-platform workflows

**Available integrations:**

* Zapier
* Make.com
* n8n

**Setup:**

* Connect accounts
* Configure triggers
* Map fields
  {% endtab %}
  {% endtabs %}

## CSV Upload Process

{% stepper %}
{% step %}
**Prepare Your CSV File**

**Download the Template**

Navigate to **Contacts** and click **Import Contacts**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3ce87627a5fa6f64101755c2bfd7626243e4ba4c%2Fmarketing-contacts-import-button.png?alt=media" alt="Import Contacts button in the contacts interface" width="563"></div>

Download our CSV template by clicking **Download CSV Template**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-185997c214c66d3d611f41f6161f6c7c78dc6c84%2Fmarketing-contacts-download-template.png?alt=media" alt="Download CSV Template button for importing contacts" width="563"></div>

**Format Your Data**

Structure your CSV with:

* **Email column** (required)
* **Custom field columns** matching your created fields
* **One contact per row**

{% code title="contacts.csv" %}

```csv
email,first_name,last_name,company,signup_date
john@example.com,John,Doe,Acme Corp,2024-01-15
jane@example.com,Jane,Smith,Tech Inc,2024-01-20
```

{% endcode %}
{% endstep %}

{% step %}
**Upload Your File**

Click **Browse files** or drag and drop your CSV file into the upload area.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-818861c851a8ae2daae5910431f438fb91b0d1ed%2Fmarketing-contacts-upload-csv.png?alt=media" alt="File upload area to import contacts CSV file" width="563"></div>

Click **Import File** to proceed.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-0a6c81e684ed1f668f7501d035228530658133f7%2Fmarketing-contacts-import-file.png?alt=media" alt="Import File button to proceed with contact upload" width="563"></div>
{% endstep %}

{% step %}
**Map Your Fields**

Assign CSV columns to your Mailtrap fields:

* Match column headers to custom fields
* Preview data mapping
* Verify field assignments

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b4d267c8d98f4bfcdf04f734d36874fb79941428%2Fmarketing-contacts-field-mapping.png?alt=media" alt="Field mapping interface to assign CSV columns to contact fields" width="563"></div>

Click **Confirm Mapping** when ready.

{% hint style="info" %}
**Mapping Tips**

* Field names are case-insensitive
* Unmapped columns will be ignored
* Email field is automatically mapped if column is named "email"
  {% endhint %}
  {% endstep %}

{% step %}
**Assign to Lists**

Choose which lists should include these contacts:

**Add to Existing Lists**

Select one or more lists from the dropdown and click **Continue**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-880e3e234720fe54e7e3ff1c9f7eca518d07cbed%2Fmarketing-contacts-add-to-list.png?alt=media" alt="Interface to add contacts to existing lists" width="563"></div>

**Create New List**

Click **Create New List**, enter a name, and click **Create**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a8e2be1deff224bb7339338748f47b0235703127%2Fmarketing-contacts-create-new-list.png?alt=media" alt="Form to create a new contact list" width="563"></div>

{% hint style="success" %}
**Multiple Lists** You can add contacts to multiple lists simultaneously for better segmentation.
{% endhint %}

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-10689af977663a6d3d7417ef63fea5cb25ec3921%2Fmarketing-contacts-multiple-lists.png?alt=media" alt="Interface showing contacts being added to multiple lists" width="563"></div>
{% endstep %}

{% step %}
**Confirm Consent**

Check the consent verification box to confirm you have permission to email these contacts.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ea4b0e1bb1e85cc58d86ed915f3d8243b16d08bd%2Fmarketing-contacts-confirm-consent.png?alt=media" alt="Consent confirmation checkbox before importing contacts" width="563"></div>

{% hint style="danger" %}
**Legal Requirement** You cannot proceed without confirming consent. Ensure you have explicit permission from all contacts before importing.
{% endhint %}

Click **Confirm Import** to complete the process.
{% endstep %}

{% step %}
**Import Confirmation**

You'll receive a success notification once the import is complete.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c0c5d29d7b7fa6b15a485dca13d9dad320ab798a%2Fmarketing-contacts-import-success.png?alt=media" alt="Success notification after contacts are imported" width="563"></div>

Your contacts are now available under **Contacts** and in their assigned **Lists**.
{% endstep %}
{% endstepper %}

## API Import

### Quick Start

{% tabs %}
{% tab title="cURL" %}
{% code title="Add single contact" %}

```bash
curl -X POST https://api.mailtrap.io/contacts \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "lists": ["list_id_1", "list_id_2"]
  }'
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code title="Add multiple contacts" %}

```javascript
const contacts = [
  {
    email: "user1@example.com",
    first_name: "John",
    custom_fields: { company: "Acme Corp" }
  },
  {
    email: "user2@example.com",
    first_name: "Jane",
    custom_fields: { company: "Tech Inc" }
  }
];

await fetch('https://api.mailtrap.io/contacts/batch', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ contacts, lists: ["list_id"] })
});
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code title="Update contact" %}

```python
import requests

contact_data = {
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Updated",
    "custom_fields": {
        "last_activity": "2024-01-20"
    }
}

response = requests.put(
    "https://api.mailtrap.io/contacts/user@example.com",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json=contact_data
)
```

{% endcode %}
{% endtab %}
{% endtabs %}

For complete API documentation, see [Contacts API Reference](https://github.com/mailtrap/mailtrap-docs/blob/main/api-docs/contacts-api.md).

## Third-party Integrations

### Zapier Integration

{% stepper %}
{% step %}
**Connect Mailtrap**

Add Mailtrap as an action in your Zap.
{% endstep %}

{% step %}
**Configure Trigger**

Set up your trigger app (CRM, form, spreadsheet).
{% endstep %}

{% step %}
**Map Fields**

Match trigger data to Mailtrap contact fields.
{% endstep %}

{% step %}
**Test & Activate**

Run a test and activate your Zap.
{% endstep %}
{% endstepper %}

### Make.com Scenario

Create automated workflows that sync contacts from multiple sources:

{% code title="Example Scenario" %}

```json
{
  "trigger": "New form submission",
  "actions": [
    {
      "app": "Mailtrap",
      "action": "Create/Update Contact",
      "fields": {
        "email": "{{form.email}}",
        "first_name": "{{form.name}}",
        "source": "Website Form"
      }
    }
  ]
}
```

{% endcode %}

## Import Best Practices

{% hint style="success" %}
**Data Quality Guidelines**

1. **Validate emails**: Remove invalid or malformed addresses
2. **Remove duplicates**: Clean your list before importing
3. **Standardize formats**: Use consistent date and text formats
4. **Test small batches**: Import a test batch first
5. **Monitor bounces**: Track delivery after first campaign
   {% endhint %}

## Handling Import Errors

## Import Limits

{% hint style="info" %}
**Upload Specifications**

* **File size**: Up to 10MB per CSV
* **Contacts per import**: Up to 50,000
* **Import frequency**: No limit
* **Processing time**: 1-5 minutes for large files
  {% endhint %}


# Lists

Organize contacts into targeted groups for effective email campaigns

Lists are static groups of contacts that help you organize your audience for targeted email campaigns. Unlike segments, lists don't update automatically - contacts must be manually added or removed.

## Understanding Lists

{% hint style="info" %}
**Lists vs. Segments**

* **Lists**: Static groups that you manually manage
* **Segments**: Dynamic groups that update automatically based on criteria

Use lists for stable groups (e.g., "Newsletter Subscribers") and segments for criteria-based targeting (e.g., "Active in last 30 days").
{% endhint %}

## Creating Lists

### Quick Create

{% stepper %}
{% step %}
**Navigate to Lists**

Go to **Contacts** → **Lists** in your dashboard.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b50901dc346a047817f1dc543cd5e86a8020078c%2Fmarketing-lists-create-button.png?alt=media" alt="Create List button in the Lists interface" width="563"></div>
{% endstep %}

{% step %}
**Create New List**

Click **Create List** to open the creation dialog.
{% endstep %}

{% step %}
**Name Your List**

Enter a descriptive name for your list.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8796cf161f456e26af40f1bbf0fffaf2962128a6%2Fmarketing-lists-create-form.png?alt=media" alt="Form to enter new list name" width="563"></div>

{% hint style="warning" %}
List names must be unique. You cannot create duplicate list names.
{% endhint %}
{% endstep %}

{% step %}
**Save List**

Click **Create** to save your new list.

Your list is now ready to receive contacts.
{% endstep %}
{% endstepper %}

### List Creation During Import

You can also create lists while importing contacts:

{% code title="Import Flow" %}

```
1. Upload CSV → 2. Map Fields → 3. Create New List → 4. Add Contacts
```

{% endcode %}

## Managing Lists

Access all your lists from **Contacts** → **Lists**:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-eef638c08c368ea5285f46a28e6cc5fda1617f76%2Fmarketing-lists-manage.png?alt=media" alt="Lists management page showing all created lists" width="563"></div>

### List Actions

{% tabs %}
{% tab title="View Contacts" %}
**See all contacts in a list**

* Click on list name
* View contact count
* Filter within list
* Export list members
  {% endtab %}

{% tab title="Rename List" %}
**Change list name**

* Click rename icon
* Enter new name
* Ensure uniqueness
* Save changes
  {% endtab %}

{% tab title="Delete List" %}
**Remove list permanently**

* Click delete icon
* Confirm deletion
* Contacts remain in database
* Only list association removed

{% hint style="info" %}
Deleting a list doesn't delete the contacts, only their association with that list.
{% endhint %}
{% endtab %}

{% tab title="Merge Lists" %}
**Combine multiple lists**

* Select source lists
* Choose destination
* Remove duplicates
* Preserve all contacts
  {% endtab %}
  {% endtabs %}

## Adding Contacts to Lists

### Methods Overview

{% tabs %}
{% tab title="During Import" %}
Add contacts to lists while uploading CSV files:

* Select existing lists
* Create new lists on the fly
* Add to multiple lists at once
  {% endtab %}

{% tab title="Individual Add" %}
Add single contacts from contact details:

1. Open contact profile
2. Click "Add to Lists"
3. Select target lists
4. Save changes
   {% endtab %}

{% tab title="Bulk Add" %}
Add multiple contacts at once:

1. Select contacts in grid
2. Choose "Add to Lists"
3. Pick destination lists
4. Confirm action
   {% endtab %}

{% tab title="API Integration" %}
Programmatically add contacts:

```javascript
{
  "email": "user@example.com",
  "lists": ["list_id_1", "list_id_2"]
}
```

{% endtab %}
{% endtabs %}

## List Best Practices

{% hint style="success" %}
**Effective List Management**

1. **Naming Convention**: Use clear, consistent names (e.g., "2024-Q1-Newsletter")
2. **Regular Maintenance**: Review and clean lists quarterly
3. **Documentation**: Note list purpose and criteria
4. **Size Limits**: Keep lists under 50,000 for optimal performance
5. **Avoid Duplication**: Use segments for criteria-based filtering
   {% endhint %}

## List Strategies

### Welcome Series Lists

{% stepper %}
{% step %}
**Create Onboarding Lists**

* Day 1 Welcome
* Day 3 Follow-up
* Week 1 Check-in
* Day 30 Milestone
  {% endstep %}

{% step %}
**Automate Movement**

Use API or integrations to move contacts through lists based on timeline.
{% endstep %}

{% step %}
**Track Progress**

Monitor engagement at each stage to optimize onboarding.
{% endstep %}
{% endstepper %}

### A/B Testing Lists

Split your audience for testing:

{% code title="Test Structure" %}

```
Main List: Newsletter Subscribers (10,000)
├── Test Group A (2,500) - Subject Line A
├── Test Group B (2,500) - Subject Line B
└── Remainder (5,000) - Winning Version
```

{% endcode %}

### Suppression Lists

Create lists for contacts to exclude:

* Competitors
* Internal emails
* Bounced addresses
* Complaint/spam reporters
* Do not contact

## List Performance Metrics

### Key Indicators

{% tabs %}
{% tab title="Growth Rate" %}
**Track list expansion**

```
Monthly Growth = (New - Removed) / Total × 100
```

Healthy growth: 2-5% monthly
{% endtab %}

{% tab title="Engagement Score" %}
**Measure list quality**

```
Engagement = (Opens + Clicks) / Sent × 100
```

Good engagement: >25% open rate
{% endtab %}

{% tab title="Churn Rate" %}
**Monitor list health**

```
Churn = Unsubscribes / Total × 100
```

Acceptable churn: <2% per campaign
{% endtab %}

{% tab title="List Overlap" %}
**Identify redundancy**

```
Overlap = Shared Contacts / Smaller List × 100
```

Consider merging if >70% overlap
{% endtab %}
{% endtabs %}

## Advanced List Management

### Dynamic List Updates

Use webhooks to automatically update lists:

{% code title="Webhook Example" %}

```json
{
  "event": "user.signup",
  "action": "add_to_list",
  "list_id": "new_users_2024",
  "contact": {
    "email": "user@example.com",
    "signup_date": "2024-01-20"
  }
}
```

{% endcode %}

### List Segmentation

Combine lists with segments for powerful targeting:

{% code title="Combined Targeting" %}

```
List: "Premium Customers"
  + Segment: "Opened Last Campaign"
  + Filter: "Location = USA"
  = Targeted Campaign Group
```

{% endcode %}

## List Limits and Quotas

{% hint style="info" %}
**Technical Specifications**

* **Lists per account**: Unlimited
* **Contacts per list**: No hard limit (recommend <50,000)
* **List name length**: 100 characters
* **Bulk operations**: 1,000 contacts at once
* **API rate limits**: 100 requests/minute
  {% endhint %}


# Segments

Create dynamic contact groups that automatically update based on criteria

Segments are dynamic groups of contacts that automatically update based on criteria you define. Unlike static lists, segments continuously evaluate your contacts and adjust membership as contact properties change.

## Understanding Segments

{% hint style="info" %}
**Dynamic vs. Static Groups**

* **Segments**: Automatically update based on rules and conditions
* **Lists**: Manually managed, static groups

Example: A segment for "Active Users" automatically adds contacts who opened emails in the last 30 days and removes those who haven't.
{% endhint %}

## Why Use Segments?

{% tabs %}
{% tab title="Automation" %}
**Self-maintaining groups**

* No manual updates needed
* Always current membership
* Reduces human error
* Saves time on list management
  {% endtab %}

{% tab title="Precision Targeting" %}
**Complex criteria combinations**

* Multiple conditions (AND/OR)
* Behavioral targeting
* Demographic filtering
* Engagement-based grouping
  {% endtab %}

{% tab title="Real-time Updates" %}
**Always accurate**

* Instant membership changes
* Reflects latest data
* No stale information
* Perfect for time-sensitive campaigns
  {% endtab %}

{% tab title="Scalability" %}
**Grows with your database**

* Handles any contact volume
* Consistent rules application
* No performance degradation
* Efficient processing
  {% endtab %}
  {% endtabs %}

## Creating Segments

{% stepper %}
{% step %}
**Navigate to Segments**

Go to **Contacts** → **Segments** in your dashboard.
{% endstep %}

{% step %}
**Click Create Segment**

Select **Create Segment** to start building your dynamic group.
{% endstep %}

{% step %}
**Name Your Segment**

Provide a descriptive name that clearly indicates the segment's purpose.

Example: "High-Value Customers - Last 90 Days"
{% endstep %}

{% step %}
**Define Conditions**

Set up rules using:

* Contact fields
* Engagement metrics
* List membership
* Custom properties

Use AND/OR logic to combine multiple conditions.
{% endstep %}

{% step %}
**Preview Results**

Review the contacts that match your criteria before saving.
{% endstep %}

{% step %}
**Save and Activate**

Save your segment to start using it in campaigns.
{% endstep %}
{% endstepper %}


# Help & Support

Get help with Email Marketing issues and find answers to common questions

Find answers to common questions and troubleshoot issues with Email Marketing. Get help with campaign creation, contact management, analytics, and more.

### Campaign Creation Issues

#### Domain not verified

**Problem**: Can't send campaigns without verified domain **Solution**:

1. Go to Sending Domains
2. Add your domain
3. Add DNS records to your provider
4. Wait for verification (usually < 1 hour)
5. Check verification status

#### Template not saving

**Problem**: Changes to email template lost **Solution**:

* Click "Save" before navigating away
* Check for HTML validation errors
* Ensure template size < 100KB
* Clear browser cache if persistent

#### Images not displaying

**Problem**: Images broken in preview/sent emails **Solution**:

* Use absolute URLs for images
* Host images on reliable CDN
* Check image file size (< 1MB recommended)
* Verify image format (JPG, PNG, GIF)

### Contact Management Issues

#### Import failures

**Problem**: CSV import not working **Solution**:

```csv
email,first_name,last_name,custom_field
john@example.com,John,Doe,Value1
jane@example.com,Jane,Smith,Value2
```

* Use UTF-8 encoding
* Include email header
* Remove special characters
* Check for duplicate emails

#### Contacts not receiving emails

**Possible causes**:

1. **Suppressed**: Check suppression list
2. **Bounced**: Review bounce status
3. **Unsubscribed**: Verify subscription status
4. **Invalid email**: Check email format
5. **Segment exclusion**: Review segment criteria

### Delivery Issues

#### Low open rates

**Troubleshooting checklist**:

* ✓ Subject line optimization
* ✓ Sender name recognition
* ✓ Send time optimization
* ✓ List quality check
* ✓ Spam score review

#### High bounce rate

**Common causes & fixes**:

| Bounce Type | Cause         | Solution         |
| ----------- | ------------- | ---------------- |
| Hard bounce | Invalid email | Remove from list |
| Soft bounce | Mailbox full  | Retry later      |
| Block       | Spam filters  | Improve content  |
| Technical   | Server issue  | Contact support  |

#### Spam complaints

**Prevention strategies**:

* Use double opt-in
* Clear unsubscribe link
* Relevant content only
* Consistent sending frequency
* Honor preferences immediately

## Getting Help

### Self-Service Options

1. **Documentation Search**: Use search bar above
2. **Video Tutorials**: [YouTube Channel](https://www.youtube.com/@mailtrap-official)
3. **Blog Resources**: [mailtrap.io/blog](https://mailtrap.io/blog)
4. **API Reference**: [API Docs](https://api-docs.mailtrap.io)

### <i class="fa-comments-question-check">:comments-question-check:</i>Contact Support

If you can’t find the answer you need in our documentation and would like to contact support and speak with an agent, we’re here to help.

You can get in touch with the Mailtrap Support team using one of the following ways:

* **From your Mailtrap account**&#x20;

1. Log in to your account [here](https://mailtrap.io/signin).
2. Go to the <i class="fa-circle-question">:circle-question:</i>[<mark style="color:$primary;">**Help Center**</mark>](https://mailtrap.io/help-center) > <i class="fa-message-dots">:message-dots:</i> Get Help
3. Click <mark style="color:$primary;">**Start conversation.**</mark>&#x20;

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7hftpJFYZKk1D4GQCYd8%2FScreenshot%202026-02-19%20at%2017.12.57.png?alt=media&#x26;token=90aebf2d-07b7-4c5b-aa6b-07623bc02077" alt=""><figcaption></figcaption></figure>

* **Email us at** 📧 <support@mailtrap.io>

Whether you need technical assistance, help troubleshooting an issue, or simply want to talk to customer support, our team will be happy to assist you.

## Quick Solutions

### Campaign Issues

#### Schedule campaign not sending

```javascript
// Check schedule settings
{
  "scheduled_for": "2024-01-15T10:00:00Z",
  "timezone": "America/New_York",
  "status": "scheduled"
}
```

* Verify time zone settings
* Check for past dates
* Confirm campaign approved
* Review sending limits

#### A/B test not working

Requirements for A/B testing:

* Minimum 1,000 recipients
* Test percentage 10-50%
* Single variable change
* Sufficient test duration

### Analytics Problems

#### Stats not updating

* **Wait time**: Allow 5-10 minutes
* **Cache**: Clear browser cache
* **Filters**: Check date range
* **Timezone**: Verify settings

#### Click tracking not working

```html
<!-- Ensure links are properly formatted -->
<a href="https://example.com/page">Click here</a>

<!-- Not tracked -->
<a href="javascript:void(0)">Click</a>
<a href="mailto:email@example.com">Email</a>
```

## Best Practices

### Campaign Optimization

* **Subject Lines**: 30-50 characters
* **Preview Text**: 35-90 characters
* **Send Time**: Tuesday-Thursday, 10 AM
* **Frequency**: 1-4 emails/month
* **Segmentation**: Target < 1000 per segment

### List Management

* Regular list cleaning (quarterly)
* Re-engagement campaigns
* Sunset policy for inactives
* Double opt-in for new subscribers
* Preference center implementation

### Content Guidelines

* Mobile-first design
* Clear CTA above fold
* Alt text for images
* Plain text version
* Accessibility compliance

## Debugging Tools

### Email Testing Checklist

```markdown
- [ ] Preview in major clients
- [ ] Test all links
- [ ] Verify personalization
- [ ] Check spam score
- [ ] Test on mobile devices
- [ ] Verify unsubscribe link
- [ ] Review footer compliance
- [ ] Test dynamic content
```

### Campaign Diagnostics

```sql
-- Check campaign performance
SELECT
  sent_count,
  delivered_count,
  open_count,
  click_count,
  bounce_count,
  unsubscribe_count
FROM campaigns
WHERE campaign_id = 'YOUR_CAMPAIGN_ID';
```

## Feedback & suggestions

*We welcome technical feedback and contributions that help us improve Mailtrap’s functionality and documentation. Please use the appropriate channel depending on the type of request.*

#### <i class="fa-bug">:bug:</i>Bug Reports

**If you encounter a product issue or unexpected behavior, please** [#contact-support](#contact-support "mention")**.**

To help us investigate efficiently, include:

* A detailed description of the issue
* Exact reproduction steps
* Relevant stream, domain, sandbox, or account details
* Timestamps (including timezone)
* Screenshots or logs if available

#### <i class="fa-file-circle-plus">:file-circle-plus:</i>Feature Requests

For product improvements or new feature proposals, use our [Public Roadmap](https://mailtrap.featurebase.app/en) portal.

There you can:

* **Submit a new feature request**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ff9yf6pEv5ZXR4EHh5ABg%2FScreenshot%202026-03-02%20at%2010.32.03.png?alt=media&#x26;token=2cea9a79-0387-4fb3-988d-272d13327b77" alt="" width="375"><figcaption></figcaption></figure></div>

* **Upvote existing requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fax54DgMBWcXzIQEiLeCg%2FScreenshot%202026-03-02%20at%2010.33.40.png?alt=media&#x26;token=0454c018-c008-4287-a329-407bcd3e1c35" alt="" width="375"><figcaption></figcaption></figure></div>

* **Subscribe to updates for specific requests**

<div align="left"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FmB0AdDAkT5l43l0jmBps%2FScreenshot%202026-03-02%20at%2010.33.11.png?alt=media&#x26;token=790a0502-73e1-4bd2-803a-c4b4c7973d60" alt="" width="375"><figcaption></figcaption></figure></div>

:soon:**The following enhancements are currently planned or in progress:**

* Advanced automation workflows
* Enhanced personalization
* SMS marketing integration
* AI content suggestions
* Advanced segmentation

You can follow updates and release progress directly in Featurebase.

#### <i class="fa-file-doc">:file-doc:</i>Documentation Improvements

If you identify unclear, incomplete, or outdated documentation:

1. Use the **feedback widget** located on the right-hand side of the page to rate the article:\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FOLpynTOT2XMAP3d7c7Ct%2FScreenshot%202026-03-02%20at%2010.30.47.png?alt=media\&token=c71836e0-95da-47ae-b9d7-917dbebc9149)
2. **Provide specific feedback** describing what should be corrected, clarified, or expanded\
   ![](https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FU94kVQcPPjT7e6bgJz4m%2FScreenshot%202026-03-02%20at%2010.31.22.png?alt=media\&token=7e0ec64d-058e-4b47-a25f-4bd01d40e549)

This helps us continuously refine our docs.

#### <i class="fa-square-code">:square-code:</i>GitHub & Technical Collaboration

For open-source projects, SDKs, or public repositories, join us on [GitHub](https://github.com/mailtrap).

## Training Resources

### Getting Started

* [Quick Start Guide](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/copy-of-email-marketing.md)
* [Video Walkthrough](https://www.youtube.com/watch?v=example)
* [Best Practices Guide](https://mailtrap.io/blog/email-marketing-best-practices/)

### Advanced Topics

* [Segmentation Strategies](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/help/broken-reference/README.md)
* [Automation Workflows](https://docs.mailtrap.io/documentation/email-marketing/automations)
* [Analytics Deep Dive](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-marketing/help/broken-reference/README.md)
* [Template Optimization](https://docs.mailtrap.io/documentation/email-marketing/campaigns/email-templates)

### Webinars & Training

* Monthly product webinars
* On-demand training videos
* Custom training (Enterprise)
* Certification program

## System Status

### Check Service Status

* **Status Page**: [status.mailtrap.io](https://status.mailtrap.io)
* **Planned Maintenance**: Announced 48 hours ahead
* **API Status**: Separate monitoring
* **Subscribe**: Get status updates via email

### Performance Metrics

* Email delivery: 99.9% uptime
* API availability: 99.95% uptime
* Average send time: < 2 seconds
* Support response: < 24 hours


# FAQs

Frequently asked questions about Mailtrap Email Marketing

Find quick answers to common questions about Mailtrap Email Marketing, including campaign creation, contact management, analytics, and more.

## General Questions

<details>

<summary>What is Mailtrap Email Marketing?</summary>

Mailtrap Email Marketing is a complete solution for creating, sending, and tracking email campaigns. It includes a drag-and-drop editor, contact management, automation tools, and detailed analytics.

</details>

<details>

<summary>How is Email Marketing different from Email API/SMTP?</summary>

Email Marketing is designed for bulk promotional emails with built-in campaign tools, while Email API/SMTP is for transactional emails like password resets. Email Marketing includes visual editors, contact management, and campaign analytics.

</details>

## Campaign Creation

<details>

<summary>Do I need coding skills to create campaigns?</summary>

No! Our drag-and-drop editor requires no coding. However, we also offer an HTML editor for those who prefer to code their emails.

</details>

<details>

<summary>Can I use my own HTML templates?</summary>

Yes, you can import your own HTML templates or create them from scratch using our HTML editor. Templates can be saved and reused across campaigns.

</details>

<details>

<summary>How do I personalize emails?</summary>

Use merge tags in your content:

```
Hi {{first_name}},

Thank you for being a {{customer_type}} customer for {{years_active}} years!
```

These will be replaced with actual contact data when sent.

</details>

## Contact Management

<details>

<summary>How do I import contacts?</summary>

You can import contacts via:

1. **CSV Upload**: Upload a CSV file with contact data
2. **Copy/Paste**: Paste contact list directly
3. **API**: Import programmatically
4. **Integrations**: Sync from CRM or e-commerce platforms using our Zapier, Make.com, n8n integrations.

</details>

<details>

<summary>Can I export my contacts?</summary>

Yes, you can export contacts anytime as CSV including all custom fields and engagement data. This ensures data portability and GDPR compliance.

</details>

<details>

<summary>What happens to unsubscribed contacts?</summary>

Unsubscribed contacts:

* Remain in your account for record-keeping
* Cannot receive campaigns
* Count toward your plan limits

</details>

## Sending & Delivery

<details>

<summary>Why do I need to verify my domain?</summary>

Domain verification:

* Proves you own the domain
* Improves deliverability
* Required for sending campaigns
* Enables DKIM and SPF authentication
* Reduces spam classification

</details>

<details>

<summary>What are typical open rates?</summary>

Industry averages:

* B2B: 21-23%
* E-commerce: 15-18%
* Non-profit: 25-28%
* Media: 20-22%

Your rates depend on list quality, content relevance, and sending practices.

</details>

<details>

<summary>How can I improve deliverability?</summary>

Best practices:

1. Verify your domain properly
2. Use double opt-in
3. Clean your list regularly
4. Maintain consistent sending
5. Avoid spam trigger words
6. Include unsubscribe links
7. Monitor engagement metrics

Check our [Deliverability Guide](https://mailtrap.io/email-deliverability-guide/) for more info.

</details>

<details>

<summary>Can I send to purchased lists?</summary>

No. Sending to purchased lists:

* Violates our Terms of Service
* Results in high bounce/spam rates
* Can lead to account suspension
* Damages sender reputation Only send to contacts who explicitly opted in.

</details>

## Analytics & Reporting

<details>

<summary>When will I see campaign statistics?</summary>

* **Delivery stats**: Within 5 minutes
* **Opens**: Real-time as they happen
* **Clicks**: Real-time tracking
* **Unsubscribes**: Immediate
* **Full report**: 24-48 hours for completion

</details>

<details>

<summary>How is open rate tracked?</summary>

Open tracking works via a tiny, invisible image (pixel) in the email. When the image loads, we record an open. Note that:

* Some clients block images (undercounts opens)
* Privacy features may affect accuracy

</details>

## Compliance & Legal

<details>

<summary>Is Mailtrap GDPR compliant?</summary>

Yes, we are fully GDPR compliant:

* Data processing agreements available
* Data portability features
* Right to deletion support

</details>

<details>

<summary>What's required in email footers?</summary>

Legal requirements:

* Physical mailing address
* Unsubscribe link
* Company identification
* Clear sender information

We automatically add these if missing.

</details>

<details>

<summary>How are unsubscribes handled?</summary>

Unsubscribe process:

1. One-click unsubscribe link in every email
2. Immediate processing (within seconds)
3. Confirmation page shown
4. Contact moved to suppression list

</details>

## Billing & Account

<details>

<summary>Can I change plans anytime?</summary>

Yes, you can:

* Upgrade instantly
* Downgrade at end of billing cycle
* Switch between monthly/annual
* Cancel anytime
* No long-term contracts required

</details>

<details>

<summary>Do unused emails roll over?</summary>

No, monthly email quotas don't roll over. However:

* Additional emails counted as overage
* Upgrade anytime for more capacity

</details>


# User Management & Organizations

Manage users, teams, and organizational structure in Mailtrap. Control permissions, access, and collaboration.

Efficiently manage your team's access to Mailtrap. Control permissions, organize users into teams, and maintain security across your organization.

## User Management Features

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Organization &#x26; Sub-Accounts</strong></td><td><em>Structure your Mailtrap account with organizations and sub-accounts for better resource management and billing separation.</em></td><td><a href="management/organization-and-sub-accounts">organization-and-sub-accounts</a></td></tr><tr><td><strong>User Roles &#x26; Management</strong></td><td><em>Add, remove, and manage team members. Control access levels and permissions for different users.</em></td><td><a href="management/users">users</a></td></tr><tr><td><strong>User Profile</strong></td><td><em>Manage individual user profiles, preferences, and settings within your organization.</em></td><td><a href="management/user-profile">user-profile</a></td></tr><tr><td><strong>My Profile</strong></td><td><em>Personal profile management including account settings, notifications, and security options.</em></td><td><a href="management/my-profile">my-profile</a></td></tr><tr><td><strong>SSO Guide</strong></td><td><em>Learn how to configure SAML 2.0 single sign-on (SSO) with Mailtrap using any Identity Provider that supports the SAML 2.0 protocol.</em></td><td><a href="management/sso">sso</a></td></tr></tbody></table>


# Organization & Sub-Accounts

Manage complex setups with Mailtrap Organization & Sub‑Accounts. Learn about centralized billing, isolated workspaces, permissions, and how to create and migrate sub-accounts.

### Overview

The **Organization & Sub-Accounts** structure is designed to help you manage complex setups involving multiple teams, clients, environments, or products - all under a single Organization.

Each **sub-account** functions as a fully isolated workspace with its own set of projects, sending domains, email templates, stats, credentials (SMTP/API), and even team members. This separation ensures that data, permissions, and sending behavior in one sub‑account will never affect the others.

At the same time, your **Organization** acts as the central hub:

* **Centralized billing** lets you keep all sub‑accounts under one subscription plan and one invoice.
* **Shared quota pools** apply across all sub‑accounts using Email API/SMTP, Email Campaigns or Email Sandbox, making it easy to allocate resources flexibly.
* **Org-level permissions** give users access to all current and future sub‑accounts by default - ideal for admins or managers.
* **Sub-account-level permissions** can be assigned when you need to restrict access to just selected environments or clients.
* **Clear separation of data**. Projects, templates, stats, and domains stay neatly separated between sub‑accounts.
* **Deliverability isolation**. Each sub‑account's sending reputation stays isolated. If one goes off track, others remain unaffected.
* **Smooth migration of accounts**. Existing standalone accounts can be converted to sub‑accounts, bringing over settings, stats, and domains seamlessly.

This structure is ideal whether you're working with:

* **API/SMTP**
* **Email Campaigns**
* **Email Sandbox**

No matter the product, sub‑accounts remain consistently isolated and manageable.

Additionally, if your teams or clients shift over time, you can **transfer sub‑accounts between Organizations** without losing historical data, settings, or domain authentications. Our support team can guide you through this process to make it smooth and safe.

{% hint style="info" %}
The Organization & Sub‑Accounts feature is available only on **Business** and **Enterprise** Email Sending or Sandbox plans. If you don't see this option in your user panel, you may need to upgrade your plan to access it.
{% endhint %}

{% hint style="warning" %}
If your account is currently using Braintree as the payment gateway, you'll need to migrate to Stripe in order to enable and use the Organization & Sub‑Accounts feature.
{% endhint %}

### When to use Organization & Sub-accounts

Use Organization & Sub‑accounts to:

* Isolate own projects or products.
* Serve multiple clients or brands without overlap.
* Control access for different teams, business units or clients.
* Prevent issues in one sub‑account affecting others.
* Keep email stats, templates, or sender configurations isolated.

### Creating a sub-account

{% stepper %}
{% step %}
Go to the left-side menu and select **Organization**. This will open the **Organization** panel.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ec75eae58cddc7c93130bbf623e8bebfb79d3109%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Sub-accounts** menu item and **Create Sub-Account** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b1f0c5ad0ccacce3f0319bfcafa7fc844a2f5fb9%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter the sub-account name and click **Create**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-03af7222cc226abd1f4ba029df63b72fe1583b08%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
You will be automatically redirected to the new account settings page, where you can manage other account settings.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-ee19e67666ab6d7529f96809be65405d103a6b0f%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

You're ready! Each sub‑account starts fresh with no domains, tokens, or stats - configure however you like.

You can create as many sub‑accounts as needed - there is no limit, making this feature scalable for any organization size.

{% hint style="info" %}
Sub‑accounts can be created through the user interface or through the API as well.
{% endhint %}

Switch between your organizations and sub‑accounts from the left-side menu anytime.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aed34102ed12822f184ea43788c644d299237372%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

### Migrating an already existing account

If you have multiple Mailtrap accounts and want to merge them under a single Organization (without re-authenticating domains or losing data), our Support Team can help make the process smooth. You can transfer any account, including free ones. The only requirement is that the **destination Organization** is on a subscription plan that includes **Organization & Sub-accounts**.

To start, email us at <support@mailtrap.io> from the account owner's email address (the one who owns the account you want to move) and include:

* **Account name or ID** you want to transfer
* **Destination Organization name or ID**
* **Email address of the destination Organization Owner** (for security verification)
* **Reason for the transfer** (e.g., merging workspaces, restructuring your team, etc.)

Once we receive your request, our team will confirm the transfer with both sides.

{% hint style="warning" %}
**Important notes**

* If you need to transfer multiple accounts, please submit **one request per account**. Always send each request from the account owner's email.
* The transferred account will be **removed from the original Organization**.
* Original Organization admins and viewers will lose access to this account. **Account-level admins and viewers will retain their access.**
* If the transferred account was the **only one** in the original Organization, the subscription for that Organization will be canceled. If no accounts remain, the empty Organization will be deleted.
  {% endhint %}

**Transfer and access**

After both sides approve:

* The account will be moved from the Original Organization to the Destination Organization.
* The account will now use the **subscription and usage limits of the Destination Organization**.
* Usage counters will reset, since the account is now part of a new shared plan.

### Permissions & user management

The Organization & Sub‑Accounts structure offers flexible and secure user access controls, so you can easily tailor permissions based on team roles, client needs, or project scope.

#### Types of access

There are two levels of user access:

**1.&#x20;*****Organization-level access***

Users with this access-level can see and manage **all current and future sub-accounts** within the Organization. This is ideal for admins, finance, or central teams that need a global overview. You can assign roles such as:

* **Org Owner** – The highest-level role within Organization structure. This role is automatically assigned to the person who created the Organization and comes with full, unrestricted access.
* **Org Admin** – Full access to organization settings and billing, as well as admin access to all sub‑accounts.
* **Org Viewer** – View-only access to organization settings and billing, as well as view access to all sub‑accounts.

{% hint style="info" %}
A user with organization-level permissions will always have access to all organization-related pages in the Mailtrap UI, regardless of which sub‑account they are currently logged into.
{% endhint %}

* **Billing Admin** - Full access to billing.
* **Billing Viewer** - View-only access to billing.

**2.&#x20;*****Account-level access***

If a user only needs access to selected sub‑accounts, you can invite them to those accounts only. Description of account-level roles can be found here: [Account-level User Management](https://docs.mailtrap.io/documentation/account-and-organization/management/users).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-14639c91e38635d46da298c498a227c7135da257%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Users can be invited with a single email address to both Organization and selected Sub‑accounts as needed. You don't need to create multiple invitations for the same person.
{% endhint %}

#### Viewing current users

You can easily check who has access to your account.

* **Account users**:

Go to the **Settings** → **User Management** tab to see a list of all users with account-level access. Permissions can be updated at any time from this panel - you can change access rights or remove users with just a few clicks.

* **Organization-level users**:

All users with Organization-level access also have access to your account, and they are listed in a separate **"Organization"** tab. These users automatically have access to all current and future sub‑accounts.

If you are an Organization Owner or Organization Admin, you can edit organization-level users (e.g., invite, remove, or change roles). If you don't have admin rights, you will still see the full list of org-level users, but only in view-only mode.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-baf4791e65f58a393ca5c615735f7faa78c8cbf2%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

### API tokens

API tokens in Mailtrap are account–level. That means each sub‑account has its own isolated set of tokens used for authentication when interacting with Mailtrap's API or SMTP services. Also, an organization has its own tokens to create and list their sub-accounts.

#### Key Points

* **Isolated by design**: Tokens are unique to each sub‑account and cannot be used to access resources from other sub‑accounts or the entire Organization.
* **Scoped access**: API tokens grant access only to the specific data and resources within the sub‑account they were created in, helping maintain strict separation between teams or environments.
* **Management via UI**: Tokens can currently be created, viewed, and revoked via the API Tokens section inside each sub‑account.

### FAQ

#### Users and Permissions

<details>

<summary>Are the number of users shared for all the sub-accounts under the organization?</summary>

Yes, user counts are shared across all sub-accounts within the organization.

</details>

<details>

<summary>How am I counted as a user if I have permissions to more than 1 sub-account?</summary>

You'll still be counted as one user, regardless of how many sub-accounts you have access to within the organization.

</details>

<details>

<summary>Can a user be in multiple sub-accounts?</summary>

Yes, just invite them to each sub‑account and assign the right role. You can also add users to the entire Organization, and thus, they will have access to all sub-accounts within your Organization.

</details>

#### Organization and Sub-Account Management

<details>

<summary>How can a sub-account be removed from the organization they're currently in?</summary>

You can either fully delete the sub-account (using the same process as deleting standard accounts) or contact our Support Team to transfer the sub-account to another Organization.

</details>

<details>

<summary>Need to migrate existing accounts into one Organization?</summary>

Sure! Reach out to us, and we'll help you move everything over without losing data or re-verifying domains.

</details>

<details>

<summary>Can sub-accounts have different plan levels?</summary>

No, the subscription plan is defined at the Organization level and shared across all sub‑accounts.

</details>

<details>

<summary>What about billing?</summary>

All usage is tracked and billed under the Organization's plan. If you need billing per account, we recommend keeping them as standalone accounts.

</details>

<details>

<summary>How to update the organization owner?</summary>

Submit a support request to update the organization owner.

</details>

#### Quotas and Stats

<details>

<summary>Can we set a per sub-account quota limit?</summary>

This feature is currently in development and will be available soon.

</details>

<details>

<summary>Are stats and email quotas shared?</summary>

Quotas apply at the Organization level, but stats are tracked separately for each sub‑account.

</details>

#### General

<details>

<summary>Can sub-accounts share templates?</summary>

No, templates are isolated per sub‑account. You can manually export and import them if needed.

</details>

<details>

<summary>Not seeing the "Organization" menu item?</summary>

Your current plan may not include this feature. You can check our pricing or contact support for help.

</details>


# User Roles & User Management

Manage user roles and permissions in your Mailtrap account. Learn about account owners, admins, viewers, domain permissions, template access, and billing roles.

* **Account Owner** is a person who has registered an account or to whom [it has been transferred](https://docs.mailtrap.io/documentation/account-and-organization/management/my-profile). Account Owner can rename an account, delete it, transfer ownership, manage all projects and sandboxes, and add/edit/invite team members. Nobody can alter the permissions of an Account Owner.
  * **Note**: If the [Organization & Sub-Accounts](https://docs.mailtrap.io/documentation/account-and-organization/management/organization-and-sub-accounts) feature is enabled, this role will be called **Organization Owner**.

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e75dd28c7ff5252fc8070240e6eeb2ce09efbf60%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure></div>

* **Organization Admin** has the same permissions as an Organization Owner, with the exception of deleting an account and transferring its ownership. Organization Owner can alter the permission of Organization Viewers.
* **Organization Viewer** has access to all the entities in the account (projects, sandboxes, billing) but can’t add, edit, or remove anything. For example, the Organization Viewer can view all projects but can’t add new ones or edit existing ones.
* **Account Admin** has the same permissions as an Account Owner, with the exception of deleting an account and transferring its ownership. Account Owner and other Account Admins can alter the permission of Account Admins.
* **Account Viewer** has access to all the entities in the account (projects, sandboxes, billing) but can’t add, edit, or remove anything. For example, the Account Viewer can view all projects but can’t add new ones or edit existing ones.
* **Domain Admin** can rename and delete a domain, manage domain settings (e.g., reset the credentials, enable/disable open or click tracking, or modify unsubscribe footer settings), and add/remove domain team members.
* **Domain Viewer** can view domain settings, reports, statistics, and email logs (except for email content) for the domain but can't add, edit, or remove anything.
* **Templates Admin** can create, edit, delete, and duplicate the templates.
* **Templates Viewer** can only preview templates, check their type, category, and update date.
* **View Email Content** permission is available for all sending domains. It enables Account Owners, Account Admins, and Domain Admins to grant Viewers access to view email bodies in Email Logs. They can provide View Email Content permission for one domain and limit it for another. By default, Account Owners, Account Admins, and Domain Admins have the right to view email bodies, while Viewers don’t.
  * If the user doesn’t have the permission to view email content, they will see the following message in Email Logs:

    <div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3128c32495897402876279d214d44a7a345b5d1a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure></div>
* **Email Campaign Admin** can create, edit, delete, and send email campaigns, as well as view reports.
* **Email Campaign Viewer** can only view email campaigns and campaign reports.
* **Project Admin** can rename and delete a project, fully manage all its sandboxes (add new or delete existing ones), and add or remove project team members. They cannot add new projects in the account.
* **Project Viewer** can see all the sandboxes in the project but can't edit anything (e.g., [sandbox email address](https://docs.mailtrap.io/documentation/email-sandbox/setup/email-address-per-sandbox) or [forwarding settings](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding)). They also can't add or remove teammates, projects, or sandboxes.
* **Sandbox Admin** can rename and delete a sandbox, manage sandbox settings (e.g., reset the credentials or add forwarding rules), and add/remove sandbox team members. However, they can't add new sandbox or projects.
* **Sandbox Viewer** Can see all the sandbox messages but can't edit anything (e.g., [sandbox email address](https://docs.mailtrap.io/documentation/email-sandbox/setup/email-address-per-sandbox) or [forwarding domains](https://docs.mailtrap.io/documentation/email-sandbox/management/automatic-email-forwarding)). They also can't add or remove sandbox teammates, sandboxes, or projects.
* **Billing Admin** permission allows users to manage the Billing settings, add or remove credit cards, upgrade and downgrade the account, and cancel the subscription.
* **Billing Viewer** can only see the credit card on file and details of the current subscription. They can also opt out of receiving invoices to their email address.
  * **Note**: If the Organization & Sub-Accounts feature is enabled, the Billing roles will be visible on a [user management page](https://mailtrap.io/user-management).

<div data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-22eae28856daec9c170251d3f08cf71e082ed89d%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure></div>

When you remove a user on the User Management page, they immediately lose access to your account, but stay in the system as Mailtrap users.

If you remove a person from a Sandbox or a Project, they remain in your account but lose access to a sandbox or a project in question.

A person can stay in your account without any permissions at all. This can happen if you remove them from all projects/sandboxes but not from the list on the User Management page. If you no longer work with a teammate, the best way to remove them is to use the User Management page. Otherwise, users with zero access who are still present on your account will be counted towards your [account limits](https://mailtrap.io/billing/dashboard).

To check your own permissions, find your user on the list and click “edit permissions” in the three dots menu. You’ll see which entities are available to you. You cannot change your own permissions.


# User Profile

Manage your Mailtrap user profile and account settings. Learn how to update your profile, delete your user account, create new accounts, and leave existing accounts.

Once you register with Mailtrap, we automatically create an **account** and a **user profile** for you.**Users** belong to accounts (organisations). Each user and user profile is defined by their email address and may belong to multiple accounts. You use the same credentials to access all your Mailtrap accounts.

### User Profile Management

To manage your user profile, select your current account name or email address in the upper right corner, then click **MyProfile** in the drop-down menu.

There you will be able to copy or reset tokens, view, and edit OAuth providers, change your name, email, and/or password, and set the time zone.

And you can associate a different email address with your account manually, in case you need to transfer your Mailtrap user profile to another person.

**Important Note:**

The tokens under **User settings** work only with Mailtrap Email API v1 and will be deprecated in the future. [Click here](https://docs.mailtrap.io/documentation/email-api-smtp/setup/api-tokens) to learn more about Email API tokens v2 and how to manage them.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-684dcea8cbe5c187b1b5b04c5e51846e1e992ce2%2Fuser-profile-settings.png?alt=media" alt="" width="188"></div>

### Deleting Your User Profile

Click on your account name or email address and choose **My Profile**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-95def529c88f0a9d08c1a52b63ae9e88b8005166%2Fuser-profile-my-profile-dropdown.png?alt=media" alt="" width="261"></div>

Click the **Delete My Profile** button, and follow instructions to remove your user profile.

Only, keep in mind that the action is irreversible and wipes out all associated information. These include your account(s), project(s), sandbox(es), domain(s), and all the related messages.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-33c65a41383c5f7453ad133e51be9bb150795666%2Fuser-profile-delete-button.png?alt=media" alt="" width="188"></div>

If you have problems deleting your Mailtrap user profile, send us an email with your request at <support@mailtrap.io>.

### Create Account

When you delete just your account, your Mailtrap user profile isn't deleted and you can create a new account. This is the only available thing to do when you don't own or don't belong to any account.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-911bce04c9ad1a26a2ae016c397421240c6ca867%2Fuser-profile-create-account.png?alt=media" alt="" width="375"></div>

If you want to delete your Mailtrap user profile, follow the steps described in the previous section. For more information on privacy protection, check your [rights to be forgotten](https://mailtrap.io/dpa/#411-Deletion-or-Retrieval-of-Personal-Data).

### Leave Account

You can also leave accounts that you belong to but don't own them. All the account data stays intact, but you lose the access to it. Use this option if you no longer work with an organisation or a team and don't want to access their data anymore.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-4359776578aaf94998b58f4c1918f63b5b4ab054%2Fuser-profile-leave-account.png?alt=media" alt="Account Settings page with Leave Account option in the menu" width="375"></div>


# My Profile

Manage your Mailtrap user profile settings, including email address, password, OAuth providers, and account access. Learn how to delete your profile or switch between accounts.

Mailtrap defines your user profile by your email address, and you can't use Mailtrap without the address.

To manage **User settings**, select your user name or email in the upper right corner and click My Profile. As a Mailtrap user, you can own or belong to multiple Mailtrap Accounts. When you sign up with Mailtrap, a free account is created for you automatically.

By default, the account name is either the owner's email address or name, if the latter was provided by OAuth.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-393b5091ec3f4015467e49bc5611ebbc300f77fe%2Fuser-my-profile-menu.png?alt=media" alt="Mailtrap user menu dropdown showing My Profile option and list of accounts" width="563"></div>

When you delete your user, all your data is deleted. Check your [rights to be forgotten](https://mailtrap.io/privacy/#39-Data-Retention).If you own account(s) and delete your user profile, all the account data, including projects, sandboxes, and team mate accesses will be deleted. This action is irreversible. If you need this data in the future, consider downgrading to the Free plan instead of terminating your subscription.If you don't own any account, deleting your user profile results in losing access to Mailtrap as well as all your user data, such as email, billing plan, account accesses, linked OAuth providers, etc.And within the **User settings** menu, you can see which account(s) you belong to and your level of access for each.

* **Owner** means you have the highest account access - can delete accounts, transfer ownership and manage team mates.
* **Admin** means that you have rights to fully manage all or some account entities (projects, sandboxes). You can, for example, delete them and provide access for team mates.
* **Viewer** access gives you read-only rights to some or all account entities. [See User Management](https://docs.mailtrap.io/documentation/account-and-organization/management/users) to learn more about permissions.

Clicking gear icon near the account name will bring you to the [Account settings](https://mailtrap.io/account-management). Depending your access level, you'll be able to rename or delete an account, transfer its ownership, or leave it.


# SSO Guide

Learn how to configure SAML 2.0 single sign-on (SSO) with Mailtrap using any Identity Provider that supports the SAML 2.0 protocol.

Need help setting up SSO with your specific Identity Provider? Check out our detailed step-by-step guides:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Azure (Microsoft Entra)</td><td><a href="sso/azure-microsoft-entra">azure-microsoft-entra</a></td></tr><tr><td>Okta</td><td><a href="sso/okta">okta</a></td></tr><tr><td>Google Workspace</td><td><a href="sso/google-workspace">google-workspace</a></td></tr><tr><td>OneLogin</td><td><a href="sso/onelogin">onelogin</a></td></tr><tr><td>JumpCloud</td><td><a href="sso/jumpcloud">jumpcloud</a></td></tr></tbody></table>

## Overview

You can use any Identity Provider that supports the [SAML 2.0](https://en.wikipedia.org/wiki/SAML_2.0) protocol in order to authenticate users via single sign-on (SSO) on Mailtrap.

Mailtrap automatically creates users using just-in-time provisioning when a user logs in with Mailtrap SSO.

{% hint style="info" %}
SSO is available only for users on Enterprise plans.
{% endhint %}

## How to enable SAML SSO in Mailtrap

{% hint style="warning" %}
Only the Account Owner has access to enable/disable SAML on an account.
{% endhint %}

To enable the SAML configuration for the Mailtrap account - go to **Settings** > **Account settings** > **SSO** to [open the SSO tab](https://mailtrap.io/account-management?current_tab=sso) and add/edit the SAML configuration.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-16187b8d9857c400894e97a6a9b15d2626968dfc%2Fsso-guide-1.png?alt=media" alt="SSO domains table showing active and pending domains with TXT record verification" width="563"><figcaption></figcaption></figure></div>

{% stepper %}
{% step %}
**Add and verify the domain**

* Enter your domain in the Domain field and click the **Add Domain** button.
* In the displayed table, you will find the record and its value generated by Mailtrap.
* Go to your domain settings page, select Manage DNS, and choose TXT from the list of options (for details, consult your domain provider documentation).
* Copy the authentication key generated by Mailtrap from the *Value* column and paste it to your TXT record.
* Once completed, get back to Mailtrap and click the **Verify** button for this domain. The status should change to *Active*.
  {% endstep %}

{% step %}
**Configure SSO**

* Choose whether you want to enforce SSO sign-in for users provisioned by SSO. When enabled, users whose sign-in is provisioned by SSO won't be able to sign in using any method except SSO.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-fdecc5bb8e4a475ca2bf111d0e5c4c458ad592e0%2Fsso-guide-2.png?alt=media" alt="SSO enforcement toggle enabled for designated SSO-active domains highlighted" width="563"><figcaption></figcaption></figure></div>

* Choose whether you want to create a separate free account for users provisioned by SSO. When enabled, new users won't get a separate account. When disabled, each new user will also get a separate account in addition to the one they get via SSO. Applies to newly provisioned users only.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-0f773a7788efdc374a28f8f3f669e9fb9e7b47bc%2Fsso-guide-3.png?alt=media" alt="Toggle enabled to prevent creating separate Free accounts for SSO users" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
**Mailtrap → Identity Provider**

**You'll need to provide the following to Mailtrap from your Identity Provider:**

* IdP Entity ID (Identity Provider Issuer)
* Single Sign-on URL
* Optional: Single Logout Service (SLO) URL
* X509 Certificate
  {% endstep %}

{% step %}
**Identity Provider → Mailtrap**

**You'll need to provide the following SAML Provider details to your Identity Provider from Mailtrap:**

* Entity ID
* Assertion Consumer Service URL
* Single Logout Service URL
  {% endstep %}

{% step %}
**Role mapping**

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-00239363872af2b0f84bd4fc1265f6ac84428b61%2Fsso-guide-4.png?alt=media" alt="SAML Role Mapping table with Admin and Viewer role attribute configurations" width="375"><figcaption></figcaption></figure></div>

By default, users created in Mailtrap via SSO have roles with empty permission, so users cannot View or Edit any projects or sandboxes. In this case, you can assign permissions manually within Mailtrap User Management.

To map your IdP roles to roles in Mailtrap, you need to create a mapping in the **SAML Role Mapping** section in Mailtrap.

In the example above, a user with the IdP attribute "MtRoleFromAppProfile" and the name "admin" (which should be configured as Attributes in the IdP) should be assigned the "Admin" role in Mailtrap.

You have the option to enforce IdP role mapping on every sign-in. That way, Mailtrap will fetch a new role from the IdP provider to check for any changes on its side. IdP provider **should sign out** of Mailtrap so that we can fetch the updated role attribute.
{% endstep %}
{% endstepper %}


# Azure (Microsoft Entra)

Step-by-step guide to configure SAML-based Single Sign-On between Azure Active Directory and Mailtrap with role mapping support.

## Overview

This guide walks you through configuring SAML-based Single Sign-On (SSO) between Azure Active Directory (Microsoft Entra) and Mailtrap.

## Configure Single Sign-On with Azure

### Create an Enterprise application

{% stepper %}
{% step %}
Open your Azure Active Directory and select **Enterprise applications**
{% endstep %}

{% step %}
Add a new application by clicking the **+ New application** button

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FH3G2frc29yvbNloKtJ25%2Fsetup-sso-with-azure-1.png?alt=media&#x26;token=f41b70e5-b9c8-4a39-b541-81ec7c3e379d" alt="" width="375"></div>
{% endstep %}

{% step %}
Choose **+ Create your own application**, enter the name of the application (e.g., "Mailtrap"), and select **Integrate any other application you don't find in the gallery (Non-gallery)**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F63Fk9Idem668CGJP7LF9%2Fsetup-sso-with-azure-2.png?alt=media&#x26;token=bec59cf3-792c-41b9-aead-ca9f68f837d8" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

### Set up Single Sign-On

After the application has been created, you can set up single sign-on:

{% stepper %}
{% step %}
Choose **Set up single sign-on** in the **Getting Started** section

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fn7ezSpWQAFiVooH0abOD%2Fsetup-sso-with-azure-3.png?alt=media&#x26;token=d010bd92-b632-419b-8ae9-7faa151598e1" alt=""></div>
{% endstep %}

{% step %}
For **Single Sign-on** mode, select **SAML** based Sign-on

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FDRKhjj2zaEpCamUQIec1%2Fsetup-sso-with-azure-4.png?alt=media&#x26;token=14c75c9f-b1ea-4776-b4b3-a2ed4bed814f" alt=""></div>

Follow the steps on the SSO with SAML screen. Azure AD has a detailed [configuration guide](https://docs.microsoft.com/en-gb/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications) at the top of the page for further guidance.
{% endstep %}
{% endstepper %}

### Basic SAML configuration

Click edit in the dropdown menu and provide the following SAML Provider details to your Azure from Mailtrap:

* **Entity ID** → Identifier (Entity ID)
* **Assertion Consumer Service URL** → Reply URL (Assertion Consumer Service URL)
* **Single Logout Service URL** → Logout URL

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FVQepfCpqQ5L8O54TQZxn%2Fsetup-sso-with-azure-5.png?alt=media&#x26;token=c040bf24-9287-4ddb-aff3-d3ae8f497c61" alt="" width="563"></div>

### User attributes and claims

In the User Identifier field, enter **user.mail**.

### SAML signing certificate

{% stepper %}
{% step %}
Click **Edit** and choose **SHA-1** Signing Algorithm
{% endstep %}

{% step %}
Click **Save**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F5jVKRNWKoDBB2VOh7BVV%2Fsetup-sso-with-azure-6.png?alt=media&#x26;token=dd80cb0e-88a0-4f37-946a-07215d7df161" alt="" width="375"></div>
{% endstep %}

{% step %}
Download **Certificate (Base64)**
{% endstep %}

{% step %}
Open it in any text editor and copy its content
{% endstep %}

{% step %}
Paste the certificate content into the Mailtrap **X509 Certificate** field
{% endstep %}
{% endstepper %}

### Identity provider details

Provide the following to Mailtrap from Azure:

* **IdP Entity ID** (Identity Provider Issuer) → Azure AD Identifier
* **Single Sign-on URL** → Login URL
* **Optional: Single Logout Service (SLO) URL** → Logout URL

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2F7wF0QDeFPl1R3HfOluc6%2Fsetup-sso-with-azure-7.png?alt=media&#x26;token=ac90eb0a-7388-4a67-83e5-4b885e29e19f" alt="" width="563"></div>

Now you can save your SAML configuration on Mailtrap.

### Assign Users and Groups

With SAML configuration complete, you need to add users or groups to your application in Azure:

{% stepper %}
{% step %}
Click **Users and groups** on the left sidebar
{% endstep %}

{% step %}
Click on **+ Add User → Users and Groups**
{% endstep %}

{% step %}
Select all users you want to add to the application and click **Select**
{% endstep %}
{% endstepper %}

## Permissions

By default, we create users with no permissions. If you want the user to be automatically assigned to Account Admin or Account Viewer role, you need to set up the role mapping.

### Configure role mapping in Mailtrap

In the following example, we assign the roles depending on the **title** attribute value:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FnDx75vBlNMFmXDKr90j6%2Fsetup-sso-with-azure-8.png?alt=media&#x26;token=819d1b85-4158-49a1-a079-ab3924ce00e3" alt="" width="375"></div>

### Configure attributes in Azure

{% stepper %}
{% step %}
Navigate to **Attributes & Claims**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FPaEERfQLfzIAVD3oGdB1%2Fsetup-sso-with-azure-9.png?alt=media&#x26;token=77e4da62-1edd-43a1-aa67-3cb6f8b631d4" alt="" width="563"></div>
{% endstep %}

{% step %}
Click **Add new claim**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzptgvMI50DVFQPq8M68R%2Fsetup-sso-with-azure-10.png?alt=media&#x26;token=e74db03a-749d-4dd2-b2af-abba0c8596c0" alt="" width="375"></div>
{% endstep %}

{% step %}
Add the **title** claim with the appropriate source attribute (e.g., **user.jobtitle**)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fg9GNFooHahMzkgiptgR8%2Fsetup-sso-with-azure-11.png?alt=media&#x26;token=14706ff6-a689-4b90-8de3-974a589337c4" alt="" width="375"></div>
{% endstep %}

{% step %}
Click **Save**
{% endstep %}
{% endstepper %}

Your Azure SSO configuration with role mapping is now complete.


# Okta

Learn how to configure Single Sign-On (SSO) integration between Okta and Mailtrap using SAML 2.0, including role mapping and debugging.

This guide walks you through setting up SSO integration between Okta and Mailtrap using SAML 2.0, including optional role mapping configuration.

## On Okta side

{% stepper %}
{% step %}
Navigate to **Applications** and click **Create App Integration**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FpUG3o3V9tmhTJOicwG94%2Fsetup-sso-with-okta-1.png?alt=media&#x26;token=55f0ee1d-3d7a-421d-a43f-6b44b45ebf88" alt="" width="375"></div>
{% endstep %}

{% step %}
Select the **Web Platform** and **SAML 2.0** as the Sign on method.
{% endstep %}

{% step %}
Enter app name and click on **Next**.
{% endstep %}

{% step %}
Provide the following **SAML Provider details** to Okta:

* **Entity ID** = Audience URI (SP Entity ID)
* **Assertion Consumer Service URL** = Single sign on URL
* **Name ID format** should be set to `EmailAddress`
* **Application username** should be set to `email`

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FWs9FsHc41F0sDyaInTmc%2Fsetup-sso-with-okta-2.png?alt=media&#x26;token=cb775362-20cd-431b-84c6-dc5ee23029c5" alt="" width="563"></div>
{% endstep %}

{% step %}
To apply role mapping please add used for mapping attribute in **Attribute Statements (optional)**
{% endstep %}

{% step %}
Click **Next** and **Finish**.
{% endstep %}
{% endstepper %}

## Mailtrap configuration

After configuration is ready on Okta side, next step would be to setup Mailtrap.

In Okta, you will see info that "**SAML 2.0** is not configured until you complete the setup instructions"

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FOISU6Lrc26EL3z95zM6x%2Fsetup-sso-with-okta-3.png?alt=media&#x26;token=b70147c7-11b2-4fa4-9a47-40e3a94baed2" alt="" width="375"></div>

{% stepper %}
{% step %}
Click **"View Setup Instructions"**

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FXRyU1eHhpNu6IpGrWKvf%2Fsetup-sso-with-okta-4.png?alt=media&#x26;token=b4c6a7c8-2590-43ea-a930-f320d842fd36" alt=""></div>
{% endstep %}

{% step %}
Provide the following to Mailtrap from Okta:

* **IdP Entity ID (Identity Provider Issuer)** = Identity Provider Issuer
* **Single Sign-on URL** = Identity Provider Single Sign-On URL
* **X509 Certificate** = X509 Certificate
  {% endstep %}

{% step %}
Click **Save** in Mailtrap SSO configuration.
{% endstep %}

{% step %}
For **Role mapping** there is additional configuration, please find more details in the SSO Guide Step 4: Role mapping section
{% endstep %}
{% endstepper %}

## SAML role mapping

There are different ways how you can configure your Okta to provide needed `attribute` to Mailtrap.

Mailtrap allows you to configure role attributes mapping (it's name and value). So you can configure will Mailtrap receive a role name from Okta or `true|false` as a value.

* **Example of receiving boolean values in Attribute value**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FE53BdL6K3wk2zNN6CS83%2Fsetup-sso-with-okta-5.png?alt=media&#x26;token=833880e3-0580-434b-84ef-1e64d27fa668" alt="" width="375"></div>

* **Example with Role name in Attribute value**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FQTpDGsAQkU9Wa5xvUKMD%2Fsetup-sso-with-okta-6.png?alt=media&#x26;token=7675846a-9677-47ea-908d-4c07953379f2" alt="" width="563"></div>

{% hint style="info" %}
There are several ways to do it in Okta. The best way is to consult with your team with help with configuration.
{% endhint %}

### Map Okta group names to Mailtrap permissions

{% stepper %}
{% step %}
Create groups in Okta:

* "MT Admin Group"
* "MT Viewer Group"

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FgtHvI9iVJzRsZ4CGw2gQ%2Fsetup-sso-with-okta-7.png?alt=media&#x26;token=ce0304f9-6b58-4057-88dd-30af34c97a27" alt="" width="375"></div>
{% endstep %}

{% step %}
Add users to groups
{% endstep %}

{% step %}
Update Okta application SAML attributes mapping

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FpKNAgp0yjI8enALZVuSg%2Fsetup-sso-with-okta-8.png?alt=media&#x26;token=bcf98023-0b9d-46f0-a7e7-8f359bd5c2dc" alt="" width="375"></div>
{% endstep %}

{% step %}
Update attribute statements to return new SAML attributes:

* `isMailtrapAdmin` with value `isMemberOfGroupName("MT Admin Group")`
* `isMailtrapViewer` with value `isMemberOfGroup("00ggiqham4LuYTBPL5d7")`
  * `isMemberOfGroup` accepts group id. Group id can be taken from URL when visiting group page
* More about Okta expressions language [here](https://developer.okta.com/docs/reference/okta-expression-language/)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FQqz08fE5W2FKgKwtanrg%2Fsetup-sso-with-okta-9.png?alt=media&#x26;token=2eb3f22c-a7ff-45cc-80a7-bb44ecdeff89" alt="" width="375"></div>
{% endstep %}

{% step %}
Add SAML attributes mapping in Mailtrap with same attribute names

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FFwXxBQpgNzDZlUV0Oaez%2Fsetup-sso-with-okta-10.png?alt=media&#x26;token=1b7c5798-0daa-464c-aad0-ca67603e4c6a" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

## Debugging Okta integration

You can use [SAML tracer](https://developer.okta.com/docs/guides/saml-tracer/main/) to debug your SAML integration with Mailtrap.

You need to see a proper Attribute Name and Attribute Value in SAML request from Okta and they should match the ones you specified in Mailtrap SSO settings.


# Google Workspace

Step-by-step guide to configure SAML-based Single Sign-On between Google Workspace and Mailtrap with role mapping support.

## Overview

This guide walks you through configuring SAML-based Single Sign-On (SSO) between Google Workspace and Mailtrap.

## On Google Admin side

### Access the Apps section

{% stepper %}
{% step %}
Go to **Apps** in the **Google Admin console**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fauq1VsOyQV3Ug1LF4Vhz%2Fsetup-sso-with-google-workspace-1.png?alt=media&#x26;token=d96fedd1-f20b-4c59-b417-57bd776e7de8" alt="" width="375"></div>
{% endstep %}

{% step %}
Navigate to **Web and mobile apps**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FXPMvdRKDZEImFwA7PQpS%2Fsetup-sso-with-google-workspace-2.png?alt=media&#x26;token=846d76b2-825d-4e20-9a97-9feafd69b126" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

### Create a custom SAML app

{% stepper %}
{% step %}
Navigate to the **Web and mobile apps** section in Google Admin.
{% endstep %}

{% step %}
Click the **Add app** dropdown button to see available app options.
{% endstep %}

{% step %}
Select **Add custom SAML app** from the dropdown menu.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzzIN5JEn9X0E3oS6ctq6%2Fsetup-sso-with-google-workspace-3.png?alt=media&#x26;token=25598f52-358d-49ad-9e8d-b025e401ba7b" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

### Copy Google identity provider details

Google will provide you with the following SAML configuration details. Copy these values to use in Mailtrap:

* **SSO URL**
* **Entity ID**
* **Certificate**

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FoQy4uqOExto7BOtIuLH1%2Fsetup-sso-with-google-workspace-4.png?alt=media&#x26;token=f85ce951-2254-48f2-a6be-6390581f1092" alt="" width="375"></div>

### Configure service provider details

Provide the following SAML Provider details to Google from Mailtrap:

* **ACS URL** → Assertion Consumer Service URL from Mailtrap
* **Entity ID** → Entity ID from Mailtrap

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FkJ79ZkYpni7xGFc7bom4%2Fsetup-sso-with-google-workspace-5.png?alt=media&#x26;token=6e158dbe-bdc7-4bfa-87a6-27e08ac9c957" alt="" width="375"></div>

### Verify the application

After configuration, your SAML app will appear in the Web and mobile apps list:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FRNxupZ9ou7WFS95Uw73a%2Fsetup-sso-with-google-workspace-6.png?alt=media&#x26;token=495b50ab-0b77-4010-9cc7-551729e79caa" alt="" width="563"></div>

### Review the configuration

You can review the service provider details and configure attribute mapping:

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FnCTFQHlFn2lb1kC2wJmm%2Fsetup-sso-with-google-workspace-7.png?alt=media&#x26;token=3acde508-db45-42c8-8169-42ada8625d22" alt="" width="563"></div>

### Enable the application

Turn on the SAML app for your users:

{% stepper %}
{% step %}
Go to the **Service Status** section for your SAML app.
{% endstep %}

{% step %}
Select **ON for everyone** to enable the app for all users, or choose specific organizational units if you want to limit access.
{% endstep %}

{% step %}
Click **Save** to apply the changes and enable the application.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FFbyTDddpi5GtLIe9JKrV%2Fsetup-sso-with-google-workspace-8.png?alt=media&#x26;token=0a69836b-a272-434c-ba8f-d0fbfb87b03e" alt="" width="563"></div>
{% endstep %}
{% endstepper %}

## Permissions

By default, we create users with no permissions. If you want the user to be automatically assigned to Account Admin or Account Viewer role, you need to set up the role mapping.

### Configure role mapping

In the following example, we assign the roles depending on the **Type** of employee attribute value.

#### Configure attribute mapping in Google

{% stepper %}
{% step %}
Click **SAML attribute mapping**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Ff219KSZQb0SKAItE3PC9%2Fsetup-sso-with-google-workspace-9.png?alt=media&#x26;token=76f8ec1e-5493-4e1e-8a5e-b2e575457b3e" alt="" width="375"></div>
{% endstep %}

{% step %}
Map the **Google Directory attribute** to the **App attribute**

* **Google Directory attributes**: Employee Details > Type
* **App attributes**: Type

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FiL3EU1uzeUM2bxrGbNP9%2Fsetup-sso-with-google-workspace-10.png?alt=media&#x26;token=63d88680-cf04-4b8a-83d6-28781bc6a6b3" alt="" width="563"></div>
{% endstep %}

{% step %}
Save your attribute mapping configuration.
{% endstep %}
{% endstepper %}

#### Set employee type in Google Directory

In the **Google Directory** user profile, set the **Type of employee** field (e.g., "Admin", "Viewer"):

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FalVfthPMIOyitxAoiLMk%2Fsetup-sso-with-google-workspace-11.png?alt=media&#x26;token=66b3237f-fa97-45db-85ea-51c5c022c9d3" alt="" width="375"></div>

#### Configure role mapping in Mailtrap

In Mailtrap SSO settings, map the **Type** attribute to the appropriate Mailtrap roles (Admin, Viewer)

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FzL9kQtTrxiPXcgwfigwZ%2Fsetup-sso-with-google-workspace-12.png?alt=media&#x26;token=6d55dcec-e1a0-4261-a3d5-268a85303875" alt="" width="563"></div>

Your Google Workspace SSO configuration with role mapping is now complete.




---

[Next Page](/llms-full.txt/1)

