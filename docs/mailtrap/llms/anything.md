# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/anything.md

# Anything

[Anything](https://www.createanything.com/) is an AI agent that can turn your ideas into sites, apps, tools, products, and more with simple prompts. In this article, you’ll learn how to connect it to Mailtrap and add email-sending functionality to your projects.

**Prerequisites**:&#x20;

* Add and [verify your email sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) since Mailtrap allows you to send emails only from a verified domain.
* Make sure your [API Token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens) has admin access level to that domain.

### Step 1. Add your Mailtrap credentials

To add your Mailtrap credentials, open **Project Settings** in the sidebar, navigate to **Secrets**, and click on the **Add new secret** button.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FIhDyx8OYJ2Qi4kOB4qKH%2Fany%201.png?alt=media&#x26;token=f374fd66-ec52-4e81-b137-c7b75267efb2" alt=""><figcaption></figcaption></figure>

This way, you need to add the following two secrets:

* `MAILTRAP_API_TOKEN`&#x20;

This is the [Mailtrap API token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens), which you can create at any time from your account. And here’s what the secret should look like:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FnEEzQNq7etU6b8oJ4Ly4%2Fany%202.png?alt=media&#x26;token=e91f641c-342e-418e-ab8d-93fa158125fa" alt=""><figcaption></figcaption></figure>

* `MAILTRAP_FROM_EMAIL`&#x20;

This is the email address with the verified Mailtrap sending domain you’ve added after creating an account. And here’s the secret:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FUQAmyiSrO9M3eVdbBN8m%2Fany%203.png?alt=media&#x26;token=7af44c2d-4d07-4ff8-a1e5-8318bcb47bde" alt=""><figcaption></figcaption></figure>

Once you’re done adding the secrets, simply tell the Anything AI that you’re done with a prompt like this one, for example:

> Please use Mailtrap email API for sending emails from my project, I've added the MAILTRAP\_API\_TOKEN and MAILTRAP\_FROM\_EMAIL secrets

The AI will then go over [Mailtrap Email API documentation](https://docs.mailtrap.io/developers), connect it to your project, and confirm once it’s done.

### Step 2. Start sending emails

Once you add your credentials, try sending an email from your project. If you followed everything thus far, you should receive the email in your inbox in a few seconds.

Here it is in a Gmail inbox I used as my `to` address:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FfPRBSZqYQ0t0wD9Dn8Ep%2Fany%204.png?alt=media&#x26;token=bf8700b5-bace-4916-aeaa-1cd73d8667ce" alt=""><figcaption></figcaption></figure>

And here it is in the [Mailtrap Email Logs](https://docs.mailtrap.io/email-api-smtp/analytics/logs):

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FIcV7VY9WkQeG1DSWu3l3%2Fany%205.png?alt=media&#x26;token=e2856fe6-c65d-4338-b35f-9fbc360cbff6" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you plan on collecting email addresses for a list, you can connect your Anything project with [Mailtrap Contacts](https://mailtrap.io/mailtrap-contacts/) and store your addresses in your Mailtrap account automatically. For reference, check out the official [Mailtrap Contacts API documentation](https://docs.mailtrap.io/developers/promotional/contacts).
{% endhint %}

### Next steps

* Use [Mailtrap Templates](https://docs.mailtrap.io/email-marketing/campaigns/email-templates) to send branded emails with variables.
* Configure [Mailtrap Contacts](https://mailtrap.io/mailtrap-contacts/) to push user information to your Mailtrap Lists, so you can later send campaigns to them or use Automations.
* [Add automation triggers](https://docs.mailtrap.io/email-marketing/automations) in Mailtrap to send follow-ups to new contacts.
* Track open and click rates with [Mailtrap Analytics](https://mailtrap.io/actionable-analytics/).
