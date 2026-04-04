# Source: https://docs.upsun.com/learn/tutorials/dependency-updates.md

# Automate your code updates

Upsun allows you to update your dependencies through [source operations](https://docs.upsun.com/create-apps/source-operations.md).

## Before you start

You need:

- The [Upsun CLI](https://docs.upsun.com/administration/cli.md)
- An [API token](https://docs.upsun.com/administration/cli/api-tokens.md#2-create-an-api-token)

## 1. Define a source operation to update your dependencies

To facilitate updating your dependencies in your project,
define a source operation in your `.upsun/config.yaml` file
depending on your dependency manager:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            composer update
            git add composer.lock
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update Composer dependencies"            
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            npm update
            git add package.json package-lock.json
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update npm dependencies"            
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            yarn upgrade
            git add yarn.lock
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update yarn dependencies"            
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            go get -u
            go mod tidy
            git add go.mod go.sum
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update Go dependencies"            
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            pipenv update
            git add Pipfile Pipfile.lock
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update Python dependencies"            
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    source:
      operations:
        update:
          command: |
            set -e
            bundle update --all
            git add Gemfile Gemfile.lock
            git add -A
            git diff-index --quiet HEAD || git commit --allow-empty -m "Update Ruby dependencies"            
```

## 2. Automate your dependency updates with a cron job

After you've defined a source operation to [update your dependencies on your project](#1-define-a-source-operation-to-update-your-dependencies),
you can automate it using a cron job.

Note that it’s best not to run source operations on your production environment,
but rather on a dedicated environment where you can test changes.

Make sure you have the [Upsun CLI](https://docs.upsun.com/administration/cli.md) installed
and [an API token](https://docs.upsun.com/administration/cli/api-tokens.md#2-create-an-api-token)
so you can run a cron job in your app container.

1. Set your API token as a top-level environment variable:

 - Open the environment where you want to add the variable.
 - Click Settings **Settings**.
 - Click **Variables**.
 - Click **+ Add variable**.
 - In the **Variable name** field, enter ``env:UPSUN_CLI_TOKEN``.
 - In the **Value** field, enter your API token.
 - Make sure the **Available at runtime** and **Sensitive variable** options are selected.
 - Click **Add variable**.

**Note**: 

Once you add the API token as an environment variable,
anyone with [SSH access](https://docs.upsun.com/development/ssh.md) can read its value.
Make sure you carefully check your [user access on this project](https://docs.upsun.com/administration/users.md#manage-project-users).

2. Add a build hook to your app configuration to install the CLI as part of the build process:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    hooks:
      build: |
        set -e
        echo "Installing Upsun CLI"
        curl -fsSL https://raw.githubusercontent.com/platformsh/cli/main/installer.sh | bash

        echo "Testing Upsun CLI"
        upsun
```

3. Then, to configure a cron job to automatically update your dependencies once a day,
   use a configuration similar to the following:

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    # ...
    crons:
      update:
        # Run the code below every day at midnight.
        spec: '0 0 * * *'
        commands:
          start: |
            set -e
            upsun sync -e development code data --no-wait --yes
            upsun source-operation:run update --no-wait --yes
```

The example above synchronizes the `development` environment with its parent
and then runs the `update` source operation defined [previously](#1-define-a-source-operation-to-update-your-dependencies).

**Note**: 

If you have enabled a [source integration](https://docs.upsun.com/integrations/source.md), and have enabled ``--fetch-branches`` on that
integration, merging on Upsun is not possible. Therefore, the ``sync`` command in the example above would
fail.

## 3. Configure notifications about dependency updates

To get notified every time a source operation is triggered and therefore every time a dependency is updated,
you can configure activity scripts or webhooks.

### Notifications through an activity script

After you've defined a source operation to [update your dependencies on your project](#1-define-a-source-operation-to-update-your-dependencies),
you can configure an activity script
to receive notifications every time a dependency update is triggered.

**Example**: 

You want to get notified of every dependency update
through a message posted on a Slack channel.
To do so, follow these steps:

 - In your Slack administrative interface, [create a new Slack webhook](https://api.slack.com/messaging/webhooks).
You get a URL starting with ``https://hooks.slack.com/``.

 - Replace ``SLACK_URL`` in the following ``.js`` script with your webhook URL.

 - Add the following code to a ``.js`` file:

```javascript {}
/**
 * Sends a color-coded formatted message to Slack.
 *
 * To control what events trigger it, use the --events switch in
 * the Upsun CLI.
 *
 * Replace SLACK_URL in the following script with your Slack webhook URL.
 * Get one here: https://api.slack.com/messaging/webhooks
 * You should get something like: const url = 'https://hooks.slack.com/...';
 *
 * activity.text: a brief, one-line statement of what happened.
 * activity.log: the complete build and deploy log output, as it would be seen in the Console log screen.
 */
function sendSlackMessage(title, message) {
  const url = 'SLACK_URL';
  const messageTitle = title;
  const color = activity.result === "success" ? "#66c000" : "#ff0000";
  const body = {
    attachments: [
      {
        title: messageTitle,
        text: message,
        color: color,
      },
    ],
  };
  const resp = fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!resp.ok) {
    console.log("Sending slack message failed: " + resp.body.text());
  }
}
sendSlackMessage(activity.text, activity.log);
```

 - Run the following [Upsun CLI](https://docs.upsun.com/administration/cli.md) command:

```bash {}
upsun integration:add --type script --file ./my_script.js --events=environment.source-operation
```

Optional: to only get notifications about specific environments,
add the following flag to the command: ``--environments=your_environment_name``.

Anytime a dependency is updated via a source operation,
the activity script now reports it to Slack.

### Notifications through a webhook

After you've defined a source operation to [update your dependencies on your project](#1-define-a-source-operation-to-update-your-dependencies),
you can configure a webhook to receive notifications every time a dependency update is triggered.

[Webhooks](https://docs.upsun.com/integrations/activity/webhooks.md) allow you to host a script yourself externally.
This script receives the same payload as an activity script and responds to the same events,
but can be hosted on your own server and in your own language.

To configure the integration between your webhook and your source operation,
run the following [Upsun CLI](https://docs.upsun.com/administration/cli.md) command:

```bash
upsun integration:add --type=webhook --url=URL_TO_RECEIVE_JSON --events=environment.source-operation
```

Optional: to only get notifications about specific environments,
add the following flag to the command: `--environments=your_environment_name`.

To test the integration and the JSON response,
you can generate a URL from a service such as [webhook.site](https://webhook.site)
and use the generated URL as `URL_TO_RECEIVE_JSON`.
This URL then receives the JSON response when a source operation is triggered.

Anytime a dependency is updated via a source operation,
the webhook now receives a POST message.
This POST message contains complete information about the entire state of the project at that time.

