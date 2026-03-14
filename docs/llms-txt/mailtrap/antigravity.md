# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/antigravity.md

# Antigravity

[Antigravity](https://antigravity.google/) is Google’s development platform powered by Gemini 3 that gives you an AI-powered IDE experience with autonomous agents that can plan, execute, and verify complex software tasks across your editor.&#x20;

In this guide, you’ll learn how to integrate it with the Mailtrap MCP which allows you to, amongst other things, perform the following actions:

* [Connect Mailtrap to your project](#integrating-mailtrap-into-your-project)
* [Fetch and preview Sandbox messages](#sandbox-operations-during-code-review)
* [Validate and edit email templates during code review](#template-validation-during-code-review)
* [Forward email templates to your teammates](#sending-emails-to-your-teammate)

#### Prerequisites

Before you start, make sure to:

* Set up your [sending domain](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain) (this takes approximately 5 minutes).
* Install the [latest Node.js version](https://nodejs.org/en) since [Mailtrap MCP](https://www.npmjs.com/package/mcp-mailtrap) is implemented as a Node.js command line utility.

### Step 1. Add Mailtrap MCP to Antigravity

Start by opening the Antigravity and clicking on **MCP Servers** from the three-dotted menu in the upper-right corner of the agent chatbox.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FYERHYwahd5HUAN1fbmM9%2Fantigravity%201.png?alt=media&#x26;token=138ed621-aa70-43df-88dc-7ab2ecb292c1" alt=""><figcaption></figcaption></figure>

Next, click on **Manage MCP Servers**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FixTc0zHQGMEnVDOcTbSR%2Fantigravity%202.png?alt=media&#x26;token=abca19a0-c2f4-48ed-b81f-ebe2aa6f2f3e" alt=""><figcaption></figcaption></figure>

Then, click on **View raw config**, which should open the **mcp\_config.json** file.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FqTrpSGORdx6IhcVCqruX%2Fantigravity%203.png?alt=media&#x26;token=264cef52-5575-4548-b838-fbf952d282d2" alt=""><figcaption></figcaption></figure>

In the **mcp\_config.json** file, simply copy/paste the following code snippet:

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

Next, all you need to do is replace the following values in the **mcp\_config.json** file:

* `MAILTRAP_API_TOKEN` – Required for all functionality, used to authenticate API requests, which you can copy/paste from the credentials tab.
* `DEFAULT_FROM_EMAIL` – Required for email sending. Make sure the email’s domain matches your own domain from the **Sending Domains** tab in Mailtrap.

You can find these credentials in your Mailtrap account by navigating to **Sending Domains** → **Integration** → **API**.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FjIbm84D7OycdNddRRQel%2FScreenshot%202026-03-10%20at%2017.06.42.png?alt=media&#x26;token=343a6113-a4ed-45b7-b02c-c542cbebf287" alt=""><figcaption></figcaption></figure>

* `MAILTRAP_ACCOUNT_ID` – This is required for template management purposes. You can find the account ID under **Settings** → **Account Settings**.&#x20;

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FkT8ht62sS2SUrbE3JKeJ%2FScreenshot%202026-03-10%20at%2017.07.13.png?alt=media&#x26;token=caf44e16-73da-4a07-b53b-80511cb842fd" alt=""><figcaption></figcaption></figure>

* `MAILTRAP_TEST_INBOX_ID` – If you need sandbox email functionality, you can find this ID in your Sandbox.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FcGKWBHgbgNZWdfWrdNXy%2FScreenshot%202026-03-10%20at%2017.07.34.png?alt=media&#x26;token=2d67031c-f620-4fae-972e-345b612f6625" alt=""><figcaption></figcaption></figure>

Once you insert your Mailtrap credentials and refresh the page or reopen Antigravity, you should see a list of available tools that come with Mailtrap MCP.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FpWrn3fL8EqzxNUXso67K%2Fantigravity%204.png?alt=media&#x26;token=4a331af7-e448-4dd4-be95-020f3c0ce4c7" alt=""><figcaption></figcaption></figure>

### Antigravity + Mailtrap MCP server possible use cases

#### Integrating Mailtrap into your project

To easily integrate Mailtrap into your project, you can simply prompt the Antigravity agent to do it in your stead with a prompt like this one:

> Integrate Mailtrap into my project, so that it can send emails through the Mailtrap email API. Additionally, safely store the Mailtrap credentials from the MCP configuration into an .env file

Antigravity agent will then go through the Mailtrap documentation, integrate the email API, and safely store your credentials in a **.env** file. Then, you can proceed to test the configuration. For instance, here’s our contact form email in our Gmail inbox we used as our `to` address:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FqUUFZQizV4sMJwmRlMJq%2FScreenshot%202026-03-10%20at%2017.11.27.png?alt=media&#x26;token=438b8f8d-f4e0-497f-8fe3-f1192de98478" alt=""><figcaption></figcaption></figure>

And here is the same email in the [Mailtrap Email Logs](https://docs.mailtrap.io/email-api-smtp/analytics/logs):

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F8cwEWyOz4wUuQfLPU06M%2FScreenshot%202026-03-10%20at%2015.07.11.png?alt=media&#x26;token=af7016f3-fc93-4e28-bf77-6cdb77c94353" alt=""><figcaption></figcaption></figure>

#### Sandbox operations during code review

If you’re reviewing code for sending emails or emails themselves in a staging environment using [Sandbox](https://mailtrap.io/email-sandbox/), you can trigger sending logic to better understand or verify behavior, test emails, etc.

With Antigravity connected to Mailtrap MCP, you can complete the following actions by prompting the agent:

* Verify what the code actually does without switching to the Mailtrap UI and back to the IDE
* Inspect basic message metadata
* Use the returned message ID to request full message details (content, headers, etc.), and more.

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FGU7nQkAKnt2H6hGRoMQh%2FScreenshot%202026-03-10%20at%2017.15.17.png?alt=media&#x26;token=e64fc962-28bd-4949-a2c8-4512aa69f802" alt=""><figcaption></figcaption></figure>

#### Template validation during debugging

Want to edit your templates without switching to the Mailtrap UI? You can prompt the Antigravity agent to list them, fetch a specific template ID, or even change the subject lines you don’t like:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2FQ3jQZNTphTD8BH7sAtWg%2FScreenshot%202026-03-10%20at%2017.15.35.png?alt=media&#x26;token=f64c473e-5055-48eb-b6eb-6d0ca3be29e6" alt=""><figcaption></figcaption></figure>

#### Sending emails to your teammate

Furthermore, you can forward the emails you’re working on in Sandbox (or actual templates) to your teammate’s addresses. For this, you can use a prompt like this one:

<figure><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2F6y8lKihXX7SB13G0pD8b%2FScreenshot%202026-03-10%20at%2017.15.50.png?alt=media&#x26;token=d679dfd5-a270-497f-b301-b740199471ca" alt=""><figcaption></figcaption></figure>
