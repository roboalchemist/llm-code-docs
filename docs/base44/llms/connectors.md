# Source: https://docs.base44.com/Integrations/Connectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Connectors

> Connect your app to popular tools like Google Workspace, BigQuery, Slack, Salesforce, GitHub, and more using secure OAuth connections without managing API keys.

## About connectors

Connectors are OAuth integrations that let your Base44 app securely access external tools without managing API keys.

When you connect a tool, you authorize your app to access **your account** in that service. Each connector is app-level, meaning one connected account per tool is shared across the app.

<iframe src="https://www.youtube.com/embed/OTQH8rXAa3c" title="Using connectors in Base44" className="w-full aspect-video rounded-xl" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen />

<Warning>
  **Connectors are shared across your app.** Connected accounts are app-level, not per person. Do not use connectors for private per-user data, for example in a multi-user app where each person expects to connect their own calendar or inbox. Only use connectors when everyone who can access the app is allowed to see the same external data.
</Warning>

<Note>
  You need a [**Builder plan**](https://base44.com/pricing) or higher to use connectors.
</Note>

***

## Adding a connector

Connect your app to a tool by prompting the Base44 **AI chat**. Describe what you want the app to do using that tool.

You can also use example prompts tailored to your app by going to **Integrations** → **Browse** in your app's dashboard. Base44 suggests prompts based on your app's structure, pages, and data to help you get started faster.

<Frame caption="Using connectors in Base44">
    <img src="https://mintcdn.com/base44/oYRfhOUNxDzBL1-M/images/2025-11-23_11-14-53.png?fit=max&auto=format&n=oYRfhOUNxDzBL1-M&q=85&s=979aa4cef53b3b76023c7696a9231d28" alt="Using connectors in Base44" width="600" height="350" data-path="images/2025-11-23_11-14-53.png" />
</Frame>

<Tip>
  **Common connector use cases:**

  * Send reports, alerts, or summaries through **Gmail** or **Outlook**.
  * Generate documents, spreadsheets, presentations, or files using **Google Workspace** tools.
  * Create and manage events or availability using **Google Calendar** or **Outlook**.
  * Power dashboards and data agents with analytics from **Google BigQuery**.
  * Send notifications or updates to teams through **Slack User** or as a **Slack Bot**.
  * Access Wix site data and business tools with **Wix**.
  * Store, sync, and organize files using **Dropbox** or **Box**.
  * Track code activity, issues, and pull requests with **GitHub**.
  * Create and track project tasks with **Linear**, **ClickUp**, or **Wrike**.
</Tip>

**To connect your app to a tool:**

1. In your app editor, open the **AI chat**.
2. Describe what you want the app to do, or use a ready-made prompt:
   * In the **AI chat**, type what you want the app to do.
   * Go to your app's dashboard and click **Integrations** → **Browse**, then click **Use** on a connector. Click an example prompt to add it to the chat, then edit it if needed.
3. Review the **Action required** and **Required permissions**.
4. Click **Connect to \[tool]**.
5. Complete the sign-in authorization.

Approving access lets your app use your account only with the permissions listed for that connector in this app.

<Note>
  **Notes:**

  * If you click **Skip** in the authorization window, the connector is not added. You can run the connection flow again from the AI chat or from **Integrations → Browse**.
  * Some tools require additional steps on their platform after connecting to your Base44 app.
</Note>

***

## Prompt examples

Use the prompts below to connect your app to external tools and automate workflows such as messaging, data syncing, reporting, and updates.

<AccordionGroup>
  <Accordion icon="envelope" title="Gmail">
    ```text  theme={null}
    Send me a daily email with my to-do list using Gmail.
    ```

    ```text  theme={null}
    Email me a summary of all new signups from today.
    ```

    ```text  theme={null}
    Send a Gmail alert when a new task is marked as high priority.
    ```

    ```text  theme={null}
    Send a weekly Gmail digest with key metrics from this dashboard.
    ```

    ```text  theme={null}
    Email my team from Gmail when a deal moves to the Closed Won stage.
    ```
  </Accordion>

  <Accordion icon="envelopes-bulk" title="Outlook">
    ```text  theme={null}
    Connect to my Outlook account and send me a daily email summary from this app.
    ```

    ```text  theme={null}
    Create Outlook calendar events when a new meeting is confirmed in this app.
    ```

    ```text  theme={null}
    Show my upcoming Outlook calendar events in a dashboard.
    ```

    ```text  theme={null}
    Send an Outlook email to my team when a request is marked urgent.
    ```

    ```text  theme={null}
    Check my Outlook calendar availability before scheduling appointments.
    ```
  </Accordion>

  <Accordion icon="google" title="Google Workspace">
    ```text  theme={null}
    Save generated PDF reports from my app to Google Drive.
    ```

    ```text  theme={null}
    Create a Google Doc with a daily summary of activity from my app.
    ```

    ```text  theme={null}
    Sync new records from this app into a Google Sheets spreadsheet.
    ```

    ```text  theme={null}
    Keep a Google Sheets dashboard updated with daily metrics from my app.
    ```

    ```text  theme={null}
    Generate a Google Slides presentation summarizing this week's key KPIs.
    ```
  </Accordion>

  <Accordion icon="google" title="Google Calendar">
    ```text  theme={null}
    Sync all my bookings directly to my Google Calendar.
    ```

    ```text  theme={null}
    Show my real-time availability from Google Calendar to clients.
    ```

    ```text  theme={null}
    When an appointment is confirmed, create a calendar event and invite attendees.
    ```

    ```text  theme={null}
    Block time on my calendar when a task is marked as deep work.
    ```

    ```text  theme={null}
    Create a daily agenda view from my upcoming calendar events.
    ```
  </Accordion>

  <Accordion icon="magnifying-glass-chart" title="Google BigQuery">
    Connect your Base44 app to Google BigQuery to power a data agent that queries your analytics warehouse in natural language.

    ```text  theme={null}
    Connect this app to my BigQuery project and add a data agent that answers questions about my analytics.
    ```

    ```text  theme={null}
    Let users ask questions about sales trends from my BigQuery dataset.
    ```

    ```text  theme={null}
    Build a dashboard powered by BigQuery and let the agent explain performance changes.
    ```

    ```text  theme={null}
    Alert me when a KPI drops below a threshold based on BigQuery data.
    ```
  </Accordion>

  <Accordion icon="signal-bars-good" title="Google Analytics">
    ```text  theme={null}
    Connect Google Analytics and show pageviews, sessions, and top pages in a dashboard.
    ```

    ```text  theme={null}
    Pull my Google Analytics traffic by source and show trends week over week.
    ```

    ```text  theme={null}
    Alert me when organic traffic drops below a threshold in Google Analytics.
    ```

    ```text  theme={null}
    Create a weekly report from Google Analytics and email it to me.
    ```

    ```text  theme={null}
    Let me filter Google Analytics metrics by date range and page path in this app.
    ```
  </Accordion>

  <Accordion icon="slack" title="Slack User">
    ```text  theme={null}
    Post a message to the #support channel when a new ticket is created.
    ```

    ```text  theme={null}
    Send a daily summary of completed tasks to my team's Slack channel.
    ```

    ```text  theme={null}
    Notify me in Slack when a sale is made in my app.
    ```

    ```text  theme={null}
    Share important updates in the #announcements channel when a document is approved.
    ```

    ```text  theme={null}
    Send alerts to a Slack channel when deadlines are approaching.
    ```
  </Accordion>

  <Accordion icon="slack" title="Slack Bot">
    ```text  theme={null}
    Send a message as a bot to the #announcements channel when a release is published.
    ```

    ```text  theme={null}
    Post a bot message to #support when a new ticket is created.
    ```

    ```text  theme={null}
    Send a daily bot summary to #team-updates at 5pm.
    ```

    ```text  theme={null}
    Post a bot message to the selected Slack channel when an admin clicks "Send update".
    ```

    ```text  theme={null}
    Send a bot message to #product-updates when a feature flag is enabled.
    ```
  </Accordion>

  <Accordion icon="discord" title="Discord">
    Use the Discord connector to send messages and post updates to channels in Discord servers you authorize.

    <Note>
      Direct messages (DMs) are not supported.
    </Note>

    ```text  theme={null}
    Post a message to the #announcements channel when a new feature is released.
    ```

    ```text  theme={null}
    Send an alert to the #ops channel when a critical error occurs.
    ```

    ```text  theme={null}
    Notify a Discord channel when a new support ticket is created.
    ```

    ```text  theme={null}
    Sync approved announcements from this app to a Discord server.
    ```

    ```text  theme={null}
    Send a daily summary of activity to a Discord channel.
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="m0 7.354 2.113 9.292h.801a1.54 1.54 0 0 0 1.506-1.218l1.351-6.34a.171.171 0 0 1 .167-.137c.08 0 .15.058.167.137l1.352 6.34a1.54 1.54 0 0 0 1.506 1.218h.805l2.113-9.292h-.565c-.62 0-1.159.43-1.296 1.035l-1.26 5.545-1.106-5.176a1.76 1.76 0 0 0-2.19-1.324c-.639.176-1.113.716-1.251 1.365l-1.094 5.127-1.26-5.537A1.33 1.33 0 0 0 .563 7.354H0zm13.992 0a.951.951 0 0 0-.951.95v8.342h.635a.952.952 0 0 0 .951-.95V7.353h-.635zm1.778 0 3.158 4.66-3.14 4.632h1.325c.368 0 .712-.181.918-.486l1.756-2.59a.12.12 0 0 1 .197 0l1.754 2.59c.206.305.55.486.918.486h1.326l-3.14-4.632L24 7.354h-1.326c-.368 0-.712.181-.918.486l-1.772 2.617a.12.12 0 0 1-.197 0L18.014 7.84a1.108 1.108 0 0 0-.918-.486H15.77z" fill="currentColor"/></svg>} title="Wix">
    ```text  theme={null}
    Connect to my Wix account and show key site analytics in a dashboard.
    ```

    ```text  theme={null}
    Sync customer data from my Wix site into a CRM table in this app.
    ```

    ```text  theme={null}
    Show recent orders from my Wix store in a management dashboard.
    ```

    ```text  theme={null}
    Create an internal dashboard to track website activity and business data from Wix.
    ```

    ```text  theme={null}
    Import business data from Wix so I can build workflows and reports in this app.
    ```
  </Accordion>

  <Accordion icon="github" title="GitHub">
    Use the GitHub connector to manage repositories, list issues, review pull requests, and automate workflows connected to your codebase.

    ```text  theme={null}
    Connect to my GitHub account and list all open pull requests for review.
    ```

    ```text  theme={null}
    Show open issues from my repository in a dashboard.
    ```

    ```text  theme={null}
    Create a new GitHub issue when a bug is reported in this app.
    ```

    ```text  theme={null}
    Sync the latest commits from my repository into a changelog page.
    ```

    ```text  theme={null}
    Create a GitHub issue automatically when a critical incident is created.
    ```
  </Accordion>

  <Accordion icon="notion" title="Notion">
    ```text  theme={null}
    Sync a Notion database with my CRM records.
    ```

    ```text  theme={null}
    Write project updates from this app into a Notion page.
    ```

    ```text  theme={null}
    Show Notion checklist progress for team onboarding in my dashboard.
    ```

    ```text  theme={null}
    Create new Notion pages for every new client added in this app.
    ```

    ```text  theme={null}
    Post meeting notes from the app to a specific Notion page.
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M2 18.439l3.69-2.828c1.961 2.56 4.044 3.739 6.363 3.739 2.307 0 4.33-1.166 6.203-3.704L22 18.405C19.298 22.065 15.941 24 12.053 24 8.178 24 4.788 22.078 2 18.439zM12.04 6.15l-6.568 5.66-3.036-3.52L12.055 0l9.543 8.296-3.05 3.509z" fill="currentColor"/></svg>} title="ClickUp">
    ```text  theme={null}
    Connect ClickUp and show my tasks by status and due date in a dashboard.
    ```

    ```text  theme={null}
    Create a new ClickUp task when a new record is added to my Requests entity.
    ```

    ```text  theme={null}
    When a request is marked as urgent, assign a ClickUp task to a teammate and set a due date.
    ```

    ```text  theme={null}
    Sync ClickUp task status back into this app so I can track progress here.
    ```

    ```text  theme={null}
    Post a Slack update when a ClickUp task moves to Done.
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M2.886 4.18A11.982 11.982 0 0 1 11.99 0C18.624 0 24 5.376 24 12.009c0 3.64-1.62 6.903-4.18 9.105L2.887 4.18ZM1.817 5.626l16.556 16.556c-.524.33-1.075.62-1.65.866L0.951 7.277c.247-.575.537-1.126.866-1.65ZM0.322 9.163l14.515 14.515c-.71.172-1.443.282-2.195.322L0 11.358a12 12 0 0 1 .322-2.195Zm-.17 4.862 9.823 9.824a12.02 12.02 0 0 1-9.824-9.824Z" fill="currentColor"/></svg>} title="Linear">
    ```text  theme={null}
    Connect Linear and show my issues by status, assignee, and priority in a dashboard.
    ```

    ```text  theme={null}
    Create a Linear issue automatically when a bug is submitted in this app.
    ```

    ```text  theme={null}
    Sync Linear issue status back into this app so I can track progress here.
    ```

    ```text  theme={null}
    Show open Linear issues for a selected project in this app.
    ```

    ```text  theme={null}
    Notify me when a Linear issue is moved to Done.
    ```
  </Accordion>

  <Accordion icon="check" title="Wrike">
    ```text  theme={null}
    Connect Wrike and show tasks for a selected project in a dashboard.
    ```

    ```text  theme={null}
    Create a Wrike task when a new bug is reported in this app.
    ```

    ```text  theme={null}
    Sync Wrike task status and assignee into my internal tracker table.
    ```

    ```text  theme={null}
    Notify me when Wrike tasks are overdue.
    ```

    ```text  theme={null}
    Generate a weekly Wrike project status report and email it to me.
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M.959 5.523c-.54 0-.959.42-.959.899v7.549a4.59 4.59 0 004.613 4.494 4.717 4.717 0 004.135-2.457c.779 1.438 2.337 2.457 4.074 2.457 2.577 0 4.674-2.037 4.674-4.613.06-2.457-2.037-4.495-4.613-4.495-1.738 0-3.295.959-4.074 2.397-.78-1.438-2.338-2.397-4.135-2.397-1.079 0-2.038.36-2.817.899V6.422a.92.92 0 00-.898-.899zM17.602 9.26a.95.95 0 00-.704.158c-.36.3-.479.899-.18 1.318l2.397 3.116-2.396 3.115c-.3.42-.24.96.18 1.26.419.3 1.016.298 1.316-.122l2.039-2.636 2.096 2.697c.3.36.899.419 1.318.12.36-.3.42-.84.121-1.259l-2.338-3.115 2.338-3.057c.3-.419.298-1.018-.121-1.318-.48-.3-1.019-.24-1.318.18l-2.096 2.576-2.04-2.695c-.149-.18-.373-.3-.612-.338zM4.613 11.154c1.558 0 2.817 1.26 2.817 2.758 0 1.558-1.259 2.756-2.817 2.756-1.558 0-2.816-1.198-2.816-2.756 0-1.498 1.258-2.758 2.816-2.758zm8.27 0c1.558 0 2.816 1.26 2.816 2.758-.06 1.558-1.318 2.756-2.816 2.756-1.558 0-2.817-1.198-2.817-2.756 0-1.498 1.259-2.758 2.817-2.758Z" fill="currentColor"/></svg>} title="Box">
    ```text  theme={null}
    Connect Box and list files and folders for this project inside my app.
    ```

    ```text  theme={null}
    Upload new files from this app to a selected Box folder.
    ```

    ```text  theme={null}
    Keep a Box folder in sync with records in my Files entity.
    ```

    ```text  theme={null}
    Create a simple approval flow for Box files, and post status updates to Slack.
    ```

    ```text  theme={null}
    Search Box for files by name and show results in a table.
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M6 1.807L0 5.629l6 3.822 6.001-3.822L6 1.807zM18 1.807l-6 3.822 6 3.822 6-3.822-6-3.822zM0 13.274l6 3.822 6.001-3.822L6 9.452l-6 3.822zM18 9.452l-6 3.822 6 3.822 6-3.822-6-3.822zM6 18.371l6.001 3.822 6-3.822-6-3.822L6 18.371z" fill="currentColor"/></svg>} title="Dropbox">
    ```text  theme={null}
    Connect Dropbox and show project files in this app.
    ```

    ```text  theme={null}
    Upload files from this app to a selected Dropbox folder.
    ```

    ```text  theme={null}
    Sync Dropbox files with records in my Files table.
    ```

    ```text  theme={null}
    Search Dropbox for files by name and display the results in a dashboard.
    ```

    ```text  theme={null}
    Build a file management view for documents stored in Dropbox.
    ```
  </Accordion>

  <Accordion icon="salesforce" title="Salesforce">
    ```text  theme={null}
    Sync new leads from this app into Salesforce.
    ```

    ```text  theme={null}
    Show Salesforce opportunity stages inside my project dashboard.
    ```

    ```text  theme={null}
    Log customer support requests in Salesforce automatically.
    ```

    ```text  theme={null}
    Update Salesforce contact records when app data changes.
    ```

    ```text  theme={null}
    Pull recent Salesforce tasks into a daily action list in my app.
    ```
  </Accordion>

  <Accordion icon="hubspot" title="HubSpot">
    ```text  theme={null}
    Sync new leads from this app into HubSpot contacts.
    ```

    ```text  theme={null}
    Show HubSpot deal stages inside my project dashboard.
    ```

    ```text  theme={null}
    Create HubSpot contacts when users sign up in this app.
    ```

    ```text  theme={null}
    Update HubSpot deal values when orders are placed.
    ```

    ```text  theme={null}
    Import HubSpot contact lists to segment users in my app.
    ```
  </Accordion>

  <Accordion icon="linkedin" title="LinkedIn">
    ```text  theme={null}
    Post a status update to my LinkedIn feed when I publish a new article.
    ```

    ```text  theme={null}
    Share company announcements to my LinkedIn profile.
    ```

    ```text  theme={null}
    Post project milestones to LinkedIn automatically.
    ```

    ```text  theme={null}
    Create a LinkedIn post when a new blog post is published.
    ```

    ```text  theme={null}
    Draft a LinkedIn post and let me approve it before publishing.
    ```
  </Accordion>

  <Accordion icon="tiktok" title="TikTok">
    ```text  theme={null}
    Show my TikTok profile stats and follower count in a dashboard.
    ```

    ```text  theme={null}
    List my recent TikTok videos with their view counts.
    ```

    ```text  theme={null}
    Display my TikTok bio and verification status.
    ```

    ```text  theme={null}
    Show my total likes, followers, and video count from TikTok.
    ```

    ```text  theme={null}
    Create a gallery of my TikTok videos.
    ```
  </Accordion>
</AccordionGroup>

***

## Using connectors

Once you connect a tool to your app, you can reuse it across pages, flows, and backend functions. In the **AI chat**, ask Base44 to build pages, tables, dashboards, or automations that read from or write to the connector.

When you include a connector in a flow, Base44 also creates a backend function in **Dashboard** → **Code** → **Functions**. Open that function to review the generated code. You can edit it yourself or prompt the AI chat to update it so it uses the connector the way you need. For example: `Send a Slack message to #product-updates when this function runs.`

If you later add a flow that needs extra permissions, you may be asked to review and approve the new actions and permissions for that tool.

<Frame caption="Slack connector in backend functions">
    <img src="https://mintcdn.com/base44/yBFCOCQofInfb8rN/images/ConnectorFunction.png?fit=max&auto=format&n=yBFCOCQofInfb8rN&q=85&s=09eee2155c15b85d8c9f3458788310fe" alt="Code editor showing a Base44 backend function that posts a message to the #product-updates Slack channel." width="1141" height="722" data-path="images/ConnectorFunction.png" />
</Frame>

***

## Managing connectors

View and manage your app's connectors, review what each can access, and switch or disconnect the connected account per tool as needed.

<Frame caption="Viewing and managing your app connections">
    <img src="https://mintcdn.com/base44/mGUAlD89bINtD9VJ/images/MyIntegrationsTab.png?fit=max&auto=format&n=mGUAlD89bINtD9VJ&q=85&s=2e7002711c099c1ad7cb3907e56aa5d7" alt="App dashboard showing the Integrations page with the My integrations tab selected, listing connected tools and a View access button." width="1084" height="619" data-path="images/MyIntegrationsTab.png" />
</Frame>

**To manage your connectors:**

1. Go to your app's dashboard and click **Integrations**.
2. Click the **My integrations** tab.
3. For each connector, choose what you want to do:
   * **View access:** Check the permissions granted to the app.
   * **More actions:** Switch or disconnect an account. The new account is used for future actions.
   * **Reconnect:** Connect an account again.

***

## Connector permissions

When you connect a tool, the connector requests a set of permissions, also called scopes. These define what your app can do with the connected account. Depending on what you build, you are prompted to authorize only the permissions required for that flow.

Base44 only uses permissions to support the features you enable, so you always stay in control of what your app can access.

<Warning>
  **Important**: The use of raw and derived information received from Google Workspace APIs will adhere to the [Google User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the [Limited Use requirements](https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes).
</Warning>

<Frame caption="Authorizing permissions to connect to Slack">
    <img src="https://mintcdn.com/base44/Z04m0iWfMQSYvNwM/images/ConnectorSlack.png?fit=max&auto=format&n=Z04m0iWfMQSYvNwM&q=85&s=88d98cef6e5720e377efcd6e6b873fa0" alt="AI chat showing the Slack connector with required permissions and a Connect to Slack button." width="453" height="681" data-path="images/ConnectorSlack.png" />
</Frame>

Click a connector below to see the permissions it may request, depending on the flows you build.

<Note>
  Scope lists can change as providers update their APIs. Always review the permissions shown when you connect a tool because they reflect the current access your app is requesting.
</Note>

<AccordionGroup>
  <Accordion icon="envelope" title="Gmail">
    These permissions allow your app to send and manage email using your connected Gmail account.

    ```text  theme={null}
    https://www.googleapis.com/auth/gmail.readonly
    https://www.googleapis.com/auth/gmail.send
    https://www.googleapis.com/auth/gmail.modify
    https://www.googleapis.com/auth/gmail.compose
    ```
  </Accordion>

  <Accordion icon="envelopes-bulk" title="Outlook">
    These permissions allow your app to read and send email, manage calendar events, and access basic user account information using your connected Outlook account.

    **Core authentication:**

    ```text  theme={null}
    offline_access
    openid
    profile
    email
    User.Read
    ```

    **Mail access:**

    ```text  theme={null}
    Mail.Read
    Mail.ReadBasic
    Mail.ReadWrite
    Mail.Send
    ```

    **Calendar access:**

    ```text  theme={null}
    Calendars.Read
    Calendars.ReadWrite
    ```

    **Mailbox settings:**

    ```text  theme={null}
    MailboxSettings.Read
    MailboxSettings.ReadWrite
    ```

    **Shared mail and contacts (recommended):**

    ```text  theme={null}
    Mail.Read.Shared
    Mail.Send.Shared
    Contacts.Read
    ```
  </Accordion>

  <Accordion icon="google" title="Google Workspace">
    These permissions allow your app to work with Google Docs, Sheets, Slides, and Drive files.

    **Docs**

    ```text  theme={null}
    https://www.googleapis.com/auth/documents
    https://www.googleapis.com/auth/documents.readonly
    ```

    **Sheets**

    ```text  theme={null}
    https://www.googleapis.com/auth/spreadsheets
    https://www.googleapis.com/auth/spreadsheets.readonly
    ```

    **Slides**

    ```text  theme={null}
    https://www.googleapis.com/auth/presentations
    https://www.googleapis.com/auth/presentations.readonly
    ```

    **Drive**

    ```text  theme={null}
    https://www.googleapis.com/auth/drive.file
    ```
  </Accordion>

  <Accordion icon="google" title="Google Calendar">
    These permissions allow your app to read and manage Google Calendar events and availability.

    ```text  theme={null}
    https://www.googleapis.com/auth/calendar
    https://www.googleapis.com/auth/calendar.readonly
    https://www.googleapis.com/auth/calendar.events
    https://www.googleapis.com/auth/calendar.events.readonly
    https://www.googleapis.com/auth/calendar.events.freebusy
    https://www.googleapis.com/auth/calendar.freebusy
    https://www.googleapis.com/auth/calendar.app.created
    https://www.googleapis.com/auth/calendar.calendarlist.readonly
    https://www.googleapis.com/auth/calendar.events.public.readonly
    https://www.googleapis.com/auth/calendar.settings.readonly
    ```
  </Accordion>

  <Accordion icon="magnifying-glass-chart" title="Google BigQuery">
    These permissions allow your app to read data from BigQuery datasets and tables.

    ```text  theme={null}
    https://www.googleapis.com/auth/bigquery.readonly
    ```
  </Accordion>

  <Accordion icon="signal-bars-good" title="Google Analytics">
    These permissions allow your app to read data and edit management entities.

    ```text  theme={null}
    analytics.readonly
    analytics.edit
    ```
  </Accordion>

  <Accordion icon="slack" title="Slack User">
    The Slack User connector requests permissions required to read and manage channels, messages, files, reactions, reminders, user data, and workspace settings.

    ```text  theme={null}
    channels:read
    channels:write
    channels:history
    chat:write
    chat:read
    files:read
    files:write
    groups:read
    groups:write
    groups:history
    im:read
    im:write
    im:history
    mpim:read
    mpim:write
    mpim:history
    reactions:read
    reactions:write
    users:read
    users:read.email
    team:read
    usergroups:read
    usergroups:write
    pins:read
    pins:write
    bookmarks:read
    bookmarks:write
    reminders:read
    reminders:write
    stars:read
    stars:write
    search:read
    emoji:read
    dnd:read
    dnd:write
    links:read
    links:write
    ```
  </Accordion>

  <Accordion icon="slack" title="Slack Bot">
    These permissions allow your app to send messages to Slack channels using a bot identity.

    ```text  theme={null}
    app_mentions:read
    channels:history
    channels:join
    channels:read
    chat:write
    chat:write.customize
    chat:write.public
    commands
    files:read
    files:write
    groups:history
    groups:read
    groups:write
    im:history
    im:read
    im:write
    reactions:write
    users:read
    mpim:read
    mpim:history
    ```
  </Accordion>

  <Accordion icon="discord" title="Discord">
    These permissions allow your app to send messages and post updates to channels in the Discord servers you authorize.

    <Note>
      The Discord connector does not support viewing or sending direct messages (DMs).
    </Note>

    ```text  theme={null}
    identify
    guilds
    email
    guilds.members.read
    guilds.join
    gdm.join
    messages.read
    connections
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="m0 7.354 2.113 9.292h.801a1.54 1.54 0 0 0 1.506-1.218l1.351-6.34a.171.171 0 0 1 .167-.137c.08 0 .15.058.167.137l1.352 6.34a1.54 1.54 0 0 0 1.506 1.218h.805l2.113-9.292h-.565c-.62 0-1.159.43-1.296 1.035l-1.26 5.545-1.106-5.176a1.76 1.76 0 0 0-2.19-1.324c-.639.176-1.113.716-1.251 1.365l-1.094 5.127-1.26-5.537A1.33 1.33 0 0 0 .563 7.354H0zm13.992 0a.951.951 0 0 0-.951.95v8.342h.635a.952.952 0 0 0 .951-.95V7.353h-.635zm1.778 0 3.158 4.66-3.14 4.632h1.325c.368 0 .712-.181.918-.486l1.756-2.59a.12.12 0 0 1 .197 0l1.754 2.59c.206.305.55.486.918.486h1.326l-3.14-4.632L24 7.354h-1.326c-.368 0-.712.181-.918.486l-1.772 2.617a.12.12 0 0 1-.197 0L18.014 7.84a1.108 1.108 0 0 0-.918-.486H15.77z" fill="currentColor"/></svg>} title="Wix">
    These permissions allow your app to access Wix site data and business tools such as customer data, orders, analytics, and other site resources to power dashboards, workflows, and automations in your app.

    The exact permissions requested depend on the Wix data and business actions your app needs to use.
  </Accordion>

  <Accordion icon="github" title="GitHub">
    These permissions allow your app to access GitHub data such as repositories, issues, and pull requests. Some flows may also request permission to create or update issues.

    The exact scopes requested depend on the flows you build and may include access to repositories and organization data.
  </Accordion>

  <Accordion icon="notion" title="Notion">
    The Notion connector allows your app to read and update content, create pages and comments, and access user information within the workspace you authorize.

    ```text  theme={null}
    read_content
    update_content
    insert_content
    read_comments
    create_comments
    read_users
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M2 18.439l3.69-2.828c1.961 2.56 4.044 3.739 6.363 3.739 2.307 0 4.33-1.166 6.203-3.704L22 18.405C19.298 22.065 15.941 24 12.053 24 8.178 24 4.788 22.078 2 18.439zM12.04 6.15l-6.568 5.66-3.036-3.52L12.055 0l9.543 8.296-3.05 3.509z" fill="currentColor"/></svg>} title="ClickUp">
    The ClickUp connector uses ClickUp's OAuth authorization model. When you authorize the connector, it can access ClickUp resources such as tasks, lists, and spaces based on the permissions you already have in your workspace.
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M2.886 4.18A11.982 11.982 0 0 1 11.99 0C18.624 0 24 5.376 24 12.009c0 3.64-1.62 6.903-4.18 9.105L2.887 4.18ZM1.817 5.626l16.556 16.556c-.524.33-1.075.62-1.65.866L0.951 7.277c.247-.575.537-1.126.866-1.65ZM0.322 9.163l14.515 14.515c-.71.172-1.443.282-2.195.322L0 11.358a12 12 0 0 1 .322-2.195Zm-.17 4.862 9.823 9.824a12.02 12.02 0 0 1-9.824-9.824Z" fill="currentColor"/></svg>} title="Linear">
    These permissions allow your app to access Linear workspace data, create and manage issues, add comments, and automate workflows based on issue activity. Some advanced actions such as webhook management may require additional admin permissions.

    ```text  theme={null}
    read
    issues:create
    comments:create
    write
    admin
    ```
  </Accordion>

  <Accordion icon="check" title="Wrike">
    These permissions allow your app to access Wrike workspace data.

    ```text  theme={null}
    Default
    wsReadOnly
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M.959 5.523c-.54 0-.959.42-.959.899v7.549a4.59 4.59 0 004.613 4.494 4.717 4.717 0 004.135-2.457c.779 1.438 2.337 2.457 4.074 2.457 2.577 0 4.674-2.037 4.674-4.613.06-2.457-2.037-4.495-4.613-4.495-1.738 0-3.295.959-4.074 2.397-.78-1.438-2.338-2.397-4.135-2.397-1.079 0-2.038.36-2.817.899V6.422a.92.92 0 00-.898-.899zM17.602 9.26a.95.95 0 00-.704.158c-.36.3-.479.899-.18 1.318l2.397 3.116-2.396 3.115c-.3.42-.24.96.18 1.26.419.3 1.016.298 1.316-.122l2.039-2.636 2.096 2.697c.3.36.899.419 1.318.12.36-.3.42-.84.121-1.259l-2.338-3.115 2.338-3.057c.3-.419.298-1.018-.121-1.318-.48-.3-1.019-.24-1.318.18l-2.096 2.576-2.04-2.695c-.149-.18-.373-.3-.612-.338zM4.613 11.154c1.558 0 2.817 1.26 2.817 2.758 0 1.558-1.259 2.756-2.817 2.756-1.558 0-2.816-1.198-2.816-2.756 0-1.498 1.258-2.758 2.816-2.758zm8.27 0c1.558 0 2.816 1.26 2.816 2.758-.06 1.558-1.318 2.756-2.816 2.756-1.558 0-2.817-1.198-2.817-2.756 0-1.498 1.259-2.758 2.817-2.758Z" fill="currentColor"/></svg>} title="Box">
    These permissions allow your app to access and manage files and folders in the connected Box account.

    ```text  theme={null}
    root_readwrite
    ```
  </Accordion>

  <Accordion icon={<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="20" height="20"><path d="M6 1.807L0 5.629l6 3.822 6.001-3.822L6 1.807zM18 1.807l-6 3.822 6 3.822 6-3.822-6-3.822zM0 13.274l6 3.822 6.001-3.822L6 9.452l-6 3.822zM18 9.452l-6 3.822 6 3.822 6-3.822-6-3.822zM6 18.371l6.001 3.822 6-3.822-6-3.822L6 18.371z" fill="currentColor"/></svg>} title="Dropbox">
    These permissions allow your app to access account information and read, upload, and manage files in the connected Dropbox account.

    ```text  theme={null}
    account_info.read
    files.metadata.read
    files.content.read
    files.content.write
    ```
  </Accordion>

  <Accordion icon="salesforce" title="Salesforce">
    These permissions allow your app to access Salesforce APIs, user identity data, CRM records, content, analytics, marketing tools, and customer data platform services.

    ```text  theme={null}
    api
    refresh_token
    full
    web
    id
    openid
    profile
    email
    address
    phone
    offline_access
    custom_permissions
    wave_api
    chatter_api
    visualforce
    content
    cdp_api
    cdp_profile_api
    cdp_query_api
    cdp_segment_api
    interaction_api
    cdp_ingest_api
    pardot_api
    ```
  </Accordion>

  <Accordion icon="hubspot" title="HubSpot">
    These permissions allow your app to read and write CRM data, manage deals, quotes, tickets, marketing tools, automation, forms, files, and analytics data.

    ```text  theme={null}
    crm.objects.contacts.read
    crm.objects.contacts.write
    crm.objects.companies.read
    crm.objects.companies.write
    crm.objects.deals.read
    crm.objects.deals.write
    crm.objects.owners.read
    crm.objects.quotes.read
    crm.objects.quotes.write
    crm.lists.read
    crm.lists.write
    crm.schemas.contacts.read
    crm.schemas.companies.read
    crm.schemas.deals.read
    tickets
    e-commerce
    automation
    forms
    files
    content
    social
    analytics.read
    ```
  </Accordion>

  <Accordion icon="linkedin" title="LinkedIn">
    These permissions allow your app to manage profiles, company pages, posts, and advertising insights.

    ```text  theme={null}
    openid
    profile
    r_ads_reporting
    r_organization_social
    rw_organization_admin
    w_member_social
    r_profile_basicinfo
    r_ads
    r_verify
    w_organization_social
    rw_ads
    r_basicprofile
    r_organization_admin
    email
    r_1st_connections_size
    ```
  </Accordion>

  <Accordion icon="tiktok" title="TikTok">
    These permissions allow your app to access profile data and read performance metrics.

    **Product**

    ```text  theme={null}
    Login Kit
    ```

    **Permissions**

    ```text  theme={null}
    artist.certification.read
    artist.certification.update
    user.info.basic
    user.info.profile
    user.info.stats
    video.list
    ```
  </Accordion>
</AccordionGroup>

***

## Individual account connections

Connectors are app-level integrations. When you connect any tool or service, your Base44 app uses a single shared account for that connector that everyone in the app shares.

If you need each person to connect their own account, you need to create a custom per-user OAuth flow using backend functions and the provider's API. Connectors do not support this scenario.

<Warning>
  **Important:** Per user OAuth is an advanced integration pattern. Exact endpoints, scopes, and parameters depend on the provider, so always follow the provider's OAuth documentation together with the steps above.
</Warning>

**To build a per-person OAuth flow:**

1. **Plan the OAuth flow with Discuss mode:** Use Discuss mode in the AI chat and describe what you want, for example: “Each person should connect their own LinkedIn account. Help me design the OAuth flow with backend functions.” Work with the AI to outline the redirect, callback, token storage, and token refresh steps based on the provider's documentation.
2. **Implement the OAuth flow in backend code:** Use backend functions (and the plan you created in Discuss mode) to:
   * Send people to the provider's authorization page.
   * Receive the authorization callback.
   * Store user-specific tokens securely in your app's data.
   * Add token refresh logic if the provider uses expiring tokens.

***

## FAQs

<AccordionGroup>
  <Accordion title="Which tools can I connect my app to?">
    You can connect your Base44 app to Gmail, Google Workspace tools (Drive, Docs, Sheets, Slides), Google Calendar, Outlook, Google BigQuery, Google Analytics, Slack User, Slack Bot, Discord, Wix, GitHub, Notion, ClickUp, Wrike, Linear, Box, Dropbox, Salesforce, HubSpot, LinkedIn, and TikTok, with more tools coming.

    To see the most up-to-date list, go to your app's dashboard and click **Integrations** → **Browse**.
  </Accordion>

  <Accordion title="What is the difference between the Slack User and Slack Bot connectors?">
    * **Slack User** connects as a user in your Slack workspace and allows your app to read and interact with workspace data.
    * **Slack Bot** connects as a bot in your Slack workspace and allows your app to send messages as a configurable bot in Slack channels and power bot-based workflows.
  </Accordion>

  <Accordion title="Can I connect multiple tools to my app?">
    Yes. You can connect multiple tools to the same app.
  </Accordion>

  <Accordion title="Can I connect multiple accounts to the same tool?">
    Each app uses one account per connector type, for example a single Gmail account for a Gmail connector or a single Slack account for a Slack connector. To connect to a different account, click the **More actions** icon and choose **Switch account**.
  </Accordion>

  <Accordion title="How do permissions work for connectors?">
    When you connect a tool, the **Required permissions** list shows the OAuth scopes and capabilities that your app will be able to use, such as reading or writing data. The connector can only perform actions that match the permissions you approved for that tool in this specific app.

    To see the exact scopes and permissions for each connector, review the [Connector permissions](#connector-permissions) section above.
  </Accordion>

  <Accordion title="What happens if a flow needs additional permissions?">
    If you build a flow that requires additional permissions from a connector you already connected, Base44 prompts you to review and approve the updated permissions for that tool before the flow can run.
  </Accordion>

  <Accordion title="Who connects an account, and who can use it?">
    Any teammate who can edit the app can connect an external tool. Each app uses one connected account per tool. Once connected, all teammates who can edit the app can use the shared connector in that app. People who use your published app interact with data and actions powered by that connector; they do not connect their own accounts.
  </Accordion>

  <Accordion title="Can I still create custom integrations?">
    Yes. You can still create [custom integrations](/Integrations/How-to-create-integrations) and use [manual integrations](/Integrations/Using-integrations) for custom APIs or advanced workflows. Connectors focus on managed, OAuth-based connections to popular tools.
  </Accordion>

  <Accordion title="What is the difference between connectors and integrations?">
    * **Connectors** are managed, OAuth-based connections to popular tools that you can set up from the **AI chat** without handling API keys. They are designed for quick, no-code connections to external tools.
    * **Integrations** include custom and manual integrations, where you configure API keys and credentials yourself. Use integrations when you need fine-grained control over a specific API or a tool that does not yet have a connector.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).