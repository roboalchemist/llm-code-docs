# Source: https://docs.mailtrap.io/guides/integrations/replit.md

# Replit

[Replit](https://replit.com/) is a tool that lets you build and deploy software using AI without any coding whatsoever. In this article, you’ll learn how to connect it to Mailtrap and add email-sending functionality to your projects.

**Prerequisites**:&#x20;

* Add and [verify your email sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) since Mailtrap allows you to send emails only from a verified domain.
* Make sure your [API Token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens) has `admin` access level to that domain.

### Step 1. Add your Mailtrap credentials

The Mailtrap credentials you need to add to Replit include:

* `MAILTRAP_API_TOKEN` – This is the [Mailtrap API token](https://docs.mailtrap.io/email-api-smtp/setup/api-tokens), which you can create at any time from your account.
* `MAILTRAP_FROM_EMAIL` – This is the email address with the verified Mailtrap sending domain you’ve added after creating an account.

To add these, open your Replit project, click on **Tools & files**, and navigate to the **Secrets** tab. Then, click on **New Secret** and add your secrets, just like so:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F3scvSYjozTbMZKT4H3yg%2FScreenshot%202026-02-22%20at%2014.46.37.png?alt=media&#x26;token=74ca32d9-7db0-4e47-800b-67bca38d5990" alt=""><figcaption></figcaption></figure>

Next, prompt the AI to use the secrets you just added so it can start sending emails from your projects using the Mailtrap email API. For this, you can use a prompt like this one:

> Please use Mailtrap email API for sending emails from my project. I’ve added the following secrets: MAILTRAP\_FROM\_EMAIL and MAILTRAP\_TOKEN

The AI will then go over [Mailtrap Email API documentation](https://docs.mailtrap.io/developers), connect it to your project, and confirm once it’s done.

### Step 2. Start sending emails

Once you add your credentials, try sending an email from your project. If you followed everything thus far, you should receive the email in your inbox in a few seconds.

Here it is in a Gmail inbox I used as my `to` address:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FbZqYPaTuBZvGq0JJThLK%2Freplit%201.png?alt=media&#x26;token=8ecd1a34-8115-45d4-8096-77dd0eb1117e" alt=""><figcaption></figcaption></figure>

And here it is in the [Mailtrap Email Logs](https://docs.mailtrap.io/email-api-smtp/analytics/logs):

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FHBqrIi6Ts7XWK0d6E4H5%2Freplit%202.png?alt=media&#x26;token=daf5fb68-dc8c-4c17-84b0-fc0ea4440e80" alt=""><figcaption></figcaption></figure>

### Next steps

* Use [Mailtrap Templates](https://docs.mailtrap.io/email-marketing/campaigns/email-templates) to send branded emails with variables.
* Configure [Mailtrap Contacts](https://mailtrap.io/mailtrap-contacts/) to push user information to your Mailtrap Lists, so you can later send campaigns to them or use Automations.
* [Add automation triggers](https://docs.mailtrap.io/email-marketing/automations) in Mailtrap to send follow-ups to new contacts.
* Track open and click rates with [Mailtrap Analytics](https://mailtrap.io/actionable-analytics/).
