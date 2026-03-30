# Source: https://docs.xano.com/xano-cli/guide-from-scratch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start from Scratch

> Build a new Xano backend from zero using the CLI and AI

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

This guide walks you through building a brand new Xano backend entirely from the command line — from initial setup to pushing your first XanoScript.

## Prerequisites

* A [Xano account](https://app.xano.com/signup) (free tier works)
* [Node.js](https://nodejs.org/) 18 or later
* A code editor (VS Code or Cursor recommended)

***

<Steps>
  <Step title="Install the Xano CLI">
    If you haven't already, install the CLI globally:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      npm install -g @xano/cli
      ```
    </BrowserFrame>

    Verify with `xano --version`.
  </Step>

  <Step title="Authenticate">
    Log in with your Xano account:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano auth
      ```
    </BrowserFrame>

    Your browser will open for authentication. After logging in, select your instance and name your profile.

    <Note>
      For self-hosted or beta environments, add `-o https://your-environment-url.com`. See [Get Started](/xano-cli/get-started#other-environments) for details.
    </Note>
  </Step>

  <Step title="Create a workspace">
    Create a new workspace for your project:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace create "My New App"
      ```
    </BrowserFrame>

    Note the workspace ID from the output, then add it to your profile:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano profile edit -w WORKSPACE_ID
      ```
    </BrowserFrame>
  </Step>

  <Step title="Set up your local project">
    Pull the empty workspace scaffold to create your local directory structure:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace pull ./my-new-app
      ```
    </BrowserFrame>

    This creates the directory structure where you'll add your XanoScript files.

    <Tip>
      Want to start with a working example instead of an empty workspace? Pull the **Hello World** sample from the [XanoScript examples repo](https://github.com/xano-inc/xanoscript-examples):

      <BrowserFrame url="Terminal">
        ```bash  theme={null}
        xano workspace git pull ./my-new-app \
          -r https://github.com/xano-inc/xanoscript-examples \
          --path helloworld
        xano workspace push ./my-new-app
        ```
      </BrowserFrame>

      This gives you tables, functions, and API endpoints to explore and build on.
    </Tip>
  </Step>

  <Step title="Install the VS Code Extension">
    For the best development experience, install the [XanoScript VS Code Extension](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript). It provides:

    * Syntax highlighting for `.xs` files
    * Autocomplete for XanoScript keywords and functions
    * Inline error detection

    Search for **XanoScript** in the VS Code extensions marketplace, or install from the command line:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      code --install-extension xano.xanoscript
      ```
    </BrowserFrame>
  </Step>

  <Step title="Build with AI">
    This is where the power of local XanoScript development shines. Use AI tools to generate your backend:

    **With the Xano MCP Server + an AI assistant (Claude, Cursor, etc.):**

    Connect your AI assistant to the [Xano MCP Server](/ai-tools/xano-mcp-server) to give it direct access to your Xano workspace context. The AI can then generate XanoScript for tables, APIs, functions, and more — all grounded in your actual workspace.

    **With any AI model directly:**

    You can also write XanoScript by hand or paste the [XanoScript documentation](/xanoscript/introduction) into your AI tool's context and ask it to generate `.xs` files. Place them in the appropriate subdirectories (`table/`, `api/`, `function/`, `task/`).

    <Tip>
      Start with your database tables first, then functions, then API endpoints. This order ensures dependencies are resolved correctly when you push.
    </Tip>
  </Step>

  <Step title="Push to Xano">
    When you're ready to deploy your backend, push everything:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace push ./my-new-app
      ```
    </BrowserFrame>

    Your tables, APIs, functions, and tasks are now live in Xano.
  </Step>

  <Step title="Verify in Xano">
    Open your workspace in the [Xano dashboard](https://app.xano.com) to see your resources. You can test APIs directly from the dashboard, view your database tables, and make visual adjustments.

    Any changes you make visually in Xano can be pulled back down:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace pull ./my-new-app
      ```
    </BrowserFrame>
  </Step>
</Steps>

***

## Recommended Workflow

Once you're up and running, a typical development cycle looks like this:

1. **Edit locally** — Write or generate XanoScript in your editor with AI assistance
2. **Push** — `xano workspace push ./my-new-app`
3. **Test** — Verify in the Xano dashboard or call your APIs
4. **Iterate** — Pull any dashboard changes, edit, and push again

<Tip>
  Use a [development branch](/xano-cli/workspaces-and-branches#create-a-branch) to keep your work separate from the live environment. When ready, [set the branch live](/xano-cli/workspaces-and-branches#set-a-branch-live).
</Tip>

***

## Version Control with Git

Track your XanoScript in Git for full change history:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  cd my-new-app
  git init
  git add .
  git commit -m "Initial backend setup"
  ```
</BrowserFrame>

This pairs well with Xano's own [branching system](/xano-cli/workspaces-and-branches) — use Git for code history and Xano branches for deployment environments.


Built with [Mintlify](https://mintlify.com).