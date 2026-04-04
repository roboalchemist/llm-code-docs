# Source: https://docs.replit.com/getting-started/quickstarts/webscrape-and-slack-notifications.md

# Create a HackerNews Slack bot

> Build a bot that scrapes HackerNews and sends updates to Slack. Learn how to use Scheduled Deployments and integrate with external services.

Learn how to create a bot that monitors HackerNews and sends notifications to Slack. This guide shows you how to use Scheduled Deployments and external APIs.

## What you'll learn

<CardGroup cols={2}>
  <Card title="Web Scraping" icon="spider-web">
    Fetch data from HackerNews
  </Card>

  <Card title="Slack Integration" icon="slack">
    Send notifications to Slack channels
  </Card>

  <Card title="Scheduling" icon="clock">
    Configure automated publishing
  </Card>

  <Card title="API Usage" icon="code">
    Work with external services
  </Card>
</CardGroup>

## Create your bot

<Steps>
  <Step title="Fork the template">
    Sign in to Replit and fork the [HackerNews webscraper template](https://replit.com/@replit-matt/Hacker-News-Alert-Slackbot?v=1#app.py). Select **+ Use Template** and follow the prompts to create your Replit App.
  </Step>

  <Step title="Create a Slack app">
    1. Go to [Slack Apps](https://api.slack.com/apps) and select **Create an App**
    2. Choose **From an app manifest**
    3. Select your workspace

    4) Replace the manifest with [this JSON](https://replit.com/@replit-matt/Hacker-News-Alert-Slackbot?v=1#manifest.json)

    (/\* vale on \*/}

    5. Review and select **Create**
    6. Select **Install the App**

    <Note>
      You may need administrator approval based on your organization's policies.
    </Note>
  </Step>

  <Step title="Configure tokens">
    Add these secrets to your Replit App's **Secrets** tab:

    1. **SLACK\_BOT\_TOKEN**

       * Go to Settings > Install App
       * Copy the **Bot User OAuth Token**

    2. **SLACK\_SIGNING\_SECRET**

       * Go to Settings > Basic Information
       * Copy the **Signing Secret** from App Credentials

    3. **SLACK\_APP\_TOKEN**
       * Go to Settings > Basic Information
       * Under App-Level Tokens, select **Generate Token and Scopes**
       * Add permissions and generate token
  </Step>

  <Step title="Customize your bot">
    Update `app.py` with your preferences:

    ```python  theme={null}
    KEYWORDS = ["h"]  # Terms to search for
    ALERT_UIDS = ["U06C34217C5"]  # Your Slack member ID
    NUM_TOP_STORIES = 25  # Number of stories to check
    ```

    <Tip>
      Get your Slack member ID from your profile settings under the ellipsis menu.
    </Tip>
  </Step>
</Steps>

## Publish with scheduling

<Steps>
  <Step title="Start publishing">
    Select **Publish** in the workspace header.
  </Step>

  <Step title="Configure schedule">
    1. Choose [Scheduled
       Deployments](/cloud-services/deployments/scheduled-deployments) 2. Set your
       preferred schedule 3. Select **Publish**
  </Step>

  <Step title="Monitor">
    Your bot will now run automatically according to your schedule.
  </Step>
</Steps>

## Customization options

<CardGroup cols={2}>
  <Card title="Enhance filtering">
    * Add more keywords - Refine matching criteria - Customize scoring
  </Card>

  <Card title="Improve notifications">
    * Format messages - Add rich previews - Include metadata
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="AI Integration" icon="robot" href="/getting-started/quickstarts/ai-slack-channel-summarizer">
    Add AI summaries to notifications
  </Card>

  <Card title="Deployments" icon="cloud" href="/cloud-services/deployments/scheduled-deployments">
    Learn more about scheduling
  </Card>

  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database/">
    Store historical data
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a Slack summarizer" icon="slack" href="/getting-started/quickstarts/ai-slack-channel-summarizer">
    Build a bot that summarizes Slack channels
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent and Assistant
  </Card>
</CardGroup>

<Note>
  Want to learn more about publishing? Check out our [publishing documentation](/category/replit-deployments).
</Note>
