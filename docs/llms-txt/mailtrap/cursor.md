# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/cursor.md

# Cursor

Mailtrap is an email-sending solution for developer and product teams. Focused on fast delivery and high inboxing rates for transactional and promo emails. Provides highly customizable API and 24/7 tech support.

## Overview

With the Cursor and Mailtrap integration, you can now send emails from Cursor using Model Context Protocol. In this guide, you'll learn how to set it all up and start sending emails in three steps.

### Prerequisites

* If you haven't set up your sending domain already, you'll need to do it before we start—it takes \~5 minutes, and you can use our [step-by-step article](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/sending-domain) as a guide.
* Install the [latest Node.js version](https://nodejs.org/en) since [Mailtrap MCP](https://www.npmjs.com/package/mcp-mailtrap) is implemented as a Node.js command line utility.
* If you haven't already done so, install the [Cursor app](https://cursor.com/). But if you have, make sure it's updated and uses the latest version.

{% stepper %}
{% step %}
**Add Mailtrap MCP to Cursor**

To add Mailtrap MCP to Cursor, you can use the [quick install link](https://cursor.com/en/install-mcp?name=mailtrap\&config=eyJjb21tYW5kIjoibnB4IC15IG1jcC1tYWlsdHJhcCIsImVudiI6eyJNQUlMVFJBUF9BUElfVE9LRU4iOiJ5b3VyX21haWx0cmFwX2FwaV90b2tlbiIsIkRFRkFVTFRfRlJPTV9FTUFJTCI6InlvdXJfc2VuZGVyQGV4YW1wbGUuY29tIiwiTUFJTFRSQVBfQUNDT1VOVF9JRCI6InlvdXJfYWNjb3VudF9pZCJ9fQ%3D%3D) or in your Cursor editor, navigate to Settings → Cursor Settings.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-77f97946349ee5c84088076493cb6162c8e4d55b%2Fsend-email-with-cursor-1.png?alt=media" alt="Cursor application menu showing Settings option and Profiles menu" width="375"></div>

Go to the MCP tab and click on Add new global MCP server.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-460c9b145a4f35557cffb9e2ca9d4c2c771ef4b5%2Fsend-email-with-cursor-2.png?alt=media" alt="Cursor Settings window displaying MCP Servers section with Add new global MCP server button" width="563"></div>

The Add new global MCP server should open a new mcp.json config file, where we'll store the Mailtrap MCP configuration.

Tip: You can also open the mcp.json file in the following locations:

* MacOS: \~/.cursor/mcp.json
* Windows: %USERPROFILE%.cursor\mcp.json

Once you open the mcp.json file, copy/paste the following configuration inside it:

{% code title="mcp.json" %}

```json
{
  "mcpServers": {
    "mailtrap": {
      "command": "npx",
      "args": ["-y", "mcp-mailtrap"],
      "env": {
        "MAILTRAP_API_TOKEN": "your_mailtrap_api_token",
        "DEFAULT_FROM_EMAIL": "your_sender@example.com"
      }
    }
  }
}
```

{% endcode %}

Note: In case you're using asdf to manage Node.js, you must use an absolute path to the executable. Here's an example for Mac:

{% code title="mcp.json with asdf" %}

```json
{
  "mcpServers": {
    "mailtrap": {
      "command": "/Users/<username>/.asdf/shims/npx",
      "args": ["-y", "mcp-mailtrap"],
      "env": {
        "PATH": "/Users/<username>/.asdf/shims:/usr/bin:/bin",
        "ASDF_DIR": "/opt/homebrew/opt/asdf/libexec",
        "ASDF_DATA_DIR": "/Users/<username>/.asdf",
        "ASDF_NODEJS_VERSION": "20.6.1",
        "MAILTRAP_API_TOKEN": "your_mailtrap_api_token",
        "DEFAULT_FROM_EMAIL": "your_sender@example.com"
      }
    }
  }
}
```

{% endcode %}
{% endstep %}

{% step %}
**Add Mailtrap API credentials**

Open your Mailtrap account and navigate to Sending Domains → Integration → API.

Once in the Integration/API page, update the following values in your mcp.json file with Mailtrap credentials:

* **MAILTRAP\_API\_TOKEN** – Used to authenticate API requests, which you can copy/paste from the credentials tab.
* **DEFAULT\_FROM\_EMAIL** – Make sure the email's domain matches your own domain from the Sending Domains tab in Mailtrap.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-8de9ffb85657c34cd6f547c02bc8205a2a72e67f%2Fmailtrap-api-credentials.png?alt=media" alt="Mailtrap account Integration tab showing sending domain name and API token" width="375"></div>

For example, here's what your mcp.json file should ultimately look like:

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-70c12436ead65208cd4a1d52cc5a31f64cc670da%2Fsend-email-with-cursor-4.png?alt=media" alt="" width="375"></div>

And that's it! Hit save, reload, and you can start sending emails via Cursor with simple prompts.
{% endstep %}

{% step %}
**Send emails with a prompt**

First, toggle the AI Pane, located in the upper-right corner of the Cursor editor.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-db67937c8548333b2ca8822f584d4f0636d71b3f%2Fsend-email-with-cursor-5.png?alt=media" alt="" width="359"></div>

In the opened pane, make sure that the Agent mode is configured since it allows Cursor to perform actions for us.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-04a27c724d4a1be4326d38e6a1191bab37ec3b76%2Fsend-email-with-cursor-6.png?alt=media" alt="" width="375"></div>

To send a plain-text email, you can use a prompt like this one (although we encourage you to use your own prompts and experiment with them since the possibilities are endless):

Send an email to <john.doe@example.com> with the subject 'Hi John!' and a message that wishes John a great day.

Cursor will then identify the Mailtrap MCP server for your request, suggest running the right tool, in this case, send\_email, and generate the email with all the parameters and values for you. As soon as you're ready to send, click Run tool.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-93d748b0224e19321ee0d9ba3675671e73c9c8de%2Fsend-email-with-cursor-7.png?alt=media" alt="" width="375"></div>

Lastly, Cursor AI will notify you when it successfully delivers the email.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-994808bb6032cacd15e8811cbe753cf0af388078%2Fsend-email-with-cursor-8.png?alt=media" alt="" width="375"></div>

And here is the generated message in the Mailtrap [Email Logs](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/analytics/logs).

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-022d19b13a2edbea0aa286509416fb7bf4f36076%2Fsend-email-with-cursor-9.png?alt=media" alt="Mailtrap Email Logs dashboard showing delivered email with Hi John subject and metadata" width="563"></div>
{% endstep %}
{% endstepper %}

## Next steps

You can now use Cursor to compose and send various types of emails by adjusting your prompts. Experiment with different email templates, formatting options, and automation scenarios to maximize your productivity.
