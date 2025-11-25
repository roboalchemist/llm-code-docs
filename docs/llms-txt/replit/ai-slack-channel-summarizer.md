# Source: https://docs.replit.com/getting-started/quickstarts/ai-slack-channel-summarizer.md

# Create a Slack channel summarizer

> Build a Slack bot that summarizes channel activity using GPT-4. Learn how to integrate AI with Slack's API.

Turn your Slack conversations into concise summaries with AI. This guide shows you how to create a bot that summarizes channel activity using GPT-4.

## Features

<CardGroup cols={2}>
  <Card title="Channel Summaries" icon="message-bot">
    Summarize Slack channel activity for any time period
  </Card>

  <Card title="GPT-4 Integration" icon="brain-circuit">
    Generate intelligent, context-aware summaries using OpenAI's GPT-4
  </Card>
</CardGroup>

## Create your summarizer

<Steps>
  <Step title="Fork the template">
    1. Sign in to Replit
    2. Navigate to the [AI Slack summary template](https://replit.com/@replit-matt/Slack-Channel-Summary-Bot)
    3. Select **+ Use Template** in the upper-right corner
    4. Follow the prompts to create your Replit App
  </Step>

  <Step title="Create a Slack app">
    1. Go to the [Slack Apps page](https://api.slack.com/apps)
    2. Select **Create an App**
    3. Choose **From an app manifest**
    4. Select your workspace from the dropdown
    5. Replace the manifest content with the [manifest.json](https://replit.com/@replit-matt/Slack-Channel-Summary-Bot#assets/manifest.json) file
    6. Review the configuration and select **Create**
    7. Select **Install the App**

    <Note>
      You may need administrator approval to install the app depending on your organization's settings.
    </Note>
  </Step>

  <Step title="Configure your tokens">
    Add the following secrets to your Replit App's **Secrets** tab:

    1. **SLACK\_BOT\_TOKEN**
       * Navigate to Settings > Install App in your Slack App
       * Copy the **Bot User OAuth Token**

    2. **SLACK\_SIGNING\_SECRET**
       * Go to Settings > Basic Information
       * Copy the **Signing Secret** from App Credentials

    3. **SLACK\_APP\_TOKEN**
       * Go to Settings > Basic Information
       * Under App-Level Tokens, select **Generate Token and Scopes**
       * Add a token name and select permissions
       * Copy the generated token

    4. **OPENAI\_API\_KEY**
       * Get your API key from OpenAI's platform
  </Step>

  <Step title="Publish your bot">
    1. Select **Publish** in the Workspace header
    2. Choose **Reserved VM Deployments**
    3. Select **Set up your published app**
    4. Select **Publish**
  </Step>
</Steps>

## Using your summarizer

Add your bot to a channel and send it a direct message with the following command:

```bash  theme={null}
/summarize-channel #channel-name duration
```

For example, to summarize the last 24 hours of activity in #general:

```bash  theme={null}
/summarize-channel #general 24
```

## Customization options

<AccordionGroup>
  <Accordion title="Summarization criteria">
    Customize your summaries by modifying the prompt to focus on specific
    keywords or topics.
  </Accordion>

  <Accordion title="Platform integrations">
    Extend functionality by connecting with additional platforms and services.
  </Accordion>

  <Accordion title="Alert messages">
    Customize the format and content of Slack alert messages.
  </Accordion>

  <Accordion title="Summary frequency">
    Configure different summarization intervals for channels or topics.
  </Accordion>
</AccordionGroup>
