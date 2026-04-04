# Source: https://jam.dev/docs/debug-a-jam/mcp.md

# MCP

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fry7sdmxcTVw3WZoMYff1%2Fimage.png?alt=media&#x26;token=a800886e-5217-443b-80f2-e823182a5feb" alt=""><figcaption></figcaption></figure>

### Overview&#x20;

Jam MCP (Model Context Protocol) lets your developer tools and AI agents open a [Jam recording](https://jam.dev/docs/get-started/welcome-to-jam) and automatically load its data into context (video, user events, console logs, errors and network requests). As a developer, you’ll debug faster without hand-typing steps to reproduce, copy-pasting stack traces, or screen-sharing.

Your AI models and agents can use Jam’s MCP server to access your Jam recordings and their data in a simple and secure way.&#x20;

Paste an existing Jam link into supported MCP clients like VS Code, Cursor, Windsurf, or Claude Code, and the Jam's context appears right where you’re working.&#x20;

### Prerequisites

<details>

<summary>Record a Jam first</summary>

1. [Install](https://chromewebstore.google.com/detail/jam/iohjgamcilhbgmhbnllfolmkmmekfmci) the **Jam** Chrome extension.
2. Hit **Record** to capture your screen and voice.
3. Stop the recording, and your Jam link is ready for an agent to consume via MCP.

</details>

### 1. Configure

<details>

<summary>ChatGPT</summary>

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FkreA2swop1AL4Yd3YW9K%2FJamChatGPT-connector.gif?alt=media&#x26;token=45277eb5-7491-4d9d-9ae4-804ba09e79c6" alt=""><figcaption></figcaption></figure>

**Steps:**

1. From the home page go to **Settings**
2. Click **Apps &** **Connectors**&#x20;
3. Select **Jam** and click the **Connect** button
4. Sign in to Jam and allow access to your workspace

</details>

<details>

<summary>Claude Desktop</summary>

<div data-full-width="true"><figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FRYaPU7i4WX1SbVWR91Du%2FClaude%20MCP.gif?alt=media&#x26;token=e6011757-7fdb-42cb-9c1f-08b184b528c2" alt=""><figcaption></figcaption></figure></div>

\
**Steps:**

1. From the home page click  <i class="fa-sliders-simple">:sliders-simple:</i>  **search and tools** on web or desktop
2. Click **+Add connectors**&#x20;
3. Find **Jam** in the Connector Directory and click the  <i class="fa-plus">:plus:</i>  button to connect
4. Sign in to Jam and **pick the workspace** Claude should access

</details>

<details>

<summary>Claude Code</summary>

**Steps:**

1. Install [Claude Code in your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
2. In your terminal run

```bash
claude mcp add Jam https://mcp.jam.dev/mcp -t http -s user
```

</details>

<details>

<summary>Cursor</summary>

<a href="cursor://anysphere.cursor-deeplink/mcp/install?name=jam&#x26;config=eyJ1cmwiOiJodHRwczovL21jcC5qYW0uZGV2L21jcCJ9" class="button primary" data-icon="square-terminal">Add to cursor</a>

***

```json
{
  "mcpServers": {
    "jam": {
      "url": "https://mcp.jam.dev/mcp"
    }
  }
}
```

Once you make the above changes, make sure to restart Cursor to use Jam.

</details>

<details>

<summary>Visual Studio Code</summary>

1. <kbd>CTRL/CMDP</kbd> + <kbd>P</kbd> and enter `>MCP: Add Server`
2. Select **HTTP (HTTP or Server-Sent Events)**
3. Enter `https://mcp.jam.dev/mcp`&#x20;
4. Enter `Jam`&#x20;
5. Your `mcp.json` file should look like this:&#x20;

```json
{
  "servers": {
    "Jam": {
      "url": "https://mcp.jam.dev/mcp",
      "type": "http"
      
    }
  }
}
```

</details>

<details>

<summary>Windsurf</summary>

1. <kbd>CTRL/CMDP</kbd> + <kbd>P</kbd> and enter `>MCP: Add Server`
2. Select **HTTP (Server-Sent Events)**
3. Enter `https://mcp.jam.dev/mcp`&#x20;
4. Enter `Jam`&#x20;
5. Your `mcp.json` file should look like this:&#x20;

```json
{
    "mcp": {
        "servers": {
            "Jam": {
                "type": "http",
                "url": "https://mcp.jam.dev/mcp"
            }
        }
    }
}
```

</details>

<details>

<summary>OpenCode</summary>

1. Edit your `opencode.json`:&#x20;

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "jam": {
      "type": "remote",
      "url": "https://mcp.jam.dev/mcp"
    }
  }
}
```

2. Run `opencode mcp auth jam` to start oauth2 authorization flow

</details>

{% hint style="info" %}
Jam MCP is backwards compatible with the deprecated [HTTP+SSE transport](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse)&#x20;
{% endhint %}

### 2. Getting Started

Once you have configured your MCP:

1. Copy one or multiple Jam links
2. Prompt your agent and paste the Jam link. \
   \&#xNAN;*See our* [*prompt tips*](#id-4.-tips) *and examples below*
3. Authenticate your IDE with Jam
4. Approve any of the tool requests the agent makes

### 3. Available Features in Jam MCP

**Tools**

| Tool name                                                                     | Description                                                                                        |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| <i class="fa-comments">:comments:</i>  **getDetails**                         | Get a quick snapshot of the Jam. Who made it, what happened, and which other tools to try next.    |
| <i class="fa-rectangle-terminal">:rectangle-terminal:</i>  **getConsoleLogs** | Grab the console logs from the Jam                                                                 |
| <i class="fa-network-wired">:network-wired:</i>  **getNetworkRequests**       | List every web request from the Jam as JSON, trimmed to the essentials for fast debugging.         |
| <i class="fa-camera-viewfinder">:camera-viewfinder:</i>  **getScreenshot**    | Get every screenshot from a screenshot Jam so you can inspect                                      |
| <i class="fa-arrow-pointer">:arrow-pointer:</i>  **getUserEvents**            | Read each click, input and page navigation change in plain language.                               |
| <i class="fa-video">:video:</i>  **analyzeVideo**                             | Analyzes Jam video recordings to extract insights, detect issues, and provide structured feedback. |

### 4. Tips

Prompting tips:

1. Use Jam MCP to help with bug analysis, product feedback, and give agents context to debug issues.
2. Be as specific as you would with another engineer for the best results
3. Start with small features or bug fixes, tell your Agent to propose a plan using Jam MCP, and verify its plan before moving on to suggested edits

### 5. Examples

Examples of how the team at Jam uses Jam MCP:

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fry7sdmxcTVw3WZoMYff1%2Fimage.png?alt=media&#x26;token=a800886e-5217-443b-80f2-e823182a5feb" alt=""><figcaption></figcaption></figure>

**Tomasz (Product Engineer)** Uses Jam MCP to debug issues, by providing the context of a bug to Cursor, to ship a fix.

{% code title="Prompt" overflow="wrap" %}

```
Review this Jam <Jam Link Placeholder> and analyze the problem, cross-reference it with the existing codebase, and prepare a detailed plan for implementation.
```

{% endcode %}

<details>

<summary>Stack used</summary>

* Jam (recordings)
* Jam MCP
* [Cursor](https://cursor.com/agents)

</details>

***

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FKMAVyzXlQBAvvTECtXUO%2Fimage.png?alt=media&#x26;token=b7fe7039-9cf6-49e8-8119-02ae58a25ad5" alt=""><figcaption></figcaption></figure>

**Frits (Product Manager)** let’s Claude review and analyze customer Jams to spot common issues and patterns. Claude turns the findings into neatly grouped Linear tickets.

{% code title="Prompt" overflow="wrap" %}

```
Analyze these Jams, perform root-cause analysis, and organize them into efficient work packages to minimize engineers’ context switching; create Linear tickets from the analysis. 

<Jam Link Placeholder>
```

{% endcode %}

<details>

<summary>Stack used</summary>

* Jam (customer recordings)
* Jam MCP
* [Claude Desktop](https://www.notion.so/Jam-MCP-Docs-Early-Access-207f727817b9802abfaacf9064c14fe7?pvs=21) (analysis & ticket drafting)
* [Linear MCP](https://linear.app/docs/mcp) (issue creation)

</details>

***

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FmEzDZHbEmzQeiVo7gWGl%2Fimage.png?alt=media&#x26;token=ad1de41e-8362-4edd-87fa-2bb9f4002120" alt=""><figcaption></figcaption></figure>

\
**Martin (Product Designer)** records product and design feedback with the Jam extension. Jam MCP provides the context for Claude Code to plan and ship a ready-to-review PR with the implemented Feedback.

{% code title="Prompt" overflow="wrap" %}

```
I recorded product feedback in a Jam. Create an implementation plan for the changes requested in this Jam:

<Jam Link Placeholder>
```

{% endcode %}

<details>

<summary>Stack used</summary>

* Jam (recording via [extension](https://chromewebstore.google.com/detail/jam/iohjgamcilhbgmhbnllfolmkmmekfmci))
* Jam MCP
* [Claude Code](https://www.anthropic.com/claude-code) inside of Cursor

</details>

***

### 6. Feedback

Got an idea that would make Jam MCP faster, smarter or more useful? Drop it in the form below (30 seconds, tops).

<a href="https://jamdotdev.notion.site/207f727817b980c0a430fddd7ed2092a?pvs=105" class="button primary" data-icon="arrow-up-right">Request a feature</a>

***

### FAQ

<details>

<summary>Can I use MCP without the Chrome extension?</summary>

Yes. You only need an existing Jam link. Anyone (you, your team, or a customer) can record a Jam. If you want to record and [create new Jams](https://jam.dev/docs/get-started/creating-a-jam), install the Chrome extension or use our iOS app.

</details>

<details>

<summary>Can I paste multiple Jam links at once?</summary>

**Yes.** You can paste more than one link, but we recommend **one Jam at a time** so your agent doesn’t hit context window limits.

</details>

<details>

<summary>How do I review or revoke tools that can access Jam via MCP?</summary>

Go to **Settings → Integrations → AI Agents** to see connected tools. Select a tool to **revoke** or **disconnect** access at any time.

<figure><img src="https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FbzISnmIbLDR0hk6JAoJH%2Fimage.png?alt=media&#x26;token=2442ce11-7865-4a1a-8efb-9b2ac5ab8d0b" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Does Jam MCP send my Jam data to third parties?</summary>

Some MCP tools use Google’s Gemini. We **opt out of training** on Jam customer data and take steps to de-identify it. See our[ AI Policies](https://jam.dev/docs/company/ai-policy) for more details.

</details>

<details>

<summary>Does MCP work the same with Instant Replay Jams?</summary>

Not exactly. getScreenshot and videoAnalysis are **not** available for Instant Replay Jams. Other MCP tools still work and return data/context.

</details>

<details>

<summary>How can admins control what MCP can access?</summary>

MCP mirrors your existing Jam permissions. It doesn’t grant new access. Use your normal admin controls for [members and roles,](https://jam.dev/docs/administration/members-and-roles) or [SSO](https://jam.dev/docs/administration/sso) in workspace settings. Nothing is exposed via MCP that a user couldn’t already see in the Jam web or mobile apps.

</details>
