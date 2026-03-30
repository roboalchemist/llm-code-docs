# Source: https://docs.base44.com/developers/changelog.md

# Source: https://docs.base44.com/Getting-started/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Base44 changelog

> Stay up to date with the latest Base44 features

See what is new in Base44, from AI upgrades to workspace tools and integrations. Check back often to discover updates that can make your next app easier and faster to ship.

To get involved with the community and hear more about new updates as they land, join our [Discord](https://discord.com/invite/ThpYPZpVts).

<Update label="March 9, 2026" tags={["Account & workspace", "Security & access"]}>
  ### Move apps between workspaces

  App owners can now move apps between workspaces instead of recreating them from scratch.

  * You must be the app owner and a member of the target workspace to move an app.
  * Workspace owners control who can move apps between workspaces from **Workspace settings → App configuration → App transfers**.

  Doc: [Managing your workspace apps](https://docs.base44.com/documentation/using-your-workspaces/managing-your-workspace-apps)
</Update>

<Update label="March 8, 2026" tags={["AI", "AI chat"]}>
  ### New model: ChatGPT 5.4

  ChatGPT 5.4 is now available as an AI model option in Base44.

  * Use it for prompts and agents that benefit from stronger reasoning and more natural responses.
  * Combine it with per-agent model selection to match the model to each app or workflow.

  Doc: [AI chat modes](https://docs.base44.com/Building-your-app/AI-chat-modes)
</Update>

<Update label="March 8, 2026" tags={["AI", "Integrations"]}>
  ### Choose models for built-in integrations

  The built-in **invokeLLM** integration now lets you choose which AI model runs LLM calls in your app.

  * Ask the AI chat to switch invokeLLM to any supported model in your workspace for a given app.
  * Agents and flows that use invokeLLM automatically start using the new model, so you can balance reasoning quality and cost.

  Doc: [Built-in integrations](https://docs.base44.com/Integrations/built-in-integrations#choosing-the-model-for-invokellm)
</Update>

<Update label="March 8, 2026" tags={["Mobile", "App stores"]}>
  ### Add Google Play SHA keys for your mobile app

  * You can now add your Google Play SHA keys when configuring your mobile app so Google Play can verify your builds.
  * This makes it easier to connect your Base44 app to Android features that rely on SHA-based verification.

  Doc: [Uploading to app stores](https://docs.base44.com/documentation/building-your-app/uploading-to-app-stores)
</Update>

<Update label="March 8, 2026" tags={["Connectors"]}>
  ### New connectors: ClickUp, Wrike, Google Analytics, Box, Dropbox, Microsoft Outlook, Linear

  Seven new OAuth connectors are now available in the connector catalog.

  * **ClickUp**, **Wrike**, **Google Analytics**, **Box**, **Dropbox**, **Microsoft Outlook**, and **Linear** each add a dedicated connector so you can sync tasks, analytics, files, email, and issues with your apps.
  * Each connector includes documented scopes, connection steps, and example use cases.

  Doc: [Connectors overview](https://docs.base44.com/Integrations/Connectors)
</Update>

<Update label="March 4, 2026" tags={["Connectors"]}>
  ### New: GitHub connector

  A dedicated **GitHub** connector has been added to the connector catalog.

  * Connect to repositories and automate actions such as creating issues or reading pull requests.
  * Use GitHub data inside your own dashboards or internal tools without managing GitHub API calls manually.

  Doc: [GitHub connector](https://docs.base44.com/Integrations/github-connector)
</Update>

<Update label="March 2, 2026" tags={["Security & access", "Account & workspace"]}>
  ### Review app access requests from in-app notifications

  Private apps are now easier to manage.

  * When someone requests access to a private app, you receive an in-app notification.
  * Click **Review** to see who is asking and approve or deny the request from the same place.

  Doc: [Managing access](/Setting-up-your-app/Managing-access)
</Update>

<Update label="March 2, 2026" tags={["Connectors"]}>
  ### New: Slack Bot connector

  The Slack connector now supports a **bot** option in addition to personal connections.

  * Choose a **Slack Bot** connector that uses a bot token instead of a personal token.
  * Post messages as a custom bot with its own display name and icon, keeping automations separate from personal accounts.

  Doc: [Slack connector](https://docs.base44.com/Integrations/slack-connector)
</Update>

<Update label="March 2, 2026" tags={["AI"]}>
  ### Choose the AI model for each agent

  You can now set the AI model that powers each app agent.

  * Pick a fast model for routing or a higher quality model for complex help.
  * Pricing for agents is now based on the selected model and token usage.

  Doc: [AI agent model](https://docs.base44.com/Building-your-app/AI-agents-for-apps#guidelines-and-ai-model)
</Update>

<Update label="March 2, 2026" tags={["AI", "AI chat", "Account & workspace"]}>
  ### Teach the AI how you work with skills

  A new **Skills** section in your account settings lets you define reusable instructions for the AI.

  * Add skills that describe your brand voice, coding style, workflows, or internal rules.
  * The AI uses these skills as shared context wherever it appears.

  Doc: [Adding workspace skills](https://docs.base44.com/documentation/using-your-workspaces/adding-workspace-skills)
</Update>

<Update label="February 26, 2026" tags={["Developer tools", "Integrations"]}>
  ### Backend functions are always available

  Backend functions are now available by default for apps that support them.

  * You no longer need to enable a toggle before calling external APIs or writing server-side logic.
</Update>

<Update label="February 24, 2026" tags={["Connectors"]}>
  ### New: Discord connector

  A **Discord** connector is now available.

  * Connect to a Discord server and send messages to channels from your Base44 apps.
  * Use it to power announcement bots, alerts, and workflow notifications.

  Doc: [Connectors overview](https://docs.base44.com/Integrations/Connectors)
</Update>

<Update label="February 24, 2026" tags={["Security & access", "Account & workspace"]}>
  ### Stronger account security with two factor authentication

  You can now protect your Base44 account with two factor authentication (2FA).

  * Turn on 2FA in your account settings and choose SMS, an authenticator app, or both.

  Doc: [Managing your account](https://docs.base44.com/documentation/account-and-billing/managing-your-account)
</Update>

<Update label="February 23, 2026" tags={["Account & workspace"]}>
  ### New Manage app menu on the Apps page

  The Apps page now includes a **Manage app** menu on every app card and row.

  * Use the three-dot menu to view, share, rename, clone, open settings, or delete an app from one place.
</Update>

<Update label="February 23, 2026" tags={["Analytics"]}>
  ### New sales overview in analytics

  Analytics now includes a dedicated **Sales overview** tab.

  * Track revenue, orders, and performance trends in one place.

  Doc: [App analytics](https://docs.base44.com/documentation/performance-and-seo/app-analytics)
</Update>

<Update label="February 18, 2026" tags={["AI", "AI chat"]}>
  ### New model: Claude Sonnet 4.6

  Claude Sonnet 4.6 is now available as an AI model option.

  * Use it for agents and prompts that need strong reasoning or detailed answers.

  Doc: [AI chat modes](https://docs.base44.com/Building-your-app/AI-chat-modes)
</Update>

<Update label="February 17, 2026" tags={["AI", "AI chat"]}>
  ### Queue multiple prompts while the AI is working

  The AI chat now supports **message queues**, so you can keep thinking while the AI responds.

  * Send multiple prompts while a response is in progress, then reorder, edit, or remove them in the queue.
  * Pause or clear the queue; queued prompts are stored locally so they survive reloads while the tab stays open.

  Doc: [AI chat modes](https://docs.base44.com/Building-your-app/AI-chat-modes)
</Update>

<Update label="February 17, 2026" tags={["Account & workspace", "Community"]}>
  ### Spotlight: discover examples and resources

  The new **Spotlight** page is live at [app.base44.com/spotlight](https://app.base44.com/spotlight).

  * Browse curated apps, guides, and patterns to see concrete examples of what you can build.
  * Open examples to explore how they work and adapt ideas to your own apps.
</Update>

<Update label="February 17, 2026" tags={["Integrations", "Payments"]}>
  ### Base Payments: built-in payments for your apps

  Base Payments powered by Wix is now documented as the built-in payments solution for Base44.

  * Accept payments directly in your apps and connect orders to your entities, automations, and analytics.

  Doc: [Setting up Base Payments](https://docs.base44.com/Setting-up-your-app/setting-up-wix-payments)
</Update>

<Update label="February 17, 2026" tags={["Security & access", "Authentication"]}>
  ### New: Sign in with Apple

  Apple is now a supported authentication provider.

  * Let people sign in to your app with their Apple ID alongside existing providers such as Google and Microsoft.
</Update>

<Update label="February 16, 2026" tags={["Connectors"]}>
  ### New: Google BigQuery connector

  A **Google BigQuery** connector is now available.

  * Run queries against BigQuery from your app and bring results into your own dashboards or workflows.

  Doc: [Connectors overview](https://docs.base44.com/Integrations/Connectors)
</Update>

<Update label="February 16, 2026" tags={["Account & workspace", "Security & access"]}>
  ### App collaborator roles

  Collaboration is now more flexible at the app level.

  * Invite collaborators to help build or maintain a single app without giving full workspace access.
  * Choose whether collaborators come from workspace members or external builders you invite.

  Doc: [Managing access to your app](https://docs.base44.com/Setting-up-your-app/Managing-access#inviting-collaborators-to-your-app)
</Update>

<Update label="February 16, 2026" tags={["Account & workspace", "Developer tools"]}>
  ### Search across app dashboard pages from the sidebar

  The app editor dashboard sidebar now includes a search bar.

  * Type to find any dashboard page, section, entity, or connector, and jump straight to the matching section.
</Update>

<Update label="February 12, 2026" tags={["Mobile"]}>
  ### Base44 on Google Play

  The Base44 Android app is now in the Google Play Store.

  * Install the app to keep an eye on apps, data, and activity while you are away from your computer.

  Doc: [Mobile experience](https://docs.base44.com/Building-your-app/Mobile-experience)
</Update>

<Update label="February 9, 2026" tags={["AI", "AI chat"]}>
  ### Edit previous messages in the AI chat

  You can now edit earlier messages in the AI chat instead of reverting.

  * Edit a previous message and any later messages are reverted so the AI continues from your updated instructions.

  Doc: [AI chat modes](https://docs.base44.com/Building-your-app/AI-chat-modes)
</Update>

<Update label="February 8, 2026" tags={["Account & workspace"]}>
  ### Control browser notifications for the builder

  You can now manage browser notification preferences from a dedicated notifications panel.

  * Choose which in-browser notifications you receive from Base44.

  Doc: [Managing your account](https://docs.base44.com/documentation/account-and-billing/managing-your-account)
</Update>

<Update label="February 5, 2026" tags={["AI", "AI chat"]}>
  ### Plan mode for new apps

  A new **plan mode** helps you design apps before the first version is created.

  * Answer a short set of questions about your goal and audience; the AI then uses this plan to generate the first version of your app.

  Doc: [Quick start guide](https://docs.base44.com/Getting-Started/Quick-start-guide)
</Update>

<Update label="February 5, 2026" tags={["AI", "AI chat"]}>
  ### Capture: start from an existing website

  The new **Capture** feature lets you start an app from an existing public URL that you own.

  * Capture recreates the visible layout and key UI elements in the editor so you can refine them with the AI chat.

  Doc: [Quick start guide](https://docs.base44.com/Getting-Started/Quick-start-guide)
</Update>

<Update label="February 3, 2026" tags={["Data & media"]}>
  ### More file types for uploads

  File uploads in Base44 now support more formats in both the builder and live apps.

  * Upload CSV, Excel, and other document types so the AI can analyze them or turn them into entities and flows.

  Doc: [Uploading files](https://docs.base44.com/Building-your-app/Using-media)
</Update>

<Update label="February 3, 2026" tags={["Mobile", "App stores"]}>
  ### Submit apps to the app stores

  You can now prepare and package your Base44 app for the Apple App Store and Google Play directly from the editor.

  * Scan your app against store guidelines and generate App Store (IPA) and Google Play (AAB) files from the **Mobile app** tab.
  * Your mobile app wraps your published Base44 app in a secure web view so most content and design changes go live without a new store submission.

  Doc: [Submitting your app to app stores](https://docs.base44.com/documentation/building-your-app/uploading-to-app-stores)
</Update>

<Update label="February 2, 2026" tags={["Account & workspace"]}>
  ### Updated workspace account menu

  The workspace account menu has been redesigned.

  * Key actions such as switching workspaces, managing plans, and opening account settings are easier to find.
</Update>

<Update label="February 1, 2026" tags={["AI", "Integrations"]}>
  ### Custom MCP servers at the account level

  You can now add **custom MCP (Model Context Protocol) servers** at the account level.

  * Connect external tools and data sources so the AI builder can pull in extra context while you work.
  * Reuse the same MCP connections across multiple apps without repeating the setup.

  Doc: [Setting up a custom MCP](https://docs.base44.com/documentation/account-and-billing/setting-up-a-custom-mcp)
</Update>

<Update label="February 1, 2026" tags={["Analytics", "Security & access"]}>
  ### App logs explorer upgrade

  The **App logs** explorer has been upgraded with broader audit coverage, richer metadata, and faster queries.

  * Track more event types with extra context, and filter by category, event type, user email, or errors only.
</Update>

<Update label="January 26, 2026" tags={["Security & access", "Account & workspace"]}>
  ### Delete your Base44 account

  You can now delete your Base44 account following updated account deletion flows.

  * A dedicated guide explains how to request deletion and what happens to your data.

  Doc: [Managing your account](https://docs.base44.com/documentation/account-and-billing/managing-your-account)
</Update>

<Update label="January 22, 2026" tags={["Connectors"]}>
  ### New: Gmail connector

  A **Gmail** connector is now available.

  * Connect Gmail to send emails, read messages, or automate inbox workflows from your apps.

  Doc: [Gmail connector](https://docs.base44.com/Integrations/gmail-connector)
</Update>

<Update label="January 22, 2026" tags={["Data & media"]}>
  ### Share a test link for your data

  A new **preview test link** option has been added to the data experience.

  * Share a link that shows how test data behaves in your app without exposing production records.

  Doc: [Testing your data](https://docs.base44.com/documentation/managing-app-data/testing-your-data)
</Update>

<Update label="January 20, 2026" tags={["AI", "AI chat", "Debugging"]}>
  ### Debug mode: tell the AI when something is wrong

  You can now ask the AI to debug your app logic without writing a detailed bug report.

  * When something feels off in your logic, type a short message like “something is wrong” and let the AI inspect recent changes for issues.
</Update>

<Update label="January 20, 2026" tags={["AI", "AI chat"]}>
  ### Builder questions: follow-ups for unclear prompts

  Builder questions are now available for everyone in the AI chat.

  * When a prompt is short or ambiguous, the AI can ask a few follow-up questions before building, and these questions do not use message credits.
</Update>

<Update label="January 15, 2026" tags={["Automations"]}>
  ### Scheduled tasks are now automations

  Scheduled tasks have evolved into **automations**.

  * Automations now support more triggers, such as data changes, with additional triggers and integrations planned.

  Doc: [Creating automations](https://docs.base44.com/Building-your-app/Creating-automations)
</Update>

<Update label="January 15, 2026" tags={["Data & media"]}>
  ### Test data environment for safer experiments

  A dedicated **test data** environment is now available.

  * Use sample records to design and test flows, then switch to live data when you are ready.

  Doc: [Testing your data](https://docs.base44.com/documentation/managing-app-data/testing-your-data)
</Update>

<Update label="January 12, 2026" tags={["Analytics"]}>
  ### New analytics dashboard

  A new analytics dashboard has rolled out.

  * Track key events with updated retention windows per plan, and export data for deeper analysis.

  Doc: [App analytics](https://docs.base44.com/documentation/performance-and-seo/app-analytics)
</Update>

<Update label="January 11, 2026" tags={["Security & access", "Account & workspace"]}>
  ### Transfer app ownership

  You can now transfer ownership of an app to another person.

  * Move full control of an app when handing it over to a client or another team.

  Doc: [Managing your workspace apps](https://docs.base44.com/documentation/using-your-workspaces/managing-your-workspace-apps)
</Update>

<Update label="January 8, 2026" tags={["Data & media"]}>
  ### Search in your data

  Data views now support searching.

  * Quickly filter and find records in entities by typing keywords.

  Doc: [Managing your app data](https://docs.base44.com/documentation/managing-app-data/Managing-your-app-data)
</Update>

<Update label="January 8, 2026" tags={["Integrations", "Developer tools"]}>
  ### Workspace-level custom integrations

  You can now create **custom OpenAPI integrations** at the workspace level.

  * Connect an API once and reuse it across apps in the same workspace.

  Doc: [Managing workspace integrations](https://docs.base44.com/documentation/integrations/managing-workspace-integrations)
</Update>

<Update label="January 5, 2026" tags={["SEO"]}>
  ### New SEO guide for Base44 apps

  A new SEO guide explains how Base44 handles search optimization and what you can do to improve results.

  * See what the platform handles automatically and what you can configure for better visibility.

  Doc: [SEO and search visibility](https://docs.base44.com/Performance-and-SEO/SEO-and-search-visibility)
</Update>

<Update label="January 4, 2026" tags={["Integrations", "Payments"]}>
  ### New Stripe integration

  A Stripe integration is now available in Base44.

  * Connect Stripe from the AI chat, including setting up products and test mode, and manage transactions from your app dashboard.

  Doc: [Setting up payments](https://docs.base44.com/documentation/setting-up-your-app/setting-up-payments)
</Update>


Built with [Mintlify](https://mintlify.com).