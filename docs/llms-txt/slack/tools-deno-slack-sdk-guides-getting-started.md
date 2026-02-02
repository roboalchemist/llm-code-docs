# Getting started with the Deno Slack SDK

## Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

In the following guide, you'll install the Slack CLI and authorize it in your workspace. Then, you'll use the Slack CLI to scaffold a fully-functional workflow app and run it locally.

Don't have a workspace yet? You can get up and running by provisioning a sandbox with an associated workspace by following [this guide](/tools/developer-sandboxes/). Come on back when you're ready!

## Step 1: Install the Slack CLI

Refer to [these instructions](/tools/slack-cli/guides/installing-the-slack-cli-for-mac-and-linux) to install the latest version of the Slack CLI. The instructions will guide you through installing the Slack CLI and all required dependencies.

## Step 2: Authorize the Slack CLI

With the Slack CLI installed, authorize the Slack CLI in your workspace with the following command:

```bash
slack login
```

In your terminal window, you should see an authorization ticket in the form of a slash command, and a prompt to enter a challenge code:

```bash
$ slack login
📋 Run the following slash command in any Slack channel or DM
   This will open a modal with user permissions for you to approve
   Once approved, a challenge code will be generated in Slack
/myworkspace (Team ID: T123ABC456)
User ID: U123ABC456
Last updated: 2023-01-01 12:00:00 -07:00
Authorization Level: Workspace
```

You should see an entry for the workspace you just authorized. If you don't, get a new authorization ticket with `slack login` to try again.

## Step 3: Create an app from a template

Evaluate third-party apps and exercise caution when using third-party applications and automations (those outside of [`slack-samples`](https://github.com/slack-samples)). Review all source code created by third-parties before running `slack create` or `slack deploy`.

The `create` command is how you create a workflow app.

For this guide, we'll be creating a Slack app using the [Deno Starter Template](https://github.com/slack-samples/deno-starter-template) as a template:

```bash
slack create my-app --template https://github.com/slack-samples/deno-starter-template
```

The Slack CLI creates an app project folder and fills it with the sample app code. Once it has finished, `cd` into your new project directory:

```bash
cd my-app
```

Then continue to the next step.

## Step 4: Run the app in local development mode

While building your app, you can see your changes propagated to your workspace in real-time by running `slack run` within your app's directory.

When you execute `slack run`, you'll be asked to select a local environment:

```bash
? Choose a local environment
> Install to a new workspace or organization
```

Since you've not installed your app to any workspaces, select _Install to a new workspace_. Then select the workspace you authenticated in.

The Slack CLI will attempt to list any triggers, and in this case, will inform you there are no existing triggers installed for the app.

[Triggers](/tools/deno-slack-sdk/guides/using-triggers) are what cause workflows to run. A [link trigger](/tools/deno-slack-sdk/guides/creating-link-triggers) generates a _Shortcut URL_ which, when posted in a channel or added as a bookmark, becomes a link.

Triggers are created from trigger definition files. The Slack CLI will then look for any trigger definition files and prompt you to select one. In this case, there is only one trigger: `sample_trigger.ts`. Select it.

```bash
? Choose a trigger definition file:
> triggers/sample_trigger.ts
  Do not create a trigger
```

Once your app's trigger is created, you will see the following output:

```bash
⚡ Trigger successfully created!
  Sample trigger (local) Ft0123ABC456 (shortcut)
  Created: 2023-01-01 12:00:00 -07:00 (1 second ago)
  Collaborators:
    You! @You U123ABC456DE
  Can be found and used by:
    everyone in the workspace
  https://slack.com/shortcuts/Ft0123ABC456/XYZ123
```

The Slack CLI will also start a local development server, syncing changes to your workspace's development version of your app. You'll know your local development server is up and running when your terminal window tells you it's `Connected, awaiting events`.

## Step 5: Use your app

Grab the `Shortcut URL` you generated in the previous step and paste it in a public channel in your workspace. You will see the shortcut unfurl with a "Start Workflow" button. Click the button to execute the shortcut.

In the modal that appears, select a channel, and enter a message. When you click the "Send message" button, you should see your message appear in the channel you specified.

When you want to turn _off_ the local development server, use `Ctrl+c` in the command prompt.

---

## Onward

At this point your Slack CLI is fully authorized and ready to create new projects. It's time to choose the next path of adventure.

We have curated a collection of sample apps. Many have tutorials. All highlight features of workflow apps. Learn how to:

- design [datastores](/tools/deno-slack-sdk/guides/using-datastores) to store data with the [Virtual Running Buddies app](/tools/deno-slack-sdk/tutorials/virtual-running-buddies-app).
- send [event-triggered](/tools/deno-slack-sdk/guides/creating-event-triggers) automated [messages](/tools/deno-slack-sdk/reference/slack-functions/send_message) with the [Welcome Bot app](/tools/deno-slack-sdk/tutorials/welcome-bot).
- create [forms](/tools/deno-slack-sdk/guides/creating-a-form) to receive user input with the [Give Kudos app](/tools/deno-slack-sdk/tutorials/give-kudos-app).

Each tutorial will expose you to many aspects of the workflow automations. If you'd rather explore the documentation on your own, here are a few places to start. You can learn how to:

- [deploy your app](/tools/deno-slack-sdk/guides/deploying-to-slack) so you don't need to run it locally.
- [build an app from scratch](/tools/deno-slack-sdk/guides/creating-an-app).
- use workflow apps in conjunction with other services, whether that's with [third-party API calls](/faq#third-party) or [external authentication](/tools/deno-slack-sdk/guides/integrating-with-services-requiring-external-authentication).
- use the [Deno Slack SDK](https://github.com/slackapi/deno-slack-sdk) in tandem with the Slack CLI to access the API, additional documentation, and code libraries. You'll first need to download and install [Deno](/tools/deno-slack-sdk/guides/installing-deno). If you're using VSCode for development, make sure to also download the [Deno extension for VSCode](/tools/deno-slack-sdk/guides/installing-deno#vscode).