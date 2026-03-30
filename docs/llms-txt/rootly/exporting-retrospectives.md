# Source: https://docs.rootly.com/collaborative-retrospectives/exporting-retrospectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Retrospectives

> Sync retrospective content to external documentation providers like Google Docs, Confluence, Notion, and more.

## Overview

Rootly can sync retrospective content to external documentation providers, allowing teams to use their preferred tools while benefiting from Rootly's incident management features.

### Supported Providers

Rootly supports the following external document providers:

* Google Docs
* Confluence
* Notion
* SharePoint
* Dropbox Paper
* Coda
* Quip
* Datadog

<Info>
  Each provider has its own authentication and configuration requirements. Contact your administrator if you need access to a specific provider.
</Info>

## Native Editor vs External Providers

### When to Use the Native Editor

The built-in collaborative editor is ideal when:

* Multiple team members need to edit simultaneously
* You want data blocks and variables that update automatically
* You prefer keeping incident data within Rootly
* You want to share a published retrospective with stakeholders outside of your organization

### When to Use External Providers

External providers work well when:

* Your organization standardizes on a specific documentation tool
* You need to share retrospectives with stakeholders outside Rootly
* You want documents accessible in your existing knowledge base
* Compliance or governance requires specific storage locations

### Using Both

Many teams combine approaches:

1. **Draft in Rootly:** Use the native editor for initial drafting and collaboration
2. **Export for distribution:** Sync to an external provider when ready to share broadly
3. **Link back:** The external document links back to the incident in Rootly

<Info>
  Exporting typically happens at specific points rather than in real-time.
</Info>

***

### What Gets Exported

When exporting to your external providers, Rootly processes your retrospective content to ensure compatibility.

### Content That Syncs

| Content Type         | How It's Handled                                     |
| :------------------- | :--------------------------------------------------- |
| **Rich text**        | Formatting preserved (bold, italic, headings, lists) |
| **Tables**           | Converted to provider-native table format            |
| **Data blocks**      | Rendered as static content at sync time              |
| **Liquid variables** | Resolved to actual values at sync time               |
| **Code blocks**      | Formatted appropriately for each provider            |
| **Links**            | Preserved as clickable hyperlinks                    |

### Incident Data Blocks in External Documents

If your retrospective document contains data blocks:

* **Timeline:** Rendered as a formatted table with event date, source, user, and description
* **Follow-ups:** Rendered as a list with title, priority, status, assignee, and due date

<Info>
  Data blocks become static content in external documents. They won't update automatically if the incident data changes after sync.
</Info>

### Provider-Specific Formatting

Rootly adjusts content formatting for each provider:

| Provider        | Special Handling                            |
| :-------------- | :------------------------------------------ |
| **Confluence**  | Inline code converted to Confluence macros  |
| **Google Docs** | Tables formatted with borders and styling   |
| **Notion**      | Content structured for Notion's block model |
| **Others**      | Standard HTML-to-provider conversion        |

***

## How to Export

The editor header provides two ways to share and export your retrospective: the **Share** dropdown and the **Export** dropdown (for external providers).

### Share Dropdown

Click **Share** in the editor header to access these options:

| Option                      | Description                                                                   |
| :-------------------------- | :---------------------------------------------------------------------------- |
| **Preview public document** | Opens the published retrospective in a new tab (only team members can access) |
| **Customize document**      | Opens document settings (gear icon next to Preview)                           |
| **Copy document URL**       | Copies the retrospective link to your clipboard                               |
| **Export document to PDF**  | Downloads the retrospective as a PDF file                                     |

### Exporting to External Providers

If your team has external integrations configured, you can click the **Export** button in the editor header to export to connected providers.

The dropdown shows each configured provider (Confluence, Google Docs, Notion, etc.) with:

* Provider name and icon
* Last export timestamp (if previously exported)
* **Export** button to sync the current content

Click **Export** next to a provider to push the current retrospective content to that external document. This updates the existing document if one was already created and overwrites its content.

<Info>
  If you have no external integrations configured, the you can click **Connect Integrations** in the dropdown configure one. You can contact your administrator to set up an integrations in **Configuration → Integrations**.
</Info>

### Managing Export Workflows

At the bottom of the View dropdown, click **Manage workflows** to configure where retrospectives are automatically created when incidents resolve.

Workflows can automatically create external documents when:

* An incident is resolved
* A retrospective is created
* A retrospective is published
* A workflow step is completed

<Info>
  Initial document creation happens via workflows. The Export button in the dropdown is for re-exporting updates to an existing document.
</Info>

### Working with Exported Documents

Once a retrospective is exported to an external provider:

* A link to the external document is stored on the incident
* The document lives in your external provider's system
* Edits in the external document do **not** sync back to Rootly

### Document Links

After exporting, you can reference external document URLs using Liquid variables:

* `{{ incident.confluence_page_url }}`
* `{{ incident.google_drive_url }}`
* `{{ incident.notion_page_url }}`
* `{{ incident.sharepoint_page_url }}`

### Keeping Documents Updated

If you make changes to the retrospective in Rootly after the initial export:

1. Open the **Export** dropdown in the editor header
2. Click the **Export document contents** button next to the provider you want to update
3. The external document will be updated with the current content

<Info>
  Export is one-way (Rootly → Provider). Changes made directly in the external document won't sync back to Rootly.
</Info>

***

### Best Practices

* **Set up workflows for initial creation:** Configure workflows to automatically create external documents when incidents resolve, so you don't have to manually export each time.
* **Use Export for updates:** After editing a retrospective, use the Export button to push changes to the external document.
* **Include data blocks before exporting:** Add Timeline and Follow-ups blocks before exporting so they're rendered in the external document.
* **Verify liquid variables have values:** Empty variables create gaps in the external document. Check that referenced fields exist for the incident.

## Frequently Asked Questions

<Accordion title="My export failed with an authentication error">
  The connection to the external provider may have expired. Re-authenticate the integration in **Configuration → Integrations** or contact your administrator.
</Accordion>

<Accordion title="Data blocks are empty.">
  Data blocks must have data to render. If the incident has no timeline events or follow-ups, the blocks may appear empty. Add data to the incident before exporting.
</Accordion>

<Accordion title="Liquid variables resolve to N/A">
  Ensure the incident has the expected data. Variables without values resolve to N/A. Check that referenced fields (Jira ticket, assigned roles, etc.) exist for this incident.
</Accordion>

<Accordion title="Changes in the external document aren't in Rootly">
  Export is one-way. Edits made directly in the external provider don't sync back to Rootly. Make edits in Rootly and re-export.
</Accordion>

<Accordion title="How do I update an already-exported document?">
  Open the Export dropdown and click Export next to the provider. This updates the existing external document with the current retrospective content.
</Accordion>

<Accordion title="Can I export to multiple providers?">
  Yes, if multiple workflows are configured. Click Export for each provider you want to sync to.
</Accordion>


Built with [Mintlify](https://mintlify.com).