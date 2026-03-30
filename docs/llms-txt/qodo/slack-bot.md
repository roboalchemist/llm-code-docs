# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/slack-bot.md

# Slack Bot

This guide will help you set up the Qodo Slack Bot with support for both **HTTP Webhook** and **Socket Mode** approaches.

### Choose Your Mode

Qodo CLI tool supports two communication modes with Slack:

* **HTTP Webhook Mode** (default): Requires a public endpoint, best for production
* **Socket Mode**: Works behind firewalls, great for development and enterprise environments

| Feature                      | HTTP Webhook       | Socket Mode                 |
| ---------------------------- | ------------------ | --------------------------- |
| Public endpoint required     | ✅ Yes              | ❌ No                        |
| Works behind firewalls       | ❌ No               | ✅ Yes                       |
| Slack Marketplace compatible | ✅ Yes              | ❌ No                        |
| Scalability                  | ✅ Excellent        | ⚠️ Limited (10 connections) |
| Local development            | ⚠️ Needs tunneling | ✅ Direct                    |

### Prerequisites

1. A Slack workspace where you have permission to install apps
2. A Qodo API key (get one from [Qodo Dashboard](https://app.qodo.ai))
3. Node.js and the Qodo CLI installed

### Step 1: Create a Slack App

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Click "Create New App"
3. Choose "From scratch"
4. Enter your app name (e.g., "Qodo Bot")
5. Select your workspace
6. Click "Create App"

### Step 2: Configure OAuth & Permissions

1. In your app settings, go to "OAuth & Permissions"
2. Scroll down to "Scopes" → "Bot Token Scopes"
3. Add the following scopes:
   * `chat:write` - Send messages
   * `chat:write.public` - Send messages to channels the bot isn't in
   * `reactions:write` - Add reactions to messages
   * `channels:read` - Read channel information
   * `groups:read` - Read private channel information
   * `im:read` - Read direct message information
   * `mpim:read` - Read group direct message information
4. Scroll up and click "Install to Workspace"
5. Authorize the app
6. Copy the "Bot User OAuth Token" (starts with `xoxb-`)

### Step 3A: Configure Event Subscriptions (HTTP Webhook Mode)

**Skip this step if you're using Socket Mode**

1. Go to "Event Subscriptions" in your app settings
2. Turn on "Enable Events"
3. Set the Request URL to: `http://your-server.com/slack/events`
   * For local development: `http://localhost:4444/slack/events` (default port)
   * For custom port: `http://localhost:YOUR_PORT/slack/events`
   * For production: Use your actual server URL with HTTPS
4. Under "Subscribe to bot events", add:
   * `app_mention` - When your bot is mentioned
   * `message.channels` - Messages in public channels
   * `message.groups` - Messages in private channels
   * `message.im` - Direct messages
   * `message.mpim` - Group direct messages
5. Click "Save Changes"

### Step 3B: Configure Socket Mode (Socket Mode Only)

**Skip this step if you're using HTTP Webhook Mode**

1. Go to "Socket Mode" in your app settings
2. Toggle "Enable Socket Mode" to ON
3. Go to "Event Subscriptions" in your app settings
4. Turn on "Enable Events" (no Request URL needed for Socket Mode)
5. Under "Subscribe to bot events", add:
   * `app_mention` - When your bot is mentioned
   * `message.channels` - Messages in public channels
   * `message.groups` - Messages in private channels
   * `message.im` - Direct messages
   * `message.mpim` - Group direct messages
6. Click "Save Changes"

### Step 4A: Get Your Signing Secret (HTTP Webhook Mode Only)

**Skip this step if you're using Socket Mode**

1. Go to "Basic Information" in your app settings
2. Under "App Credentials", find "Signing Secret"
3. Click "Show" and copy the secret

### Step 4B: Generate App-Level Token (Socket Mode Only)

**Skip this step if you're using HTTP Webhook Mode**

1. Go to "Basic Information" in your app settings
2. Scroll down to "App-Level Tokens"
3. Click "Generate Token and Scopes"
4. Enter a token name (e.g., "socket-mode-token")
5. Add the scope: `connections:write`
6. Click "Generate"
7. Copy the token (starts with `xapp-`)

### Step 5: Configure Environment Variables

1. Copy the example environment file:

   ```bash
   cp .env.slack.example .env
   ```
2. Edit `.env` and fill in your values based on your chosen mode:

#### For HTTP Webhook Mode (default):

```bash
SLACK_BOT_TOKEN=xoxb-your-actual-bot-token
SLACK_SIGNING_SECRET=your-actual-signing-secret
SLACK_BOT_USER_ID=U1234567890  # Optional but recommended
QODO_API_KEY=your-qodo-api-key
# SLACK_USE_SOCKET_MODE=false  # This is the default
```

#### For Socket Mode:

```bash
SLACK_BOT_TOKEN=xoxb-your-actual-bot-token
SLACK_APP_TOKEN=xapp-your-actual-app-token
SLACK_USE_SOCKET_MODE=true
SLACK_BOT_USER_ID=U1234567890  # Optional but recommended
QODO_API_KEY=your-qodo-api-key
# No SLACK_SIGNING_SECRET needed for Socket Mode
```

### Step 6: Find Your Bot User ID (Optional but Recommended)

1. In your Slack workspace, mention your bot: `@YourBotName`
2. Right-click on the bot mention and select "Copy link"
3. The link will contain the user ID: `https://yourworkspace.slack.com/team/U1234567890`
4. Copy the `U1234567890` part to your `.env` file

### Step 7: Test Your Setup

1. Start the Slack bot:

   ```bash
   qodo --slack
   ```

   Or with a custom port:

   ```bash
   qodo --slack --port 3000
   ```
2. You should see different output depending on your mode:

   **HTTP Webhook Mode:**

   ```
   🚀 Starting Slack Bot...
   📡 Using HTTP Webhook (webhook mode)
   🔗 Slack event handler listening on port 4444
   📡 Webhook URL: http://localhost:4444/slack/events
   ✅ Slack Bot is running and listening for events
   🌐 Webhook Mode: Ensure your endpoint is publicly accessible
   ```

   **Socket Mode:**

   ```
   🚀 Starting Slack Bot...
   📡 Using Socket Mode (socket mode)
   🚀 Starting Slack Socket Mode connection...
   ✅ Socket Mode connected to Slack
   🔗 Socket Mode handler started successfully
   ✅ Slack Bot is running and listening for events
   🔌 Socket Mode: No public endpoint required
   ```
3. In Slack, mention your bot:

   ```
   @YourBotName help
   ```
4. The bot should respond with available commands.

### Step 8: Configure Your Agent Commands

Create an agent configuration file (e.g., `agent.toml`):

```toml
[commands.review]
description = "Review code for issues and improvements"
instructions = "Please review the provided code for potential issues, bugs, and improvements."

[commands.test]
description = "Generate or run tests"
instructions = "Help with testing - generate test cases or run existing tests."

[commands.deploy]
description = "Help with deployment tasks"
instructions = "Assist with deployment processes and configurations."
```

Then start the bot with your agent file:

```bash
qodo --slack --agentFile=agent.toml
```

### Switching Between Modes

You can easily switch between HTTP Webhook and Socket Mode by changing your environment variables:

#### Switch to Socket Mode:

```bash
# Add these to your .env file
SLACK_USE_SOCKET_MODE=true
SLACK_APP_TOKEN=xapp-your-app-token
# Remove or comment out SLACK_SIGNING_SECRET
```

#### Switch to HTTP Webhook Mode:

```bash
# Remove or comment out these from your .env file
# SLACK_USE_SOCKET_MODE=true
# SLACK_APP_TOKEN=xapp-your-app-token
# Add back SLACK_SIGNING_SECRET
SLACK_SIGNING_SECRET=your-signing-secret
```

Restart the bot after making changes.

### Troubleshooting

#### Bot Not Responding

**For HTTP Webhook Mode:**

* Check that your webhook URL is accessible from the internet
* Verify your bot token and signing secret are correct
* Ensure your Slack app's Request URL is set correctly

**For Socket Mode:**

* Verify your bot token and app-level token are correct
* Check that Socket Mode is enabled in your Slack app settings
* Ensure your app-level token has `connections:write` scope

**For Both Modes:**

* Check the bot has the required OAuth scopes
* Make sure the bot is invited to the channel
* Verify the bot is mentioned correctly (e.g., `@YourBotName`)

#### Environment Variable Errors

**"SLACK\_SIGNING\_SECRET is required":**

* You're in HTTP Webhook mode but missing the signing secret
* Either add the signing secret or switch to Socket Mode

**"SLACK\_APP\_TOKEN is required":**

* You're in Socket Mode but missing the app-level token
* Either add the app-level token or switch to HTTP Webhook mode

#### "Unknown command" Errors

* Ensure your agent configuration file is loaded
* Check that command names match exactly
* Verify the agent file syntax is correct

#### Permission Errors

* Make sure the bot has the required OAuth scopes
* Check that the bot is invited to channels where you're trying to use it
* Verify your Qodo API key is valid

#### Local Development

For local development, you'll need to expose your local server to the internet so Slack can send events to it. You can use tools like:

* [ngrok](https://ngrok.com/): `ngrok http 3000`
* [localtunnel](https://localtunnel.github.io/www/): `lt --port 4444`

Update your Slack app's Request URL with the public URL provided by these tools.

### Production Deployment

For production:

1. Deploy your bot to a server with a public HTTPS URL
2. Update the Request URL in your Slack app settings
3. Set environment variables on your server
4. Ensure your server can handle Slack's event delivery requirements
5. Consider using a process manager like PM2 to keep the bot running

### Usage Examples

Once set up, you can use the bot like this:

```
@YourBotName review this pull request
@YourBotName test the authentication module
@YourBotName deploy to staging with extra logging
@YourBotName help
```

The bot maintains separate conversation sessions per thread, so you can have multiple ongoing conversations.
