Source: https://docs.slack.dev/tools/slack-github-action/sending-techniques/sending-data-webhook-slack-workflow/post-release-announcements

# Example workflow: post release announcements

This workflow allows you to select a channel to post news about the most recent release to.

This example uses [Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions/) and inline inputs to do the following:

1. Open a form to select a channel.
2. Send a message to the selected channel.
3. React with a `:tada:` emoji.

## Files {#files}

### GitHub Actions workflow {#github-actions-workflow}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/announcements.gha.yml

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/announcements.gha.yml
)

#### Slack app manifest {#slack-app-manifest}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/announcements.manifest.json

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/announcements.manifest.json
)

### Slack webhook trigger {#slack-webhook-trigger}

example-workflows/Technique\_1\_Slack\_Workflow\_Builder/announcements.trigger.json

```text
loading...
```

[View on GitHub](https://github.com/slackapi/slack-github-action/blob/main/example-workflows/Technique_1_Slack_Workflow_Builder/announcements.trigger.json
)
