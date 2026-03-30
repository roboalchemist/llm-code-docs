# Source: https://docs.xano.com/getting-started-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building with the VS Code Extension

> A guide to setting up VS Code for Xano development, editing endpoints in XanoScript, and syncing changes.

<Info>
  **Using Claude Code?** You don't need VS Code at all. Install the [Developer MCP](/developer-mcp/get-started) and use the [Xano CLI](/xano-cli/get-started) to pull, edit, and push — no extension required.
</Info>

This guide walks you through setting up VS Code for Xano development — connecting your workspace, configuring your AI assistant, editing an endpoint, and syncing changes back to Xano.

<Steps>
  <Step title="Set up your editor">
    Install the [XanoScript extension for VS Code](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript). This provides syntax highlighting, real-time validation, code completion, and a built-in connection manager for syncing with your Xano workspace.

    <Tip>
      **Using Cursor, Windsurf, or another .vsix-compatible IDE?** Download the extension from the [Open VSX Registry](https://open-vsx.org/extension/xano/xanoscript) and follow your IDE's instructions for installing .vsix files.
    </Tip>

    <Info>
      **Using the Developer MCP?** Install the [XanoScript Language Server](https://marketplace.visualstudio.com/items?itemName=xano.xanoscript-language-server) instead. It provides syntax highlighting and validation without conflicting with the MCP. The full extension above should not be installed alongside the Developer MCP.
    </Info>
  </Step>

  <Step title="Configure your AI assistant">
    The XanoScript extension works with multiple AI coding tools. Choose the setup that matches your workflow.

    <Tabs>
      <Tab title="GitHub Copilot">
        <Tip>
          Make sure you have **GitHub Copilot Pro or higher** enabled in VS Code. For the best results generating XanoScript, use:

          * GPT 5 or higher
          * Sonnet 4.5, or Opus
        </Tip>

        No additional installation is needed — you'll generate AI Agent Instructions when you connect to Xano in the next step. These files help Copilot understand your workspace structure and XanoScript conventions.
      </Tab>

      <Tab title="Claude Code / MCP-compatible tools">
        Install the [Developer MCP](/developer-mcp/get-started) to give your AI coding tools direct access to XanoScript documentation and real-time code validation. This significantly improves the quality of AI-generated XanoScript.

        Quick install for Claude Code:

        ```bash  theme={null}
        claude mcp add xano -- npx -y @xano/developer-mcp
        ```

        The Developer MCP replaces the need for AI Agent Instructions — it provides XanoScript context to your AI tools directly.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Connect to Xano">
    *Make sure you have the folder you want to work in open before continuing.*

    <Info>
      **Using the XanoScript Language Server + CLI?** Run `xano auth` to authenticate, then `xano workspace pull ./my-workspace` to pull your workspace. See the [CLI Get Started](/xano-cli/get-started) guide for details, and skip ahead to the next step.
    </Info>

    <Steps>
      <Step title="Click the Xano logo in the left sidebar and choose Get Started">
                <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-095637.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=701e1ae17f11ba2deb25ebec9fc23fcb" alt="getting-started-code-20260112-095637" width="897" height="740" data-path="images/getting-started-code-20260112-095637.png" />
      </Step>

      <Step title="Login to Xano">
        Click *Login to Xano* to authenticate with your Xano account and follow the instructions.

                <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-095955.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=0900ffc17eb8884ae0bafdf88ae6616b" alt="getting-started-code-20260112-095955" width="756" height="172" data-path="images/getting-started-code-20260112-095955.png" />
      </Step>

      <Step title="Pull changes from Xano into your IDE">
        Select your instance from the dropdown that appears, and then select your workspace and your live branch.

        After selection, click *Pull Changes* to get everything that's currently present in your Xano workspace.

                <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-100203.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=8c24043852e9f6528c10ff0f0319ce49" alt="getting-started-code-20260112-100203" width="324" height="216" data-path="images/getting-started-code-20260112-100203.png" />
      </Step>

      <Step title="Generate AI Agent Instructions (Copilot users)">
        **If you're using GitHub Copilot**, select *Setup AI Agent Instructions* to generate context files for your workspace. These help Copilot understand your workspace structure and XanoScript conventions. It is highly recommended to generate these for the best possible experience.

        <Info>
          **Using the Developer MCP?** Skip this step — the MCP provides XanoScript context to your AI tools directly.
        </Info>
      </Step>
    </Steps>
  </Step>

  <Step title="Understand where things live">
    Xano repos follow a very simple structure. Each primitive lives in its folder, with logic stored inside `.xs` files.

    **Repository Layout**

    ```bash  theme={null}
    api/
        authentication/
          api_group.xs
          000_auth_signup_post.xs
          000_auth_login_post.xs
          000_auth_me_get.xs

    table/
        000_user.xs
    ```

    You'll see other folders for things like functions, AI Agents, and more -- for this quick start, we're just looking at APIs and tables.
  </Step>

  <Step title="Open the Signup endpoint and make a change">
    Navigate to `api/authentication/000_auth_signup_post.xs`

    Add a new function below `security.create_auth_token`. Order matters — this ensures the email is sent only after signup succeeds. This is our `send_email` function; just copy and paste the code below.

    ```
    util.send_email {
      service_provider = "xano"
      subject = "Welcome!"
      message = "Thanks for checking out Xano. We're so glad you're here."
    } as $x1
    ```

    This is what you should be seeing now:

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-101408.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=9b297793ee0a1b772219f289492d75b9" alt="getting-started-code-20260112-101408" width="1534" height="836" data-path="images/getting-started-code-20260112-101408.png" />
  </Step>

  <Step title="Save and sync to Xano">
    Save your changes, and then click the option in the XanoScript extension to stage your changes.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-101847.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=f7a4754ba23827efb93261684ab90f12" alt="getting-started-code-20260112-101847" width="807" height="333" data-path="images/getting-started-code-20260112-101847.png" />

    Push your changes to Xano. Progress is shown in a notification in the bottom-right corner.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-code-20260112-101647.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=7a55848d916ed2a0a7f01b7b4965ba8d" alt="getting-started-code-20260112-101647" width="622" height="149" data-path="images/getting-started-code-20260112-101647.png" />

    <Tip>
      Prefer the terminal? You can also use `xano workspace push` and `xano workspace pull` via the [Xano CLI](/xano-cli/get-started) instead of the extension's UI.
    </Tip>

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


Built with [Mintlify](https://mintlify.com).