# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/qodo.md

# Qodo

[Qodo](https://qodo.ai/) is an AI code review platform that gives engineering teams deep codebase context to move faster without sacrificing code quality. In this guide, you’ll learn how to integrate it with Mailtrap MCP.&#x20;

**Note**: You can use your AI agent to help you integrate Mailtrap or even migrate from another email service provider.

### Prerequisites

Before you start, make sure to:

* Set up your [sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) (this takes approximately 5 minutes).
* Install the [latest Node.js version](https://nodejs.org/en) since [Mailtrap MCP](https://www.npmjs.com/package/mcp-mailtrap) is implemented as a Node.js command line utility.
* Install or update the IDE you’re using for Qodo.ai to the latest version.

### Step 1. Add Mailtrap MCP to Qodo.ai

First, open Qodo.ai from your preferred IDE. This can be VS Code, JetBrains IDEs, etc. For the purposes of this guide, we’ll use VSC.

Next, click on the **Tools** button right above the Qodo AI chatbox.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgu4EPywdZC1we2emZtmI%2FScreenshot%202026-03-10%20at%2019.50.30.png?alt=media&#x26;token=29e7e007-c5db-404c-be06-ced4175eb747" alt=""><figcaption></figcaption></figure>

Then, click on + **Add new MCP**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRWmEoCGyDYPfIXlIlykC%2FScreenshot%202026-03-10%20at%2019.50.52.png?alt=media&#x26;token=41c1105c-0a6d-4ad9-b8f6-984a46841a35" alt=""><figcaption></figcaption></figure>

Once the following window appears after you click on **Add new MCP**, copy/paste the following code snippet:

```json
{
  "mcpServers": {
    "mailtrap": {
      "command": "npx",
      "args": ["-y", "mcp-mailtrap"],
      "env": {
        "MAILTRAP_API_TOKEN": "your_mailtrap_api_token",
        "DEFAULT_FROM_EMAIL": "your_sender@example.com",
        "MAILTRAP_ACCOUNT_ID": "your_account_id",
        "MAILTRAP_TEST_INBOX_ID": "your_test_inbox_id"
      }
    }
  }
}
```

### Step 2. Insert Mailtrap API credentials

Next, all you need to do is replace the following values in the **settings.json** file:

* `MAILTRAP_API_TOKEN` – Required for all functionality, used to authenticate API requests, which you can copy/paste from the credentials tab.
* `DEFAULT_FROM_EMAIL` – Required for email sending. Make sure the email’s domain matches your own domain from the **Sending Domains** tab in Mailtrap.

You can find these credentials in your Mailtrap account by navigating to **Sending Domains** → **Integration** → **API**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F7Ho5742LtZtvTx893SIf%2FScreenshot%202026-03-10%20at%2017.06.42.png?alt=media&#x26;token=ef93e684-0a61-45b4-827e-6e67ad458cad" alt=""><figcaption></figcaption></figure>

* `MAILTRAP_ACCOUNT_ID` – This is required for template management purposes. You can find the account ID under **Settings** → **Account Settings**.&#x20;

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FMmwdeUK83PYhsAtuQxXC%2FScreenshot%202026-03-10%20at%2017.07.13.png?alt=media&#x26;token=27ad6cd2-5282-449a-b824-dc1b691c6545" alt=""><figcaption></figcaption></figure>

* `MAILTRAP_TEST_INBOX_ID` – If you need sandbox email functionality, you can find this ID in your Sandbox.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FFt5jv4Tm0c2EYJ5bjO64%2FScreenshot%202026-03-10%20at%2017.07.34.png?alt=media&#x26;token=aed93c0c-72b2-4f58-b119-8c59e260f55b" alt=""><figcaption></figcaption></figure>

### Qodo.AI + Mailtrap MCP server possible use cases

#### Sandbox operations during code review

Imagine that you’re reviewing a part of the code responsible for sending emails and that you’re working in a staging environment using [Sandbox](https://mailtrap.io/email-sandbox/).

While reviewing your code, you want to trigger email-sending logic to better understand or verify behavior, test emails, etc.

This is possible from the Qodo agent, which lets you use simple prompts to, among other things:&#x20;

* Verify what the code actually does without switching to the Mailtrap UI and back to the IDE
* Inspect basic message metadata
* Use the returned message ID to request full message details (content, headers, etc.), and more.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FJ35thx7yclLOwnGVWeRb%2FScreenshot%202026-03-10%20at%2019.51.12.png?alt=media&#x26;token=586f9b33-447d-4d51-a3bc-6985920a9e25" alt=""><figcaption></figcaption></figure>

#### Template validation during code review

Let’s say that while reviewing code, you notice a Mailtrap template ID being used and you’re unsure whether it’s the correct template.

From the Qodo agent, you can request the list of available templates in the Mailtrap account.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FdJdqFG0FNy5MESXokjD9%2FScreenshot%202026-03-10%20at%2019.51.36.png?alt=media&#x26;token=c62f1264-20ed-4585-9969-c069859489c2" alt=""><figcaption></figcaption></figure>

This allows you to quickly confirm that the referenced template is correct, directly within the review flow.

Don’t like the subject line of your template? Tweak it with a simple prompt, just like so:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FKOotwtf9X4mjKFpCcEFa%2FScreenshot%202026-03-10%20at%2019.51.46.png?alt=media&#x26;token=47fb4b89-b4f2-4678-af31-94420212bb96" alt=""><figcaption></figcaption></figure>

#### Sending emails to your teammate

You’re working on designing an email or a template, and you want your teammate’s opinion.

For this, you can prompt Qodo something like this:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FRFKOruutROmYTyBzRhcW%2FScreenshot%202026-03-10%20at%2019.52.12.png?alt=media&#x26;token=e2613498-1918-4cbb-a293-fed445dc314b" alt=""><figcaption></figcaption></figure>

#### Migrating from another email service provider

If you’re migrating from another email service provider or just starting out with Mailtrap, you can ask the Qodo agent to update your credentials so you can start sending emails in no time.

Simply copy/paste the credentials or one of the ready-made code snippets into the chatbox and prompt the AI, like so:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FvsDXEqO0Hqtg30K3GBZO%2FScreenshot%202026-03-10%20at%2019.52.45.png?alt=media&#x26;token=02fe3496-e685-4ef4-9bc7-723b99a62f0a" alt=""><figcaption></figcaption></figure>
