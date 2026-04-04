# Source: https://docs.bito.ai/ai-architect/guide-for-claude.ai-web.md

# Guide for Claude.ai (Web)

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **Claude.ai (Web)** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), Claude.ai can leverage AI Architect's deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
   * **Note:** The **Bito MCP URL** must be publicly accessible. Localhost or private network URLs (for example, `http://localhost` or internal IP addresses) are not supported and will not work.
2. [Download **BitoAIArchitectGuidelines.md file**](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.
3. **A paid Claude.ai subscription** - MCP integrations require one of the following:
   * Claude Pro
   * Claude Max
   * Claude Team
   * Claude Enterprise

{% hint style="info" %}
**Note:** Free tier accounts do not have access to MCP Integrations.
{% endhint %}

## OAuth authentication

Claude.ai uses **OAuth 2.1 with PKCE** for secure authentication, so you don't need to manually manage access tokens. Your email will be collected during the OAuth consent flow for tracking purposes.

**How OAuth authentication works:**

1. You add the MCP server URL in Claude.ai Integrations settings
2. Claude.ai initiates an OAuth flow
3. Your browser opens a consent page hosted by Bito
4. You enter your email and approve the connection
5. Claude.ai receives secure tokens automatically
6. Your email is tracked for usage analytics (collected during OAuth consent)

**Benefits:**

* No manual token management
* Secure browser-based authentication
* Automatic token refresh
* Email collected during consent (no separate header needed)

**OAuth Callback URL:** `https://claude.ai/api/mcp/auth_callback`

## Set up AI Architect

{% stepper %}
{% step %}

### Open Claude.ai integrations

1. Go to [claude.ai](https://claude.ai) and sign in with your paid account
2. Click on your **profile icon** (bottom-left corner)
3. Select **Settings**
4. Navigate to **Integrations** section
   {% endstep %}

{% step %}

### Add Bito AI Architect MCP server

1. Click **"+ Add Custom Integration"**
2. Enter the integration details:
   * **Name:** BitoAIArchitect
   * **URL:** `<Your-Bito-MCP-URL>`

{% hint style="info" %}

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
    {% endhint %}

3. Click **"Connect"** or **"Add"**
   {% endstep %}

{% step %}

### Complete OAuth authorization

1. A new browser window/tab will open showing the **Bito Authorization** page
2. Review the requested permissions
3. **Enter your email address** (required for tracking/identification)
4. Click **"Authorize"** or **"Allow"**
5. The window will close and you'll be returned to Claude.ai
   {% endstep %}

{% step %}

### Verify connection

1. Return to Claude.ai Settings → Integrations
2. BitoAIArchitect should show as **"Connected"** with a green indicator
3. Start a new conversation and try:

   ```
   What repositories are available in my organization?
   ```

{% endstep %}
{% endstepper %}

## Troubleshooting Claude.ai

#### **"Integrations" option not visible:**

* Verify you have a paid Claude subscription (Pro, Max, Team, or Enterprise)
* Free tier accounts do not have MCP access
* Contact Anthropic support if you have a paid plan but don't see the option

#### **OAuth authorization fails:**

* Ensure pop-ups are allowed for claude.ai
* Check that your Workspace ID is correct
* Verify your organization has OAuth enabled for the MCP server
* Try clearing browser cache and cookies, then retry

#### **Connection shows "Disconnected":**

* Click the server entry and select "Reconnect"
* OAuth tokens may have expired - re-authorize when prompted
* Check if your Bito workspace is still active

#### **Tools not appearing in conversation:**

* Ensure the MCP server shows "Connected" status
* Try starting a fresh conversation
* Some tools may require specific prompts to activate
