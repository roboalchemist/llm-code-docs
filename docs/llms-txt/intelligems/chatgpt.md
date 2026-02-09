# Source: https://docs.intelligems.io/developer-resources/mcp-server/chatgpt.md

# ChatGPT

{% hint style="warning" %}
Custom Connectors require a ChatGPT Plus, Team, or Enterprise plan. \[[OpenAI Documentation](https://platform.openai.com/docs/guides/developer-mode)]
{% endhint %}

ChatGPT supports MCP servers through Developer Mode. To add the Intelligems MCP Server:

1. Open ChatGPT in your web browser
2. Click your profile name in the sidebar and select Settings
3. Navigate to Apps > Advanced settings

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FjXovmho8WmvResO26iS2%2FScreenshot%202026-01-21%20at%202.42.42%E2%80%AFPM.png?alt=media&#x26;token=66d390ea-0907-4e65-960b-f9fea2e55ccc" alt=""><figcaption></figcaption></figure>

4. Enable Developer mode

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fn8kgwsoYaOSwxHL1cE5J%2FScreenshot%202026-01-21%20at%202.43.38%E2%80%AFPM.png?alt=media&#x26;token=56c2b3ca-dbba-4865-8a81-bf4fb68a5cb9" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Don't see Developer mode? This setting will only appear if you're on a ChatGPT Pro, Plus, Business, Enterprise or Education account. [Link to Documentation](https://platform.openai.com/docs/guides/developer-mode).
{% endhint %}

5. Click Create app

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FrAnbkdkWT4qALQjvy3OL%2FScreenshot%202026-01-21%20at%202.44.19%E2%80%AFPM.png?alt=media&#x26;token=b73d41cd-a132-4a96-a834-bb8b34823611" alt=""><figcaption></figcaption></figure>

6. Configure the connector:
   * **Name:** Intelligems
   * **MCP Server URL:** `https://ai.intelligems.io/mcp`
   * **Authentication:** Select OAuth
   * Check "I understand and want to continue"
7. Click Create and complete the OAuth authorization flow

{% hint style="info" %}
Are you an agency? Complete the OAuth flow using the email address in your Intelligems settings. Located in Settings > General > Personal Settings.
{% endhint %}

**To use in a chat:**

1. Open a new chat
2. Click the + icon in the message bar
3. Select More > Developer Mode
4. Choose Add sources and enable the Intelligems MCP server
