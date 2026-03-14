# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/bolt-new.md

# Bolt.new

[Bolt.new](https://bolt.new/) is an AI-powered builder that lets you generate and scale high-performing websites and apps using prompts. In this article, you’ll learn how to connect it to Mailtrap and add email-sending functionality to your projects.

**Before we start**:

* Add and [verify your email sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) since Mailtrap allows you to send emails only from a verified domain.
* Make sure your [API Token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens) has `admin` access level to that domain.

### Step 1. Add your Mailtrap credentials

Open your Bolt.new project and add your:

* `MAILTRAP_FROM_EMAIL` – This is the email address with the verified Mailtrap sending domain you’ve added after creating an account.
* `MAILTRAP_API_TOKEN` – This is the [Mailtrap API token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens), which you can create at any time from your account.

To do this, click on **More Options** (usually located above your project) and then on **Secrets**, and add the following two values:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FsIBC538FQnCJ8xqdBIFs%2Fbolt%201.png?alt=media&#x26;token=a0a13ebc-9970-4034-bf77-444c9be90741" alt=""><figcaption></figcaption></figure>

Next, prompt the AI to use the secrets you just added so it can start sending emails from your projects using the Mailtrap email API. For this, you can use a prompt like this one:

> Please use Mailtrap email API for sending emails from my project. I’ve added the following secrets: MAILTRAP\_FROM\_EMAIL and MAILTRAP\_API\_TOKEN

The AI will then go over [Mailtrap Email API documentation](https://docs.mailtrap.io/developers), connect it to your project, and confirm once it’s done.

### Step 2. Start sending emails

Once you add your credentials, try sending an email from your project. If you followed everything thus far, you should receive the email in your inbox in a few seconds.

Here is the email in a Gmail inbox I used as my `to` address:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRJt4iXPLy2ZpGWLzCYwu%2Fbolt%202.png?alt=media&#x26;token=c2b01a28-4a69-42dc-91f2-9b8b7865d76e" alt=""><figcaption></figcaption></figure>

And here it is in the [Mailtrap Email Logs](https://docs.mailtrap.io/email-api-smtp/analytics/logs):

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FACxTAvqkvBibm4U8Cu1m%2Fbolt%20.png?alt=media&#x26;token=c37c16a0-c104-43bb-8f1b-0fd88d5e58bb" alt=""><figcaption></figcaption></figure>

### Next steps

* Use [Mailtrap Templates](https://docs.mailtrap.io/email-marketing/campaigns/email-templates) to send branded emails with variables.
* Configure [Mailtrap Contacts](https://mailtrap.io/mailtrap-contacts/) to push user information to your Mailtrap Lists, so you can later send campaigns to them or use Automations.
* [Add automation triggers](https://docs.mailtrap.io/email-marketing/automations) in Mailtrap to send follow-ups to new contacts.
* Track open and click rates with [Mailtrap Analytics](https://mailtrap.io/actionable-analytics/).
