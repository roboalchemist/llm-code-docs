# Source: https://docs.replit.com/replitai/integrations.md

# Agent integrations

> Agent supports numerous integrations enabled automatically when your prompt contains specific keywords.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

<Frame>
  <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=d98e494833cceffef3c48d9abcdf047f" alt="Agent logo with integration connections illustrated around it" data-og-width="1280" width="1280" data-og-height="720" height="720" data-path="images/replitai/agent-logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=6fb21064203dfefe200f04d8ae904240 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=a74edbd65ec1a9607ba8d4e63e4155ba 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=7729f87fe2b932eb7e988fd83aa5ea4c 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=b1e377a10e6c51a5d017a4b9d12c1d77 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=cfcb43143d10d7e6de1c69dd3196f86d 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/replitai/agent-logo.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=2246ca457c164c03119a596f2a48be47 2500w" />
</Frame>

Agent supports three types of integrations so you can go from idea to app, fast:

* Replit managed: Built-in integrations that work automatically. Create an app and your Agent can start using these right away.
* Connectors: First‑party integrations Replit supports. Sign in once, then build with them across your apps.
* External integrations: Trusted third‑party services you can build with. Ask Agent to set them up; you’ll provide API keys.

## Getting started

To use an integration, mention the service or functionality you need. For example:

<AiPrompt>
  Create a web app that uses Stripe to accept payments and Sendgrid to send confirmation emails
</AiPrompt>

Agent automatically detects these keywords and implements the necessary code and configuration.

## Replit managed integrations

These built-ins require no setup. Just ask Agent to use them.

<AccordionGroup>
  <Accordion title="Replit Database">
    A simple built-in database for storing app data quickly.
    <AiPrompt>Add Replit Database to my app</AiPrompt>
  </Accordion>

  <Accordion title="PostgreSQL">
    Managed PostgreSQL for relational data and SQL queries.
    <AiPrompt>Use PostgreSQL in my app for relational data</AiPrompt>
  </Accordion>

  <Accordion title="Replit App Storage">
    Built-in storage for app files and assets.
    <AiPrompt>Use Replit App Storage to save files</AiPrompt>
  </Accordion>

  <Accordion title="App Storage">
    Cloud-based storage for images, videos, and other files.
    <AiPrompt>Add App Storage to my app to store files</AiPrompt>
  </Accordion>

  <Accordion title="Replit Auth">
    Native authentication so people can sign in with Replit.
    <AiPrompt>Add Replit Auth to my app</AiPrompt>
  </Accordion>

  <Accordion title="Replit Domains">
    Configure and manage custom domains for your app.
    <AiPrompt>Set up a custom domain for my app</AiPrompt>
  </Accordion>
</AccordionGroup>

## Connectors

Connectors let Agent build with your real data. They are first‑party integrations supported by Replit. Sign in once on the Connectors page in your Workspace, then reuse those connections across apps.

### Available connectors

