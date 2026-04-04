# Source: https://docs.base44.com/developers/backend/overview/link-existing-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Link an Existing Backend Project

> Set up and run existing Base44 backend project code, such as example apps

import { Tree } from "@mintlify/components";

You can link existing Base44 backend project code, such as from an [example app](https://github.com/base44/apps-examples), to a backend on Base44. Use this when you already have Base44 backend project files locally.

If you don't have any project files yet, use [`base44 create`](/developers/references/cli/commands/create) to generate a new project instead.

<Note>
  * This guide is for linking existing Base44 backend project code, such as example apps or projects shared by team members. If you created an app with the [Base44 app editor](https://base44.com) and want to develop it locally, use [`base44 eject`](/developers/backend/overview/start-from-existing-app) instead.
  * The CLI requires Node.js 20.19.0 or higher.
</Note>

## Understanding local code vs. backend projects

When working with Base44, there are two separate components:

* **Local code:** The project files on your computer, such as your frontend code, entity schemas and backend functions.
* **Base44 backend project:** The backend infrastructure on Base44's servers, including the database, endpoints, hosting, and so on.

Linking connects your local code to a backend project so your app can use Base44's infrastructure. During the linking process, you'll choose one of two options:

* **Create a new project:** Creates a fresh backend on Base44 for your code. Choose this if you're setting up this code for the first time.
* **Link to existing:** Connects to a backend that already exists on Base44. Choose this if you're reconnecting to a backend you set up earlier, or if you're joining a team project where the backend has already been created.

## Link a project

<Steps>
  <Step title="Get the project code">
    Clone an example app or download existing project code, then navigate to the project directory.

    The project should already contain a `base44/` folder with a `config.jsonc` file.
  </Step>

  <Step title="Install dependencies">
    Install the project dependencies:

    ```bash  theme={null}
    npm install
    ```
  </Step>

  <Step title="Install the Base44 CLI">
    Install the Base44 CLI globally:

    ```bash  theme={null}
    npm install -g base44@latest
    ```
  </Step>

  <Step title="Authenticate">
    Log in to your Base44 account:

    ```bash  theme={null}
    base44 login
    ```

    The CLI generates a device code. Open the provided URL, enter the code, and complete authentication in your browser.
  </Step>

  <Step title="Link the project">
    Link your local project to a Base44 backend:

    ```bash  theme={null}
    base44 link
    ```

    The CLI will prompt you to either create a new backend project or link to an existing one. This creates an `.app.jsonc` file in your `base44/` directory with your app ID:

    ```jsonc  theme={null}
    {
      "id": "your-app-id"
    }
    ```

    <Warning>
      The `.app.jsonc` file should never be committed to version control. It's automatically added to `.gitignore` and is specific to each developer and deployment environment.
    </Warning>
  </Step>

  <Step title="Set up environment variables (if needed)">
    Your app ID is required when configuring an SDK client. Projects typically store their app ID in an environment variable and retrieve it to create a client. Check the project's documentation or configuration files for instructions on setting the required environment variables.
  </Step>

  <Step title="Build the frontend if the project has one">
    If your project includes a frontend, build it so it's ready to deploy in the next step.
  </Step>

  <Step title="Push resources">
    Sync your project's resources to your Base44 backend:

    ```bash  theme={null}
    base44 deploy
    ```

    This pushes entities, functions, and the site if your project has one.

    If your project has agents, push them as well:

    ```bash  theme={null}
    base44 agents push
    ```
  </Step>
</Steps>

## Next steps

Now that your project is set up and running, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your frontend, if the project has one.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/backend-functions/overview), and [agents](/developers/backend/resources/agents-config).
* Continue building and deploy updates with [`base44 deploy`](/developers/references/cli/commands/deploy).

## See also

* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [JavaScript SDK Documentation](/developers/references/sdk/getting-started/overview): Connect your app to the backend
* [Base44 Skills](/developers/backend/overview/base44-skills): Teach AI assistants to work with Base44
* [Example apps repository](https://github.com/base44/apps-examples): Sample projects to learn from


Built with [Mintlify](https://mintlify.com).