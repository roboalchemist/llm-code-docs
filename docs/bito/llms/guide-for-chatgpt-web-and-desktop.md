# Source: https://docs.bito.ai/ai-architect/guide-for-chatgpt-web-and-desktop.md

# Guide for ChatGPT (Web & Desktop)

Use Bito's [**AI Architect**](https://docs.bito.ai/ai-architect/overview) with **ChatGPT (Web & Desktop)** to enhance your AI-powered coding experience.

Once connected via MCP (Model Context Protocol), ChatGPT can leverage AI Architect's deep contextual understanding of your project, enabling more accurate code suggestions, explanations, and code insights.

{% hint style="info" %}
**Note:** This guide covers setup for both the web interface (chat.openai.com) and the ChatGPT desktop app. The configuration is identical for both platforms.
{% endhint %}

## Prerequisites

1. Follow the [**AI Architect installation instructions**](https://docs.bito.ai/ai-architect/install-ai-architect-self-hosted). Upon successful setup, you will receive a **Bito MCP URL** and **Bito MCP Access Token** that you need to enter in your coding agent.
   * **Note:** When using Bito AI Architect MCP with ChatGPT (Web), the **Bito MCP URL** must be publicly accessible. Localhost or private network URLs (for example, `http://localhost` or internal IP addresses) are not supported and will not work.
2. [Download **BitoAIArchitectGuidelines.md file**](https://github.com/gitbito/ai-architect/blob/main/BitoAIArchitectGuidelines.md). You will need to copy/paste the content from this file later when configuring AI Architect.
   * **Note:** This file contains best practices, usage instructions, and prompting guidelines for the Bito AI Architect MCP server. The setup will work without this file, but including it helps AI tools interact more effectively with the Bito AI Architect MCP server.
3. **A paid ChatGPT subscription** - MCP connectors require one of the following:
   * ChatGPT Plus
   * ChatGPT Pro
   * ChatGPT Team
   * ChatGPT Enterprise
   * ChatGPT Edu

{% hint style="info" %}
**Note:** Free tier accounts do not have access to MCP connectors.
{% endhint %}

{% hint style="info" %}
**Note:** Full MCP support (including write/modify actions) is available for Team, Enterprise, and Edu plans. Plus and Pro users have read/fetch permissions via Developer Mode.
{% endhint %}

## OAuth authentication

ChatGPT uses **OAuth 2.1 with PKCE** for secure MCP server authentication via the Connectors feature in Developer Mode.

**How OAuth authentication works:**

1. You enable Developer Mode and add the MCP server URL in Connectors settings
2. ChatGPT initiates an OAuth flow
3. Your browser opens a consent page hosted by Bito
4. You enter your email and approve the connection
5. ChatGPT receives secure tokens automatically
6. Your email is tracked for usage analytics (collected during OAuth consent)

**Benefits:**

* No manual token management
* Secure browser-based authentication
* Automatic token refresh
* Email collected during consent (no separate header needed)

## Set up AI Architect

{% stepper %}
{% step %}

### Enable Developer mode

1. Go to [chatgpt.com](https://chatgpt.com) (or open the ChatGPT desktop app) and sign in
2. Click on your **profile icon** (bottom-left corner)
3. Select **Settings**
4. Go to **Apps and Connectors** (or just **Connectors**)
5. Scroll down and click **"Advanced Settings"**
6. Toggle **"Developer Mode"** to ON
   {% endstep %}

{% step %}

### Create Bito AI Architect Connector

1. In the **Connectors** section, click **"Create"** or **"+ Add Connector"**
2. Fill in the connector details:
   * **Connector Name:** BitoAIArchitect
   * **Description:** Repository intelligence and architecture analysis for your organization
   * **MCP Server URL:** `<Your-Bito-MCP-URL>`
   * **Authentication:** Select **"OAuth"**

{% hint style="info" %}
**Note:**

* Replace `<Your-Bito-MCP-URL>` with the **Bito MCP URL** you received after completing the AI Architect setup.
  * For the Bito-hosted AI Architect, use the following URL format: `https://mcp.bito.ai/<Your-Bito-Workspace-ID>/mcp`

    Replace `<Your-Bito-Workspace-ID>` with your actual Bito workspace ID, which you can find after logging into your Bito account at [**alpha.bito.ai**](https://alpha.bito.ai/)
    {% endhint %}

3. Click **"Create"** or **"Save"**
   {% endstep %}

{% step %}

### Complete OAuth authorization

1. Click on the newly created BitoAIArchitect connector
2. Click **"Connect"** to initiate the OAuth flow
3. A browser window opens showing the **Bito Authorization** page
4. Review the requested permissions
5. **Enter your email address** (required for tracking)
6. Click **"Authorize"** or **"Allow"**
7. Return to ChatGPT - the connection is now active
   {% endstep %}

{% step %}

### Verify connection

1. Return to ChatGPT Settings → Connectors
2. BitoAIArchitect should show as **"Connected"**
3. Start a new conversation
4. In the composer, click **"Use Connectors"** or look for the connector tools
5. Try asking:

   ```
   What repositories are available in my organization?
   ```

{% endstep %}

{% step %}

### Using Bito AI Architect in ChatGPT

Once connected, you can use **BitoAIArchitect** in several ways:

* **Direct prompts:** Ask questions about your repositories
* **Deep Research:** BitoAIArchitect tools appear in "Deep Research" mode
* **Connectors menu:** Select BitoAIArchitect from the "Use Connectors" option
  {% endstep %}
  {% endstepper %}

## Troubleshooting ChatGPT

#### **"Connectors" or Developer Mode option not visible:**

* Verify you have a paid ChatGPT subscription (Plus, Pro, Team, Enterprise, or Edu)
* Free tier accounts do not have connector access
* The feature may be rolling out gradually - check back later if recently subscribed

#### **OAuth authorization fails:**

* Ensure pop-ups are allowed for chatgpt.com
* Check that your Workspace ID is correct
* Verify your organization has OAuth enabled for the MCP server
* Try using an incognito/private browser window

#### **"Error fetching OAuth configuration":**

* Verify the MCP server URL is correct and accessible
* Ensure the server supports OAuth 2.1 with dynamic client registration
* Check that `code_challenge_methods_supported` includes `S256` in the authorization server metadata

#### **Connection shows "Error" or "Disconnected":**

* Click the connection and select "Reconnect"
* OAuth tokens may have expired - re-authorize when prompted
* Check if your Bito workspace is still active

#### **Tools not working in conversation:**

* Ensure the MCP connection shows "Connected" status
* Try starting a fresh conversation
* Explicitly mention "use BitoAIArchitect" in your prompt if tools don't activate automatically
* Check that you're using the connector in a mode that supports tools (not all chat modes do)