<AccordionGroup>
  <Accordion title="Spotify">
    Access and manage Spotify playlists and library from your apps.
    <AiPrompt>Build a dashboard to browse my playlists and save tracks</AiPrompt>
  </Accordion>

  <Accordion title="Asana">
    Read Asana tasks and project data from your workspace.
    <AiPrompt>Sync and display my Asana tasks by project</AiPrompt>
  </Accordion>

  <Accordion title="Box">
    Read and access your Box files and folders from your apps.
    <AiPrompt>Browse and download files from my Box account</AiPrompt>
  </Accordion>

  <Accordion title="Confluence">
    Read users and groups, write content to Confluence spaces.
    <AiPrompt>Create a Confluence page and list my spaces</AiPrompt>
  </Accordion>

  <Accordion title="Discord">
    Access Discord guild information and user profiles.
    <AiPrompt>Show my guilds and post a message to a channel</AiPrompt>
  </Accordion>

  <Accordion title="Dropbox">
    Read Dropbox files, content, and metadata from your apps.
    <AiPrompt>List Dropbox folders and preview recent files</AiPrompt>
  </Accordion>

  <Accordion title="GitHub">
    Access GitHub repositories, users, and organizations from your apps.
    <AiPrompt>List my repositories and open pull requests</AiPrompt>
  </Accordion>

  <Accordion title="Google Calendar">
    Read and write Google Calendar events and settings.
    <AiPrompt>Create events and show my weekly calendar</AiPrompt>
  </Accordion>

  <Accordion title="Google Docs">
    Create, read, and edit Google Docs from your apps.
    <AiPrompt>Create a Google Doc and update its content</AiPrompt>
  </Accordion>

  <Accordion title="Google Drive">
    Access and manage your Google Drive files and folders.
    <AiPrompt>Search my Drive and upload a file</AiPrompt>
  </Accordion>

  <Accordion title="Gmail">
    Send, receive, and manage Gmail messages from your apps.
    <AiPrompt>Read unread messages and send an email</AiPrompt>
  </Accordion>

  <Accordion title="Google Sheets">
    Read and write to Google Sheets from your apps.
    <AiPrompt>Append rows to a Google Sheet and read values</AiPrompt>
  </Accordion>

  <Accordion title="HubSpot">
    Read HubSpot CRM objects, contacts, and deals from your apps.
    <AiPrompt>List contacts and create a new deal</AiPrompt>
  </Accordion>

  <Accordion title="Jira">
    Read users and manage Jira work items and issues.
    <AiPrompt>Create a Jira issue and update its status</AiPrompt>
  </Accordion>

  <Accordion title="Linear">
    Create and manage Linear issues, comments, and schedules.
    <AiPrompt>Create a Linear issue and add a comment</AiPrompt>
  </Accordion>

  <Accordion title="Notion">
    Read and write to your Notion workspace and pages.
    <AiPrompt>Query a Notion database and create a page</AiPrompt>
  </Accordion>

  <Accordion title="OneDrive">
    Access and manage your OneDrive files and folders.
    <AiPrompt>List OneDrive files and upload a document</AiPrompt>
  </Accordion>

  <Accordion title="Outlook">
    Send, receive emails and manage Outlook calendar events.
    <AiPrompt>Read my inbox and schedule a meeting</AiPrompt>
  </Accordion>

  <Accordion title="Resend">
    Send transactional emails using Resend API from your apps.
    <AiPrompt>Send a transactional email via Resend</AiPrompt>
  </Accordion>

  <Accordion title="SendGrid">
    Send transactional emails using SendGrid API from your apps.
    <AiPrompt>Send a transactional email via SendGrid</AiPrompt>
  </Accordion>

  <Accordion title="Salesforce">
    Access Salesforce CRM data and perform operations via REST API.
    <AiPrompt>List Salesforce contacts and create opportunities</AiPrompt>
  </Accordion>

  <Accordion title="SharePoint">
    Read, write, and manage SharePoint sites and documents.
    <AiPrompt>List SharePoint sites and upload a document</AiPrompt>
  </Accordion>

  <Accordion title="Twilio">
    Send SMS messages and make voice calls using Twilio API.
    <AiPrompt>Send an SMS and log delivery status</AiPrompt>
  </Accordion>

  <Accordion title="YouTube">
    Upload, manage YouTube videos, channels, and access analytics.
    <AiPrompt>Upload a video and fetch channel analytics</AiPrompt>
  </Accordion>

  <Accordion title="Zendesk">
    Read and write access to Zendesk Ticket API for support workflows.
    <AiPrompt>Sync Zendesk tickets to Linear and update both when status changes</AiPrompt>
  </Accordion>
</AccordionGroup>

### Accessing Connectors

You can access Connectors from the sidebar in your Workspace:

1. Navigate to your Workspace
2. Select "Connectors" from the sidebar
3. Choose "Add new integration" to browse available connectors
4. Select "Connect" next to the service you want to integrate

<Frame>
  <img src="https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=44fc5899e21e5b11318ab41887ff86b5" alt="App connectors interface showing available integrations including GitHub, OneDrive, Outlook, Spotify, Linear, Dropbox, Monday.com, Google Docs, and YouTube with their connection status and manage options" data-og-width="3456" width="3456" data-og-height="1688" height="1688" data-path="images/replitai/connectors-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=280&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=a29a9a200192b7bb1d38c965c02ee2e7 280w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=560&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=c4439e6d64eb334e36788c4f4fe0b82d 560w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=840&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=b37a91a43d6f777067065c5205a78ac2 840w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=1100&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=14f7b62cbd8d547982041e5fc6664bd8 1100w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=1650&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=e81016cf278b65d14ec90d4d083947c6 1650w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-overview.png?w=2500&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=59c7ef34d36cbbc84b83d3449d333dc0 2500w" />
