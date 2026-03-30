# Source: https://docs.mailtrap.io/getting-started/email-api-smtp.md

# Email API/SMTP

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

Check our [Sending Domain Setup Guide](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) for detailed instructions on adding and verifying your domain.
{% endstep %}

{% step %}
**Integrate your application via Email API or SMTP**

**SMTP Integration**

To send emails via Mailtrap SMTP, follow the instructions [in this article](https://docs.mailtrap.io/email-api-smtp/setup/smtp-integration).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-b3f6c0e6edcf50132a4514612bbf3dfabfb59518%2Fgetting-started-smtp-integration-credentials.png?alt=media" alt="SMTP integration credentials and code samples" width="563"><figcaption></figcaption></figure></div>

**Email API Integration**

To send emails via Mailtrap Email API, follow the steps [in this article](https://docs.mailtrap.io/email-api-smtp/setup/api-integration).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-602b5f9aee3c5224140faf8c5f40b6ef0e609592%2Fgetting-started-api-integration-credentials.png?alt=media" alt="Email API integration credentials and code samples" width="563"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### What else you can do with Mailtrap Email API/SMTP

* [Set up Tracking Settings](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain#optional-tracking-settings-ffi49)
* [Set up Unsubscribe Settings](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain#unsubscribe-settings-ekyqh)
* [Set up Webhooks](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain#optional-webhooks-4hmes)
* [Set up Email Categories](https://docs.mailtrap.io/email-api-smtp/analytics/categories)
* [Add or import Suppressions](https://docs.mailtrap.io/email-api-smtp/deliverability/suppressions-list)
* [Create templates](https://github.com/mailtrap/mailtrap-docs/blob/main/documentation/email-api-smtp/email-templates.md)
