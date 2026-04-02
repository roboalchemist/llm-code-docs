Source: https://docs.slack.dev/tools/slack-github-action/sending-techniques/running-slack-cli-commands

# Running Slack CLI commands

The Slack CLI technique installs and runs [Slack CLI](/tools/slack-cli/) commands directly from a GitHub Actions workflow.

This is useful for automating tasks such as deploying apps, validating an app manifest, or interacting with Slack platform features that are available with the CLI.

## Setup {#setup}

### Authentication {#authentication}

Pass a [service token](/authentication/tokens/) via the `token` input. This is appended as `--token <value>` to the CLI command. The [`slack auth token`](/tools/slack-cli/reference/commands/slack_auth_token) command can be used to gather this.

### CLI version {#cli-version}

By default, the latest version of the Slack CLI is installed. To pin a specific version, use the `version` input:

```python
- uses: slackapi/slack-github-action/cli@v3.0.1  with:    command: "version"    version: "3.14.0"
```

If the `slack` command already exists on `PATH`, installation is skipped entirely.

## Usage {#usage}

Provide a `command` input with the Slack CLI command to run, omitting the `slack` prefix.

```python
- uses: slackapi/slack-github-action/cli@v3.0.1  with:    command: "version"
```

## Debug logging {#debug-logging}

When a workflow is re-run with **Enable debug logging**, the action automatically appends `--verbose` to the CLI command. You can also include `--verbose` in your `command` input manually at any time.

```python
- uses: slackapi/slack-github-action/cli@v3.0.1  with:    command: "deploy --app ${{ vars.SLACK_APP_ID }} --verbose"    token: ${{ secrets.SLACK_SERVICE_TOKEN }}
```

## Outputs {#outputs}

The following outputs are available after a CLI command runs:

Output

Type

Description

`ok`

`boolean`

If the command completed with a `0` exit code.

`response`

`string`

The standard output from the CLI command.

`time`

`number`

The Unix [epoch time](https://en.wikipedia.org/wiki/Unix_time) that the step completed.

## Examples {#examples}

### Check the installed CLI version {#check-the-installed-cli-version}

```python
steps:  - uses: slackapi/slack-github-action/cli@v3.0.1    id: slack    with:      command: "version"  - run: echo "${{ steps.slack.outputs.response }}"
```

### Validate the app manifest {#validate-the-app-manifest}

```python
steps:  - uses: actions/checkout@v4  - uses: slackapi/slack-github-action/cli@v3.0.1    with:      command: "manifest validate --app ${{ vars.SLACK_APP_ID }}"      token: ${{ secrets.SLACK_SERVICE_TOKEN }}
```

### Deploy an app with a service token {#deploy-an-app-with-a-service-token}

```python
steps:  - uses: actions/checkout@v4  - uses: slackapi/slack-github-action/cli@v3.0.1    with:      command: "deploy --app ${{ vars.SLACK_APP_ID }} --force"      token: ${{ secrets.SLACK_SERVICE_TOKEN }}
```

## Example workflows {#example-workflows}

* [**Deploy an app**](/tools/slack-github-action/sending-techniques/running-slack-cli-commands/deploy-an-app): Deploy to Slack on push to the main branch.
* [**Validate a manifest**](/tools/slack-github-action/sending-techniques/running-slack-cli-commands/validate-a-manifest): Check the app manifest on pull requests.
* [**Manage collaborators**](/tools/slack-github-action/sending-techniques/running-slack-cli-commands/manage-collaborators): Add or remove an app collaborator using CLI and API techniques together.
