# Source: https://docs.mailtrap.io/email-api-smtp/setup/smtp-integration.md

# SMTP Integration

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
