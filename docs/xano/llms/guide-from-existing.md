# Source: https://docs.xano.com/xano-cli/guide-from-existing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Work from Existing

> Pull down an existing Xano workspace and develop locally

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

This guide walks you through pulling an existing Xano workspace to your local machine so you can edit XanoScript locally, use AI tools, and push changes back.

## Prerequisites

* An existing Xano workspace with tables, APIs, or functions already built
* [Node.js](https://nodejs.org/) 18 or later
* A code editor (VS Code or Cursor recommended)

***

<Steps>
  <Step title="Install the Xano CLI (if needed)">
    If you haven't installed the CLI yet:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      npm install -g @xano/cli
      ```
    </BrowserFrame>

    Already have it? Make sure you're on the latest version:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano update
      ```
    </BrowserFrame>
  </Step>

  <Step title="Authenticate (if needed)">
    If you haven't set up a profile yet, authenticate with your Xano account:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano auth
      ```
    </BrowserFrame>

    Select your instance and the workspace you want to work with during the setup flow.

    <Note>
      For self-hosted or beta environments, add `-o https://your-environment-url.com`. See [Get Started](/xano-cli/get-started#other-environments) for details.
    </Note>

    If you already have a profile but need to point it to a different workspace:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano profile edit -w WORKSPACE_ID
      ```
    </BrowserFrame>
  </Step>

  <Step title="Pull your workspace">
    Download your entire workspace as XanoScript files:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace pull ./my-workspace
      ```
    </BrowserFrame>

    This creates a local directory with all of your resources organized by type:

    ```
    my-workspace/
    ├── table/
    │   ├── user.xs
    │   └── product.xs
    ├── function/
    │   └── calculate_total.xs
    ├── api/
    │   ├── user/
    │   │   ├── api_group.xs
    │   │   └── get_user_get.xs
    │   └── product/
    │       ├── api_group.xs
    │       └── list_products_get.xs
    ├── task/
    │   └── daily_cleanup.xs
    └── ...
    ```

    API endpoints are grouped under `api/{group_name}/` directories, with filenames in `{name}_{verb}.xs` format. See [Push & Pull](/xano-cli/push-pull) for the full directory structure reference.

    To include environment variables and records:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace pull ./my-workspace --env --records
      ```
    </BrowserFrame>
  </Step>

  <Step title="Install the VS Code Extension">
    For the best editing experience, install the [XanoScript VS Code Extension](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript):

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      code --install-extension xano.xanoscript
      ```
    </BrowserFrame>

    This gives you syntax highlighting, autocomplete, and inline error detection for `.xs` files.
  </Step>

  <Step title="Develop locally with AI">
    With your workspace files on disk, you can use AI tools to understand, modify, and extend your backend:

    **With the Xano MCP Server + an AI assistant (Claude, Cursor, etc.):**

    Connect your AI assistant to the [Xano MCP Server](/ai-tools/xano-mcp-server) for workspace-aware code generation. The AI can read your existing XanoScript, understand your data model, and generate new APIs, functions, or modifications that fit your existing architecture.

    **Editing directly:**

    Open the `.xs` files in your editor and make changes. The directory structure makes it easy to find what you need — tables in `table/`, APIs in `api/`, functions in `function/`, and so on.

    <Tip>
      When making significant changes, consider creating a [development branch](/xano-cli/workspaces-and-branches#create-a-branch) first so your live environment isn't affected.
    </Tip>
  </Step>

  <Step title="Push your changes">
    When you're ready to deploy your changes:

    <BrowserFrame url="Terminal">
      ```bash  theme={null}
      xano workspace push ./my-workspace
      ```
    </BrowserFrame>

    Your updated XanoScript is sent to Xano and applied to the workspace.
  </Step>

  <Step title="Verify">
    Check the [Xano dashboard](https://app.xano.com) to confirm your changes. Test your APIs, review updated functions, and validate that everything works as expected.
  </Step>
</Steps>

***

## Keeping in Sync

If you or your teammates also make changes in the Xano dashboard, pull regularly to stay up to date:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workspace pull ./my-workspace
  ```
</BrowserFrame>

A good habit is to **pull before you push** to avoid overwriting dashboard changes.

***

## Working on a Branch

For larger changes, work on a dedicated branch to avoid impacting the live environment:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  # Create a development branch
  xano branch create -l dev -s v1

  # Pull the branch
  xano workspace pull ./my-workspace -b dev

  # ... make changes ...

  # Push to the branch
  xano workspace push ./my-workspace -b dev

  # When ready, promote to live
  xano branch set_live dev
  ```
</BrowserFrame>

***

## Version Control with Git

Initialize a Git repository in your workspace directory to track changes over time:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  cd my-workspace
  git init
  git add .
  git commit -m "Pull from Xano workspace"
  ```
</BrowserFrame>

After each pull or local edit, commit to keep a clean history of what changed and when.


Built with [Mintlify](https://mintlify.com).