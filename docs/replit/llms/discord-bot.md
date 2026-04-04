# Source: https://docs.replit.com/getting-started/quickstarts/discord-bot.md

# Create a Discord bot

> Build a fun Discord bot that tells jokes. Learn how to use the Discord API and publish your bot on Replit.

Learn how to create an interactive Discord bot. This guide shows you how to build and publish a bot that responds to commands with jokes.

## What you'll learn

<CardGroup cols={2}>
  <Card title="Discord API" icon="discord">
    Build interactive bot features
  </Card>

  <Card title="Bot Commands" icon="terminal">
    Handle user interactions
  </Card>

  <Card title="Publishing" icon="cloud">
    Host your bot 24/7
  </Card>

  <Card title="Authentication" icon="key">
    Manage bot tokens securely
  </Card>
</CardGroup>

## Create your bot

<Steps>
  <Step title="Fork the template">
    Sign in to Replit and fork the [Discord bot template](https://replit.com/@replit-matt/Discord-Python-Quickstart?v=1#main.py). Select **+ Use Template** and follow the prompts to create your Replit App.
  </Step>

  <Step title="Set up Discord developer portal">
    1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
    2. Navigate to your application's Bot section
    3. Under Build-A-Bot, select **Reset Token**
    4. Copy the token

    <Warning>
      Keep your bot token secret! Never share it or commit it to version control.
    </Warning>
  </Step>

  <Step title="Configure your bot">
    Add your bot token to your Replit App:

    1. Open the Secrets tab
    2. Create a new secret named `DISCORD_BOT_TOKEN`
    3. Paste your bot token as the value

    <Tip>
      Use Replit Secrets to securely store sensitive information like API tokens.
    </Tip>
  </Step>
</Steps>

## Publish your bot

<Steps>
  <Step title="Set up publishing">
    1. Select **Publish** in the workspace header
    2. Choose **Reserved VM** deployment
    3. Select **Publish**
  </Step>

  <Step title="Test">
    1. Invite your bot to a server
    2. Try the `/tell-me-a-joke` command
    3. Verify the bot responds correctly

    <Note>
      Reserved VM deployments ensure your bot stays online continuously.
    </Note>
  </Step>
</Steps>

## Customization options

<CardGroup cols={2}>
  <Card title="Commands">
    * Add new commands - Create custom responses - Handle different events
  </Card>

  <Card title="Features">
    * Add moderation tools - Create games - Integrate with APIs
  </Card>
</CardGroup>

## Next steps

<CardGroup cols={3}>
  <Card title="Databases" icon="database" href="/cloud-services/storage-and-databases/sql-database">
    Add persistent storage
  </Card>

  <Card title="Monitoring" icon="chart-line" href="/category/replit-deployments/">
    Track bot performance
  </Card>

  <Card title="Slash Commands" icon="terminal" href="https://discord.com/developers/docs/interactions/application-commands">
    Add more interactions
  </Card>
</CardGroup>

## Related guides

<CardGroup cols={2}>
  <Card title="Create a Slack bot" icon="slack" href="/getting-started/quickstarts/webscrape-and-slack-notifications">
    Build a Slack integration
  </Card>

  <Card title="Build with AI" icon="wand-magic-sparkles" href="/getting-started/quickstarts/build-with-ai">
    Create apps using Agent
  </Card>
</CardGroup>

<Note>
  Want to learn more about bot development? Check out our [publishing documentation](/category/replit-deployments).
</Note>
