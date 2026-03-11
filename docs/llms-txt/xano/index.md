# Source: https://docs.xano.com/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started

> Go from zero to a live backend in minutes.

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

Xano is a secure, scalable backend-as-a-service platform that gives you everything you need to build and operate your backend — without managing infrastructure. Build fast with AI, then validate and refine visually with full transparency into your core business logic.

* Build your backend with AI using built-in AI agents or code-first tools like Claude Code and Cursor
* Power your entire backend — APIs, workflows, database, runtime, CI/CD, and observability
* Maintain complete visibility into your business logic with visual validation, audit trails, and standardized architecture
* Deploy and scale on enterprise-grade infrastructure with HIPAA compliance, SOC 2 certification, GDPR readiness — without managing DevOps

***

## Build your first backend

<div className="hero-tabs">
  <Tabs>
    <Tab title="Build visually in Xano editor" icon="brush">
      This guide walks you through running a pre-built signup endpoint, inspecting the steps, and making a small modification to send a welcome email to new users. Xano gives you a `user` table and default `authentication` APIs out of the box, and we'll use those here.

      <Steps>
        <Step title="Open up your auth/signup endpoint">
          Navigate to the API section in the left-hand navigation, choose the Authentication group, and select your auth/signup endpoint.
        </Step>

        <Step title="Test the endpoint">
          Click <span class="ui-bubble">Run</span> in the top-right corner.

          Enter a name, email, and a password to create a new user. You'll use this later on, so make sure to remember the credentials you enter here. Click <span class="ui-bubble">Run</span> in the lower-right corner to execute the request.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-172818.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=9a9f5569d16d02bbbd5d2bc6953932ce" alt="getting-started-visual-20260108-172818" width="1434" height="515" data-path="images/getting-started-visual-20260108-172818.png" />

          If all goes well, you should see a successful response with an <Tooltip tip="Xano generates JWE tokens for authentication. These tokens are secure and can be used to authenticate API requests.">
          authentication token
          </Tooltip> returned.

                    <img src="https://mintcdn.com/xano-997cb9ee/Vpka8BlEU-rO5dmS/images/index-20260224-120515.png?fit=max&auto=format&n=Vpka8BlEU-rO5dmS&q=85&s=3373767290d4162312780ecaa73198ba" alt="index-20260224-120515" width="707" height="418" data-path="images/index-20260224-120515.png" />
        </Step>

        <Step title="Explore the visual builder">
          The visual builder has two different views: **Canvas** and **Stack**. Canvas presents a node-style view of the steps in your endpoint, while Stack presents a linear, step-by-step list of the same information, more similar to traditional code.

          <Frame caption="Canvas View">
                        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175031.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=29fc03a0a0e77c4b9920189c1faee9b7" alt="getting-started-visual-20260108-175031" width="1170" height="841" data-path="images/getting-started-visual-20260108-175031.png" />
          </Frame>

          <Frame caption="Stack View">
                        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175050.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=1ae673f6fbf5de9caa417527337c69bb" alt="getting-started-visual-20260108-175050" width="948" height="777" data-path="images/getting-started-visual-20260108-175050.png" />
          </Frame>

          Click on a step to see more details about what it does and how it's configured.
        </Step>

        <Step title="Modify the signup endpoint to add a welcome email">
          Let's add a step to send a welcome email after signup. We'll use the **Send Email** function for this.

          Click the <span class="ui-bubble">+ Add Step</span> button at the bottom of the stack view, or in between the Create Authentication Token step and the Response in the canvas view.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175517.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=e0400c3be1c8a6be893a127a9174496a" alt="getting-started-visual-20260108-175517" width="746" height="342" data-path="images/getting-started-visual-20260108-175517.png" />

          Select the **Send Email** function.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175545.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=f419a07ddc6f3abf5afd282c1e767e56" alt="getting-started-visual-20260108-175545" width="431" height="249" data-path="images/getting-started-visual-20260108-175545.png" />

          Add a subject and a body for the email. Xano includes free access to Resend for development and testing (up to 100 emails), limited to the email address you signed up for Xano with.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175705.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=983067965d96b790f17aa4a03b19a953" alt="getting-started-visual-20260108-175705" width="664" height="930" data-path="images/getting-started-visual-20260108-175705.png" />

          Click <span class="ui-bubble">Save</span> to save the step.
        </Step>

        <Step title="Test the modified signup endpoint">
          Run the signup endpoint again with a different email address. You should receive a welcome email shortly after the run completes.
        </Step>

        <Step title="Explore the Run panel">
          After a run, open the <span class="ui-bubble">Timing</span> dropdown to view step timing, output, inputs, and variables.

          Click the <span class="ui-bubble">></span> next to the first Get Record step. We can see the first Get Record function returned `null`, meaning that the user didn't already exist.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-180843.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=3ed640484f3aaf40a67ed7ea4e230621" alt="getting-started-visual-20260108-180843" width="653" height="312" data-path="images/getting-started-visual-20260108-180843.png" />

          <Tip>
            Try to register the same user again to see how the output changes.

                        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260109-090050.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=44509ab70e5af9b5b2ca34fb5f222e0b" alt="getting-started-visual-20260109-090050" width="665" height="560" data-path="images/getting-started-visual-20260109-090050.png" />
          </Tip>

          Expand the `input` and `vars` sections for each step to see how the data changes throughout execution.

                    <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-181247.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=0e2fdee6acc2b08756973011409b5886" alt="getting-started-visual-20260108-181247" width="623" height="620" data-path="images/getting-started-visual-20260108-181247.png" />

          <Tip>
            Xano will automatically hide information labeled as sensitive, such as password fields, in the run panel.
          </Tip>
        </Step>

        <Step title="Publish your changes and test externally">
          Click the dropdown in the upper-right corner and choose <span class="ui-bubble">Publish Now</span>. This immediately deploys your changes to the live API.

          Click <span class="ui-bubble"><Icon icon="link" /></span> to copy the endpoint URL.

          Take it over to your favorite API testing tool, like [Postman](https://www.postman.com/), [Insomnia](https://www.insomnia.rest), or [Bruno](https://www.usebruno.com). Send a `POST` request to the signup endpoint with the required parameters (name, email, password) in the body.

          You should see a successful response, just like in Xano, and have received another welcome email.
        </Step>
      </Steps>

      ### Troubleshooting

      <Accordion title="I deleted my default authentication APIs; can I get them back?">
        <Steps>
          <Step title="">
            Click <span class="ui-bubble">API</span> in the left-hand navigation.
          </Step>

          <Step title="">
            Click the <span class="ui-bubble">+ Create API</span> button in the top-right corner.
          </Step>

          <Step title="">
            Select <span class="ui-bubble">Authentication</span>
          </Step>

          <Step title="">
            Add the three default API endpoints offered: `/signup`, `/login`, and `/me`
          </Step>
        </Steps>
      </Accordion>

      <Accordion title="Common Signup Errors">
        <Danger>
          **Error Traceback (Most recent call last):**

          at `API /auth/signup(Get Record)`
          Exception: Param: field\_value - Missing param: field\_value
        </Danger>

        > The required parameters were not provided when running the endpoint -- specifically the email. Make sure to enter a name, email, and a password.

        <Danger>
          **Error Traceback (Most recent call last):**

          at `API /auth/signup(Precondition)`
          Exception: Access Denied
        </Danger>

        > The account already exists. Try using a different email address to create a new user.

        <Danger>
          **Error Traceback (Most recent call last):**

          at `API /auth/signup(Add Record)`
          Exception: Param: password - Input does not meet minimum length requirement of 8 characters
        </Danger>

        > Password inputs have some default requirements: at least 8 characters, one uppercase letter, and one number. Make sure your password meets these requirements.
      </Accordion>
    </Tab>

    <Tab title="Build with AI using CLI or IDE" icon="terminal">
      You need two things: the **Xano CLI** and **Claude Code**. The CLI syncs your code to Xano. Claude Code writes it.

      **Prerequisites:** [Node.js](https://nodejs.org/) 18+, and [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed.

      <div className="qs-step">
        <div className="qs-step-number">1</div>

        ### Install the CLI

        Install the Xano CLI globally to manage workspaces, sync code, and more from your terminal.

        ```bash  theme={null}
        npm install -g @xano/cli
        ```

        <sup><Icon icon="link" /> [CLI Documentation](xano-cli/get-started)</sup>
      </div>

      <div className="qs-step">
        <div className="qs-step-number">2</div>

        ### Create a profile

        Set up your connection to Xano with the interactive wizard. It guides you through connecting to your instance, selecting a workspace, and saving your credentials securely. If you don't have a Xano account, you'll be able to create one for free.

        ```bash  theme={null}
        xano auth
        ```

        <Tip>
          The wizard will walk you through either creating or logging into your Xano account and authenticating with the CLI.
        </Tip>
      </div>

      <div className="qs-step">
        <div className="qs-step-number">3</div>

        ### Pull your workspace

        Download your workspace to a local directory. This is where Claude Code will read and write XanoScript files.

        ```bash  theme={null}
        xano workspace pull ./my-workspace
        ```

        This creates a `my-workspace` folder in your current directory and downloads your workspace into it. You can also pull into the current folder with `xano workspace pull .`

        <Tip>
          **Starting fresh?** Create a new workspace first with `xano workspace create "my-workspace"`, then pull it.
        </Tip>
      </div>

      <div className="qs-step">
        <div className="qs-step-number">4</div>

        ### Connect the Developer MCP

        Give Claude Code access to XanoScript documentation and real-time code validation. This is what makes Claude Code actually *good* at writing XanoScript.

        ```bash  theme={null}
        claude mcp add xano -- npx -y @xano/developer-mcp
        ```
      </div>

      <div className="qs-step">
        <div className="qs-step-number">5</div>

        ### Build and push

        Open Claude Code in your workspace directory, describe what you want, and push the result to Xano.

        ```bash  theme={null}
        cd my-workspace && claude
        ```

        Ask Claude to build something — for example:

        > Create a notes table with title, content, and is\_archived fields. Then create CRUD API endpoints for notes.

        When you're done, push to Xano:

        ```bash  theme={null}
        xano workspace push ./my-workspace
        ```

        Your backend is live. Open the [Xano dashboard](https://app.xano.com) to see everything Claude built — tables, APIs, and logic — fully visible and editable in the visual builder.
      </div>

      ## <Icon icon="https://mintcdn.com/xano-997cb9ee/Vpka8BlEU-rO5dmS/images/icons/GitHub_light.png?fit=max&auto=format&n=Vpka8BlEU-rO5dmS&q=85&s=a835425bdbc8ee8a1ca4c18ea6a8d7e8" size={24} width="4096" height="4096" data-path="images/icons/GitHub_light.png" /><Icon icon="https://mintcdn.com/xano-997cb9ee/gnZk-FE3FPw_RPZv/images/icons/GitHub_dark.png?fit=max&auto=format&n=gnZk-FE3FPw_RPZv&q=85&s=8c9b58b6a842b6826535ea6d65e675cf" size={24} width="4096" height="4096" data-path="images/icons/GitHub_dark.png" /> <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/gitlab.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=9c4f55426b9ab4cbeabe567578ad364a" size={24} width="32" height="32" data-path="images/icons/gitlab.svg" /> Git works like it always has

      Your workspace is plain files on disk. `git init`, commit, branch, open PRs — everything you already do. Xano's CLI push/pull fits right into your existing Git workflow, not the other way around.

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
    </Tab>
  </Tabs>
</div>

***

## Keep going

<CardGroup cols={2}>
  <Card title="Logic & Workflows" icon="brain" href="/building/logic/logic">
    Learn more about all of the logic that can power your backend.
  </Card>

  <Card title="Database" icon="database" href="/the-database/database">
    Design, manage, and query your database.
  </Card>

  <Card title="AI Agents" icon="robot" href="/ai-tools/agents">
    Build AI agents that can reason, use tools, and take actions.
  </Card>

  <Card title="Authentication" icon="lock" href="/building-backend-features/user-authentication-and-user-data">
    Add user auth, RBAC, and OAuth/SSO to your API.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).