</Frame>

When you select Connect for a service, Replit redirects you to authenticate with that service and grant permissions for Replit to access your data:

<Frame>
  <img src="https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=16716e418094fdc09882d1e6e2d0103f" alt="OAuth authentication flow showing the Linear connection dialog with privacy and security information, explaining data usage and user control" data-og-width="1345" width="1345" data-og-height="1213" height="1213" data-path="images/replitai/connectors-oauth-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=280&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=bb6ecf98d2fd81153d03086ad03a972c 280w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=560&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=15048c0020083fda0099f28a1510df9c 560w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=840&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=228e6341e950c45b5e0d5d21066e0269 840w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=1100&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=d2b886cf0baaf0362482010d636001f3 1100w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=1650&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=301fe8dba8258a85a84546028c25e738 1650w, https://mintcdn.com/replit/azgaw651Z-a6J23V/images/replitai/connectors-oauth-flow.png?w=2500&fit=max&auto=format&n=azgaw651Z-a6J23V&q=85&s=ae488cc2cdfb5c9ed034f3750774f731 2500w" />
</Frame>

### Example prompts

* "Integrate with Outlook to create an email dashboard"
* "Build a GitHub repository manager using my connected GitHub account"
* "Create a Linear task tracker for my team"
* "Build a Notion-powered website using my connected Workspace"
* "Create a Monday.com project dashboard"

<Note>
  Connectors provide authenticated access to your external services, eliminating
  the need to manage API keys or authentication tokens manually.
</Note>

<Callout>
  Looking for organization-wide connectors? See
  <a href="/replitai/connectors-for-organizations">Connectors for Organizations</a>.
</Callout>

## External integrations

Trusted third‑party services. Ask Agent to set them up; you’ll provide API keys.

### AI providers

<AccordionGroup>
  <Accordion title="OpenAI">
    Access GPT models for text generation, analysis, and assistants.
    <AiPrompt>Create a web app that uses OpenAI to summarize text</AiPrompt>
  </Accordion>

  <Accordion title="Google AI (Gemini)">
    Use Gemini models for multimodal understanding and generation.
    <AiPrompt>Use Google Gemini to analyze and summarize documents</AiPrompt>
  </Accordion>

  <Accordion title="Anthropic (Claude)">
    Access Claude models for reasoning, writing, and coding.
    <AiPrompt>Create a web app that uses Anthropic to generate content</AiPrompt>
  </Accordion>

  <Accordion title="Perplexity">
    AI-powered search and answer generation with citations.
    <AiPrompt>Create a web app that uses Perplexity to answer questions</AiPrompt>
  </Accordion>

  <Accordion title="Mistral AI">
    Fast, efficient language models for NLP tasks.
    <AiPrompt>Use Mistral to extract key facts from text</AiPrompt>
  </Accordion>
</AccordionGroup>

### Business and automation

<AccordionGroup>
  <Accordion title="Workato">
    Trigger automation recipes and call APIs from your apps.
    <AiPrompt>Connect my app to a Workato recipe that syncs leads</AiPrompt>
  </Accordion>

  <Accordion title="Stripe">
    Process payments and manage subscriptions.
    <AiPrompt>Add Stripe to my app for payments</AiPrompt>

    <br />

    See the <a href="/replitai/stripe-payments">Stripe payments (Agent)</a> guide for end‑to‑end setup, testing, and go‑live steps.
  </Accordion>

  <Accordion title="HubSpot">
    Access CRM data and manage contacts.
    <AiPrompt>Connect my app to HubSpot to manage contacts</AiPrompt>
  </Accordion>
</AccordionGroup>

### Communication and community

<AccordionGroup>
  <Accordion title="Discord">
    Send messages and manage servers from your apps.
    <AiPrompt>Send a message to my Discord channel when a new signup happens</AiPrompt>
  </Accordion>
</AccordionGroup>
