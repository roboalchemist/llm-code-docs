# Source: https://docs.base44.com/developers/backend/overview/start-from-existing-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start from an Existing Base44 App

> Clone a Base44 app into a separate local project with its own backend on Base44

Use the [`eject`](/developers/references/cli/commands/eject) command to clone an app you've built with the [Base44 app editor](https://base44.com) into a new Base44 project with a local codebase. The command creates a new backend on Base44 with its own app ID and downloads your code locally, giving you full control over development in your own IDE. Your original app remains in Base44 unchanged.

<Note>
  * This guide is for apps created with the Base44 app editor. To connect backend project code, such as example apps or projects shared by team members, to a Base44 backend, see [Link an Existing Backend Project](/developers/backend/overview/link-existing-project).
  * The CLI requires Node.js 20.19.0 or higher.
</Note>

<Steps>
  <Step title="Install the CLI">
    Install the Base44 CLI globally:

    ```bash  theme={null}
    npm install -g base44@latest
    ```
  </Step>

  <Step title="Eject your app">
    Run the eject command:

    ```bash  theme={null}
    base44 eject
    ```

    If you're not already logged in, the command will prompt you to authenticate.

    Select the app you want to clone, then choose a destination folder. The CLI creates a new Base44 backend project with a unique app ID and downloads your app's frontend code and backend resources locally.
  </Step>
</Steps>

When complete, you have:

* **New Base44 backend project**: A separate backend on Base44 with its own app ID and empty database.
* **Local project files**:
  * **Frontend code**: Your app's React frontend, ready to modify and build.
  * **Backend resources**: Entity schemas, functions, and configuration files in the `base44/` directory.

Your entity schemas are copied to the new project, but data is not. See [Work with data](/developers/references/sdk/getting-started/work-with-data) to add records.

For details on the generated files, see [Project Structure](/developers/backend/overview/project-structure).

## When to use eject

Use eject when you:

* Want to develop an existing app in your own IDE with full code control.
* Want to build additional clients that share your backend, such as a mobile app or Chrome extension.
* Need version control workflows beyond the [GitHub integration](/developers/app-code/local-development/github), such as feature branches or pull requests.

## Next steps

Now that you have a local project, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your frontend.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/backend-functions/overview), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Continue building your frontend and deploy updates with [`base44 deploy`](/developers/references/cli/commands/deploy).

## See also

* [`eject` command reference](/developers/references/cli/commands/eject): Export your Base44 backend configuration
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands


Built with [Mintlify](https://mintlify.com).