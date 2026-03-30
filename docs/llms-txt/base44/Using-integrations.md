# Source: https://docs.base44.com/Integrations/Using-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Integrations

> Connect your Base44 apps, workspaces, and account to external tools and services

## About integrations

Integrations connect Base44 to the rest of your stack so you can automate workflows, pull in data, and call external services without wiring every API call by hand.

You can integrate at 3 levels:

* **<u>App level</u>**<u>:</u> Integrations inside a single app:
  * **Built-in integrations** such as Invoke LLM and SendEmail.
  * **Connectors** for OAuth-based connections to tools like Notion, Slack, or Google Workspace.
  * **External API calls with backend functions** that use per-app Secrets and functions.
* **<u>Workspace level</u>**<u>:</u> Shared APIs managed once for the whole workspace:
  * **Custom OpenAPI integrations** based on OpenAPI specs that any app in the shared workspace can call securely.
* **<u>Account level</u>**<u>:</u> Connections that live on your Base44 account:
  * **MCP connections** that you configure once so the Base44 AI chat can use external tools while you build, without changing your app's deployed code.

***

## App level integrations

App-level integrations live inside a single app. They include built-in integrations, connectors, and backend-powered external APIs that you wire to that app only.

### Built-in integrations

Some integrations come preinstalled in Base44 and are available to use immediately. They do not require a paid plan, extra setup, or separate API keys. With these core integrations, you can add AI, messaging, file handling, and advanced logic to any app with no additional configuration.

**Base44 built-in integrations include:**

* **Invoke LLM:** Generate AI responses from the built-in language model using detailed prompts. Supports JSON schema outputs, file attachments for added context, image analysis, and web search for up-to-date information.
* **SendEmail:** Send emails to people in your Base44 app with customizable sender names and rich HTML content.

  <Note>
    SendEmail does not support sending to external mailing lists or adding file attachments.
  </Note>
* **UploadFile:** Let people upload files to your app. Use the returned file URL in other integrations or workflows.
* **GenerateImage:** Create images from detailed text prompts. Returns a URL to the generated image.
* **ExtractDataFromUploadedFile:** Pull structured data from uploaded files (CSV, PNG, JPG, JPEG, PDF) using JSON schemas. Useful for importing data in bulk.

<Tip>
  Learn more about [built-in integrations](/Integrations/built-in-integrations).
</Tip>

### Connectors

Connectors are OAuth-enabled integrations that let a specific app connect to supported tools. You ask the AI chat to connect a service, sign in, and approve the requested permissions. Your app can then read or write data in that tool based on what you allow.

