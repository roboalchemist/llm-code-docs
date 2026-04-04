# Source: https://docs.xano.com/getting-started-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI-Assisted Development

> Use Claude Code with the Xano Developer MCP and the Xano CLI to build your backend with AI.

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

The following guide walks you through setting up an AI-powered [XanoScript](xanoscript/introduction) development workflow using **Claude Code**, the **Xano Developer MCP**, and the **Xano CLI**.

**Prerequisites:** [Node.js](https://nodejs.org/) 18+, and [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed.

<Note>
  We're actively working on support for other development platforms, such as Cursor and Codex. Check back soon!
</Note>

<Steps>
  <Step title="Install the Xano CLI">
    Install the [Xano CLI](/xano-cli/get-started) globally:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      npm install -g @xano/cli
      ```
    </BrowserFrame>

    Then authenticate and pull your workspace:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano auth
      xano workspace pull ./my-workspace
      ```
    </BrowserFrame>

    This creates a `my-workspace` folder in your current directory and downloads your workspace into it. You can also pull into the current folder with `xano workspace pull .`

    See the [CLI Get Started](/xano-cli/get-started) guide for full details.
  </Step>

  <Step title="Install the Developer MCP">
    The [Developer MCP](/developer-mcp/get-started) gives AI tools direct access to XanoScript documentation and real-time code validation, significantly improving AI-generated XanoScript quality.

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      claude mcp add xano -- npx -y @xano/developer-mcp
      ```
    </BrowserFrame>

    <Tip>
      Not using Claude Code? See the [Developer MCP guide](/developer-mcp/get-started) for setup instructions for Cursor, Windsurf, VS Code Copilot, and other AI tools.
    </Tip>
  </Step>

  <Step title="Ask Claude Code to make a change">
    Open your workspace folder in VS Code, launch Claude Code, and ask it to make a change. For example:

    > Add a step to the auth/signup endpoint that sends a welcome email after a successful registration.

    Claude Code will read your existing XanoScript, plan the change, and write the updated code — with the Developer MCP providing documentation and validation along the way.
  </Step>

  <Step title="Sync to Xano">
    Push your changes back to Xano using the CLI:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace push
      ```
    </BrowserFrame>

    <Info>
      <Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_light.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=7304b7cb9606506e332ca0504388559e" size={20} width="1024" height="1024" data-path="images/icons/GitHub_light.svg" /><Icon icon="https://mintcdn.com/xano-997cb9ee/How4y2-NUVnTIPUm/images/icons/GitHub_dark.svg?fit=max&auto=format&n=How4y2-NUVnTIPUm&q=85&s=adb0b7079fcba72618143a25d1fafdff" size={20} width="1024" height="1024" data-path="images/icons/GitHub_dark.svg" /> <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/gitlab.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=9c4f55426b9ab4cbeabe567578ad364a" size={20} width="32" height="32" data-path="images/icons/gitlab.svg" /> **Git works like it always has** — your workspace is plain files on disk. Commit your changes to Git before or after pushing to Xano for full version history, branching, and collaboration.
    </Info>
  </Step>

  <Step title="Call the modified API">
    Send a POST request to your auth/signup endpoint and review the results.

    ```bash  theme={null}
    curl -X POST "https://your-xano-instance.xano.io/api:abcD123/auth/signup" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "John Doe",
      "email": "john.doe@example.com",
      "password": "super_secure_password"
    }'
    ```

    You should receive a welcome email shortly after the request completes.
  </Step>

  <Step title="Visually validate the change in Xano">
    *This step is optional, but you can quickly see the parity between your code and the visual representation.*

    Head into Xano, and navigate to your `auth/signup` API by clicking <span class="ui-bubble">API</span> in the left-hand nav, choose the **Authentication** group, and click `auth/signup`.

    You should see the *Send Email* step at the end of the logic, right after the *Create Authentication Token* step.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-103534.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=8326b1977574207c7fc71298d4771041" alt="getting-started-code-20260112-103534" width="1428" height="434" data-path="images/getting-started-code-20260112-103534.png" />
  </Step>
</Steps>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/vscode.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=c9ca342a4c7cc10adcf78c89f822c596" size={24} width="100" height="100" data-path="images/icons/vscode.svg" /> Enhance your experience with VS Code

Claude Code is the recommended path — it has the most reliable experience with the Developer MCP today. You can enhance your Xano developer experience by utilizing VS Code and our XanoScript Language Server extension.

<Warning>
  **If you have the old XanoScript extension installed, uninstall it first.** The previous extension (publisher: Xano, name: XanoScript) conflicts with the Developer MCP. After uninstalling, delete any leftover artifact files it created (like `agents.md` or other `.md` files in your workspace root) — these can confuse AI assistants.
</Warning>

**Setup:**

1. Install the [XanoScript Language Server](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript-language-server) extension for syntax highlighting and validation.

2. Utilize Claude Code in the chat panel or via the terminal for a premium Xano development experience.

<Note>
  We're actively working on support for other development platforms, such as Cursor and Codex. Check back soon!
</Note>

***

## What's next

<CardGroup cols={2}>
  <Card title="Developer MCP" icon="plug" href="/developer-mcp/get-started">
    Explore the full set of tools and resources the Developer MCP exposes to your AI assistant.
  </Card>

  <Card title="CLI Reference" icon="terminal" href="/xano-cli/get-started">
    Learn about push, pull, branching, workflow tests, and more with the Xano CLI.
  </Card>

  <Card title="Logic & Workflows" icon="brain" href="/building/logic/logic">
    Dive deeper into the logic that powers your APIs, functions, and background tasks.
  </Card>

  <Card title="AI Agents" icon="robot" href="/ai-tools/agents">
    Build AI agents in Xano that can reason, use tools, and take actions.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).