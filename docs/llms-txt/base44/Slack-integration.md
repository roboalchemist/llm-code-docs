# Source: https://docs.base44.com/Integrations/Slack-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Integration

> Connect your Base44 app to Slack so it can send real-time messages whenever something important happens like a new task being created or a status changing. This is a great way to keep your team updated directly inside Slack without switching between tools.

<Info>
  <u>Note</u>: Slack integration is available on Builder tier and above.
</Info>

# Step by step setup:

## Part 1: The Slack side

If you already have your Slack webhook, you can skip ahead to [Part 2 - The Base44 side.](https://docs.base44.com/Integrations/Slack-integration#part-2%3A-the-base44-side)

<Steps>
  <Step title="Go to Slack API Apps">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/SlackCreateApp.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=665ce65dff5bb32ded5bd5455d46b334" alt="Slack Create App Pn" width="1582" height="812" data-path="images/SlackCreateApp.png" />

    * Head over to: [https://api.slack.com/apps](https://api.slack.com/apps)
    * Click **Create an App**
    * Click **From Scratch**

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/SlackFromScratch.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=c4ca31f4e81b72b99d87851699e5d155" alt="Slack From Scratch Pn" width="1590" height="789" data-path="images/SlackFromScratch.png" />
  </Step>

  <Step title="Give it a name">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/Slack-nameWorkspace.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=8f770788c510c5db160b8e27cd3b737d" alt="Slack Name Workspace Pn" width="1999" height="1003" data-path="images/Slack-nameWorkspace.png" />

    * For example: `Base44 Notifications`
    * Pick your workspace
  </Step>

  <Step title="Set up Incoming Webhooks">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/Screenshot2025-08-23at1.39.17PM.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=f692e79c91c3f120b208fcf1da1956af" alt="Screenshot2025 08 23at1 39 17PM Pn" width="1581" height="705" data-path="images/Screenshot2025-08-23at1.39.17PM.png" />

    * In the sidebar, open **Incoming Webhooks**
    * Toggle **Activate Incoming Webhooks** to On
  </Step>

  <Step title="Connect Webhook to Workspace">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/Screenshot2025-08-23at1.41.31PM.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=f704aa5753256f5abe3ae417aa1771ec" alt="Screenshot2025 08 23at1 41 31PM Pn" width="1579" height="704" data-path="images/Screenshot2025-08-23at1.41.31PM.png" />

    * Scroll down on this same page
    * Click on **Add New Webhook to Workspace**
    * Select the channel where messages should appear
    * Click **Allow**
  </Step>

  <Step title="Copy your Webhook URL">
    * Your webhook URL should look similar to this:

      `https://hooks.slack.com/services/T000/B000/XXXXXXXX`
    * Keep this handy, you'll use this in Base44 when it prompts you for the **secret**.
  </Step>
</Steps>

***

## Part 2: The Base44 side

Once you have your Slack webhook URL, you can connect it to Base44 in two different ways:

<CardGroup cols={2}>
  <Card icon="sparkle" href="https://docs.base44.com/Integrations/Slack-integration#option-a%3A-ready-made-integration-for-new-apps" title="Option A: Ready-made integration (preferred)">
    * Choose this path if you are starting a new app from scratch.
  </Card>

  <Card icon="bolt" href="https://docs.base44.com/Integrations/Slack-integration#option-b%3A-instant-integration-connecting-slack-to-an-existing-app" title="Option B: Instant integration">
    * Choose this path if you are already in the midst of building and would like to integrate Slack into an existing app.
  </Card>
</CardGroup>

***

### Option A: Ready-made integration (for new apps)

<Steps>
  <Step title="Open the integrations catalog">
    * In Base44 click on Integrations

      <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />
    * Select **Slack**
    * Select **Use this Integration**

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/SlackCatalog.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=b1ba898486c17d838ebdcb378e2b0727" alt="Slack Catalog Pn" width="1869" height="860" data-path="images/SlackCatalog.png" />
  </Step>

  <Step title="Paste your secret">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/SlackWebhookIntegration.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=7bdea82b9adb64802cd47999228a53e3" alt="Slack Webhook Integration Pn" width="1878" height="861" data-path="images/SlackWebhookIntegration.png" />

    * When prompted, paste your `SLACK_WEBHOOK_URL`
  </Step>

  <Step title="Create your app">
    * Type out your first prompt to scaffold the app
    * Sample prompt:

      `Build me a to-do list app "Todo" that will send a message to my Slack channel every time a task is created or the status changes to Done, In Progress, or Deleted.`
  </Step>

  <Step title="Test your app">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/Base44SlackTest.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=747a305a3a27c40b96f24a70ec7ecf29" alt="Base44slack Test Pn" width="1999" height="1609" data-path="images/Base44SlackTest.png" />

    * Creating or updating your tasks should now post a message into your Slack channel
    * If nothing appears, double-check:
      * The webhook belongs to the correct channel
      * The secret is saved correctly
      * Posts are happening from the backend only (not the browser)
  </Step>
</Steps>

***

### Option B: Instant integration (connecting Slack to an existing app)

<Steps>
  <Step title="Open your existing app">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/ToDoListApp.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=22e08d98bb0dedcf86dbc22495e54383" alt="To Do List App Pn" width="1853" height="860" data-path="images/ToDoListApp.png" />

    * Here's the prompt that we typed out in the AI chat to build our sample app: \
      `Build me a to-do list app called Todo`
  </Step>

  <Step stepNumber={2} title="Prompt the AI Chat to connect your app to Slack">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/Base44UpdateSlacksecret.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=e1c3c0f0801662cf38c7b351d3e5d80e" alt="Base44update Slacksecret Pn" width="1885" height="860" data-path="images/Base44UpdateSlacksecret.png" />

    * Sample prompt for the AI Chat:

      `Connect this app to Slack using an Incoming Webhook. Ask me for SLACK_WEBHOOK_URL and save it as a Secret. Post to Slack from the backend only.`
  </Step>

  <Step stepNumber={3} title="Paste your webhook URL">
        <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/SlackWebhookPopup.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=35850648cc954557e140745ab7517e0d" alt="Slack Webhook Popup Pn" width="1866" height="843" data-path="images/SlackWebhookPopup.png" />

    * When prompted by the AI Chat, click on `Update SLACK_WEBHOOK_URL secret`
    * Then paste your webhook URL into the pop up window
  </Step>

  <Step title="Wire the events">
    * Tell the AI chat how you want your app to use Slack
    * Sample prompt:

    `Hook the backend Slack post into the todo lifecycle:`

    `- On create: post "New task: {title}"`

    `- On status change: post "Task status updated: {title} -> {status}"`

    `- On delete: post "Task deleted: {title}"`

    `Use the channel from SLACK_WEBHOOK_URL. If a call fails, show a small toast and continue.`
  </Step>

  <Step title="Test your app">
        <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/Base44SlackTest.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=747a305a3a27c40b96f24a70ec7ecf29" alt="Base44slack Test Pn" width="1999" height="1609" data-path="images/Base44SlackTest.png" />

    * Create a task.
    * Change its status to *In Progress*, then *Done*.
    * You should see the corresponding messages land in your Slack channel.
  </Step>
</Steps>

***

## Troubleshooting

* **No message in Slack** → The webhook might point to a different channel. Create a new one for the right channel.
* **Frontend errors (401 / CORS)** → Don’t call Slack directly from the browser. Always post from the backend.
* **Webhook rotated or revoked** → Paste the new webhook into Base44 Secrets.
* **Workspace blocks custom apps** → Ask a workspace admin to approve your Slack app.

***

## **Common use cases for the Base44 × Slack integration**

This integration is great for keeping your team in the loop without leaving Slack. Some popular patterns include:

* **Task tracking:** Post a message every time a new task is created, updated, or completed in your app.
* **Team notifications:** Send alerts to a shared channel when key events happen—like a status change to *Done*, *In Progress*, or *Blocked*.
* **Error reporting:** Have your backend send a Slack message when something fails (for example, a payment or data sync) so you can react quickly.
* **Daily summaries:** Combine with Zapier or another integration to push a morning digest into Slack, showing todos created or completed yesterday.


Built with [Mintlify](https://mintlify.com).