<Warning>
  You need a [**Builder plan**](https://base44.com/pricing) or higher to use connectors in your app.
</Warning>

**Examples of what you can build with connectors:**

* Sync a Notion database to power a knowledge view in your app.
* Post updates to a Slack channel.
* Sync Salesforce or HubSpot records into an internal dashboard.
* Save files from your app to Google Drive.
* Block off time in Google Calendar when a new booking is made.
* Publish a LinkedIn post when a new blog post is published.
* Show TikTok profile stats and follower counts in a dashboard.

<Tip>
  [Learn more about connectors](/Integrations/Connectors).
</Tip>

### External API calls with backend functions

External integrations using backend functions let a specific app talk directly to third-party services like Stripe, Twilio, or Google APIs with per-app credentials. These calls are wired through your own backend functions and Secrets.

<Frame caption="Connecting an integration to your Base44 app using the AI chat">
  <img src="https://mintcdn.com/base44/dZ1qJi0krzKe0iew/images/resend.png?fit=max&auto=format&n=dZ1qJi0krzKe0iew&q=85&s=147297448e51613a3fd7b1117c24d753" alt="Connecting an integration to your app using the AI chat" className="mx-auto" width="1111" height="835" data-path="images/resend.png" />
</Frame>

**Use backend functions when:**

* You want a one-off integration for a single app.
* You need custom logic that is tightly coupled to that app.
* The service is not yet set up as a custom OpenAPI integration in your workspace.

**Examples of external integrations with backend functions:**

* Sending welcome emails to new people using your app via your email provider.
* Syncing your existing CRM with your app database.
* Alerting your team in Slack when someone submits a form.
* Generating content with AI tools using your own provider keys.
* Calling vendor-specific APIs that do not have a connector or custom OpenAPI integration yet.

<Warning>
  **Important:** You need a [**Builder plan**](https://base44.com/pricing) or higher to use backend functions.
</Warning>

When you request an integration in the AI chat, Base44 guides you step by step and asks for credentials or authorization when needed. It then connects the backend and frontend logic automatically so you can get up and running fast.

You store credentials as **Secrets** in the app dashboard and use them in TypeScript functions under **Dashboard → Code → Functions**.

<Tip>
  Each backend function has a code file you can edit, view, and test. You can also check logs for each function from **Dashboard → Code → Functions**.
</Tip>

***

## Workspace level integrations

Workspace-level integrations live in a shared workspace and can be reused across many apps without repeating setup or credentials.

### Custom OpenAPI integrations

Custom OpenAPI integrations let you register shared external APIs at the workspace level from an OpenAPI specification. You import a spec once, select the operations you want to expose, and any app in that shared workspace can call those operations through the SDK.

The AI builder and your frontend code can call custom OpenAPI integrations directly through `base44.integrations.custom` without exposing credentials. Calls are proxied through the Base44 backend, so secrets never reach the browser.

This is ideal for internal APIs and partner APIs that your team uses across many apps.

<Warning>
  **Important:**

  * Custom OpenAPI integrations are only available in **shared workspaces**.
  * Only **workspace owners and admins on a Builder plan or higher** can create or edit custom OpenAPI integrations.
  * Anyone in the shared workspace can use an existing custom OpenAPI integration in their apps, even on a free plan.
</Warning>

<Tip>
  Learn how to configure these APIs in detail in [**Managing custom OpenAPI integrations**](/documentation/integrations/managing-workspace-integrations).
</Tip>

***

## Account level connections

Account-level connections are configured once for your Base44 account and are available wherever you use the Base44 AI chat.

### MCP connections

MCP connections let you connect custom MCP servers to your Base44 account so the AI chat can use external tools and data as context while you build. This gives you a context-aware builder chat without changing your app's deployed runtime.

<Warning>
  **Important:**

  * MCP connections are available on the **Builder plan or higher.**
  * MCP servers are configured once per account under **Account Settings → MCP Connections**.
  * The AI chat only calls an MCP server when your prompt requires it (for example, when you mention that server or ask for data it provides). It does not contact every MCP server for every message.
</Warning>

**Examples of what you can do with MCP connections:**

* Ask the AI chat to search an internal docs MCP and summarize the most relevant pages for a feature.
* Connect a GitHub MCP server and ask for a summary of open issues in a specific repo.
* Connect an analytics MCP, such as Amplitude or a custom metrics service, and ask the chat to pull recent product metrics into the conversation while you plan changes.

<Tip>
  Learn how to add and manage MCP servers in [**Using MCP connections**](/documentation/integrations/mcp-connections).
</Tip>

***

## Getting your API keys

Some integrations require an API key, which acts like a private password between Base44 and the external service. Your API key proves ownership and keeps your connection secure. Base44 stores your key safely so your app can use it without exposing it.

<Warning>
  Never share your API key publicly. Treat it like a password.
</Warning>

**To get your API key:**

1. Log into the external service (for example, OpenAI, Resend, Notion).
2. Find the **Developer**, **API**, or **Integrations** section.
3. Click **Create API Key** or **Generate Token** and copy it.
4. Paste your API key in Base44:

   * **Using the AI chat:** Enter your API key in the AI chat when prompted.

     <Frame caption="Adding your API key in the AI chat in Base44">
       <img src="https://mintcdn.com/base44/_sloqzobDUv4viJs/images/chataiapi.png?fit=max&auto=format&n=_sloqzobDUv4viJs&q=85&s=c66214a04f7b320fc4c72d77963335ac" alt="Adding your API key in the AI chat in Base44" title="Adding your API key in the AI chat in Base44" className="mx-auto" style={{ width:"61%" }} width="1006" height="1234" data-path="images/chataiapi.png" />
     </Frame>
   * **Setting up manually:** Save your API key in **Secrets**.\
     a. Click **Dashboard** in your app's editor.\
     b. Click **Secrets**.\
     c. Click **Add Secret**.

   <Frame caption="Adding secrets in the app dashboard of Base44">
     <img src="https://mintcdn.com/base44/md0uEgmxEQCB9Nzh/images/apikeys.png?fit=max&auto=format&n=md0uEgmxEQCB9Nzh&q=85&s=38737506f2d314b714dcc48fbfea347c" alt="Adding secrets in the app dashboard of Base44" className="mx-auto" width="1270" height="727" data-path="images/apikeys.png" />
   </Frame>

Custom OpenAPI integrations also use secrets, but these are configured once by a workspace admin when creating or editing the integration and are stored as encrypted workspace secrets, not per-app Secrets.

***

## FAQs

Click a question below to learn more about using integrations.

<AccordionGroup>
  <Accordion title="What is the difference between custom OpenAPI integrations and per-app external APIs?">
    Custom OpenAPI integrations are configured once in a shared workspace from an OpenAPI spec and are available to every app in that workspace through `base44.integrations.custom.call()`. Credentials are stored as encrypted workspace secrets and never exposed to app code, and you do not need backend functions to use them.

    Per-app external APIs use backend functions and Secrets in a specific app. They are ideal for app-specific logic or when you do not want to share an API across all apps in a workspace.
  </Accordion>

  <Accordion title="How should I test my integration before I publish?">
    Before publishing your app, test your integration so you can catch issues early:

    1. Use sandbox or test mode (for example, Stripe test keys), if the provider offers it.
    2. Try real flows and edge cases, not just a single happy path.
    3. Check that inputs and outputs match your expectations in your UI and in the provider's dashboard.
    4. Monitor integration credit usage in both Base44 and the external service.
    5. Preview your app to catch slow loading, failed API calls, or missing data before going live.
  </Accordion>

  <Accordion title="Why is my integration not working?">
    If you run into issues, check the following:

    * The app owner has a Builder plan or higher (for per-app external APIs that use backend functions).
    * Your API key is correct and saved in Secrets or in the custom OpenAPI integration, if relevant.
    * You have enough active credits in the external service.
    * You are using live credentials, not test ones, when testing production flows.
    * Your API request includes the correct endpoint, payload, and parameters.
    * You have not hit the service's rate limits.
  </Accordion>

  <Accordion title="Who can use backend functions and per-app external APIs?">
    Backend functions and per-app external APIs are available automatically based on your plan and role.

    * The app owner must have a Builder plan or higher. If the app owner is on a Free or Starter plan, backend functions and integrations that depend on them are unavailable, even if the workspace owner has a Builder seat.
    * Workspace owners and admins with a Builder plan or higher can create backend functions in apps they own.
    * Admin collaborators on Starter plans can edit and create backend functions in an app as long as the app owner has a Builder plan or higher.
  </Accordion>

  <Accordion title="Why do I get 403 errors when using backend functions?">
    If you see a 403 error when using backend functions, it may mean backend functions are not available for your app or workspace, or the request is missing permissions.

    Common causes and fixes:

    * Plan requirement: Backend functions are only available when the app owner has a Builder plan or higher. If the app owner is on a Free or Starter plan, backend calls and per-app integrations that rely on them can fail with 403, even if the workspace owner has a Builder seat.
    * Permissions in your function: Your backend function may be rejecting the request because the person is not signed in or does not have the right role. Check any role or access checks you added in the function code.
    * External service permissions: A 403 can also come from the external API you are calling. Make sure the API key has the right scopes and that the request uses the correct endpoint and method.
    * Still having trouble: If none of these apply, see the [Troubleshooting Issues](https://docs.base44.com/Guides/Troubleshooting) article or contact Base44 support.
  </Accordion>

  <Accordion title="How do I regenerate or update my API key?">
    There are 2 types of API keys you may need to regenerate or update:

    * Third-party service keys: Regenerate your key in that service's developer portal, for example OpenAI, Resend, Notion, then update it in **Dashboard → Secrets** or in your custom OpenAPI integration settings.
    * Your Base44 account API key:
      1. Click your profile icon at the top right of your workspace.
      2. Select **Settings**.
      3. Click **Account**.
      4. Click **Regenerate** next to **API Key**.

    <Note>
      Once regenerated, your Base44 API key updates across all of your Base44 apps automatically. If you have added your Base44 key in another service, update it there as well.
    </Note>
  </Accordion>

  <Accordion title="What happens to my integrations if I downgrade my plan?">
    * Built-in integrations remain available.
    * Connectors, custom OpenAPI integrations, MCP connections, and per-app external APIs that rely on backend functions may stop working until you upgrade to a [**Builder plan**](https://base44.com/pricing) or higher.
  </Accordion>

  <Accordion title="Can I use multiple integrations in one app?">
    Yes. You can mix built-in integrations, connectors, custom OpenAPI integrations, and per-app external APIs in the same app, as long as your plan and settings support them.
  </Accordion>

  <Accordion title="Why can Base44 or the AI not fetch my API key for me?">
    For security reasons, external services like Stripe, OpenAI, or Notion do not let third parties, including Base44, access your credentials automatically. Instead, you need to:

    1. Log in to the service.
    2. Go to the API or developer section.
    3. Generate your key.
    4. Paste it into Base44 as a Secret or workspace header.

    Once added, your app or custom OpenAPI integration can use that key behind the scenes safely and without code.

    <Note>
      **Why this matters:** API keys act like passwords for services. Keeping them private and under your control keeps your data safe and ensures only you authorize access.
    </Note>
  </Accordion>

  <Accordion title="Do MCP connections work like other app integrations?">
    No. MCP connections are only for the Base44 AI chat while you build. They are configured at the account level under **Settings → MCP Connections** and are used only when your prompt requires that MCP server. Your deployed app does not call MCP servers through this settings page.
  </Accordion>
</AccordionGroup>

<Tip>
  Still need help? Join our [**Discord**](https://discord.com/invite/ThpYPZpVts) and get real-time support from the Base44 team and community.
</Tip>


Built with [Mintlify](https://mintlify.com).