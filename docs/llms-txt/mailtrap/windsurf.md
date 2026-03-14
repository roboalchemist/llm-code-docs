# Source: https://docs.mailtrap.io/guides/ai-powered-integrations/windsurf.md

# Windsurf

With the Windsurf Mailtrap integration, you can send emails directly from Windsurf using the Cascade AI assistant and simple prompts.

Mailtrap is an email-sending solution for developer and product teams focused on fast delivery and high inboxing rates for transactional and promo emails. It provides a highly customizable API and 24/7 technical support.

In this guide, you'll set up the integration and send emails in three steps.

## Prerequisites

Before you start, ensure the following:

* [Set up your sending domain](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/setup/sending-domain) — this takes approximately 5 minutes
* Install the [latest Node.js version](https://nodejs.org/en) since [Mailtrap MCP](https://www.npmjs.com/package/mcp-mailtrap) is implemented as a Node.js command line utility
* Install or update [Windsurf](https://windsurf.com/) to the latest version

{% stepper %}
{% step %}
**Add Mailtrap MCP to Windsurf**

To add the Mailtrap MCP server to Windsurf:

1. Open Windsurf
2. Navigate to **Settings → Windsurf Settings**

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-ca645abfa09dd67f4f12bfdd3e3c684c69f9d4fe%2Fsend-email-with-windsurf-1.png?alt=media" alt="" width="375"></div>

3. On the Windsurf Settings page, click the **Manage MCPs** button

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-494822240079109172f57c718b02f6369581a650%2Fsend-email-with-windsurf-2.png?alt=media" alt="" width="563"></div>

This will open the mcp.config.json file. Add the following code snippet:

{% code title="mcp.config.json" %}

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
{% endstep %}

{% step %}
**Add Mailtrap API credentials**

Replace the following values in your mcp.config.json file:

* **MAILTRAP\_API\_TOKEN** — Authentication token for API requests. You can copy this from the **Credentials** tab in your Mailtrap account
* **DEFAULT\_FROM\_EMAIL** — Must match your verified domain in Mailtrap's **Sending Domains** tab

Find these credentials in your Mailtrap account by navigating to **Sending Domains → Integration → API**.

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-8de9ffb85657c34cd6f547c02bc8205a2a72e67f%2Fmailtrap-api-credentials.png?alt=media" alt="" width="375"></div>

{% hint style="info" %}
Although you shouldn't face any issues, reload Windsurf to ensure everything is set up correctly.
{% endhint %}
{% endstep %}

{% step %}
**Send emails with a prompt**

To send an email:

1. Open the **Cascade** sidebar in the upper-right corner
2. Make sure the **Mailtrap MCP server** is enabled under **Customizations**

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-c0211f282486d1690e9f8b1690892d922acb72b6%2Fsend-email-with-windsurf-4.png?alt=media" alt="" width="563"></div>

3. Use this prompt (or create your own):

```
Send an email to john.doe@example.com with the subject 'Hi John!' and a message that wishes John a great day.
```

Cascade will process your request and confirm the email was sent:

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-ef86661e17b3e6b5db0d9b07628df65ec18020d6%2Fsend-email-with-windsurf-5.png?alt=media" alt="" width="375"></div>
{% endstep %}
{% endstepper %}

### Verify in Gmail

The email will arrive in your inbox:

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-267d27d3124601640a9dee4a7007e6f6eafcbbf8%2Fsend-email-with-windsurf-6.png?alt=media" alt="" width="375"></div>

### Check Mailtrap Email Logs

You can also verify the email in the [Email Logs](https://app.gitbook.com/s/S3xyr7ba7aGO19rc8dSK/email-api-smtp/analytics/logs) tab of your Mailtrap dashboard:

<div align="left" data-with-frame="true"><img src="https://365478608-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgkNigAKiqQtQub1GOdjY%2Fuploads%2Fgit-blob-bf2da38c82355102ecb0ba6bdcd62b0c29948c66%2Fsend-email-with-windsurf-7.png?alt=media" alt="" width="375"></div>
