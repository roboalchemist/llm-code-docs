Source: https://docs.slack.dev/tools/slack-github-action/sending-techniques/sending-data-webhook-slack-workflow/format-generated-files

# Example workflow: format generated files

This workflow converts build outputs from earlier GitHub Action steps into a Slack message.

This example uses data from a payload file to [send a message](/tools/deno-slack-sdk/reference/slack-functions/send_message/) to a hardcoded channel.

## Files {#files}

### Payload file being sent {#payload-file-being-sent}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/builds.data.json

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/builds.data.json
)

### GitHub Actions workflow {#github-actions-workflow}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/builds.gha.yml

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/builds.gha.yml
)

### Slack app manifest {#slack-app-manifest}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/builds.manifest.json

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/builds.manifest.json
)

### Slack webhook trigger {#slack-webhook-trigger}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/builds.trigger.json

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/builds.trigger.json
)
